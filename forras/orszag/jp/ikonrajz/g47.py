import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 47. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1542 ライナウ: a young man with an acoustic guitar on a riverside bench in warm morning light, 2020 folk-pop
d,b=bg([(0,'#ffd8a0'),(1,'#fff4e0')])
b+='<circle cx="620" cy="200" r="70" fill="#fff8d0"/>'+rays(620,200,16,'#fff',.3,10)+'<rect y="480" width="800" height="120" fill="#8ab0d8"/><rect y="600" width="800" height="200" fill="#8ab86a"/>'
b+='<rect x="200" y="580" width="280" height="14" fill="#5a3a2a"/><rect x="210" y="594" width="10" height="50" fill="#5a3a2a"/><rect x="460" y="594" width="10" height="50" fill="#5a3a2a"/>'+figure(320,600,220,'#2a2a34')+guitar(340,540,.55,40,'#c8702a')
I[1542]=svg(b,d)

# 1770 White Silent Night: a single candle-lit window in a silent snowy church at night, 1997 visual-kei ballad
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+=snow(100,1770)+'<rect x="260" y="300" width="280" height="340" fill="#e8eef8"/><path d="M240 310 L400 180 L560 310Z" fill="#c8d0e0"/><rect x="380" y="100" width="40" height="90" fill="#e8eef8"/><path d="M400 70 L400 110 M386 86 L414 86" stroke="#c8d0e0" stroke-width="5"/>'
b+='<path d="M360 640 L360 480 Q400 420 440 480 L440 640Z" fill="#ffd27a"/>'+glow(400,540,120,'#ffd27a',.5)+'<rect y="640" width="800" height="160" fill="#f4f6ff"/>'
I[1770]=svg(b,d)

# 428 リ・ボ・ン: a giant pink satin ribbon bow tied around a gift-wrapped heart, 80s idol
d,b=bg([(0,'#ffe0ec'),(1,'#f0e0ff')])
b+=heart(400,460,140,'#ff9ac0')+'<rect x="380" y="320" width="40" height="320" fill="#e8508a"/>'
b+='<path d="M400 320 Q300 200 240 260 Q220 340 400 330 Q580 340 560 260 Q500 200 400 320Z" fill="#e8508a"/><circle cx="400" cy="320" r="26" fill="#c8306a"/><path d="M390 340 L330 440 M410 340 L470 440" stroke="#e8508a" stroke-width="22" stroke-linecap="round"/>'
I[428]=svg(b,d)

# 1765 Mr.サマータイム: a summer straw hat and sunglasses left on a deck chair facing a sparkling sea, 1978
d,b=bg([(0,'#1ab0ff'),(1,'#d8f4ff')])
b+='<rect y="420" width="800" height="200" fill="#1a7ad8"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(200,480,18),(420,520,14),(620,460,20)])+'<rect y="620" width="800" height="180" fill="#f4dca0"/>'
b+='<path d="M260 720 L320 560 L520 560 L560 720" stroke="#8a5a2a" stroke-width="10" fill="none"/><path d="M320 560 L520 560 L500 640 L300 640Z" fill="#3ab0ff"/>'+''.join(f'<rect x="{x}" y="560" width="20" height="80" fill="#fff"/>' for x in (340,400,460))
b+='<ellipse cx="420" cy="540" rx="80" ry="16" fill="#e8c870"/><path d="M370 540 Q420 490 470 540Z" fill="#e8c870"/><rect x="372" y="526" width="96" height="10" fill="#e8302a"/>'
I[1765]=svg(b,d)

# 50 寒い朝: frost-covered fields at sunrise with a schoolgirl's silhouette in a scarf, breath visible, 1962
d,b=bg([(0,'#c8d8f0'),(1,'#ffe8d0')])
b+='<circle cx="560" cy="460" r="70" fill="#fff4d8"/><rect y="480" width="800" height="320" fill="#e8eef4"/>'+''.join(f'<path d="M{x} 800 L{x+6} {560+(x%5)*10}" stroke="#c8d0d8" stroke-width="4"/>' for x in range(10,800,22))
b+=figure(320,660,240,'#2a2a3a',hair='#2a2a3a')+'<path d="M300 470 Q320 460 360 470 L370 520" stroke="#c8302a" stroke-width="14" fill="none"/>'+''.join(f'<circle cx="{360+k*24}" cy="{440-k*10}" r="{10+k*4}" fill="#fff" opacity="{.6-k*.15}"/>' for k in range(3))
I[50]=svg(b,d)

