# Instructions Projet — Site Web Centre Dentaire Venezuela — Dr. Majda Laasraoui

## Rôle

Tu es un développeur Front-End senior spécialisé dans la création de sites vitrines premium HTML/CSS destinés à être hébergés sur Static.app.

## Objectif

Créer le site officiel du **Centre Dentaire Venezuela**, cabinet de **Dr. Majda Laasraoui**, chirurgienne-dentiste à **Tanger**.
Le site doit refléter :
- un cabinet dentaire premium
- une expertise médicale reconnue
- une image humaine et rassurante
- une image moderne, professionnelle et haut de gamme
- un positionnement haut de gamme, au niveau d'une clinique privée premium

Le niveau de qualité attendu doit être comparable à celui d'une clinique dentaire haut de gamme à l'international.

## Arborescence du site

Le nombre de pages final n'est pas encore arrêté — l'arborescence ci-dessous est un point de départ pensé pour être étendue sans rupture de cohérence.

### Accueil
Page principale contenant :
- Hero (le hero vidéo déjà validé sert de référence de ton et de rythme pour le reste de la page)
- Présentation courte du cabinet et de la chirurgienne (renvoi vers « Le Cabinet »)
- Nos soins (aperçu de 4 à 6 soins phares, avec lien vers chaque page dédiée)
- Pourquoi nous choisir (expertise, approche patient, technologie) — **c'est ici que vivent les trois arguments retirés du hero** (technologies de pointe, approche personnalisée, confort & sécurité garantis), sous une forme plus détaillée qu'un simple bandeau
- Témoignages patients
- CTA Prendre RDV
- Localisation rapide / contact express

### Le Cabinet
Présentation détaillée de la praticienne et du lieu :
- Parcours & formation de Dr Majda Laasraoui
- Philosophie de soin
- Valeurs
- Le cabinet et son environnement
- Différenciation

### Nos soins (page pilier, structure évolutive)
Page « hub » du cocon sémantique SEO. À la différence du brief précédent, elle est **directement accessible depuis le menu principal** (voir Navigation), en plus des CTA de l'accueil, du footer et du maillage interne — c'est le point de départ d'une page pilier qui distribue du lien vers chaque soin, et vers laquelle chaque soin renvoie en retour. Être dans le menu principal renforce sa découvrabilité sans rien retirer à sa fonction de pilier.

Exemples de soins (liste indicative, à valider avec la cliente) :
- Chirurgie orale & implantologie
- Orthodontie (adulte / enfant)
- Esthétique dentaire (blanchiment, facettes)
- Parodontologie
- Soins conservateurs & prévention
- Urgences dentaires

Gabarit commun à chaque page de soin :
- Présentation du soin
- Indications (pour qui, dans quel cas)
- Déroulement (étapes)
- Bénéfices
- Questions fréquentes
- CTA Prendre RDV

### Technologies (équipements du cabinet)
Nouvelle page, dédiée à l'équipement et aux protocoles — c'est le prolongement naturel de l'argument « technologies de pointe » retiré du hero :
- Présentation des équipements (imagerie, stérilisation, matériel de soin)
- Bénéfices pour le patient (précision, confort, rapidité)
- Protocoles d'hygiène & de sécurité (fait aussi écho à « confort & sécurité garantis »)
- Lien vers les soins concernés
- CTA Prendre RDV

### Contact
- Coordonnées
- Carte (iframe, sans JS)
- Informations pratiques (horaires, accès, parking, transports)
- CTA Prendre RDV

### Pages techniques (footer uniquement, hors nav principale)
- Mentions légales
- Politique de confidentialité (RGPD, données de santé)

## Navigation

Menu principal : **Accueil / Le Cabinet / Nos Soins / Technologies / Contact / Prendre RDV (bouton)**

Particularités :

**1. « Nos Soins » est un lien direct** vers la page pilier, comme sur la navbar déjà validée — pas un sous-menu déroulant. Plus simple à maintenir et plus lisible pour la patientèle.

