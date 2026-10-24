import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 37. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 340 Silhouette Romance: two silhouettes about to kiss behind a translucent curtain lit by a lamp, city pop
d,b=bg([(0,'#ff9a6a'),(1,'#ffd8b0')])
b+='<rect x="120" y="100" width="560" height="560" fill="#ffe8c8"/>'+glow(400,380,260,'#fff4c8',.6)+profile(280,620,1.3,'#5a2a2a')+profile(520,620,1.3,'#5a2a2a',True)
b+=''.join(f'<path d="M{x} 100 Q{x+20} 380 {x} 660" stroke="#ffc8a0" stroke-width="4" fill="none" opacity=".6"/>' for x in range(140,680,50))+'<rect y="660" width="800" height="140" fill="#a85a4a"/>'
I[340]=svg(b,d)

# 467 冬のオペラグラス: opera glasses on a velvet seat with snowflakes falling past a theatre window, 80s idol
d,b=bg([(0,'#2a1a3a'),(1,'#5a2a4a')])
b+='<rect x="200" y="80" width="400" height="300" rx="200" fill="#3a5a8a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#fff"/>' for x,y in [(260,150),(340,200),(420,130),(500,220),(540,160),(300,300),(460,320)])
b+='<rect y="440" width="800" height="360" fill="#8a1a2a"/>'
b+='<circle cx="320" cy="560" r="70" fill="#1a1a1a" stroke="#c8a24a" stroke-width="14"/><circle cx="480" cy="560" r="70" fill="#1a1a1a" stroke="#c8a24a" stroke-width="14"/><rect x="380" y="540" width="40" height="30" fill="#c8a24a"/><path d="M560 590 Q640 660 600 760" stroke="#c8a24a" stroke-width="10" fill="none"/>'
b+='<circle cx="320" cy="560" r="50" fill="#3a5a8a" opacity=".6"/><circle cx="480" cy="560" r="50" fill="#3a5a8a" opacity=".6"/>'
I[467]=svg(b,d)

# 502 Forget-me-not: a small bunch of blue forget-me-not flowers on a weathered windowsill, 80s ballad
d,b=bg([(0,'#c8d8e8'),(1,'#f0f0e8')])
b+='<rect x="100" y="80" width="600" height="440" fill="#e0ecf4"/><rect x="100" y="80" width="600" height="440" fill="none" stroke="#8a7a6a" stroke-width="18"/><rect x="60" y="520" width="680" height="40" fill="#8a7a6a"/><rect y="560" width="800" height="240" fill="#5a4a40"/>'
b+='<path d="M360 520 L340 460 L460 460 L440 520Z" fill="#c8b8a8"/>'+''.join(f'<path d="M400 460 L{x} {y}" stroke="#4a8a3a" stroke-width="5"/>' for x,y in [(320,320),(400,280),(480,330),(360,380),(450,390)])
b+=''.join(flower(x,y,22,5,'#5a9ae8','#ffe04a') for x,y in [(320,320),(400,280),(480,330),(360,380),(450,390),(300,370),(500,280)])
I[502]=svg(b,d)

# 789 RED×BLUE: a red and a blue light beam crossing into violet on a dark stage, 2004 rock
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+='<path d="M0 0 L120 0 L520 800 L340 800Z" fill="#ff2a3a" opacity=".55"/><path d="M800 0 L680 0 L280 800 L460 800Z" fill="#2a6aff" opacity=".55"/>'+glow(400,600,140,'#a04aff',.6)
b+='<rect y="700" width="800" height="100" fill="#0a0a10"/>'+guitar(400,560,.8,-20,'#000')
I[789]=svg(b,d)

# 884 クラシック: a gramophone with a big brass horn blossoming into pink flowers, 90s pop-punk
d,b=bg([(0,'#ffe0ec'),(1,'#f4e8d8')])
b+='<rect x="240" y="560" width="300" height="160" fill="#8a4a2a"/><ellipse cx="390" cy="560" rx="140" ry="20" fill="#3a2a2a"/><path d="M390 540 L420 420" stroke="#c8a24a" stroke-width="16"/>'
b+='<path d="M420 420 L520 180 Q680 140 700 280Z" fill="#e8b830"/><ellipse cx="610" cy="230" rx="90" ry="60" fill="#c8982a" transform="rotate(30 610 230)"/>'+''.join(flower(x,y,26,5,'#ff7aa8','#fff') for x,y in [(600,180),(660,250),(560,250),(700,170)])
b+=note(200,260,50,'#e8508a')+note(150,420,36,'#e8508a',True)
I[884]=svg(b,d)

