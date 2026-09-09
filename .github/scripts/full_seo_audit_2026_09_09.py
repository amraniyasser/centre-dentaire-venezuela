from pathlib import Path
import re, json, html as htmlmod
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin

ROOT = Path('.')
DOMAIN = 'https://centredentairevenezuela.com'
EXPECTED_PHONE = '+212531112127'
EXPECTED_EMAIL = 'centredentairevenezuela@gmail.com'
EXPECTED_ADDRESS_TOKEN = '89 Rue Moussa Ben Noussair'

errors = []
warnings = []
infos = []

HTML_FILES = sorted([p for p in ROOT.rglob('*.html') if '.github' not in p.parts])


def add_error(path, msg): errors.append(f'{path}: {msg}')
def add_warning(path, msg): warnings.append(f'{path}: {msg}')

def page_url(path: Path):
    s = path.as_posix()
    if s == 'index.html': return DOMAIN + '/'
    if s.endswith('/index.html'): return DOMAIN + '/' + s[:-10]
    return DOMAIN + '/' + s

def path_from_internal_url(url: str):
    parsed = urlparse(url)
    path = parsed.path or '/'
    if path == '/': return Path('index.html'), parsed.fragment
    rel = path.lstrip('/')
    if rel.endswith('/'):
        return Path(rel) / 'index.html', parsed.fragment
    p = Path(rel)
    if p.suffix:
        return p, parsed.fragment
    if (ROOT / p / 'index.html').exists():
        return p / 'index.html', parsed.fragment
    if (ROOT / (rel + '.html')).exists():
        return Path(rel + '.html'), parsed.fragment
    return p, parsed.fragment

def attrs(tag):
    return {m.group(1).lower(): htmlmod.unescape(m.group(3) or m.group(4) or m.group(5) or '')
            for m in re.finditer(r'([:\w-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', tag)}

pages = {}
titles = {}
metas = {}
canonicals = {}
indexable_urls = set()

