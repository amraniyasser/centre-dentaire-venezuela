from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_lead = "<p class=\"section-lead\">Au cœur de Tanger, le Centre Dentaire Venezuela associe un plateau technique complet à une prise en charge attentive. Dr Majda Laasraoui y reçoit chaque patient dans un cadre calme et lumineux, avec le temps nécessaire pour expliquer, rassurer et soigner.</p>"
new_lead = "<p class=\"section-lead\">Au cœur de Tanger, le Centre Dentaire Venezuela accueille chaque patient dans un cadre calme et lumineux. L’équipe prend le temps d’expliquer chaque étape, de répondre aux questions et d’adapter la prise en charge aux besoins de chacun.</p>"
if old_lead not in s:
    raise SystemExit('Cabinet intro paragraph not found')
s = s.replace(old_lead, new_lead, 1)

contact_html = '''      <aside class="cabinet-contact" aria-label="Coordonnées du Centre Dentaire Venezuela">
        <span class="cabinet-contact-kicker">Nous trouver &amp; nous contacter</span>

        <div class="cabinet-address">
          <span class="cabinet-contact-icon">
            <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-pin"/></svg>
          </span>
          <div>
            <b>Centre Dentaire Venezuela</b>
            <span>4ème étage n°74, Immeuble Venezuela<br>89 Rue Moussa Ben Noussair<br>Tanger 90000, Maroc</span>
            <a class="cabinet-map-link" href="https://share.google/NQdfjEYv9MC4431Lz" target="_blank" rel="noopener">Voir sur Google Maps <span aria-hidden="true">→</span></a>
          </div>
        </div>

        <div class="cabinet-contact-list">
          <a class="cabinet-contact-row" href="tel:+212531112127" aria-label="Appeler le Centre Dentaire Venezuela au +212 5 31 11 21 27">
            <span class="cabinet-contact-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-phone"/></svg></span>
            <span class="cabinet-contact-copy"><small>Téléphone</small><b>+212 5 31 11 21 27</b></span>
            <span class="cabinet-contact-arrow" aria-hidden="true">↗</span>
          </a>

          <a class="cabinet-contact-row" href="https://wa.me/212771158018" target="_blank" rel="noopener" aria-label="Ouvrir une conversation WhatsApp avec le Centre Dentaire Venezuela">
            <span class="cabinet-contact-icon">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 11.8a8.5 8.5 0 0 1-12.6 7.4L3 20.5l1.3-4.7A8.5 8.5 0 1 1 20.5 11.8Z"/><path d="M8.1 7.7c.2-.4.4-.4.7-.4h.5c.2 0 .4 0 .5.4l.7 1.7c.1.3.1.5-.1.7l-.6.7c-.2.2-.2.4-.1.6.6 1.2 1.6 2.2 2.8 2.8.2.1.4.1.6-.1l.8-.9c.2-.2.4-.3.7-.2l1.7.8c.3.1.4.3.4.5 0 .3-.1 1.3-.6 1.8-.5.5-1.4.8-2.2.8-.6 0-1.4-.2-2.4-.6-1-.4-4.2-1.6-5.7-5.4-.4-.9-.4-1.6-.4-2.1 0-.5.2-.9.4-1.1Z"/></svg>
            </span>
            <span class="cabinet-contact-copy"><small>WhatsApp</small><b>+212 771 158 018</b></span>
            <span class="cabinet-contact-arrow" aria-hidden="true">↗</span>
          </a>

          <a class="cabinet-contact-row" href="mailto:centredentairevenezuela@gmail.com" aria-label="Envoyer un email au Centre Dentaire Venezuela">
            <span class="cabinet-contact-icon">
              <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/></svg>
            </span>
            <span class="cabinet-contact-copy"><small>Email</small><b>centredentairevenezuela@gmail.com</b></span>
            <span class="cabinet-contact-arrow" aria-hidden="true">↗</span>
          </a>

          <a class="cabinet-contact-row" href="https://www.instagram.com/centre.dentaire.venezuela/" target="_blank" rel="noopener" aria-label="Instagram du Centre Dentaire Venezuela">
            <span class="cabinet-contact-icon">
              <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg>
            </span>
            <span class="cabinet-contact-copy"><small>Instagram</small><b>@centre.dentaire.venezuela</b></span>
            <span class="cabinet-contact-arrow" aria-hidden="true">↗</span>
          </a>
        </div>
      </aside>'''

pattern = re.compile(r'      <ul class="perks">.*?      </ul>', re.S)
match = pattern.search(s)
if not match:
    raise SystemExit('Cabinet perks block not found')
s = s[:match.start()] + contact_html + s[match.end():]

