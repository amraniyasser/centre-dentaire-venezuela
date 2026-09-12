from pathlib import Path
import re

ROOT = Path('.')
HTML_FILES = [p for p in ROOT.rglob('*.html') if '.github' not in p.parts]

# Shared shell styles extracted from the canonical blocks already injected on every page.
# The script intentionally moves them to external assets without changing declarations.
def extract_unique_block(pattern, label):
    blocks = []
    for p in HTML_FILES:
        s = p.read_text(encoding='utf-8')
        m = re.search(pattern, s, flags=re.S | re.I)
        if m:
            blocks.append(m.group(1).strip())
    if not blocks:
        raise RuntimeError(f'No {label} block found')
    # Canonical rollout should have made these identical. If not, stop rather than guess.
    first = blocks[0]
    mismatches = [i for i, b in enumerate(blocks[1:], start=2) if b != first]
    if mismatches:
        raise RuntimeError(f'{label} blocks are not identical across pages; refusing automatic cleanup')
    return first

footer_css = extract_unique_block(r'<style id="cv-footer-styles">(.*?)</style>', 'footer CSS')
header_css = extract_unique_block(r'<style id="cv-header-styles">(.*?)</style>', 'header CSS')
header_js = extract_unique_block(r'<script id="cv-header-script">(.*?)</script>', 'header JS')

css_dir = ROOT / 'assets' / 'css'
js_dir = ROOT / 'assets' / 'js'
css_dir.mkdir(parents=True, exist_ok=True)
js_dir.mkdir(parents=True, exist_ok=True)

site_shell_css = '''/* Centre Dentaire Venezuela — shared site shell\n   Canonical header + footer styles. Keep page-specific styles in each page until\n   the next refactor so visual output stays unchanged. */\n\n''' + header_css + '\n\n' + footer_css + '\n'
(css_dir / 'site-shell.css').write_text(site_shell_css, encoding='utf-8')

site_shell_js = '''/* Centre Dentaire Venezuela — shared site shell behavior */\n''' + header_js + '\n'
(js_dir / 'site-shell.js').write_text(site_shell_js, encoding='utf-8')

# Conservative dead-CSS cleanup. Only remove legacy sections with explicit comments or
# old footer/header selectors when the corresponding legacy markup no longer exists.
def remove_dead_legacy_css(s, path):
    body = re.sub(r'<style\b.*?</style>', '', s, flags=re.S | re.I)
    body = re.sub(r'<script\b.*?</script>', '', body, flags=re.S | re.I)

    # Homepage old footer section is explicitly marked and no .footer markup remains.
    if path.as_posix() == 'index.html' and 'class="footer"' not in body:
        s = re.sub(
            r'/\* ==========================================================================\n   12\. Pied de page\n   ========================================================================== \*/.*?(?=/\* ==========================================================================\n   13\.)',
            '', s, flags=re.S)

    # Inner pages historically used .foot markup; canonical footer replaced it.
    if 'class="foot"' not in body:
        s = re.sub(r'\n\.foot\{[^{}]*\}\s*\.foot \.wrap\{[^{}]*\}\s*\.foot p\{[^{}]*\}\s*\.foot a\{[^{}]*\}\s*', '\n', s, flags=re.S)
        s = re.sub(r'\n\s*\.foot \.wrap\{[^{}]*\}', '', s, flags=re.S)

    # Legacy .top header existed on older treatment pages. Remove only the explicitly
    # labelled block before the Hero comment, and only if there is no .top element left.
    if 'class="top"' not in body:
        s = re.sub(
            r'/\* Header[^*]*\*/.*?(?=/\* Hero)',
            '', s, flags=re.S | re.I)

    return s

