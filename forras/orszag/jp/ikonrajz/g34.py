import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 34. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1836 ETERNAL BLAZE: a magic staff with a pink crystal tip blazing with an eternal flame ring, night sky
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=starsf(80,1836,800)+''.join(ring(400,300,r,'#ff7ad0',4,.7) for r in (90,130))+glow(400,300,120,'#ff6ac0',.6)
b+='<g transform="rotate(20 400 500)"><rect x="390" y="300" width="20" height="440" fill="#e8e8f4"/><polygon points="400,180 440,280 400,320 360,280" fill="#ff6ac0"/><rect x="370" y="300" width="60" height="16" fill="#ffd02a"/></g>'
b+=''.join(f'<path d="M{400+150*math.cos(a)} {300+150*math.sin(a)} q10 -30 0 -50" stroke="#ffb02a" stroke-width="8" fill="none"/>' for a in [k*math.pi/4 for k in range(8)])
I[1836]=svg(b,d)

# 483 Cloudy Heart: a heart made of grey storm clouds with rain falling from it, 80s rock
d,b=bg([(0,'#2a2a3a'),(1,'#4a4a5a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9a9aa8"/>' for x,y,r in [(320,300,80),(480,300,80),(400,360,90),(340,400,60),(460,400,60),(400,470,40)])+'<circle cx="300" cy="280" r="40" fill="#b8b8c4"/>'
b+=''.join(f'<path d="M{x} {500+(x%3)*10} l-10 40" stroke="#cfe6ff" stroke-width="4" stroke-linecap="round"/>' for x in range(330,480,26))+rain(30,483,'#cfe6ff',.3,8)
I[483]=svg(b,d)

# 494 Bambina: a little girl's red balloon floating above a millennium city skyline at dawn
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=skyline(640,'#3a2a3a',494,120,380,'#ffd27a',50)+'<rect y="640" width="800" height="160" fill="#2a1a2a"/>'
b+='<path d="M420 300 Q440 460 400 640" stroke="#2a1a2a" stroke-width="3" fill="none"/><ellipse cx="420" cy="230" rx="70" ry="84" fill="#e8102a"/><ellipse cx="396" cy="200" rx="14" ry="22" fill="#fff" opacity=".5"/>'+figure(400,700,120,'#000',pose='up',hair='#000')
I[494]=svg(b,d)

# 552 私について: a hand mirror reflecting a woman's eye-free silhouette with a single red rose, 1990 diva
d,b=bg([(0,'#3a1a2a'),(1,'#7a3a4a')])
b+='<ellipse cx="400" cy="340" rx="190" ry="230" fill="#c8a24a"/><ellipse cx="400" cy="340" rx="170" ry="210" fill="#e8dce0"/><rect x="380" y="560" width="40" height="200" rx="16" fill="#c8a24a"/>'
b+=profile(420,540,1.0,'#3a1a2a',True)+rose(320,480,.6,-20)
I[552]=svg(b,d)

# 563 はいからさんが通る: a Taisho-era girl in hakama riding a bicycle, cherry blossoms, retro romance
d,b=bg([(0,'#ffe8f0'),(1,'#f4d8c8')])
b+=petals(30,563,'#ffb8cc')+''.join(sakura(x,y,s,'#ffc0d6','#ff7aa8',r) for x,y,s,r in [(100,120,60,0),(700,160,50,20)])+'<rect y="620" width="800" height="180" fill="#c8a888"/>'
b+=ring(300,640,60,'#3a2a2a',8)+ring(520,640,60,'#3a2a2a',8)+'<path d="M300 640 L390 560 L520 640 M390 560 L440 540" stroke="#3a2a2a" stroke-width="8" fill="none"/>'
b+=figure(410,580,200,'#5a2a5a',hair='#1a1a1a')+'<path d="M370 500 L450 500 L470 600 L350 600Z" fill="#7a2a5a"/>'+'<path d="M385 330 Q410 300 440 330" stroke="#e8102a" stroke-width="12" fill="none"/>'
I[563]=svg(b,d)

# 583 ザ・ストレス 中近東バージョン: a stressed office clock melting over a desert with palm trees, belly-dance pop
d,b=bg([(0,'#ffb04a'),(1,'#ffe8a0')])
b+='<circle cx="620" cy="160" r="70" fill="#fff4c8"/><path d="M0 560 Q200 500 400 540 Q600 580 800 520 L800 800 L0 800Z" fill="#e8b860"/>'+''.join(f'<path d="M{x} 560 L{x} 380" stroke="#6a4a2a" stroke-width="10"/><path d="M{x} 380 q-50 -10 -80 20 M{x} 380 q50 -10 80 20 M{x} 380 q-20 -40 -50 -50 M{x} 380 q20 -40 50 -50" stroke="#3a7a2a" stroke-width="10" fill="none"/>' for x in (130,690))
b+='<path d="M280 300 Q400 240 520 300 Q560 420 500 480 Q480 540 470 600 Q440 520 400 500 Q320 480 290 420Z" fill="#f4f4f8" stroke="#3a3a3a" stroke-width="6"/><path d="M400 380 L400 310 M400 380 L450 400" stroke="#3a3a3a" stroke-width="8" stroke-linecap="round"/>'
I[583]=svg(b,d)

# 1018 ハッピーサマーウェディング: a wedding bouquet tossed high into a bright summer sky with confetti
d,b=bg([(0,'#3ab0ff'),(1,'#d8f4ff')])
b+=confetti(70,1018,['#ff8ab0','#fff','#ffd02a','#8ad0ff'])+cloud(160,180,1.2)
b+='<path d="M380 460 L420 460 L400 560Z" fill="#fff"/>'+''.join(rose(x,y,.4,a) for x,y,a in [(370,420,0),(430,420,30),(400,390,60),(400,440,90)])+'<path d="M400 560 Q380 620 400 680" stroke="#fff" stroke-width="6" fill="none"/>'
b+=figure(250,800,260,'#fff',pose='up',hair='#fff')
I[1018]=svg(b,d)

# 1644 All 4 U: eleven little stars forming one big heart shape in a youthful night sky
d,b=bg([(0,'#0a1a3a'),(1,'#3a2a6a')])
pts=[(400+180*16*math.sin(t)**3/16,370-180*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))/16) for t in [k*2*math.pi/11 for k in range(11)]]
b+=starsf(60,1644,800)+''.join(star5(x,y,22,'#fff4c8')+glow(x,y,20,'#fff4c8',.5) for x,y in pts)+'<polyline points="'+' '.join(f'{x:.0f},{y:.0f}' for x,y in pts+[pts[0]])+'" stroke="#fff4c8" stroke-width="2" fill="none" opacity=".4"/>'
I[1644]=svg(b,d)

