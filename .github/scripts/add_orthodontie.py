from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# 1) Add orthodontics to the visible services carousel, after parodontology.
anchor = '''          <article class="soin-card">
            <span class="soin-num">06</span>
            <span class="soin-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c-1.7 0-2.3.6-3.5.6-1.4 0-2.6.9-2.6 2.9 0 1.8.5 2.8.9 4.2.3 1.2.4 2.7.6 3.9M12 2.5c1.7 0 2.3.6 3.5.6 1.4 0 2.6.9 2.6 2.9 0 1.8-.5 2.8-.9 4.2-.3 1.2-.4 2.7-.6 3.9"/><path d="M3.5 16.6c2.7 1.9 5.5 2.8 8.5 2.8s5.8-.9 8.5-2.8"/></svg></span>
            <h3>Parodontologie et soins des gencives</h3>
            <p>Gencives qui saignent ou se rétractent : on traite le tissu qui tient vos dents en place.</p>
          </article>'''

ortho_card = anchor + '''
          <article class="soin-card">
            <span class="soin-num">07</span>
            <span class="soin-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5.5c1.7-1 3.7-1.5 6-1.5s4.3.5 6 1.5"/><path d="M5.5 9.2c1.8.9 4 1.3 6.5 1.3s4.7-.4 6.5-1.3"/><path d="M6 13h12"/><rect x="6.2" y="11.4" width="2.6" height="3.2" rx=".6"/><rect x="10.7" y="11.4" width="2.6" height="3.2" rx=".6"/><rect x="15.2" y="11.4" width="2.6" height="3.2" rx=".6"/><path d="M7.5 15.5c.5 2.8 2 4.5 4.5 4.5s4-1.7 4.5-4.5"/></svg></span>
            <h3>Orthodontie et alignement dentaire</h3>
            <p>Correction de l’alignement des dents et des malocclusions, avec un suivi adapté à chaque patient.</p>
          </article>'''

if 'Orthodontie et alignement dentaire' not in s:
    if anchor not in s:
        raise SystemExit('Visible parodontology card anchor not found')
    s = s.replace(anchor, ortho_card, 1)

# 2) Keep the structured data consistent with the visible services.
schema_old = '''      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Endodontie et traitement de canal"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Parodontologie et soins des gencives"}}'''
schema_new = '''      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Endodontie et traitement de canal"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Parodontologie et soins des gencives"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Orthodontie et alignement dentaire"}}'''
if '"name": "Orthodontie et alignement dentaire"' not in s:
    if schema_old not in s:
        raise SystemExit('Schema services anchor not found')
    s = s.replace(schema_old, schema_new, 1)

# 3) Add orthodontics to the footer services list.
footer_old = '''          <a href="#soins">Endodontie</a>
          <a href="#soins">Parodontologie</a>'''
footer_new = '''          <a href="#soins">Endodontie</a>
          <a href="#soins">Parodontologie</a>
          <a href="#soins">Orthodontie</a>'''
if '<a href="#soins">Orthodontie</a>' not in s:
    if footer_old not in s:
        raise SystemExit('Footer services anchor not found')
    s = s.replace(footer_old, footer_new, 1)

# 4) Mention orthodontics in the schema description as well.
s = s.replace(
    'Cabinet dentaire à Tanger proposant des soins dentaires généraux, chirurgie dentaire, dentisterie esthétique, implantologie, endodontie et parodontologie.',
    'Cabinet dentaire à Tanger proposant des soins dentaires généraux, chirurgie dentaire, dentisterie esthétique, implantologie, endodontie, parodontologie et orthodontie.',
    1
)

path.write_text(s, encoding='utf-8')
