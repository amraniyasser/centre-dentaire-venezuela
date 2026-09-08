from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old = "<p>Appareils orthodontiques classiques et aligneurs invisibles pour corriger l’alignement des dents et les malocclusions.</p>"
new = "<p>Traitements multi-bagues et aligneurs invisibles pour corriger l’alignement des dents et les malocclusions.</p>"

if old not in s:
    raise SystemExit('Current orthodontics description not found')

s = s.replace(old, new, 1)
path.write_text(s, encoding='utf-8')