# 569 フィルムの向こう側: a strip of film frames curling across the sky with a girl's silhouette in the last frame, 1989
d,b=bg([(0,'#3a3a6a'),(1,'#ffb8a0')])
b+='<path d="M-40 520 Q200 300 400 400 T840 240" stroke="#1a1a1a" stroke-width="120" fill="none"/>'+''.join(f'<rect x="{x-40}" y="{y-36}" width="80" height="72" fill="#ffe8c8" transform="rotate({r} {x} {y})"/>' for x,y,r in [(80,460,-30),(220,370,-15),(400,400,10),(560,350,-20),(720,270,-20)])
b+=figure(720,290,60,'#3a2a3a',hair='#3a2a3a')
I[569]=svg(b,d)

# 1758 風のInvitation: an invitation card carried off by the wind through a field of flowers, 80s idol
d,b=bg([(0,'#8ad8ff'),(1,'#fff8e8')])
b+=''.join(f'<path d="M-20 {y} Q200 {y-60} 400 {y} T820 {y}" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>' for y in (240,360))+'<rect y="580" width="800" height="220" fill="#9ad06a"/>'+''.join(flower(x,y,14,5,c,'#ffd02a',x) for x,y,c in [(100,640,'#ff8ab0'),(240,700,'#fff'),(400,620,'#ffd02a'),(560,700,'#ff8ab0'),(700,640,'#fff')])
b+='<g transform="rotate(-18 460 320)"><rect x="380" y="270" width="160" height="110" fill="#fff" stroke="#e8c8d8" stroke-width="4"/><path d="M380 270 L460 330 L540 270" stroke="#e8c8d8" stroke-width="4" fill="none"/></g>'+heart(470,340,16,'#ff6aa0')
I[1758]=svg(b,d)

# 154 ウイスキーが、お好きでしょ: a whisky glass with a single large ice ball under a soft bar lamp, 1990 ballad
d,b=bg([(0,'#1a1410'),(1,'#3a2a1a')])
b+=glow(400,240,240,'#ffb070',.35)+'<rect y="580" width="800" height="220" fill="#4a2a14"/><rect y="560" width="800" height="24" fill="#6a3a1a"/>'
b+='<path d="M290 360 L510 360 L490 560 L310 560Z" fill="#f4ece0" opacity=".4"/><path d="M300 440 L500 440 L490 560 L310 560Z" fill="#c8802a" opacity=".85"/><circle cx="400" cy="460" r="60" fill="#e8f4ff" opacity=".7"/>'
I[154]=svg(b,d)

# 262 親父の一番長い日: a father's silhouette walking his daughter in a wedding veil down a sunlit aisle, 1979
d,b=bg([(0,'#fff4e0'),(1,'#f0e0c8')])
b+=rays(400,0,12,'#fff',.4,30,40,140)+'<path d="M340 800 L380 300 L420 300 L460 800Z" fill="#c8302a" opacity=".7"/>'
b+=figure(340,640,300,'#1a1a24')+figure(460,640,280,'#f4f4f8',hair='#f4f4f8')+'<path d="M440 360 Q520 460 540 640 L470 640Z" fill="#fff" opacity=".7"/>'
I[262]=svg(b,d)

# 1280 奇跡の人: a person's silhouette lifting a single glowing light up in a dark stadium, 2017 ballad
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=starsf(50,1280,500)+'<path d="M0 600 Q400 500 800 600 L800 800 L0 800Z" fill="#0a0a14"/>'+figure(400,620,280,'#000',pose='up')+'<circle cx="400" cy="300" r="30" fill="#fff4c8"/>'+glow(400,300,160,'#fff4c8',.7)
I[1280]=svg(b,d)

