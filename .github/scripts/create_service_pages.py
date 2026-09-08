from pathlib import Path
import json

ROOT = 'https://centredentairevenezuela.com'
TODAY = '2026-09-08'
CLINIC_ID = ROOT + '/#dentist'

clinic = {
    'name': 'Centre Dentaire Venezuela',
    'phone_display': '+212 5 31 11 21 27',
    'phone': '+212531112127',
    'whatsapp_display': '+212 771 158 018',
    'whatsapp': '+212771158018',
    'email': 'centredentairevenezuela@gmail.com',
    'instagram': 'https://www.instagram.com/centre.dentaire.venezuela/',
    'maps': 'https://share.google/NQdfjEYv9MC4431Lz',
    'address': '4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair, Tanger 90000, Maroc',
}

services = [
    {
        'name':'Soins dentaires généraux','slug':'soins-dentaires-tanger','h1':'Soins dentaires à Tanger','title':'Soins dentaires à Tanger | Centre Dentaire Venezuela',
        'meta':'Soins dentaires à Tanger : détartrage, traitement des caries, obturations et suivi régulier au Centre Dentaire Venezuela.',
        'eyebrow':'Dentisterie générale à Tanger','intro':'Le Centre Dentaire Venezuela à Tanger propose les soins dentaires courants pour prévenir, diagnostiquer et traiter les problèmes bucco-dentaires du quotidien : contrôles, détartrage, caries, obturations et suivi régulier.',
        'keywords':['dentiste généraliste Tanger','soins dentaires Tanger','détartrage Tanger','carie dentaire Tanger','obturation dentaire Tanger'],
        'when_title':'Quand consulter pour des soins dentaires généraux ?','when_items':['Contrôle dentaire de routine ou suivi périodique','Tartre, coloration ou sensation de dents moins lisses','Suspicion de carie, sensibilité au froid ou au chaud','Dent abîmée nécessitant une restauration ou une obturation','Besoin d’un bilan avant un autre traitement dentaire'],
        'treatment_title':'Quels soins sont réalisés au cabinet ?','treatment_paras':['La prise en charge commence par un examen clinique afin d’identifier les besoins prioritaires. Selon la situation, le traitement peut comprendre un détartrage, le traitement d’une carie, une obturation ou un suivi préventif.','L’objectif est de conserver les dents naturelles aussi longtemps que possible et de traiter les problèmes avant qu’ils ne deviennent plus complexes. Le plan de soins est expliqué au patient avant toute intervention.'],
        'steps':['Examen et identification des besoins','Explication du diagnostic et des options de traitement','Réalisation du soin indiqué','Conseils d’hygiène et contrôle si nécessaire'],
        'faqs':[('À quelle fréquence faut-il consulter un dentiste ?','La fréquence dépend de votre état bucco-dentaire, de vos antécédents et de vos facteurs de risque. Le dentiste peut recommander un rythme de contrôle adapté à votre situation.'),('Un détartrage abîme-t-il les dents ?','Lorsqu’il est réalisé correctement, le détartrage vise à retirer le tartre accumulé sur les dents et autour des gencives. Il ne consiste pas à retirer l’émail.'),('Comment savoir si une carie doit être traitée ?','Une carie peut parfois être asymptomatique. Un examen dentaire permet d’évaluer sa profondeur et de déterminer le traitement adapté.'),('Peut-on prendre rendez-vous directement sur WhatsApp ?','Oui. Le bouton WhatsApp ouvre directement la conversation avec le cabinet, sans message prérempli.')]
    },
    {
        'name':'Chirurgie dentaire','slug':'chirurgie-dentaire-tanger','h1':'Chirurgie dentaire à Tanger','title':'Chirurgie dentaire à Tanger | Centre Dentaire Venezuela',
        'meta':'Chirurgie dentaire à Tanger : extractions, frénectomies, gingivectomies et actes chirurgicaux au Centre Dentaire Venezuela.',
        'eyebrow':'Chirurgien-dentiste à Tanger','intro':'Le Centre Dentaire Venezuela à Tanger prend en charge différents actes de chirurgie dentaire, notamment les extractions, les frénectomies, les gingivectomies et la chirurgie implantaire, selon le diagnostic et les indications cliniques.',
        'keywords':['chirurgie dentaire Tanger','extraction dentaire Tanger','chirurgien dentiste Tanger','frénectomie Tanger','gingivectomie Tanger'],
        'when_title':'Dans quels cas une chirurgie dentaire peut-elle être indiquée ?','when_items':['Dent qui ne peut pas être conservée et nécessite une extraction','Situation nécessitant un acte sur les tissus mous de la bouche','Indication de frénectomie ou de gingivectomie','Projet de remplacement d’une dent par implant','Besoin d’une évaluation chirurgicale après examen dentaire'],
        'treatment_title':'Quels actes chirurgicaux sont proposés ?','treatment_paras':['Les actes chirurgicaux sont planifiés après un examen clinique. Selon la situation, la prise en charge peut comprendre une extraction dentaire, une frénectomie, une gingivectomie ou une intervention liée à l’implantologie.','Le choix de l’acte dépend du diagnostic, de l’état des tissus et du projet de traitement global. Le déroulement, les suites attendues et les précautions post-opératoires sont expliqués avant l’intervention.'],
        'steps':['Consultation et diagnostic','Planification de l’intervention','Réalisation de l’acte sous anesthésie locale adaptée','Consignes post-opératoires et contrôle'],
        'faqs':[('Une extraction dentaire est-elle toujours nécessaire quand une dent est très abîmée ?','Non. La possibilité de conserver la dent doit d’abord être évaluée. L’extraction est proposée lorsqu’elle est indiquée après examen.'),('Qu’est-ce qu’une frénectomie ?','La frénectomie est un acte chirurgical qui consiste à intervenir sur un frein buccal lorsque sa position ou sa tension pose une indication clinique.'),('Qu’est-ce qu’une gingivectomie ?','La gingivectomie consiste à retirer une partie de tissu gingival dans certaines indications. La décision se fait après évaluation clinique.'),('Comment se passe le suivi après une chirurgie dentaire ?','Des consignes sont données après l’intervention et un contrôle peut être programmé selon l’acte réalisé et l’évolution.')]
    },
    {
        'name':'Dentisterie esthétique','slug':'dentisterie-esthetique-tanger','h1':'Dentisterie esthétique à Tanger','title':'Dentisterie esthétique à Tanger | Centre Dentaire Venezuela',
        'meta':'Dentisterie esthétique à Tanger : blanchiment, facettes composite ou céramique, couronnes et bridges au Centre Dentaire Venezuela.',
        'eyebrow':'Sourire et esthétique dentaire à Tanger','intro':'Au Centre Dentaire Venezuela à Tanger, la dentisterie esthétique vise à améliorer la couleur, la forme, l’harmonie ou la restauration du sourire avec des solutions adaptées à chaque situation : blanchiment, facettes en composite ou en céramique, couronnes et bridges.',
        'keywords':['dentiste esthétique Tanger','blanchiment dentaire Tanger','facettes dentaires Tanger','facettes céramique Tanger','facettes composite Tanger','couronne dentaire Tanger','bridge dentaire Tanger'],
        'when_title':'Quels objectifs peut traiter la dentisterie esthétique ?','when_items':['Dents colorées ou teinte jugée trop foncée','Forme ou proportions dentaires à harmoniser','Dent antérieure abîmée ou restaurée de façon visible','Projet de facettes en composite ou en céramique','Besoin de couronne ou de bridge dans un projet esthétique et fonctionnel'],
        'treatment_title':'Blanchiment, facettes, couronnes et bridges','treatment_paras':['Le blanchiment vise à éclaircir la teinte des dents lorsque l’indication est adaptée. Les facettes permettent de modifier l’apparence de certaines dents avec une approche en composite ou en céramique selon le cas.','Les couronnes et bridges peuvent intervenir lorsqu’une restauration plus importante est nécessaire. Avant tout traitement esthétique, l’état des dents et des gencives doit être évalué afin de choisir une solution compatible avec la santé bucco-dentaire.'],
        'steps':['Analyse du sourire et de la situation dentaire','Discussion du résultat recherché et des options possibles','Choix du traitement adapté','Réalisation puis contrôles si nécessaire'],
        'faqs':[('Quelle est la différence entre facette composite et facette céramique ?','Les deux techniques utilisent des matériaux différents et répondent à des indications différentes. Le choix dépend notamment de la situation dentaire, du résultat recherché et du plan de traitement.'),('Le blanchiment fonctionne-t-il sur les couronnes et les facettes ?','Le blanchiment agit sur les dents naturelles. Les restaurations existantes ne réagissent pas de la même manière, ce qui doit être pris en compte dans le plan esthétique.'),('Peut-on faire des facettes sur toutes les dents ?','Une indication de facettes doit être évaluée dent par dent. L’état de l’émail, des gencives et de l’occlusion influence le choix du traitement.'),('Quel traitement choisir pour améliorer son sourire ?','Le traitement dépend du problème principal : couleur, forme, position, usure, dent manquante ou restauration existante. Une consultation permet de définir la stratégie adaptée.')]
    },
    {
        'name':'Endodontie','slug':'endodontie-tanger','h1':'Endodontie à Tanger','title':'Endodontie à Tanger | Traitement de canal | Centre Dentaire Venezuela',
        'meta':'Endodontie à Tanger : traitement de canal et prise en charge des dents atteintes en profondeur au Centre Dentaire Venezuela.',
        'eyebrow':'Traitement de canal à Tanger','intro':'L’endodontie traite l’intérieur de la dent lorsque la pulpe est atteinte par une carie profonde, une infection ou un traumatisme. Au Centre Dentaire Venezuela à Tanger, le traitement de canal vise à conserver une dent qui pourrait autrement devoir être extraite.',
        'keywords':['endodontie Tanger','traitement de canal Tanger','dévitalisation Tanger','mal de dent Tanger','carie profonde Tanger'],
        'when_title':'Quand un traitement de canal peut-il être nécessaire ?','when_items':['Carie profonde proche ou au contact de la pulpe','Douleur dentaire persistante ou spontanée','Sensibilité importante et durable au chaud ou au froid','Infection d’origine dentaire','Dent traumatisée avec atteinte pulpaire'],
        'treatment_title':'En quoi consiste un traitement endodontique ?','treatment_paras':['Le traitement endodontique consiste à accéder à l’intérieur de la dent, nettoyer et désinfecter le système canalaire puis l’obturer afin de limiter la persistance ou la récidive de l’infection.','Après le traitement de canal, la dent doit être restaurée de manière adaptée à la quantité de tissu dentaire restante. Selon la situation, une restauration directe ou une solution prothétique peut être discutée.'],
        'steps':['Diagnostic de la dent concernée','Accès et nettoyage des canaux','Désinfection et obturation du système canalaire','Restauration et contrôle de la dent'],
        'faqs':[('Un traitement de canal permet-il de garder la dent ?','Son objectif principal est précisément de traiter l’intérieur de la dent afin de permettre sa conservation lorsque cela est possible.'),('Une dent dévitalisée est-elle morte ?','La pulpe n’est plus présente après le traitement endodontique, mais la dent reste intégrée à l’arcade et peut continuer à assurer sa fonction lorsqu’elle est correctement restaurée.'),('Pourquoi une dent peut-elle encore être sensible après le traitement ?','Une sensibilité transitoire peut survenir après un traitement endodontique. Sa durée et son intensité varient selon la situation. Une douleur importante ou persistante doit être signalée au dentiste.'),('Faut-il toujours poser une couronne après un traitement de canal ?','Pas systématiquement. Le choix de la restauration dépend notamment de la dent concernée et de la quantité de structure dentaire restante.')]
    },
    {
        'name':'Parodontologie','slug':'parodontologie-tanger','h1':'Parodontologie à Tanger','title':'Parodontologie à Tanger | Soins des gencives | Centre Dentaire Venezuela',
        'meta':'Parodontologie à Tanger : prise en charge des gencives qui saignent, inflammation et déchaussement au Centre Dentaire Venezuela.',
        'eyebrow':'Soins des gencives à Tanger','intro':'La parodontologie concerne les tissus qui soutiennent les dents, notamment les gencives et l’os. Au Centre Dentaire Venezuela à Tanger, une évaluation parodontale peut être proposée en cas de saignement, inflammation, rétraction gingivale, mobilité ou suspicion de maladie parodontale.',
        'keywords':['parodontologie Tanger','gencives qui saignent Tanger','parodontite Tanger','déchaussement dentaire Tanger','soins gencives Tanger'],
        'when_title':'Quels signes doivent faire consulter pour les gencives ?','when_items':['Saignement lors du brossage ou spontanément','Gencives rouges, gonflées ou douloureuses','Rétraction des gencives ou impression de dents plus longues','Mauvaise haleine persistante associée à une inflammation gingivale','Mobilité dentaire ou suspicion de déchaussement'],
        'treatment_title':'Comment les problèmes parodontaux sont-ils pris en charge ?','treatment_paras':['La première étape consiste à évaluer l’état des gencives et des tissus de soutien. Selon le diagnostic, le plan de traitement peut inclure des mesures d’hygiène, un nettoyage adapté et un suivi parodontal.','Certaines situations peuvent nécessiter des actes complémentaires, notamment sur les tissus gingivaux, lorsque l’indication est posée. Le traitement dépend toujours de la sévérité et de l’étendue du problème.'],
        'steps':['Examen des gencives et des tissus de soutien','Identification des facteurs d’inflammation','Traitement adapté à la situation','Suivi et maintien parodontal'],
        'faqs':[('Pourquoi mes gencives saignent-elles au brossage ?','Le saignement peut être lié à une inflammation gingivale, mais d’autres facteurs sont possibles. Un examen permet d’en rechercher la cause.'),('Une parodontite peut-elle faire bouger les dents ?','Une atteinte parodontale avancée peut toucher les tissus qui maintiennent les dents et entraîner une mobilité. Plus le diagnostic est précoce, plus la prise en charge peut être adaptée.'),('Le détartrage suffit-il toujours pour traiter les gencives ?','Non. Le traitement dépend de la profondeur et de l’étendue de l’atteinte. Un simple détartrage n’est pas nécessairement suffisant dans toutes les situations.'),('Peut-on stabiliser une maladie parodontale ?','Une prise en charge et un suivi adaptés peuvent aider à contrôler la maladie. Le pronostic dépend notamment de sa sévérité, de l’hygiène et des facteurs de risque individuels.')]
    },
    {
        'name':'Orthodontie','slug':'orthodontie-tanger','h1':'Orthodontie à Tanger','title':'Orthodontie à Tanger | Bagues & aligneurs invisibles | Centre Dentaire Venezuela',
        'meta':'Orthodontie à Tanger : traitements multi-bagues et aligneurs invisibles pour corriger l’alignement et les malocclusions.',
        'eyebrow':'Bagues et aligneurs invisibles à Tanger','intro':'Le Centre Dentaire Venezuela à Tanger propose des traitements orthodontiques par multi-bagues et par aligneurs invisibles afin de corriger l’alignement des dents et certaines malocclusions, selon le diagnostic orthodontique.',
        'keywords':['orthodontie Tanger','orthodontiste Tanger','bagues dentaires Tanger','appareil dentaire Tanger','aligneurs invisibles Tanger','gouttières orthodontiques Tanger'],
        'when_title':'Pourquoi consulter pour un traitement orthodontique ?','when_items':['Dents chevauchées ou mal alignées','Espaces entre les dents','Décalage entre les arcades ou malocclusion','Projet de traitement multi-bagues','Recherche d’une solution par aligneurs invisibles lorsque l’indication le permet'],
        'treatment_title':'Multi-bagues ou aligneurs invisibles : quelle différence ?','treatment_paras':['Le traitement multi-bagues utilise un dispositif fixe permettant de déplacer progressivement les dents. Les aligneurs invisibles sont des gouttières amovibles successives utilisées dans certaines indications orthodontiques.','Le choix entre ces solutions dépend de la nature des mouvements nécessaires, de la malocclusion, de la coopération du patient et des objectifs du traitement. Une évaluation orthodontique est nécessaire avant de choisir la technique.'],
        'steps':['Bilan orthodontique et diagnostic','Définition des objectifs de correction','Choix entre multi-bagues ou aligneurs si les deux options sont possibles','Suivi régulier jusqu’à la fin du traitement'],
        'faqs':[('Les aligneurs invisibles conviennent-ils à tous les cas ?','Non. Leur indication dépend du type et de l’importance des mouvements dentaires nécessaires. Certains cas peuvent être mieux adaptés à un traitement multi-bagues.'),('Combien de temps dure un traitement orthodontique ?','La durée varie selon le problème à corriger, la technique utilisée et la réponse au traitement. Une estimation est donnée après le bilan.'),('Quelle est la différence entre bagues et aligneurs ?','Les bagues sont un dispositif fixe. Les aligneurs sont amovibles et doivent être portés selon les consignes pour être efficaces.'),('L’orthodontie sert-elle uniquement à l’esthétique ?','Non. L’alignement dentaire et l’occlusion ont aussi une dimension fonctionnelle. Le plan de traitement tient compte de l’ensemble de la situation.')]
    }
]

