from pathlib import Path
p=Path('dentisterie-esthetique-tanger/index.html')
s=p.read_text(encoding='utf-8')
old='<p>Un blanchiment agit sur la couleur des dents naturelles. Les facettes peuvent modifier la forme, la teinte ou certaines proportions du sourire.'
new='<p>Un <a href="/blanchiment-dentaire-tanger/">blanchiment dentaire à Tanger</a> agit sur la couleur des dents naturelles. Les facettes peuvent modifier la forme, la teinte ou certaines proportions du sourire.'
if '/blanchiment-dentaire-tanger/' not in s:
    if old not in s:
        raise SystemExit('Target paragraph not found')
    s=s.replace(old,new,1)
    p.write_text(s,encoding='utf-8')
print('Whitening internal link ensured.')