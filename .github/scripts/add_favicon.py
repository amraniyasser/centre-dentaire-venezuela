from pathlib import Path
import re

FAVICON = '<link rel="icon" type="image/webp" href="/assets/images/logo-centre-dentaire-venezuela.webp">\n<link rel="shortcut icon" type="image/webp" href="/assets/images/logo-centre-dentaire-venezuela.webp">\n'

paths = [Path('index.html'), Path('merci.html')]
paths += sorted(p for p in Path('.').glob('*/index.html') if '.github' not in p.parts)

for path in paths:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    if 'logo-centre-dentaire-venezuela.webp' in text and 'rel="icon"' in text:
        continue
    new_text, count = re.subn(
        r'(<meta\s+name=["\']viewport["\'][^>]*>\s*)',
        r'\1' + FAVICON,
        text,
        count=1,
        flags=re.I,
    )
    if count == 0:
        raise RuntimeError(f'Viewport meta not found in {path}')
    path.write_text(new_text, encoding='utf-8')
    print(f'Updated {path}')
