import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 4. csoport, 2026-10-24
I={}
def rose(x,y,s,rot=0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#a8081e',1),(60,'#c81028',.9),(-60,'#c81028',.9),(150,'#e01a34',.7),(-150,'#e01a34',.7)])+'</g>'
def star5(x,y,s,col,rot=0):
    return f'<path transform="rotate({rot} {x} {y})" d="'+' '.join(f'{"M" if k==0 else "L"}{x+s*(1 if k%2==0 else .42)*math.sin(k*math.pi/5):.1f} {y-s*(1 if k%2==0 else .42)*math.cos(k*math.pi/5):.1f}' for k in range(10))+f'Z" fill="{col}"/>'

# 1149 蕾: a single tight flower bud on a slender stem, about to open in the first warm morning light
d,b=bg([(0,'#ffe8d0'),(1,'#ffc8b0')])
b+=glow(400,300,220,'#fffbe8',.8)+rays(400,300,14,'#ffffff',.25,8)
b+='<path d="M400 800 Q380 600 400 420" stroke="#4a8a3a" stroke-width="14" fill="none"/><path d="M394 620 Q300 560 280 480 Q360 520 400 590Z M402 540 Q500 500 520 430 Q440 450 402 510Z" fill="#5aa04a"/>'
b+='<path d="M400 430 Q330 380 350 280 Q370 220 400 200 Q430 220 450 280 Q470 380 400 430Z" fill="#ff7a9a"/><path d="M400 430 Q350 380 368 300 Q380 250 400 230Z" fill="#ff9ab4"/>'
b+='<path d="M400 440 Q360 420 350 380 Q380 400 400 410 Q420 400 450 380 Q440 420 400 440Z" fill="#4a8a3a"/>'
I[1149]=svg(b,d)

# 1540 香水: an elegant perfume bottle on a dark vanity, a pale swirl of scent curling up into the air
d,b=bg([(0,'#1a1020'),(1,'#3a2030')])
b+=glow(400,450,200,'#ffc8e0',.35)
for k in range(3): b+=f'<path d="M{400+k*10} 300 Q{460+k*30} 220 {400} 160 Q{340-k*30} 100 {420+k*20} 40" stroke="#ffd8ec" stroke-width="{10-k*3}" fill="none" opacity="{.5-k*.12:.2f}" stroke-linecap="round"/>'
d+=lg('pf',S((0,'#ffd0e4',.9),(1,'#c86a9a',.9)))
b+='<rect x="300" y="420" width="200" height="220" rx="30" fill="url(#pf)"/><rect x="320" y="440" width="40" height="180" rx="16" fill="#fff" opacity=".35"/>'
b+='<rect x="372" y="370" width="56" height="54" rx="8" fill="#d8b050"/><rect x="384" y="330" width="32" height="44" rx="6" fill="#e8c860"/>'
b+='<rect y="640" width="800" height="160" fill="#2a1420"/><ellipse cx="400" cy="646" rx="140" ry="12" fill="#000" opacity=".35"/>'
I[1540]=svg(b,d)

# 1647 Blue Jeans: a worn pair of blue jeans hanging on a clothesline against a bright city sky, patches and all
d,b=bg([(0,'#4ab0f0'),(1,'#c8ecff')])
b+=skyline(760,'#a8c8e0',1647,60,200)
b+='<path d="M60 190 Q400 240 740 180" stroke="#4a4a4a" stroke-width="5" fill="none"/>'
b+='<path d="M260 210 L540 210 L560 700 L440 700 L410 360 L390 360 L360 700 L240 700Z" fill="#2a5aa8"/><path d="M260 210 L540 210 L542 260 L258 260Z" fill="#1a4a90"/>'
b+='<path d="M290 280 Q330 330 370 280 M430 280 Q470 330 510 280" stroke="#e8b040" stroke-width="4" fill="none"/><path d="M400 260 L400 360" stroke="#e8b040" stroke-width="4"/><circle cx="400" cy="236" r="9" fill="#d8a030"/>'
b+='<rect x="290" y="520" width="56" height="56" fill="#ff7a8a" transform="rotate(8 318 548)"/><rect x="456" y="580" width="50" height="50" fill="#ffd84a" transform="rotate(-6 481 605)"/>'
b+='<rect x="250" y="190" width="20" height="40" rx="4" fill="#e8302a"/><rect x="530" y="190" width="20" height="40" rx="4" fill="#e8302a"/>'
I[1647]=svg(b,d)

# 1706 世界中の誰よりきっと: a glowing globe with a red heart pinned on Japan, two figures standing hand in hand on top of it
d,b=bg([(0,'#0a1a4a'),(1,'#2a3a7a')])
b+=starsf(70,1706,800,'#e8f0ff')+glow(400,520,280,'#5ab0ff',.3)
b+='<circle cx="400" cy="620" r="300" fill="#1a7ad8"/><path d="M200 520 Q260 470 320 500 Q360 540 300 580 Q240 600 200 520Z M480 440 Q560 420 620 470 Q640 540 570 560 Q500 540 480 440Z M360 640 Q420 610 470 650 Q480 700 420 720 Q360 700 360 640Z" fill="#3ac86a"/>'
b+=heart(610,470,22,'#ff3a5a')+figure(370,330,130,'#0a1430')+figure(430,330,124,'#0a1430',hair='#0a1430')
I[1706]=svg(b,d)

# 1464 灰色と青: a sky split between heavy grey clouds and clear blue, two bicycles parked under the line where they meet
d,b=bg([(0,'#7a7a84'),(1,'#a8a8b0')])
b+='<path d="M400 0 L800 0 L800 800 L400 800Z" fill="#3a8ae8"/><path d="M400 0 L800 0 L800 800 L400 800Z" fill="url(#bg)" opacity="0"/>'
for x,y,s in [(160,180,1.4),(240,330,1.0)]: b+=cloud(x,y,s,'#5a5a64',.9)
b+=cloud(620,200,1.1,'#fff',.9)
b+='<rect y="620" width="800" height="180" fill="#3a3a44"/><rect x="400" y="620" width="400" height="180" fill="#2a5a9a"/>'
for cx,c in [(280,'#c8c8d0'),(520,'#fff')]:
    b+=f'<g stroke="{c}" stroke-width="10" fill="none"><circle cx="{cx-60}" cy="620" r="50"/><circle cx="{cx+60}" cy="620" r="50"/><path d="M{cx-60} 620 L{cx-10} 540 L{cx+40} 540 L{cx+60} 620 M{cx-10} 540 L{cx} 620 L{cx+40} 540 M{cx-20} 520 L{cx} 520 M{cx+40} 540 L{cx+36} 510 L{cx+60} 506"/></g>'
I[1464]=svg(b,d)

# 280 エロティカ・セブン: a glowing red neon 7 behind a pair of scarlet lips and a gold saxophone, late-night club
d,b=bg([(0,'#12040a'),(1,'#2a0614')])
b+=neon(400,520,'7','#ff2a4a',520,'DejaVu Sans,sans-serif')
b+='<g transform="translate(400 600)"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="#e8102a"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="#b80a20"/></g>'
b+='<g transform="rotate(-30 640 300)"><rect x="620" y="140" width="34" height="280" rx="16" fill="#e8b830"/><path d="M620 400 Q600 480 660 490 Q720 480 700 400Z" fill="#e8b830"/><path d="M630 140 L600 110" stroke="#1a1a1a" stroke-width="8"/></g>'
I[280]=svg(b,d)

# 1194 Five: five stars in five colours joined in a ring, shining together against a deep night
d,b=bg([(0,'#0a0a2a'),(1,'#1a1a4a')])
b+=starsf(60,1194,800,'#e8f0ff')+glow(400,400,220,'#ffffff',.25)
b+='<circle cx="400" cy="400" r="200" fill="none" stroke="#fff" stroke-width="5" opacity=".5"/>'
for k,c in enumerate(['#3a6aff','#ff3a3a','#3ac84a','#ffd82a','#a84aff']):
    a=math.radians(-90+k*72);x=400+200*math.cos(a);y=400+200*math.sin(a)
    b+=glow(x,y,60,c,.5)+star5(x,y,74,c)
I[1194]=svg(b,d)

# 1195 Monster: a horned monster's shadow looming over a gothic castle under a huge full moon
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=moon(400,330,170,'#f4ecc8',.4)
b+='<g fill="#2a0a3a"><path d="M220 520 Q200 300 300 220 L280 140 L330 210 Q400 180 470 210 L520 140 L500 220 Q600 300 580 520Z"/></g>'
b+='<circle cx="350" cy="320" r="18" fill="#ffd82a"/><circle cx="450" cy="320" r="18" fill="#ffd82a"/><path d="M350 400 L370 420 L390 400 L410 420 L430 400 L450 420" stroke="#ffd82a" stroke-width="6" fill="none"/>'
b+='<g fill="#0a0414"><rect x="120" y="520" width="560" height="280"/><rect x="100" y="420" width="90" height="380"/><rect x="610" y="420" width="90" height="380"/><path d="M90 420 L145 330 L200 420Z M600 420 L655 330 L710 420Z"/>'
for x in range(130,680,40): b+=f'<rect x="{x}" y="500" width="22" height="24"/>'
b+='</g><rect x="380" y="640" width="40" height="60" fill="#ffd27a"/>'
I[1195]=svg(b,d)

# 892 fragile: a delicate glass vase with a fine crack running through it, one white flower still standing inside
d,b=bg([(0,'#e0e8f0'),(1,'#b8c8d8')])
b+=glow(400,420,200,'#ffffff',.7)
b+='<path d="M400 320 Q440 300 440 260 L360 260 Q360 300 400 320Z" fill="#fff" opacity=".6"/>'
b+='<path d="M350 260 L450 260 L450 300 Q540 360 540 500 Q540 640 400 650 Q260 640 260 500 Q260 360 350 300Z" fill="#d8ecff" opacity=".7" stroke="#fff" stroke-width="5"/>'
b+='<path d="M400 640 L400 200" stroke="#4a8a3a" stroke-width="6"/>'+flower(400,190,90,7,'#ffffff','#ffd84a',10,.6)
b+=bolt([(470,330),(450,400),(490,450),(460,540)],'#5a6a8a',3,.9)
b+='<ellipse cx="400" cy="660" rx="160" ry="16" fill="#000" opacity=".12"/>'
I[892]=svg(b,d)

# 930 ボクの背中には羽根がある: a boy seen from behind, a pair of white feathered wings unfolding from his back at sunset
d,b=bg([(0,'#3a2a6a'),(.6,'#e8806a'),(1,'#ffc890')])
b+=glow(400,420,220,'#fff0d8',.5)
for sx in (-1,1):
    for k in range(6):
        b+=f'<path d="M400 360 Q{400+sx*(120+k*30)} {280-k*20} {400+sx*(200+k*40)} {200+k*40} Q{400+sx*(140+k*20)} {330+k*10} 400 {380+k*6}Z" fill="#fff" opacity="{.95-k*.08:.2f}"/>'
b+=figure(400,760,380,'#1a1020')
I[930]=svg(b,d)

# 1465 感電: a dancer jolted by electricity, crackling neon lightning arcing out of a tangle of power cables
d,b=bg([(0,'#0a0a1a'),(1,'#1a0a2a')])
b+=glow(400,400,240,'#5ae8ff',.3)
b+=bolt([(120,120),(220,240),(170,300),(300,400)],'#5ae8ff',10,.9)+bolt([(680,100),(600,230),(660,290),(520,380)],'#ffe05a',10,.9)+bolt([(400,60),(380,180),(420,240),(400,330)],'#ff5ad8',8,.9)
b+='<path d="M0 700 Q200 640 300 720 T560 680 T800 720" stroke="#2a2a3a" stroke-width="16" fill="none"/><path d="M0 740 Q200 680 320 760 T600 730 T800 760" stroke="#3a3a4a" stroke-width="14" fill="none"/>'
b+=figure(400,700,300,'#060610',pose='up')
I[1465]=svg(b,d)

# 233 地上の星: a night valley of factory and city lights seen from a hill, mirroring the stars above
d,b=bg([(0,'#04081e'),(1,'#121a3a')])
b+=starsf(120,233,360,'#e8f0ff')+''.join(sparkle(x,y,s,'#fff6d8') for x,y,s in [(200,120,22),(420,80,30),(620,150,24),(330,220,16),(540,250,14)])
b+='<path d="M-10 380 Q400 340 810 380 L810 810 L-10 810Z" fill="#06081a"/>'
r=R(233)
for _ in range(200):
    y=r.uniform(400,720);x=r.uniform(0,800);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.choice([2,2.5,3])}" fill="{r.choice(["#ffd27a","#fff6d8","#ffb05a"])}" opacity="{r.uniform(.5,1):.2f}"/>'
