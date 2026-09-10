from pathlib import Path

FAQ_MARKER='data-site-faq="true"'

homepage = Path('index.html')
blog = Path('blog/index.html')
article = Path('blog/blanchiment-dentaire-guide/index.html')

FAQ_CSS = '''\n/* FAQ site-wide */\n.site-faq{padding:72px 20px;background:#f2f7f6}\n.site-faq .faq-inner{max-width:980px;margin:0 auto}\n.site-faq .faq-kicker{display:block;margin-bottom:12px;font-size:10.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#8fb5b1}\n.site-faq h2{margin:0 0 26px;font-size:clamp(30px,4vw,46px);font-weight:300;line-height:1.1;color:#143b3e}\n.site-faq details{border-top:1px solid rgba(20,59,62,.11)}\n.site-faq details:last-child{border-bottom:1px solid rgba(20,59,62,.11)}\n.site-faq summary{cursor:pointer;list-style:none;padding:21px 38px 21px 0;font-size:16px;font-weight:600;color:#143b3e;position:relative}\n.site-faq summary::-webkit-details-marker{display:none}\n.site-faq summary:after{content:"+";position:absolute;right:4px;top:17px;font-size:24px;font-weight:300;color:#2f6d6b}\n.site-faq details[open] summary:after{content:"–"}\n.site-faq details p{margin:-3px 0 22px;max-width:820px;font-size:14.5px;line-height:1.72;color:#5d7d7c}\n@media(max-width:680px){.site-faq{padding:52px 20px}.site-faq summary{font-size:15px}}\n'''

HOME_FAQ = '''\n<section class="site-faq" data-site-faq="true" aria-labelledby="faq-accueil-title"><div class="faq-inner"><span class="faq-kicker">Questions fréquentes</span><h2 id="faq-accueil-title">FAQ sur le Centre Dentaire Venezuela à Tanger</h2><details><summary>Quels soins dentaires sont proposés au cabinet ?</summary><p>Le Centre Dentaire Venezuela propose notamment des soins dentaires généraux, de la chirurgie dentaire, de l’implantologie, de la dentisterie esthétique, de l’endodontie, de la parodontologie et de l’orthodontie.</p></details><details><summary>Comment prendre rendez-vous ?</summary><p>Vous pouvez prendre rendez-vous par téléphone, par WhatsApp ou via le formulaire de rendez-vous disponible sur le site.</p></details><details><summary>Où se trouve le Centre Dentaire Venezuela à Tanger ?</summary><p>Le cabinet est situé au 4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair, Tanger 90000.</p></details><details><summary>Dans quelles langues les consultations sont-elles possibles ?</summary><p>Les consultations peuvent être réalisées en français, arabe, anglais et espagnol.</p></details><details><summary>Faut-il un bilan avant un traitement dentaire ?</summary><p>Oui. Le choix d’un traitement dépend de l’examen clinique, de vos symptômes, de vos attentes et de l’état de vos dents et de vos gencives.</p></details></div></section>\n'''

BLOG_FAQ = '''\n<section class="site-faq" data-site-faq="true" aria-labelledby="faq-blog-title"><div class="faq-inner"><span class="faq-kicker">Questions fréquentes</span><h2 id="faq-blog-title">Questions sur nos conseils dentaires</h2><details><summary>Les articles du blog remplacent-ils une consultation dentaire ?</summary><p>Non. Les articles donnent des informations générales et documentées, mais seul un examen permet d’établir un diagnostic et de proposer un traitement adapté.</p></details><details><summary>Les articles sont-ils adaptés aux patients de Tanger ?</summary><p>Oui. Les sujets sont choisis en fonction des questions fréquentes des patients et des soins proposés au Centre Dentaire Venezuela à Tanger.</p></details><details><summary>Comment savoir quel traitement est adapté à ma situation ?</summary><p>Le choix dépend de la cause du problème, de l’état des dents et des gencives et de vos objectifs. Une consultation permet de comparer les options pertinentes.</p></details><details><summary>Les informations médicales sont-elles sourcées ?</summary><p>Lorsque le sujet le nécessite, les articles s’appuient sur des recommandations institutionnelles et des publications scientifiques récentes, avec les références indiquées dans l’article.</p></details></div></section>\n'''

