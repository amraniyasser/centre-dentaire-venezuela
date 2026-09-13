# Règles SEO éditoriales

## FAQ obligatoire

- Toute page de contenu indexable du site doit comporter une FAQ visible et pertinente pour l’intention de la page.
- Tout article de blog doit comporter une FAQ visible, spécifique au sujet traité.
- Les réponses doivent rester médicalement prudentes, utiles et cohérentes avec le contenu principal.
- Quand un article s’appuie sur des données médicales, les réponses de FAQ doivent rester cohérentes avec les sources citées dans l’article.
- Ne pas ajouter de balisage `FAQPage` uniquement dans l’espoir d’obtenir un rich result Google. La FAQ visible reste utile pour l’UX, le SEO sémantique et le GEO.
- Les pages techniques `noindex` sans intention éditoriale, par exemple une page de confirmation après formulaire, sont exclues de cette règle.


## Validation médicale obligatoire des articles

- Tout article de blog publié doit afficher visiblement : **« Validé médicalement par Dr Majda Laasraoui, chirurgienne-dentiste à Tanger »**, avec un lien vers `/dr-majda-laasraoui-dentiste-tanger/`.
- Le balisage `Article` doit inclure `reviewedBy` vers l’entité `https://centredentairevenezuela.com/dr-majda-laasraoui-dentiste-tanger/#person`.
- Cette validation doit correspondre à une relecture réelle avant publication. Un brouillon non relu ne doit pas être publié avec cette mention.
- L’auteur éditorial peut rester le Centre Dentaire Venezuela ; la validation médicale est portée séparément par `reviewedBy`.

## Format visuel canonique des articles de blog

- Tous les articles de blog doivent utiliser exactement le même composant FAQ visible : `section.site-faq` > `.faq-inner` > `.faq-kicker` + `h2` + `details`. Le contenu des questions reste spécifique au sujet, mais le format visuel ne varie pas d’un article à l’autre.
- Le style de la FAQ est centralisé dans `/assets/css/site-shell.css`. Ne pas recopier les règles `.site-faq` dans le `<style>` d’un article.
- Tous les articles de blog doivent comporter un bloc **« En bref »** visible après l’introduction et avant le développement principal.
- Le bloc « En bref » utilise le composant partagé `.blog-summary` ; il résume l’article en quelques phrases utiles, sans bourrage de mots-clés ni promesse médicale ou commerciale non vérifiée.
- Le contenu du bloc « En bref » doit rester cohérent avec les sources et conclusions de l’article.

## Architecture des clusters et intention de recherche

- Une page soin locale reste la page commerciale/transactionnelle principale pour son service.
- Les articles ciblent des intentions informationnelles distinctes et renvoient vers la page soin correspondante.
- Quand un article dédié existe, la page soin répond brièvement puis renvoie vers lui au lieu de dupliquer toute la réponse.
- Éviter plusieurs pages visant exactement la même combinaison service + ville.
- `/nos-soins/` est le hub des traitements et spécialités ; `/soins-dentaires-tanger/` cible les soins courants.
- Les articles d’un même cluster peuvent se lier entre eux lorsque le lien est naturel, puis tous renvoient vers la page soin mère.
- Les entités structurées utilisent les IDs canoniques `/#website`, `/#dentist` et `/dr-majda-laasraoui-dentiste-tanger/#person`.