for p in HTML_FILES:
    raw = p.read_text(encoding='utf-8')
    low = raw.lower()
    data = {'raw': raw}
    pages[p] = data

    # HTML/lang/head basics
    mhtml = re.search(r'<html\b[^>]*>', raw, re.I)
    if not mhtml: add_error(p, 'balise <html> absente')
    else:
        a = attrs(mhtml.group(0))
        if a.get('lang','').lower() != 'fr': add_error(p, 'html lang doit être fr')
    if not re.search(r'<meta\s+[^>]*charset=["\']?utf-8', raw, re.I): add_error(p, 'meta charset utf-8 absente')
    if not re.search(r'<meta\s+[^>]*name=["\']viewport["\'][^>]*>', raw, re.I): add_error(p, 'meta viewport absente')

    # title
    mt = re.findall(r'<title>(.*?)</title>', raw, re.I|re.S)
    if len(mt) != 1: add_error(p, f'{len(mt)} balise(s) title au lieu de 1')
    title = re.sub(r'\s+',' ', htmlmod.unescape(mt[0])).strip() if mt else ''
    data['title'] = title
    if title: titles.setdefault(title, []).append(p)

    # meta description
    descs = []
    for tag in re.findall(r'<meta\b[^>]*>', raw, re.I):
        a = attrs(tag)
        if a.get('name','').lower() == 'description': descs.append(a.get('content','').strip())
    if len(descs) != 1: add_error(p, f'{len(descs)} meta description au lieu de 1')
    desc = descs[0] if descs else ''
    data['desc'] = desc
    if desc: metas.setdefault(desc, []).append(p)

    # robots
    robots = []
    for tag in re.findall(r'<meta\b[^>]*>', raw, re.I):
        a = attrs(tag)
        if a.get('name','').lower() == 'robots': robots.append(a.get('content','').lower())
    if len(robots) != 1: add_error(p, f'{len(robots)} meta robots au lieu de 1')
    robots_txt = robots[0] if robots else ''
    noindex = 'noindex' in robots_txt
    data['noindex'] = noindex

    # canonical
    cands = []
    for tag in re.findall(r'<link\b[^>]*>', raw, re.I):
        a = attrs(tag)
        if 'canonical' in a.get('rel','').lower().split(): cands.append(a.get('href','').strip())
    if not noindex and len(cands) != 1: add_error(p, f'{len(cands)} canonical(s) sur page indexable')
    if len(cands) > 1: add_error(p, 'plusieurs canonicales')
    canonical = cands[0] if cands else ''
    data['canonical'] = canonical
    if canonical:
        canonicals.setdefault(canonical, []).append(p)
        if not canonical.startswith(DOMAIN + '/') and canonical != DOMAIN + '/': add_error(p, f'canonical hors domaine apex: {canonical}')
        expected = page_url(p)
        if not noindex and canonical != expected: add_error(p, f'canonical {canonical} != URL attendue {expected}')
    if not noindex:
        indexable_urls.add(page_url(p))

    # H1 exactly one + hierarchy
    h1s = re.findall(r'<h1\b[^>]*>.*?</h1>', raw, re.I|re.S)
    if len(h1s) != 1: add_error(p, f'{len(h1s)} H1 au lieu de 1')
    headings = [(int(n), re.sub('<[^>]+>','',t)) for n,t in re.findall(r'<h([1-6])\b[^>]*>(.*?)</h\1>', raw, re.I|re.S)]
    prev = None
    for level, text in headings:
        if prev and level > prev + 1:
            add_error(p, f'saut de hiérarchie H{prev} vers H{level}')
            break
        prev = level

    # duplicate IDs
    ids = []
    for tag in re.findall(r'<[a-zA-Z][^>]*>', raw):
        a = attrs(tag)
        if a.get('id'): ids.append(a['id'])
    dups = sorted({x for x in ids if ids.count(x) > 1})
    if dups: add_error(p, f'IDs dupliqués: {", ".join(dups[:8])}')
    idset = set(ids)
    data['ids'] = idset

    # images alt + assets
    for tag in re.findall(r'<img\b[^>]*>', raw, re.I):
        a = attrs(tag)
        src = a.get('src','')
        if 'alt' not in a: add_error(p, f'image sans alt: {src}')
        if src and not src.startswith(('http://','https://','data:')):
            target = (ROOT / src.lstrip('/')) if src.startswith('/') else (p.parent / src)
            if not target.exists(): add_error(p, f'image locale introuvable: {src}')

    # favicon exists
    favs = []
    for tag in re.findall(r'<link\b[^>]*>', raw, re.I):
        a=attrs(tag)
        if 'icon' in a.get('rel','').lower(): favs.append(a.get('href',''))
    if not favs: add_error(p, 'favicon absente')
    for fav in favs:
        if fav.startswith('/') and not (ROOT / fav.lstrip('/')).exists(): add_error(p, f'favicon introuvable: {fav}')

    # Open Graph / Twitter on indexable pages
    props = {}
    names = {}
    for tag in re.findall(r'<meta\b[^>]*>', raw, re.I):
        a=attrs(tag)
        if a.get('property'): props[a['property']] = a.get('content','')
        if a.get('name'): names[a['name']] = a.get('content','')
    if not noindex:
        for k in ['og:type','og:locale','og:site_name','og:title','og:description','og:url','og:image']:
            if not props.get(k): add_error(p, f'{k} absent')
        if not names.get('twitter:card'): add_error(p, 'twitter:card absent')
        if props.get('og:url') and props.get('og:url') != page_url(p): add_error(p, f'og:url incorrect: {props.get("og:url")}')
        ogimg = props.get('og:image','')
        if ogimg.startswith(DOMAIN + '/'):
            opath = ROOT / urlparse(ogimg).path.lstrip('/')
            if not opath.exists(): add_error(p, f'og:image locale introuvable: {ogimg}')

    # JSON-LD parse all blocks
    jblocks = re.findall(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', raw, re.I|re.S)
    data['jsonld'] = []
    for i,b in enumerate(jblocks,1):
        try:
            obj=json.loads(b)
            data['jsonld'].append(obj)
        except Exception as e:
            add_error(p, f'JSON-LD #{i} invalide: {e}')

    if 'faqpage' in low: add_error(p, 'FAQPage schema présent alors qu’il ne doit pas l’être')
    if 'aggregaterating' in low: add_error(p, 'aggregateRating statique présent')

    # unsafe/forbidden claims
    if re.search(r'panoramique|radiographie panoramique', raw, re.I): add_error(p, 'mention de radiographie panoramique détectée')
    if re.search(r'orthodontiste', raw, re.I): add_error(p, 'terme orthodontiste détecté sans qualification confirmée')

    # links: broken internal file/anchor + target blank safety
    for tag in re.findall(r'<a\b[^>]*>', raw, re.I):
        a=attrs(tag)
        href=a.get('href','').strip()
        if not href: add_error(p, 'lien <a> sans href') ; continue
        if a.get('target','').lower() == '_blank' and 'noopener' not in a.get('rel','').lower(): add_error(p, f'target=_blank sans noopener: {href}')
        if href.startswith(('#','mailto:','tel:','javascript:')): 
            if href.startswith('#') and href[1:] and href[1:] not in idset: add_error(p, f'ancre locale introuvable: {href}')
            continue
        parsed=urlparse(href)
        if parsed.scheme in ('http','https') and parsed.netloc not in ('centredentairevenezuela.com','www.centredentairevenezuela.com'):
            continue
        if href.startswith('//'): continue
        absurl = href if parsed.scheme else urljoin(page_url(p), href)
        pu=urlparse(absurl)
        if pu.netloc in ('centredentairevenezuela.com','www.centredentairevenezuela.com'):
            target, frag = path_from_internal_url(absurl)
            if not (ROOT/target).exists(): add_error(p, f'lien interne cassé: {href} -> {target}')
            elif frag:
                targetraw=(ROOT/target).read_text(encoding='utf-8')
                tids=set(re.findall(r'\bid=["\']([^"\']+)["\']', targetraw, re.I))
                if frag not in tids: add_error(p, f'ancre cible introuvable: {href}')

    # informational metrics only
    text = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', raw, flags=re.I|re.S)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = re.findall(r"[A-Za-zÀ-ÿ0-9’'-]+", htmlmod.unescape(text))
    infos.append((str(p), title, len(title), len(desc), len(words), noindex))

