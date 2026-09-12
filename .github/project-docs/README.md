# Centre Dentaire Venezuela — site officiel

Site statique du Centre Dentaire Venezuela à Tanger, publié depuis la branche `main`.
Le projet reste volontairement simple : HTML, CSS et JavaScript sans framework ni dépendances de build.

## Architecture actuelle

```text
.
├── index.html
├── merci.html
├── favicon.svg
├── robots.txt
├── sitemap.xml
├── CNAME
├── assets/
│   ├── css/
│   │   └── site-shell.css        # header + footer communs
│   ├── js/
│   │   └── site-shell.js         # comportement commun du header
│   ├── images/
│   ├── video/
│   └── sources/                  # sources historiques, non chargées par le site
├── nos-soins/
├── soins-dentaires-tanger/
├── chirurgie-dentaire-tanger/
├── dentisterie-esthetique-tanger/
├── blanchiment-dentaire-tanger/
├── implant-dentaire-tanger/
├── endodontie-tanger/
├── parodontologie-tanger/
├── orthodontie-tanger/
├── dr-majda-laasraoui-dentiste-tanger/
├── blog/
│   └── blanchiment-dentaire-guide/
├── mentions-legales/
├── politique-confidentialite/
└── .github/project-docs/
```

## Règles de maintenance

- Conserver les URLs existantes et leurs balises canonical.
- Une seule balise H1 principale par page indexable.
- Le header et le footer visibles doivent rester cohérents avec la homepage.
- Les styles communs du header/footer sont dans `assets/css/site-shell.css`. Ne pas recopier ces blocs dans chaque page.
- Le comportement commun du header est dans `assets/js/site-shell.js`.
- Les pages de soins gardent leur contenu et leurs styles propres tant qu'aucun refactor visuel n'est demandé.
- Toute page indexable doit conserver title, meta description, canonical, robots, Open Graph, données structurées pertinentes et FAQ visible lorsque le sujet s'y prête.
- Toute nouvelle page indexable doit être ajoutée à `sitemap.xml`.
- Ne pas ajouter de FAQPage schema par défaut.
- Ne pas afficher de mention publique de l'infrastructure de dépôt/hébergement dans les pages du site.

## Navigation / composants communs

Le header et le footer sont présents directement dans chaque page HTML pour rester compatibles avec un hébergement statique sans moteur de template. Leur CSS et le comportement JavaScript communs sont externalisés dans `assets/css/site-shell.css` et `assets/js/site-shell.js`.

Il n'y a plus de workflow qui réécrit automatiquement tous les footers après chaque modification HTML. Cela évite les commits automatiques en cascade et rend l'historique du dépôt plus lisible. Quand une nouvelle page est créée, copier le header/footer canonique d'une page existante puis utiliser les assets partagés.

## Formulaire de rendez-vous

Le formulaire de la homepage ne dépend pas de Netlify Forms. Il prépare un message WhatsApp à partir des informations saisies et ouvre WhatsApp pour l'envoi.

## SEO

La base actuelle comprend :
- `robots.txt` avec référence au sitemap ;
- `sitemap.xml` ;
- canonicals ;
- métadonnées Open Graph/Twitter ;
- données structurées Dentist / Service / Person / Article selon les pages ;
- maillage interne entre le hub de soins, les traitements, la praticienne et le blog.

## Coordonnées de référence

- Centre Dentaire Venezuela
- 4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair, Tanger 90000, Maroc
- Téléphone : +212 5 31 11 21 27
- WhatsApp : +212 771 158 018
- Email : centredentairevenezuela@gmail.com
- Instagram : https://www.instagram.com/centre.dentaire.venezuela/
- TikTok : https://www.tiktok.com/@centredentairevenezuela

## Horaires

- Lundi, mercredi, vendredi : 09:30–17:30
- Mardi, jeudi : 09:30–13:00 et 15:00–18:30
- Samedi : 10:00–14:00
- Dimanche : fermé

## Performance

Les principaux médias lourds sont les vidéos. Le hero utilise actuellement la vidéo longue avec `preload="auto"`; la vidéo de présentation utilise `preload="metadata"`. Toute optimisation future des performances doit d'abord mesurer l'impact de ces médias avant de modifier le design.

## Documentation projet

Les règles métier, SEO et éditoriales complémentaires sont dans `.github/project-docs/`.
