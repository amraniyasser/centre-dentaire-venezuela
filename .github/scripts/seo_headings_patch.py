from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

replacements = {
    '<title>Centre Dentaire Venezuela, Dr Majda Laasraoui chirurgienne-dentiste à Tanger</title>': '<title>Dentiste à Tanger | Centre Dentaire Venezuela – Dr Majda Laasraoui</title>',
    '<meta property="og:title" content="Centre Dentaire Venezuela, Dr Majda Laasraoui chirurgienne-dentiste à Tanger">': '<meta property="og:title" content="Dentiste à Tanger | Centre Dentaire Venezuela – Dr Majda Laasraoui">',

    '<h1>L’excellence<br><span class="soft">au service<br>de votre</span><br><span class="accent">sourire</span></h1>': '<h1>Dentiste à Tanger<br><span class="soft">Centre Dentaire</span><br><span class="accent">Venezuela</span></h1>',

    '<h2 class="section-title" id="cabinet-title">Un lieu pensé<br><span class="accent-teal">pour votre confort.</span></h2>': '<h2 class="section-title" id="cabinet-title">Un cabinet dentaire à Tanger<br><span class="accent-teal">pensé pour votre confort</span></h2>',
    '<h2 class="section-title" id="praticienne-title">Dr Majda Laasraoui,<br><span class="accent-teal">chirurgienne-dentiste.</span></h2>': '<h2 class="section-title" id="praticienne-title">Dr Majda Laasraoui,<br><span class="accent-teal">chirurgienne-dentiste à Tanger</span></h2>',
    '<h2 class="section-title" id="resultats-title">Les sourires que nous<br><span class="accent-teal">avons transformés.</span></h2>': '<h2 class="section-title" id="resultats-title">Nos cas dentaires avant / après<br><span class="accent-teal">réalisés au cabinet</span></h2>',
    '<h2 class="section-title" id="soins-title">Des soins dentaires complets,<br><span class="accent-teal">pour toute la famille.</span></h2>': '<h2 class="section-title" id="soins-title">Nos soins dentaires<br><span class="accent-teal">à Tanger</span></h2>',
    '<h2 class="section-title" id="avis-title">Des sourires qui<br><span class="accent-teal">parlent pour nous.</span></h2>': '<h2 class="section-title" id="avis-title">Avis patients du Centre Dentaire<br><span class="accent-teal">Venezuela à Tanger</span></h2>',
    '<h2 class="section-title" id="contact-title">Votre sourire mérite<br><span class="accent-teal">toute notre attention.</span></h2>': '<h2 class="section-title" id="contact-title">Prendre rendez-vous avec<br><span class="accent-teal">votre dentiste à Tanger</span></h2>',

    '<h3>Soins généraux</h3>': '<h3>Soins dentaires généraux et détartrage</h3>',
    '<h3>Chirurgie</h3>': '<h3>Chirurgie dentaire et extractions</h3>',
    '<h3>Esthétique</h3>': '<h3>Dentisterie esthétique : blanchiment et facettes</h3>',
    '<h3>Implantologie</h3>': '<h3>Implants dentaires et implantologie</h3>',
    '<h3>Endodontie</h3>': '<h3>Endodontie et traitement de canal</h3>',
    '<h3>Parodontologie</h3>': '<h3>Parodontologie et soins des gencives</h3>',
    '<h3>Adresse</h3>': '<h3>Adresse du cabinet dentaire à Tanger</h3>',
    '<h3>Téléphone</h3>': '<h3>Téléphone et WhatsApp</h3>',
    '<h3>Horaires</h3>': '<h3>Horaires du cabinet</h3>',

    '<h2 class="footer-head">Nos soins</h2>': '<p class="footer-head">Nos soins</p>',
    '<h2 class="footer-head">Suivez-nous</h2>': '<p class="footer-head">Suivez-nous</p>',
    '<h2 class="footer-head">Horaires</h2>': '<p class="footer-head">Horaires</p>',
}

missing = []
for old, new in replacements.items():
    if old not in s:
        missing.append(old)
    else:
        s = s.replace(old, new, 1)

if missing:
    raise SystemExit('Missing expected snippets:\n' + '\n---\n'.join(missing))

path.write_text(s, encoding='utf-8')
