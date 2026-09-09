from pathlib import Path
import shutil


def replace_once(path, old, new, label):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'Missing pattern for {label} in {path}')
    text = text.replace(old, new, 1)
    p.write_text(text, encoding='utf-8')
    print(f'OK: {label}')

# 2) Clarify homepage intent vs generic service page.
replace_once(
    'index.html',
    '<h2 class="section-title" id="soins-title">Nos soins dentaires<br><span class="accent-teal">à Tanger</span></h2>',
    '<h2 class="section-title" id="soins-title">Nos traitements dentaires<br><span class="accent-teal">à Tanger</span></h2>',
    'homepage treatments H2'
)

# 12) Absolute Open Graph image URL on homepage.
replace_once(
    'index.html',
    '<meta property="og:image" content="assets/images/hero-poster-cabinet-dentaire-venezuela-tanger.webp">',
    '<meta property="og:image" content="https://centredentairevenezuela.com/assets/images/hero-poster-cabinet-dentaire-venezuela-tanger.webp">',
    'homepage absolute og:image'
)

# 7) Complete Orthodontie offer URL in homepage structured data.
replace_once(
    'index.html',
    '{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Orthodontie et alignement dentaire"}}',
    '{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Orthodontie et alignement dentaire", "url": "https://centredentairevenezuela.com/orthodontie-tanger/"}}',
    'orthodontie schema URL'
)

# 7) Remove static aggregateRating so it cannot become stale/inaccurate.
replace_once(
    'index.html',
    '  ],\n  "aggregateRating": {\n    "@type": "AggregateRating",\n    "ratingValue": "5",\n    "bestRating": "5",\n    "reviewCount": "50"\n  }\n}',
    '  ]\n}',
    'remove static aggregateRating'
)

# 4) Add contextual internal links across service content.
replace_once(
    'soins-dentaires-tanger/index.html',
    '<p>L’objectif est de conserver les dents naturelles aussi longtemps que possible et de traiter les problèmes avant qu’ils ne deviennent plus complexes. Le plan de soins est expliqué au patient avant toute intervention.</p>',
    '<p>L’objectif est de conserver les dents naturelles aussi longtemps que possible et de traiter les problèmes avant qu’ils ne deviennent plus complexes. Le plan de soins est expliqué au patient avant toute intervention. Lorsqu’une carie atteint la pulpe, un <a href="/endodontie-tanger/">traitement endodontique</a> peut devenir nécessaire.</p>',
    'soins to endodontie contextual link'
)

replace_once(
    'chirurgie-dentaire-tanger/index.html',
    '<li>Projet de remplacement d’une dent par implant</li>',
    '<li>Projet de remplacement d’une dent par <a href="/implant-dentaire-tanger/">implant dentaire</a></li>',
    'chirurgie to implant contextual link'
)

replace_once(
    'dentisterie-esthetique-tanger/index.html',
    'Avant tout traitement esthétique, l’état des dents et des gencives doit être évalué afin de choisir une solution compatible avec la santé bucco-dentaire.',
    'Avant tout traitement esthétique, l’état des dents et des <a href="/parodontologie-tanger/">gencives</a> doit être évalué afin de choisir une solution compatible avec la santé bucco-dentaire.',
    'esthetique to parodontologie contextual link'
)
replace_once(
    'dentisterie-esthetique-tanger/index.html',
    'Le traitement dépend du problème principal : couleur, forme, position, usure, dent manquante ou restauration existante.',
    'Le traitement dépend du problème principal : couleur, forme, <a href="/orthodontie-tanger/">position des dents</a>, usure, <a href="/implant-dentaire-tanger/">dent manquante</a> ou restauration existante.',
    'esthetique to orthodontie and implant contextual links'
)

