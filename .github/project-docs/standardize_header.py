from pathlib import Path
import re

# Canonical header rollout script.
repo=Path('.')
home=(repo/'index.html').read_text(encoding='utf-8')
m=re.search(r'(<header>\s*<nav class="nav" aria-label="Navigation principale">.*?</nav>\s*</header>)', home, flags=re.S)
if not m:
    raise SystemExit('Homepage canonical header not found')
canonical=m.group(1)
inner=canonical
for a in ['cabinet','resultats','localisation','rdv']:
    inner=inner.replace(f'href="#{a}"',f'href="/#{a}"')
inner=inner.replace(' aria-current="page"','')

css='''<style id="cv-header-styles">
:root{--cv-nav-h:68px;--cv-gutter:4.6%;--cv-ink:#143b3e;--cv-teal:#8abdb8;--cv-teal-soft:#8fb5b1;--cv-teal-deep:#2f6d6b;--cv-btn:#8fbdb6;--cv-link:#3c5c5c;--cv-white:#fff}
body>header:has(>.nav){position:sticky;top:0;z-index:100}
.nav{position:relative;height:var(--cv-nav-h);display:flex;align-items:center;justify-content:space-between;gap:28px;padding:0 var(--cv-gutter);background:rgba(255,255,255,.96);transition:background .3s,box-shadow .3s,backdrop-filter .3s;font-family:"Avenir Next","Helvetica Neue",Arial,sans-serif}
.nav.is-scrolled{background:rgba(255,255,255,.62);backdrop-filter:blur(14px) saturate(1.4);box-shadow:0 1px 0 rgba(20,59,62,.08)}
.nav a{text-decoration:none}.nav-right{display:flex;align-items:center;gap:12px}
.nav .brand{display:flex;flex-direction:column;justify-content:center;gap:5px;line-height:1;text-decoration:none}
.nav .brand-kicker{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--cv-teal-soft);font-weight:500}
.nav .brand-name{font-size:18.6px;letter-spacing:.126em;text-transform:uppercase;color:var(--cv-teal-deep);font-weight:400}
.nav .links{display:flex;align-items:center;gap:30px;white-space:nowrap}
.nav .links a{position:relative;padding:6px 0;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--cv-link)}
.nav-menu{display:none;position:relative}.nav-menu>summary{display:grid;place-items:center;width:40px;height:40px;border-radius:11px;border:1px solid rgba(20,59,62,.14);background:var(--cv-white);color:var(--cv-ink);cursor:pointer;list-style:none}.nav-menu>summary::-webkit-details-marker{display:none}.nav-menu>summary svg{width:19px;height:19px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round}.nav-menu[open]>summary{background:var(--cv-ink);border-color:var(--cv-ink);color:var(--cv-white)}
.nav-panel{position:absolute;top:calc(100% + 12px);right:0;min-width:236px;display:flex;flex-direction:column;padding:8px;border-radius:16px;background:var(--cv-white);box-shadow:0 18px 40px rgba(20,59,62,.16);border:1px solid rgba(20,59,62,.08)}
.nav-panel a{padding:11px 13px;border-radius:10px;font-size:12.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--cv-link)}.nav-panel a:hover{background:#f2f7f6}
.nav-rdv{display:inline-flex;align-items:center;height:38px;padding:0 20px;border-radius:10px;background:var(--cv-btn);color:var(--cv-white)!important;font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;box-shadow:0 6px 18px rgba(55,113,109,.16)}.rdv-short{display:none}
@media(max-width:1080px){.nav .links{gap:18px}.nav .links a{font-size:10.5px}.nav-rdv{padding:0 14px}.rdv-long{display:none}.rdv-short{display:inline}}
@media(max-width:820px){.nav{padding:0 20px}.nav .links{display:none}.nav-menu{display:block}.nav-rdv{height:40px}.nav .brand-name{font-size:17px}}
@media(max-width:430px){.nav{gap:10px}.nav-rdv{padding:0 11px;font-size:10px}.nav-panel{min-width:220px;right:-52px}}
</style>'''
js='''<script id="cv-header-script">(function(){var nav=document.querySelector('.nav');if(!nav)return;function sync(){nav.classList.toggle('is-scrolled',window.scrollY>8)}sync();window.addEventListener('scroll',sync,{passive:true});var menu=nav.querySelector('.nav-menu');if(menu){document.addEventListener('pointerdown',function(e){if(menu.open&&!menu.contains(e.target))menu.open=false});menu.addEventListener('click',function(e){if(e.target.closest('.nav-panel a'))menu.open=false})}})();</script>'''

html_files=[p for p in repo.rglob('*.html') if '.github' not in p.parts]
updated=[]
for p in html_files:
    if p.as_posix()=='index.html':
        continue
    s=p.read_text(encoding='utf-8')
    s=re.sub(r'<style id="cv-header-styles">.*?</style>','',s,flags=re.S)
    s=re.sub(r'<script id="cv-header-script">.*?</script>','',s,flags=re.S)
    if re.search(r'<header\b.*?</header>',s,flags=re.S|re.I):
        s=re.sub(r'<header\b.*?</header>',inner,s,count=1,flags=re.S|re.I)
    elif '<body>' in s:
        s=s.replace('<body>','<body>'+inner,1)
    else:
        continue
    s=s.replace('</head>',css+'\n</head>',1)
    s=s.replace('</body>',js+'\n</body>',1)
    p.write_text(s,encoding='utf-8')
    updated.append(str(p))

rules=repo/'.github/project-docs/instructions-projet-centre-dentaire-venezuela.md'
if rules.exists():
    r=rules.read_text(encoding='utf-8')
    marker='## Header canonique — règle obligatoire'
    block='''\n\n## Header canonique — règle obligatoire\n- Toute nouvelle page HTML doit reprendre le même header/navbar que la homepage.\n- Même design, même ordre de navigation, même menu mobile et même bouton de rendez-vous.\n- Sur les pages internes, les ancres Cabinet / Transformations / Localisation / RDV doivent renvoyer vers les sections correspondantes de la homepage avec des URLs `/#...`.\n- Ne jamais créer une variante de header pour une page de soin, blog, praticienne ou page légale.\n'''
    if marker not in r:
        rules.write_text(r.rstrip()+block+'\n',encoding='utf-8')

for p in html_files:
    s=p.read_text(encoding='utf-8')
    assert 'class="nav" aria-label="Navigation principale"' in s, f'canonical nav missing: {p}'
    assert '/nos-soins/' in s and '/blog/' in s, f'nav links missing: {p}'
print('Updated',len(updated),'inner HTML pages')
