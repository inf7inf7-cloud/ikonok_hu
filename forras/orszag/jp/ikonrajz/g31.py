import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 31. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'
def piece(x,y,s,col,rot=0): return f'<path transform="translate({x} {y}) rotate({rot}) scale({s/100})" d="M-50 -50 L-12 -50 Q-14 -72 0 -72 Q14 -72 12 -50 L50 -50 L50 -12 Q72 -14 72 0 Q72 14 50 12 L50 50 L12 50 Q14 28 0 28 Q-14 28 -12 50 L-50 50 L-50 12 Q-28 14 -28 0 Q-28 -14 -50 -12Z" fill="{col}"/>'

# 1881 PUZZLE: a jigsaw puzzle of a sunny landscape with one missing piece, held in a hand
d,b=bg([(0,'#2a2a3a'),(1,'#4a4a5a')])
b+=''.join(piece(x,y,100,c) for x,y,c in [(250,250,'#6ac8ff'),(400,250,'#8ad8ff'),(550,250,'#6ac8ff'),(250,400,'#ffd27a'),(550,400,'#ffd27a'),(250,550,'#5ab85a'),(400,550,'#4aa84a'),(550,550,'#5ab85a')])
b+='<rect x="340" y="340" width="120" height="120" fill="#1a1a24"/>'+piece(660,180,90,'#ffc040',25)+glow(660,180,80,'#fff',.25)
I[1881]=svg(b,d)

# 237 浅い眠り: a woman half asleep on a pillow under a pale moon, thin dream mist, early-90s drama
d,b=bg([(0,'#1a1a3a'),(1,'#4a4a7a')])
b+=moon(600,180,50,'#f4f0ff',.4)+''.join(f'<path d="M{x} {y} q60 -30 120 0 q60 30 120 0" stroke="#c8c8ff" stroke-width="5" fill="none" opacity=".35"/>' for x,y in [(80,300),(240,360),(160,420)])
b+='<rect x="60" y="520" width="680" height="200" rx="40" fill="#e8e4f4"/><ellipse cx="220" cy="520" rx="140" ry="50" fill="#fff"/>'+profile(240,520,.7,'#2a2a3a')+'<path d="M300 540 Q500 500 740 560 L740 720 L300 720Z" fill="#9a9ad0"/>'
I[237]=svg(b,d)

# 248 守ってあげたい: a big hand shielding a small paper boat from rain under a protective umbrella of fingers
d,b=bg([(0,'#5a7aa8'),(1,'#a8c0d8')])
b+=rain(80,248,'#fff',.35)+'<rect y="560" width="800" height="240" fill="#4a6a8a"/>'+''.join(f'<path d="M{x} 600 q30 -12 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".4"/>' for x in range(40,800,140))
b+='<path d="M330 560 L470 560 L440 600 L360 600Z" fill="#fff"/><path d="M400 470 L400 560 L460 560Z" fill="#f4f0e8"/>'
b+='<path d="M140 400 Q400 200 660 400 Q640 420 620 410 Q400 260 180 410 Q160 420 140 400Z" fill="#f0c8a8"/>'
I[248]=svg(b,d)

# 295 ガンダーラ: a golden fantasy temple silhouette on a far mountain at sunrise, a traveller with a staff
d,b=bg([(0,'#ffb05a'),(.6,'#ffd8a0'),(1,'#fff4d8')])
b+=glow(530,300,130,'#fff4b0',.6)+hills(420,60,'#c8906a',295,4)+'<g fill="#a85a2a"><rect x="440" y="360" width="180" height="40"/><rect x="460" y="330" width="140" height="34"/><path d="M470 332 Q470 250 530 240 Q590 250 590 332Z"/><rect x="522" y="190" width="16" height="54"/><path d="M510 200 L550 200 L530 170Z"/></g>'+''.join(sparkle(x,y,10,'#fff') for x,y in [(460,230),(610,260)])
b+='<path d="M0 600 Q400 540 800 620 L800 800 L0 800Z" fill="#8a5a3a"/>'+figure(240,640,200,'#2a1a10')+'<path d="M290 440 L320 650" stroke="#2a1a10" stroke-width="8"/>'
I[295]=svg(b,d)

