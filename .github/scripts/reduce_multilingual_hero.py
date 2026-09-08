from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old = '<div><b>Multilingue</b><span>Français · Arabe · Anglais · Espagnol</span></div>'
new = '<div class="proof-multilingual"><b>Multilingue</b><span>Français · Arabe · Anglais · Espagnol</span></div>'
if old not in s:
    raise SystemExit('Multilingual hero block not found')
s = s.replace(old, new, 1)

css = '''\n/* Ajustement du bloc multilingue dans la preuve du hero */\n.proof-multilingual b{font-size:12.5px;line-height:1.05}\n.proof-multilingual span{font-size:9.5px;line-height:1.15}\n'''
if css.strip() not in s:
    marker = '</style>'
    idx = s.find(marker)
    if idx == -1:
        raise SystemExit('Closing style tag not found')
    s = s[:idx] + css + '\n' + s[idx:]

path.write_text(s, encoding='utf-8')