replace_once(
    'endodontie-tanger/index.html',
    '<p>Le traitement endodontique consiste à accéder à l’intérieur de la dent, nettoyer et désinfecter le système canalaire puis l’obturer afin de limiter la persistance ou la récidive de l’infection.</p>',
    '<p>Le traitement endodontique consiste à accéder à l’intérieur de la dent, nettoyer et désinfecter le système canalaire puis l’obturer afin de limiter la persistance ou la récidive de l’infection. Une carie moins profonde peut relever des <a href="/soins-dentaires-tanger/">soins dentaires généraux</a>.</p>',
    'endodontie to general care contextual link'
)
replace_once(
    'endodontie-tanger/index.html',
    'Pas systématiquement. Le choix de la restauration dépend notamment de la dent concernée et de la quantité de structure dentaire restante.',
    'Pas systématiquement. Le choix de la restauration, notamment une <a href="/dentisterie-esthetique-tanger/">couronne dentaire</a> lorsque celle-ci est indiquée, dépend de la dent concernée et de la quantité de structure dentaire restante.',
    'endodontie to esthetique contextual link'
)

replace_once(
    'parodontologie-tanger/index.html',
    '<p>Certaines situations peuvent nécessiter des actes complémentaires, notamment sur les tissus gingivaux, lorsque l’indication est posée. Le traitement dépend toujours de la sévérité et de l’étendue du problème.</p>',
    '<p>Certaines situations peuvent nécessiter des actes complémentaires, notamment sur les tissus gingivaux, lorsque l’indication est posée. Certaines interventions relèvent alors de la <a href="/chirurgie-dentaire-tanger/">chirurgie dentaire</a>. Le traitement dépend toujours de la sévérité et de l’étendue du problème.</p>',
    'parodontologie to chirurgie contextual link'
)
replace_once(
    'parodontologie-tanger/index.html',
    'Un simple détartrage n’est pas nécessairement suffisant dans toutes les situations.',
    'Un simple <a href="/soins-dentaires-tanger/">détartrage</a> n’est pas nécessairement suffisant dans toutes les situations.',
    'parodontologie to general care contextual link'
)

replace_once(
    'orthodontie-tanger/index.html',
    '<p>Le choix entre ces solutions dépend de la nature des mouvements nécessaires, de la malocclusion, de la coopération du patient et des objectifs du traitement. Une évaluation orthodontique est nécessaire avant de choisir la technique.</p>',
    '<p>Le choix entre ces solutions dépend de la nature des mouvements nécessaires, de la malocclusion, de la coopération du patient et des objectifs du traitement. Une évaluation orthodontique est nécessaire avant de choisir la technique. Lorsque le projet associe alignement et amélioration du sourire, il peut aussi être coordonné avec la <a href="/dentisterie-esthetique-tanger/">dentisterie esthétique</a>.</p>',
    'orthodontie to esthetique contextual link'
)

# 3 + 4) Implant page: contextual links and a dedicated related-services block.
replace_once(
    'implant-dentaire-tanger/index.html',
    'Après la phase de cicatrisation, il peut recevoir une couronne, un bridge ou participer à la stabilisation d’une prothèse selon le cas.',
    'Après la phase de cicatrisation, il peut recevoir une <a href="/dentisterie-esthetique-tanger/">couronne</a>, un bridge ou participer à la stabilisation d’une prothèse selon le cas.',
    'implant to esthetique contextual link'
)
replace_once(
    'implant-dentaire-tanger/index.html',
    'La décision de poser un implant se prend après avoir évalué la gencive, l’occlusion, le volume osseux, les dents adjacentes et les facteurs médicaux pouvant influencer la cicatrisation.',
    'La décision de poser un implant se prend après avoir évalué la <a href="/parodontologie-tanger/">santé des gencives</a>, l’occlusion, le volume osseux, les dents adjacentes et les facteurs médicaux pouvant influencer la cicatrisation.',
    'implant to parodontologie contextual link'
)
replace_once(
    'implant-dentaire-tanger/index.html',
    '<article class="step"><span class="step-num">03</span><h3>Phase chirurgicale</h3><p>L’implant est placé sous anesthésie locale lorsque les conditions sont réunies. Les consignes postopératoires sont ensuite expliquées.</p></article>',
    '<article class="step"><span class="step-num">03</span><h3>Phase chirurgicale</h3><p>La pose de l’implant fait partie de la <a href="/chirurgie-dentaire-tanger/">chirurgie dentaire</a> et est réalisée sous anesthésie locale lorsque les conditions sont réunies. Les consignes postopératoires sont ensuite expliquées.</p></article>',
    'implant to chirurgie contextual link'
)

