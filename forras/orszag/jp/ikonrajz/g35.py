import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 35. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 849 Blue Jean: a pair of faded blue jeans hanging on a line against a wide 2000s rock sky
d,b=bg([(0,'#2a5aa0'),(1,'#a8d0f0')])
b+=cloud(180,160,1.1)+cloud(620,220,.8)+'<path d="M60 260 Q400 300 740 260" stroke="#3a3a4a" stroke-width="4" fill="none"/>'
b+='<path d="M300 280 L500 280 L520 700 L430 700 L400 420 L370 700 L280 700Z" fill="#3a6aa8"/><rect x="300" y="280" width="200" height="30" fill="#2a508a"/><path d="M330 330 Q360 380 340 420 M470 330 Q440 380 460 420" stroke="#8ab0d8" stroke-width="4" fill="none"/><path d="M290 650 L520 650" stroke="#8ab0d8" stroke-width="3" stroke-dasharray="8 6"/>'
b+='<rect x="320" y="266" width="14" height="34" fill="#c8a24a"/><rect x="466" y="266" width="14" height="34" fill="#c8a24a"/>'
I[849]=svg(b,d)

# 1040 LA・LA・LA LOVE SONG: a couple dancing on a city rooftop under a disco-blue night with music notes, 90s R&B
d,b=bg([(0,'#0a1a4a'),(1,'#3a5aa8')])
b+=starsf(60,1040,500)+skyline(620,'#0a1030',1040,60,200,'#ffd27a',60)+'<rect y="620" width="800" height="180" fill="#101830"/>'
b+=figure(360,640,250,'#000',pose='up',hair='#000')+figure(450,640,230,'#000',hair='#000')
b+=''.join(note(x,y,s,c) for x,y,s,c in [(240,260,40,'#ff8ad0'),(560,220,46,'#8ad0ff'),(640,330,34,'#ffd02a'),(180,380,30,'#ffd02a')])
I[1040]=svg(b,d)

# 1250 SIGNAL: a traffic light switching to green on a dark crossing, sharp light beams, 2006 boyband
d,b=bg([(0,'#0a0a14'),(1,'#1a2030')])
b+=rays(400,320,14,'#3aff8a',.08,30)+'<rect x="330" y="140" width="140" height="380" rx="30" fill="#1a1a1a" stroke="#4a4a4a" stroke-width="6"/><rect x="390" y="520" width="20" height="280" fill="#2a2a2a"/>'
b+='<circle cx="400" cy="210" r="44" fill="#3a1010"/><circle cx="400" cy="330" r="44" fill="#3a3010"/><circle cx="400" cy="450" r="44" fill="#3aff8a"/>'+glow(400,450,90,'#3aff8a',.7)
I[1250]=svg(b,d)

# 1394 Gimme Chocolate!!: a chocolate bar snapping in half with heavy-metal lightning sparks, kawaii metal
d,b=bg([(0,'#0a0a0a'),(1,'#3a0a14')])
b+=bolt([(150,100),(220,260),(180,280),(260,440)],'#ff2a4a',10)+bolt([(650,120),(590,260),(630,280),(560,420)],'#ff2a4a',10)
b+='<g transform="rotate(-12 300 480)"><rect x="160" y="380" width="230" height="220" rx="8" fill="#5a2a14"/>'+''.join(f'<rect x="{x}" y="{y}" width="60" height="60" rx="6" fill="#7a3a1a"/>' for x in (175,245,315) for y in (395,465,535))+'</g>'
b+='<g transform="rotate(12 500 480)"><rect x="410" y="380" width="230" height="220" rx="8" fill="#5a2a14"/>'+''.join(f'<rect x="{x}" y="{y}" width="60" height="60" rx="6" fill="#7a3a1a"/>' for x in (425,495,565) for y in (395,465,535))+'</g>'
b+=''.join(sparkle(x,y,s,'#ffd02a') for x,y,s in [(400,360,30),(380,620,20),(430,500,16)])
I[1394]=svg(b,d)

