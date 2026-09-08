from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old = "<p>Correction de l’alignement des dents et des malocclusions, avec un suivi adapté à chaque patient.</p>"
new = "<p>Appareils orthodontiques classiques et aligneurs invisibles pour corriger l’alignement des dents et les malocclusions.</p>"

if old not in s:
    raise SystemExit('Orthodontics description not found')

s = s.replace(old, new, 1)
path.write_text(s, encoding='utf-8')