all_services = services + [{'name':'Implantologie','slug':'implant-dentaire-tanger'}]

CSS = r'''
:root{--ink:#143b3e;--teal:#8abdb8;--teal2:#c3dfdc;--deep:#2f6d6b;--soft:#8fb5b1;--gold:#e5bd8c;--paper:#fbfcfb;--white:#fff;--muted:#5d7d7c;--line:rgba(20,59,62,.11);--font:"Avenir Next","Helvetica Neue",Arial,sans-serif;--nav:68px;--gutter:4.6%}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}.wrap{max-width:1180px;margin:auto;padding:0 22px}.top{position:sticky;top:0;z-index:30;height:var(--nav);background:rgba(255,255,255,.95);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}.top .wrap{height:100%;display:flex;align-items:center;justify-content:space-between;gap:28px}.brand{display:flex;flex-direction:column;gap:4px;line-height:1}.brand small{font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--soft)}.brand b{font-size:17px;letter-spacing:.12em;text-transform:uppercase;color:var(--deep);font-weight:500}.nav{display:flex;gap:24px;align-items:center;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.nav a:hover{color:var(--deep)}.nav .cta{padding:11px 16px;border-radius:10px;background:var(--teal);color:white}.hero{margin:18px 1.1vw 0;border-radius:32px;overflow:hidden;background:linear-gradient(125deg,#143b3e 0%,#2f6d6b 54%,#8abdb8 100%);color:white}.hero .wrap{padding-top:70px;padding-bottom:70px}.crumb{font-size:11px;color:rgba(255,255,255,.72);margin-bottom:22px}.crumb a{text-decoration:underline;text-underline-offset:3px}.pill{display:inline-flex;padding:7px 11px;border:1px solid rgba(255,255,255,.24);border-radius:999px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:22px;background:rgba(255,255,255,.08)}h1{font-size:clamp(42px,6vw,76px);line-height:1.02;font-weight:300;margin:0;max-width:880px;letter-spacing:.005em}.hero p{max-width:760px;font-size:17px;line-height:1.7;color:rgba(255,255,255,.9);margin:22px 0 0}.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}.btn{display:inline-flex;align-items:center;justify-content:center;padding:14px 20px;border-radius:12px;font-weight:700;font-size:13px}.btn-primary{background:var(--white);color:var(--ink)}.btn-secondary{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.25);color:white}.main{padding:66px 0}.grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(280px,.75fr);gap:44px;align-items:start}.content h2{font-size:clamp(28px,3vw,40px);font-weight:350;line-height:1.18;margin:54px 0 16px}.content h2:first-child{margin-top:0}.content p,.content li{font-size:15.5px;line-height:1.78;color:#4f6f6e}.content ul{padding-left:20px}.introbox{padding:24px;border:1px solid var(--line);border-radius:20px;background:white}.introbox strong{display:block;font-size:13px;margin-bottom:10px}.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{padding:7px 10px;border-radius:999px;background:#eef6f5;color:var(--deep);font-size:11.5px}.steps{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.step{padding:20px;border-radius:18px;background:white;border:1px solid var(--line)}.step b{display:block;color:var(--gold);font-size:12px;margin-bottom:7px}.step span{font-size:14px;line-height:1.5}.faq details{border-top:1px solid var(--line);padding:18px 0}.faq details:last-child{border-bottom:1px solid var(--line)}.faq summary{cursor:pointer;font-weight:650;font-size:15px}.faq p{margin-bottom:0}.side{position:sticky;top:94px}.card{background:white;border:1px solid var(--line);border-radius:22px;padding:22px;box-shadow:0 16px 38px rgba(20,59,62,.06)}.card+.card{margin-top:16px}.card h3{font-size:16px;margin:0 0 15px}.contactline{display:block;padding:11px 0;border-top:1px solid var(--line);font-size:13px;line-height:1.45}.contactline:first-of-type{border-top:0}.contactline small{display:block;color:#7d9997;margin-bottom:2px}.contactline b{font-weight:650}.contactline:hover b{color:var(--deep)}.related{display:flex;flex-wrap:wrap;gap:8px}.related a{font-size:11.5px;padding:8px 10px;border-radius:999px;background:#eef6f5;color:var(--deep)}.local{margin-top:58px;padding:30px;border-radius:24px;background:#eef6f5}.local h2{margin-top:0}.local p{margin-bottom:0}.foot{background:var(--ink);color:white;margin-top:56px}.foot .wrap{padding-top:36px;padding-bottom:36px;display:flex;justify-content:space-between;gap:24px;align-items:center}.foot p{margin:0;font-size:12px;color:rgba(255,255,255,.7)}.foot a{font-size:12px;color:var(--teal2)}
@media(max-width:850px){.nav a:not(.cta){display:none}.grid{grid-template-columns:1fr}.side{position:static}.steps{grid-template-columns:1fr}.hero .wrap{padding-top:52px;padding-bottom:52px}.foot .wrap{flex-direction:column;align-items:flex-start}}
@media(max-width:560px){.wrap{padding-left:18px;padding-right:18px}.hero{border-radius:24px;margin-left:8px;margin-right:8px}.hero p{font-size:15px}.actions{flex-direction:column}.btn{width:100%}.main{padding-top:44px}.content h2{margin-top:42px}}
'''

