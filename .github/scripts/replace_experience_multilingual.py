from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_main = '<div><b>8 ans</b><span>d’expérience</span></div>'
new_main = '<div><b>Multilingue</b><span>Français · Arabe · Anglais · Espagnol</span></div>'
if old_main not in s:
    raise SystemExit('Hero experience block not found')
s = s.replace(old_main, new_main, 1)

old_ribbon = '<span class="ribbon-item"><b>8 ans</b> d’expérience</span>'
new_ribbon = '<span class="ribbon-item"><b>Multilingue</b> Français · Arabe · Anglais · Espagnol</span>'
count = s.count(old_ribbon)
if count < 2:
    raise SystemExit(f'Expected 2 mobile ribbon experience items, found {count}')
s = s.replace(old_ribbon, new_ribbon)

path.write_text(s, encoding='utf-8')