# 1707 ただ泣きたくなるの: a single woman at a wedding reception window, a bridal veil drifting past, mid-90s
d,b=bg([(0,'#e8d8e8'),(1,'#b8a8c8')])
b+='<rect x="100" y="100" width="300" height="460" fill="#fff4e8"/>'+glow(250,320,160,'#fff',.5)+'<path d="M180 160 Q260 300 200 520 Q300 400 320 200Z" fill="#fff" opacity=".8"/>'
b+='<rect y="560" width="800" height="240" fill="#8a7a98"/>'+figure(560,620,280,'#2a1a3a',hair='#2a1a3a')+'<path d="M560 330 Q552 350 560 360 Q568 350 560 330Z" fill="#cfe6ff"/>'
I[1707]=svg(b,d)

# 193 夢の中へ: someone searching through a drawer that opens into a starry dream world, early-70s
d,b=bg([(0,'#f0e0c8'),(1,'#d8c0a0')])
b+='<rect x="160" y="300" width="480" height="380" fill="#8a5a3a"/><rect x="180" y="320" width="440" height="160" fill="#7a4a2a"/><rect x="140" y="480" width="520" height="160" fill="#a86a3a"/>'
b+='<rect x="160" y="490" width="480" height="40" fill="#1a1a4a"/>'+''.join(sparkle(x,y,s,'#fff4c8') for x,y,s in [(260,420,20),(400,360,30),(520,440,18),(330,250,14),(480,220,22)])+glow(400,420,140,'#7ab0ff',.5)+'<circle cx="400" cy="560" r="14" fill="#ffd02a"/>'
I[193]=svg(b,d)