# 915 ありがとうのうた: a bouquet handed over with a small thank-you card, warm golden light
d,b=bg([(0,'#ffd88a'),(1,'#fff4e0')])
b+=rays(400,200,16,'#fff',.25,10)+'<path d="M300 420 L500 420 L420 700 L380 700Z" fill="#f4e0c8"/>'+''.join(flower(x,y,40,6,c,'#ffd02a') for x,y,c in [(330,360,'#ff7aa8'),(400,320,'#fff'),(470,360,'#ff9a4a'),(370,420,'#ffc0d8'),(440,410,'#e8508a')])
b+='<rect x="490" y="500" width="130" height="90" rx="8" fill="#fff" transform="rotate(10 555 545)"/>'+heart(555,545,24,'#ff5a7a')
I[915]=svg(b,d)

# 1289 明日がくるなら: two silhouettes holding hands toward a sunrise on a long road, soulful duet
d,b=bg([(0,'#4a5a9a'),(1,'#ffc08a')])
b+='<circle cx="400" cy="460" r="90" fill="#fff0c0"/>'+rays(400,460,18,'#fff',.15,10)+'<rect y="480" width="800" height="320" fill="#3a3448"/><path d="M380 480 L200 800 L600 800 L420 480Z" fill="#5a5068"/>'
b+=figure(360,740,230,'#0a0a14')+figure(440,740,220,'#0a0a14',hair='#0a0a14')
I[1289]=svg(b,d)

# 1753 君は僕だ: a figure facing her own reflection in a rippling water mirror, soft blue dusk
d,b=bg([(0,'#3a4a8a'),(1,'#c8a8d8')])
b+='<rect y="460" width="800" height="340" fill="#4a5a9a"/>'+figure(400,460,240,'#1a1a2a',hair='#1a1a2a')+'<g transform="translate(0 920) scale(1 -1)" opacity=".5">'+figure(400,460,240,'#8ab0e8',hair='#8ab0e8')+'</g>'
b+=''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(200,520),(500,560),(330,620),(560,680)])
I[1753]=svg(b,d)

# 90 冬の駅: a small country station in deep snow, a woman with a suitcase under a single lamp, 1974
d,b=bg([(0,'#2a3450'),(1,'#5a6a8a')])
b+=snow(80,90)+'<rect x="420" y="360" width="300" height="200" fill="#5a3a2a"/><path d="M400 370 L570 280 L740 370Z" fill="#f0f4ff"/><rect x="540" y="440" width="70" height="120" fill="#ffd27a"/>'
b+='<rect x="200" y="300" width="10" height="260" fill="#3a3a44"/><circle cx="205" cy="300" r="16" fill="#fff4c8"/>'+glow(205,300,90,'#fff4c8',.5)+'<rect y="560" width="800" height="240" fill="#e8eef8"/>'
b+=figure(300,600,200,'#1a1a2a',hair='#1a1a2a')+'<rect x="320" y="540" width="50" height="40" rx="5" fill="#6a3a2a"/>'
I[90]=svg(b,d)

