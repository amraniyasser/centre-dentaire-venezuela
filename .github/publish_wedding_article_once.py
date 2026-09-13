from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path('.')
NEW_URL = 'https://centredentairevenezuela.com/blog/blanchiment-dentaire-avant-mariage/'
NEW_ARTICLE_ID = NEW_URL + '#article'

# 1) Blog index: card + structured data.
blog_path = ROOT / 'blog/index.html'
blog = blog_path.read_text(encoding='utf-8')
card = '<article class="card" data-category="esthetique"><a href="/blog/blanchiment-dentaire-avant-mariage/"><div class="cover"><span class="tag">Mariage · Esthétique</span><span class="scribble"></span><p class="cover-title">Blanchiment dentaire avant mariage : quand le faire ?</p></div><div class="meta">13 sept. 2026</div><h2>Blanchiment avant mariage : le bon timing avant le jour J</h2></a></article>'
marker = '<div class="grid" id="article-grid">'
if '/blog/blanchiment-dentaire-avant-mariage/' not in blog:
    blog = blog.replace(marker, marker + card, 1)

script_re = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
for match in list(script_re.finditer(blog)):
    raw = match.group(1)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        continue
    graph = data.get('@graph', []) if isinstance(data, dict) else []
    if not any(isinstance(x, dict) and x.get('@id') == 'https://centredentairevenezuela.com/blog/#webpage' for x in graph):
        continue
    for obj in graph:
        if not isinstance(obj, dict):
            continue
        if obj.get('@type') == 'Blog':
            posts = obj.setdefault('blogPost', [])
            if not any(isinstance(x, dict) and x.get('@id') == NEW_ARTICLE_ID for x in posts):
                posts.insert(0, {'@id': NEW_ARTICLE_ID})
        if obj.get('@type') == 'ItemList' and obj.get('@id') == 'https://centredentairevenezuela.com/blog/#articles':
            items = obj.setdefault('itemListElement', [])
            if not any(isinstance(x, dict) and x.get('url') == NEW_URL for x in items):
                for item in items:
                    if isinstance(item, dict) and isinstance(item.get('position'), int):
                        item['position'] += 1
                items.insert(0, {'@type':'ListItem','position':1,'name':'Blanchiment dentaire avant un mariage : quand faut-il le faire ?','url':NEW_URL})
    replacement = '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '</script>'
    blog = blog[:match.start()] + replacement + blog[match.end():]
    break
blog_path.write_text(blog, encoding='utf-8')

# 2) Service page: contextual link back to wedding article.
service_path = ROOT / 'blanchiment-dentaire-tanger/index.html'
service = service_path.read_text(encoding='utf-8')
old = '<div class="related"><a href="/dentisterie-esthetique-tanger/">Dentisterie esthétique</a><a href="/blog/blanchiment-dentaire-guide/">7 choses à savoir avant un blanchiment</a>'
new = '<div class="related"><a href="/dentisterie-esthetique-tanger/">Dentisterie esthétique</a><a href="/blog/blanchiment-dentaire-guide/">7 choses à savoir avant un blanchiment</a><a href="/blog/blanchiment-dentaire-avant-mariage/">Blanchiment avant un mariage : quand le faire ?</a>'
if '/blog/blanchiment-dentaire-avant-mariage/' not in service:
    if old not in service:
        raise SystemExit('Service related-links marker not found')
    service = service.replace(old, new, 1)
service_path.write_text(service, encoding='utf-8')

# 3) General whitening guide: contextual wedding link for reciprocal internal linking.
guide_path = ROOT / 'blog/blanchiment-dentaire-guide/index.html'
guide = guide_path.read_text(encoding='utf-8')
wedding_callout = '<div class="callout"><b>Vous préparez un mariage ?</b><p>Le timing devient une question à part entière : délai avant le jour J, risque de sensibilité dans les jours qui suivent et marge à garder avant les photos. Consultez notre guide dédié <a href="/blog/blanchiment-dentaire-avant-mariage/"><strong>blanchiment dentaire avant un mariage : quand faut-il le faire ?</strong></a>.</p></div>\n'
if '/blog/blanchiment-dentaire-avant-mariage/' not in guide:
    cta = '<div class="cta-box"><h2>Vous envisagez un blanchiment dentaire à Tanger&nbsp;?</h2>'
    if cta not in guide:
        raise SystemExit('Guide CTA marker not found')
    guide = guide.replace(cta, wedding_callout + cta, 1)
guide_path.write_text(guide, encoding='utf-8')

# 4) Sitemap: add the new article.
sitemap_path = ROOT / 'sitemap.xml'
sitemap = sitemap_path.read_text(encoding='utf-8')
entry = '  <url><loc>' + NEW_URL + '</loc><lastmod>2026-09-13</lastmod></url>\n'
if NEW_URL not in sitemap:
    sitemap = sitemap.replace('</urlset>', entry + '</urlset>')
sitemap_path.write_text(sitemap, encoding='utf-8')

# 5) Validation.
article = (ROOT / 'blog/blanchiment-dentaire-avant-mariage/index.html').read_text(encoding='utf-8')
assert article.count('<h1>') == 1
assert 'blog-summary' in article
assert article.count('class="geo-table"') >= 3
assert 'Dr Majda Laasraoui' in article
assert '/blanchiment-dentaire-tanger/' in article
assert 'www.brides.com/story/wedding-teeth-whitening-ideas' in article
assert article.count('pubmed.ncbi.nlm.nih.gov') >= 4
assert 'avant-apres-03-blanchiment-avant.webp' in article and 'avant-apres-03-blanchiment-apres.webp' in article
for path in [ROOT/'blog/index.html', ROOT/'blanchiment-dentaire-tanger/index.html', ROOT/'blog/blanchiment-dentaire-guide/index.html', ROOT/'blog/blanchiment-dentaire-avant-mariage/index.html']:
    text = path.read_text(encoding='utf-8')
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, flags=re.S):
        json.loads(raw)
ET.parse(sitemap_path)
assert NEW_URL in sitemap_path.read_text(encoding='utf-8')
assert '/blog/blanchiment-dentaire-avant-mariage/' in service_path.read_text(encoding='utf-8')
assert '/blog/blanchiment-dentaire-avant-mariage/' in guide_path.read_text(encoding='utf-8')
print('Wedding article publication checks passed')
