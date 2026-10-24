import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 41. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 721 突然 (FIELD OF VIEW): a sudden summer cloudburst over a seaside road with a boy and a bicycle
d,b=bg([(0,'#3a8ae8'),(1,'#d8f0ff')])
b+=cloud(300,160,1.6,'#c8d0e0')+rain(30,721,'#fff',.5,0,520)+'<rect y="480" width="800" height="120" fill="#2a7ac8"/><rect y="600" width="800" height="200" fill="#d8c8a8"/>'
b+=ring(480,680,44,'#1a1a2a',6)+ring(600,680,44,'#1a1a2a',6)+'<path d="M480 680 L540 620 L600 680 M540 620 L560 600" stroke="#1a1a2a" stroke-width="6" fill="none"/>'+figure(380,700,220,'#1a1a2a',pose='up')
I[721]=svg(b,d)

# 1708 You're My Only Shinin' Star: a single bright star reflected in a still lake at night with a figure on a pier
d,b=bg([(0,'#050a24'),(1,'#1a2a5a')])
b+=starsf(60,1708,440)+star5(400,180,44,'#fff4c8')+glow(400,180,100,'#fff4c8',.6)+'<rect y="440" width="800" height="360" fill="#0a1430"/>'
b+=star5(400,700,30,'#fff4c8')+glow(400,700,60,'#fff4c8',.3)+'<rect x="0" y="500" width="300" height="16" fill="#2a2a3a"/>'+figure(240,500,160,'#000',hair='#000')
I[1708]=svg(b,d)

# 1810 My First Kiss: two skateboards side by side on a sunny curb with a small heart scribble, punk rock
d,b=bg([(0,'#ffd04a'),(1,'#ff9a6a')])
b+='<rect y="520" width="800" height="280" fill="#7a7a84"/><rect y="500" width="800" height="30" fill="#b8b8c0"/>'
for x,y,c in [(200,600,'#3ab0ff'),(420,640,'#e8302a')]:
  b+=f'<rect x="{x}" y="{y}" width="240" height="22" rx="11" fill="{c}"/><circle cx="{x+40}" cy="{y+30}" r="12" fill="#f4f4f4"/><circle cx="{x+200}" cy="{y+30}" r="12" fill="#f4f4f4"/>'
b+='<path d="M380 340 Q340 280 380 260 Q400 252 400 290 Q400 252 420 260 Q460 280 420 340 L400 360Z" fill="none" stroke="#fff" stroke-width="10" stroke-linejoin="round"/>'
I[1810]=svg(b,d)

# 219 秋の気配: a harbour-side park at autumn dusk with a single falling leaf and an empty bench, 1977
d,b=bg([(0,'#7a6a9a'),(1,'#f8c08a')])
b+='<rect y="480" width="800" height="120" fill="#5a6a9a"/><rect y="600" width="800" height="200" fill="#8a6a4a"/>'+tree(640,600,360,'#c8602a',219)
b+='<rect x="220" y="560" width="260" height="14" fill="#3a2a2a"/><rect x="230" y="574" width="10" height="40" fill="#3a2a2a"/><rect x="460" y="574" width="10" height="40" fill="#3a2a2a"/><rect x="220" y="520" width="260" height="10" fill="#3a2a2a"/>'
b+='<path d="M360 300 q20 -30 40 0 q-20 30 -40 0Z" fill="#e8802a" transform="rotate(30 380 300)"/>'
I[219]=svg(b,d)

# 459 NO MORE 恋愛ごっこ: a toy heart crossed out with a big red X tape, schoolgirl idol group
d,b=bg([(0,'#ffe0f0'),(1,'#e0eaff')])
b+=heart(400,420,140,'#ff9ac0')+'<path d="M250 260 L550 580 M550 260 L250 580" stroke="#e8102a" stroke-width="30" stroke-linecap="round" opacity=".85"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(140,160,20),(660,180,26),(640,620,18)])
I[459]=svg(b,d)

# 534 きづいてよ: a girl waving behind a tall boy's back in a crowd, a tiny heart floating unseen
d,b=bg([(0,'#9ad0ff'),(1,'#fff0e0')])
b+='<rect y="640" width="800" height="160" fill="#c8b8a8"/>'+''.join(figure(x,660,260,'#8a8a9a') for x in (80,640,740))+figure(440,660,360,'#2a2a3a')+figure(250,660,220,'#e85a8a',pose='up',hair='#e85a8a')+heart(330,260,24,'#ff4a8a')
I[534]=svg(b,d)

