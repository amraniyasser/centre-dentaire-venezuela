from pathlib import Path

PAGES = {
    'soins-dentaires-tanger/index.html': [
        'Contrôle dentaire', 'Détartrage', 'Carie dentaire', 'Obturation dentaire', 'Soins conservateurs'
    ],
    'chirurgie-dentaire-tanger/index.html': [
        'Extraction dentaire', 'Chirurgie orale', 'Frénectomie', 'Gingivectomie', 'Chirurgie implantaire'
    ],
    'dentisterie-esthetique-tanger/index.html': [
        'Blanchiment dentaire', 'Facettes dentaires', 'Facettes céramique', 'Facettes composite', 'Couronne dentaire', 'Bridge dentaire'
    ],
    'implant-dentaire-tanger/index.html': [
        'Dent manquante', 'Remplacement d’une dent', 'Plusieurs dents absentes', 'Implant après extraction', 'Bridge ou implant'
    ],
    'endodontie-tanger/index.html': [
        'Traitement de canal', 'Dévitalisation', 'Douleur dentaire persistante', 'Carie profonde', 'Infection d’origine dentaire'
    ],
    'parodontologie-tanger/index.html': [
        'Gencives qui saignent', 'Inflammation gingivale', 'Parodontite', 'Déchaussement dentaire', 'Soins des gencives'
    ],
    'orthodontie-tanger/index.html': [
        'Bagues dentaires', 'Appareil dentaire', 'Aligneurs invisibles', 'Gouttières orthodontiques', 'Malocclusion'
    ],
}

CSS = '''
/* Motifs fréquents de consultation */
.motifs-section{padding:20px 20px 8px}
.motifs-section .inner{max-width:1180px;margin:0 auto}
.motifs-section .kicker{margin-bottom:12px}
.motif-chips{display:flex;flex-wrap:wrap;gap:9px}
.motif-chip{display:inline-flex;align-items:center;padding:9px 13px;border-radius:999px;background:#eef6f5;border:1px solid rgba(20,59,62,.07);color:var(--teal-deep);font-size:12px;font-weight:650;line-height:1.2}
@media(max-width:680px){.motifs-section{padding:14px 20px 2px}.motif-chip{font-size:11.5px;padding:8px 11px}}
'''

for path_str, motifs in PAGES.items():
    path = Path(path_str)
    html = path.read_text(encoding='utf-8')
    if 'Motifs fréquents de consultation' in html:
        continue

    chips = ''.join(f'<span class="motif-chip">{m}</span>' for m in motifs)
    block = (
        '\n<section class="motifs-section" aria-label="Motifs fréquents de consultation">'
        '<div class="inner">'
        '<span class="kicker">Motifs fréquents de consultation</span>'
        f'<div class="motif-chips">{chips}</div>'
        '</div></section>\n'
    )

    marker = '\n<section class="section">'
    if marker not in html:
        raise RuntimeError(f'Insertion marker not found in {path_str}')
    html = html.replace(marker, block + '<section class="section">', 1)

    if '.motifs-section{' not in html:
        if '</style>' not in html:
            raise RuntimeError(f'Style closing tag not found in {path_str}')
        html = html.replace('</style>', CSS + '\n</style>', 1)

    path.write_text(html, encoding='utf-8')

print('Restored consultation motifs on all seven service pages.')