# 165 舟唄: a lone fishing boat on a dark winter sea with a lantern, a sake bottle on the bow, enka
d,b=bg([(0,'#0a1424'),(1,'#2a3a5a')])
b+=moon(620,160,50)+'<rect y="480" width="800" height="320" fill="#0a1a30"/>'+''.join(f'<path d="M{x} {y} q40 -14 80 0" stroke="#5a7aa8" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(100,540),(500,600),(250,680),(600,720)])
b+='<path d="M200 480 L600 480 L540 560 L250 560Z" fill="#3a2a1a"/><rect x="380" y="300" width="10" height="180" fill="#3a2a1a"/>'+chochin(440,420,36)+'<path d="M300 460 L300 420 Q300 400 312 400 Q324 400 324 420 L324 460Z" fill="#f4f0e8"/>'
I[165]=svg(b,d)

# 464 かしこ: a pastel letter sealed with a ribbon and a fountain pen, a schoolgirl idol unit
d,b=bg([(0,'#d8f0ff'),(1,'#ffe0f0')])
b+='<rect x="200" y="240" width="400" height="360" fill="#fff" transform="rotate(-6 400 420)"/>'+''.join(f'<path d="M250 {y} L550 {y-30}" stroke="#c8d8ec" stroke-width="3"/>' for y in range(320,580,40))
b+='<path d="M560 200 L620 220 L420 560 L400 570 L405 548Z" fill="#3a3a5a"/>'+'<path d="M290 560 Q320 520 350 560 Q320 600 290 560Z M350 560 Q380 520 410 560 Q380 600 350 560Z" fill="#ff7aa8"/>'
I[464]=svg(b,d)

# 625 LOVE SONG: a grand piano lid open under a single spotlight with notes rising, 1989 ballad
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+='<path d="M340 0 L460 0 L640 680 L160 680Z" fill="#fff4c8" opacity=".15"/>'
b+='<path d="M180 560 Q180 440 300 440 L520 440 Q640 460 640 560Z" fill="#111"/><path d="M200 440 L560 260" stroke="#111" stroke-width="16"/><rect x="180" y="560" width="460" height="40" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="560" width="10" height="24" fill="#fff"/>' for x in range(200,620,14))
b+=''.join(note(x,y,s,'#fff4c8') for x,y,s in [(420,220,40),(520,150,32),(330,180,28)])
I[625]=svg(b,d)

# 1128 僕が死のうと思ったのは: a figure on a pier at dawn watching seagulls fly toward a brightening horizon, hopeful
d,b=bg([(0,'#3a4a7a'),(1,'#ffc8a0')])
b+='<circle cx="400" cy="480" r="80" fill="#fff4d0"/><rect y="480" width="800" height="320" fill="#5a6a9a"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(150,560),(500,600),(300,700)])
b+='<rect x="0" y="600" width="420" height="20" fill="#3a2a2a"/>'+''.join(f'<rect x="{x}" y="620" width="12" height="180" fill="#3a2a2a"/>' for x in (60,200,340))+figure(340,600,170,'#1a1424')
b+=bird(500,280,30,'#1a1424')+bird(560,240,24,'#1a1424')+bird(620,300,20,'#1a1424')
I[1128]=svg(b,d)

# 1286 Happiness: a big yellow smiling sun peeking out after the rain with a rainbow, soul pop
d,b=bg([(0,'#5ab8ff'),(1,'#e0f4ff')])
b+=''.join(f'<path d="M80 640 A320 320 0 0 1 720 640" stroke="{c}" stroke-width="30" fill="none"/>'.replace('320 320',f'{320-k*30} {320-k*30}').replace('M80',f'M{80+k*30}').replace('720',f'{720-k*30}') for k,c in enumerate(['#ff4a4a','#ff9a2a','#ffe02a','#5ad85a','#3a9aff','#8a5aff']))
b+=cloud(160,620,1.4)+cloud(640,640,1.3)+'<circle cx="400" cy="420" r="90" fill="#ffd82a"/><path d="M360 430 Q400 480 440 430" stroke="#c8702a" stroke-width="8" fill="none"/><circle cx="370" cy="400" r="8" fill="#c8702a"/><circle cx="430" cy="400" r="8" fill="#c8702a"/>'
I[1286]=svg(b,d)

# 1335 ジャーバージャ: a mysterious tropical jungle with a giant glowing flower at night, idol pop
d,b=bg([(0,'#0a1a14'),(1,'#1a3a2a')])
b+=''.join(f'<path d="M{x} 800 Q{x+r} 500 {x+2*r} {y}" stroke="#2a6a3a" stroke-width="30" fill="none"/>' for x,r,y in [(0,60,300),(700,-60,280),(100,80,420),(640,-70,400)])
b+=glow(400,420,200,'#ff4fd0',.5)+flower(400,420,120,6,'#ff4fd0','#ffd02a')+sparkle(220,200,20,'#fff')+sparkle(600,180,24,'#fff')
I[1335]=svg(b,d)