# 449 シンデレラは眠れない: a glass slipper on a satin pillow under a clock at almost midnight, glam 80s
d,b=bg([(0,'#1a0a3a'),(1,'#4a2a6a')])
b+=starsf(60,449,500)+ring(400,220,110,'#f4e0a0',10)+'<circle cx="400" cy="220" r="100" fill="#f8f0d8"/><path d="M400 220 L400 140 M400 220 L390 130" stroke="#2a1a3a" stroke-width="8" stroke-linecap="round"/>'
b+='<ellipse cx="400" cy="600" rx="220" ry="60" fill="#c8102a"/><path d="M300 580 Q300 500 380 500 L460 520 Q520 540 520 580Z" fill="#cfe8ff" opacity=".85"/>'+sparkle(500,500,24,'#fff')
I[449]=svg(b,d)

# 1161 笑顔: a sunflower turning toward a beaming sun with a smiling curve in the sky, kids' warm palette
d,b=bg([(0,'#7ad0ff'),(1,'#e0f6ff')])
b+=rays(560,220,20,'#fff',.3,8)+'<circle cx="560" cy="220" r="90" fill="#ffe46a"/><path d="M520 240 Q560 280 600 240" stroke="#e88a2a" stroke-width="8" fill="none"/>'
b+=hills(620,30,'#6ab85a',1161)+'<path d="M300 800 L300 480" stroke="#3a8a2a" stroke-width="14"/>'+flower(300,440,140,16,'#ffd02a','#7a4a1a')
I[1161]=svg(b,d)

# 1247 DON'T U EVER STOP: a figure walking forward through a dark neon city in rain, a red scarf flying
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=skyline(520,'#141420',1247,120,400,'#ff3a6a',70)+rain(60,1247,'#9ab0d8',.35)+'<rect y="520" width="800" height="280" fill="#0a0a10"/>'
b+=figure(400,720,320,'#000')+'<path d="M380 460 Q300 440 200 470 Q300 470 380 490Z" fill="#e8102a"/>'+''.join(f'<rect x="{x}" y="540" width="6" height="{80+x%60}" fill="#ff3a6a" opacity=".3"/>' for x in range(30,800,90))
I[1247]=svg(b,d)

# 1329 前しか向かねえ: a girl in a school uniform walking forward on a long road, petals blowing behind
d,b=bg([(0,'#7ac0ff'),(1,'#f0f8ff')])
b+='<polygon points="400,380 0,800 800,800" fill="#c8c8c8"/><polygon points="400,380 360,800 440,800" fill="#fff" opacity=".4"/>'+hills(400,20,'#7ab87a',1329)+petals(30,1329,'#ffc0d0',380,800)
b+=figure(400,700,280,'#1a1a3a',pose='reach',hair='#1a1a3a')
I[1329]=svg(b,d)

# 1855 フィクション: an open storybook with paper figures and a sun popping up from its pages
d,b=bg([(0,'#ffe8c8'),(1,'#ffc8a0')])
b+='<path d="M80 560 Q240 500 400 550 Q560 500 720 560 L720 680 Q560 630 400 680 Q240 630 80 680Z" fill="#fffaf2"/><path d="M400 550 L400 680" stroke="#d8c8b8" stroke-width="4"/>'
b+='<path d="M250 540 L250 380 L330 300 L410 380 L410 540Z" fill="#ff8a6a"/><circle cx="560" cy="330" r="70" fill="#ffd02a"/>'+rays(560,330,14,'#ffd02a',.3,6)+figure(500,540,120,'#3a3a6a')+tree(650,540,120,'#4aa84a')
I[1855]=svg(b,d)

# 325 駅: a woman glimpsing her old love across a crowded station platform at dusk, city pop pastel
d,b=bg([(0,'#5a5a8a'),(1,'#e8a0a0')])
b+='<rect y="0" width="800" height="120" fill="#2a2a3a"/>'+''.join(f'<rect x="{x}" y="120" width="12" height="440" fill="#3a3a4a"/>' for x in (120,400,680))+'<rect x="240" y="150" width="320" height="50" fill="#1a1a2a"/>'+txt(400,188,'駅',36,'#fff')
b+='<rect y="560" width="800" height="240" fill="#6a6a7a"/>'+''.join(figure(x,600,h,'#2a2a3a') for x,h in [(80,200),(200,220),(520,210),(740,190)])+figure(320,600,230,'#000',hair='#000')+figure(620,600,240,'#000')
I[325]=svg(b,d)

