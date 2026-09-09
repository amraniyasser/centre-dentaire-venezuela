from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'name="twitter:card"' not in s:
    marker='<meta property="og:image" content="https://centredentairevenezuela.com/assets/images/hero-poster-cabinet-dentaire-venezuela-tanger.webp">'
    if marker not in s:
        raise SystemExit('OG image marker not found')
    s=s.replace(marker, marker+'\n<meta name="twitter:card" content="summary_large_image">',1)
p.write_text(s,encoding='utf-8')
print('Homepage twitter:card ensured.')
