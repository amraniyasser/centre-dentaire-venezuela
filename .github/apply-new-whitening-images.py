from pathlib import Path
import base64, json, re

ROOT = Path(__file__).resolve().parents[1]
article = ROOT / "blog/blanchiment-dentaire-avant-mariage/index.html"
before_path = ROOT / "assets/images/blog/blanchiment-avant-mariage-avant-dr-majda.webp"
after_path = ROOT / "assets/images/blog/blanchiment-avant-mariage-apres-dr-majda.webp"

before_b64 = (ROOT / ".github/tmp-before-b64.txt").read_text().strip()
after_b64 = ((ROOT / ".github/tmp-after-a.txt").read_text().strip() +
             (ROOT / ".github/tmp-after-b.txt").read_text().strip())

before = base64.b64decode(before_b64, validate=True)
after = base64.b64decode(after_b64, validate=True)
for name, payload in [("before", before), ("after", after)]:
    assert len(payload) > 4000, f"{name} image unexpectedly small"
    assert payload[:4] == b"RIFF" and payload[8:12] == b"WEBP", f"{name} is not WEBP"

before_path.write_bytes(before)
after_path.write_bytes(after)

html = article.read_text()

html = html.replace(
    'https://centredentairevenezuela.com/assets/images/avant-apres-03-blanchiment-apres.webp',
    'https://centredentairevenezuela.com/assets/images/blog/blanchiment-avant-mariage-apres-dr-majda.webp'
)
html = html.replace(
    'https://centredentairevenezuela.com/assets/images/avant-apres-03-blanchiment-avant.webp',
    'https://centredentairevenezuela.com/assets/images/blog/blanchiment-avant-mariage-avant-dr-majda.webp'
)
html = html.replace(
    '.photo-card img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}',
    '.photo-card img{display:block;width:100%;height:auto;object-fit:contain;background:#f7faf9}'
)
html = html.replace(
    'Les photos ci-dessous illustrent un cas de blanchiment réalisé au Centre Dentaire Venezuela.',
    'Les photos ci-dessous illustrent un cas de blanchiment réalisé au Centre Dentaire Venezuela par <a href="/dr-majda-laasraoui-dentiste-tanger/"><strong>Dr Majda Laasraoui</strong></a>, chirurgienne-dentiste à Tanger.'
)
old_pair = '<div class="photo-pair"><figure class="photo-card"><img src="/assets/images/avant-apres-03-blanchiment-avant.webp" alt="Avant un blanchiment dentaire réalisé au Centre Dentaire Venezuela à Tanger" loading="lazy" width="1200" height="900"><figcaption>Avant le blanchiment</figcaption></figure><figure class="photo-card"><img src="/assets/images/avant-apres-03-blanchiment-apres.webp" alt="Après un blanchiment dentaire réalisé au Centre Dentaire Venezuela à Tanger" loading="lazy" width="1200" height="900"><figcaption>Après le blanchiment</figcaption></figure></div>'
new_pair = '<div class="photo-pair"><figure class="photo-card"><img src="/assets/images/blog/blanchiment-avant-mariage-avant-dr-majda.webp" alt="Avant un blanchiment dentaire réalisé par Dr Majda Laasraoui au Centre Dentaire Venezuela à Tanger" loading="lazy" width="390" height="276"><figcaption><strong>Avant</strong> — teinte initiale avant le blanchiment.</figcaption></figure><figure class="photo-card"><img src="/assets/images/blog/blanchiment-avant-mariage-apres-dr-majda.webp" alt="Après un blanchiment dentaire réalisé par Dr Majda Laasraoui au Centre Dentaire Venezuela à Tanger" loading="lazy" width="390" height="276"><figcaption><strong>Après</strong> — résultat obtenu après le blanchiment.</figcaption></figure></div>'
assert old_pair in html, "old photo pair not found"
html = html.replace(old_pair, new_pair)
html = html.replace(
    '<p class="photo-note">Cas clinique illustratif. Le résultat varie selon la teinte de départ, la cause des colorations et le protocole retenu ; il ne constitue pas une promesse de résultat identique.</p>',
    '<p class="photo-note">Blanchiment réalisé par <a href="/dr-majda-laasraoui-dentiste-tanger/"><strong>Dr Majda Laasraoui</strong></a> au Centre Dentaire Venezuela à Tanger. Cas clinique illustratif : le résultat varie selon la teinte de départ, la cause des colorations et le protocole retenu ; il ne constitue pas une promesse de résultat identique.</p>'
)

if 'name="twitter:image"' not in html:
    html = html.replace(
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://centredentairevenezuela.com/assets/images/blog/blanchiment-avant-mariage-apres-dr-majda.webp">'
    )

assert '/assets/images/avant-apres-03-blanchiment-avant.webp' not in html
assert '/assets/images/avant-apres-03-blanchiment-apres.webp' not in html
assert html.count('blanchiment-avant-mariage-avant-dr-majda.webp') >= 2
assert html.count('blanchiment-avant-mariage-apres-dr-majda.webp') >= 3
assert html.count('/dr-majda-laasraoui-dentiste-tanger/') >= 2

for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.S):
    json.loads(block)

article.write_text(html)
print("Updated wedding whitening article and clinical before/after images.")