# 484 Dreamin': a teenager on a rooftop with a guitar staring at a giant moon, 80s rebel dreams
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=starsf(80,484,500)+moon(400,300,150)+skyline(640,'#0a0a1a',484,40,160)+'<rect y="640" width="800" height="160" fill="#14141e"/>'
b+=figure(400,660,200,'#000')+guitar(430,560,.5,30,'#000')
I[484]=svg(b,d)

# 181 恋人も濡れる街角: a rainy Yokohama street corner with a gas lamp, a couple under one coat, early-80s
d,b=bg([(0,'#1a2030'),(1,'#3a4050')])
b+=rain(100,181,'#cfe6ff',.4)+'<rect x="0" y="200" width="260" height="400" fill="#3a2a24"/>'+''.join(f'<rect x="{x}" y="260" width="40" height="60" fill="#ffd27a" opacity=".7"/>' for x in (40,120,200))
b+='<rect x="560" y="220" width="12" height="380" fill="#1a1a1a"/><path d="M540 200 L590 200 L580 240 L550 240Z" fill="#1a1a1a"/>'+glow(566,230,60,'#ffd27a',.6)+'<rect y="600" width="800" height="200" fill="#2a2a34"/>'
b+=figure(380,640,240,'#000')+figure(430,640,220,'#000',hair='#000')+'<path d="M340 400 Q400 360 470 400 L470 430 L340 430Z" fill="#000"/>'
I[181]=svg(b,d)

# 377 ピンクのモーツァルト: a pink grand piano keyboard with a sparkling lipstick-pink bow, autumn cosmetic
d,b=bg([(0,'#ffd8e8'),(1,'#f4b8d0')])
b+='<path d="M100 500 Q100 400 260 400 L560 400 Q700 400 700 520 L700 580 L100 580Z" fill="#ff8ab8"/>'+''.join(f'<rect x="{x}" y="540" width="24" height="40" fill="#fff"/>' for x in range(120,690,28))
b+='<path d="M400 320 Q330 260 340 240 Q390 250 400 320 Q410 250 460 240 Q470 260 400 320Z" fill="#e8306a"/>'+''.join(note(x,y,24,'#c8306a') for x,y in [(200,260),(600,220),(660,330)])+''.join(f'<path d="M{x} {y} q10 20 0 40" stroke="#d8803a" stroke-width="4" fill="none"/>' for x,y in [(140,140),(700,120)])
I[377]=svg(b,d)

# 564 話しかけたかった: a girl hiding behind a library bookshelf watching a boy reading, shy pastel
d,b=bg([(0,'#f8ead8'),(1,'#e8d0b0')])
b+='<rect x="60" y="100" width="260" height="640" fill="#7a4a2a"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="90" fill="{c}"/>' for y in (130,250,370,490,610) for x,w,c in [(80,30,'#c8402a'),(114,24,'#3a6aa8'),(142,36,'#e8c050'),(182,22,'#5a8a4a'),(208,30,'#a85a8a'),(242,26,'#3a6aa8'),(272,30,'#e8c050')])
b+=figure(360,740,300,'#3a2a3a',hair='#3a2a3a')+'<rect x="440" y="560" width="300" height="20" fill="#8a5a3a"/>'+figure(600,560,180,'#2a2a3a')+'<rect x="560" y="490" width="70" height="44" fill="#f4f0e8"/>'+heart(330,380,16,'#ff5a8a')
I[564]=svg(b,d)

# 588 ドレス: an empty black gothic dress on a mannequin fading into dust, dim purple
d,b=bg([(0,'#0a0614'),(1,'#2a1a3a')])
b+=glow(400,400,200,'#8a4ab0',.35)+'<rect x="394" y="110" width="12" height="80" fill="#3a2a3a"/><ellipse cx="400" cy="200" rx="60" ry="30" fill="#3a2a3a"/>'
b+='<path d="M340 210 L460 210 L470 340 Q560 560 600 700 L200 700 Q240 560 330 340Z" fill="#050208"/><path d="M330 340 L470 340" stroke="#8a4ab0" stroke-width="5"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#c8a0e8" opacity=".7"/>' for x,y in [(620,600),(650,560),(680,520),(640,480),(700,460),(670,420)])
I[588]=svg(b,d)