# 1782 RETURNER: a lone sword-bearing silhouette emerging from darkness into a crimson dawn, gothic rock
d,b=bg([(0,'#0a0a0a'),(1,'#5a0a14')])
b+='<rect y="460" width="800" height="340" fill="#0a0a0a"/>'+glow(400,460,300,'#ff3a2a',.5)+'<path d="M0 460 L800 460" stroke="#ff3a2a" stroke-width="3"/>'
b+=figure(400,720,380,'#000',hair='#000')+'<path d="M300 400 Q260 600 220 720 L400 720Z" fill="#000"/><rect x="470" y="380" width="10" height="320" fill="#c8c8d0" transform="rotate(10 475 540)"/>'
I[1782]=svg(b,d)

# 1838 Synchrogazer: two glowing rings of light locking into resonance in a cosmic sky, anime song
d,b=bg([(0,'#0a0a2a'),(1,'#2a0a4a')])
b+=starsf(80,1838,800)+ring(330,400,150,'#ff4a8a',14)+ring(470,400,150,'#4ad0ff',14)+glow(400,400,90,'#fff',.6)+'<path d="M400 270 L400 530" stroke="#fff" stroke-width="6" opacity=".8"/>'
I[1838]=svg(b,d)

# 132 個人授業: a chalkboard with an apple on a teacher's desk, a young pupil's desk with a heart doodle, 1973
d,b=bg([(0,'#f0e0c0'),(1,'#d8c0a0')])
b+='<rect x="100" y="100" width="600" height="320" fill="#2a4a3a" stroke="#8a6a4a" stroke-width="16"/><path d="M180 200 Q240 160 300 200 M180 260 L420 260 M180 320 L360 320" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/>'+heart(560,260,40,'none',' stroke="#ffc0d8" stroke-width="5"')
b+='<rect x="120" y="540" width="560" height="30" fill="#8a5a3a"/><rect x="140" y="570" width="20" height="230" fill="#6a4a2a"/><rect x="640" y="570" width="20" height="230" fill="#6a4a2a"/>'
b+='<circle cx="400" cy="500" r="44" fill="#e8102a"/><path d="M400 460 L404 430" stroke="#3a2a1a" stroke-width="6"/><path d="M404 440 q20 -20 40 -6 q-20 16 -40 6Z" fill="#3a8a3a"/>'
I[132]=svg(b,d)

# 465 象さんのすきゃんてぃ: a playful pink elephant spraying a fountain of hearts, comedic 80s idol unit
d,b=bg([(0,'#fff0a0'),(1,'#ffd0e0')])
b+='<ellipse cx="380" cy="520" rx="180" ry="130" fill="#ff9ac0"/><circle cx="520" cy="420" r="100" fill="#ff9ac0"/><ellipse cx="480" cy="420" rx="60" ry="80" fill="#ff7aa8"/><circle cx="550" cy="400" r="12" fill="#3a2a2a"/>'
b+='<path d="M600 450 Q680 460 680 360 Q680 300 640 280" stroke="#ff9ac0" stroke-width="40" fill="none" stroke-linecap="round"/>'+''.join(f'<rect x="{x}" y="620" width="50" height="90" rx="20" fill="#ff9ac0"/>' for x in (260,340,420,480))
b+=''.join(heart(x,y,s,'#e8508a') for x,y,s in [(620,200,24),(680,150,18),(580,140,16),(720,220,14)])
I[465]=svg(b,d)

# 879 バラ色の日々: a rose-tinted sky over a long highway with a guitar case leaning on a mile marker, 1999
d,b=bg([(0,'#ff7aa0'),(1,'#ffd8c8')])
b+='<rect y="500" width="800" height="300" fill="#6a4a5a"/><path d="M380 500 L120 800 L680 800 L420 500Z" fill="#3a3040"/><path d="M400 520 L400 800" stroke="#ffd02a" stroke-width="6" stroke-dasharray="30 30"/>'
b+=''.join(rose(x,y,.5,r) for x,y,r in [(120,200,0),(660,160,30),(250,100,60)])+'<rect x="600" y="560" width="30" height="120" fill="#fff"/><rect x="630" y="580" width="40" height="130" rx="14" fill="#1a1a1a" transform="rotate(-10 650 640)"/>'
I[879]=svg(b,d)

