from pathlib import Path
import re

COMPACT = [
    Path('soins-dentaires-tanger/index.html'),
    Path('chirurgie-dentaire-tanger/index.html'),
    Path('dentisterie-esthetique-tanger/index.html'),
    Path('endodontie-tanger/index.html'),
    Path('parodontologie-tanger/index.html'),
    Path('orthodontie-tanger/index.html'),
]
IMPLANT = Path('implant-dentaire-tanger/index.html')


def replace_once(text, old, new, label, path):
    if old not in text:
        raise RuntimeError(f'{label} anchor not found in {path}')
    return text.replace(old, new, 1)

# Six service pages that share the compact markup.
for path in COMPACT:
    text = path.read_text(encoding='utf-8')
    before = text

    text = replace_once(
        text,
        '.hero .wrap{max-width:1400px;margin:0 auto;padding:26px var(--gutter) 62px;position:relative;z-index:1}',
        '.hero .wrap{max-width:1400px;margin:0 auto;padding:18px var(--gutter) 38px;position:relative;z-index:1}',
        'hero padding', path,
    )
    text = replace_once(text, 'margin-bottom:40px;font-size:12px;color:rgba(255,255,255,.7)', 'margin-bottom:24px;font-size:12px;color:rgba(255,255,255,.7)', 'breadcrumb spacing', path)
    text = replace_once(text, '.pill{display:inline-flex;align-items:center;gap:9px;margin-bottom:17px;', '.pill{display:inline-flex;align-items:center;gap:9px;margin-bottom:12px;', 'eyebrow spacing', path)
    text = replace_once(
        text,
        'h1{margin:0;max-width:840px;font-size:clamp(44px,6vw,82px);font-weight:300;line-height:.98;letter-spacing:-.025em}',
        'h1{margin:0;max-width:none;font-size:clamp(40px,4.8vw,68px);font-weight:300;line-height:1;letter-spacing:-.025em;white-space:nowrap}',
        'H1 sizing', path,
    )
    text = replace_once(text, '.hero p{max-width:720px;margin:24px 0 0;font-size:17px;line-height:1.72;', '.hero p{max-width:760px;margin:14px 0 0;font-size:16px;line-height:1.62;', 'hero lead spacing', path)
    text = replace_once(text, '.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}', '.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}', 'hero actions spacing', path)
    text = replace_once(text, '.hero .wrap{padding:22px 20px 38px}', '.hero .wrap{padding:16px 20px 28px}', 'mobile hero padding', path)
    text = replace_once(text, '.crumb{margin-bottom:28px}', '.crumb{margin-bottom:18px}', 'mobile breadcrumb spacing', path)
    text = replace_once(text, 'h1{font-size:clamp(38px,12vw,54px)}', 'h1{font-size:clamp(34px,10vw,50px);white-space:normal}', 'mobile H1 sizing', path)

    if text == before:
        raise RuntimeError(f'No change made to {path}')
    path.write_text(text, encoding='utf-8')
    print(f'Compacted hero in {path}')

# Implant page: same compact hero, remove the “À retenir” card, and align breadcrumb wording.
path = IMPLANT
text = path.read_text(encoding='utf-8')
before = text

text = replace_once(
    text,
    '.hero-inner{max-width:1400px;margin:0 auto;padding:26px var(--gutter) 62px;position:relative;z-index:1}',
    '.hero-inner{max-width:1400px;margin:0 auto;padding:18px var(--gutter) 38px;position:relative;z-index:1}',
    'implant hero padding', path,
)
text = replace_once(text, 'margin-bottom:40px;font-size:12px;color:rgba(255,255,255,.7)', 'margin-bottom:24px;font-size:12px;color:rgba(255,255,255,.7)', 'implant breadcrumb spacing', path)
text = replace_once(text, '.hero-grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(290px,.65fr);gap:clamp(36px,6vw,88px);align-items:center}', '.hero-grid{display:block}', 'implant hero grid', path)
text = replace_once(text, '.eyebrow{display:inline-flex;align-items:center;gap:9px;margin-bottom:17px;', '.eyebrow{display:inline-flex;align-items:center;gap:9px;margin-bottom:12px;', 'implant eyebrow spacing', path)
text = replace_once(
    text,
    'h1{margin:0;max-width:840px;font-size:clamp(44px,6vw,82px);font-weight:300;line-height:.98;letter-spacing:-.025em}',
    'h1{margin:0;max-width:none;font-size:clamp(40px,4.8vw,68px);font-weight:300;line-height:1;letter-spacing:-.025em;white-space:nowrap}',
    'implant H1 sizing', path,
)
text = replace_once(text, '.hero-lead{max-width:720px;margin:24px 0 0;font-size:17px;line-height:1.72;', '.hero-lead{max-width:760px;margin:14px 0 0;font-size:16px;line-height:1.62;', 'implant lead spacing', path)
text = replace_once(text, '.hero-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}', '.hero-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}', 'implant actions spacing', path)

text, quick_count = re.subn(r'\n\s*<aside class="quick" aria-label="À retenir sur les implants dentaires">.*?</aside>', '', text, count=1, flags=re.S)
if quick_count != 1:
    raise RuntimeError(f'Expected one À retenir card in {path}, got {quick_count}')

text = replace_once(
    text,
    '<nav class="breadcrumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span>›</span><a href="/#soins">Nos soins</a><span>›</span><span>Implantologie</span></nav>',
    '<nav class="breadcrumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a> / <a href="/#soins">Nos soins</a> / <span>Implant dentaire</span></nav>',
    'implant visible breadcrumb', path,
)
text = text.replace('"position":3,"name":"Implantologie"', '"position":3,"name":"Implant dentaire"', 1)

text = replace_once(text, '.hero-inner{padding:22px 20px 38px}', '.hero-inner{padding:16px 20px 28px}', 'implant mobile hero padding', path)
text = replace_once(text, '.breadcrumbs{margin-bottom:28px}', '.breadcrumbs{margin-bottom:18px}', 'implant mobile breadcrumb spacing', path)
text = replace_once(text, 'h1{font-size:clamp(38px,12vw,54px)}', 'h1{font-size:clamp(34px,10vw,50px);white-space:normal}', 'implant mobile H1 sizing', path)

if text == before:
    raise RuntimeError(f'No change made to {path}')
path.write_text(text, encoding='utf-8')
print(f'Compacted hero and aligned breadcrumb in {path}')

print('All seven service heroes compacted; desktop H1s are one line; implant À retenir card removed.')