# 1704 約束: two pinky fingers linked over an old school desk, a spring promise, 1986 idol
d,b=bg([(0,'#ffe8d8'),(1,'#f8f0e8')])
b+='<rect x="0" y="480" width="800" height="320" fill="#c89a6a"/>'+''.join(f'<path d="M{x} 520 Q{x+40} 540 {x+80} 520" stroke="#a87a4a" stroke-width="3" fill="none"/>' for x in range(40,760,100))
b+='<path d="M0 420 Q160 380 300 380 L340 400 Q200 440 0 500Z" fill="#f4c8a8"/><path d="M800 420 Q640 380 500 380 L460 400 Q600 440 800 500Z" fill="#e8b494"/>'
b+='<path d="M330 390 Q380 330 420 360 Q440 380 400 400 Q370 410 380 380 Q420 330 470 390" stroke="#f0bc98" stroke-width="22" fill="none" stroke-linecap="round"/>'+heart(400,260,26,'#ff6aa0')
I[1704]=svg(b,d)

# 81 さよならの夏: an empty beach at the end of summer with a deflated float and seagulls, 1976 ballad
d,b=bg([(0,'#c8a8c8'),(1,'#ffd8b0')])
b+='<circle cx="400" cy="420" r="70" fill="#fff0c8"/><rect y="440" width="800" height="140" fill="#7a8ac8"/><path d="M0 580 Q400 540 800 580 L800 800 L0 800Z" fill="#e8d0a8"/>'
b+='<ellipse cx="520" cy="660" rx="90" ry="30" fill="#ff8a8a"/><ellipse cx="520" cy="660" rx="44" ry="14" fill="#e8d0a8"/>'+bird(240,240,30,'#3a3a4a')+bird(300,200,24,'#3a3a4a')+''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="#c8b088"/>' for x,y in [(200,720),(240,700),(280,680)])
I[81]=svg(b,d)

# 110 ヤマトより愛をこめて: a lone figure on a cliff watching a distant ship's light vanish among the stars, 1978 ballad
d,b=bg([(0,'#02040e'),(1,'#141a3a')])
b+=starsf(120,110,800)+'<path d="M560 260 L640 250 L660 230 L670 240 L660 256 L700 262 L700 266 L660 268 L650 280 L640 280 L644 268Z" fill="#8a90a8"/>'+'<path d="M560 262 L380 300" stroke="#8ab0ff" stroke-width="3" opacity=".5"/>'+glow(560,262,30,'#8ab0ff',.6)
b+='<path d="M0 560 L340 520 L340 800 L0 800Z" fill="#05050a"/>'+figure(220,540,200,'#000')
I[110]=svg(b,d)

# 1805 Snow halation: snow falling in a bell-like halo of light that shifts from white to warm orange, idol anime song
d,b=bg([(0,'#0a1a3a'),(1,'#3a4a7a')])
b+=glow(400,420,320,'#ff9a3a',.45)+glow(400,420,200,'#fff',.4)+snow(120,1805)+'<path d="M300 520 Q300 360 400 340 Q500 360 500 520 L520 560 L280 560Z" fill="#fff4e0" opacity=".85"/><circle cx="400" cy="580" r="20" fill="#fff4e0"/>'
b+='<rect y="660" width="800" height="140" fill="#e8eef8"/>'
I[1805]=svg(b,d)

# 471 悲しいね: a girl's silhouette sitting on a swing at twilight with a single tear-shaped streetlight, 80s pop-rock
d,b=bg([(0,'#3a3a6a'),(1,'#c88aa8')])
b+='<rect y="640" width="800" height="160" fill="#3a3044"/><path d="M220 640 L300 300 L380 640 M300 300 L580 300 M520 300 L600 640" stroke="#1a1424" stroke-width="10" fill="none"/>'
b+='<path d="M380 300 L380 520 M460 300 L460 520" stroke="#1a1424" stroke-width="3"/><rect x="370" y="520" width="100" height="12" fill="#1a1424"/>'+figure(420,640,170,'#1a1424',hair='#1a1424')
b+='<rect x="660" y="300" width="8" height="340" fill="#2a2030"/><path d="M664 280 Q680 300 664 318 Q648 300 664 280Z" fill="#cfe6ff"/>'+glow(664,300,50,'#cfe6ff',.5)
I[471]=svg(b,d)