# 1811 Another Starting Line: a punk skateboard resting on a fresh white starting line painted on asphalt, dawn
d,b=bg([(0,'#ff8a4a'),(1,'#ffd88a')])
b+='<circle cx="400" cy="420" r="90" fill="#fff4c8"/><path d="M0 440 L800 440 L800 800 L0 800Z" fill="#3a3a44"/><path d="M60 600 L740 600 L760 640 L40 640Z" fill="#f4f4f4"/>'
b+='<path d="M400 440 L380 800 M400 440 L420 800" stroke="#ffd02a" stroke-width="4" stroke-dasharray="30 30" opacity=".6"/>'
b+='<rect x="250" y="560" width="300" height="24" rx="12" fill="#e8302a"/><circle cx="300" cy="594" r="16" fill="#f4f4f4"/><circle cx="500" cy="594" r="16" fill="#f4f4f4"/>'
I[1811]=svg(b,d)

# 155 北酒場: a snowy northern harbour-town tavern with red lanterns and a warm doorway, enka
d,b=bg([(0,'#1a2440'),(1,'#3a4a6a')])
b+=snow(60,155)+'<rect x="180" y="360" width="440" height="300" fill="#4a3424"/><path d="M150 370 L400 250 L650 370Z" fill="#e8eef8"/><rect x="340" y="480" width="120" height="180" fill="#ffc870"/>'+glow(400,560,120,'#ffb070',.5)
b+=chochin(240,440,60)+chochin(560,440,60)+'<rect y="660" width="800" height="140" fill="#e8eef8"/>'
b+='<rect x="320" y="470" width="160" height="50" fill="#1a3a6a"/>'+''.join(f'<rect x="{x}" y="470" width="4" height="50" fill="#e8eef8"/>' for x in (358,398,438))
I[155]=svg(b,d)

# 414 Say Yes!: a white envelope sealed with a pink heart, floating in a soft pastel sky, 80s idol
d,b=bg([(0,'#ffd8ea'),(1,'#d8e8ff')])
b+=sparkle(180,200,26,'#fff')+sparkle(620,180,20,'#fff')+sparkle(640,600,24,'#fff')
b+='<g transform="rotate(-8 400 420)"><rect x="220" y="300" width="360" height="240" rx="10" fill="#fff"/><path d="M220 300 L400 440 L580 300" stroke="#e8c8d8" stroke-width="6" fill="none"/></g>'+heart(400,440,70,'#ff6aa0')
I[414]=svg(b,d)

# 500 卒業: a school building at night with a broken window and a lone youth walking away, 80s rebel
d,b=bg([(0,'#0a0a1a'),(1,'#1a2440')])
b+=starsf(50,500,380)+moon(640,140,50)+'<rect x="120" y="300" width="560" height="320" fill="#2a2a3a"/><rect x="360" y="230" width="80" height="80" fill="#2a2a3a"/><circle cx="400" cy="270" r="26" fill="#e8e8d8"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="60" height="70" fill="#3a3a54"/>' for x in (160,260,500,600) for y in (340,460))
b+='<path d="M500 340 L560 340 L560 410 L500 410Z M510 350 L540 380 L520 400 M540 380 L555 360" fill="#1a1a2a" stroke="#cfe6ff" stroke-width="3"/>'
b+='<rect y="620" width="800" height="180" fill="#14141e"/>'+figure(300,760,170,'#000')
I[500]=svg(b,d)

# 713 あー夏休み: a beach with a big sun, a surfboard stuck in the sand and a beach umbrella, summer band
d,b=bg([(0,'#2ab0ff'),(1,'#a8e8ff')])
b+='<circle cx="620" cy="160" r="80" fill="#ffe84a"/>'+rays(620,160,16,'#fff',.25,8)+'<rect y="440" width="800" height="120" fill="#1a8ad8"/><path d="M0 540 Q400 500 800 540 L800 800 L0 800Z" fill="#f4dca0"/>'
b+='<path d="M200 760 L240 420 Q260 360 280 420 L320 760Z" fill="#ff6a2a"/><path d="M260 400 L260 760" stroke="#fff" stroke-width="6"/>'
b+='<path d="M500 700 L540 480" stroke="#4a3a2a" stroke-width="8"/><path d="M400 500 Q540 380 680 500Z" fill="#e8302a"/><path d="M450 500 Q540 420 540 380 M630 500 Q540 420 540 380" stroke="#fff" stroke-width="10" fill="none"/>'
I[713]=svg(b,d)

