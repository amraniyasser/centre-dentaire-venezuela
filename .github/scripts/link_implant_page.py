from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_card = '''            <h3>Implantologie</h3>
            <p>Une dent absente remplacée par une racine artificielle, fixe, qui se comporte comme la vôtre.</p>'''
new_card = '''            <h3>Implantologie</h3>
            <p>Une dent absente remplacée par une racine artificielle, fixe, qui se comporte comme la vôtre.</p>
            <a class="soin-more" href="/implant-dentaire-tanger/" aria-label="Découvrir notre page Implant dentaire à Tanger">Découvrir le traitement <span aria-hidden="true">→</span></a>'''
if old_card not in s:
    raise SystemExit('Implant card anchor not found')
s = s.replace(old_card, new_card, 1)

old_footer = '<a href="#soins">Implantologie</a>'
new_footer = '<a href="/implant-dentaire-tanger/">Implantologie</a>'
if old_footer not in s:
    raise SystemExit('Implant footer link not found')
s = s.replace(old_footer, new_footer, 1)

old_schema = '{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Implants dentaires et implantologie"}},'
new_schema = '{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Implants dentaires et implantologie", "url": "https://centredentairevenezuela.com/implant-dentaire-tanger/"}},'
if old_schema in s:
    s = s.replace(old_schema, new_schema, 1)

css = '''\n/* Lien vers la page dédiée Implantologie */\n.soin-more{display:inline-flex;align-items:center;gap:6px;margin-top:14px;font-size:11.5px;font-weight:700;color:var(--teal-deep);text-decoration:none}\n.soin-more span{color:var(--gold);transition:transform .2s}\n.soin-more:hover span{transform:translateX(3px)}\n'''
if css.strip() not in s:
    marker = '</style>'
    idx = s.find(marker)
    if idx == -1:
        raise SystemExit('Closing style tag not found')
    s = s[:idx] + css + '\n' + s[idx:]

path.write_text(s, encoding='utf-8')