b+='<path d="M-10 800 L-10 700 Q200 660 330 720 L400 810Z" fill="#020410"/>'+figure(200,700,110,'#020410')
I[233]=svg(b,d)

# 717 ら・ら・ら: a glittering karaoke microphone in a spotlight, music notes bursting out like confetti
d,b=bg([(0,'#3a0a5a'),(1,'#ff4a8a')])
b+=rays(400,420,20,'#ffffff',.15,6)+confetti(40,717,['#ffe05a','#5ae8ff','#ffffff'])
b+='<g transform="rotate(-24 400 460)"><circle cx="400" cy="300" r="90" fill="#d8d8e0"/>'+''.join(f'<path d="M{330+k*20} 240 L{330+k*20} 360" stroke="#9a9aa8" stroke-width="4"/>' for k in range(8))+'<path d="M350 380 L450 380 L420 640 L380 640Z" fill="#2a2a34"/><rect x="380" y="430" width="40" height="40" rx="8" fill="#ff4a8a"/></g>'
b+=note(170,220,40,'#fff',True)+note(620,180,36,'#ffe05a')+note(640,560,30,'#fff')+note(150,560,28,'#5ae8ff',True)
I[717]=svg(b,d)

# 854 READY STEADY GO: a sprinter crouched in the starting blocks on a red track, the starting gun smoking
d,b=bg([(0,'#2a2a4a'),(1,'#5a3a5a')])
b+=glow(400,300,240,'#ffe8c8',.3)
b+='<path d="M-10 800 L-10 460 L810 460 L810 800Z" fill="#c8402a"/>'+''.join(f'<path d="M{-200+k*200} 800 L{200+k*100} 460" stroke="#fff" stroke-width="5"/>' for k in range(6))
b+='<rect y="456" width="800" height="10" fill="#fff"/>'
b+='<g fill="#0a0a14"><ellipse cx="420" cy="380" rx="22" ry="24"/><path d="M400 400 Q300 410 260 480 L280 490 Q320 440 400 430Z"/><path d="M430 400 Q460 420 470 470 L456 476 Q440 440 420 430Z"/><path d="M300 470 L230 520 L250 540 L320 490Z"/><path d="M270 480 L220 470 L210 500 L260 500Z"/><path d="M420 410 L410 470 L424 470 L436 412Z"/></g>'
b+='<g transform="translate(600 220)"><rect x="0" y="0" width="90" height="34" rx="8" fill="#2a2a34"/><rect x="0" y="20" width="26" height="60" rx="6" fill="#2a2a34"/></g>'+cloud(720,180,.4,'#e8e8f0',.8)
I[854]=svg(b,d)

