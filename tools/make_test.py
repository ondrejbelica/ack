import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf8').read()
def rep(a,b,count=None):
    global s
    if a not in s: raise SystemExit("MISSING: "+a[:70])
    s=s.replace(a,b) if count is None else s.replace(a,b,count)

rep('<title>Honorářová kalkulačka AČK</title>','<title>TEST – Honorářová kalkulačka AČK</title>\n<meta name="robots" content="noindex, nofollow">')
rep('content="Spočítejte honorář kameramana zvlášť za přípravu, natáčení a postprodukci. Výchozí sazby vycházejí z průzkumu AČK 2024."',
    'content="Testovací verze honorářové kalkulačky AČK. Všechny částky jsou smyšlené."')

# testovací označení – styly
rep('</style>','''
/* ===== TESTOVACÍ REŽIM ===== */
:root{--test:#FFD400}
body{
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='160'%3E%3Ctext x='20' y='100' transform='rotate(-24 120 80)' font-family='Arial,sans-serif' font-size='64' font-weight='700' fill='%23393838' fill-opacity='.07'%3ETEST%3C/text%3E%3C/svg%3E");
  background-attachment:fixed;
}
.testbar{
  position:sticky;top:0;z-index:10;
  background:repeating-linear-gradient(-45deg,var(--test) 0 18px,#1A1A1A 18px 36px);
  padding:6px 0;
}
.testbar .in{
  max-width:1120px;margin:0 auto;padding:0 16px;display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;justify-content:space-between;
}
.testbar strong,.testbar a{
  background:#1A1A1A;color:var(--test);padding:4px 10px;font-weight:700;font-size:15px;
}
.testbar a{background:var(--test);color:#1A1A1A;text-decoration:underline}
.screen{outline:6px solid var(--test);outline-offset:-6px}
.screen .top{justify-content:flex-start}
.screen .top #vatLabel{margin-left:auto}
.screen .top::after{content:"TEST";background:var(--test);color:#1A1A1A;font-weight:700;padding:2px 8px;margin-left:8px}
.phase,.box{box-shadow:inset 0 0 0 2px rgba(255,212,0,.9)}
.mini{border-top:6px solid var(--test)}
@media print{
  .testbar{position:static;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>''')

rep('<body>\n','''<body>
<div class="testbar" role="note">
  <div class="in">
    <strong>TESTOVACÍ VERZE – částky nejsou skutečné</strong>
    <a href="../">Přejít na ostrou verzi</a>
  </div>
</div>
''')
rep('<h1>Honorářová kalkulačka kameramana</h1>','<h1>Honorářová kalkulačka kameramana (test)</h1>')
rep('Výchozí sazby jsou mediány z průzkumu Asociace českých kameramanů z roku 2024.',
    'V testovací verzi jsou všechny sazby smyšlené a počítají se v jednotkách TEST místo korun.')
rep('Vyberte typ projektu. Denní sazba se doplní podle průzkumu AČK a můžete ji přepsat.',
    'Vyberte typ projektu. Denní sazba se doplní testovací hodnotou a můžete ji přepsat.')

# měna
rep('data-u="Kč"','data-u="TEST"')
rep('<small>Kč</small>','<small>TEST</small>')
rep('<strong id="miniTotal">0 Kč</strong>','<strong id="miniTotal">0 TEST</strong>')
rep('const kc = n => Math.round(n).toLocaleString("cs-CZ") + " Kč";','const kc = n => Math.round(n).toLocaleString("cs-CZ") + " TEST";')
rep('id="rate" min="0" step="500"','id="rate" min="0" step="5"')
rep('id="flat" min="0" step="1000"','id="flat" min="0" step="10"')

# smyšlené sazby: všechny kategorie stejně, důstojná 100, minimální 80
s=re.sub(r'aday:\s*\d+,\s*mday:\s*\d+,','aday:100, mday:80,',s)
rep('// Mediány z průzkumu AČK 2024 (Kč za natáčecí den)','// TESTOVACÍ REŽIM: smyšlené sazby v jednotkách TEST, neodpovídají průzkumu')

# patička
s=re.sub(r'<p>Výchozí denní sazby jsou mediány.*?</p>\s*<p>Pro srovnání:.*?</p>',
  '<p>Testovací verze. Všechny sazby a částky jsou smyšlené, uvádějí se v jednotkách TEST a neodpovídají průzkumu AČK ani skutečným honorářům. Slouží jen k vyzkoušení ovládání a výpočtu.</p>',s,flags=re.S)

rep("Hodnoty jsou nastavené podle průzkumu.","Hodnoty jsou nastavené na testovací výchozí.")
# souhrn
rep('`Honorář kameramana – ${c.name}`','`TESTOVACÍ VERZE (smyšlené částky) – Honorář kameramana – ${c.name}`')
rep('"Spočítáno honorářovou kalkulačkou AČK: "','"Spočítáno testovací verzí kalkulačky AČK: "')

if re.search(r'\bKč\b',s): print("POZOR: zbylo Kč:",[m.start() for m in re.finditer(r'\bKč\b',s)])
assert not re.search(r'aday:\s*1\d{4}',s)
open(dst,'w',encoding='utf8').write(s)
print("ok")