# 585 Start: a runner's silhouette on starting blocks at a sunlit track, 1991 punk-pop
d,b=bg([(0,'#3ab0ff'),(1,'#fff0d0')])
b+='<rect y="520" width="800" height="280" fill="#d86a4a"/>'+''.join(f'<path d="M0 {y} L800 {y-60}" stroke="#fff" stroke-width="5"/>' for y in (600,680,760))
b+='<g transform="rotate(25 400 560)">'+figure(400,700,300,'#1a1a2a',pose='up')+'</g>'+''.join(f'<path d="M{x} {y} L{x-140} {y}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>' for x,y in [(260,420),(240,480),(270,540)])
I[585]=svg(b,d)

# 1686 L.O.V.E.: four glowing neon heart frames spelling love in pulsing colours on a dark stage
d,b=bg([(0,'#0a0a1a'),(1,'#2a0a2a')])
b+=''.join(heart(x,y,56,'none',f' stroke="{c}" stroke-width="10"')+glow(x,y,70,c,.35) for x,y,c in [(180,320,'#ff4a8a'),(330,480,'#ffd02a'),(470,320,'#3affe8'),(620,480,'#a85aff')])
I[1686]=svg(b,d)

# 1748 春はどこから来るのか?: a snowy field with the first green shoots and a girl looking for spring, Niigata idol
d,b=bg([(0,'#c8e0f8'),(1,'#f4f4f0')])
b+='<rect y="520" width="800" height="280" fill="#f4f6ff"/>'+''.join(f'<path d="M{x} 560 q-14 -30 0 -50 q14 20 0 50Z" fill="#5ac84a"/>' for x in (140,240,520,640,700))+'<path d="M300 560 L320 520 L340 560Z" fill="#5ac84a"/>'
b+=figure(420,560,240,'#3a3a5a',hair='#3a3a5a')+'<path d="M450 410 L500 360" stroke="#3a3a5a" stroke-width="10" stroke-linecap="round"/>'+flower(560,320,24,5,'#ffc0d8','#ffd02a')
I[1748]=svg(b,d)

# 70 砂漠のような東京で: a woman's silhouette in a desert of sand dunes with Tokyo skyscrapers on the horizon, 1971
d,b=bg([(0,'#e8a06a'),(1,'#f8e0b0')])
b+=skyline(440,'#a87a5a',70,40,160)+'<path d="M0 480 Q200 420 400 480 T800 460 L800 800 L0 800Z" fill="#e8c088"/><path d="M0 620 Q300 560 520 620 T800 600 L800 800 L0 800Z" fill="#d8a870"/>'
b+=figure(320,640,240,'#3a2a1a',hair='#3a2a1a')+'<circle cx="620" cy="160" r="60" fill="#fff4d0"/>'
I[70]=svg(b,d)

# 472 夏が来た!: a girl jumping off a pier into a sparkling summer sea with a big sun, 80s pop-rock
d,b=bg([(0,'#1ab0ff'),(1,'#d8f8ff')])
b+='<circle cx="640" cy="140" r="70" fill="#fff4a0"/><rect y="460" width="800" height="340" fill="#1a8ad8"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(200,520,16),(500,580,20),(640,520,14)])
b+='<rect x="0" y="480" width="300" height="24" fill="#8a5a3a"/>'+''.join(f'<rect x="{x}" y="504" width="14" height="200" fill="#6a4a2a"/>' for x in (40,160,270))+'<g transform="rotate(-20 420 340)">'+figure(420,460,220,'#1a1a2a',pose='up',hair='#1a1a2a')+'</g>'
I[472]=svg(b,d)

