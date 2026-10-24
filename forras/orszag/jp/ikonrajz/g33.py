import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 33. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 530 連れてって 連れてって: a car interior on a snowy night, wipers sweeping, two silhouettes in the front seats
d,b=bg([(0,'#0a1028'),(1,'#2a3a5a')])
b+=snow(80,530)+'<path d="M0 0 L800 0 L800 800 L0 800Z M80 120 L720 120 L760 520 L40 520Z" fill="#0a0a10" fill-rule="evenodd"/>'
b+='<path d="M400 520 L180 260" stroke="#1a1a1a" stroke-width="8"/>'+''.join(glow(x,500,40,'#ffd27a',.4) for x in (300,500))
b+='<rect y="520" width="800" height="280" fill="#14141c"/>'+''.join(f'<g fill="#000"><ellipse cx="{x}" cy="600" rx="44" ry="50"/><path d="M{x-80} 800 L{x-70} 660 Q{x} 630 {x+70} 660 L{x+80} 800Z"/></g>' for x in (240,560))+ring(240,690,60,'#2a2a2a',14)
I[530]=svg(b,d)

# 624 Something There: a jet plane rising above a sea of clouds into a red sunrise, early-90s airline
d,b=bg([(0,'#1a2a5a'),(.6,'#ff8a5a'),(1,'#ffd8a0')])
b+='<circle cx="560" cy="460" r="90" fill="#fff0c0"/>'+''.join(cloud(x,y,s,'#fff',.9) for x,y,s in [(100,560,1.8),(360,600,2.2),(660,560,1.8),(220,680,2),(560,700,2.2)])
b+='<g transform="rotate(-18 320 300)"><path d="M180 300 L460 290 Q500 300 460 310 L180 316Z" fill="#f4f4f8"/><path d="M300 300 L360 220 L390 220 L350 302Z M300 310 L360 390 L390 390 L350 308Z" fill="#e8e8f0"/><path d="M190 300 L180 250 L210 250 L230 300Z" fill="#c8102a"/></g>'
I[624]=svg(b,d)

# 1184 Flash: a karuta card being swept away in a flash of motion, red-and-white speed lines
d,b=bg([(0,'#f8f0e0'),(1,'#e8dcc4')])
b+=''.join(f'<path d="M0 {y} L800 {y-120}" stroke="#c8102a" stroke-width="{4+k%3*3}" opacity=".35"/>' for k,y in enumerate(range(200,900,60)))
b+='<g transform="rotate(-18 440 400)"><rect x="360" y="280" width="170" height="240" rx="10" fill="#fff" stroke="#3a3a3a" stroke-width="5"/><rect x="380" y="300" width="130" height="200" fill="none" stroke="#3a7a3a" stroke-width="4"/>'+txt(445,420,'ち',90,'#1a1a1a',900)+'</g>'
b+='<path d="M80 600 Q200 520 330 470 L350 510 Q230 560 140 660Z" fill="#f0c8a8"/>'+glow(360,470,80,'#fff',.6)
I[1184]=svg(b,d)

# 1379 The growing up train: a train bursting out of a long dark tunnel into bright green light
d,b=bg([(0,'#0a0a0a'),(1,'#1a1a1a')])
b+='<rect x="0" y="0" width="800" height="800" fill="#1a1410"/><path d="M200 800 L200 300 Q400 120 600 300 L600 800Z" fill="#cfffb0"/>'+glow(400,420,240,'#e8ffd0',.6)+hills(560,20,'#7ac85a',1379)
b+='<path d="M300 800 L360 520 L440 520 L500 800Z" fill="#e8e8f0"/><rect x="370" y="560" width="60" height="40" fill="#3a8ac8"/>'+glow(370,640,20,'#fff4b0',.9,'glow2')+glow(430,640,20,'#fff4b0',.9,'glow2')
I[1379]=svg(b,d)