# duplicate key metadata on indexable pages
for title, ps in titles.items():
    ips=[p for p in ps if not pages[p]['noindex']]
    if len(ips)>1: errors.append(f'Title dupliqué entre pages indexables: {title} -> {ips}')
for desc, ps in metas.items():
    ips=[p for p in ps if not pages[p]['noindex']]
    if len(ips)>1: errors.append(f'Meta description dupliquée entre pages indexables -> {ips}')
for can, ps in canonicals.items():
    ips=[p for p in ps if not pages[p]['noindex']]
    if len(ips)>1: errors.append(f'Canonical dupliquée: {can} -> {ips}')

# sitemap
sitemap = ROOT / 'sitemap.xml'
if not sitemap.exists():
    add_error('sitemap.xml','fichier absent')
    sitemap_urls=set()
else:
    try:
        tree=ET.parse(sitemap)
        ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        sitemap_urls={e.text.strip() for e in tree.findall('.//s:loc',ns) if e.text}
        for u in sitemap_urls:
            if not u.startswith(DOMAIN + '/') and u != DOMAIN + '/': add_error('sitemap.xml',f'URL hors domaine apex: {u}')
            fp,_=path_from_internal_url(u)
            if not (ROOT/fp).exists(): add_error('sitemap.xml',f'URL sans fichier: {u}')
            elif pages.get(fp,{}).get('noindex'): add_error('sitemap.xml',f'URL noindex incluse: {u}')
        missing = sorted(indexable_urls - sitemap_urls)
        extra = sorted(sitemap_urls - indexable_urls)
        if missing: add_error('sitemap.xml',f'pages indexables absentes: {missing}')
        if extra: add_error('sitemap.xml',f'URLs sitemap non indexables/inconnues: {extra}')
    except Exception as e:
        add_error('sitemap.xml',f'XML invalide: {e}')