# 16 君といつまでも: a young couple on a beach watching the sunset with a ukulele, 1965
d,b=bg([(0,'#ff8a5a'),(1,'#ffd8a0')])
b+='<circle cx="400" cy="440" r="90" fill="#fff0b0"/><rect y="480" width="800" height="120" fill="#e8805a"/><rect y="600" width="800" height="200" fill="#f0c890"/>'
b+=figure(360,690,220,'#2a1a1a')+figure(440,690,200,'#2a1a1a',hair='#2a1a1a')+guitar(330,580,.35,30,'#2a1a1a')
I[16]=svg(b,d)

# 33 古城: the ruins of an old castle stone wall overgrown with grass under a lonely moon, 1959
d,b=bg([(0,'#1a2440'),(1,'#5a6a8a')])
b+=moon(560,160,60)+'<path d="M80 800 L120 460 L680 460 L720 800Z" fill="#4a4a54"/>'+''.join(f'<path d="M{x} {y} L{x+60} {y}" stroke="#3a3a44" stroke-width="3"/>' for x in range(120,680,60) for y in range(500,800,40))
b+='<rect x="300" y="300" width="200" height="160" fill="#2a2a34"/><path d="M270 310 L400 230 L530 310Z" fill="#1a1a24"/>'+''.join(f'<path d="M{x} 460 q10 -30 20 0" stroke="#5a7a4a" stroke-width="4" fill="none"/>' for x in range(130,680,30))
I[33]=svg(b,d)

# 56 青い鳥: a single bluebird perched in an open birdcage on a sunny windowsill, 1968 group sounds
d,b=bg([(0,'#cfe8ff'),(1,'#fff8e8')])
b+='<rect y="560" width="800" height="240" fill="#a8988a"/><path d="M280 560 L280 360 Q280 240 400 220 Q520 240 520 360 L520 560Z" fill="none" stroke="#c8a24a" stroke-width="6"/>'+''.join(f'<path d="M{x} 560 L{x} {300+abs(400-x)*.5}" stroke="#c8a24a" stroke-width="3"/>' for x in range(310,500,30))
b+='<path d="M520 400 L620 380 L620 520 L520 520Z" fill="#fff" opacity=".3"/>'+'<ellipse cx="400" cy="460" rx="50" ry="36" fill="#2a7ae8"/><circle cx="440" cy="430" r="26" fill="#2a7ae8"/><path d="M462 430 L486 436 L462 442Z" fill="#ffd02a"/><circle cx="446" cy="424" r="5" fill="#111"/><path d="M350 460 L310 480 L350 480Z" fill="#1a5ab8"/>'
I[56]=svg(b,d)

# 111 コバルトの季節の中で: a cobalt-blue sky over a quiet seaside road with a lone figure in autumn, 1976
d,b=bg([(0,'#1a3aa8'),(1,'#8ab0e8')])
b+='<rect y="480" width="800" height="120" fill="#1a4ab8"/><path d="M0 600 L800 560 L800 800 L0 800Z" fill="#c8b8a0"/>'+tree(640,620,300,'#c8602a',111)+figure(320,680,220,'#1a1a2a')
I[111]=svg(b,d)

# 513 SEVEN YEARS AFTER: two adults' silhouettes meeting again at the same old school gate, 1991 girl band
d,b=bg([(0,'#ffb88a'),(1,'#ffe8d0')])
b+='<rect x="100" y="300" width="60" height="320" fill="#8a7a7a"/><rect x="640" y="300" width="60" height="320" fill="#8a7a7a"/>'+''.join(f'<rect x="{x}" y="400" width="8" height="220" fill="#5a5a5a"/>' for x in range(160,240,20))+'<rect y="620" width="800" height="180" fill="#b8a090"/>'
b+=figure(340,640,260,'#2a1a2a',hair='#2a1a2a')+figure(460,640,260,'#2a1a2a',hair='#2a1a2a')+'<path d="M370 430 L430 430" stroke="#2a1a2a" stroke-width="12" stroke-linecap="round"/>'
I[513]=svg(b,d)