# 1073 歩行者優先: two friends with guitars strolling across a zebra crossing in morning sun, folk duo
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+='<rect y="480" width="800" height="320" fill="#4a4a54"/>'+''.join(f'<rect x="{x}" y="560" width="50" height="200" fill="#f4f4f4"/>' for x in range(80,760,90))
b+=figure(320,700,260,'#1a1a2a')+figure(480,700,250,'#1a1a2a')+guitar(300,580,.45,30,'#1a1a2a')+guitar(500,580,.45,-30,'#1a1a2a')
I[1073]=svg(b,d)

# 1652 Tokyo Calling: schoolgirls' silhouettes dancing in sync in front of Tokyo Tower at night
d,b=bg([(0,'#0a0a2a'),(1,'#3a1a4a')])
b+=skyline(640,'#140a24',1652,60,220,'#ffd27a',60)+tokyo_tower(600,640,420)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'
b+=''.join(figure(x,740,220,'#000',pose=p,hair='#000') for x,p in [(160,'up'),(280,'stand'),(400,'up')])
I[1652]=svg(b,d)

# 1812 この世の花: a single camellia flower blooming against a muted 1950s sepia sky
d,b=bg([(0,'#d8c8a8'),(1,'#a8987a')])
b+='<path d="M400 800 Q380 600 420 480" stroke="#3a3a2a" stroke-width="12" fill="none"/><path d="M410 560 q-100 -40 -130 30 q80 20 130 -30Z M420 520 q100 -60 140 0 q-80 40 -140 0Z" fill="#3a5a3a"/>'
b+=flower(420,380,120,5,'#c8203a','#ffd02a',0,.65)+glow(420,380,140,'#ff8a8a',.2)
I[1812]=svg(b,d)

# 542 ふたりの夏物語: a convertible on a coastal road at sunset with a palm tree, 80s summer city pop
d,b=bg([(0,'#ff6a8a'),(1,'#ffd08a')])
b+='<circle cx="400" cy="440" r="110" fill="#fff0b0"/>'+''.join(f'<rect x="290" y="{y}" width="220" height="6" fill="#ff8a8a"/>' for y in (430,460,490,520))+'<rect y="520" width="800" height="120" fill="#3a6ab8"/><rect y="640" width="800" height="160" fill="#2a2a3a"/>'
b+='<path d="M640 640 L660 260" stroke="#1a1424" stroke-width="16"/>'+''.join(f'<path d="M660 260 Q{660+dx} {260+dy-40} {660+dx*1.4} {260+dy}" stroke="#1a1424" stroke-width="14" fill="none"/>' for dx,dy in [(-100,40),(100,40),(-60,80),(80,90)])
b+='<path d="M140 680 L180 630 L380 630 L420 680Z" fill="#1a1424"/><circle cx="200" cy="690" r="22" fill="#1a1424"/><circle cx="370" cy="690" r="22" fill="#1a1424"/>'+figure(240,640,80,'#1a1424')+figure(310,640,76,'#1a1424',hair='#1a1424')
I[542]=svg(b,d)

# 581 Sexy Music: two doll-like silhouettes back to back on a glittering disco floor, Eurobeat duo
d,b=bg([(0,'#2a0a3a'),(1,'#ff4a9a')])
b+=''.join(f'<rect x="{x}" y="{y}" width="100" height="40" fill="{c}" opacity=".6"/>' for i,x in enumerate(range(0,800,100)) for j,y in enumerate(range(640,800,40)) for c in [['#ff8ad0','#8ad0ff','#ffd02a'][(i+j)%3]])
b+=figure(350,660,380,'#0a0a14',hair='#0a0a14')+figure(450,660,380,'#0a0a14',hair='#0a0a14')+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(150,180,24),(650,140,30),(600,400,18),(200,420,16)])
I[581]=svg(b,d)