# 1696 メロンジュース: a tall glass of green melon soda with a straw and a cherry, retro café, idol pop
d,b=bg([(0,'#fff0d8'),(1,'#d8f4e0')])
b+='<path d="M290 260 L510 260 L480 700 L320 700Z" fill="#e8fff0" opacity=".6"/><path d="M300 340 L500 340 L480 700 L320 700Z" fill="#5ad87a"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".6"/>' for x,y,r in [(360,600,10),(420,520,8),(380,450,12),(450,640,6),(440,400,7)])
b+='<path d="M430 340 L520 120" stroke="#ff5a7a" stroke-width="14" stroke-linecap="round"/><circle cx="360" cy="320" r="34" fill="#e8102a"/><path d="M360 288 Q380 240 410 230" stroke="#3a7a2a" stroke-width="6" fill="none"/>'
I[1696]=svg(b,d)

# 1788 SAYONARAベイベー: two people waving goodbye from opposite ends of a train platform at dusk
d,b=bg([(0,'#ff8a6a'),(1,'#5a4a8a')])
b+='<rect y="560" width="800" height="240" fill="#3a3448"/><rect y="560" width="800" height="14" fill="#ffd02a"/>'+''.join(f'<rect x="{x}" y="120" width="10" height="440" fill="#2a2438"/>' for x in (120,680))+'<rect x="80" y="120" width="640" height="16" fill="#2a2438"/>'
b+=figure(200,580,220,'#1a1424',pose='up',hair='#1a1424')+figure(600,580,240,'#1a1424',pose='up')
b+=heart(400,330,40,'#ff6aa0',' opacity=".7"')
I[1788]=svg(b,d)

# 1798 SAKURA: a single cherry blossom branch over a pale spring sky with petals in the wind
d,b=bg([(0,'#d8eeff'),(1,'#fff0f6')])
b+='<path d="M800 120 Q560 180 420 320 Q340 400 220 440 M560 200 Q520 120 600 60 M420 320 Q440 420 380 500" stroke="#5a3a2a" stroke-width="14" fill="none" stroke-linecap="round"/>'
b+=''.join(sakura(x,y,s,'#ffc2d6','#ff7aa8',r) for x,y,s,r in [(620,170,60,0),(500,250,70,30),(400,330,64,10),(250,430,56,40),(590,80,44,20),(380,500,50,0),(700,130,40,50)])+petals(30,1798)
I[1798]=svg(b,d)

# 900 Steady: two girls' hands linked by a tied ribbon, a promise of steady friendship, 90s teen pop
d,b=bg([(0,'#ffe0f0'),(1,'#ffeccc')])
b+=sparkle(160,180,24,'#fff')+sparkle(640,220,30,'#fff')
b+='<path d="M0 520 Q200 460 340 440 L340 520 Q200 540 0 600Z" fill="#f4c8a8"/><path d="M800 520 Q600 460 460 440 L460 520 Q600 540 800 600Z" fill="#e8b494"/>'
b+='<rect x="320" y="430" width="160" height="60" rx="30" fill="#f0c0a0"/><path d="M400 460 Q340 380 300 400 Q320 460 400 460 Q480 380 520 400 Q480 460 400 460 L360 580 M400 460 L450 590" stroke="#ff4a8a" stroke-width="10" fill="#ff7aa8"/>'
I[900]=svg(b,d)

# 912 グッデイ!!: a bright morning with a big smiling sun rising over rooftops and laundry flapping
d,b=bg([(0,'#ffc84a'),(1,'#fff4c8')])
b+=rays(400,420,20,'#fff',.25,10)+'<circle cx="400" cy="420" r="120" fill="#ffe84a"/><path d="M350 430 Q400 490 450 430" stroke="#c8702a" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="360" cy="390" r="10" fill="#c8702a"/><circle cx="440" cy="390" r="10" fill="#c8702a"/>'
b+='<path d="M0 560 L120 500 L240 560 L360 500 L480 560 L600 500 L720 560 L800 520 L800 800 L0 800Z" fill="#c8483a"/><rect y="600" width="800" height="200" fill="#e8d8c0"/>'
b+='<path d="M40 640 L760 640" stroke="#6a5a4a" stroke-width="3"/>'+''.join(f'<rect x="{x}" y="640" width="60" height="70" fill="{c}"/>' for x,c in [(100,'#3ab0ff'),(260,'#ff6a8a'),(460,'#fff'),(620,'#5ad87a')])
I[912]=svg(b,d)

