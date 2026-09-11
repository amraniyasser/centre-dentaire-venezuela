# Audit performance — 11 septembre 2026

## État observé
- Hero vidéo longue : environ 2,5 Mo.
- Variante hero courte : environ 1,0 Mo.
- Vidéo de présentation du cabinet : environ 3,4 Mo.
- Carte Google Maps chargée en lazy loading.
- Images principales en WebP.

## Décision P0
Aucune dégradation visuelle n'est introduite sans mesure réelle. Le point principal à surveiller est le LCP mobile de la homepage à cause de la vidéo hero. Mesurer PageSpeed / Core Web Vitals avant de remplacer la vidéo longue par la version courte.

## Règle
Toute nouvelle image doit être dimensionnée, compressée et servie dans un format moderne. Toute nouvelle vidéo doit être compressée et ne doit pas bloquer le rendu initial.
