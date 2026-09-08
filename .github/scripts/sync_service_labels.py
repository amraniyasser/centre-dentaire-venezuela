from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

replacements = {
    '<a href="#soins">Soins généraux</a>': '<a href="#soins">Soins dentaires généraux</a>',
    '<a href="#soins">Chirurgie</a>': '<a href="#soins">Chirurgie dentaire</a>',
    '<a href="#soins">Esthétique</a>': '<a href="#soins">Dentisterie esthétique</a>',
    '<option>Soins généraux, contrôle ou détartrage</option>': '<option>Soins dentaires généraux</option>',
    '<option>Chirurgie</option>': '<option>Chirurgie dentaire</option>',
    '<option>Esthétique</option>': '<option>Dentisterie esthétique</option>',
}

for old, new in replacements.items():
    if old not in s:
        raise SystemExit(f'Expected label not found: {old}')
    s = s.replace(old, new, 1)

if '<option>Orthodontie</option>' not in s:
    anchor = '<option>Parodontologie</option>\n                    <option>Urgence</option>'
    replacement = '<option>Parodontologie</option>\n                    <option>Orthodontie</option>\n                    <option>Urgence</option>'
    if anchor not in s:
        raise SystemExit('Motif dropdown anchor not found')
    s = s.replace(anchor, replacement, 1)

path.write_text(s, encoding='utf-8')