# 822 SKIPPED BEAT: a heart-rate monitor line jumping erratically into a heart shape, 80s rock band
d,b=bg([(0,'#0a1a14'),(1,'#0a2a1a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#1a4a2a" stroke-width="2"/>' for y in range(100,800,60))+''.join(f'<path d="M{x} 0 L{x} 800" stroke="#1a4a2a" stroke-width="2"/>' for x in range(40,800,60))
b+='<path d="M0 440 L180 440 L210 360 L240 520 L270 440 L320 440 Q340 380 380 400 Q400 420 400 440 Q400 420 420 400 Q460 380 480 440 L400 540 L320 440 M480 440 L560 440 L590 300 L620 560 L650 440 L800 440" stroke="#3aff8a" stroke-width="8" fill="none" stroke-linejoin="round"/>'+glow(400,440,200,'#3aff8a',.25)
I[822]=svg(b,d)

# 152 津軽海峡・冬景色: a ferry crossing a stormy grey northern strait in snow with seagulls crying, enka
d,b=bg([(0,'#4a5468'),(1,'#9aa4b8')])
b+=snow(90,152)+'<rect y="460" width="800" height="340" fill="#3a4a5a"/>'+''.join(f'<path d="M{x} {y} q30 -24 60 0" stroke="#e8eef8" stroke-width="5" fill="none" opacity=".7"/>' for x,y in [(80,520),(300,560),(560,520),(200,660),(480,700),(660,640)])
b+='<path d="M260 480 L620 480 L580 540 L300 540Z" fill="#e8e8ec"/><rect x="340" y="420" width="200" height="60" fill="#f4f4f4"/><rect x="420" y="380" width="40" height="40" fill="#c8302a"/>'+''.join(f'<rect x="{x}" y="440" width="24" height="16" fill="#3a4a5a"/>' for x in range(360,530,40))
b+=bird(200,240,40,'#f4f4f4')+bird(280,200,30,'#f4f4f4')+bird(640,280,34,'#f4f4f4')+figure(600,480,80,'#1a1a24',hair='#1a1a24')
I[152]=svg(b,d)

# 141 おまえとふたり: an old couple sharing one umbrella and a paper lantern on a quiet evening lane, enka
d,b=bg([(0,'#2a2a3a'),(1,'#5a4a5a')])
b+=rain(50,141,'#cfe6ff',.3)+'<rect y="640" width="800" height="160" fill="#2a2430"/>'+figure(350,660,240,'#0a0a14')+figure(450,660,220,'#0a0a14',hair='#0a0a14')+wagasa(400,420,140,'#8a2a3a',0)+chochin(560,560,30)
I[141]=svg(b,d)

# 271 止まらないHa~Ha: a rock star's silhouette with a mic stand swung high, a white towel flying, 80s rock
d,b=bg([(0,'#0a0a0a'),(1,'#3a0a0a')])
b+=rays(400,0,10,'#fff',.15,40,40,140)+'<rect y="660" width="800" height="140" fill="#14100e"/>'+figure(400,680,380,'#000')
b+='<path d="M440 400 L620 160" stroke="#c8c8d0" stroke-width="10"/><circle cx="630" cy="146" r="16" fill="#3a3a3a"/><path d="M200 220 Q260 160 320 210 Q300 250 260 260 Q220 270 200 220Z" fill="#f4f4f4"/>'
I[271]=svg(b,d)

# 576 True Love: two hands forming a heart shape around the setting sun on a beach, 80s idol
d,b=bg([(0,'#ff6a8a'),(1,'#ffd8a0')])
b+='<circle cx="400" cy="400" r="80" fill="#fff0b0"/><rect y="480" width="800" height="120" fill="#e8806a"/><rect y="600" width="800" height="200" fill="#f0c890"/>'
b+='<path d="M400 520 Q300 460 270 380 Q250 300 330 290 Q380 290 400 340 Q420 290 470 290 Q550 300 530 380 Q500 460 400 520Z" fill="none" stroke="#3a1a1a" stroke-width="28" stroke-linejoin="round"/><rect x="250" y="520" width="50" height="280" fill="#3a1a1a" transform="rotate(20 275 520)"/><rect x="500" y="520" width="50" height="280" fill="#3a1a1a" transform="rotate(-20 525 520)"/>'
I[576]=svg(b,d)

# 1274 ワッハッハー: a giant laughing open-mouthed sun face with tears of joy over a cheering crowd
d,b=bg([(0,'#ffd04a'),(1,'#ff7a3a')])
b+=rays(400,320,22,'#fff',.25,12)+'<circle cx="400" cy="320" r="170" fill="#ffe84a"/><path d="M320 350 Q400 470 480 350Z" fill="#a8302a"/><path d="M330 290 Q350 270 370 290 M430 290 Q450 270 470 290" stroke="#a8302a" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+='<path d="M310 300 Q300 330 310 340 Q320 330 310 300Z M490 300 Q480 330 490 340 Q500 330 490 300Z" fill="#5ab0ff"/>'+''.join(figure(x,820,200,'#3a1a0a',pose='up') for x in range(70,800,110))
I[1274]=svg(b,d)

# 1653 恋ゲバ: a schoolgirl's silhouette in a fighting stance with a heart-shaped boxing target, quirky J-pop
d,b=bg([(0,'#ff3a5a'),(1,'#ffd04a')])
b+=''.join(ring(560,360,r,c,20) for r,c in [(140,'#fff'),(100,'#e8102a'),(60,'#fff')])+heart(560,360,34,'#e8102a')
b+='<rect y="640" width="800" height="160" fill="#2a1a2a"/>'+figure(240,660,340,'#1a1a2a',hair='#1a1a2a')+'<path d="M280 420 L400 380" stroke="#1a1a2a" stroke-width="24" stroke-linecap="round"/><path d="M220 440 L170 400" stroke="#1a1a2a" stroke-width="24" stroke-linecap="round"/>'
I[1653]=svg(b,d)

# 1679 We never give up!: a group of boys' silhouettes climbing a steep rope wall toward a sunrise
d,b=bg([(0,'#3a5ac8'),(1,'#ffc08a')])
b+='<circle cx="400" cy="140" r="70" fill="#fff4c8"/>'+rays(400,140,16,'#fff',.2,10)+'<path d="M80 800 L400 200 L720 800Z" fill="#4a3a4a"/>'+'<path d="M400 200 L400 800" stroke="#c8a870" stroke-width="8"/>'
b+=''.join(figure(400+dx,y,110,'#0a0a14',pose='up') for dx,y in [(-30,380),(30,480),(-40,590),(40,700)])
I[1679]=svg(b,d)

# 348 雨あがりの夜空に: a car's headlights and a wet road under a clear starry night sky after the rain, 1980 rock
d,b=bg([(0,'#050a24'),(1,'#1a2a4a')])
b+=starsf(90,348,500)+moon(620,140,40)+'<rect y="500" width="800" height="300" fill="#141a2a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="60" ry="8" fill="#8ab0e8" opacity=".25"/>' for x,y in [(120,620),(500,680),(680,600)])
b+='<path d="M220 560 L260 500 L460 500 L520 560 L560 570 L560 610 L180 610 L180 570Z" fill="#2a2a34"/><circle cx="250" cy="612" r="24" fill="#111"/><circle cx="490" cy="612" r="24" fill="#111"/><circle cx="550" cy="580" r="10" fill="#fff4c8"/><path d="M560 580 L800 540 L800 640Z" fill="#fff4c8" opacity=".25"/>'
I[348]=svg(b,d)

# 804 GOING GOING HOME: a night bus heading down a long road toward a small lit hometown, 90s techno-pop
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=starsf(50,804,400)+'<rect y="440" width="800" height="360" fill="#141428"/><path d="M380 440 L120 800 L680 800 L420 440Z" fill="#2a2a3a"/><path d="M400 460 L400 800" stroke="#ffd02a" stroke-width="5" stroke-dasharray="20 20"/>'
b+=''.join(f'<rect x="{x}" y="420" width="12" height="16" fill="#ffd27a"/>' for x in range(340,470,20))+'<rect x="300" y="600" width="200" height="120" rx="14" fill="#e8e8f0"/><rect x="316" y="616" width="168" height="50" fill="#3a5a8a"/><circle cx="330" cy="700" r="10" fill="#ff4a4a"/><circle cx="470" cy="700" r="10" fill="#ff4a4a"/>'
I[804]=svg(b,d)

# 919 本気がいっぱい: a big red heart bursting with flames and sparks above a stadium, 90s boy group
d,b=bg([(0,'#1a0a2a'),(1,'#a83a2a')])
b+=rays(400,340,20,'#ffd02a',.12,14)+'<path d="M400 160 Q480 260 450 300 Q540 260 510 190 Q600 320 530 440 L270 440 Q200 320 290 190 Q260 260 350 300 Q320 260 400 160Z" fill="#ff8a2a"/>'+heart(400,380,100,'#e8102a')
b+='<path d="M0 640 Q400 560 800 640 L800 800 L0 800Z" fill="#14080a"/>'+''.join(f'<circle cx="{x}" cy="{620+(x%5)*8}" r="5" fill="#ffd02a"/>' for x in range(30,800,40))
I[919]=svg(b,d)

# 959 HAKKA CANDY: a swirled mint candy unwrapping in a cool breeze, fresh mint leaves around
d,b=bg([(0,'#c8fff0'),(1,'#e8f8ff')])
b+='<path d="M180 420 L270 360 L270 480Z M620 420 L530 360 L530 480Z" fill="#8ad8c8"/><circle cx="400" cy="420" r="140" fill="#fff"/>'+''.join(f'<path d="M400 420 L{400+140*math.cos(a)} {420+140*math.sin(a)} A140 140 0 0 1 {400+140*math.cos(a+.5)} {420+140*math.sin(a+.5)}Z" fill="#3ad8a8"/>' for a in [k*math.pi/3 for k in range(6)])
b+=''.join(f'<path d="M{x} {y} q40 -40 80 0 q-40 40 -80 0Z" fill="#3aa86a" transform="rotate({r} {x} {y})"/>' for x,y,r in [(120,200,-30),(600,180,20),(150,640,40),(620,640,-20)])+''.join(f'<path d="M{x} {y} q40 -14 80 0" stroke="#8ad8c8" stroke-width="4" fill="none"/>' for x,y in [(80,320),(640,300),(300,700)])
I[959]=svg(b,d)

# 114 春一番: the first strong spring wind blowing hats, petals and a scarf across a sunny park, 1976 idol trio
d,b=bg([(0,'#8ad8ff'),(1,'#fff4e0')])
b+=''.join(f'<path d="M-20 {y} Q200 {y-60} 400 {y} T820 {y}" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>' for y in (240,360,480))+''.join(flower(x,y,14,5,'#ffc0d8','#ffd02a',x) for x,y in [(160,200),(300,300),(520,240),(640,380),(420,180),(220,420)])
b+='<rect y="620" width="800" height="180" fill="#8ac86a"/>'+''.join(figure(x,640,200,'#3a2a3a',hair='#3a2a3a') for x in (260,380,500))+'<g transform="rotate(-20 620 200)"><ellipse cx="620" cy="200" rx="60" ry="14" fill="#f4e0b0"/><path d="M580 198 Q620 150 660 198Z" fill="#f4e0b0"/></g>'
I[114]=svg(b,d)

# 272 YES MY LOVE: a white convertible at a night pier with a single rose on the seat, 80s rock ballad
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+=starsf(40,272,400)+moon(160,140,40)+'<rect y="480" width="800" height="320" fill="#0a1430"/>'+''.join(f'<rect x="{x}" y="500" width="40" height="6" fill="#ffd27a" opacity=".4"/>' for x in range(60,800,90))
b+='<path d="M140 640 L200 580 L560 580 L640 640 L680 650 L680 700 L120 700 L120 650Z" fill="#f4f4f4"/><circle cx="220" cy="704" r="34" fill="#111"/><circle cx="560" cy="704" r="34" fill="#111"/>'+rose(380,580,.6,0)
I[272]=svg(b,d)

# 504 十七歳の地図: a crumpled city map with a hand-drawn route and a youth on a pedestrian bridge, 1983 rock
d,b=bg([(0,'#3a2a4a'),(1,'#e88a5a')])
b+='<rect x="120" y="120" width="560" height="440" fill="#f4ecd8" transform="rotate(-4 400 340)"/>'+''.join(f'<path d="M{x} 140 L{x+20} 540" stroke="#c8b898" stroke-width="3"/>' for x in range(160,680,80))+''.join(f'<path d="M140 {y} L660 {y-20}" stroke="#c8b898" stroke-width="3"/>' for y in range(180,560,70))
b+='<path d="M200 480 Q300 400 360 420 Q460 460 500 320 Q540 240 600 220" stroke="#e8302a" stroke-width="8" fill="none" stroke-dasharray="16 10"/>'+star5(600,220,26,'#e8302a')
b+='<rect y="640" width="800" height="20" fill="#2a1a24"/><rect y="660" width="800" height="140" fill="#1a1018"/>'+figure(300,640,160,'#000')
I[504]=svg(b,d)

# 1478 TACTIC: a chessboard with a knight piece casting a long neon shadow, 2026 electro duet
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a4a')])
b+=''.join(f'<path d="M{100+i*75} 760 L{250+i*37.5} 420" stroke="#3a3a5a" stroke-width="2"/>' for i in range(9))+''.join(f'<path d="M{100+k*18.75} {760-k*42.5} L{700-k*18.75} {760-k*42.5}" stroke="#3a3a5a" stroke-width="2"/>' for k in range(9))
b+='<path d="M360 640 L460 640 L450 600 L430 600 L440 520 Q470 480 450 440 Q420 380 360 400 L330 450 L350 470 L380 450 L370 500 L380 600 L360 600Z" fill="#f4f4f4"/><rect x="340" y="640" width="140" height="24" fill="#f4f4f4"/>'+'<path d="M480 660 L760 560" stroke="#ff4fd0" stroke-width="40" opacity=".3"/>'+glow(410,520,160,'#3affe8',.3)
I[1478]=svg(b,d)

# 13 明日があるさ: a cheerful young salaryman's silhouette walking with a briefcase toward a smiling morning sun, 1960s
d,b=bg([(0,'#7ac8ff'),(1,'#fff4d8')])
b+='<circle cx="560" cy="240" r="90" fill="#ffe04a"/><path d="M520 250 Q560 290 600 250" stroke="#c8702a" stroke-width="8" fill="none"/><circle cx="530" cy="220" r="8" fill="#c8702a"/><circle cx="590" cy="220" r="8" fill="#c8702a"/>'+rays(560,240,16,'#fff',.3,10)
b+='<rect y="600" width="800" height="200" fill="#c8c0b0"/>'+figure(300,620,280,'#1a1a2a')+'<rect x="330" y="500" width="60" height="44" rx="6" fill="#5a3a2a"/>'
I[13]=svg(b,d)

# 175 きよしのズンドコ節: a big festival drum with a fan and colourful streamers, energetic enka-pop
d,b=bg([(0,'#ff4a4a'),(1,'#ffd04a')])
b+=rays(400,400,20,'#fff',.2,12)+confetti(40,175,['#fff','#3ab0ff','#5ad87a'])+'<circle cx="400" cy="420" r="170" fill="#8a3a1a"/><circle cx="400" cy="420" r="140" fill="#f4e8d0"/>'+''.join(f'<circle cx="{400+155*math.cos(a)}" cy="{420+155*math.sin(a)}" r="6" fill="#1a1a1a"/>' for a in [k*math.pi/10 for k in range(20)])
b+='<path d="M220 240 L360 380 M580 240 L440 380" stroke="#5a3a2a" stroke-width="16" stroke-linecap="round"/>'
I[175]=svg(b,d)

# 460 かたつむりサンバ: a snail with maracas dancing samba on a rainy hydrangea leaf, quirky idol song
d,b=bg([(0,'#9ab8e8'),(1,'#e0e8ff')])
b+=rain(30,460,'#fff',.4)+'<path d="M80 600 Q400 380 720 600 Q400 700 80 600Z" fill="#5ab84a"/>'+''.join(''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="18" fill="{c}"/>' for dx,dy in [(-20,0),(20,0),(0,-18),(0,18)]) for x,y,c in [(120,300,'#8a6ae8'),(660,280,'#6a8ae8')])
b+='<circle cx="380" cy="480" r="70" fill="#e8a05a"/>'+''.join(ring(380,480,r,'#a8602a',6) for r in (24,48))+'<path d="M300 560 Q320 540 460 540 Q520 540 520 480 L540 470 L540 560 Q520 580 300 570Z" fill="#c8c08a"/><path d="M520 480 L530 430 M535 480 L555 435" stroke="#c8c08a" stroke-width="5"/>'
b+='<ellipse cx="570" cy="430" rx="16" ry="22" fill="#ff5a5a"/><ellipse cx="270" cy="460" rx="16" ry="22" fill="#ffd02a"/>'+note(640,420,30,'#3a3a5a')
I[460]=svg(b,d)

# 1766 Mr.Summertime: a man in a white suit's silhouette walking on a summer beach at golden hour, 70s chorus pop
d,b=bg([(0,'#ff9a5a'),(1,'#ffe0a0')])
b+='<circle cx="560" cy="440" r="100" fill="#fff0b0"/><rect y="480" width="800" height="120" fill="#e8805a"/><rect y="600" width="800" height="200" fill="#f0c890"/>'
b+=figure(300,700,320,'#f4f0e8')+'<ellipse cx="300" cy="400" rx="56" ry="12" fill="#f4f0e8"/><path d="M270 400 Q300 360 330 400Z" fill="#f4f0e8"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="6" fill="#d8a870"/>' for x,y in [(380,720),(440,740),(500,730),(560,760)])
I[1766]=svg(b,d)

# 142 倖せさがして: a small lit house window far across a snowy field seen by a wandering figure, enka
d,b=bg([(0,'#1a2440'),(1,'#4a5a7a')])
b+=snow(60,142)+'<rect y="520" width="800" height="280" fill="#e0e8f4"/><rect x="560" y="440" width="120" height="80" fill="#3a2a2a"/><path d="M550 445 L620 400 L690 445Z" fill="#f4f6ff"/><rect x="600" y="465" width="30" height="30" fill="#ffd27a"/>'+glow(615,480,80,'#ffd27a',.6)
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="#b8c4d8"/>' for x,y in [(200,760),(230,720),(270,690),(300,650)])+figure(320,640,200,'#1a1a24')
I[142]=svg(b,d)

# 163 俺ら東京さ行ぐだ: a farmer's silhouette with a bundle on a stick leaving a thatched village toward a distant city skyline
d,b=bg([(0,'#8ac8ff'),(1,'#f4f0d8')])
b+='<path d="M0 520 L800 520 L800 800 L0 800Z" fill="#a8c86a"/>'+skyline(520,'#9aa0b8',163,20,100)+'<path d="M380 800 L460 520 L480 520 L420 800Z" fill="#d8c8a0"/>'
b+='<rect x="60" y="440" width="200" height="120" fill="#8a6a4a"/><path d="M30 450 L160 340 L290 450Z" fill="#c8a860"/>'+figure(520,700,240,'#2a2a1a')+'<path d="M560 460 L640 360" stroke="#5a3a2a" stroke-width="6"/><circle cx="645" cy="350" r="26" fill="#3a6aa8"/>'
I[163]=svg(b,d)

# 1275 急☆上☆Show!!: a rocket-shaped rising chart arrow shooting up through stars, comedic boy group
d,b=bg([(0,'#1a0a4a'),(1,'#ff5a8a')])
b+=starsf(50,1275,700)+''.join(f'<rect x="{x}" y="{800-h}" width="70" height="{h}" fill="#fff" opacity=".2"/>' for x,h in [(100,100),(200,180),(300,260),(400,380),(500,520)])
b+='<path d="M120 700 L260 600 L360 640 L520 360 L600 300" stroke="#ffd02a" stroke-width="18" fill="none" stroke-linejoin="round"/><polygon points="660,220 580,260 640,320" fill="#ffd02a"/>'+star5(660,180,30,'#fff')+star5(560,140,20,'#fff')
I[1275]=svg(b,d)

# 186 流星: a shooting star over a dark mountain lake with a lone camper's fire, 1979 folk
d,b=bg([(0,'#050a1a'),(1,'#1a2440')])
b+=starsf(100,186,500)+'<path d="M180 120 L520 300" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>'+glow(520,300,40,'#fff',.7)+hills(500,80,'#0a0e1a',186,4)
b+='<rect y="540" width="800" height="260" fill="#0a1020"/>'+'<path d="M380 620 L420 620 L400 580Z" fill="#ff8a2a"/>'+glow(400,610,80,'#ff8a2a',.6)+figure(330,640,140,'#000')
I[186]=svg(b,d)

# 293 君こそスターだ: a spotlight hitting an ordinary person in a crowd as glitter falls, 2005 rock
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+='<path d="M360 0 L440 0 L560 680 L240 680Z" fill="#fff4c8" opacity=".25"/>'+confetti(50,293,['#ffd02a','#fff'],0,600)+''.join(figure(x,820,200,'#1a1a24') for x in (80,180,600,700))+figure(400,740,240,'#ffd02a',pose='up')
I[293]=svg(b,d)

# 678 J.BOY: a young man in a jacket at a busy scramble crossing at night with neon around, 1986/99 rock
d,b=bg([(0,'#0a0a24'),(1,'#2a1a3a')])
b+=skyline(460,'#14142a',678,100,320,'#ff8ad0',80)+'<rect y="460" width="800" height="340" fill="#1a1a24"/>'+''.join(f'<rect x="{x}" y="{y}" width="60" height="16" fill="#e8e8e8" transform="rotate(30 {x} {y})"/>' for x in range(60,800,90) for y in (560,700))
b+=''.join(figure(x,y,120,'#3a3a4a') for x,y in [(120,620),(620,600),(700,700),(200,740)])+figure(400,760,300,'#000')
I[678]=svg(b,d)

# 1276 なぐりガキBEAT: messy crayon scribbles forming a drum and lightning beat, raw punk energy
d,b=bg([(0,'#f4f0e4'),(1,'#e8e0d0')])
b+=''.join(f'<path d="M{x} {y} q30 -40 60 0 t60 0 t60 0" stroke="{c}" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>' for x,y,c in [(80,140,'#e8302a'),(480,200,'#3a6ae8'),(100,680,'#5ab84a'),(480,700,'#ff9a2a')])
b+='<ellipse cx="400" cy="380" rx="170" ry="50" fill="none" stroke="#1a1a1a" stroke-width="10"/><path d="M230 380 L250 560 Q400 620 550 560 L570 380" fill="none" stroke="#1a1a1a" stroke-width="10"/><path d="M260 420 L540 540 M540 420 L260 540" stroke="#e8302a" stroke-width="8"/>'
b+='<path d="M300 280 L230 160 M500 280 L580 160" stroke="#1a1a1a" stroke-width="12" stroke-linecap="round"/>'+bolt([(640,260),(600,360),(650,370),(610,470)],'#ffd02a',12)
I[1276]=svg(b,d)

# 1670 春咲小紅: a bright red camellia blossom blooming early beside a pair of red lips-shaped petals, techno-pop
d,b=bg([(0,'#fff0f4'),(1,'#ffe0d0')])
b+=''.join(f'<rect x="{x}" y="0" width="4" height="800" fill="#ffc0c8" opacity=".5"/>' for x in range(40,800,80))+'<path d="M380 800 Q360 640 400 520" stroke="#3a6a3a" stroke-width="10" fill="none"/><path d="M390 640 q-80 -30 -100 20 q60 20 100 -20Z" fill="#3a8a3a"/>'
b+=flower(400,420,130,6,'#e8102a','#ffd02a',15)+sparkle(200,200,24,'#ff7aa8')+sparkle(620,260,20,'#ff7aa8')
I[1670]=svg(b,d)

# 1826 愛がひとりぼっち: a single heart-shaped balloon drifting alone over an empty playground at dusk, 1985
d,b=bg([(0,'#5a4a8a'),(1,'#ffa88a')])
b+='<rect y="600" width="800" height="200" fill="#7a6a6a"/><path d="M120 600 L180 400 L240 600 M180 400 L460 400 M400 400 L340 600 M460 400 L520 600" stroke="#2a2030" stroke-width="10" fill="none"/><path d="M280 400 L280 520 M360 400 L360 520" stroke="#2a2030" stroke-width="3"/><rect x="270" y="520" width="100" height="12" fill="#2a2030"/>'
b+='<path d="M600 300 Q580 450 560 600" stroke="#2a2030" stroke-width="3" fill="none"/>'+heart(600,260,50,'#ff4a6a')
I[1826]=svg(b,d)

# 21 大阪の女: a woman in a kimono on a canal bridge at night with neon reflections, 1970 twin-sister enka
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a3a')])
b+=skyline(480,'#14102a',21,80,240,'#ff8ad0',50)+'<rect y="480" width="800" height="320" fill="#100a24"/>'+''.join(f'<rect x="{x}" y="500" width="10" height="200" fill="{c}" opacity=".3"/>' for x,c in [(120,'#ff4fa0'),(260,'#ffd02a'),(560,'#4fd0ff'),(680,'#ff4fa0')])
b+='<path d="M200 520 Q400 440 600 520" stroke="#3a2a3a" stroke-width="18" fill="none"/>'+figure(400,490,220,'#000',hair='#000')+'<path d="M370 360 L430 360 L450 490 L350 490Z" fill="#6a1a3a"/>'
I[21]=svg(b,d)

# 115 年下の男の子: a girl patting the head of a shorter boy under a blossom-free spring sky, 1975 idol trio
d,b=bg([(0,'#ffd8e8'),(1,'#e0f0ff')])
b+='<rect y="620" width="800" height="180" fill="#a8d08a"/>'+figure(320,640,300,'#5a2a4a',hair='#5a2a4a')+figure(470,640,220,'#2a3a5a')+'<path d="M350 400 Q420 380 460 420" stroke="#5a2a4a" stroke-width="20" fill="none" stroke-linecap="round"/>'+heart(560,280,30,'#ff7aa8')+heart(610,230,18,'#ff9ac0')
I[115]=svg(b,d)

# 148 好きになった人: a woman waving a handkerchief from a station platform as a train departs, 1968 enka
d,b=bg([(0,'#ffb08a'),(1,'#f8e0c8')])
b+='<rect y="560" width="800" height="240" fill="#8a7a7a"/><rect y="560" width="800" height="14" fill="#e8e0d0"/><rect x="420" y="400" width="380" height="160" fill="#4a6a5a"/>'+''.join(f'<rect x="{x}" y="430" width="50" height="40" fill="#ffe8b0"/>' for x in (450,530,610,690))
b+=figure(260,580,240,'#2a1a2a',hair='#2a1a2a',pose='up')+'<path d="M290 340 L330 320 L340 360 L300 370Z" fill="#fff"/>'
I[148]=svg(b,d)

# 212 サボテンの花: a small cactus in a pot blooming with one pink flower on a frosty window sill, 1975 folk rock
d,b=bg([(0,'#c8d8e8'),(1,'#eef2f6')])
b+='<rect x="120" y="80" width="560" height="420" fill="#dce8f4"/>'+snow(30,212,.7,500)+'<rect x="120" y="80" width="560" height="420" fill="none" stroke="#7a6a5a" stroke-width="18"/><rect x="80" y="500" width="640" height="40" fill="#7a6a5a"/><rect y="540" width="800" height="260" fill="#5a4a40"/>'
b+='<path d="M340 500 L330 420 L470 420 L460 500Z" fill="#c8704a"/><rect x="370" y="260" width="60" height="170" rx="30" fill="#3a8a4a"/><rect x="320" y="320" width="40" height="70" rx="20" fill="#3a8a4a"/><rect x="440" y="300" width="40" height="80" rx="20" fill="#3a8a4a"/>'+flower(400,250,30,6,'#ff7aa8','#ffd02a')
I[212]=svg(b,d)

# 1637 GOD_i: a silhouette standing in a beam of golden light with a glowing halo ring above, 2025 hip-hop
d,b=bg([(0,'#0a0a0a'),(1,'#2a2010')])
b+='<path d="M340 0 L460 0 L600 700 L200 700Z" fill="#ffd27a" opacity=".2"/>'+'<ellipse cx="400" cy="250" rx="70" ry="16" fill="none" stroke="#ffd02a" stroke-width="8"/>'+glow(400,250,90,'#ffd02a',.6)+figure(400,700,420,'#000')+'<rect y="700" width="800" height="100" fill="#14100a"/>'
I[1637]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
