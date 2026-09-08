# Centre Dentaire Venezuela — Dr. Majda Laasraoui

Site vitrine premium du Centre Dentaire Venezuela (Dr. Majda Laasraoui, chirurgienne-dentiste à Tanger). HTML5 / CSS3 uniquement, hébergement cible : Static.app.

## Statut actuel

La page Accueil comporte pour le moment le **hero**, **Le Cabinet**, **Notre praticienne**, **Cas réels**, **Nos soins**, **Avis patients** et **Contact** (`index.html`) : navbar fine, hero vidéo, CTA téléphone / cabinet, et un bloc social proof (100% de satisfaction + avis Google, +300 patients traités, 8 ans d'expérience) affiché en carte sur desktop et en ruban défilant sur mobile. Les autres pages de l'arborescence (Le Cabinet, Nos Soins, Technologies, Contact) restent à faire — voir `docs/instructions-projet-centre-dentaire-venezuela.md` pour le brief complet.

Rien n'est figé : l'arborescence, la liste des soins et le design system restent modifiables.

## Coordonnées (NAP de référence)

À reprendre **à l'identique** sur toutes les pages, dans le footer et dans les données structurées :

- **Nom** : Centre Dentaire Venezuela (Dr Majda Laasraoui)
- **Adresse** : 4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair, Tanger 90000, Maroc
- **Téléphone** : +212 5 31 11 21 27

**Horaires** (dans le JSON-LD, à afficher aussi dans le footer et la page Contact) :

| Jour | Horaires |
|---|---|
| Lundi | 09:30 – 17:30 |
| Mardi | 09:30 – 13:00 et 15:00 – 18:30 |
| Mercredi | 09:30 – 17:30 |
| Jeudi | 09:30 – 13:00 et 15:00 – 18:30 |
| Vendredi | 09:30 – 17:30 |
| Samedi | 10:00 – 14:00 |
| Dimanche | Fermé |

## Structure

```
.
├── index.html                          → page d'accueil
├── merci.html                          → page de confirmation après envoi du formulaire
├── assets/
│   ├── images/
│   │   ├── logo-centre-dentaire-venezuela.webp
│   │   ├── hero-poster-cabinet-dentaire-venezuela-tanger.webp   → poster de la vidéo (1re frame)
│   │   ├── dr-majda-laasraoui-cabinet-dentaire-venezuela-tanger.webp   → vraie photo cabinet (pas encore utilisée dans le HTML)
│   │   ├── hero-visuel-alternatif-dent-3d.webp                  → écarté par la cliente, non utilisé (voir note ci-dessous)
│   │   ├── dr-majda-laasraoui-portrait-cabinet-dentaire-venezuela-tanger.webp   → 1re photo du carrousel, face caméra
│   │   ├── dr-majda-laasraoui-soin-cabinet-dentaire-venezuela-tanger.webp       → 2e photo du carrousel, démonstration de brossage
│   │   └── poster-presentation-cabinet-dentaire-venezuela-tanger.webp   → poster de la vidéo de présentation (frame à 6,5 s)
│   └── video/
│       ├── hero-cabinet-dentaire-venezuela-long.mp4    → vidéo de fond du hero (22s), en lecture auto
│       ├── hero-cabinet-dentaire-venezuela-short.mp4   → variante courte (9s), en réserve
│       └── presentation-cabinet-dentaire-venezuela-tanger.mp4   → visite du cabinet (32s), section Le Cabinet
└── docs/
    └── instructions-projet-centre-dentaire-venezuela.md   → brief projet complet (design system, SEO, arborescence...)
```

## Prévisualiser en local

Aucune dépendance : ouvrir `index.html` dans un navigateur, ou lancer un petit serveur local depuis la racine du projet (nécessaire pour que la vidéo/les images en chemins relatifs se chargent bien, selon le navigateur) :

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

## Changer de vidéo (courte / longue)

Dans `index.html`, sur la balise `<video>`, changer l'attribut `src` :

```html
src="assets/video/hero-cabinet-dentaire-venezuela-short.mp4"
```

## Pied de page

`<footer class="footer">` ferme la page sur le vert sapin `--ink`, en trois colonnes : identité et coordonnées, liste des soins, réseaux et horaires. Sous 1000 px la colonne identité passe sur toute la largeur et les deux autres se partagent la ligne ; sous 720 px tout s'empile.

Les six entrées de la colonne « Nos soins » pointent toutes vers `#soins` : il n'existe pas encore de page par soin. Le jour où elles seront créées, seules ces six `href` sont à changer. La puce Google du bloc « Suivez-nous » utilise un glyphe en aplat écrit en dur, et non le symbole partagé `#ico-google` : celui-ci porte ses propres attributs `fill` multicolores, que le CSS ne peut pas atteindre à travers un `<use>`.

En bas, la barre `.signature` : copyright et rappel « Prendre rendez-vous » à gauche, crédit de réalisation à droite. L'année se met à jour seule au chargement, la valeur écrite dans le HTML servant de repli si le script ne s'exécute pas.

Le nom de l'agence est en doré avec un reflet qui le traverse toutes les 4,5 secondes, doublé d'un halo qui s'allume au même moment : sur un texte de 12,5 px, le seul dégradé était trop discret pour se remarquer. Deux points de vigilance si ce bloc est retouché : la position du dégradé doit rester entre 0 et 100%, car avec `background-repeat:no-repeat` une valeur au delà le fait sortir de la boîte et le texte disparaît ; et le trait de survol est porté par `.signature-agency`, pas par le texte lui-même, qu'un `background-clip:text` rognerait avec lui. Reflet, halo et trait se coupent sous `prefers-reduced-motion`.

Restent à ajouter au pied de page : mentions légales et politique de confidentialité.

## Réseaux sociaux

- Instagram : https://www.instagram.com/centre.dentaire.venezuela/
- Fiche Google : https://share.google/NQdfjEYv9MC4431Lz

Les deux sont déclarés en `sameAs` dans le JSON-LD. Le bouton « Laissez-nous un avis » ouvre la fiche Google ; pour ouvrir directement le formulaire d'avis, remplacer ce lien par celui en `g.page/r/.../review` fourni par Google Business Profile.

## Formulaire de rendez-vous

Le formulaire de la section Contact est câblé pour **Netlify Forms** et ne fonctionne donc que sur un hébergement Netlify :

- `name="rendez-vous"` et `data-netlify="true"` déclarent le formulaire au moment du déploiement ;
- le champ caché `form-name` identifie l'envoi côté Netlify ;
- `data-netlify-honeypot="bot-field"` et le champ `bot-field` (hors écran, `tabindex="-1"`) filtrent les robots ;
- `action="/merci"` renvoie vers `merci.html` au lieu de la page de confirmation générique de Netlify.

Les envois arrivent dans l'onglet **Forms** du tableau de bord Netlify. Pour être prévenu par courriel à chaque demande, activer une notification dans *Site configuration > Forms > Form notifications*.

Champs transmis : `nom`, `motif`, `telephone`, `creneau`, `message`.

## Navigation

Menu, dans l'ordre d'apparition des sections : Accueil, Le cabinet, Nos transformations (`#resultats`), Nos soins (`#soins`), Notre localisation (lien direct vers l'itinéraire Google Maps), plus le bouton Prendre rendez-vous (`#rdv`).

Sous 1100px les liens passent dans un menu `<details>/<summary>`, et le bouton s'abrège en « Prendre RDV ». La barre est collante : c'est le `<header>` qui porte `position:sticky`, pas la barre elle-même, sinon elle ne pourrait coller que dans la boîte du header, qui fait exactement sa hauteur. Au delà de 40px de défilement elle s'allège (fond translucide et flou d'arrière-plan).

Les deux lignes de la marque se terminent au même endroit. La taille de `.brand-name` est ajustée au chargement par un court script qui mesure le texte réellement rendu : une valeur figée ne tiendrait pas, puisque la police retombe sur Arial hors écosystème Apple et que les proportions changent. Le calage est refait au redimensionnement et une fois les polices chargées. La valeur CSS de 18,6px sert de repli avant exécution.

## Règles de rédaction

- **Pas de tiret cadratin ni de tiret d'incise** dans les textes du site. Utiliser une virgule, un deux-points, une parenthèse ou une phrase séparée. Les traits d'union des mots composés (`chirurgienne-dentiste`, `rendez-vous`) ne sont pas concernés.

## Photos avant / après

Les huit cas de la section Cas réels viennent de montages verticaux fournis par la cliente, conservés tels quels dans `assets/sources/`. Chaque montage a été coupé en deux, puis les deux moitiés ont été recadrées **avec la même boîte**, ce qui est indispensable : le comparateur balaie une image par dessus l'autre, et deux cadrages différents donneraient l'impression que la photo saute au passage du curseur.

Toutes les images font exactement 4/3, comme la carte, donc rien n'est rogné à l'affichage. Chaque paire est vérifiable : les deux fichiers d'un même cas ont des dimensions identiques.

Pour ajouter un cas, découper le montage, recadrer les deux moitiés à l'identique en 4/3, exporter en WebP qualité 90 sous `avant-apres-NN-slug-avant.webp` et `-apres.webp`, puis dupliquer une carte dans le HTML.

## Photos de la praticienne

Les deux photos du carrousel sont recadrées en 1:1 depuis les originaux fournis :

- `dr-majda-laasraoui-portrait-...webp` : recadrage de la photo face caméra, coupé juste sous la signature murale. Garder « Dr. Majda Laasraoui, chirurgien dentiste » visible sur la photo faisait doublon avec le titre de la section.
- `dr-majda-laasraoui-soin-...webp` : recadrage de `dr-majda-laasraoui-cabinet-dentaire-venezuela-tanger.webp`, qui reste dans le repo comme source non recadrée.

`hero-visuel-alternatif-dent-3d.webp` (photo retouchée avec la dent 3D et le fond assombri) a été écartée par la cliente. Le fichier est conservé pour archive mais n'est référencé nulle part.

## Vidéo de présentation du cabinet

Le fichier source livré (`présentation cabinet Venezuela.MOV`) était un conteneur QuickTime — refusé par Chrome et Firefox, et au nom de fichier inexploitable en URL (espaces, accent). Il a été remuxé en MP4 sans réencodage (mêmes flux H.264 / AAC, aucune perte de qualité), avec `faststart` pour que la lecture démarre avant la fin du téléchargement. Le `.MOV` d'origine reste récupérable dans l'historique Git (commit `c34c3b3` sur `main`).

## Note sur `hero-visuel-alternatif-dent-3d.webp`

Ce visuel (photo + illustration de dent 3D en surimpression) avait été fourni comme option. Il se rapproche du rendu « 3D clipart générique » explicitement à éviter dans le brief design, et la cliente l'a écarté. Fichier conservé pour archive, non intégré dans le HTML.

## Stack

HTML5 + CSS3, avec une seule exception JavaScript : les comparateurs avant/après et le défilement des deux carrousels par flèches, validés explicitement. Tout le reste est en CSS pur, y compris la vidéo du hero (`autoplay muted loop playsinline`), le ruban défilant mobile et le carrousel de la praticienne. Les données structurées `application/ld+json` (schema.org `Dentist`) sont des métadonnées SEO, pas du JavaScript exécutable.

## Points ouverts

- **Typographie** : la pile actuelle (`Avenir Next` / `Helvetica Neue` / Arial) retombe sur Arial hors écosystème Apple. À remplacer par une géométrique auto-hébergée en `.woff2` — le changement se fait sur le token `--font`.
- **Lecture de la vidéo** : sans contrôles ni bouton de repli, si un navigateur bloque la lecture automatique (iPhone en mode économie d'énergie par exemple), le poster reste affiché — c'est une vraie image du cabinet, donc le rendu reste correct.
- **Points clés de la praticienne** : seul le diplôme (CEU Cardinal Herrera University, Valence) est confirmé ; les deux autres lignes décrivent l'approche et sont à remplacer par les informations à venir.
- **Avis publiés** : les onze avis de la section sont repris mot pour mot depuis Google, fautes de frappe comprises, avec le nom tel qu'il apparaît publiquement. Ils peuvent être abrégés en prénom + initiale si la cliente le préfère.
