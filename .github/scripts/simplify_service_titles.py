from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

replacements = {
    '<h3>Soins dentaires généraux et détartrage</h3>': '<h3>Soins dentaires généraux</h3>',
    '<h3>Chirurgie dentaire et extractions</h3>': '<h3>Chirurgie dentaire</h3>',
    '<h3>Dentisterie esthétique : blanchiment et facettes</h3>': '<h3>Dentisterie esthétique</h3>',
    '<h3>Implants dentaires et implantologie</h3>': '<h3>Implantologie</h3>',
    '<h3>Endodontie et traitement de canal</h3>': '<h3>Endodontie</h3>',
    '<h3>Parodontologie et soins des gencives</h3>': '<h3>Parodontologie</h3>',
    '<h3>Orthodontie et alignement dentaire</h3>': '<h3>Orthodontie</h3>',
}

for old, new in replacements.items():
    if old not in s:
        raise SystemExit(f'Expected service title not found: {old}')
    s = s.replace(old, new, 1)

path.write_text(s, encoding='utf-8')