# 462 渚の『・・・・・』: a beach with four dots of ellipsis written in the sand, a wave about to wash them, pop 80s
d,b=bg([(0,'#4ad0ff'),(1,'#d0f4ff')])
b+='<rect y="360" width="800" height="200" fill="#2ab0d8"/><path d="M0 560 Q200 520 400 560 Q600 600 800 560 L800 800 L0 800Z" fill="#f8e8c0"/><path d="M0 560 Q200 520 400 560 Q600 600 800 560" stroke="#fff" stroke-width="12" fill="none"/>'
b+=''.join(f'<circle cx="{x}" cy="680" r="18" fill="#c8a870"/>' for x in (250,350,450,550))+txt(400,280,'『　』',120,'#fff',900,op=.8)+cloud(620,160,1)
I[462]=svg(b,d)

# 557 ROSÉCOLOR: a soft pink rose blooming in a spring breeze, glossy cosmetic pastel
d,b=bg([(0,'#ffe0e8'),(1,'#ffc0d0')])
b+=glow(400,400,240,'#fff',.5)+'<g transform="translate(400 400) scale(2.2)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#f48aa8',1),(72,'#f8a0b8',.95),(144,'#f48aa8',.95),(216,'#f8a0b8',.95),(288,'#f48aa8',.95),(36,'#e86a90',.6),(180,'#e86a90',.55)])+'<circle r="10" fill="#d84a7a"/></g>'
b+=petals(10,557,'#ffb0c8')
I[557]=svg(b,d)

