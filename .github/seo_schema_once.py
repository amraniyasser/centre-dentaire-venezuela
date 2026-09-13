from pathlib import Path
import json,re
BASE='https://centredentairevenezuela.com'; TODAY='2026-09-13'
D=BASE+'/#dentist'; W=BASE+'/#website'; P=BASE+'/dr-majda-laasraoui-dentiste-tanger/#person'

def rd(p): return Path(p).read_text(encoding='utf-8')
def wr(p,s): Path(p).write_text(s,encoding='utf-8'); print('updated',p)
def website(): return {'@type':'WebSite','@id':W,'url':BASE+'/','name':'Centre Dentaire Venezuela','inLanguage':'fr-MA','publisher':{'@id':D}}
def dentist(): return {'@type':'Dentist','@id':D,'name':'Centre Dentaire Venezuela','alternateName':'Centre Dentaire Venezuela Tanger','url':BASE+'/','telephone':'+212531112127','email':'centredentairevenezuela@gmail.com','address':{'@type':'PostalAddress','streetAddress':'4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair','postalCode':'90000','addressLocality':'Tanger','addressRegion':'Tanger-Tétouan-Al Hoceïma','addressCountry':'MA'},'geo':{'@type':'GeoCoordinates','latitude':35.7781833,'longitude':-5.8165155},'areaServed':{'@type':'City','name':'Tanger'},'hasMap':'https://maps.app.goo.gl/6SJrWgcmshbDhSLH7','sameAs':['https://www.instagram.com/centre.dentaire.venezuela/','https://www.tiktok.com/@centredentairevenezuela','https://maps.app.goo.gl/6SJrWgcmshbDhSLH7'],'knowsLanguage':['fr','ar','en','es'],'employee':{'@id':P},'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Wednesday','Friday'],'opens':'09:30','closes':'17:30'},{'@type':'OpeningHoursSpecification','dayOfWeek':['Tuesday','Thursday'],'opens':'09:30','closes':'13:00'},{'@type':'OpeningHoursSpecification','dayOfWeek':['Tuesday','Thursday'],'opens':'15:00','closes':'18:30'},{'@type':'OpeningHoursSpecification','dayOfWeek':'Saturday','opens':'10:00','closes':'14:00'}]}
def person(): return {'@type':'Person','@id':P,'name':'Dr Majda Laasraoui','jobTitle':'Chirurgienne-dentiste','url':BASE+'/dr-majda-laasraoui-dentiste-tanger/','worksFor':{'@id':D},'alumniOf':{'@type':'EducationalOrganization','name':'CEU Cardinal Herrera University','address':{'@type':'PostalAddress','addressLocality':'Valence','addressCountry':'ES'}},'knowsLanguage':['fr','ar','en','es']}

def add_master_schema(path):
    s=rd(path)
    if W in s and 'application/ld+json' in s: return
    data={'@context':'https://schema.org','@graph':[website(),dentist(),person()]}
    block='<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':'))+'</script>\n'
    if '</head>' not in s: raise RuntimeError('no head '+path)
    wr(path,s.replace('</head>',block+'</head>',1))