def schema_for(s):
    url = f"{ROOT}/{s['slug']}/"
    graph = {
        '@context':'https://schema.org','@graph':[
            {'@type':'WebPage','@id':url+'#webpage','url':url,'name':s['title'],'description':s['meta'],'inLanguage':'fr-MA','isPartOf':{'@id':ROOT+'/#website'},'about':{'@id':url+'#service'}},
            {'@type':'WebSite','@id':ROOT+'/#website','url':ROOT+'/','name':'Centre Dentaire Venezuela','inLanguage':'fr-MA'},
            {'@type':'Service','@id':url+'#service','name':s['h1'],'serviceType':s['name'],'url':url,'description':s['intro'],'provider':{'@id':CLINIC_ID},'areaServed':{'@type':'City','name':'Tanger'},'mainEntityOfPage':{'@id':url+'#webpage'}},
            {'@type':'Dentist','@id':CLINIC_ID,'name':'Centre Dentaire Venezuela','url':ROOT+'/','telephone':clinic['phone'],'email':clinic['email'],'address':{'@type':'PostalAddress','streetAddress':'4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair','addressLocality':'Tanger','postalCode':'90000','addressCountry':'MA'},'geo':{'@type':'GeoCoordinates','latitude':35.7781833,'longitude':-5.8165155},'hasMap':clinic['maps'],'sameAs':[clinic['instagram'],clinic['maps']],'employee':{'@type':'Person','name':'Dr Majda Laasraoui','jobTitle':'Chirurgienne-dentiste','knowsLanguage':['français','arabe','anglais','espagnol']}},
            {'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Accueil','item':ROOT+'/'},{'@type':'ListItem','position':2,'name':s['name'],'item':url}]}
        ]
    }
    return json.dumps(graph, ensure_ascii=False, separators=(',',':'))