# robots
robots = ROOT/'robots.txt'
if not robots.exists(): add_error('robots.txt','absent')
else:
    rt=robots.read_text(encoding='utf-8')
    if 'User-agent: *' not in rt: add_error('robots.txt','User-agent: * absent')
    if 'Allow: /' not in rt: add_error('robots.txt','Allow: / absent')
    if f'Sitemap: {DOMAIN}/sitemap.xml' not in rt: add_error('robots.txt','déclaration sitemap incorrecte/absente')

# CNAME
cname=ROOT/'CNAME'
if not cname.exists(): add_error('CNAME','absent')
elif cname.read_text(encoding='utf-8').strip() != 'centredentairevenezuela.com': add_error('CNAME','doit être centredentairevenezuela.com')

# service page business schema + breadcrumb / motifs
service_paths = [Path(x) for x in [
 'soins-dentaires-tanger/index.html','chirurgie-dentaire-tanger/index.html','dentisterie-esthetique-tanger/index.html',
 'implant-dentaire-tanger/index.html','endodontie-tanger/index.html','parodontologie-tanger/index.html','orthodontie-tanger/index.html']]
for p in service_paths:
    if p not in pages: add_error(p,'page de soin absente'); continue
    raw=pages[p]['raw']
    if 'Motifs fréquents de consultation' not in raw: add_error(p,'bloc Motifs fréquents de consultation absent')
    if 'BreadcrumbList' not in raw: add_error(p,'BreadcrumbList schema absent')
    if 'Service' not in raw: add_error(p,'Service schema absent')
    if EXPECTED_PHONE not in raw: add_error(p,'téléphone NAP canonique absent')
    if EXPECTED_EMAIL not in raw: add_error(p,'email canonique absent')
    if EXPECTED_ADDRESS_TOKEN not in raw: add_error(p,'adresse NAP canonique absente')

# blog and merci should remain noindex for now
for p in [Path('blog/index.html'), Path('merci.html')]:
    if p.exists() and not pages[p]['noindex']: add_error(p,'doit rester noindex pour le moment')

# report
lines=[]
lines.append('# Audit SEO technique complet')
lines.append('')
lines.append(f'- Fichiers HTML analysés : **{len(HTML_FILES)}**')
lines.append(f'- Erreurs bloquantes / techniques : **{len(errors)}**')
lines.append(f'- Avertissements : **{len(warnings)}**')
lines.append('')
if errors:
    lines.append('## Erreurs')
    for e in errors: lines.append(f'- {e}')
else:
    lines.append('## Erreurs')
    lines.append('- Aucune erreur détectée par les contrôles automatisés.')
if warnings:
    lines.append('')
    lines.append('## Avertissements')
    for w in warnings: lines.append(f'- {w}')
lines.append('')
lines.append('## Inventaire')
lines.append('| Page | Title chars | Meta chars | Mots | Indexable |')
lines.append('|---|---:|---:|---:|---|')
for path,title,tl,dl,wc,noidx in infos:
    lines.append(f'| `{path}` | {tl} | {dl} | {wc} | {"non" if noidx else "oui"} |')
lines.append('')
lines.append('## Contrôles couverts')
lines.append('HTML/lang/charset/viewport, title/meta/robots/canonical, H1 et hiérarchie Hn, IDs dupliqués, images/alt/assets, favicon, Open Graph/Twitter, JSON-LD, liens internes et ancres, target blank/noopener, sitemap, robots, CNAME, duplication de métadonnées, NAP des pages soins, breadcrumbs/service schema, bloc Motifs fréquents, exclusions FAQPage/aggregateRating, mentions interdites panoramique/orthodontiste.')
Path('.github/seo-audit-report.md').write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines[:30]))
if errors:
    raise SystemExit(2)
