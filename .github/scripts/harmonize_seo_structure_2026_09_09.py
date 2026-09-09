from pathlib import Path
import re

BASE = "https://centredentairevenezuela.com"

pages = {
    "soins-dentaires-tanger/index.html": {
        "label": "Soins dentaires généraux",
        "chips": ["Contrôle dentaire", "Détartrage", "Carie dentaire", "Obturation dentaire", "Soins conservateurs"],
    },
    "chirurgie-dentaire-tanger/index.html": {
        "label": "Chirurgie dentaire",
        "chips": ["Extraction dentaire", "Chirurgie orale", "Frénectomie", "Gingivectomie", "Chirurgie implantaire"],
    },
    "dentisterie-esthetique-tanger/index.html": {
        "label": "Dentisterie esthétique",
        "chips": ["Blanchiment dentaire", "Facettes dentaires", "Facettes en céramique", "Facettes en composite", "Couronne dentaire", "Bridge dentaire"],
    },
    "endodontie-tanger/index.html": {
        "label": "Endodontie",
        "chips": ["Traitement de canal", "Dévitalisation", "Douleur dentaire", "Carie profonde", "Infection dentaire"],
    },
    "parodontologie-tanger/index.html": {
        "label": "Parodontologie",
        "chips": ["Saignement des gencives", "Parodontite", "Déchaussement dentaire", "Rétraction gingivale", "Soins des gencives"],
    },
    "orthodontie-tanger/index.html": {
        "label": "Orthodontie",
        "chips": ["Dents mal alignées", "Bagues dentaires", "Appareil dentaire", "Aligneurs invisibles", "Gouttières orthodontiques", "Malocclusion"],
    },
}

nav_old = '<a href="/">Accueil</a><a href="/#soins">Nos soins</a><a href="/#localisation">Localisation</a><a class="cta" href="/#rdv">Prendre RDV</a>'
nav_new = '<a href="/">Accueil</a><a href="/#soins">Nos soins</a><a href="/#localisation">Localisation</a><a href="/blog/">Blog</a><a class="cta" href="/#rdv">Prendre RDV</a>'

for path_str, cfg in pages.items():
    path = Path(path_str)
    text = path.read_text(encoding="utf-8")
    original = text

    # 1) Transform the SEO-looking keyword box into a patient-facing consultation-motifs box.
    block_pattern = re.compile(
        r'<div class="introbox"><strong>Recherches liées à ce soin à Tanger</strong><div class="chips">.*?</div></div>',
        re.S,
    )
    chips_html = ''.join(f'<span class="chip">{chip}</span>' for chip in cfg["chips"])
    replacement = f'<div class="introbox"><strong>Motifs fréquents de consultation</strong><div class="chips">{chips_html}</div></div>'
    text, n = block_pattern.subn(replacement, text, count=1)
    if n != 1:
        raise RuntimeError(f"Keyword block not found exactly once in {path_str}: {n}")

    # 2) Keep generic 'dentiste à Tanger / chirurgien-dentiste à Tanger' intent on the homepage.
    if path_str == "chirurgie-dentaire-tanger/index.html":
        text = text.replace('<span class="pill">Chirurgien-dentiste à Tanger</span>', '<span class="pill">Chirurgie orale à Tanger</span>')

    # 3) Add Blog consistently to service-page navigation, without touching meta descriptions.
    if nav_old not in text:
        raise RuntimeError(f"Navigation pattern missing in {path_str}")
    text = text.replace(nav_old, nav_new, 1)

    # 4) Harmonize visible breadcrumb to Accueil > Nos soins > Service.
    old_crumb = f'<div class="crumb"><a href="/">Accueil</a> / {cfg["label"]}</div>'
    new_crumb = f'<div class="crumb"><a href="/">Accueil</a> / <a href="/#soins">Nos soins</a> / {cfg["label"]}</div>'
    if old_crumb not in text:
        raise RuntimeError(f"Visible breadcrumb pattern missing in {path_str}")
    text = text.replace(old_crumb, new_crumb, 1)

    # 5) Harmonize BreadcrumbList schema to the same three-level hierarchy.
    url = f'{BASE}/{path.parent.name}/'
    old_schema = (
        f'{{"@type":"ListItem","position":1,"name":"Accueil","item":"{BASE}/"}},'
        f'{{"@type":"ListItem","position":2,"name":"{cfg["label"]}","item":"{url}"}}'
    )
    new_schema = (
        f'{{"@type":"ListItem","position":1,"name":"Accueil","item":"{BASE}/"}},'
        f'{{"@type":"ListItem","position":2,"name":"Nos soins","item":"{BASE}/#soins"}},'
        f'{{"@type":"ListItem","position":3,"name":"{cfg["label"]}","item":"{url}"}}'
    )
    if old_schema not in text:
        raise RuntimeError(f"Schema breadcrumb pattern missing in {path_str}")
    text = text.replace(old_schema, new_schema, 1)

    if text == original:
        raise RuntimeError(f"No changes made to {path_str}")
    path.write_text(text, encoding="utf-8")

# Implant page already has the correct 3-level breadcrumb; just align navigation with Blog.
implant = Path("implant-dentaire-tanger/index.html")
text = implant.read_text(encoding="utf-8")
original = text
text = text.replace(
    '<a href="/#soins">Nos soins</a>\n      <a href="/#localisation">Notre localisation</a>',
    '<a href="/#soins">Nos soins</a>\n      <a href="/#localisation">Notre localisation</a>\n      <a href="/blog/">Blog</a>',
    1,
)
text = text.replace(
    '<a href="/">Accueil</a><a href="/#cabinet">Le cabinet</a><a href="/#resultats">Nos transformations</a><a href="/#soins">Nos soins</a><a href="/#localisation">Notre localisation</a>',
    '<a href="/">Accueil</a><a href="/#cabinet">Le cabinet</a><a href="/#resultats">Nos transformations</a><a href="/#soins">Nos soins</a><a href="/#localisation">Notre localisation</a><a href="/blog/">Blog</a>',
    1,
)
text = text.replace(
    '<a href="/#soins">Nos soins</a><a href="/#resultats">Nos transformations</a><a href="/#rdv">Prendre rendez-vous</a>',
    '<a href="/#soins">Nos soins</a><a href="/#resultats">Nos transformations</a><a href="/blog/">Blog</a><a href="/#rdv">Prendre rendez-vous</a>',
    1,
)
if text == original:
    raise RuntimeError("No implant navigation changes made")
implant.write_text(text, encoding="utf-8")

print("SEO structure harmonization complete. Meta descriptions intentionally unchanged.")