# 1045 POP STAR: a bubblegum-pink star bursting with sparkles, a heart-shaped microphone in the middle
d,b=bg([(0,'#ffd8f4'),(1,'#ff9ad8')])
b+=rays(400,400,18,'#ffffff',.35,8)+star5(400,420,300,'#ff4ab8')+star5(400,420,230,'#ff8ad4')
b+='<rect x="390" y="430" width="20" height="160" rx="10" fill="#fff"/>'+heart(400,380,60,'#fff')+heart(400,380,44,'#ffd84a')
for x,y,s in [(160,170,26),(650,160,30),(140,620,22),(660,640,28)]: b+=sparkle(x,y,s,'#fff')
I[1045]=svg(b,d)

# 1131 Hello,World!: an old computer terminal glowing green with the first words of every program
d,b=bg([(0,'#0a1a14'),(1,'#1a2a20')])
b+=glow(400,360,220,'#5aff8a',.25)
b+='<rect x="160" y="160" width="480" height="380" rx="30" fill="#d8d0b8"/><rect x="200" y="200" width="400" height="290" rx="16" fill="#041a0a"/>'
b+='<text x="230" y="300" font-family="DejaVu Sans Mono,monospace" font-weight="700" font-size="44" fill="#5aff8a">Hello,</text><text x="230" y="360" font-family="DejaVu Sans Mono,monospace" font-weight="700" font-size="44" fill="#5aff8a">World!</text><rect x="400" y="330" width="24" height="36" fill="#5aff8a"/>'
b+='<path d="M300 540 L500 540 L540 620 L260 620Z" fill="#c8c0a8"/><rect x="200" y="620" width="400" height="60" rx="10" fill="#b8b0a0"/>'
I[1131]=svg(b,d)