# 913 over: a dancer's silhouette leaping over a glowing horizontal line in a dark arena, late-90s
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=rays(400,0,10,'#8ab0ff',.1,40,60,120)+'<rect x="0" y="560" width="800" height="8" fill="#8ad0ff"/>'+glow(400,564,300,'#8ad0ff',.4)
b+='<g transform="rotate(-20 400 380)">'+figure(400,520,220,'#000',pose='up')+'</g>'
I[913]=svg(b,d)

# 少年時代 1090: a boy in a straw hat by a rice field at sunset with dragonflies, nostalgic summer
d,b=bg([(0,'#ff9a4a'),(1,'#ffd8a0')])
b+='<circle cx="560" cy="380" r="80" fill="#fff0b0"/><rect y="440" width="800" height="360" fill="#7aa83a"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#5a8a2a" stroke-width="4"/>' for y in range(470,800,40))
b+=figure(260,740,280,'#2a1a14')+'<ellipse cx="260" cy="482" rx="64" ry="14" fill="#e8c870"/><path d="M228 480 Q260 430 292 480Z" fill="#e8c870"/>'
b+=''.join(f'<g transform="translate({x} {y})"><path d="M-20 0 L20 0" stroke="#3a2a2a" stroke-width="5"/><ellipse cx="-4" cy="-6" rx="14" ry="5" fill="#fff" opacity=".6"/><ellipse cx="-4" cy="6" rx="14" ry="5" fill="#fff" opacity=".6"/></g>' for x,y in [(460,240),(620,280),(380,320)])
I[1090]=svg(b,d)

# 1260 EMMA: a mysterious woman's silhouette in a wide hat behind a red velvet curtain, film-noir pop
d,b=bg([(0,'#1a0a0a'),(1,'#3a0a14')])
b+='<path d="M0 0 L240 0 Q200 400 260 800 L0 800Z" fill="#8a0a1a"/><path d="M800 0 L560 0 Q600 400 540 800 L800 800Z" fill="#8a0a1a"/>'+''.join(f'<path d="M{x} 0 Q{x-20} 400 {x+10} 800" stroke="#5a0010" stroke-width="6" fill="none"/>' for x in (60,140,660,740))
b+=glow(400,400,200,'#ffd0a0',.3)+figure(400,760,420,'#000',hair='#000')+'<ellipse cx="400" cy="380" rx="110" ry="20" fill="#000"/><path d="M350 378 Q400 300 450 378Z" fill="#000"/>'
I[1260]=svg(b,d)

# 1271 イッツ マイ ソウル: a heart engulfed in flames held up in a fist, funky soul party
d,b=bg([(0,'#3a0a4a'),(1,'#ff5a2a')])
b+=rays(400,340,18,'#ffd02a',.15,14)+'<path d="M400 140 Q470 240 450 280 Q520 260 500 180 Q580 300 520 420 L280 420 Q220 300 300 200 Q300 260 340 280 Q320 200 400 140Z" fill="#ffb02a"/>'
b+=heart(400,360,90,'#e8102a')+'<rect y="660" width="800" height="140" fill="#1a0a14"/>'+''.join(figure(x,820,220,'#1a0a14',pose='up') for x in (130,270,530,670))
I[1271]=svg(b,d)

# 1640 Infinite City: an endless neon city folding into an infinity loop at night, 2020s boy group
d,b=bg([(0,'#0a0a2a'),(1,'#2a0a4a')])
b+=skyline(700,'#140a2a',1640,80,300,'#8ad0ff',100)
b+='<path d="M400 340 C320 240 160 240 160 340 C160 440 320 440 400 340 C480 240 640 240 640 340 C640 440 480 440 400 340Z" fill="none" stroke="#ff4fd0" stroke-width="16"/>'+glow(400,340,260,'#ff4fd0',.35)
I[1640]=svg(b,d)

# 438 WANDERER: a drifter with a guitar case walking along railway tracks under a red evening sky, 80s
d,b=bg([(0,'#c83a2a'),(1,'#ffb07a')])
b+='<circle cx="400" cy="460" r="70" fill="#ffe0a0"/><rect y="480" width="800" height="320" fill="#3a2a24"/>'
b+='<path d="M380 480 L120 800 M420 480 L680 800" stroke="#8a8a8a" stroke-width="8"/>'+''.join(f'<rect x="{400-(y-480)*.85}" y="{y}" width="{(y-480)*1.7}" height="{4+(y-480)/30}" fill="#5a3a2a"/>' for y in (520,580,660,760))
b+=figure(560,720,220,'#000')+'<rect x="590" y="620" width="40" height="110" rx="14" fill="#000" transform="rotate(10 610 670)"/>'
I[438]=svg(b,d)

