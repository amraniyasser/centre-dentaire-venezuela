from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

form_pattern = re.compile(
    r'<form name="rendez-vous" method="POST" action="/merci" data-netlify="true" data-netlify-honeypot="bot-field">\s*'
    r'<input type="hidden" name="form-name" value="rendez-vous">\s*'
    r'<p class="honeypot" aria-hidden="true">.*?</p>',
    re.S,
)
s, count = form_pattern.subn('<form id="rdv-form" name="rendez-vous">', s, count=1)
if count != 1:
    raise SystemExit('Could not find the Netlify form block exactly once')

s = s.replace(
    '''          <!-- Netlify Forms : data-netlify déclare le formulaire au déploiement, le champ
               caché form-name identifie l'envoi, et bot-field est le piège à robots.
               Ces trois éléments ne fonctionnent que sur un hébergement Netlify. -->\n''',
    '''          <!-- Le formulaire reste entièrement local : au clic, le JavaScript construit
               le message puis ouvre WhatsApp avec les informations préremplies. -->\n''',
    1,
)

s = s.replace(
    '''                <b>Vos données restent confidentielles</b>
                <p>Les informations transmises servent uniquement à traiter votre demande de rendez-vous. Elles ne sont ni revendues ni partagées.</p>''',
    '''                <b>Vos données restent confidentielles</b>
                <p>Les informations saisies servent uniquement à préparer votre message WhatsApp vers le cabinet. Aucun formulaire n’est stocké par ce site.</p>''',
    1,
)

marker = '''/* Comparateurs avant / après : glisser à la souris et au doigt, clic direct,
   et flèches du clavier via l'input range invisible. */'''
if marker not in s:
    raise SystemExit('Could not find JavaScript insertion marker')

whatsapp_js = r'''/* Formulaire de rendez-vous : construit un message WhatsApp à partir des
   informations saisies, puis ouvre WhatsApp avec le message prérempli. */
(function () {
  var form = document.getElementById('rdv-form');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;

    var nom = document.getElementById('rdv-nom').value.trim();
    var motif = document.getElementById('rdv-motif').value;
    var telephone = document.getElementById('rdv-tel').value.trim();
    var creneau = document.getElementById('rdv-creneau').value || 'Indifférent';
    var messageLibre = document.getElementById('rdv-message').value.trim();

    var lignes = [
      'Bonjour, je souhaite prendre rendez-vous au Centre Dentaire Venezuela.',
      '',
      'Nom : ' + nom,
      'Motif : ' + motif,
      'Téléphone : ' + telephone,
      'Créneau préféré : ' + creneau
    ];

    if (messageLibre) lignes.push('Message : ' + messageLibre);

    var whatsappUrl = 'https://wa.me/212771158018?text=' + encodeURIComponent(lignes.join('\n'));
    var nouvelleFenetre = window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    if (!nouvelleFenetre) window.location.href = whatsappUrl;
  });
})();

'''

s = s.replace(marker, whatsapp_js + marker, 1)
path.write_text(s, encoding='utf-8')