# 1196 truth: a black chess king standing alone on a lightning-lit board, the white pieces fallen around it
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=bolt([(600,0),(560,120),(610,170),(540,320)],'#e8e8ff',6,.8)+glow(560,180,100,'#c8c8ff',.25)
for i in range(8):
    for j in range(4):
        x=-80+i*120+j*30;y=520+j*70
        b+=f'<polygon points="{x},{y} {x+120},{y} {x+150},{y+70} {x+30},{y+70}" fill="{"#d8d8e0" if (i+j)%2 else "#2a2a34"}"/>'
b+='<g fill="#08080c"><path d="M340 580 L460 580 L440 540 L360 540Z"/><path d="M370 540 Q350 420 380 360 L420 360 Q450 420 430 540Z"/><rect x="360" y="330" width="80" height="34" rx="8"/><rect x="390" y="270" width="20" height="64"/><rect x="370" y="290" width="60" height="18"/></g>'
b+='<g fill="#e8e8f0"><ellipse cx="220" cy="600" rx="50" ry="18" transform="rotate(-10 220 600)"/><ellipse cx="590" cy="640" rx="44" ry="16" transform="rotate(14 590 640)"/></g>'
I[1196]=svg(b,d)

# 1491 Cry Baby: a giant teardrop reflecting a neon night street, smaller tears splashing below
d,b=bg([(0,'#0a0a24'),(1,'#2a0a3a')])
d+=lg('td',S((0,'#5ae0ff'),(.5,'#3a6aff'),(1,'#ff4ab8')))
b+=glow(400,400,220,'#5ab0ff',.35)
b+='<path d="M400 120 Q520 320 540 420 Q560 580 400 600 Q240 580 260 420 Q280 320 400 120Z" fill="url(#td)"/>'
b+=skyline(560,'#1a0a3a',1491,40,130,'#ffd27a',30).replace('<g fill','<g opacity=".0" fill')
b+='<path d="M300 520 L300 470 L330 470 L330 440 L360 440 L360 500 L400 500 L400 450 L440 450 L440 520 L500 520" stroke="#ffe8ff" stroke-width="5" fill="none" opacity=".7"/>'
b+='<ellipse cx="330" cy="300" rx="20" ry="40" fill="#fff" opacity=".5" transform="rotate(20 330 300)"/>'
b+='<ellipse cx="400" cy="720" rx="200" ry="26" fill="#3a6aff" opacity=".4"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="13" fill="#8ad0ff"/>' for x,y in [(300,680),(510,690),(400,660)])
I[1491]=svg(b,d)

# 1839 廻廻奇譚: a swirling vortex of red and black, paper talismans spinning around its glowing centre
d,b=bg([(0,'#0a0004'),(1,'#2a0408')])
for k in range(28):
    a=k*0.45;r_=20+k*12
    b+=f'<circle cx="{400+r_*math.cos(a):.0f}" cy="{400+r_*math.sin(a):.0f}" r="{8+k*.6:.1f}" fill="{"#e8102a" if k%2 else "#3a0a10"}" opacity=".8"/>'
b+=glow(400,400,90,'#ff2a3a',.8)
r=R(1839)
for k in range(7):
    a=k*51;x=400+250*math.cos(math.radians(a));y=400+250*math.sin(math.radians(a))
    b+=f'<g transform="rotate({a+90:.0f} {x:.0f} {y:.0f})"><rect x="{x-24:.0f}" y="{y-60:.0f}" width="48" height="120" fill="#f4e8c8"/><path d="M{x:.0f} {y-44:.0f} L{x:.0f} {y+44:.0f} M{x-14:.0f} {y-20:.0f} L{x+14:.0f} {y-20:.0f}" stroke="#c8101a" stroke-width="6"/></g>'
I[1839]=svg(b,d)

# 832 Winter, again: a lone tree and a small red-roofed house standing in a vast Hokkaido snowfield under falling snow
d,b=bg([(0,'#7a8aa8'),(1,'#d8e0ec')])
b+=snow(160,832,.9)
b+='<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#f4f8ff"/>'
b+='<path d="M560 560 L560 380 M560 440 L510 380 M560 420 L610 360 M560 480 L600 440" stroke="#2a2a34" stroke-width="10" fill="none"/>'
b+='<rect x="200" y="470" width="160" height="100" fill="#d8d0c8"/><path d="M180 480 L280 400 L380 480Z" fill="#c8302a"/><path d="M190 476 L280 404 L370 476" stroke="#fff" stroke-width="10" fill="none"/><rect x="240" y="500" width="34" height="30" fill="#ffd27a"/>'
for x in range(40,800,90): b+=f'<rect x="{x}" y="620" width="6" height="40" fill="#5a5a64"/>'
b+='<path d="M0 630 L800 630" stroke="#5a5a64" stroke-width="3"/>'
I[832]=svg(b,d)