def add_blog_schema():
    p='blog/index.html'; s=rd(p)
    if BASE+'/blog/#blog' in s: return
    arts=[('Implants dentaires en 2026 : 7 choses à savoir',BASE+'/blog/implants-dentaires-2026-7-choses-a-savoir/'),('Philips Zoom, fläsh ou Opalescence : quelles différences ?',BASE+'/blog/flash-opalescence-philips-zoom-blanchiment/'),('Avant un blanchiment dentaire : 7 choses à savoir',BASE+'/blog/blanchiment-dentaire-guide/')]
    graph=[{'@type':'CollectionPage','@id':BASE+'/blog/#webpage','url':BASE+'/blog/','name':'Blog dentaire à Tanger | Centre Dentaire Venezuela','description':'Conseils dentaires documentés sur le blanchiment, les implants et les soins bucco-dentaires.','inLanguage':'fr-MA','isPartOf':{'@id':W},'mainEntity':{'@id':BASE+'/blog/#articles'}},{'@type':'Blog','@id':BASE+'/blog/#blog','url':BASE+'/blog/','name':'Blog dentaire du Centre Dentaire Venezuela','inLanguage':'fr-MA','publisher':{'@id':D},'blogPost':[{'@id':u+'#article'} for _,u in arts]},{'@type':'ItemList','@id':BASE+'/blog/#articles','name':'Articles du blog dentaire','itemListElement':[{'@type':'ListItem','position':i,'name':n,'url':u} for i,(n,u) in enumerate(arts,1)]},{'@type':'BreadcrumbList','@id':BASE+'/blog/#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Accueil','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'Blog','item':BASE+'/blog/'}]},website(),dentist()]
    block='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,separators=(',',':'))+'</script>\n'
    wr(p,s.replace('</head>',block+'</head>',1))

def faq(text,fid):
    m=re.search(r'<section class="site-faq"[^>]*>(.*?)</section>',text,re.S)
    if not m:return None
    q=[]
    for a,b in re.findall(r'<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>',m.group(1),re.S):
        a=re.sub(r'<[^>]+>','',a).strip(); b=re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',b)).strip()
        q.append({'@type':'Question','name':a,'acceptedAnswer':{'@type':'Answer','text':b}})
    return {'@type':'FAQPage','@id':fid,'mainEntity':q} if q else None

def standardize(path):
    s=rd(path); article=None
    if path=='blog/blanchiment-dentaire-guide/index.html': article=BASE+'/blog/blanchiment-dentaire-guide/'
    if path=='blog/flash-opalescence-philips-zoom-blanchiment/index.html': article=BASE+'/blog/flash-opalescence-philips-zoom-blanchiment/'
    changed=False
    def f(m):
        nonlocal changed
        try:x=json.loads(m.group(2))
        except: return m.group(0)
        g=x.get('@graph') if isinstance(x,dict) else None
        if not isinstance(g,list): return m.group(0)
        for i,o in enumerate(g):
            if not isinstance(o,dict):continue
            if o.get('@type')=='Dentist' or o.get('@id')==D:
                z=dict(o); z.update(dentist()); g[i]=z
            elif o.get('@type')=='Person' and o.get('@id')==P:
                z=dict(o); z.update(person()); g[i]=z
        if not any(isinstance(o,dict) and o.get('@id')==W for o in g): g.append(website())
        if article:
            a=next((o for o in g if isinstance(o,dict) and o.get('@type')=='Article'),None)
            if a:
                a.update({'@id':article+'#article','inLanguage':'fr-MA','mainEntityOfPage':article,'isPartOf':{'@type':'Blog','name':'Blog dentaire du Centre Dentaire Venezuela','url':BASE+'/blog/'},'dateModified':TODAY})
                if 'blanchiment-dentaire-guide' in path:
                    a['about']=[{'@type':'Thing','name':'Blanchiment dentaire'},{'@type':'Thing','name':'Peroxyde d’hydrogène'},{'@type':'Thing','name':'Sensibilité dentaire'},{'@type':'Thing','name':'Activation lumineuse'}]
                    a['contentLocation']={'@type':'City','name':'Tanger','containedInPlace':{'@type':'Country','name':'Maroc'}}
                    c=sorted(set(re.findall(r'https://pubmed\.ncbi\.nlm\.nih\.gov/\d+/',s)))
                    if c:a['citation']=c
                else:
                    a['headline']='Philips Zoom, fläsh ou Opalescence : quelles différences ?'
                    a['description']='Comparatif documenté des protocoles fläsh, Opalescence et Philips Zoom WhiteSpeed à partir des informations officielles des fabricants.'
                fq=faq(s,article+'#faq')
                if fq:
                    g[:]=[o for o in g if not(isinstance(o,dict) and o.get('@type')=='FAQPage')]; g.append(fq)
        x['@graph']=g; changed=True
        return m.group(1)+json.dumps(x,ensure_ascii=False,separators=(',',':'))+m.group(3)
    out=re.sub(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)',f,s,flags=re.S)
    if changed and out!=s: wr(path,out)

add_master_schema('index.html'); add_blog_schema()
for p in sorted(Path('.').rglob('*.html')):
    if '.git' not in p.parts: standardize(p.as_posix())

# Update lastmod only for pages touched by this SEO pass; legal/privacy stay unchanged.
p='sitemap.xml'; s=rd(p)
urls=['/','/dr-majda-laasraoui-dentiste-tanger/','/nos-soins/','/soins-dentaires-tanger/','/chirurgie-dentaire-tanger/','/dentisterie-esthetique-tanger/','/blanchiment-dentaire-tanger/','/endodontie-tanger/','/parodontologie-tanger/','/orthodontie-tanger/','/implant-dentaire-tanger/','/blog/','/blog/blanchiment-dentaire-guide/','/blog/flash-opalescence-philips-zoom-blanchiment/','/blog/implants-dentaires-2026-7-choses-a-savoir/']
for u in urls:
    pat=rf'(<loc>{re.escape(BASE+u)}</loc><lastmod>)\d{{4}}-\d{{2}}-\d{{2}}(</lastmod>)'
    s,n=re.subn(pat,rf'\g<1>{TODAY}\2',s)
    if n!=1: raise RuntimeError('sitemap '+u)
wr(p,s)