# 699 突然: a sudden gust lifting a white sunhat off into a blue summer sky above the sea
d,b=bg([(0,'#3a9ae8'),(1,'#c8ecff')])
b+=cloud(600,160,1.2)+'<rect y="560" width="800" height="240" fill="#2a7ac8"/>'+'<path d="M0 560 L800 560" stroke="#fff" stroke-width="4" opacity=".6"/>'
b+='<g transform="rotate(-24 360 320)"><ellipse cx="360" cy="330" rx="150" ry="44" fill="#f4e8c8"/><path d="M285 330 Q290 230 360 222 Q430 230 435 330Z" fill="#f4e8c8"/><path d="M287 312 Q360 300 433 312 L434 330 Q360 318 286 330Z" fill="#3a6aa8"/><path d="M434 322 Q500 300 540 340 M434 326 Q490 350 520 400" stroke="#3a6aa8" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M230 340 Q360 370 490 340" stroke="#d8c8a0" stroke-width="3" fill="none"/></g>'
b+=''.join(f'<path d="M{x} {y} q40 -20 80 0" stroke="#fff" stroke-width="4" fill="none" opacity=".7"/>' for x,y in [(120,400),(500,380),(160,240)])
I[699]=svg(b,d)

# 883 BLUE TEARS: giant blue teardrops falling over a pop-punk guitar silhouette, early-90s
d,b=bg([(0,'#1a2a5a'),(1,'#4a6ac8')])
b+=''.join(f'<path d="M{x} {y} Q{x+r} {y+r*1.6} {x} {y+r*2.2} Q{x-r} {y+r*1.6} {x} {y}Z" fill="#8ad0ff" opacity="{o}"/>' for x,y,r,o in [(250,140,50,.9),(520,100,70,.9),(640,320,40,.7),(160,360,34,.6),(400,280,30,.6)])
b+=guitar(400,600,1.0,-30,'#0a1430')
I[883]=svg(b,d)

# 969 そのスピードで: a girl on a bicycle speeding down a hill with motion lines, late-90s alt-pop
d,b=bg([(0,'#5ad0c8'),(1,'#e8fff4')])
b+='<path d="M0 360 L800 680 L800 800 L0 800Z" fill="#3a8a5a"/>'+''.join(f'<path d="M{x} {y} L{x-140} {y-56}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>' for x,y in [(300,380),(260,440),(320,480)])
b+='<g transform="rotate(22 480 540)">'+ring(400,600,56,'#1a1a1a',8)+ring(580,600,56,'#1a1a1a',8)+'<path d="M400 600 L480 520 L580 600 M480 520 L520 500" stroke="#1a1a1a" stroke-width="8" fill="none"/>'+figure(490,540,190,'#1a1a1a',hair='#1a1a1a')+'</g>'
I[969]=svg(b,d)

# 1019 ここにいるぜぇ!: a spotlight on an empty stage marked with a big X tape spot, girl-group swagger
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a3a')])
b+='<path d="M340 0 L460 0 L640 640 L160 640Z" fill="#fff4c8" opacity=".25"/><ellipse cx="400" cy="640" rx="240" ry="50" fill="#fff4c8" opacity=".5"/><rect y="640" width="800" height="160" fill="#2a1424"/>'
b+='<path d="M360 610 L440 670 M440 610 L360 670" stroke="#ff4a8a" stroke-width="14" stroke-linecap="round"/>'+figure(400,640,260,'#000',pose='up',hair='#000')
I[1019]=svg(b,d)

# 1032 能動的三分間: a stopwatch frozen at three minutes, cracking with jazzy red energy
d,b=bg([(0,'#1a1a1a'),(1,'#3a1a1a')])
b+='<circle cx="400" cy="440" r="220" fill="#f4f0e8" stroke="#c8a24a" stroke-width="20"/><rect x="380" y="180" width="40" height="40" fill="#c8a24a"/><rect x="360" y="160" width="80" height="24" rx="8" fill="#c8a24a"/>'
b+='<path d="M400 440 L400 240 A200 200 0 0 1 572 340Z" fill="#e8302a" opacity=".7"/>'+''.join(f'<rect x="397" y="236" width="6" height="22" fill="#1a1a1a" transform="rotate({a} 400 440)"/>' for a in range(0,360,30))+'<path d="M400 440 L572 340" stroke="#1a1a1a" stroke-width="8"/><circle cx="400" cy="440" r="12" fill="#1a1a1a"/>'
I[1032]=svg(b,d)