# 855 HONEY: a glass honey jar with a wooden dipper, golden honey dripping down and two bees buzzing around
d,b=bg([(0,'#ffe8a0'),(1,'#ffc040')])
for i in range(7):
    for j in range(7):
        x=60+i*112+(j%2)*56;y=60+j*96
        b+=f'<polygon points="'+' '.join(f'{x+50*math.cos(math.radians(60*k)):.0f},{y+50*math.sin(math.radians(60*k)):.0f}' for k in range(6))+'" fill="none" stroke="#ffd060" stroke-width="5"/>'
b+='<rect x="250" y="320" width="300" height="340" rx="40" fill="#ffb81a" opacity=".92"/><rect x="230" y="280" width="340" height="60" rx="14" fill="#a8582a"/>'
b+='<path d="M250 360 Q300 420 280 460 Q320 410 360 380 Q380 440 400 460 Q420 400 450 380 Q470 430 520 450 Q510 400 550 360Z" fill="#ffd060"/>'
b+='<rect x="440" y="140" width="20" height="200" fill="#8a5a2a" transform="rotate(20 450 240)"/><ellipse cx="410" cy="330" rx="40" ry="30" fill="#a8683a" transform="rotate(20 410 330)"/>'
for x,y in [(200,200),(620,250)]: b+=f'<ellipse cx="{x}" cy="{y}" rx="30" ry="22" fill="#ffd21a"/><path d="M{x-10} {y-22} L{x-10} {y+22} M{x+8} {y-22} L{x+8} {y+22}" stroke="#2a1a0a" stroke-width="8"/><ellipse cx="{x-6}" cy="{y-34}" rx="18" ry="12" fill="#fff" opacity=".8"/><ellipse cx="{x+14}" cy="{y-30}" rx="16" ry="11" fill="#fff" opacity=".8"/>'
I[855]=svg(b,d)

# 967 There will be love there -愛のある場所-: sunlight pouring through a heart-shaped gap in the clouds onto a quiet green field
d,b=bg([(0,'#5a6a8a'),(1,'#8a9ab8')])
for x,y,s in [(150,150,1.8),(650,140,1.8),(400,90,1.4),(130,330,1.3),(680,320,1.3)]: b+=cloud(x,y,s,'#c8d0e0',.95)
b+=heart(400,260,120,'#ffe8b0')+glow(400,260,140,'#fff6d8',.5)
b+='<polygon points="300,280 500,280 680,660 120,660" fill="#fff6d8" opacity=".25"/>'
b+='<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#5aa04a"/><ellipse cx="400" cy="620" rx="260" ry="40" fill="#c8e88a" opacity=".6"/>'
I[967]=svg(b,d)

# 480 Marionette: a puppet dangling from wooden control bars on long strings, its limbs pulled in a jerky dance
d,b=bg([(0,'#1a1a1a'),(1,'#3a2a2a')])
b+='<polygon points="400,-20 220,800 580,800" fill="#fff" opacity=".07"/>'
b+='<rect x="260" y="80" width="280" height="20" rx="6" fill="#8a5a3a"/><rect x="390" y="40" width="20" height="120" rx="6" fill="#8a5a3a"/>'
b+='<g fill="#d8d0c8"><circle cx="400" cy="300" r="40"/><rect x="370" y="350" width="60" height="150" rx="14"/></g>'
b+='<path d="M372 370 L280 300 M428 370 L520 280 M385 500 L340 640 M415 500 L470 620" stroke="#d8d0c8" stroke-width="20" stroke-linecap="round"/>'
b+='<path d="M270 90 L280 300 M530 90 L520 280 M400 100 L400 260 M300 100 L340 640 M500 100 L470 620" stroke="#e8e8e8" stroke-width="2" opacity=".7"/>'
b+='<circle cx="386" cy="296" r="5" fill="#1a1a1a"/><circle cx="414" cy="296" r="5" fill="#1a1a1a"/><path d="M380 260 L420 260" stroke="#e8302a" stroke-width="8"/>'
I[480]=svg(b,d)

# 960 HOT LIMIT: a thermometer bursting past its top under a scorching summer sun over a glittering sea
d,b=bg([(0,'#ff6a1a'),(.5,'#ffb02a'),(1,'#1aa8e8')])
b+=rays(400,180,24,'#fff6c8',.3,6)+glow(400,180,140,'#fffbe0',.9)+'<circle cx="400" cy="180" r="80" fill="#fff8d8"/>'
b+='<rect y="560" width="800" height="240" fill="#0a8ad8"/>'
b+='<rect x="370" y="250" width="60" height="420" rx="30" fill="#fff"/><circle cx="400" cy="680" r="56" fill="#fff"/><circle cx="400" cy="680" r="40" fill="#e8102a"/><rect x="386" y="270" width="28" height="410" fill="#e8102a"/>'
for k in range(8): b+=f'<path d="M430 {300+k*44} l20 0" stroke="#5a5a64" stroke-width="4"/>'
r=R(960)
for k in range(10): a=math.radians(-90+(k-4.5)*18);b+=f'<circle cx="{400+90*math.cos(a):.0f}" cy="{270+90*math.sin(a):.0f}" r="10" fill="#e8102a"/>'
I[960]=svg(b,d)