implant_related_css = '.related-care{display:flex;flex-wrap:wrap;gap:10px}.related-care a{display:inline-flex;padding:10px 13px;border-radius:999px;background:#eef6f5;color:var(--teal-deep);font-size:12.5px;font-weight:700}.related-care a:hover{background:#e1efed}\n'
replace_once(
    'implant-dentaire-tanger/index.html',
    '.disclaimer{margin-top:26px;padding:17px 19px;border-radius:16px;background:#f7fbfa;border:1px solid var(--line);font-size:12px;line-height:1.65;color:#718d8b}\n.footer{background:#102f31;color:#fff}',
    implant_related_css + '.disclaimer{margin-top:26px;padding:17px 19px;border-radius:16px;background:#f7fbfa;border:1px solid var(--line);font-size:12px;line-height:1.65;color:#718d8b}\n.footer{background:#102f31;color:#fff}',
    'implant related care CSS'
)

related_section = '''<section class="section alt">\n  <div class="inner">\n    <div class="section-head">\n      <span class="kicker">Soins associés</span>\n      <h2>Découvrir les autres <span class="accent">soins dentaires</span></h2>\n      <p class="lead">Selon votre situation, un projet implantaire peut s’inscrire dans une prise en charge plus globale.</p>\n    </div>\n    <div class="related-care">\n      <a href="/soins-dentaires-tanger/">Soins dentaires généraux</a>\n      <a href="/chirurgie-dentaire-tanger/">Chirurgie dentaire</a>\n      <a href="/dentisterie-esthetique-tanger/">Dentisterie esthétique</a>\n      <a href="/endodontie-tanger/">Endodontie</a>\n      <a href="/parodontologie-tanger/">Parodontologie</a>\n      <a href="/orthodontie-tanger/">Orthodontie</a>\n    </div>\n  </div>\n</section>\n\n'''
replace_once(
    'implant-dentaire-tanger/index.html',
    '<section class="section" id="contact">',
    related_section + '<section class="section" id="contact">',
    'implant related services section'
)

# Make contextual links visibly identifiable on the six compact service pages.
for path in [
    'soins-dentaires-tanger/index.html',
    'chirurgie-dentaire-tanger/index.html',
    'dentisterie-esthetique-tanger/index.html',
    'endodontie-tanger/index.html',
    'parodontologie-tanger/index.html',
    'orthodontie-tanger/index.html',
]:
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    marker = '.content ul{padding-left:20px}'
    if '.content p a,.content li a{' not in text:
        if marker not in text:
            raise SystemExit(f'Missing CSS marker in {path}')
        text = text.replace(marker, marker + '.content p a,.content li a{color:var(--deep);text-decoration:underline;text-underline-offset:3px}', 1)
        p.write_text(text, encoding='utf-8')
        print(f'OK: contextual link CSS in {path}')

# 9) Keep project documentation in the repository but outside the published Pages tree.
target_dir = Path('.github/project-docs')
target_dir.mkdir(parents=True, exist_ok=True)
for src, dest_name in [
    (Path('README.md'), 'README.md'),
    (Path('docs/instructions-projet-centre-dentaire-venezuela.md'), 'instructions-projet-centre-dentaire-venezuela.md'),
]:
    if src.exists():
        dest = target_dir / dest_name
        shutil.copy2(src, dest)
        src.unlink()
        print(f'OK: moved {src} -> {dest}')

try:
    Path('docs').rmdir()
except OSError:
    pass

# All eight indexable pages changed today; refresh sitemap lastmod.
sitemap = Path('sitemap.xml')
s = sitemap.read_text(encoding='utf-8')
s = s.replace('<lastmod>2026-09-08</lastmod>', '<lastmod>2026-09-09</lastmod>')
sitemap.write_text(s, encoding='utf-8')
print('OK: sitemap lastmod updated to 2026-09-09')