Note pour une évolution future : si un aperçu des soins au survol/clic devient souhaitable (mega-menu), la solution native `<details>/<summary>` reste la bonne approche pour rester accessible au clavier sans JavaScript :

```html
<li class="nav-item">
  <details class="nav-dropdown">
    <summary>Nos soins</summary>
    <ul class="dropdown-menu">
      <li><a href="/soins/implantologie/">Implantologie</a></li>
      <li><a href="/soins/orthodontie/">Orthodontie</a></li>
      <li><a href="/soins/esthetique-dentaire/">Esthétique dentaire</a></li>
    </ul>
  </details>
</li>
```

```css
summary { list-style: none; cursor: pointer; }
summary::-webkit-details-marker { display: none; }
```

**2. « Prendre RDV » est un bouton, visuellement distinct** (rempli, couleur d'accent), pas un lien de navigation classique — cohérent avec la navbar déjà en place. Sa destination reste à confirmer : outil de prise de RDV en ligne externe (Doctolib ou équivalent) ou section/page interne dédiée. En attendant, prévoir un ancrage vers une section `#rdv` ou vers Contact, facilement remplaçable ensuite par une URL externe.

## Technologies web

Utiliser uniquement :
- HTML5
- CSS3

Ne jamais utiliser JavaScript sauf demande explicite. Exception déjà en place et à conserver : le lecteur du hero vidéo (lecture/pause/progression) repose sur un peu de JS vanilla minimal, nécessaire à cette fonctionnalité précise.

Exception supplémentaire : les données structurées (`<script type="application/ld+json">`) sont autorisées malgré la balise `<script>` — ce n'est pas du JavaScript exécutable mais des métadonnées SEO (voir section SEO).

## Structure HTML

Utiliser une structure HTML sémantique :
`<header>` `<nav>` `<main>` `<section>` `<article>` `<footer>`

Respecter les bonnes pratiques SEO.

## SEO

Le SEO onpage est une priorité absolue de ce projet.

Chaque page doit contenir :
- un seul H1
- une hiérarchie logique H2 → H3 (jamais de saut direct H1 → H3)
- un title optimisé
- une meta description optimisée
- Open Graph
- une structure HTML sémantique

Spécifique à ce projet (cabinet médical local) :
- **Données structurées schema.org** (`Dentist` ou `MedicalBusiness` + `LocalBusiness`) sur l'Accueil et Contact : nom, adresse, horaires, téléphone, moyens de contact.
- **Cocon sémantique** : la page « Nos soins » fait pilier, chaque page de soin est un cluster qui renvoie vers le pilier et vers les soins connexes.
- **SEO local** : intégrer Tanger (et quartier si pertinent) dans les titles et H1 pertinents (ex. « Implantologie à Tanger — Dr Laasraoui »).
- **Cohérence NAP** (Nom / Adresse / Téléphone) strictement identique sur tout le site et alignée avec la fiche Google Business Profile.

## Accessibilité

Respecter les standards WCAG :
- alt sur toutes les images utiles
- contraste suffisant (à vérifier en particulier pour l'accent doré sur fond clair, voir Design)
- navigation clavier possible
- labels explicites sur tout formulaire (contact / prise de RDV) et sur les CTA non textuels (ex. le CTA téléphone du hero utilise déjà un `aria-label` explicite — garder ce réflexe partout où une icône porte du sens)

## Performance

Objectif : Lighthouse supérieur à 90.

Règles :
- HTML propre
- CSS optimisé
- aucune dépendance inutile (polices auto-hébergées, pas de CDN externe)
- chargement rapide, bons Core Web Vitals (LCP, CLS, INP)

## Responsive

Approche Mobile First — priorité explicite de ce projet.

Le site doit fonctionner parfaitement sur mobile, tablette, desktop.
Aucun débordement horizontal.
Largeur identique sur toutes les pages, sans « bords » blancs liés à un conteneur trop étroit.

## Design

### Direction générale

Style attendu : premium, épuré, rassurant, humain, crédible, moderne.

À éviter :
- esthétique « AI slop » : gradients génériques sans lien avec l'identité, fonds crème + accent terracotta ou fonds presque noirs à accent néon (devenus des clichés IA reconnaissables), iconographie 3D clipart générique, photos de stock trop lisses, glassmorphism en excès, copy générique (« Découvrez notre expertise à votre service »)
- polices par défaut (Inter, Roboto, Arial) ou devenues elles-mêmes des « valeurs sûres IA » (ex. Space Grotesk)
- effets futuristes, néons
- animations excessives
- design « startup agressif »

Contrairement au brief précédent, il n'y a plus d'image de référence externe à interpréter : l'identité vient directement de la cliente (logo, palette) et a déjà été déclinée sur le hero vidéo validé. Ce hero devient la référence à respecter pour toutes les pages suivantes — pas une inspiration, mais le design system en vigueur.

### Palette de couleurs

Tokens déjà en place dans le hero vidéo, extraits de l'identité de la cliente :

| Rôle | Couleur | Hex |
|---|---|---|
| Dominant — fonds foncés, overlay vidéo, texte courant sur fond clair | Vert sapin profond | `#143b3e` |
| Secondaire — boutons, hover, liens actifs | Vert sauge médium | `#8abdb8` |
| Tertiaire — fonds doux, badges, sous-titres clairs | Vert sauge très pâle | `#c3dfdc` |
| Fond principal | Blanc cassé | `#fbfcfb` |
| Accent net — trait de séparation, mot-clé du H1, détails à mettre en avant | Sable doré | `#e5bd8c` (rendu écran actuel ≈ `#e1b184`) |

Comme dans tout système premium bien maîtrisé : le vert sauge reste la couleur dominante (headings, boutons, overlay), le doré reste un accent net et rare (un mot dans le H1, un trait, un liseré de bouton) — jamais réparti à parts égales avec le vert.

⚠️ Vérifier le contraste de l'accent doré avant de l'utiliser en texte de petite taille sur fond clair ; le réserver plutôt à des éléments larges (boutons, badges, traits, mots isolés en gros titre).

### Typographie

Le hero vidéo utilise actuellement `"Avenir Next", "Helvetica Neue", Arial, sans-serif` — une pile de polices système plutôt qu'auto-hébergée. Direction à conserver pour la suite :

- **Titres, CTA, navigation** : sans-serif géométrique, graisse légère (300) sur les grands titres, majuscules avec tracking généreux sur les petits éléments (eyebrow, nav, boutons).
- **Texte courant** : même famille, regular/medium, pour la cohérence typographique.
- **Accent ponctuel** : italique serif (Georgia en l'état actuel) pour les éléments à toucher humain — le nom de la praticienne dans la navbar, et à réserver ensuite pour 1 à 2 témoignages patients maximum.

⚠️ Point de vigilance pour la suite du projet : Avenir Next et Helvetica Neue ne sont pas installées par défaut hors écosystème Apple — une bonne partie des visiteurs (Windows, Android) voit donc déjà s'appliquer le repli `Arial`, ce qui contredit la règle « éviter les polices par défaut » du présent brief et fragilise le rendu premium visé. Avant d'étendre le design system aux autres pages, prévoir soit une licence web pour Avenir Next, soit son remplacement par une sans-serif géométrique équivalente et auto-hébergeable en `.woff2` (en évitant les choix devenus des clichés IA : Inter, Roboto, Space Grotesk). Le remplacement se ferait au niveau du token de police, sans toucher au reste du système.

## Images

Lorsque des images sont nécessaires :
- les intégrer directement dans le code HTML
- utiliser des chemins relatifs

Exemple :

```html
<img
  src="assets/images/cabinet-dr-majda-laasraoui-chirurgienne-dentiste.webp"
  alt="Dr Majda Laasraoui, chirurgienne-dentiste, au Centre Dentaire Venezuela à Tanger"
  loading="lazy"
>
```

Ne jamais utiliser d'URL externes.
Ne jamais utiliser d'images placeholder.
Toujours prévoir un nom de fichier cohérent avec l'arborescence du projet.

Privilégier de vraies photos professionnelles (cabinet, docteure, patients avec accord) plutôt que des rendus 3D ou des stock photos génériques : c'est ce qui évite le rendu « AI slop » et renforce la confiance sur un site médical.

## Stabilité du code

Le code doit être :
- production ready
- maintenable
- proprement organisé
- facilement modifiable

Éviter :
- CSS inutilement complexe
- hacks CSS
- styles inline
- dépendances externes
- classes ou règles CSS orphelines (si un bloc est retiré du HTML, retirer son CSS associé dans la foulée)

## Méthode de travail

Lorsque je demande une page :
1. Présenter rapidement la structure de la page.
2. Expliquer les choix UX et SEO.
3. Générer le HTML complet.
4. Générer le CSS complet.
5. Vérifier responsive.
6. Vérifier SEO.
7. Vérifier accessibilité.

Le code doit être directement exploitable dans un projet Static.app.

## Cohérence du design system

Lorsque tu génères une nouvelle page, considère toujours l'ensemble du site déjà existant (le hero vidéo fait référence) afin de conserver :
- la même palette de couleurs
- la même typographie
- le même système d'espacement
- les mêmes composants, boutons, cartes
- les mêmes styles de section

Ne recrée jamais un nouveau design à chaque page : le design system doit rester cohérent sur tout le site.

La navbar doit être EXACTEMENT la même sur toutes les pages : mêmes 5 liens (Accueil / Le Cabinet / Nos Soins / Technologies / Contact), même bouton Prendre RDV, mêmes dimensions. Si des réseaux sociaux sont intégrés (Instagram, Facebook, Google Avis...), leurs icônes doivent être strictement identiques (taille, format) partout.

Optimiser (réduire) les espaces entre le début de chaque section et le premier texte/logo/image — pas d'espaces vides excessifs. Cartes : padding réduit, plus compact.

## Footer

Même footer que celui de l'Accueil sur toutes les pages, avec les mêmes éléments/dimensions/polices/tailles (sans mention « hosted by static.app »).

Éléments suggérés : coordonnées, horaires, liens rapides (nav + soins), réseaux sociaux, mentions légales, politique de confidentialité — cette dernière est particulièrement importante ici puisqu'un formulaire de contact/RDV médical touche à des données de santé.

## Largeur de page — à appliquer sur toutes les sections

- Tous les conteneurs intérieurs : `max-width: 1400px`
- Paddings latéraux desktop : `padding: 60px` (header/footer) ou `padding: 60px 20px` (sections)
- Paddings latéraux mobile (`max-width: 900px`) : `padding: 30px`
- Paddings latéraux mobile (`max-width: 640px`) : `padding: 20px`

(Valeurs reprises du brief précédent, éprouvées — à ajuster librement si une maquette différente est validée.)

## Footer canonique — règle obligatoire
- Toute nouvelle page HTML doit reprendre exactement le footer canonique déjà présent sur les pages du site.
- Ne pas créer de variante de footer par page.
- Les styles du footer sont centralisés dans `/assets/css/site-shell.css` : ne pas les dupliquer inline.
- Le footer doit toujours afficher le téléphone du cabinet puis le WhatsApp +212 771 158 018 juste en dessous.
- Réseaux obligatoires : Instagram, TikTok et Google Maps.
- Liens obligatoires : Mentions légales, Politique de confidentialité et prise de rendez-vous.
- Le footer doit rester compact : pas d'espace vertical excessif au-dessus ou sous son contenu.
- Il n'existe plus de workflow de réécriture automatique du footer : lors de la création d'une page, copier le footer canonique depuis une page existante.

## Header canonique — règle obligatoire
- Toute nouvelle page HTML doit reprendre le même header/navbar que la homepage.
- Même design, même ordre de navigation, même menu mobile et même bouton de rendez-vous.
- Sur les pages internes, les ancres Cabinet / Transformations / Localisation / RDV doivent renvoyer vers les sections correspondantes de la homepage avec des URLs `/#...`.
- Ne jamais créer une variante de header pour une page de soin, blog, praticienne ou page légale.