# 726 promise: a pinky promise between two gloved hands over a snowy ski slope at night lights
d,b=bg([(0,'#0a1a3a'),(1,'#3a5a8a')])
b+=snow(60,726)+'<path d="M0 520 L800 360 L800 800 L0 800Z" fill="#e8f0ff"/>'+''.join(glow(x,y,30,'#ffd27a',.7) for x,y in [(100,440),(260,400),(420,370),(580,340)])
b+='<path d="M180 600 Q280 520 360 500 L380 530 Q300 560 240 640Z" fill="#e8402a"/><path d="M620 600 Q520 520 440 500 L420 530 Q500 560 560 640Z" fill="#3a6ae8"/><path d="M370 505 Q400 480 430 505" stroke="#f0c8a8" stroke-width="16" fill="none" stroke-linecap="round"/>'
I[726]=svg(b,d)

# 877 JAM: a highway traffic jam at night with endless red tail-lights, a lonely radio glow, 1996 rock
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+=skyline(400,'#141420',877,40,140,'#ffd27a',40)+'<polygon points="400,400 0,800 800,800" fill="#2a2a34"/>'
for k in range(7):
    y=420+k*55;w=24+k*18
    for s in (-1,1): b+=f'<rect x="{400+s*(40+k*50)-w/2}" y="{y}" width="{w}" height="{w*.5}" rx="6" fill="#1a1a24"/>'+glow(400+s*(40+k*50)-w*.3,y+w*.3,w*.25,'#ff2a2a',.9,'glow2')+glow(400+s*(40+k*50)+w*.3,y+w*.3,w*.25,'#ff2a2a',.9,'glow2')
I[877]=svg(b,d)

# 1185 Tokyo Girl: a glamorous woman's silhouette on a Tokyo Tower-view balcony with a cocktail glass, neon pink
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a4a')])
b+=skyline(560,'#140a1a',1185,80,300,'#ff7ad0',90)+tokyo_tower(600,560,380)+'<rect y="560" width="800" height="240" fill="#0a0410"/><rect x="0" y="540" width="500" height="20" fill="#3a2a3a"/>'
b+=figure(280,560,300,'#000',pose='hold',hair='#000')+'<path d="M260 380 L300 380 L280 410Z" fill="#ff7ad0" opacity=".8"/>'
I[1185]=svg(b,d)

# 1295 SAYONARAベイベー: a woman's hand letting go of a man's tie as the string of a heart balloon snaps
d,b=bg([(0,'#2a1a2a'),(1,'#5a2a4a')])
b+='<path d="M400 340 Q380 460 430 520" stroke="#fff" stroke-width="3" fill="none"/><path d="M430 520 Q450 600 400 680" stroke="#fff" stroke-width="3" fill="none" stroke-dasharray="6 10"/>'+heart(400,240,100,'#ff3a7a')
b+='<path d="M380 700 L420 700 L440 800 L360 800Z" fill="#c8102a"/><path d="M500 640 Q560 600 620 640 L600 690 Q560 670 520 690Z" fill="#f0c8a8"/>'
I[1295]=svg(b,d)

# 328 家に帰ろう: a warm-lit house at dusk with a family dinner table glowing inside, a woman walking home
d,b=bg([(0,'#3a3a6a'),(1,'#f0a888')])
b+='<rect x="380" y="320" width="340" height="300" fill="#e8d8c0"/><path d="M360 330 L550 200 L740 330Z" fill="#8a3a2a"/><rect x="420" y="380" width="120" height="100" fill="#ffd27a"/><rect x="580" y="380" width="100" height="100" fill="#ffd27a"/>'+glow(480,430,80,'#ffd27a',.5)+'<rect x="440" y="440" width="80" height="12" fill="#6a3a2a"/>'
b+='<rect y="620" width="800" height="180" fill="#5a5a6a"/>'+figure(200,660,240,'#1a1a2a',hair='#1a1a2a')+'<rect x="220" y="520" width="40" height="50" fill="#3a2a2a"/>'
I[328]=svg(b,d)