# 987 Voyage: a tall sailing ship gliding across a moonlit sea under a sky full of stars
d,b=bg([(0,'#04082a'),(1,'#1a2a5a')])
b+=starsf(100,987,500,'#e8f0ff')+moon(620,160,50,'#f4f8ff')
b+='<rect y="560" width="800" height="240" fill="#0a1a40"/>'+''.join(f'<rect x="{560-k*16}" y="{580+k*26}" width="{120+k*32}" height="4" fill="#f4f8ff" opacity="{.6-k*.08:.2f}"/>' for k in range(7))
b+='<path d="M220 560 L560 560 L520 620 L260 620Z" fill="#1a0a0a"/><path d="M300 560 L300 220 M420 560 L420 180" stroke="#1a0a0a" stroke-width="10"/>'
b+='<path d="M310 240 Q380 330 310 420 Z M310 440 Q390 500 310 550Z M430 200 Q520 300 430 400Z M430 420 Q520 480 430 550Z" fill="#f4ecd8"/><path d="M420 180 L470 196 L420 210Z" fill="#e8302a"/>'
I[987]=svg(b,d)

# 1176 遥か: a long country road running toward distant blue mountains, a backpack resting at the roadside
d,b=bg([(0,'#5ab0f0'),(.7,'#c8e8ff'),(1,'#e8f6ff')])
b+=cloud(200,160,1.0)+'<path d="M-10 420 L150 300 L300 400 L470 260 L640 380 L810 300 L810 460 L-10 460Z" fill="#6a8ac8"/>'
b+='<path d="M-10 460 Q400 430 810 460 L810 810 L-10 810Z" fill="#8ac85a"/><path d="M200 810 L390 460 L410 460 L600 810Z" fill="#c8b890"/><path d="M398 470 L402 470 L404 520 L396 520Z M396 560 L404 560 L408 640 L392 640Z M390 690 L410 690 L416 800 L384 800Z" fill="#fff"/>'
b+='<rect x="600" y="580" width="110" height="140" rx="26" fill="#e8502a"/><rect x="616" y="620" width="78" height="60" rx="12" fill="#c83a1a"/><path d="M620 580 Q655 530 690 580" stroke="#3a2a1a" stroke-width="10" fill="none"/>'
I[1176]=svg(b,d)

# 1421 思い出せなくなるその日まで: an old photograph slowly fading to white at its edges, a couple's silhouettes almost gone
d,b=bg([(0,'#3a3a4a'),(1,'#5a5a6a')])
b+='<g transform="rotate(5 400 420)"><rect x="170" y="160" width="460" height="520" fill="#fbf8f0"/>'
d+=lg('fd',S((0,'#ff9a7a'),(1,'#8a6ab8')))
b+='<rect x="200" y="190" width="400" height="400" fill="url(#fd)"/>'+figure(360,560,200,'#2a1a3a')+figure(430,560,190,'#2a1a3a',hair='#2a1a3a')
d+=rg('wh',S((0,'#fbf8f0',0),(.55,'#fbf8f0',0),(1,'#fbf8f0',1)),.5,.5,.72)
b+='<rect x="200" y="190" width="400" height="400" fill="url(#wh)"/></g>'
I[1421]=svg(b,d)

# 1492 宿命: a pitcher at full stretch on the Koshien mound, ivy-covered stands and a blazing summer sky behind
d,b=bg([(0,'#2a8ae8'),(1,'#9ad8ff')])
b+=cloud(600,170,1.2,'#fff',.95)
b+='<rect y="360" width="800" height="120" fill="#3a6a2a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="#4a8a3a"/>' for x in range(0,820,30) for y in (370,400,430,460))
b+='<rect y="480" width="800" height="320" fill="#c89a5a"/><ellipse cx="400" cy="620" rx="160" ry="40" fill="#b8884a"/>'
b+=f'<g transform="rotate(-10 400 620)">{figure(400,620,300,"#f4f4f8",pose="reach")}</g>'
b+='<circle cx="560" cy="380" r="14" fill="#fff"/><path d="M540 380 l-60 6" stroke="#fff" stroke-width="4" opacity=".6"/>'
I[1492]=svg(b,d)

# 380 ミ・アモーレ〔Meu amor é…〕: a whirl of carnival feathers in green, gold and pink, samba fireworks over Rio
d,b=bg([(0,'#1a0a3a'),(1,'#5a0a5a')])
b+=firework(600,180,110,'#ffd82a',22,1)+firework(200,160,80,'#5aff8a',18,2)
for k in range(13):
    a=-72+k*12;c=['#3ac84a','#ffd82a','#ff4ab8','#ff7a1a'][k%4]
    b+=f'<g transform="rotate({a} 400 640)"><path d="M400 640 Q370 400 400 250 Q430 400 400 640Z" fill="{c}"/><path d="M400 620 L400 270" stroke="#fff" stroke-width="3" opacity=".6"/></g>'
b+='<circle cx="400" cy="640" r="70" fill="#ffd82a"/><circle cx="400" cy="640" r="40" fill="#e8302a"/>'
I[380]=svg(b,d)