ARTICLE_FAQ = '''\n<section class="site-faq" data-site-faq="true" aria-labelledby="faq-blanchiment-article-title"><div class="faq-inner"><span class="faq-kicker">FAQ blanchiment dentaire</span><h2 id="faq-blanchiment-article-title">Questions fréquentes avant un blanchiment dentaire</h2><details><summary>Le blanchiment dentaire fait-il mal ?</summary><p>Une sensibilité temporaire peut apparaître, surtout dans les premières heures ou les premiers jours. Son intensité dépend du protocole et de la sensibilité initiale.</p></details><details><summary>Combien de temps dure le résultat d’un blanchiment ?</summary><p>La durée varie selon la teinte de départ, les habitudes alimentaires, le tabac, l’hygiène et le protocole utilisé. Il n’existe pas une durée identique pour tous les patients.</p></details><details><summary>Peut-on blanchir des couronnes, des facettes ou des composites ?</summary><p>Les restaurations dentaires ne s’éclaircissent pas comme les dents naturelles. Leur présence doit donc être prise en compte avant de choisir la teinte et le protocole.</p></details><details><summary>LED ou laser : est-ce forcément plus efficace ?</summary><p>Les synthèses scientifiques récentes ne montrent pas de bénéfice constant de l’activation lumineuse ou laser sur le résultat final. Le gel, sa concentration et le protocole restent des éléments essentiels.</p></details><details><summary>Combien de séances faut-il pour un blanchiment ?</summary><p>Le nombre de séances dépend du type de coloration, de la teinte initiale, du produit utilisé et de la réponse au traitement. Le protocole doit être adapté au cas clinique.</p></details><details><summary>Peut-on faire un blanchiment avec des dents sensibles ?</summary><p>Une sensibilité préexistante doit être signalée lors du bilan. Le protocole, la concentration et les mesures de désensibilisation peuvent être adaptés selon la situation.</p></details><details><summary>Que faut-il éviter après le blanchiment ?</summary><p>Les conseils dépendent du protocole. Une bonne hygiène et la limitation des habitudes qui favorisent les colorations, comme le tabac et la consommation fréquente de boissons très pigmentées, peuvent aider à préserver le résultat.</p></details></div></section>\n'''


def add_css(s):
    if '/* FAQ site-wide */' in s:
        return s
    return s.replace('</style>', FAQ_CSS + '\n</style>', 1)


def insert_before_footer(s, faq):
    if FAQ_MARKER in s:
        return s
    marker = '</main>'
    if marker not in s:
        raise SystemExit('No </main> marker found')
    return s.replace(marker, faq + marker, 1)

for p, faq in [(homepage, HOME_FAQ), (blog, BLOG_FAQ), (article, ARTICLE_FAQ)]:
    s = p.read_text(encoding='utf-8')
    s = add_css(s)
    s = insert_before_footer(s, faq)
    p.write_text(s, encoding='utf-8')

# Verify every indexable content HTML page has a visible FAQ. Utility noindex pages are excluded.
missing=[]
for p in Path('.').rglob('*.html'):
    if '.github' in p.parts:
        continue
    s=p.read_text(encoding='utf-8', errors='ignore')
    if 'name="robots"' in s and 'noindex' in s.lower():
        continue
    if ('class="faq"' not in s and FAQ_MARKER not in s and 'faq-section' not in s):
        missing.append(str(p))
if missing:
    raise SystemExit('Indexable pages without visible FAQ: ' + ', '.join(missing))
print('FAQ rule satisfied on all indexable content pages.')