# 354 ハイスクールララバイ: a school desk with a sleeping head-down silhouette and floating zzz, techno-pop 1981
d,b=bg([(0,'#3a3a6a'),(1,'#8a8ab8')])
b+=''.join(f'<rect x="{x}" y="0" width="4" height="800" fill="#fff" opacity=".08"/>' for x in range(0,800,40))+'<rect x="80" y="100" width="640" height="200" fill="#2a4a3a"/>'
b+='<rect x="200" y="480" width="400" height="30" fill="#a87a4a"/><rect x="220" y="510" width="20" height="200" fill="#5a5a6a"/><rect x="560" y="510" width="20" height="200" fill="#5a5a6a"/>'
b+='<ellipse cx="400" cy="450" rx="60" ry="44" fill="#1a1a2a"/><path d="M320 480 Q400 430 480 480Z" fill="#1a1a3a"/>'+''.join(txt(x,y,'Z',s,'#fff',900) for x,y,s in [(500,380,40),(550,320,56),(610,250,72)])
I[354]=svg(b,d)

# 1144 粉雪: powder snow falling heavily on a lone figure in a white field, deep winter blue
d,b=bg([(0,'#5a7aa8'),(1,'#c8d8ec')])
b+=snow(160,1144,.95)+'<path d="M0 600 Q400 560 800 600 L800 800 L0 800Z" fill="#f4f8ff"/>'+figure(400,640,220,'#1a2a4a')+snow(60,11440,.9)
I[1144]=svg(b,d)

# 1249 ONE DROP: a single drop of red wine falling into a crystal glass, splash crown frozen in time
d,b=bg([(0,'#0a0a10'),(1,'#1a1418'),])
b+=glow(400,480,160,'#8a0a2a',.4)+'<path d="M290 360 Q290 560 400 580 Q510 560 510 360Z" fill="#cfe0ff" opacity=".2" stroke="#cfe0ff" stroke-width="3"/><path d="M296 480 Q300 560 400 572 Q500 560 504 480Z" fill="#6a0a1a"/>'
b+='<path d="M360 480 L370 450 L384 476 L400 440 L416 476 L430 450 L440 480Z" fill="#8a0a2a"/><path d="M400 240 Q384 280 400 300 Q416 280 400 240Z" fill="#a8102a"/><rect x="396" y="580" width="8" height="120" fill="#cfe0ff" opacity=".4"/>'
I[1249]=svg(b,d)

# 1886 エイリアンズ: two silhouettes on a suburban bypass bridge at night watching a UFO-like light pass, dreamy
d,b=bg([(0,'#0a0a2a'),(1,'#2a3a5a')])
b+=starsf(80,1886,500)+'<ellipse cx="560" cy="200" rx="80" ry="20" fill="#cfffe0"/><ellipse cx="560" cy="186" rx="34" ry="20" fill="#cfffe0"/>'+glow(560,200,90,'#a8ffd0',.5)+'<polygon points="560,210 480,520 640,520" fill="#a8ffd0" opacity=".12"/>'
b+='<rect y="520" width="800" height="40" fill="#3a3a4a"/><rect y="560" width="800" height="240" fill="#0a0a14"/>'+''.join(glow(x,600,14,'#ffd27a',.8,'glow2') for x in range(40,800,90))+figure(240,520,160,'#000')+figure(300,520,150,'#000',hair='#000')
I[1886]=svg(b,d)

# 254 青春のリグレット: a faded ticket stub and an old scarf left on a bench by a lake at dusk, regret
d,b=bg([(0,'#7a6a9a'),(1,'#e8b8a0')])
b+='<rect y="420" width="800" height="200" fill="#6a7aa8"/><rect y="620" width="800" height="180" fill="#6a5a4a"/>'
b+='<rect x="220" y="560" width="360" height="24" fill="#5a3a2a"/><rect x="220" y="500" width="360" height="16" fill="#5a3a2a"/><rect x="240" y="584" width="16" height="80" fill="#3a2a1a"/><rect x="544" y="584" width="16" height="80" fill="#3a2a1a"/>'
b+='<path d="M300 556 Q360 540 420 560 L410 600 L380 640" stroke="#c8402a" stroke-width="18" fill="none"/><rect x="470" y="540" width="60" height="26" fill="#f4e8c8" transform="rotate(-10 500 553)"/>'
I[254]=svg(b,d)

# 887 涙の影: a man's long shadow on a wall with a teardrop silhouette, single streetlight, mid-90s
d,b=bg([(0,'#1a1a24'),(1,'#3a3a44')])
b+='<rect x="0" y="0" width="800" height="600" fill="#4a4a54"/>'+glow(120,80,120,'#ffd27a',.4)+'<polygon points="120,80 800,600 800,0" fill="#ffd27a" opacity=".08"/>'
b+='<g opacity=".7">'+figure(560,600,460,'#14141c')+'</g>'+'<path d="M570 230 Q556 260 570 276 Q584 260 570 230Z" fill="#cfe6ff"/><rect y="600" width="800" height="200" fill="#2a2a32"/>'+figure(260,680,180,'#000')
I[887]=svg(b,d)

