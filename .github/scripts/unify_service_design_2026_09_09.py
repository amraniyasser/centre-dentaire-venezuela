from pathlib import Path
import re

PAGES = [
    Path('soins-dentaires-tanger/index.html'),
    Path('chirurgie-dentaire-tanger/index.html'),
    Path('dentisterie-esthetique-tanger/index.html'),
    Path('endodontie-tanger/index.html'),
    Path('parodontologie-tanger/index.html'),
    Path('orthodontie-tanger/index.html'),
]

CSS = r'''<style>
:root{
  --ink:#143b3e;
  --teal:#8abdb8;
  --teal2:#c3dfdc;
  --teal-deep:#2f6d6b;
  --teal-soft:#8fb5b1;
  --teal-btn:#8fbdb6;
  --deep:#2f6d6b;
  --soft:#8fb5b1;
  --gold:#e5bd8c;
  --paper:#fbfcfb;
  --white:#fff;
  --muted:#5d7d7c;
  --line:rgba(20,59,62,.11);
  --font:"Avenir Next","Helvetica Neue",Arial,sans-serif;
  --nav:68px;
  --gutter:4.6%;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img,svg{display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}

/* Header — same visual system as the implant page */
.top{position:sticky;top:0;z-index:50;height:var(--nav);background:rgba(255,255,255,.96);border-bottom:1px solid rgba(20,59,62,.07);backdrop-filter:blur(12px)}
.top .wrap{height:100%;max-width:none;padding:0 var(--gutter);display:flex;align-items:center;justify-content:space-between;gap:26px}
.brand{display:flex;flex-direction:column;gap:5px;line-height:1}
.brand small{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--teal-soft);font-weight:500}
.brand b{font-size:18.6px;letter-spacing:.126em;text-transform:uppercase;color:var(--teal-deep);font-weight:400}
.nav{display:flex;align-items:center;gap:28px;white-space:nowrap}
.nav a{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#3c5c5c}
.nav a:hover{color:var(--teal-deep)}
.nav .cta{display:inline-flex;align-items:center;height:38px;padding:0 20px;border-radius:10px;background:var(--teal-btn);color:#fff;font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}

/* Hero — matches implant page */
.hero{margin:0 1.05vw 28px;border-radius:34px;overflow:hidden;background:linear-gradient(135deg,#173e40 0%,#2c6663 58%,#7faeaa 100%);color:#fff;position:relative}
.hero:after{content:"";position:absolute;width:520px;height:520px;right:-170px;top:-180px;border-radius:50%;border:1px solid rgba(255,255,255,.13);box-shadow:0 0 0 80px rgba(255,255,255,.035),0 0 0 160px rgba(255,255,255,.025)}
.hero .wrap{max-width:1400px;margin:0 auto;padding:26px var(--gutter) 62px;position:relative;z-index:1}
.crumb{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:40px;font-size:12px;color:rgba(255,255,255,.7)}
.crumb a{text-decoration:none}.crumb a:hover{color:#fff}
.pill{display:inline-flex;align-items:center;gap:9px;margin-bottom:17px;padding:0;border:0;border-radius:0;background:transparent;font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#d8e8e6}
.pill:before{content:"";width:28px;height:2px;background:var(--gold)}
h1{margin:0;max-width:840px;font-size:clamp(44px,6vw,82px);font-weight:300;line-height:.98;letter-spacing:-.025em}
.hero p{max-width:720px;margin:24px 0 0;font-size:17px;line-height:1.72;color:rgba(255,255,255,.9)}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:50px;padding:0 23px;border-radius:14px;font-size:13.5px;font-weight:700;transition:transform .2s,background .2s}
.btn:hover{transform:translateY(-1px)}
.btn-primary{background:#fff;color:var(--teal-deep)}
.btn-secondary{border:1px solid rgba(255,255,255,.45);color:#fff;background:rgba(255,255,255,.06)}

/* Content */
.main{padding:72px 20px}
.main>.grid{max-width:1180px;margin:0 auto;padding:0;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(260px,.72fr);gap:48px;align-items:start}
.content h2{margin:58px 0 16px;font-size:clamp(30px,4vw,48px);font-weight:300;line-height:1.1;letter-spacing:-.015em;color:var(--ink)}
.content h2:first-of-type{margin-top:44px}
.content p,.content li{font-size:15px;line-height:1.78;color:var(--muted)}
.content ul{padding-left:20px}
.content li{margin:7px 0}
.content p a,.content li a{color:var(--teal-deep);text-decoration:underline;text-underline-offset:3px}

.introbox{padding:23px;border-radius:20px;background:#fff;border:1px solid var(--line);box-shadow:0 12px 28px rgba(20,59,62,.06)}
.introbox strong{display:block;margin-bottom:13px;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--teal-soft)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:8px 11px;border-radius:999px;background:#eef6f5;color:var(--teal-deep);font-size:11.5px;font-weight:650}

.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:22px}
.step{padding:24px;border-radius:20px;background:#fff;border:1px solid var(--line)}
.step b{display:grid;place-items:center;width:64px;height:38px;margin-bottom:18px;border-radius:12px;background:var(--ink);color:#fff;font-size:10.5px;font-weight:700;letter-spacing:.03em}
.step span{display:block;font-size:13.5px;line-height:1.65;color:var(--muted)}

.faq{max-width:900px}
.faq details{border-top:1px solid var(--line);padding:0}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:22px 38px 22px 0;font-size:16px;font-weight:600;color:var(--ink);position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:4px;top:18px;font-size:24px;font-weight:300;color:var(--teal-deep)}
.faq details[open] summary:after{content:"–"}
.faq p{margin:-4px 0 22px;max-width:760px;font-size:14px;line-height:1.72}

.side{position:sticky;top:94px}
.card{padding:23px;border-radius:20px;background:#fff;border:1px solid var(--line);box-shadow:0 12px 28px rgba(20,59,62,.06)}
.card+.card{margin-top:16px}
.card h3{margin:0 0 14px;font-size:15px;font-weight:650;color:var(--ink)}
.contactline{display:block;padding:12px 0;border-top:1px solid var(--line);font-size:13.5px;line-height:1.5;color:#4e706e}
.contactline:first-of-type{border-top:0}
.contactline small{display:block;margin-bottom:3px;font-size:10.5px;text-transform:uppercase;letter-spacing:.1em;color:#8aa4a1}
.contactline b{font-weight:600;color:var(--ink)}
.contactline:hover b{color:var(--teal-deep)}
.related{display:flex;flex-wrap:wrap;gap:10px}
.related a{display:inline-flex;padding:10px 13px;border-radius:999px;background:#eef6f5;color:var(--teal-deep);font-size:12px;font-weight:700}
.related a:hover{background:#e1efed}

.local{margin-top:58px;padding:34px;border-radius:26px;background:var(--ink);color:#fff;overflow:hidden;position:relative}
.local:after{content:"";position:absolute;width:260px;height:260px;right:-110px;top:-130px;border-radius:50%;border:1px solid rgba(255,255,255,.1);box-shadow:0 0 0 55px rgba(255,255,255,.025)}
.local h2{position:relative;z-index:1;margin-top:0;color:#fff}
.local p{position:relative;z-index:1;margin-bottom:0;color:rgba(255,255,255,.72)}
.local a{color:var(--teal2)}

.foot{background:#102f31;color:#fff;margin-top:0}
.foot .wrap{max-width:1180px;padding:42px 20px;display:flex;justify-content:space-between;gap:24px;align-items:center}
.foot p{margin:0;font-size:13px;color:rgba(255,255,255,.6)}
.foot a{font-size:13px;color:var(--teal2)}

@media(max-width:980px){
  .nav a:not(.cta){display:none}
  .main>.grid{grid-template-columns:1fr}
  .side{position:static}
  .steps{grid-template-columns:1fr 1fr}
}
@media(max-width:680px){
  :root{--nav:58px}
  .top .wrap{padding:0 20px}
  .brand small{font-size:8.5px}.brand b{font-size:16px}
  .nav .cta{height:36px;padding:0 13px;font-size:10px}
  .hero{margin:0 8px 18px;border-radius:24px}
  .hero .wrap{padding:22px 20px 38px}
  .crumb{margin-bottom:28px}
  h1{font-size:clamp(38px,12vw,54px)}
  .hero p{font-size:15px}
  .actions{flex-direction:column}.btn{width:100%}
  .main{padding:52px 20px}
  .content h2{margin-top:48px}
  .steps{grid-template-columns:1fr}
  .local{padding:28px 22px}
  .foot .wrap{padding:36px 20px;flex-direction:column;align-items:flex-start}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn{transition:none}}
</style>'''

for path in PAGES:
    text = path.read_text(encoding='utf-8')
    before = text
    text, count = re.subn(r'<style>.*?</style>', CSS, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Expected exactly one style block in {path}, got {count}')
    if text == before:
        raise RuntimeError(f'No change made to {path}')
    path.write_text(text, encoding='utf-8')
    print(f'Updated {path}')

print('Service page visual system unified with implant page.')