for p in HTML_FILES:
    s = p.read_text(encoding='utf-8')
    before = s

    # Remove duplicated canonical shell blocks now served from shared assets.
    s = re.sub(r'\s*<style id="cv-footer-styles">.*?</style>\s*', '\n', s, flags=re.S | re.I)
    s = re.sub(r'\s*<style id="cv-header-styles">.*?</style>\s*', '\n', s, flags=re.S | re.I)
    s = re.sub(r'\s*<script id="cv-header-script">.*?</script>\s*', '\n', s, flags=re.S | re.I)

    s = remove_dead_legacy_css(s, p)

    # Add shared assets once.
    if '/assets/css/site-shell.css' not in s:
        s = s.replace('</head>', '<link rel="stylesheet" href="/assets/css/site-shell.css">\n</head>', 1)
    if '/assets/js/site-shell.js' not in s:
        s = s.replace('</body>', '<script src="/assets/js/site-shell.js" defer></script>\n</body>', 1)

    # Minimal whitespace cleanup created by removed blocks.
    s = re.sub(r'\n{4,}', '\n\n\n', s)

    p.write_text(s, encoding='utf-8')

# Remove the self-modifying footer workflow/script. The footer remains canonical in HTML;
# shared styling now lives in assets/css/site-shell.css, avoiding an extra commit on every HTML change.
for obsolete in [
    ROOT / '.github/scripts/standardize_footer.py',
    ROOT / '.github/workflows/standardize-footer-2026-09-11.yml',
]:
    if obsolete.exists():
        obsolete.unlink()

# Update project documentation to reflect the current architecture and workflow.
readme = '''# Centre Dentaire Venezuela — site officiel\n\nSite statique du Centre Dentaire Venezuela à Tanger, publié depuis la branche `main`.\nLe projet reste volontairement simple : HTML, CSS et JavaScript sans framework ni dépendances de build.\n\n## Architecture actuelle\n\n```text\n.\n├── index.html\n├── merci.html\n├── favicon.svg\n├── robots.txt\n├── sitemap.xml\n├── CNAME\n├── assets/\n│   ├── css/\n│   │   └── site-shell.css        # header + footer communs\n│   ├── js/\n│   │   └── site-shell.js         # comportement commun du header\n│   ├── images/\n│   ├── video/\n│   └── sources/                  # sources historiques, non chargées par le site\n├── nos-soins/\n├── soins-dentaires-tanger/\n├── chirurgie-dentaire-tanger/\n├── dentisterie-esthetique-tanger/\n├── blanchiment-dentaire-tanger/\n├── implant-dentaire-tanger/\n├── endodontie-tanger/\n├── parodontologie-tanger/\n├── orthodontie-tanger/\n├── dr-majda-laasraoui-dentiste-tanger/\n├── blog/\n│   └── blanchiment-dentaire-guide/\n├── mentions-legales/\n├── politique-confidentialite/\n└── .github/project-docs/\n```\n\n## Règles de maintenance\n\n- Conserver les URLs existantes et leurs balises canonical.\n- Une seule balise H1 principale par page indexable.\n- Le header et le footer visibles doivent rester cohérents avec la homepage.\n- Les styles communs du header/footer sont dans `assets/css/site-shell.css`. Ne pas recopier ces blocs dans chaque page.\n- Le comportement commun du header est dans `assets/js/site-shell.js`.\n- Les pages de soins gardent leur contenu et leurs styles propres tant qu'aucun refactor visuel n'est demandé.\n- Toute page indexable doit conserver title, meta description, canonical, robots, Open Graph, données structurées pertinentes et FAQ visible lorsque le sujet s'y prête.\n- Toute nouvelle page indexable doit être ajoutée à `sitemap.xml`.\n- Ne pas ajouter de FAQPage schema par défaut.\n- Ne pas afficher de mention publique de l'infrastructure de dépôt/hébergement dans les pages du site.\n\n## Navigation / composants communs\n\nLe header et le footer sont présents directement dans chaque page HTML pour rester compatibles avec un hébergement statique sans moteur de template. Leur CSS et le comportement JavaScript communs sont externalisés dans `assets/css/site-shell.css` et `assets/js/site-shell.js`.\n\nIl n'y a plus de workflow qui réécrit automatiquement tous les footers après chaque modification HTML. Cela évite les commits automatiques en cascade et rend l'historique du dépôt plus lisible. Quand une nouvelle page est créée, copier le header/footer canonique d'une page existante puis utiliser les assets partagés.\n\n## Formulaire de rendez-vous\n\nLe formulaire de la homepage ne dépend pas de Netlify Forms. Il prépare un message WhatsApp à partir des informations saisies et ouvre WhatsApp pour l'envoi.\n\n## SEO\n\nLa base actuelle comprend :\n- `robots.txt` avec référence au sitemap ;\n- `sitemap.xml` ;\n- canonicals ;\n- métadonnées Open Graph/Twitter ;\n- données structurées Dentist / Service / Person / Article selon les pages ;\n- maillage interne entre le hub de soins, les traitements, la praticienne et le blog.\n\n## Coordonnées de référence\n\n- Centre Dentaire Venezuela\n- 4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair, Tanger 90000, Maroc\n- Téléphone : +212 5 31 11 21 27\n- WhatsApp : +212 771 158 018\n- Email : centredentairevenezuela@gmail.com\n- Instagram : https://www.instagram.com/centre.dentaire.venezuela/\n- TikTok : https://www.tiktok.com/@centredentairevenezuela\n\n## Horaires\n\n- Lundi, mercredi, vendredi : 09:30–17:30\n- Mardi, jeudi : 09:30–13:00 et 15:00–18:30\n- Samedi : 10:00–14:00\n- Dimanche : fermé\n\n## Performance\n\nLes principaux médias lourds sont les vidéos. Le hero utilise actuellement la vidéo longue avec `preload=\"auto\"`; la vidéo de présentation utilise `preload=\"metadata\"`. Toute optimisation future des performances doit d'abord mesurer l'impact de ces médias avant de modifier le design.\n\n## Documentation projet\n\nLes règles métier, SEO et éditoriales complémentaires sont dans `.github/project-docs/`.\n'''
(ROOT / '.github/project-docs/README.md').write_text(readme, encoding='utf-8')