# 1122 feel: a woman's silhouette with headphones, colored sound waves pouring from her, R&B vibe
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=''.join(f'<path d="M{100+k*30} 400 Q{150+k*30} {300-k*10} {200+k*30} 400 T{300+k*30} 400" stroke="{c}" stroke-width="5" fill="none" opacity=".6"/>' for k,c in enumerate(['#ff4aa8','#ffd02a','#3ad0ff','#ff4aa8']))
b+=profile(500,760,1.6,'#000')+'<path d="M380 360 Q480 220 600 330" stroke="#ff4aa8" stroke-width="16" fill="none"/><rect x="560" y="320" width="50" height="80" rx="20" fill="#ff4aa8"/>'
I[1122]=svg(b,d)

# 1171 WINDING ROAD: a small round cube-shaped car on a winding road through green hills, three friends' voices
d,b=bg([(0,'#7ad0ff'),(1,'#e8f8ff')])
b+=hills(380,40,'#7ac86a',1171,4)+hills(500,40,'#5ab85a',1172,5)+'<path d="M-20 800 Q300 700 200 600 Q120 520 400 480 Q640 440 560 380 Q500 340 640 300" stroke="#e8d8b8" stroke-width="44" fill="none"/>'
b+='<rect x="250" y="540" width="120" height="90" rx="26" fill="#f4f4f4"/><rect x="266" y="552" width="88" height="34" rx="10" fill="#a8d8f8"/><circle cx="280" cy="632" r="16" fill="#1a1a1a"/><circle cx="340" cy="632" r="16" fill="#1a1a1a"/>'+''.join(note(x,y,22,'#2a6ad8') for x,y in [(420,420),(470,380),(520,420)])
I[1171]=svg(b,d)

# 1284 A winter fairy is melting a snowman: a tiny glowing fairy touching a snowman whose edges melt into flowers
d,b=bg([(0,'#bfe0ff'),(1,'#f4faff')])
b+=snow(60,1284,.8)+'<rect y="620" width="800" height="180" fill="#fff"/><circle cx="400" cy="560" r="110" fill="#fff" stroke="#d8e8f8" stroke-width="4"/><circle cx="400" cy="400" r="74" fill="#fff" stroke="#d8e8f8" stroke-width="4"/>'
b+='<path d="M370 420 Q400 440 430 420" stroke="#5a5a6a" stroke-width="5" fill="none"/><circle cx="380" cy="390" r="6" fill="#3a3a4a"/><circle cx="420" cy="390" r="6" fill="#3a3a4a"/><path d="M400 400 L440 410 L400 414Z" fill="#ff8a2a"/>'
b+=''.join(flower(x,y,24,5,c,'#ffd02a') for x,y,c in [(310,600,'#ff8ab0'),(490,620,'#b08aff'),(300,520,'#8ad0ff')])+glow(560,300,40,'#fff4b0',.8)+sparkle(560,300,24,'#ffd02a')+'<path d="M545 290 Q520 260 540 250 Q556 270 560 300Z M575 290 Q600 260 580 250 Q564 270 560 300Z" fill="#fff" opacity=".8"/>'
I[1284]=svg(b,d)

# 1434 J.S.B. HAPPINESS: a row of dancers in sync under a stadium sky full of fireworks
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=firework(200,200,100,'#ffd02a',24,1)+firework(600,160,120,'#3ad0ff',26,2)+firework(400,260,70,'#ff4aa8',20,3)
b+='<rect y="620" width="800" height="180" fill="#14142a"/>'+''.join(figure(x,620,170,'#000',pose='up' if k%2 else 'wave') for k,x in enumerate(range(100,780,100)))
I[1434]=svg(b,d)