def page_html(s):
    url = f"{ROOT}/{s['slug']}/"
    kw = ''.join(f'<span class="chip">{x}</span>' for x in s['keywords'])
    when = ''.join(f'<li>{x}</li>' for x in s['when_items'])
    paras = ''.join(f'<p>{x}</p>' for x in s['treatment_paras'])
    steps = ''.join(f'<div class="step"><b>Étape {i}</b><span>{x}</span></div>' for i,x in enumerate(s['steps'],1))
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in s['faqs'])
    related = ''.join(f'<a href="/{x["slug"]}/">{x["name"]}</a>' for x in all_services if x['slug'] != s['slug'])
    return f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['meta']}">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_MA"><meta property="og:site_name" content="Centre Dentaire Venezuela"><meta property="og:title" content="{s['title']}"><meta property="og:description" content="{s['meta']}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ROOT}/assets/images/hero-poster-cabinet-dentaire-venezuela-tanger.webp"><meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style><script type="application/ld+json">{schema_for(s)}</script></head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="/"><small>Cabinet dentaire</small><b>Venezuela</b></a><nav class="nav" aria-label="Navigation"><a href="/">Accueil</a><a href="/#soins">Nos soins</a><a href="/#localisation">Localisation</a><a class="cta" href="/#rdv">Prendre RDV</a></nav></div></header>