# Keep the main project instructions aligned with the new non-self-modifying setup.
rules_path = ROOT / '.github/project-docs/instructions-projet-centre-dentaire-venezuela.md'
if rules_path.exists():
    r = rules_path.read_text(encoding='utf-8')
    r = re.sub(
        r'## Footer canonique — règle obligatoire.*?(?=\n## |\Z)',
        '''## Footer canonique — règle obligatoire\n- Toute nouvelle page HTML doit reprendre exactement le footer canonique déjà présent sur les pages du site.\n- Ne pas créer de variante de footer par page.\n- Les styles du footer sont centralisés dans `/assets/css/site-shell.css` : ne pas les dupliquer inline.\n- Le footer doit toujours afficher le téléphone du cabinet puis le WhatsApp +212 771 158 018 juste en dessous.\n- Réseaux obligatoires : Instagram, TikTok et Google Maps.\n- Liens obligatoires : Mentions légales, Politique de confidentialité et prise de rendez-vous.\n- Le footer doit rester compact : pas d'espace vertical excessif au-dessus ou sous son contenu.\n- Il n'existe plus de workflow de réécriture automatique du footer : lors de la création d'une page, copier le footer canonique depuis une page existante.\n''',
        r, flags=re.S)
    rules_path.write_text(r, encoding='utf-8')

# Safety checks: design/content/SEO contracts should remain present.
for p in HTML_FILES:
    s = p.read_text(encoding='utf-8')
    assert s.count('class="cv-footer"') == 1, f'Canonical footer count invalid: {p}'
    if p.as_posix() != 'merci.html':
        assert '<link rel="canonical"' in s, f'Canonical missing: {p}'
    assert '/assets/css/site-shell.css' in s, f'Shared CSS missing: {p}'
    assert '/assets/js/site-shell.js' in s, f'Shared JS missing: {p}'
    assert 'id="cv-footer-styles"' not in s, f'Duplicate footer CSS remains: {p}'
    assert 'id="cv-header-styles"' not in s, f'Duplicate header CSS remains: {p}'
    assert 'id="cv-header-script"' not in s, f'Duplicate header JS remains: {p}'

print(f'Cleaned {len(HTML_FILES)} HTML files; shared shell assets created.')