# 1649 わたしの一番かわいいところ: a pastel mirror with heart and ribbon decorations, glitter and a big bow
d,b=bg([(0,'#ffe8f4'),(1,'#e8d8ff')])
b+=''.join(sparkle(x,y,s,'#ffb0d8') for x,y,s in [(120,140,24),(680,120,30),(700,520,20),(100,560,26)])
b+='<ellipse cx="400" cy="380" rx="200" ry="240" fill="#ff8ac0"/><ellipse cx="400" cy="380" rx="170" ry="210" fill="#e8f4ff"/><ellipse cx="350" cy="300" rx="40" ry="70" fill="#fff" opacity=".6"/>'
b+='<path d="M400 140 Q330 90 300 110 Q320 150 400 150 Q480 150 500 110 Q470 90 400 140Z" fill="#ff5aa0"/><circle cx="400" cy="140" r="18" fill="#ff5aa0"/>'+heart(400,380,50,'#ff5aa0')
I[1649]=svg(b,d)

# 1688 遠くまで: a long straight desert highway to the horizon with a lone rocker walking, guitar case
d,b=bg([(0,'#ff8a4a'),(1,'#ffe0a0')])
b+='<circle cx="400" cy="400" r="70" fill="#fff4c8"/><rect y="420" width="800" height="380" fill="#c8905a"/><polygon points="400,420 300,800 500,800" fill="#4a4a4a"/>'+''.join(f'<rect x="398" y="{440+k*50}" width="4" height="{14+k*6}" fill="#ffd02a"/>' for k in range(7))
b+=figure(460,700,170,'#1a0a0a')+'<rect x="490" y="600" width="30" height="90" rx="10" fill="#1a0a0a" transform="rotate(10 505 645)"/>'
I[1688]=svg(b,d)

# 1717 Long Road: three boys walking on a long country road toward a rising sun, apple tree beside
d,b=bg([(0,'#ffb07a'),(1,'#fff0c8')])
b+='<circle cx="400" cy="440" r="90" fill="#fff6d0"/><rect y="460" width="800" height="340" fill="#7ab85a"/><polygon points="400,460 260,800 540,800" fill="#d8c8a8"/>'
b+=tree(660,560,240,'#3a8a3a',1717)+''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="#e8102a"/>' for x,y in [(620,400),(680,380),(700,440),(640,460)])+''.join(figure(x,y,h,'#2a1a1a') for x,y,h in [(370,640,140),(420,650,150),(460,640,140)])
I[1717]=svg(b,d)

# 89 わたしの城下町: a castle tower above an old town lane with lattice houses, a shy girl walking, early-70s
d,b=bg([(0,'#f8d8b0'),(1,'#f0e8d8')])
b+='<g fill="#f4f0e8"><rect x="500" y="200" width="160" height="80"/><rect x="520" y="140" width="120" height="70"/></g><g fill="#3a3a4a"><path d="M480 210 L580 160 L680 210Z"/><path d="M500 150 L580 100 L660 150Z"/></g><path d="M470 280 L690 280 L720 340 L440 340Z" fill="#8a8a8a"/>'
b+='<rect x="0" y="400" width="320" height="300" fill="#5a3a2a"/>'+''.join(f'<rect x="{x}" y="440" width="6" height="200" fill="#3a2414"/>' for x in range(20,320,24))+'<path d="M-10 400 L330 360 L340 420Z" fill="#3a3a44"/><rect y="700" width="800" height="100" fill="#a89878"/>'
b+=figure(520,720,240,'#5a2a3a',hair='#1a1a1a')
I[89]=svg(b,d)

# 255 Blizzard: two skiers lost in a white blizzard on a mountain, one reaching for the other
d,b=bg([(0,'#9ab0c8'),(1,'#e8eef4')])
b+='<path d="M0 500 L400 320 L800 520 L800 800 L0 800Z" fill="#f4f8ff"/>'+snow(220,255,.95)+rain(60,255,'#fff',.6,40)
b+=figure(320,620,200,'#e8402a',pose='reach')+figure(540,600,180,'#2a6ae8',pose='reachL')+'<path d="M260 640 L380 620 M480 620 L600 600" stroke="#3a3a3a" stroke-width="6"/>'
I[255]=svg(b,d)

