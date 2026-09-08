from pathlib import Path

changes = {
    'endodontie-tanger/index.html': (
        'Endodontie à Tanger | Traitement de canal | Centre Dentaire Venezuela',
        'Endodontie à Tanger | Traitement de canal'
    ),
    'orthodontie-tanger/index.html': (
        'Orthodontie à Tanger | Bagues & aligneurs invisibles | Centre Dentaire Venezuela',
        'Orthodontie à Tanger | Bagues & aligneurs invisibles'
    ),
    'parodontologie-tanger/index.html': (
        'Parodontologie à Tanger | Soins des gencives | Centre Dentaire Venezuela',
        'Parodontologie à Tanger | Soins des gencives'
    ),
}

for filename, (old, new) in changes.items():
    path = Path(filename)
    s = path.read_text(encoding='utf-8')
    if old not in s:
        raise SystemExit(f'Expected title not found in {filename}')
    # This replaces both <title> and og:title because both contain the same exact string.
    s = s.replace(old, new)
    path.write_text(s, encoding='utf-8')
    print(filename, len(new), new)