# 1493 イエスタデイ: a daily calendar with its pages flying backward through the air toward yesterday
d,b=bg([(0,'#3a4a6a'),(1,'#8a9ab8')])
b+='<rect x="250" y="300" width="300" height="340" rx="16" fill="#fff"/><rect x="250" y="300" width="300" height="80" rx="16" fill="#e8302a"/><rect x="250" y="360" width="300" height="20" fill="#e8302a"/>'
b+='<text x="400" y="560" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" font-size="170" fill="#2a2a34">昨</text>'.replace('DejaVu Sans','Noto Sans JP')
for x,y,a in [(200,200,-30),(330,120,-12),(520,160,18),(620,260,34)]:
    b+=f'<rect x="{x-60}" y="{y-70}" width="120" height="140" rx="8" fill="#fff" opacity=".85" transform="rotate({a} {x} {y})"/><rect x="{x-60}" y="{y-70}" width="120" height="28" rx="8" fill="#e8302a" opacity=".85" transform="rotate({a} {x} {y})"/>'
I[1493]=svg(b,d)

# 692 心を開いて: a door swinging open in a dark wall, warm light pouring out across the floor
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
b+='<polygon points="300,640 500,640 760,800 40,800" fill="#ffe0a0" opacity=".45"/>'
b+='<rect x="300" y="200" width="200" height="440" fill="#ffe8b0"/>'+glow(400,420,180,'#fff2c8',.7)
b+='<path d="M300 200 L190 240 L190 680 L300 640Z" fill="#7a4a2a"/><circle cx="210" cy="460" r="10" fill="#d8b050"/>'
b+='<rect x="290" y="190" width="220" height="460" fill="none" stroke="#3a2a1a" stroke-width="16"/>'
I[692]=svg(b,d)

# 693 揺れる想い: tall summer grass and a white dress swaying in the sea breeze on a bright headland
d,b=bg([(0,'#2a9ae8'),(1,'#bfe8ff')])
b+='<rect y="460" width="800" height="140" fill="#1a7ac8"/><rect y="456" width="800" height="6" fill="#fff" opacity=".6"/>'
b+='<path d="M-10 560 Q400 520 810 580 L810 810 L-10 810Z" fill="#6ab84a"/>'
r=R(693)
for _ in range(80):
    x=r.uniform(-20,820);y=r.uniform(580,800);h=r.uniform(80,180)
    b+=f'<path d="M{x:.0f} {y:.0f} Q{x+10:.0f} {y-h*.6:.0f} {x+40:.0f} {y-h:.0f}" stroke="{r.choice(["#4a9a3a","#7ac85a","#3a8a2a"])}" stroke-width="5" fill="none"/>'
b+=figure(380,640,260,'#ffffff',hair='#3a2a1a')+'<path d="M350 500 Q300 600 330 640 L440 640 Q470 600 420 500Z" fill="#fff"/><path d="M440 600 Q500 590 520 560" stroke="#fff" stroke-width="20" fill="none" stroke-linecap="round"/>'
I[693]=svg(b,d)

# 833 誘惑: a glossy red apple with a single bite taken, glowing in the dark like temptation itself
d,b=bg([(0,'#0a0a0e'),(1,'#1a0a14')])
b+=glow(400,440,220,'#ff3a4a',.35)
d+=rg('ap',S((0,'#ff7a7a'),(.5,'#d8101e'),(1,'#5a0008')),.38,.35,.7)
b+='<path d="M400 300 Q300 230 230 320 Q170 420 230 540 Q290 660 400 640 Q510 660 570 540 Q630 420 570 320 Q500 230 400 300Z" fill="url(#ap)"/>'
b+='<path d="M570 420 Q520 440 530 480 Q520 520 575 540 Q600 480 570 420Z" fill="#fff6e0"/>'
b+='<path d="M400 300 Q396 240 420 200" stroke="#4a2a1a" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M412 240 Q480 200 520 230 Q470 270 412 240Z" fill="#3a8a2a"/>'
b+='<ellipse cx="300" cy="380" rx="34" ry="20" fill="#fff" opacity=".45" transform="rotate(-40 300 380)"/>'
I[833]=svg(b,d)

# 1036 Everything: a vast night sky with stars arranged into one enormous heart above a silent sea
d,b=bg([(0,'#04061e'),(1,'#1a1a4a')])
b+=starsf(90,1036,560,'#c8d0ff')
for k in range(40):
    t=k/40*2*math.pi;x=400+16*math.sin(t)**3*14;y=320-(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))*14
    b+=glow(x,y,10,'#fff6d8',.6,'glow2')+f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#fff"/>'
b+='<rect y="600" width="800" height="200" fill="#0a0e2a"/>'+''.join(f'<rect x="{360-k*14}" y="{620+k*24}" width="{80+k*28}" height="3" fill="#fff6d8" opacity="{.5-k*.06:.2f}"/>' for k in range(7))
I[1036]=svg(b,d)

# 1291 トリセツ: an instruction manual opened to a cute diagram of a heart with arrows and labels
d,b=bg([(0,'#ffe8f0'),(1,'#ffd0e0')])
b+='<g transform="rotate(-4 400 420)"><rect x="140" y="180" width="520" height="460" rx="12" fill="#fff"/><path d="M400 180 L400 640" stroke="#e8d8e0" stroke-width="6"/>'
b+=heart(270,380,70,'#ff5a8a')
b+='<path d="M330 340 L370 300 M220 330 L190 290 M270 450 L270 500" stroke="#5a5a6a" stroke-width="4"/><circle cx="370" cy="300" r="10" fill="#5a5a6a"/><circle cx="190" cy="290" r="10" fill="#5a5a6a"/><circle cx="270" cy="500" r="10" fill="#5a5a6a"/>'
for k in range(7): b+=f'<rect x="440" y="{250+k*48}" width="{180-(k%3)*40}" height="14" rx="7" fill="#d8c8d0"/>'
b+='</g><rect x="560" y="120" width="60" height="140" fill="#ff5a8a" transform="rotate(10 590 190)"/>'
I[1291]=svg(b,d)