# 602 にちようび: a lazy Sunday — a cat sleeping on a sunny windowsill next to a coffee cup, cheerful pop
d,b=bg([(0,'#ffe8a0'),(1,'#fff8e0')])
b+='<rect x="140" y="80" width="520" height="420" fill="#a8e0ff"/>'+cloud(400,200,1.2)+'<rect x="140" y="80" width="520" height="420" fill="none" stroke="#ff8a4a" stroke-width="20"/><path d="M400 80 L400 500" stroke="#ff8a4a" stroke-width="12"/><rect x="100" y="500" width="600" height="40" fill="#e8c890"/>'
b+='<ellipse cx="300" cy="480" rx="90" ry="40" fill="#3a3a3a"/><circle cx="220" cy="460" r="34" fill="#3a3a3a"/><polygon points="200,436 206,410 220,430" fill="#3a3a3a"/><polygon points="230,430 244,408 246,436" fill="#3a3a3a"/>'
b+='<path d="M500 440 L560 440 L554 500 L506 500Z" fill="#fff"/><path d="M560 455 Q580 455 578 475 Q576 490 558 490" stroke="#fff" stroke-width="6" fill="none"/>'
I[602]=svg(b,d)

# 1764 時の河を越えて: a paper boat sailing across a river of clock faces and gears, pastel 80s idol
d,b=bg([(0,'#d8c8f8'),(1,'#a8d8f8')])
b+='<rect y="420" width="800" height="380" fill="#6a9ad8"/>'+''.join(ring(x,y,r,'#fff',5,.5)+f'<path d="M{x} {y} L{x} {y-r*.7} M{x} {y} L{x+r*.5} {y}" stroke="#fff" stroke-width="4" opacity=".5"/>' for x,y,r in [(140,560,60),(400,680,70),(640,540,50),(260,740,40),(580,740,46)])
b+='<path d="M300 440 L500 440 L460 490 L340 490Z" fill="#fff"/><path d="M400 330 L400 440 L470 440Z" fill="#ffe0f0"/>'+sparkle(600,180,26,'#fff')+sparkle(200,160,18,'#fff')
I[1764]=svg(b,d)

# 213 さよなら: a wintry street with a woman walking away in the snow, a man's silhouette left behind, late-70s
d,b=bg([(0,'#5a6a8a'),(1,'#b8c4d8')])
b+=snow(90,213)+'<rect y="580" width="800" height="220" fill="#e8eef8"/><polygon points="400,580 300,800 500,800" fill="#c8d0dc"/>'
b+=figure(200,720,280,'#14141e')+figure(470,600,100,'#14141e',hair='#14141e')+''.join(f'<ellipse cx="{430+k*12}" cy="{720-k*24}" rx="8" ry="4" fill="#9aa8c0"/>' for k in range(5))
I[213]=svg(b,d)

# 292 涙のキッス: a couple's kiss reflected in a rainy taxi window, a tear running down the glass
d,b=bg([(0,'#1a2a3a'),(1,'#3a4a5a')])
b+='<rect x="80" y="120" width="640" height="440" rx="40" fill="#2a3a4a"/>'+rain(70,292,'#cfe6ff',.4,0,560)+''.join(glow(x,y,30,c,.5) for x,y,c in [(200,460,'#ff4a4a'),(600,420,'#ffd27a'),(400,500,'#3ad0ff')])
b+=profile(330,560,1.1,'#000')+profile(470,560,1.05,'#000',True)+'<path d="M560 200 Q550 300 560 380" stroke="#cfe6ff" stroke-width="6" fill="none"/><circle cx="560" cy="384" r="9" fill="#cfe6ff"/><rect x="80" y="120" width="640" height="440" rx="40" fill="none" stroke="#0a0a10" stroke-width="30"/>'
I[292]=svg(b,d)

# 684 がじゃいも: a small funny potato with a big grin-shaped crack, variety-show stage lights
d,b=bg([(0,'#ffcf3a'),(1,'#ff8a2a')])
b+=rays(400,420,24,'#fff',.2,7)+'<ellipse cx="400" cy="440" rx="180" ry="140" fill="#c89a5a" transform="rotate(-10 400 440)"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#8a6a3a"/>' for x,y in [(320,380),(480,400),(360,520),(470,500),(300,460)])
b+='<path d="M330 470 Q400 530 480 460" stroke="#5a3a1a" stroke-width="10" fill="none" stroke-linecap="round"/>'+''.join(f'<rect x="{x}" y="660" width="60" height="140" fill="#e8102a"/>' for x in (0,740))
I[684]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