# Add email to local-business structured data if not already present.
if '"email": "centredentairevenezuela@gmail.com"' not in s:
    needle = '  "telephone": "+212531112127",\n'
    if needle not in s:
        raise SystemExit('Schema telephone anchor not found')
    s = s.replace(needle, needle + '  "email": "centredentairevenezuela@gmail.com",\n', 1)

css = r'''

/* ==========================================================================
   Le cabinet — coordonnées concrètes à la place des anciens blocs techniques
   ========================================================================== */
.cabinet-grid{
  grid-template-columns:minmax(0,.95fr) minmax(0,1.45fr) minmax(290px,.9fr);
  align-items:center;
}
.cabinet-contact{
  align-self:stretch;
  display:flex;
  flex-direction:column;
  justify-content:center;
  padding:24px;
  border-radius:22px;
  background:var(--white);
  border:1px solid rgba(20,59,62,.09);
  box-shadow:0 14px 34px rgba(14,47,49,.08);
}
.cabinet-contact-kicker{
  display:block;
  margin-bottom:18px;
  font-size:10.5px;
  font-weight:700;
  letter-spacing:.17em;
  text-transform:uppercase;
  color:var(--teal-soft);
}
.cabinet-address{
  display:flex;
  align-items:flex-start;
  gap:13px;
  padding-bottom:18px;
  margin-bottom:8px;
  border-bottom:1px solid rgba(20,59,62,.09);
}
.cabinet-address > div{min-width:0}
.cabinet-address b{
  display:block;
  margin-bottom:5px;
  font-size:14px;
  font-weight:600;
  color:var(--ink);
}
.cabinet-address > div > span{
  display:block;
  font-size:12.5px;
  line-height:1.55;
  color:#6f8c8b;
}
.cabinet-map-link{
  display:inline-flex;
  align-items:center;
  gap:6px;
  margin-top:9px;
  font-size:12.5px;
  font-weight:600;
  color:var(--teal-deep);
}
.cabinet-map-link > span{color:var(--gold)}
.cabinet-map-link:hover{text-decoration:underline}
.cabinet-contact-list{display:flex;flex-direction:column}
.cabinet-contact-row{
  display:grid;
  grid-template-columns:40px minmax(0,1fr) auto;
  align-items:center;
  gap:12px;
  padding:11px 0;
  border-bottom:1px solid rgba(20,59,62,.07);
  transition:transform .2s,color .2s;
}
.cabinet-contact-row:last-child{border-bottom:0;padding-bottom:0}
.cabinet-contact-row:hover{transform:translateX(3px)}
.cabinet-contact-icon{
  display:grid;
  place-items:center;
  width:40px;
  height:40px;
  border-radius:12px;
  background:#eef5f4;
  color:var(--teal-deep);
}
.cabinet-contact-icon svg{
  width:19px;
  height:19px;
  stroke:currentColor;
  fill:none;
  stroke-width:1.6;
  stroke-linecap:round;
  stroke-linejoin:round;
}
.cabinet-contact-copy{min-width:0}
.cabinet-contact-copy small{
  display:block;
  margin-bottom:2px;
  font-size:10.5px;
  color:#8aa4a1;
}
.cabinet-contact-copy b{
  display:block;
  overflow-wrap:anywhere;
  font-size:12.5px;
  font-weight:600;
  line-height:1.35;
  color:var(--ink);
}
.cabinet-contact-arrow{
  font-size:15px;
  color:var(--gold);
}

@media(max-width:1100px){
  .cabinet-grid{
    grid-template-columns:minmax(0,.9fr) minmax(0,1.25fr);
    align-items:center;
  }
  .cabinet-contact{
    grid-column:1 / -1;
    display:grid;
    grid-template-columns:minmax(230px,.8fr) minmax(0,1.2fr);
    gap:0 26px;
  }
  .cabinet-contact-kicker{grid-column:1/-1}
  .cabinet-address{margin:0;padding:0 24px 0 0;border-bottom:0;border-right:1px solid rgba(20,59,62,.09)}
  .cabinet-contact-list{padding-left:0}
}

@media(max-width:900px){
  .cabinet-grid{grid-template-columns:1fr;align-items:start}
  .cabinet-contact{grid-column:auto;display:flex}
  .cabinet-address{margin-bottom:8px;padding:0 0 18px;border-right:0;border-bottom:1px solid rgba(20,59,62,.09)}
}

@media(max-width:720px){
  .cabinet-contact{padding:20px;border-radius:20px}
  .cabinet-contact-row{padding:10px 0}
  .cabinet-contact-copy b{font-size:12px}
}
'''

if css.strip() not in s:
    marker = '</style>'
    idx = s.find(marker)
    if idx == -1:
        raise SystemExit('Style closing tag not found')
    s = s[:idx] + css + '\n' + s[idx:]

path.write_text(s, encoding='utf-8')