# 1033 Killer-Tune: a vinyl record split by a dagger, a dramatic red stage background, 2007 rock band
d,b=bg([(0,'#4a0a0a'),(1,'#1a0a0a')])
b+='<circle cx="400" cy="420" r="230" fill="#111"/>'+''.join(ring(400,420,r,'#2a2a2a',2) for r in range(110,230,18))+'<circle cx="400" cy="420" r="70" fill="#e8302a"/><circle cx="400" cy="420" r="10" fill="#111"/>'
b+='<g transform="rotate(-35 400 420)"><polygon points="400,90 420,330 380,330" fill="#d8d8e0"/><rect x="350" y="330" width="100" height="18" fill="#c8a24a"/><rect x="388" y="348" width="24" height="90" fill="#3a1a1a"/></g>'
I[1033]=svg(b,d)

# 1127 桜色舞うころ: cherry petals swirling around a lone figure on a path, the seasons turning
d,b=bg([(0,'#f8d8e4'),(1,'#e8e0f0')])
b+=''.join(tree(x,640,h,'#d89ab0',x) for x,h in [(120,380),(680,400)])+petals(70,1127)+'<rect y="640" width="800" height="160" fill="#c8b8c8"/><path d="M340 800 L390 640 L410 640 L460 800Z" fill="#e8dce0"/>'
b+=figure(400,660,190,'#3a2a3a',hair='#3a2a3a')+''.join(sakura(x,y,s,'#ffc2d6','#ff7aa8',r) for x,y,s,r in [(300,300,40,10),(500,260,34,40),(420,180,28,0)])
I[1127]=svg(b,d)

# 1760 卒業 (Saito Yuki): a graduation diploma tube tied with a red ribbon on a school desk, spring light
d,b=bg([(0,'#fff4e0'),(1,'#f0dcc0')])
b+=rays(640,80,10,'#fff',.4,30)+'<rect x="80" y="520" width="640" height="40" fill="#a8784a"/><rect x="120" y="560" width="20" height="240" fill="#7a5a3a"/><rect x="660" y="560" width="20" height="240" fill="#7a5a3a"/>'
b+='<g transform="rotate(-10 400 470)"><rect x="200" y="440" width="400" height="60" rx="30" fill="#1a1a3a"/><ellipse cx="600" cy="470" rx="14" ry="30" fill="#c8a24a"/><path d="M380 440 L380 500" stroke="#e8302a" stroke-width="14"/><path d="M380 500 Q360 560 340 580 M380 500 Q400 560 420 580" stroke="#e8302a" stroke-width="10" fill="none"/></g>'
I[1760]=svg(b,d)

# 339 Telephone Number: a red rotary phone with its cord curling into a heart, city-pop night
d,b=bg([(0,'#1a1a4a'),(1,'#ff6a8a')])
b+=starsf(40,339,400)+skyline(800,'#1a1030',339,60,180,'#ffd27a',50)
b+='<path d="M260 520 Q240 420 300 400 L500 400 Q560 420 540 520Z" fill="#e8302a"/><circle cx="400" cy="460" r="46" fill="#f4f0e8"/>'+''.join(f'<circle cx="{400+32*math.cos(a)}" cy="{460+32*math.sin(a)}" r="7" fill="#e8302a"/>' for a in [k*math.pi/5 for k in range(10)])
b+='<path d="M250 380 Q260 320 330 330 L470 330 Q540 320 550 380" stroke="#e8302a" stroke-width="34" fill="none" stroke-linecap="round"/>'
b+='<path d="M540 500 C620 520 640 600 600 640 C560 680 520 620 560 600" stroke="#f4f0e8" stroke-width="5" fill="none"/>'+heart(620,250,40,'#ffd0e0')
I[339]=svg(b,d)