# 723 Alone: a single lit window in a dark apartment block and a figure hugging their knees, 1996 ballad
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<rect x="0" y="0" width="800" height="800" fill="#14141e"/><rect x="260" y="160" width="280" height="300" fill="#2a3a6a"/>'+moon(420,260,40)+'<rect x="260" y="160" width="280" height="300" fill="none" stroke="#2a2a3a" stroke-width="14"/>'
b+='<rect y="560" width="800" height="240" fill="#1a1a24"/><ellipse cx="400" cy="560" rx="70" ry="80" fill="#000"/><circle cx="400" cy="460" r="36" fill="#000"/>'
I[723]=svg(b,d)

# 119 ハートのエースが出てこない: a fan of playing cards with the ace of hearts missing from the gap, 1975 idol trio
d,b=bg([(0,'#1a5a3a'),(1,'#2a7a4a')])
for k,a in enumerate((-40,-20,0,20,40)):
  b+=f'<g transform="rotate({a} 400 640)"><rect x="340" y="260" width="120" height="180" rx="10" fill="{"#2a7a4a" if k==2 else "#fff"}" stroke="{"#fff" if k==2 else "#ccc"}" stroke-width="4" {"stroke-dasharray=\"10 8\"" if k==2 else ""}/></g>'
b+=''.join(f'<g transform="rotate({a} 400 640)"><text x="400" y="370" text-anchor="middle" font-family="Noto Sans JP" font-size="60" fill="{c}">{t}</text></g>' for a,t,c in [(-40,'♠','#1a1a1a'),(-20,'♣','#1a1a1a'),(20,'♦','#e8102a'),(40,'♠','#1a1a1a')])
b+=heart(560,180,30,'#e8102a',' opacity=".7"')+sparkle(600,140,16,'#fff')
I[119]=svg(b,d)

# 120 あなたに夢中: a girl daydreaming with hearts floating around her head on a pastel cloud, 1973 idol trio
d,b=bg([(0,'#ffd8ec'),(1,'#e8e0ff')])
b+=cloud(400,560,3.0,'#fff')+profile(380,620,1.0,'#5a2a4a')+''.join(heart(x,y,s,c) for x,y,s,c in [(500,240,30,'#ff6aa0'),(560,320,22,'#ff9ac0'),(440,180,18,'#ff9ac0'),(600,220,16,'#ff6aa0')])
I[120]=svg(b,d)

# 17 お嫁においで: a young man in a boat on a calm bay at sunset holding out a ukulele, 1966
d,b=bg([(0,'#ff8a6a'),(1,'#ffe0b0')])
b+='<circle cx="560" cy="420" r="80" fill="#fff0b0"/><rect y="460" width="800" height="340" fill="#4a7ac8"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(100,520),(500,560),(260,680)])
b+='<path d="M200 580 L500 580 L460 630 L240 630Z" fill="#8a4a2a"/>'+figure(340,590,180,'#1a1a24')+guitar(370,520,.35,30,'#c8702a')+heart(600,320,26,'#ff6a8a')
I[17]=svg(b,d)

# 101 愛傷歌: a wounded heart wrapped with a bandage under a single spotlight, 1985 enka
d,b=bg([(0,'#1a0a14'),(1,'#3a0a1a')])
b+='<path d="M360 0 L440 0 L560 640 L240 640Z" fill="#fff" opacity=".1"/>'+heart(400,440,120,'#c8102a')+'<rect x="300" y="400" width="200" height="36" fill="#f4ece0" transform="rotate(-24 400 418)"/><path d="M400 340 L380 420 L420 460 L390 540" stroke="#3a0a14" stroke-width="8" fill="none"/>'
I[101]=svg(b,d)