# 1494 ノーダウト: a magnifying glass revealing a fingerprint on a playing card, a con artist's game exposed
d,b=bg([(0,'#0a1a2a'),(1,'#1a3a4a')])
b+='<g transform="rotate(-12 340 420)"><rect x="200" y="220" width="280" height="400" rx="20" fill="#fbfbf6"/><text x="230" y="290" font-family="DejaVu Sans" font-weight="700" font-size="60" fill="#d81a2a">A</text><path d="M340 380 Q300 440 340 480 Q380 440 340 380Z M340 380 Q380 440 340 480" fill="#d81a2a"/></g>'
b+='<circle cx="490" cy="440" r="140" fill="#bfe8ff" opacity=".35"/><circle cx="490" cy="440" r="140" fill="none" stroke="#d8b050" stroke-width="22"/><rect x="580" y="560" width="40" height="200" rx="16" fill="#3a2a1a" transform="rotate(-40 600 560)"/>'
for k in range(6): b+=f'<ellipse cx="490" cy="440" rx="{20+k*16}" ry="{26+k*18}" fill="none" stroke="#3a4a5a" stroke-width="4" opacity=".7"/>'
I[1494]=svg(b,d)

# 1095 ロコローション: a bottle of suntan lotion standing in the sand of an Okinawan beach, a surfboard and hibiscus beside it
d,b=bg([(0,'#1ac8f0'),(1,'#8af0ff')])
b+='<rect y="440" width="800" height="120" fill="#0ab0d8"/><path d="M-10 540 Q400 500 810 540 L810 810 L-10 810Z" fill="#fbe8b8"/>'
b+='<g transform="rotate(14 600 500)"><ellipse cx="600" cy="480" rx="60" ry="260" fill="#ff5a3a"/><path d="M600 220 L600 740" stroke="#fff" stroke-width="10"/></g>'
b+='<rect x="320" y="440" width="130" height="230" rx="26" fill="#ffd82a"/><rect x="350" y="400" width="70" height="50" rx="10" fill="#ff7a1a"/><circle cx="385" cy="550" r="40" fill="#ff7a1a"/>'
b+=flower(190,620,90,5,'#ff2a5a','#ffd82a',12,.8)
I[1095]=svg(b,d)

# 400 あなたに会えてよかった: a big hand-tied bouquet of sunflowers and white flowers with a red ribbon, a thank-you gift
d,b=bg([(0,'#fff2d8'),(1,'#ffd8a8')])
b+=glow(400,360,220,'#ffffff',.6)
b+='<path d="M360 760 L400 440 L440 760Z" fill="#5a9a3a"/><path d="M300 560 L400 470 L500 560 L460 620 L340 620Z" fill="#f4e8d8"/>'
for x,y,s in [(400,320,90),(290,380,70),(510,370,74),(340,240,60),(470,240,60)]: b+=flower(x,y,s*1.8,14,'#ffc81a','#7a4a1a',x%30,.4)+f'<circle cx="{x}" cy="{y}" r="{s*.45}" fill="#7a4a1a"/>'
for x,y in [(230,300),(570,290),(400,180)]: b+=flower(x,y,60,6,'#fff','#ffd84a',20,.7)
b+='<path d="M360 600 Q300 660 320 700 M440 600 Q500 660 480 700" stroke="#e8203a" stroke-width="16" fill="none"/><circle cx="400" cy="600" r="22" fill="#e8203a"/>'
I[400]=svg(b,d)

# 730 HANABI: a single firework blooming over a dark sea, a lone rescue helicopter crossing beneath it
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
b+=firework(400,280,200,'#c8e0ff',36,7)+glow(400,280,80,'#ffffff',.6)
b+='<rect y="580" width="800" height="220" fill="#06102a"/>'+''.join(f'<rect x="{360-k*16}" y="{600+k*26}" width="{80+k*32}" height="3" fill="#c8e0ff" opacity="{.6-k*.08:.2f}"/>' for k in range(6))
b+='<g transform="translate(600 500)" fill="#1a2a4a"><ellipse cx="0" cy="0" rx="50" ry="22"/><rect x="40" y="-6" width="80" height="10"/><rect x="-70" y="-34" width="140" height="6"/><rect x="-4" y="-34" width="8" height="16"/><path d="M-30 22 L-36 34 L36 34 L30 22" stroke="#1a2a4a" stroke-width="5" fill="none"/></g><circle cx="610" cy="498" r="6" fill="#ff3a3a"/>'
I[730]=svg(b,d)

# 988 Dearest: two cupped hands holding a softly glowing pink jewel, petals falling in the dark
d,b=bg([(0,'#1a0a1a'),(1,'#3a1a2a')])
b+=glow(400,400,200,'#ff9ac8',.55)+petals(24,988,'#ffb8d4',0,800,8,14,.8)
d+=rg('jw',S((0,'#ffffff'),(.4,'#ffb8d8'),(1,'#e84a8a')),.4,.35,.65)
b+='<circle cx="400" cy="390" r="70" fill="url(#jw)"/>'
b+='<path d="M200 520 Q260 420 380 470 L400 560 Q300 620 200 520Z" fill="#e8c0a8"/><path d="M600 520 Q540 420 420 470 L400 560 Q500 620 600 520Z" fill="#dab098"/>'
I[988]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
