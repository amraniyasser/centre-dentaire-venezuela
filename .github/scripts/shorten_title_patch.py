from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_title = '<title>Dentiste à Tanger | Centre Dentaire Venezuela – Dr Majda Laasraoui</title>'
new_title = '<title>Dentiste à Tanger | Centre Dentaire Venezuela</title>'
old_og = '<meta property="og:title" content="Dentiste à Tanger | Centre Dentaire Venezuela – Dr Majda Laasraoui">'
new_og = '<meta property="og:title" content="Dentiste à Tanger | Centre Dentaire Venezuela">'

if old_title not in s:
    raise SystemExit('Expected title not found')
s = s.replace(old_title, new_title, 1)

if old_og in s:
    s = s.replace(old_og, new_og, 1)

path.write_text(s, encoding='utf-8')