# 1126 KISS OF DEATH: two red lips framed by a black-and-red mecha cockpit glow, dark sci-fi romance
d,b=bg([(0,'#0a0a10'),(1,'#2a0a14')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff2a3a" stroke-width="2" opacity=".2"/>' for y in range(40,800,40))+glow(400,420,200,'#ff2a3a',.4)
b+='<path d="M220 420 Q300 340 380 380 Q400 370 420 380 Q500 340 580 420 Q500 540 400 540 Q300 540 220 420Z" fill="#e8102a"/><path d="M240 422 Q400 460 560 422 Q400 440 240 422Z" fill="#4a0010"/>'
b+='<path d="M100 120 L300 120 L260 160 L100 160Z M700 120 L500 120 L540 160 L700 160Z" fill="#c8102a"/>'
I[1126]=svg(b,d)

# 1330 シュートサイン: a wrestling ring with a spotlight and a gloved fist raised in challenge
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<polygon points="400,0 220,520 580,520" fill="#fff" opacity=".12"/><path d="M80 520 L720 520 L800 640 L0 640Z" fill="#2a4ac8"/>'+''.join(f'<path d="M{80-k*20} {440+k*30} L{720+k*20} {440+k*30}" stroke="#e8102a" stroke-width="7"/>' for k in range(3))+'<rect x="60" y="400" width="20" height="240" fill="#c8c8d0"/><rect x="720" y="400" width="20" height="240" fill="#c8c8d0"/>'
b+=figure(400,520,280,'#000',pose='wave',hair='#000')
I[1330]=svg(b,d)

# 1428 トイレの神様: a sparkling clean bathroom with a goddess-like glow and grandma's hand holding a cleaning cloth
d,b=bg([(0,'#e0f0ff'),(1,'#ffffff')])
b+=''.join(f'<rect x="{x}" y="{y}" width="96" height="96" fill="none" stroke="#c8d8e8" stroke-width="3"/>' for x in range(0,800,100) for y in range(0,500,100))+'<rect y="500" width="800" height="300" fill="#d8e0e8"/>'
b+=glow(400,280,160,'#fff4b0',.6)+sparkle(400,260,70,'#ffd02a')+sparkle(300,330,24,'#ffd02a')+sparkle(500,320,30,'#ffd02a')
b+='<path d="M200 680 Q260 600 340 580 L360 620 Q300 650 260 720Z" fill="#e8c8a8"/><rect x="330" y="570" width="90" height="60" rx="10" fill="#ff8aa8"/>'
I[1428]=svg(b,d)

# 1453 カオスが極まる: a football striking a goal net in an explosion of chaotic blue lines
d,b=bg([(0,'#04081a'),(1,'#0a1a4a')])
b+=''.join(f'<path d="M400 400 L{400+600*math.cos(a)} {400+600*math.sin(a)}" stroke="#3ab0ff" stroke-width="{2+k%4}" opacity=".5"/>' for k,a in enumerate([i*0.37 for i in range(40)]))
b+=''.join(f'<path d="M{x} 0 L{x} 800" stroke="#fff" stroke-width="2" opacity=".15"/>' for x in range(0,800,40))+''.join(f'<path d="M0 {y} L800 {y}" stroke="#fff" stroke-width="2" opacity=".15"/>' for y in range(0,800,40))
b+=glow(400,400,120,'#3ad0ff',.6)+'<circle cx="400" cy="400" r="90" fill="#fff"/><polygon points="400,350 440,380 425,425 375,425 360,380" fill="#1a1a1a"/>'
I[1453]=svg(b,d)

# 1695 桜、みんなで食べた: a picnic of cherry-blossom mochi on a sheet under sakura, monorail passing behind
d,b=bg([(0,'#bfe6ff'),(1,'#fff0f4')])
b+='<rect x="0" y="260" width="800" height="24" fill="#b8b8c0"/><rect x="420" y="200" width="300" height="60" rx="26" fill="#f4f4f8"/><rect x="430" y="214" width="280" height="14" fill="#2a8ac8"/>'
b+=''.join(sakura(x,y,s,'#ffc0d6','#ff7aa8',r) for x,y,s,r in [(120,160,60,10),(220,100,50,-20),(80,300,46,30)])+petals(26,1695,'#ffc8d8')
b+='<polygon points="120,600 680,600 760,760 40,760" fill="#3a8ac8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="28" fill="#ffc0d0"/><path d="M{x-28} {y} Q{x} {y-40} {x+28} {y}" fill="#5aa85a"/>' for x,y in [(300,660),(380,690),(460,660),(540,700)])
I[1695]=svg(b,d)

# 1732 AwA AwA: a group of runners leaping over a towering wall of bubbles, energetic orange
d,b=bg([(0,'#ff8a2a'),(1,'#ffd06a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".35"/>'+ring(x,y,r,'#fff',3,.7) for x,y,r in [(140,520,60),(260,440,80),(400,540,70),(540,430,90),(660,540,60),(330,300,40),(600,260,30)])
b+=''.join(figure(x,y,140,'#2a1a0a',pose='up') for x,y in [(220,360),(400,300),(580,360)])
I[1732]=svg(b,d)

# 710 このまま君だけを奪い去りたい: a man pulling a woman's hand as they run off into a city night, pager glow
d,b=bg([(0,'#0a1028'),(1,'#2a3a6a')])
b+=skyline(560,'#141c34',710,100,300,'#ffd27a',80)+'<rect y="560" width="800" height="240" fill="#0a0e1a"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#ffd27a" stroke-width="3" opacity=".25"/>' for y in (620,680,740))
b+=figure(460,720,260,'#000',pose='reachL')+figure(300,720,240,'#000',pose='reach',hair='#000')
I[710]=svg(b,d)

# 957 光の気配: a curtain gently lifting in a quiet room as morning light streams in, minimal ballad
d,b=bg([(0,'#e8e4dc'),(1,'#c8c0b4')])
b+='<rect x="200" y="100" width="400" height="500" fill="#fff8e0"/>'+glow(400,350,240,'#fff4c8',.6)+'<polygon points="200,600 600,600 760,800 40,800" fill="#fff4c8" opacity=".35"/>'
b+='<path d="M200 100 L320 100 Q300 360 360 600 L200 600Z" fill="#f4f4f8" opacity=".9"/><path d="M600 100 L500 100 Q560 300 470 600 L600 600Z" fill="#f4f4f8" opacity=".8"/>'
I[957]=svg(b,d)

# 1080 ラブ,トゥー,デス,トゥー: a heart split half red, half black with two dice showing two, cabaret tango palette
d,b=bg([(0,'#1a0a0a'),(1,'#3a0a14')])
b+='<clipPath id="hl"><rect x="0" y="0" width="400" height="800"/></clipPath>'
b+=heart(400,380,170,'#e8102a')+'<g clip-path="url(#hl)">'+heart(400,380,170,'#111')+'</g>'+'<path d="M400 240 L400 560" stroke="#fff" stroke-width="5" stroke-dasharray="14 10"/>'
b+=''.join(f'<g transform="rotate({a} {x} {y})"><rect x="{x-44}" y="{y-44}" width="88" height="88" rx="14" fill="#fff"/><circle cx="{x-18}" cy="{y-18}" r="9" fill="#111"/><circle cx="{x+18}" cy="{y+18}" r="9" fill="#111"/></g>' for x,y,a in [(260,640,-14),(540,640,12)])
I[1080]=svg(b,d)

# 1655 Have a nice day: a lone piano key-lit window in an apartment block at night, one plant on the sill
d,b=bg([(0,'#1a2a3a'),(1,'#3a4a5a')])
b+='<rect x="120" y="80" width="560" height="720" fill="#2a3440"/>'+''.join(f'<rect x="{x}" y="{y}" width="110" height="90" fill="#1a222a"/>' for x in (170,345,520) for y in (130,270,410,550))
b+='<rect x="345" y="410" width="110" height="90" fill="#ffd890"/>'+glow(400,455,90,'#ffd890',.5)+'<rect x="370" y="480" width="24" height="20" fill="#8a5a3a"/><path d="M382 480 Q370 450 360 446 M382 480 Q394 450 406 448" stroke="#3a9a3a" stroke-width="5" fill="none"/>'
I[1655]=svg(b,d)

# 1752 Say I do: a ring box opening with a sparkling ring, two hands, soft champagne glow
d,b=bg([(0,'#f8e8d8'),(1,'#e8c8b0')])
b+=glow(400,380,180,'#fff',.6)+'<rect x="300" y="380" width="200" height="120" rx="20" fill="#2a2a4a"/><path d="M300 380 L310 260 Q400 240 490 260 L500 380Z" fill="#3a3a5a"/><rect x="330" y="360" width="140" height="40" rx="10" fill="#fff"/>'
b+=ring(400,340,40,'#e8c86a',12)+sparkle(400,290,40,'#fff')+'<path d="M200 640 Q280 540 330 510 L350 540 Q300 590 270 680Z M600 640 Q520 540 470 510 L450 540 Q500 590 530 680Z" fill="#f0c8a8"/>'
I[1752]=svg(b,d)

# 1882 春夏秋冬: a single tree split into four quarters: pink spring, green summer, red autumn, white winter
d,b=bg([(0,'#e8eef4'),(1,'#d8e0e8')])
for k,(c,bgc) in enumerate([('#ffb0c8','#fff0f4'),('#4ab84a','#d8f4ff'),('#e86a2a','#fff0d8'),('#ffffff','#c8d8e8')]):
    x0=(k%2)*400;y0=(k//2)*400;b+=f'<rect x="{x0}" y="{y0}" width="400" height="400" fill="{bgc}"/>'
b+='<path d="M380 800 L390 420 L410 420 L420 800Z" fill="#6a4a2a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x,y,r,c in [(300,300,110,'#ffb0c8'),(500,300,110,'#4ab84a'),(300,470,90,'#e86a2a'),(500,470,90,'#ffffff')])
b+='<path d="M400 0 L400 800 M0 400 L800 400" stroke="#fff" stroke-width="4" opacity=".6"/>'
I[1882]=svg(b,d)

# 592 紅: a crimson-red sky with a lone figure screaming into the wind, scattered red petals, speed metal
d,b=bg([(0,'#3a0000'),(.5,'#c8000a'),(1,'#ff4a2a')])
b+=rays(400,800,30,'#000',.25,4,180,360)+''.join(f'<path d="M0 {y} Q400 {y-60} 800 {y}" stroke="#ff8a6a" stroke-width="3" fill="none" opacity=".4"/>' for y in (200,280,360))
b+=petals(40,592,'#ff1a1a')+'<path d="M0 640 L800 600 L800 800 L0 800Z" fill="#0a0000"/>'+figure(400,620,280,'#000',pose='up',hair='#000')+txt(620,180,'紅',140,'#1a0000',900,op=.8)
I[592]=svg(b,d)

# 1017 I WISH: a girl blowing on a dandelion clock, seeds flying toward a summer sky full of wishes
d,b=bg([(0,'#7ac8ff'),(1,'#fff4e0')])
b+=cloud(600,160,1.2)+hills(620,30,'#7ac85a',1017)+''.join(f'<g transform="translate({x} {y}) rotate({a})"><path d="M0 0 L0 20" stroke="#fff" stroke-width="2"/>'+''.join(f'<path d="M0 0 L{12*math.cos(t)} {12*math.sin(t)}" stroke="#fff" stroke-width="2"/>' for t in [k*math.pi/4-math.pi for k in range(5)])+'</g>' for x,y,a in [(500,300,10),(560,240,-20),(620,330,30),(680,220,5),(450,220,-10),(590,400,20)])
b+='<path d="M360 620 L380 440" stroke="#4a8a3a" stroke-width="6"/>'+ring(380,420,40,'#fff',5,.9)+profile(240,720,1.0,'#2a2a3a')
I[1017]=svg(b,d)

# 130 透明人間: an empty floating suit and hat with no body inside, disco dance floor lights, late-70s
d,b=bg([(0,'#1a0a3a'),(1,'#3a1a5a')])
b+=''.join(f'<rect x="{x}" y="{y}" width="98" height="58" fill="{c}" opacity=".7"/>' for x,y,c in [(x,y,['#ff3aa8','#3ad0ff','#ffd02a','#8a3aff'][(x//100+y//60)%4]) for x in range(0,800,100) for y in range(620,800,60)])
b+='<rect x="320" y="120" width="160" height="30" rx="8" fill="#f4f4f4"/><rect x="350" y="40" width="100" height="90" fill="#f4f4f4"/><path d="M300 260 L500 260 L520 460 L280 460Z" fill="#f4f4f4"/><path d="M290 470 L390 470 L380 600 L310 600Z M410 470 L510 470 L490 600 L420 600Z" fill="#f4f4f4"/>'
b+='<path d="M370 260 L400 330 L430 260" stroke="#c8102a" stroke-width="10" fill="none"/>'+''.join(sparkle(x,y,14,'#fff') for x,y in [(240,200),(580,240),(250,420),(560,520)])
I[130]=svg(b,d)

# 250 中央フリーウェイ: a car on an elevated highway at night with racetrack and brewery lights to either side
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=starsf(60,250,380)+'<rect y="380" width="800" height="420" fill="#0a0a14"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#ffd27a"/>' for x,y in [(60,420),(140,430),(220,410),(560,420),(640,440),(720,410),(680,460)])
b+='<path d="M400 380 L0 800 L800 800Z" fill="#2a2a3a"/>'+''.join(f'<path d="M400 380 L{x} 800" stroke="#ffd27a" stroke-width="3" stroke-dasharray="20 20" opacity=".7"/>' for x in (270,530))
b+='<rect x="310" y="620" width="180" height="70" rx="20" fill="#f4f4f8"/><rect x="330" y="600" width="140" height="40" rx="14" fill="#cfe0ff"/>'+glow(340,690,20,'#ff3a3a',.9,'glow2')+glow(460,690,20,'#ff3a3a',.9,'glow2')
I[250]=svg(b,d)

# 450 恋人達のペイヴメント: a couple sharing an umbrella on a shiny paved street lined with gas lamps
d,b=bg([(0,'#2a3a5a'),(1,'#6a7a9a')])
b+=rain(70,450,'#fff',.3)+'<rect y="560" width="800" height="240" fill="#4a4a5a"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#7a7a8a" stroke-width="3"/>' for y in range(600,800,40))
b+=''.join(f'<rect x="{x}" y="260" width="10" height="300" fill="#1a1a1a"/>'+glow(x+5,250,50,'#ffd27a',.6)+chochin(x+5,240,.25,'#ffd27a') for x in (120,660))
b+=figure(360,640,220,'#000')+figure(430,640,200,'#000',hair='#000')+wagasa(395,380,1.4,'#c8102a',0)
I[450]=svg(b,d)

# 1248 LIPS: a lipstick kiss mark on a mirror with a man's reflection in shadow
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<rect x="160" y="100" width="480" height="600" rx="240" fill="#5a6a7a"/><rect x="180" y="120" width="440" height="560" rx="220" fill="#8a9aaa"/>'+profile(420,700,1.6,'#2a3440',True)
b+='<path d="M300 360 Q350 320 400 340 Q450 320 500 360 Q450 420 400 420 Q350 420 300 360Z" fill="#c8102a" opacity=".9"/><path d="M310 362 Q400 380 490 362" stroke="#6a0010" stroke-width="5" fill="none"/>'
I[1248]=svg(b,d)

# 1393 from me to u: a glowing torch being passed from one hand to another, split utopia gold / dystopia grey
d,b=bg([(0,'#1a1a1a'),(1,'#2a2a2a')])
b+='<rect x="0" y="0" width="400" height="800" fill="#2a2a30"/><rect x="400" y="0" width="400" height="800" fill="#ffd8e8"/>'+''.join(f'<rect x="{x}" y="{y}" width="40" height="80" fill="#1a1a20"/>' for x,y in [(40,400),(120,320),(220,450),(300,360)])+''.join(heart(x,y,20,'#ff6aa8','opacity=".6"') for x,y in [(520,200),(660,320),(560,520)])
b+=glow(400,300,100,'#ffb02a',.7)+'<path d="M400 230 Q370 280 390 320 Q400 290 410 320 Q430 280 400 230Z" fill="#ffd02a"/><rect x="388" y="320" width="24" height="120" fill="#c8c8d0"/>'
b+='<path d="M120 600 Q260 500 380 440 L400 480 Q280 560 180 680Z" fill="#9a9aa0"/><path d="M680 600 Q540 500 420 440 L400 480 Q520 560 620 680Z" fill="#f0c8a8"/>'
I[1393]=svg(b,d)

# 1656 ナギサ: a quiet beach at blue hour with a pair of sandals left on the sand and gentle waves
d,b=bg([(0,'#3a5a9a'),(1,'#b0c8e8')])
b+='<rect y="380" width="800" height="200" fill="#4a7ab0"/><path d="M0 560 Q200 530 400 560 Q600 590 800 560 L800 800 L0 800Z" fill="#e8dcc8"/><path d="M0 560 Q200 530 400 560 Q600 590 800 560" stroke="#fff" stroke-width="10" fill="none" opacity=".8"/>'
b+='<ellipse cx="340" cy="680" rx="34" ry="70" fill="#e8402a" transform="rotate(-10 340 680)"/><ellipse cx="440" cy="690" rx="34" ry="70" fill="#e8402a" transform="rotate(14 440 690)"/>'+moon(600,160,30)
I[1656]=svg(b,d)

# 301 愛をとりもどせ!!: the Big Dipper with one star blazing over a post-apocalyptic wasteland, a clenched fist
d,b=bg([(0,'#1a0a0a'),(.6,'#6a2a1a'),(1,'#c8603a')])
P=[(180,140),(270,160),(350,200),(430,230),(470,320),(580,330),(600,230)]
b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in P)+' 470,230 430,230" stroke="#ffd8a0" stroke-width="3" fill="none" opacity=".6"/>'+''.join(sparkle(x,y,18,'#fff4d0') for x,y in P)+glow(470,320,40,'#ff3a2a',.9)
b+='<path d="M0 640 L120 600 L200 630 L320 580 L440 620 L600 570 L800 620 L800 800 L0 800Z" fill="#1a0a04"/>'
b+='<g fill="#2a1408"><rect x="320" y="440" width="160" height="120" rx="30"/><rect x="350" y="540" width="100" height="260"/></g>'+''.join(f'<path d="M{x} 470 L{x} 530" stroke="#120804" stroke-width="5"/>' for x in (360,400,440))
I[301]=svg(b,d)

# 406 すこしだけ やさしく: a soft scarf being wrapped around someone's shoulders in falling snow, gentle 80s
d,b=bg([(0,'#a8b8d8'),(1,'#e8eef8')])
b+=snow(80,406)+'<rect y="620" width="800" height="180" fill="#f4f8ff"/>'+figure(400,700,380,'#3a3a5a',hair='#3a3a5a')
b+='<path d="M320 400 Q400 430 480 400 L486 430 Q400 470 314 430Z" fill="#ff8aa8"/><rect x="430" y="420" width="34" height="140" fill="#ff8aa8" transform="rotate(-6 447 420)"/>'
I[406]=svg(b,d)

# 517 BEYOND THE TIME: a meteor-like asteroid streaking toward Earth, cut by a beam of light, space opera
d,b=bg([(0,'#000008'),(1,'#0a0a2a')])
b+=starsf(140,517,800)+'<circle cx="200" cy="760" r="300" fill="#1a4a8a"/><circle cx="200" cy="760" r="300" fill="none" stroke="#7ab0ff" stroke-width="10" opacity=".5"/>'
b+='<path d="M720 80 L520 300" stroke="#ffb02a" stroke-width="40" stroke-linecap="round" opacity=".35"/><circle cx="520" cy="300" r="60" fill="#5a4a3a"/><circle cx="500" cy="290" r="14" fill="#3a2a1a"/>'+glow(520,300,90,'#ff8a2a',.5)
b+='<path d="M200 600 L540 300" stroke="#cfe8ff" stroke-width="6"/>'+glow(380,460,40,'#cfe8ff',.6)
I[517]=svg(b,d)

# 561 楽園のDoor: a door standing alone in a field opening onto a paradise of light, a schoolgirl yo-yo silhouette
d,b=bg([(0,'#3a2a5a'),(1,'#7a5a8a')])
b+=starsf(50,561,500)+'<rect y="560" width="800" height="240" fill="#2a1a3a"/>'
b+='<rect x="320" y="200" width="200" height="380" fill="#fff4c8"/>'+glow(420,390,200,'#fff4c8',.5)+'<path d="M320 200 L250 230 L250 590 L320 580Z" fill="#6a3a2a"/>'
b+=figure(560,600,220,'#000',hair='#000')+'<path d="M600 430 L640 520" stroke="#000" stroke-width="3"/><circle cx="642" cy="526" r="12" fill="#c8c8d0"/>'
I[561]=svg(b,d)

# 705 MIND GAMES: a baseball diamond seen from above as a chessboard-like strategy grid, night stadium lights
d,b=bg([(0,'#0a1a10'),(1,'#1a3a20')])
b+=''.join(glow(x,60,60,'#fff',.4) for x in (100,700))
b+='<polygon points="400,180 640,420 400,660 160,420" fill="#c8905a"/><polygon points="400,260 560,420 400,580 240,420" fill="#3a8a3a"/>'+''.join(f'<rect x="{x-14}" y="{y-14}" width="28" height="28" fill="#fff" transform="rotate(45 {x} {y})"/>' for x,y in [(400,180),(640,420),(400,660),(160,420)])
b+='<circle cx="400" cy="420" r="30" fill="#c8905a"/><circle cx="400" cy="420" r="12" fill="#fff"/>'+''.join(f'<path d="M{a} {b2} Q400 340 {c} {d2}" stroke="#ffd02a" stroke-width="4" stroke-dasharray="10 8" fill="none"/>' for a,b2,c,d2 in [(400,660,640,420),(160,420,400,180)])
I[705]=svg(b,d)

# 1642 Present: a small gift with a ribbon on a snowy windowsill, a warm window light behind, winter love
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=snow(70,1642)+'<rect x="140" y="120" width="520" height="440" fill="#ffd890"/>'+glow(400,340,200,'#ffd890',.4)+'<path d="M400 120 L400 560 M140 340 L660 340" stroke="#3a2a2a" stroke-width="14"/><rect x="140" y="120" width="520" height="440" fill="none" stroke="#3a2a2a" stroke-width="20"/>'
b+='<rect x="100" y="560" width="600" height="40" fill="#f4f8ff"/><rect x="330" y="470" width="140" height="100" fill="#c8102a"/><rect x="390" y="470" width="20" height="100" fill="#ffd02a"/><path d="M400 470 Q360 430 370 420 Q400 430 400 470 Q400 430 430 420 Q440 430 400 470Z" fill="#ffd02a"/>'
I[1642]=svg(b,d)

# 1712 別れの朝: a train pulling away from a morning platform, a woman's hand waving goodbye, early-70s sepia
d,b=bg([(0,'#d8c0a0'),(1,'#f4e4c8')])
b+='<rect y="520" width="800" height="280" fill="#8a7a6a"/><rect y="520" width="800" height="16" fill="#e8d8b8"/>'
b+='<path d="M380 280 L800 260 L800 520 L380 520Z" fill="#3a5a4a"/>'+''.join(f'<rect x="{x}" y="320" width="70" height="80" fill="#e8d8b8"/>' for x in (420,520,620,720))
b+=figure(240,560,280,'#2a1a10',pose='wave',hair='#2a1a10')+''.join(f'<path d="M{380+k*20} {300+k*40} L{300+k*10} {300+k*40}" stroke="#fff" stroke-width="3" opacity=".5"/>' for k in range(4))
I[1712]=svg(b,d)

# 326 元気を出して: a friend handing a cup of tea and a tissue box, a sunny-yellow cheer-up scene
d,b=bg([(0,'#fff0b0'),(1,'#ffd8a0')])
b+=rays(400,120,18,'#fff',.35,8)+'<rect y="600" width="800" height="200" fill="#d8a878"/>'
b+=figure(260,640,300,'#4a3a3a',hair='#4a3a3a')+figure(540,640,300,'#3a3a5a',pose='reachL',hair='#3a3a5a')
b+='<path d="M360 450 L420 450 L414 510 L366 510Z" fill="#fff"/><path d="M420 465 Q440 465 438 485 Q436 500 418 500" stroke="#fff" stroke-width="6" fill="none"/><path d="M380 440 Q376 410 390 400" stroke="#fff" stroke-width="4" fill="none" opacity=".7"/>'
I[326]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
