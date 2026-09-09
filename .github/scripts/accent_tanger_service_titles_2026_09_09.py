from pathlib import Path
import re

PAGES = [
    Path('soins-dentaires-tanger/index.html'),
    Path('chirurgie-dentaire-tanger/index.html'),
    Path('dentisterie-esthetique-tanger/index.html'),
    Path('endodontie-tanger/index.html'),
    Path('parodontologie-tanger/index.html'),
    Path('orthodontie-tanger/index.html'),
]

for path in PAGES:
    text = path.read_text(encoding='utf-8')
    before = text

    # Match the implant page treatment: only “à Tanger” in the visible H1 is accented.
    text, h1_count = re.subn(
        r'(<h1>)([^<]*?)\s+à Tanger(</h1>)',
        r'\1\2 <span>à Tanger</span>\3',
        text,
        count=1,
    )
    if h1_count != 1:
        raise RuntimeError(f'Expected one service H1 ending in à Tanger in {path}, got {h1_count}')

    if '.hero h1 span{color:var(--gold)}' not in text:
        anchor = 'h1{margin:0;max-width:840px;font-size:clamp(44px,6vw,82px);font-weight:300;line-height:.98;letter-spacing:-.025em}'
        if anchor not in text:
            raise RuntimeError(f'H1 CSS anchor not found in {path}')
        text = text.replace(anchor, anchor + '\n.hero h1 span{color:var(--gold)}', 1)

    if text == before:
        raise RuntimeError(f'No change made to {path}')
    path.write_text(text, encoding='utf-8')
    print(f'Updated {path}')

print('Applied implant-style gold “à Tanger” accent to all other service page H1s.')