# 1281 千の風になって: a gentle wind sweeping across golden fields and up into a vast sky with light, classical ballad
d,b=bg([(0,'#5a9ae8'),(1,'#f4f0e0')])
b+=rays(400,160,16,'#fff',.3,10)+'<path d="M0 560 Q200 520 400 560 T800 540 L800 800 L0 800Z" fill="#d8b85a"/>'
b+=''.join(f'<path d="M{-20+k*20} {600-k*80} Q200 {520-k*80} 400 {560-k*90} T840 {480-k*100}" stroke="#fff" stroke-width="{6-k}" fill="none" opacity="{.8-k*.12}"/>' for k in range(5))
b+=''.join(f'<path d="M{x} 800 L{x+10} {640+(x%5)*10}" stroke="#b8983a" stroke-width="4"/>' for x in range(20,800,30))
I[1281]=svg(b,d)

# 1634 3XL: three oversized hoodies hanging side by side in bold streetwear colours, 2026 boy group
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<path d="M60 140 L740 140" stroke="#888" stroke-width="6"/>'
for x,c in [(170,'#e8302a'),(400,'#f4f4f4'),(630,'#2a6aff')]:
  b+=f'<path d="M{x} 140 L{x} 170" stroke="#888" stroke-width="5"/><path d="M{x-110} 220 Q{x} 160 {x+110} 220 L{x+150} 420 L{x+110} 430 L{x+100} 600 L{x-100} 600 L{x-110} 430 L{x-150} 420Z" fill="{c}"/><path d="M{x-50} 200 Q{x} 280 {x+50} 200" stroke="#000" stroke-width="5" fill="none" opacity=".4"/><rect x="{x-60}" y="460" width="120" height="70" rx="10" fill="#000" opacity=".15"/>'
I[1634]=svg(b,d)

# 1719 Another Days: a wall calendar's torn pages blowing toward an open window with sunrise, 2002 pop
d,b=bg([(0,'#ffd8a8'),(1,'#f8f0e0')])
b+='<rect x="440" y="100" width="300" height="420" fill="#ffe8a0"/>'+'<circle cx="590" cy="380" r="70" fill="#fff8d8"/>'+'<rect x="440" y="100" width="300" height="420" fill="none" stroke="#8a6a4a" stroke-width="14"/><rect x="583" y="100" width="14" height="420" fill="#8a6a4a"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="70" height="80" fill="#fff" stroke="#ddd" stroke-width="2" transform="rotate({r} {x} {y})"/>' for x,y,r in [(120,300,-20),(240,220,15),(340,160,-10),(200,420,30)])
b+=figure(200,760,220,'#2a2a34')+'<rect y="740" width="800" height="60" fill="#a8806a"/>'
I[1719]=svg(b,d)

# 1749 暗闇: a single lantern glowing on a dark seaside path with stars over Setouchi islands, idol ballad
d,b=bg([(0,'#050a1a'),(1,'#141e3a')])
b+=starsf(90,1749,500)+'<path d="M0 520 Q100 460 200 520Z M500 520 Q620 440 760 520Z" fill="#0a1020"/><rect y="520" width="800" height="280" fill="#0a1430"/>'
b+=''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#5a7ab8" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(100,580),(500,620),(250,700)])
b+='<rect x="396" y="560" width="8" height="160" fill="#2a2a34"/><rect x="380" y="520" width="40" height="50" rx="6" fill="#ffd27a"/>'+glow(400,545,120,'#ffd27a',.6)+figure(480,740,170,'#000',hair='#000')
I[1749]=svg(b,d)

# 215 言葉にできない: a flock of birds rising over a soft pastel horizon, wordless wonder, 1981
d,b=bg([(0,'#a8c8f0'),(1,'#fff0e0')])
b+='<circle cx="400" cy="560" r="120" fill="#fff8e0"/>'+rays(400,560,20,'#fff',.25,10)+'<path d="M0 600 Q400 560 800 600 L800 800 L0 800Z" fill="#b8c8d8"/>'
b+=''.join(bird(x,y,s,'#3a4a6a') for x,y,s in [(300,280,40),(380,220,34),(460,260,30),(520,200,26),(240,200,24),(600,300,22),(420,330,30)])
I[215]=svg(b,d)