<main>
<section class="hero"><div class="wrap"><div class="crumb"><a href="/">Accueil</a> / {s['name']}</div><span class="pill">{s['eyebrow']}</span><h1>{s['h1']}</h1><p>{s['intro']}</p><div class="actions"><a class="btn btn-primary" href="tel:{clinic['phone']}">Appeler le cabinet</a><a class="btn btn-secondary" href="https://wa.me/{clinic['whatsapp'].replace('+','')}" target="_blank" rel="noopener">WhatsApp</a></div></div></section>
<section class="main"><div class="wrap grid"><article class="content"><div class="introbox"><strong>Recherches liées à ce soin à Tanger</strong><div class="chips">{kw}</div></div>
<h2>{s['when_title']}</h2><ul>{when}</ul>
<h2>{s['treatment_title']}</h2>{paras}
<h2>Comment se déroule la prise en charge ?</h2><div class="steps">{steps}</div>
<h2>Questions fréquentes sur {s['name'].lower()} à Tanger</h2><div class="faq">{faq}</div>
<div class="local"><h2>Centre Dentaire Venezuela à Tanger</h2><p>Le cabinet se situe au {clinic['address']}. Les consultations sont proposées en français, arabe, anglais et espagnol. Pour ce soin, un diagnostic clinique est nécessaire avant de confirmer l’indication, la technique et le plan de traitement.</p></div>
</article>
<aside class="side"><div class="card"><h3>Coordonnées du cabinet</h3><a class="contactline" href="{clinic['maps']}" target="_blank" rel="noopener"><small>Adresse</small><b>{clinic['address']}</b></a><a class="contactline" href="tel:{clinic['phone']}"><small>Téléphone</small><b>{clinic['phone_display']}</b></a><a class="contactline" href="https://wa.me/{clinic['whatsapp'].replace('+','')}" target="_blank" rel="noopener"><small>WhatsApp</small><b>{clinic['whatsapp_display']}</b></a><a class="contactline" href="mailto:{clinic['email']}"><small>Email</small><b>{clinic['email']}</b></a></div><div class="card"><h3>Autres soins</h3><div class="related">{related}</div></div></aside></div></section>
</main><footer class="foot"><div class="wrap"><p>© Centre Dentaire Venezuela · Tanger</p><a href="{clinic['maps']}" target="_blank" rel="noopener">Voir sur Google Maps</a></div></footer>
</body></html>'''

for s in services:
    p = Path(s['slug']) / 'index.html'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(page_html(s), encoding='utf-8')

# Update homepage internal links and service schema.
home = Path('index.html')
h = home.read_text(encoding='utf-8')
for s in services:
    desc_map = {
        'Soins dentaires généraux':'Détartrage, caries, contrôles réguliers : le suivi qui garde votre bouche saine année après année.',
        'Chirurgie dentaire':'Extractions et interventions délicates, menées dans un cadre stérile et sous anesthésie maîtrisée.',
        'Dentisterie esthétique':'Blanchiment, facettes, harmonisation : votre sourire retravaillé sans jamais perdre son naturel.',
        'Endodontie':'Le traitement des canaux, pour éteindre la douleur et garder votre dent plutôt que de l’extraire.',
        'Parodontologie':'Gencives qui saignent ou se rétractent : on traite le tissu qui tient vos dents en place.',
        'Orthodontie':'Traitements multi-bagues et aligneurs invisibles pour corriger l’alignement des dents et les malocclusions.'
    }
    needle = f'''            <h3>{s['name']}</h3>\n            <p>{desc_map[s['name']]}</p>'''
    link = f'''            <h3>{s['name']}</h3>\n            <p>{desc_map[s['name']]}</p>\n            <a class="soin-more" href="/{s['slug']}/" aria-label="Découvrir notre page {s['h1']}">Découvrir le traitement <span aria-hidden="true">→</span></a>'''
    if needle in h and f'href="/{s["slug"]}/"' not in h[h.find(needle):h.find(needle)+600]:
        h = h.replace(needle, link, 1)
    h = h.replace(f'<a href="#soins">{s["name"]}</a>', f'<a href="/{s["slug"]}/">{s["name"]}</a>', 1)

schema_names = {
'Soins dentaires généraux':'Soins dentaires généraux et détartrage',
'Chirurgie dentaire':'Chirurgie dentaire et extractions',
'Dentisterie esthétique':'Dentisterie esthétique : blanchiment et facettes',
'Endodontie':'Endodontie et traitement de canal',
'Parodontologie':'Parodontologie et soins des gencives',
'Orthodontie':'Orthodontie et alignement dentaire'
}
for s in services:
    old = f'{{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "{schema_names[s["name"]]}"}}}},'
    new = f'{{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "{schema_names[s["name"]]}", "url": "{ROOT}/{s["slug"]}/"}}}},'
    if old in h:
        h = h.replace(old,new,1)
home.write_text(h,encoding='utf-8')

# Update sitemap with homepage + all seven service pages.
urls = [ROOT + '/'] + [f"{ROOT}/{s['slug']}/" for s in services] + [ROOT + '/implant-dentaire-tanger/']
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap += ['  <url>',f'    <loc>{u}</loc>',f'    <lastmod>{TODAY}</lastmod>','  </url>']
sitemap.append('</urlset>')
Path('sitemap.xml').write_text('\n'.join(sitemap)+'\n',encoding='utf-8')
