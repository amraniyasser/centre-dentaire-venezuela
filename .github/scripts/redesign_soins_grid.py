from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Turn the services block from a carousel into a static all-visible grid.
s = s.replace('<div class="soins-carousel" data-carousel>', '<div class="soins-carousel">', 1)
s = s.replace('<div class="soins-track" data-track>', '<div class="soins-track">', 1)

nav = '''        <div class="soins-nav" role="group" aria-label="Faire défiler les soins">
          <button type="button" data-prev aria-label="Soins précédents">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12H5"/><path d="M11 6l-6 6 6 6"/></svg>
          </button>
          <button type="button" data-next aria-label="Soins suivants">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15"/><path d="M13 6l6 6-6 6"/></svg>
          </button>
        </div>

'''
if nav not in s:
    raise SystemExit('Services navigation block not found')
s = s.replace(nav, '', 1)

dots = '''
        <div class="soins-dots" data-dots aria-hidden="true">
          <span class="is-active"></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>'''
if dots not in s:
    raise SystemExit('Services dots block not found')
s = s.replace(dots, '', 1)

# Final override lives after all existing responsive rules so the old carousel
# breakpoints cannot override the new layout.
marker = '''/* Respect des préférences d'animation réduite */
@media(prefers-reduced-motion:reduce){
  .ribbon-track{animation:none}
  .proof-ribbon{overflow-x:auto;-webkit-mask-image:none;mask-image:none}
}
</style>'''

new_css = '''/* Respect des préférences d'animation réduite */
@media(prefers-reduced-motion:reduce){
  .ribbon-track{animation:none}
  .proof-ribbon{overflow-x:auto;-webkit-mask-image:none;mask-image:none}
}

/* ==========================================================================
   Nos soins — grille complète : les 7 familles restent visibles sans slider
   ========================================================================== */
.soins .section-inner.soins-grid{
  display:block;
}
.soins-intro{
  max-width:780px;
  margin:0 auto 38px;
  text-align:center;
}
.soins-intro .section-lead{
  max-width:700px;
  margin-left:auto;
  margin-right:auto;
}
.soins-intro .btn-dark{
  margin-top:24px;
}
.soins-carousel{
  width:100%;
  max-width:1220px;
  margin:0 auto;
}
.soins-nav,.soins-dots{display:none!important}
.soins-track{
  display:grid;
  grid-template-columns:repeat(12,minmax(0,1fr));
  gap:18px;
  overflow:visible;
  padding:0;
}
.soin-card{
  grid-column:span 3;
  min-width:0;
  min-height:232px;
  margin:0;
  padding:28px 20px 25px;
  scroll-snap-align:none;
}
/* Quatre cartes sur la première rangée, trois cartes plus larges en dessous. */
.soin-card:nth-child(n+5){grid-column:span 4}
.soin-card--featured{
  margin:0;
  border-color:rgba(138,189,184,.42);
  background:linear-gradient(180deg,#f2f8f7 0%,var(--white) 48%);
}
.soins-track:hover .soin-card:not(:hover){opacity:1}

@media(max-width:1100px){
  .soins-intro{margin-bottom:32px}
  .soin-card,
  .soin-card:nth-child(n+5){grid-column:span 6}
  .soin-card:nth-child(7){grid-column:4 / span 6}
}

@media(max-width:720px){
  .soins .section-inner.soins-grid{display:block}
  .soins-intro{display:block;margin:0 auto 28px;text-align:left}
  .soins-intro .section-lead{margin-left:0;margin-right:0}
  .soins-intro .btn-dark{display:inline-flex;margin-top:20px}
  .soins-carousel{display:block;width:100%}
  .soins-track{grid-template-columns:1fr;gap:14px}
  .soin-card,
  .soin-card:nth-child(n+5),
  .soin-card:nth-child(7){
    grid-column:1;
    width:100%;
    max-width:none;
    min-height:0;
    margin:0;
    opacity:1;
  }
  .soin-card:not(.is-current){opacity:1}
  .soin-card--featured{margin:0}
}
</style>'''

if marker not in s:
    raise SystemExit('End-of-style marker not found')
s = s.replace(marker, new_css, 1)

path.write_text(s, encoding='utf-8')