# 330 September: autumn leaves falling past a sleeveless summer dress on a hanger, late-70s pop
d,b=bg([(0,'#f4c88a'),(1,'#f8e8d0')])
b+='<path d="M300 140 Q400 100 500 140" stroke="#6a5a4a" stroke-width="6" fill="none"/><path d="M400 100 L400 80 Q400 60 420 64" stroke="#6a5a4a" stroke-width="5" fill="none"/>'
b+='<path d="M330 150 L470 150 L460 260 L560 640 L240 640 L340 260Z" fill="#fff"/><path d="M340 260 L460 260" stroke="#e8c870" stroke-width="10"/>'
b+=''.join(f'<path d="M{x} {y} q20 -30 40 0 q-20 30 -40 0Z" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,c,r in [(150,200,'#e8602a',20),(620,260,'#c8402a',-40),(180,520,'#e89a2a',60),(640,560,'#e8602a',10),(120,380,'#c8402a',-20)])
I[330]=svg(b,d)

# 447 You Gotta Chance: a dancer's silhouette mid-leap over a summer beach with a giant sun, mid-80s
d,b=bg([(0,'#ff4a4a'),(1,'#ffb84a')])
b+='<circle cx="400" cy="380" r="200" fill="#ffe04a"/><rect y="560" width="800" height="80" fill="#2a8ad8"/><rect y="640" width="800" height="160" fill="#f0d090"/>'
b+='<g transform="rotate(15 400 400)">'+figure(400,560,300,'#1a0a0a',pose='up')+'</g>'
I[447]=svg(b,d)

# 916 way of life: a winding mountain path with footprints leading to a summit under clear sky
d,b=bg([(0,'#7ab8e8'),(1,'#e8f4ff')])
b+=hills(420,60,'#7a9ab8',916,4)+hills(520,50,'#5a8a6a',9161,5)+'<path d="M380 800 Q520 700 400 620 Q280 540 420 480 Q500 440 460 400" stroke="#e8d8b0" stroke-width="40" fill="none" stroke-linecap="round"/>'
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="10" fill="#8a7a5a"/>' for x,y in [(400,760),(430,720),(450,680),(430,640),(380,600),(350,560),(370,520),(420,490)])+figure(460,410,90,'#1a1a2a')
I[916]=svg(b,d)

# 600 さよなら人類: a strange tall sunflower towering over a little planet with tiny monkeys' silhouettes waving goodbye
d,b=bg([(0,'#0a1a3a'),(1,'#3a3a6a')])
b+=starsf(70,600,800)+'<circle cx="400" cy="820" r="320" fill="#5a8a4a"/>'
b+='<path d="M400 520 Q380 380 420 260" stroke="#3a7a2a" stroke-width="16" fill="none"/>'+flower(420,220,90,14,'#ffd02a','#6a4a1a',0,.5)
b+=''.join(figure(x,y,70,'#1a2a1a',pose='up') for x,y in [(260,560),(540,560),(320,520),(480,520)])
I[600]=svg(b,d)

# 1729 ミニモニ。ジャンケンぴょん!: rock-paper-scissors hands in candy colours with a hopping bunny, kids' pop
d,b=bg([(0,'#fff0a0'),(1,'#ffd0f0')])
b+=confetti(30,1729,['#ff6aa0','#3ab0ff','#5ad87a'])
b+='<circle cx="200" cy="420" r="80" fill="#ff7aa8"/><rect x="330" y="320" width="140" height="200" rx="30" fill="#3ab0ff"/><path d="M580 520 L560 340 L600 340 L620 450 L650 330 L690 340 L660 520Z" fill="#5ad87a"/><circle cx="620" cy="520" r="60" fill="#5ad87a"/>'
b+='<ellipse cx="400" cy="660" rx="50" ry="40" fill="#fff"/><ellipse cx="380" cy="600" rx="12" ry="40" fill="#fff"/><ellipse cx="420" cy="600" rx="12" ry="40" fill="#fff"/><circle cx="390" cy="650" r="5" fill="#3a2a2a"/><circle cx="410" cy="650" r="5" fill="#3a2a2a"/>'
I[1729]=svg(b,d)

# 1755 弱虫サンタ: a shy Santa's sack and red hat left in the snow beside a small doorstep, comic Christmas
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a7a')])
b+=snow(70,1755)+'<rect y="600" width="800" height="200" fill="#e8eef8"/><rect x="460" y="300" width="260" height="300" fill="#6a3a2a"/><rect x="540" y="420" width="90" height="180" fill="#ffd27a"/>'
b+='<path d="M180 600 Q160 460 260 440 Q360 460 340 600Z" fill="#c8a06a"/><path d="M220 450 Q260 420 300 450" stroke="#8a6a3a" stroke-width="10" fill="none"/>'
b+='<path d="M340 600 L400 480 L450 600Z" fill="#e8102a"/><circle cx="400" cy="480" r="16" fill="#fff"/><rect x="330" y="590" width="130" height="24" rx="12" fill="#fff"/>'
I[1755]=svg(b,d)

# 20 恋のバカンス: a striped beach parasol, two cocktail glasses and a 60s-style sun hat on a sunny shore
d,b=bg([(0,'#3ab8ff'),(1,'#d8f4ff')])
b+='<circle cx="640" cy="140" r="60" fill="#fff4a0"/><rect y="420" width="800" height="140" fill="#1a8ad8"/><path d="M0 560 Q400 520 800 560 L800 800 L0 800Z" fill="#f4dca0"/>'
b+='<path d="M260 760 L320 380" stroke="#6a4a2a" stroke-width="8"/><path d="M140 420 Q320 260 500 420Z" fill="#ff5a7a"/><path d="M200 420 Q320 300 320 300 L260 420Z M380 420 L320 300 Q350 330 440 420Z" fill="#fff"/>'
b+='<path d="M480 620 L540 620 L510 660Z M600 620 L660 620 L630 660Z" fill="#ff9ac0" opacity=".8"/><path d="M510 660 L510 700 M630 660 L630 700" stroke="#fff" stroke-width="5"/><ellipse cx="420" cy="700" rx="70" ry="16" fill="#f4e0b0"/><path d="M380 700 Q420 650 460 700Z" fill="#f4e0b0"/><rect x="380" y="690" width="80" height="10" fill="#ff5a7a"/>'
I[20]=svg(b,d)

# 91 2億4千万の瞳: a sea of glowing eyes-like lights across a neon night city, exotic 80s pop
d,b=bg([(0,'#1a0a2a'),(1,'#5a0a3a')])
b+=skyline(640,'#0a0a14',91,80,300)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="8" fill="#ffd27a" opacity=".8"/><circle cx="{x}" cy="{y}" r="4" fill="#3a1a2a"/>' for x,y in [(random.Random(91*k).randint(40,760),random.Random(91*k+1).randint(380,780)) for k in range(60)])
b+=rays(400,0,12,'#ff4fa0',.12,20,30,150)
I[91]=svg(b,d)

# 331 Manhattan Kiss: two silhouettes kissing on a fire escape above a glittering skyline, early-90s
d,b=bg([(0,'#0a1a3a'),(1,'#5a3a6a')])
b+=starsf(40,331,300)+skyline(800,'#14142a',331,120,380,'#ffd27a',140)
b+='<rect x="440" y="520" width="360" height="12" fill="#2a2a2a"/>'+''.join(f'<rect x="{x}" y="440" width="6" height="80" fill="#2a2a2a"/>' for x in range(450,800,40))+'<rect x="440" y="440" width="360" height="8" fill="#2a2a2a"/>'
b+=profile(540,520,.6,'#000')+profile(680,520,.6,'#000',True)+heart(610,330,26,'#ff6aa0')
I[331]=svg(b,d)

# 518 THE POINT OF LOVERS' NIGHT: a laser grid converging to one bright point over a futuristic city, synth rock
d,b=bg([(0,'#050514'),(1,'#1a0a3a')])
b+='<rect y="360" width="800" height="440" fill="#0a0520"/>'+''.join(f'<path d="M400 360 L{x} 800" stroke="#ff4fd0" stroke-width="2" opacity=".6"/>' for x in range(-400,1200,80))+''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff4fd0" stroke-width="2" opacity=".5"/>' for y in (420,480,560,660,780))
b+='<circle cx="400" cy="360" r="20" fill="#fff"/>'+glow(400,360,120,'#4fd0ff',.7)+heart(400,200,50,'none',' stroke="#ff4fd0" stroke-width="6"')
I[518]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