# 1768 あんたのバラード: a rock singer gripping a mic stand with a scarf, a single hard spotlight, 1977
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a0a')])
b+='<path d="M340 0 L460 0 L620 700 L180 700Z" fill="#ffd8a8" opacity=".18"/><rect y="700" width="800" height="100" fill="#14100e"/>'+figure(400,700,400,'#000',hair='#000')
b+='<rect x="440" y="300" width="8" height="400" fill="#c8c8d0" transform="rotate(-10 444 500)"/><path d="M380 340 Q340 400 320 520" stroke="#e8302a" stroke-width="14" fill="none"/>'
I[1768]=svg(b,d)

# 1671 ひとつだけ: a single small gift box glowing on an outstretched palm, 1980 piano pop
d,b=bg([(0,'#fff0e0'),(1,'#f0e0d0')])
b+=glow(400,380,200,'#fff4c8',.6)+'<rect x="350" y="320" width="100" height="90" fill="#e8302a"/><rect x="392" y="320" width="16" height="90" fill="#ffd02a"/><path d="M400 320 Q370 290 380 280 Q400 290 400 320 Q430 290 420 280 Q400 290 400 320" stroke="#ffd02a" stroke-width="6" fill="none"/>'
b+='<path d="M200 800 L260 480 Q280 420 340 420 L500 420 Q540 430 520 460 L420 470 L560 480 Q600 500 560 520 L380 540 L340 800Z" fill="#f4c8a8"/>'
I[1671]=svg(b,d)

# 60 神様お願い: a long-haired 60s rocker kneeling with hands clasped under a beam of light from heaven
d,b=bg([(0,'#1a1a3a'),(1,'#4a3a6a')])
b+='<path d="M360 0 L440 0 L560 680 L240 680Z" fill="#fff4c8" opacity=".25"/>'+starsf(40,60,400)+'<rect y="680" width="800" height="120" fill="#14101a"/>'
b+=figure(400,700,240,'#000',hair='#000')+'<path d="M380 470 L400 440 L420 470" stroke="#000" stroke-width="14" fill="none"/>'+guitar(520,640,.5,-60,'#000')
I[60]=svg(b,d)

# 97 お嫁サンバ: a wedding bouquet bursting with samba feathers and confetti on a sunny carnival day, 1981
d,b=bg([(0,'#ffd04a'),(1,'#ff8a8a')])
b+=confetti(80,97,['#fff','#3ab0ff','#5ad87a','#e8302a'])+''.join(f'<path d="M400 520 Q{400+260*math.cos(a)} {520-260*math.sin(a)} {400+300*math.cos(a)} {520-300*math.sin(a)}" stroke="{c}" stroke-width="24" fill="none" stroke-linecap="round"/>' for a,c in [(math.radians(t),cl) for t,cl in [(40,'#e8302a'),(65,'#ffd02a'),(90,'#3ab0ff'),(115,'#5ad87a'),(140,'#ff6aa0')]])
b+='<path d="M360 560 L440 560 L410 720 L390 720Z" fill="#fff"/>'+''.join(flower(x,y,30,6,'#fff','#ffd02a') for x,y in [(370,520),(430,520),(400,490)])
I[97]=svg(b,d)

# 1824 ゆうこ: a girl's name written in the fogged window of a train at night, a lone traveller, 1982 folk
d,b=bg([(0,'#1a2030'),(1,'#3a4050')])
b+='<rect x="120" y="140" width="560" height="380" rx="30" fill="#5a6a8a"/>'+''.join(f'<circle cx="{random.Random(1824*k).randint(140,660)}" cy="{random.Random(1824*k+1).randint(160,500)}" r="{random.Random(1824*k+2).randint(4,16)}" fill="#ffd27a" opacity=".4"/>' for k in range(20))
b+=heart(400,330,60,'none',' stroke="#e8eef8" stroke-width="8" opacity=".8"')+'<rect x="120" y="140" width="560" height="380" rx="30" fill="none" stroke="#2a2a34" stroke-width="20"/><rect y="520" width="800" height="280" fill="#2a2a34"/>'+profile(620,760,.8,'#0a0a10',True)
I[1824]=svg(b,d)

