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