# 415 アイドルを探せ: a magnifying glass sweeping across a starry sky and finding one shining star
d,b=bg([(0,'#3a2a7a'),(1,'#ff9ad0')])
b+=starsf(70,415,800)+'<circle cx="360" cy="360" r="140" fill="#fff" opacity=".2" stroke="#ffd02a" stroke-width="22"/><rect x="450" y="460" width="40" height="220" rx="16" fill="#ff4a8a" transform="rotate(-40 470 470)"/>'
b+=star5(360,360,60,'#fff4c8')+glow(360,360,70,'#fff4c8',.6)
I[415]=svg(b,d)

# 運命の人: two silhouettes walking toward each other on a long riverside road, connected by a red thread
d,b=bg([(0,'#a8d8f0'),(1,'#f4f0d8')])
b+='<rect y="500" width="800" height="300" fill="#8ac06a"/><path d="M0 560 Q400 520 800 560 L800 620 Q400 580 0 620Z" fill="#5aa8d8"/>'
b+=figure(200,720,220,'#2a2a3a')+figure(600,720,210,'#2a2a3a',hair='#2a2a3a')+'<path d="M222 620 Q400 720 578 620" stroke="#e8102a" stroke-width="4" fill="none"/>'
I[773]=svg(b,d)

# 1426 女々しくて: a man in a suit clutching a handkerchief in the rain beside a wilted flower, comic sorrow
d,b=bg([(0,'#c8a8e0'),(1,'#f4d0e8')])
b+=rain(70,1426,'#7a6aa8',.4)+'<rect y="640" width="800" height="160" fill="#a888c0"/>'+figure(380,660,320,'#2a1a3a')
b+='<path d="M430 420 L500 400 L520 470 L460 480Z" fill="#fff"/><path d="M620 640 L620 520 Q640 500 610 480" stroke="#3a7a2a" stroke-width="6" fill="none"/><path d="M610 480 Q580 470 590 500 Q610 520 610 480" fill="#ff7aa8"/>'
I[1426]=svg(b,d)

# 1718 Super Lover: a sleek dancer mid-spin under a disco ball shooting light beams, 2003 pop
d,b=bg([(0,'#0a0a2a'),(1,'#3a1a5a')])
b+='<line x1="400" y1="0" x2="400" y2="90" stroke="#aaa" stroke-width="3"/><circle cx="400" cy="150" r="60" fill="#c8c8d8"/>'+''.join(f'<rect x="{x}" y="{y}" width="14" height="14" fill="#fff" opacity="{o}"/>' for x,y,o in [(360,110,.8),(390,130,.5),(420,110,.9),(370,160,.6),(410,170,.8),(440,150,.5)])
b+=rays(400,150,16,'#ff8ad0',.12,10,20,160)+figure(400,720,340,'#000',pose='up')+'<path d="M300 720 Q400 690 500 720" stroke="#ff8ad0" stroke-width="4" fill="none"/>'
I[1718]=svg(b,d)

# 1878 イッサイガッサイ: a cardboard moving box overflowing with everything: records, books, a mic, hip-hop
d,b=bg([(0,'#ffd04a'),(1,'#ff9a4a')])
b+='<rect x="200" y="420" width="400" height="300" fill="#c8945a"/><path d="M200 420 L140 340 L360 380Z M600 420 L660 340 L440 380Z" fill="#b8844a"/><rect x="380" y="420" width="40" height="300" fill="#e8c88a"/>'
b+='<circle cx="300" cy="360" r="70" fill="#111"/><circle cx="300" cy="360" r="20" fill="#e8302a"/><rect x="420" y="260" width="70" height="170" fill="#3a6ab8" transform="rotate(14 455 345)"/><rect x="490" y="290" width="60" height="140" fill="#5ad87a" transform="rotate(24 520 360)"/>'
b+='<g transform="rotate(-20 380 300)"><rect x="370" y="230" width="20" height="140" fill="#2a2a2a"/><circle cx="380" cy="220" r="30" fill="#8a8a9a"/></g>'
I[1878]=svg(b,d)

# 1883 大丈夫: a hand on a friend's shoulder as two silhouettes watch the dawn over a town, hip-hop ballad
d,b=bg([(0,'#3a4a8a'),(1,'#ffb07a')])
b+='<circle cx="400" cy="560" r="100" fill="#ffe8b0"/>'+rays(400,560,16,'#fff',.15,10)+skyline(600,'#2a2438',1883,30,120)+'<rect y="600" width="800" height="200" fill="#1a1424"/>'
b+=figure(340,780,260,'#000')+figure(460,780,250,'#000')+'<path d="M370 590 Q410 570 440 600" stroke="#000" stroke-width="22" fill="none" stroke-linecap="round"/>'
I[1883]=svg(b,d)