# 1659 火種: a single glowing ember cupped in two hands in the dark, a small flame starting
d,b=bg([(0,'#0a0404'),(1,'#1a0a04')])
b+=glow(400,400,180,'#ff6a1a',.45)+'<path d="M400 300 Q370 360 380 400 Q390 380 400 410 Q412 370 420 400 Q434 360 400 300Z" fill="#ffb02a"/><path d="M400 360 Q390 390 400 410 Q410 390 400 360Z" fill="#fff4b0"/>'
b+='<path d="M220 560 Q260 440 380 430 L380 470 Q300 480 280 600Z M580 560 Q540 440 420 430 L420 470 Q500 480 520 600Z" fill="#e0a070"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#ffb02a"/>' for x,y in [(380,240),(430,200),(410,150),(360,180)])
I[1659]=svg(b,d)

# 88 京のにわか雨: a woman with a red paper umbrella in a sudden shower on a Kyoto stone lane, early-70s
d,b=bg([(0,'#7a8a8a'),(1,'#b8c0b8')])
b+=rain(90,88,'#fff',.35)+'<rect x="0" y="200" width="200" height="440" fill="#3a2a24"/><path d="M-20 200 L220 160 L240 220Z" fill="#2a1a14"/>'+chochin(150,320,.4,'#e8402a')
b+='<rect y="640" width="800" height="160" fill="#5a5a5a"/>'+''.join(f'<rect x="{x}" y="{y}" width="90" height="36" fill="#6a6a6a"/>' for y in (660,710,760) for x in range(-40*((y//50)%2),800,96))
b+=figure(460,660,230,'#1a1a24',hair='#1a1a24')+wagasa(470,400,1.4,'#c8283a',-12)
I[88]=svg(b,d)

# 481 Only You: a black leather jacket over a woman's shoulders in a neon-lit 80s night, protective
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=glow(600,180,90,'#3ad0ff',.5)+'<circle cx="600" cy="180" r="44" fill="#cff4ff"/>'+'<rect y="600" width="800" height="200" fill="#0a0a10"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#3ad0ff" stroke-width="2" opacity=".2"/>' for y in (640,700))
b+=figure(300,620,300,'#000')+figure(420,620,270,'#000',hair='#000')+'<path d="M370 380 Q420 360 480 390 L470 470 L380 460Z" fill="#141414" stroke="#3a3a4a" stroke-width="3"/>'
I[481]=svg(b,d)

# 697 君に逢いたくなったら...: a phone booth on a quiet coastal road at dusk, a woman inside, 90s ballad
d,b=bg([(0,'#5a6aa8'),(1,'#f0b8a0')])
b+='<rect y="460" width="800" height="140" fill="#4a6aa0"/><rect y="600" width="800" height="200" fill="#7a7a80"/>'
b+='<rect x="320" y="280" width="160" height="340" fill="#cfe8f0" opacity=".7" stroke="#2a8a5a" stroke-width="12"/><rect x="314" y="260" width="172" height="36" fill="#2a8a5a"/>'+glow(400,300,60,'#fff4c8',.5)+figure(400,600,240,'#1a1a2a',hair='#1a1a2a')
I[697]=svg(b,d)

# 847 100万回のKISS: a million tiny hearts swirling into a galaxy shape around two silhouettes kissing
d,b=bg([(0,'#0a0a2a'),(1,'#3a1a4a')])
b+=''.join(heart(400+r*math.cos(a+r/40),380+r*.7*math.sin(a+r/40),6,'#ff7ab0','opacity=".8"') for r in range(60,360,12) for a in (0,math.pi))
b+=profile(330,560,.9,'#000')+profile(470,560,.9,'#000',True)
I[847]=svg(b,d)

# 1332 願いごとの持ち腐れ: a school choir's wishes written on paper slips tied to a bamboo branch, unused
d,b=bg([(0,'#bfe0ff'),(1,'#f4faff')])
b+='<path d="M180 800 Q240 400 520 120" stroke="#3a8a3a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M{x} {y} q30 -10 60 0 q-30 20 -60 0Z" fill="#4ab84a"/>' for x,y in [(260,560),(330,430),(400,320),(470,210)])
b+=''.join(f'<rect x="{x}" y="{y}" width="34" height="90" fill="{c}" transform="rotate({a} {x} {y})"/>' for x,y,c,a in [(300,480,'#ff8aa8',6),(380,360,'#ffd02a',-6),(450,250,'#8ad0ff',8),(250,600,'#b88aff',-4)])
b+=''.join(note(x,y,20,'#5a7ab0') for x,y in [(600,400),(660,330),(640,480)])
I[1332]=svg(b,d)

# 1808 森の小さなレストラン: a tiny wooden cottage restaurant with a lantern deep in a misty forest
d,b=bg([(0,'#3a5a4a'),(1,'#8aa890')])
b+=''.join(tree(x,y,h,'#1a3a2a',x) for x,y,h in [(80,700,500),(700,720,520),(180,640,340),(620,640,320)])+'<rect y="680" width="800" height="120" fill="#2a4a2a"/>'
b+='<rect x="300" y="480" width="200" height="200" fill="#8a5a3a"/><path d="M280 490 L400 380 L520 490Z" fill="#5a2a1a"/><rect x="370" y="580" width="60" height="100" fill="#3a1a0a"/><rect x="320" y="520" width="50" height="40" fill="#ffd27a"/>'+glow(345,540,40,'#ffd27a',.6)+chochin(470,560,.25,'#ffd27a')
b+='<rect x="0" y="560" width="800" height="60" fill="#fff" opacity=".18"/>'
I[1808]=svg(b,d)

# 276 PURE GOLD: a gold record with a hot-dog-stand neon and a microphone, swaggering 1990 rock
d,b=bg([(0,'#1a1408'),(1,'#3a2a10')])
b+=glow(400,400,240,'#ffd02a',.3)+'<circle cx="400" cy="400" r="210" fill="#d8a82a"/>'+''.join(ring(400,400,r,'#b8881a',2) for r in range(90,210,14))+'<circle cx="400" cy="400" r="80" fill="#fff4c8"/><circle cx="400" cy="400" r="12" fill="#1a1408"/>'
b+=sparkle(560,220,30,'#fff')+sparkle(240,560,22,'#fff')
I[276]=svg(b,d)

# 482 Memory: a polaroid photo fading in a man's hand, drained colours, 80s rock nostalgia
d,b=bg([(0,'#2a2a2a'),(1,'#4a4a4a')])
b+='<g transform="rotate(8 400 380)"><rect x="270" y="200" width="260" height="300" fill="#f4f4f0"/><rect x="290" y="220" width="220" height="200" fill="#9aa0b0"/><circle cx="400" cy="300" r="40" fill="#c8c0b0" opacity=".6"/><rect x="290" y="340" width="220" height="80" fill="#b0a8a0" opacity=".6"/></g>'
b+='<path d="M200 760 Q260 560 340 500 L380 540 Q300 620 280 780Z" fill="#c8b0a0"/>'
I[482]=svg(b,d)

# 1037 ラストダンスあなたと: a couple dancing a last waltz on a highway overpass at night under city lights
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=skyline(520,'#141428',1037,100,320,'#ffd27a',80)+'<rect y="520" width="800" height="280" fill="#0a0a14"/><rect y="560" width="800" height="30" fill="#3a3a4a"/>'+''.join(f'<path d="M0 {y} Q400 {y-20} 800 {y}" stroke="{c}" stroke-width="5" fill="none" opacity=".7"/>' for y,c in [(680,'#ff3a3a'),(720,'#fff4b0')])
b+=figure(370,560,220,'#000',pose='hold')+figure(430,560,210,'#000',pose='hold',hair='#000')+'<path d="M410 480 Q470 520 500 560 L420 560Z" fill="#000"/>'
I[1037]=svg(b,d)

# 1333 So long !: a group of girls in graduation uniforms waving from a snowy hilltop, school behind
d,b=bg([(0,'#c8d8f0'),(1,'#f4f8ff')])
b+=snow(60,1333)+'<rect x="440" y="300" width="300" height="200" fill="#e8e0d8"/><rect x="560" y="240" width="60" height="70" fill="#e8e0d8"/>'+''.join(f'<rect x="{x}" y="340" width="40" height="40" fill="#9ab0c8"/>' for x in (470,540,610,680))
b+='<path d="M0 560 Q400 480 800 560 L800 800 L0 800Z" fill="#fff"/>'+''.join(figure(x,y,160,'#1a1a3a',pose=p,hair='#1a1a3a') for x,y,p in [(140,600,'wave'),(240,580,'up'),(340,580,'wave'),(440,590,'stand')])
I[1333]=svg(b,d)

# 1709 ちょこっとLOVE: a chocolate bar with one bite gone and a pink heart foil, sparkly kid-pop
d,b=bg([(0,'#ffd8ec'),(1,'#ffb0d0')])
b+=''.join(star5(x,y,18,'#fff') for x,y in [(120,140),(680,180),(140,640),(660,640)])
b+='<rect x="240" y="200" width="320" height="420" rx="16" fill="#6a3a1a"/>'+''.join(f'<rect x="{x}" y="{y}" width="130" height="110" rx="8" fill="#7a4a24"/>' for x in (262,408) for y in (220,350,480))
b+='<circle cx="560" cy="200" r="70" fill="#ffd8ec"/>'+'<path d="M240 520 L560 520 L560 620 L240 620Z" fill="#ff5a9a"/>'+heart(400,560,40,'#fff')
I[1709]=svg(b,d)

# 253 DOWNTOWN BOY: a rich girl's white convertible stopped next to a boy with a bike in a downtown alley
d,b=bg([(0,'#3a3a5a'),(1,'#a88a9a')])
b+=skyline(560,'#2a2a3a',253,120,360,'#ffd27a',60)+'<rect y="560" width="800" height="240" fill="#3a3a44"/>'
b+='<path d="M60 640 L100 580 L320 574 L370 610 L420 616 L420 670 L60 670Z" fill="#f4f4f8"/><circle cx="120" cy="672" r="24" fill="#1a1a1a"/><circle cx="360" cy="672" r="24" fill="#1a1a1a"/>'+figure(220,600,100,'#000',hair='#000')
b+=figure(580,670,200,'#000')+ring(520,680,40,'#000',8)+ring(660,680,40,'#000',8)+'<path d="M520 680 L580 620 L660 680 M580 620 L620 620" stroke="#000" stroke-width="8" fill="none"/>'
I[253]=svg(b,d)

# 515 KISS: a glass of iced tea with two straws and a lipstick mark on the rim, summer sweetness
d,b=bg([(0,'#ffe0b0'),(1,'#ffb890')])
b+='<path d="M290 260 L510 260 L480 680 L320 680Z" fill="#cfefff" opacity=".6"/><path d="M296 340 L504 340 L480 680 L320 680Z" fill="#c8702a" opacity=".85"/>'+''.join(f'<rect x="{x}" y="{y}" width="50" height="50" rx="8" fill="#fff" opacity=".6" transform="rotate({a} {x} {y})"/>' for x,y,a in [(330,380,10),(410,420,-14),(360,500,20)])
b+='<path d="M380 340 L340 140" stroke="#e8402a" stroke-width="12" stroke-linecap="round"/><path d="M430 340 L470 150" stroke="#2a6aff" stroke-width="12" stroke-linecap="round"/><path d="M470 262 Q490 250 506 262 Q490 276 470 262Z" fill="#c8102a"/>'
I[515]=svg(b,d)

# 558 Witches: a witch's hat and broom silhouette against a big pink full moon, fairy-tale 80s idol
d,b=bg([(0,'#2a1a4a'),(1,'#6a3a8a')])
b+=starsf(70,558,800)+'<circle cx="400" cy="380" r="210" fill="#ffc0d8"/>'
b+='<path d="M150 520 L620 420" stroke="#3a1a1a" stroke-width="10"/><path d="M620 420 L720 380 L700 450Z" fill="#3a1a1a"/>'+figure(400,500,180,'#1a0a2a',hair='#1a0a2a')+'<path d="M340 330 L400 210 L460 330Z" fill="#1a0a2a"/><rect x="320" y="320" width="160" height="18" rx="9" fill="#1a0a2a"/>'
I[558]=svg(b,d)

# 759 マシンガンをぶっ放せ: a mushroom cloud dissolving into a peace sign, protest rock, ochre and black
d,b=bg([(0,'#3a2a1a'),(1,'#a8784a')])
b+='<rect y="640" width="800" height="160" fill="#2a1a0a"/><path d="M370 640 L360 420 L440 420 L430 640Z" fill="#e8c890"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f4d8a8"/>' for x,y,r in [(320,340,90),(480,340,90),(400,280,110),(400,380,70)])
b+=ring(400,300,70,'#1a1a1a',14)+'<path d="M400 230 L400 370 M400 300 L350 350 M400 300 L450 350" stroke="#1a1a1a" stroke-width="14" stroke-linecap="round"/>'
I[759]=svg(b,d)

# 1334 ハート・エレキ: a red heart-shaped electric guitar with lightning sparks, 70s rock homage
d,b=bg([(0,'#1a1a3a'),(1,'#3a1a3a')])
b+=bolt([(120,100),(200,220),(150,260),(240,400)],'#ffd02a',10)+bolt([(680,120),(600,240),(660,280),(560,420)],'#ffd02a',10)
b+='<g transform="rotate(-25 400 460)">'+heart(400,520,150,'#e8102a')+'<rect x="388" y="100" width="24" height="360" fill="#2a1a1a"/><rect x="372" y="70" width="56" height="50" rx="8" fill="#2a1a1a"/><rect x="360" y="500" width="80" height="16" fill="#f4f4f4"/><circle cx="400" cy="560" r="20" fill="#f4f4f4"/></g>'
I[1334]=svg(b,d)

# 37 北の漁場: a fishing boat battling high waves in the cold northern sea, flags flying, enka
d,b=bg([(0,'#2a3a4a'),(1,'#5a6a7a')])
b+=snow(40,37,.5)+'<path d="M0 520 Q100 440 200 500 Q300 420 400 490 Q500 400 600 480 Q700 420 800 500 L800 800 L0 800Z" fill="#1a3a5a"/><path d="M0 600 Q120 540 240 590 Q360 520 480 580 Q600 520 800 590 L800 800 L0 800Z" fill="#0a2a4a"/>'
b+='<g transform="rotate(-10 400 470)"><path d="M260 470 L560 470 L520 540 L300 540Z" fill="#e8e8e8"/><rect x="380" y="400" width="90" height="70" fill="#c8102a"/><path d="M420 400 L420 260" stroke="#1a1a1a" stroke-width="6"/>'+''.join(f'<rect x="{422+k*4}" y="{270+k*30}" width="60" height="22" fill="{c}"/>' for k,c in enumerate(['#ffd02a','#e8102a','#2a6aff']))+'</g>'
I[37]=svg(b,d)

# 135 YONA YONA DANCE: a mirror ball and a big glamorous diva silhouette dancing night after night, city-pop neon
d,b=bg([(0,'#1a0a3a'),(1,'#5a1a5a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff4aa8" stroke-width="2" opacity=".2"/>' for y in range(560,800,30))+'<circle cx="620" cy="140" r="70" fill="#d8d8e8"/>'+rays(620,140,20,'#fff',.12,4)+moon(140,140,40,'#fff6dc',.2)
b+=figure(380,660,320,'#000',pose='up',hair='#000')+'<path d="M330 520 Q380 680 450 520Z" fill="#000"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(200,300,18),(560,360,22),(480,240,14)])
I[135]=svg(b,d)

# 376 旅立ちはフリージア: a bouquet of yellow freesia on an Orient-Express-style train seat by a window
d,b=bg([(0,'#f8e8c8'),(1,'#e8c898')])
b+='<rect x="100" y="120" width="600" height="320" rx="30" fill="#a8d0e8"/>'+hills(380,30,'#6aa86a',376)+'<rect x="100" y="120" width="600" height="320" rx="30" fill="none" stroke="#5a2a1a" stroke-width="20"/>'
b+='<rect y="440" width="800" height="360" fill="#7a1a2a"/><path d="M380 700 L400 520 M400 700 L420 520 M420 700 L440 530" stroke="#3a8a3a" stroke-width="6"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="14" fill="#ffd82a" transform="rotate({a} {x} {y})"/>' for x,y,a in [(390,510,-30),(410,490,10),(440,500,40),(380,540,-50),(450,530,30),(420,470,0)])
I[376]=svg(b,d)

# 401 優しい雨: soft rain falling on a quiet hydrangea garden, a woman under a clear umbrella
d,b=bg([(0,'#9aa8c8'),(1,'#d8e0ec')])
b+=rain(80,401,'#fff',.3)+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity=".9"/>' for x,y,r,c in [(120,640,70,'#8a7ae8'),(220,700,60,'#5a9ae8'),(640,650,80,'#b07ae8'),(720,720,60,'#5a9ae8')])
b+=figure(420,720,280,'#2a2a4a',hair='#2a2a4a')+'<path d="M260 420 Q420 260 580 420Z" fill="#e8f4ff" opacity=".6" stroke="#fff" stroke-width="4"/><path d="M420 420 L420 540" stroke="#fff" stroke-width="4"/>'
I[401]=svg(b,d)

# 593 Silent Jealousy: a grand piano engulfed in red and black flames, fast metal ballad
d,b=bg([(0,'#0a0000'),(1,'#2a0004')])
b+=''.join(f'<path d="M{x} 800 Q{x-30} {600-(x%7)*20} {x+20} {420-(x%5)*30} Q{x+40} 600 {x+60} 800Z" fill="{c}" opacity=".8"/>' for x,c in zip(range(-20,800,70),['#c8000a','#ff4a1a','#c8000a','#ff4a1a']*4))
b+='<path d="M150 480 Q150 400 290 400 L620 400 Q720 400 720 500 L720 540 L150 540Z" fill="#050505"/>'+''.join(f'<rect x="{x}" y="500" width="20" height="40" fill="#f4f4f4"/>' for x in range(170,700,24))
I[593]=svg(b,d)

# 599 WAO!: a burst of an aquamarine soda can popping, retro rock-and-roll lettering-free comic burst
d,b=bg([(0,'#3ad0e0'),(1,'#d0f8ff')])
b+='<polygon points="'+' '.join(f'{400+(320 if k%2 else 200)*math.cos(k*math.pi/12):.0f},{380+(320 if k%2 else 200)*math.sin(k*math.pi/12):.0f}' for k in range(24))+'" fill="#ffd02a"/>'
b+='<rect x="320" y="300" width="160" height="300" rx="20" fill="#e8f4ff"/><rect x="320" y="380" width="160" height="120" fill="#2a8ad8"/><ellipse cx="400" cy="300" rx="80" ry="16" fill="#c8d8e8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x,y,r in [(400,240,14),(430,190,10),(380,160,12),(450,130,8)])
I[599]=svg(b,d)

# 712 未来のために: a baseball soaring out of a stadium at night toward the future skyline
d,b=bg([(0,'#0a1a3a'),(1,'#1a3a5a')])
b+=starsf(60,712,400)+''.join(glow(x,120,60,'#fff',.5)+f'<rect x="{x-30}" y="100" width="60" height="40" fill="#fff"/>' for x in (120,680))
b+='<path d="M0 560 Q400 440 800 560 L800 800 L0 800Z" fill="#2a7a3a"/><path d="M0 560 Q400 440 800 560" stroke="#1a1a2a" stroke-width="40" fill="none"/>'
b+='<path d="M300 700 Q420 400 560 200" stroke="#fff" stroke-width="4" stroke-dasharray="12 10" fill="none"/><circle cx="560" cy="200" r="24" fill="#fff"/>'+figure(300,720,160,'#000',pose='up')
I[712]=svg(b,d)

# 771 君が思い出になる前に: an old film camera with a photo slowly developing of a girl by the sea, nostalgia
d,b=bg([(0,'#bfe4f0'),(1,'#f4f0e4')])
b+='<rect x="380" y="180" width="300" height="340" fill="#fff" transform="rotate(6 530 350)"/><rect x="400" y="200" width="260" height="240" fill="#7ac0d8" opacity=".55" transform="rotate(6 530 350)"/>'
b+='<rect x="100" y="420" width="300" height="200" rx="20" fill="#2a2a2a"/><circle cx="250" cy="520" r="70" fill="#5a5a5a"/><circle cx="250" cy="520" r="44" fill="#1a1a2a"/><rect x="130" y="400" width="80" height="30" fill="#2a2a2a"/>'
I[771]=svg(b,d)

# 807 Save your dream: a dream bubble with a star held safe inside cupped hands, pastel chocolate pink
d,b=bg([(0,'#ffd8e8'),(1,'#e8c8ff')])
b+=glow(400,360,160,'#fff',.6)+'<circle cx="400" cy="360" r="130" fill="#fff" opacity=".3" stroke="#fff" stroke-width="5"/>'+star5(400,360,70,'#ffd02a')+'<ellipse cx="360" cy="300" rx="30" ry="14" fill="#fff" opacity=".7"/>'
b+='<path d="M220 560 Q260 480 380 490 L380 530 Q300 530 280 620Z M580 560 Q540 480 420 490 L420 530 Q500 530 520 620Z" fill="#f0c8a8"/>'
I[807]=svg(b,d)

# 899 Body & Soul: four teen girl dancers mid-jump against a pop-art Okinawa sun, energetic 1996
d,b=bg([(0,'#ff7a2a'),(1,'#ffd02a')])
b+=rays(400,300,24,'#fff',.2,6)+'<circle cx="400" cy="300" r="80" fill="#fff6c0"/>'+'<rect y="620" width="800" height="180" fill="#1a1a2a"/>'
b+=''.join(figure(x,y,190,'#1a1a2a',pose=p,hair='#1a1a2a') for x,y,p in [(180,600,'up'),(320,560,'wave'),(480,580,'up'),(620,600,'reach')])
I[899]=svg(b,d)

# 1038 つつみ込むように・・・: a soft glowing aura wrapping a small curled-up figure, warm R&B tones
d,b=bg([(0,'#2a1a3a'),(1,'#5a3a5a')])
b+=''.join(ring(400,420,r,'#ffb88a',8,.7-r/600) for r in (120,180,240,300))+glow(400,420,160,'#ffd8a0',.5)
b+=heart(400,430,70,'#ff8a9a')+'<path d="M220 600 Q200 420 330 360 L350 400 Q260 460 280 600Z M580 600 Q600 420 470 360 L450 400 Q540 460 520 600Z" fill="#e8b090"/>'
I[1038]=svg(b,d)

# 1066 戻れない明日: a girl's hand pulling a friend up a steep staircase toward morning light
d,b=bg([(0,'#ffd8a8'),(1,'#fff4e0')])
b+=''.join(f'<rect x="{100+k*70}" y="{740-k*70}" width="{700-k*70}" height="70" fill="{"#c8b8a8" if k%2 else "#d8c8b8"}"/>' for k in range(9))+glow(700,100,140,'#fff',.6)
b+=figure(470,460,190,'#3a2a3a',pose='reachL',hair='#3a2a3a')+figure(320,600,180,'#3a2a3a',pose='reach')
I[1066]=svg(b,d)

# 1665 深い森: a deep misty forest with a single shaft of light and a lone small figure on a path
d,b=bg([(0,'#1a2a24'),(1,'#3a4a40')])
b+=''.join(f'<rect x="{x}" y="0" width="{w}" height="800" fill="#0a1410"/>' for x,w in [(40,60),(160,40),(560,50),(680,70),(300,30)])+'<polygon points="420,0 520,0 480,800 320,800" fill="#e8ffe0" opacity=".2"/>'
b+='<rect y="420" width="800" height="80" fill="#fff" opacity=".12"/><path d="M380 800 Q400 640 420 560" stroke="#5a6a4a" stroke-width="60" fill="none"/>'+figure(420,600,110,'#000')
I[1665]=svg(b,d)

# 457 恋はくえすちょん: a giant pink question mark made of hearts, a princess's sweet dumpling (anmitsu) cup
d,b=bg([(0,'#fff0f6'),(1,'#ffd0e4')])
b+='<path d="M300 260 Q300 140 410 140 Q520 140 520 240 Q520 320 420 360 L420 440" stroke="#ff5a9a" stroke-width="50" fill="none" stroke-linecap="round"/><circle cx="420" cy="540" r="32" fill="#ff5a9a"/>'
b+='<path d="M520 600 L700 600 L670 700 L550 700Z" fill="#e8f4ff"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}"/>' for x,y,c in [(570,590,'#fff'),(610,580,'#ffb0c8'),(650,590,'#8ad86a')])+heart(610,560,14,'#e8102a')
I[457]=svg(b,d)

# 499 15の夜: a teen riding a stolen motorbike out of a sleeping town at night, rebellion
d,b=bg([(0,'#04081a'),(1,'#1a2440')])
b+=starsf(80,499,400)+moon(640,160,40)+skyline(560,'#0a0e1a',499,40,160,'#ffd27a',30)+'<rect y="560" width="800" height="240" fill="#141418"/>'
b+='<polygon points="400,560 300,800 500,800" fill="#fff4b0" opacity=".12"/>'+ring(300,680,46,'#000',16)+ring(520,680,46,'#000',16)+'<path d="M300 680 L380 600 L480 600 L520 680 M380 600 L360 570" stroke="#000" stroke-width="14" fill="none"/>'
b+=figure(420,610,170,'#000',pose='reach')
I[499]=svg(b,d)

# 524 うれしい!たのしい!大好き!: three bouncing round faces of joy — no faces, just three balloons with hearts, late-80s pop
d,b=bg([(0,'#fff0a0'),(1,'#ffc8a0')])
b+=''.join(f'<path d="M{x} {y+80} Q{x+10} {y+200} {x-20} 760" stroke="#5a5a5a" stroke-width="3" fill="none"/><ellipse cx="{x}" cy="{y}" rx="80" ry="92" fill="{c}"/><ellipse cx="{x-30}" cy="{y-36}" rx="16" ry="24" fill="#fff" opacity=".5"/>' for x,y,c in [(230,320,'#ff4a6a'),(400,240,'#ffb02a'),(570,320,'#3ab0ff')])
b+=heart(400,240,30,'#fff')+star5(230,320,30,'#fff')+sparkle(570,320,30,'#fff')
I[524]=svg(b,d)

# 725 ゲレンデがとけるほど恋したい: a heart melting the ski slope snow, ski lift and goggles, 1995
d,b=bg([(0,'#3aa0ff'),(1,'#d8f0ff')])
b+='<path d="M0 360 L800 640 L800 800 L0 800Z" fill="#fff"/><path d="M0 200 L800 300" stroke="#3a3a3a" stroke-width="4"/>'+''.join(f'<path d="M{x} {200+x/8} L{x} {260+x/8}" stroke="#3a3a3a" stroke-width="4"/><rect x="{x-20}" y="{260+x/8}" width="40" height="24" fill="#e8402a"/>' for x in (200,500))
b+=glow(400,560,120,'#ff6a8a',.5)+heart(400,560,70,'#ff3a6a')+'<path d="M330 620 Q340 680 320 720 M470 620 Q460 690 480 730" stroke="#7ac8ff" stroke-width="10" fill="none" opacity=".7"/>'
I[725]=svg(b,d)

# 848 GLOBAL COMMUNICATION: a globe wrapped in glowing communication lines connecting tiny figures
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
b+=starsf(60,848,800)+'<circle cx="400" cy="420" r="220" fill="#1a4a8a"/>'+''.join(f'<path d="M{400+220*math.cos(a)} {420+220*math.sin(a)} Q400 200 {400+220*math.cos(a+2)} {420+220*math.sin(a+2)}" stroke="#7ae8ff" stroke-width="3" fill="none" opacity=".7"/>' for a in (0.3,1.4,2.6,3.8,5.0))
b+='<path d="M250 340 Q320 300 360 360 Q340 420 280 400Z M440 460 Q520 420 560 480 Q520 540 460 520Z" fill="#3a8a4a"/>'+''.join(figure(400+240*math.cos(a),420+240*math.sin(a)+10,40,'#fff') for a in (-1.2,-0.2,2.0,3.4))
I[848]=svg(b,d)

# 1714 evergreen: a single evergreen fir in snow beneath a soft pale sky, quiet remembrance
d,b=bg([(0,'#c8d4e0'),(1,'#f0f4f8')])
b+=snow(60,1714,.7)+'<rect y="620" width="800" height="180" fill="#fff"/>'
b+=''.join(f'<polygon points="400,{y} {400-w},{y+160} {400+w},{y+160}" fill="#2a5a3a"/>' for y,w in [(180,90),(260,130),(350,170),(440,210)])+'<rect x="384" y="600" width="32" height="40" fill="#4a3a2a"/>'
I[1714]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