# 1893 春夏秋冬: one tree shown in four quadrants through the seasons: blossom, green, red, snow, 1972 folk
d,b=bg([(0,'#f4f0e8'),(1,'#e8e4dc')])
for (qx,qy),bgc,lc in [((0,0),'#ffe8f0','#ffb0c8'),((400,0),'#d8f4ff','#3a9a4a'),((0,400),'#ffe8c8','#e8602a'),((400,400),'#e0e8f4','#f4f6ff')]:
  b+=f'<rect x="{qx}" y="{qy}" width="400" height="400" fill="{bgc}"/><rect x="{qx+190}" y="{qy+220}" width="20" height="140" fill="#5a3a2a"/><circle cx="{qx+200}" cy="{qy+190}" r="100" fill="{lc}"/>'
b+='<path d="M400 0 L400 800 M0 400 L800 400" stroke="#fff" stroke-width="12"/>'
I[1893]=svg(b,d)

# 25 銀色の道: a long silver road shining under moonlight across dark hills toward the horizon, 1966
d,b=bg([(0,'#0a1028'),(1,'#2a3458')])
b+=starsf(60,25,400)+moon(400,180,50)+hills(440,60,'#141a2a',25,4)+'<rect y="460" width="800" height="340" fill="#1a1e30"/><path d="M390 440 Q380 600 240 800 L560 800 Q420 600 410 440Z" fill="#c8d0e8"/>'+glow(400,600,200,'#c8d0e8',.25)
I[25]=svg(b,d)

# 34 おんな船頭唄: a woman poling a small flat boat along a misty river with reeds at dusk, 1955
d,b=bg([(0,'#5a5a7a'),(1,'#d8b8a8')])
b+='<rect y="440" width="800" height="360" fill="#6a7a9a"/>'+''.join(f'<path d="M{x} 460 L{x+4} {360+(x%5)*12}" stroke="#4a5a3a" stroke-width="4"/>' for x in list(range(0,180,14))+list(range(640,800,14)))+''.join(f'<ellipse cx="{x}" cy="{y}" rx="260" ry="30" fill="#fff" opacity=".15"/>' for x,y in [(300,440),(500,500)])
b+='<path d="M220 560 L560 560 L520 590 L260 590Z" fill="#3a2a1a"/>'+figure(400,560,200,'#1a1414',hair='#1a1414')+'<path d="M440 400 L520 700" stroke="#3a2a1a" stroke-width="6"/>'
I[34]=svg(b,d)

# 928 僕と僕らのあした: a group of silhouettes walking toward a sunrise on a road, the first with a flag, 2007
d,b=bg([(0,'#3a5ac8'),(1,'#ffc08a')])
b+='<circle cx="400" cy="480" r="90" fill="#fff0b0"/>'+rays(400,480,18,'#fff',.18,10)+'<rect y="500" width="800" height="300" fill="#4a4a5a"/><path d="M390 500 L180 800 L620 800 L410 500Z" fill="#6a6a7a"/>'
b+=''.join(figure(x,y,s,'#0a0a14') for x,y,s in [(320,740,200),(380,720,190),(440,730,200),(500,750,210)])+'<path d="M520 520 L520 400 L580 420 L520 440" stroke="#0a0a14" stroke-width="5" fill="#ffd02a"/>'
I[928]=svg(b,d)

# 18 海 その愛: a wide ocean with a single surfboard on a quiet beach and the sun breaking through clouds, 1976
d,b=bg([(0,'#3a8ae8'),(1,'#e0f4ff')])
b+=cloud(400,220,1.8,'#e8f0f8')+rays(400,240,18,'#fff',.25,10)+'<rect y="420" width="800" height="240" fill="#1a6ac8"/>'+''.join(f'<path d="M{x} {y} q40 -14 80 0" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>' for x,y in [(80,480),(400,520),(600,470),(220,600)])
b+='<path d="M0 660 Q400 620 800 660 L800 800 L0 800Z" fill="#f0d8a0"/><path d="M500 760 L540 560 Q550 520 560 560 L580 760Z" fill="#fff" stroke="#3ab0ff" stroke-width="6"/>'
I[18]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