# 346 Aqua: concentric ripples spreading from a single water drop over a still blue surface, piano ambient
d,b=bg([(0,'#0a2a4a'),(1,'#4a9ac8')])
b+=''.join(ring(400,520,r,'#cfe6ff',4,1-r/400) for r in (40,100,170,250,340))
b+='<path d="M400 160 Q440 240 400 280 Q360 240 400 160Z" fill="#cfe6ff"/>'+glow(400,520,60,'#cfe6ff',.5)
I[346]=svg(b,d)

# 501 僕が僕であるために: a youth standing alone on a highway overpass at night, city lights below, 80s rock
d,b=bg([(0,'#0a0a1a'),(1,'#2a2a4a')])
b+=starsf(40,501,300)+skyline(560,'#14142a',501,60,220,'#ffd27a',90)+'<rect y="560" width="800" height="240" fill="#0a0a14"/>'
b+='<rect x="0" y="480" width="800" height="30" fill="#3a3a4a"/><path d="M0 480 L800 480" stroke="#8a8a9a" stroke-width="4"/>'+''.join(f'<rect x="{x}" y="440" width="6" height="40" fill="#5a5a6a"/>' for x in range(20,800,60))
b+=''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>' for x,y,c in [(120,620,'#ff4a4a'),(160,630,'#ff4a4a'),(560,660,'#fff4c8'),(600,650,'#fff4c8'),(320,700,'#ff4a4a')])
b+=figure(420,480,200,'#000')
I[501]=svg(b,d)

# 1015 Bold & Delicious: a glamorous red lipstick and a cherry dessert on a gold plate, 2005 pop diva
d,b=bg([(0,'#1a0a14'),(1,'#5a0a2a')])
b+=sparkle(160,160,26,'#ffd02a')+sparkle(640,200,20,'#ffd02a')+'<ellipse cx="460" cy="620" rx="220" ry="50" fill="#c8a24a"/><ellipse cx="460" cy="610" rx="190" ry="38" fill="#e8c86a"/>'
b+='<path d="M380 600 Q460 440 540 600Z" fill="#f4e8e0"/><circle cx="460" cy="490" r="30" fill="#e8102a"/><path d="M460 460 Q470 420 500 410" stroke="#3a7a2a" stroke-width="6" fill="none"/>'
b+='<rect x="190" y="440" width="70" height="200" rx="6" fill="#c8a24a"/><path d="M200 440 L200 330 L250 300 L250 440Z" fill="#e8102a"/>'
I[1015]=svg(b,d)

# 1114 YES!: a crowd of raised hands with a big confetti burst over a stadium stage, dance group anthem
d,b=bg([(0,'#0a0a2a'),(1,'#3a2a6a')])
b+=rays(400,300,20,'#fff',.1,20)+confetti(90,1114,['#ffd02a','#fff','#ff6aa0','#8ad0ff'])+'<rect y="660" width="800" height="140" fill="#0a0a14"/>'
b+=''.join(figure(x,820,200+(x%3)*20,'#000',pose='up') for x in range(60,800,90))
I[1114]=svg(b,d)

# 1837 Exterminate: a glowing sword cutting a crimson energy slash across a stormy sky, anime-song power
d,b=bg([(0,'#1a0a2a'),(1,'#4a0a1a')])
b+=bolt([(120,80),(200,240),(160,260),(240,400)],'#ff8ad0',6,.7)+'<path d="M80 640 Q400 360 740 160" stroke="#ff2a4a" stroke-width="40" fill="none" opacity=".6"/><path d="M80 640 Q400 360 740 160" stroke="#fff" stroke-width="10" fill="none"/>'+glow(400,420,180,'#ff2a4a',.4)
b+='<g transform="rotate(-35 400 420)"><polygon points="400,150 420,520 380,520" fill="#e8eef8"/><rect x="340" y="520" width="120" height="20" fill="#c8a24a"/><rect x="388" y="540" width="24" height="110" fill="#2a1a2a"/></g>'
I[1837]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
