import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 17. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 941 SNOW! SNOW! SNOW!: two snowmen side by side on a lit street, heavy snow swirling, a red scarf shared between them
d,b=bg([(0,'#2a3a6a'),(1,'#5a6a9a')])
b+=snow(110,941)+'<rect y="600" width="800" height="200" fill="#eef2fa"/>'+glow(400,200,160,'#ffe8b0',.35)
for x,s in [(280,1),(520,.9)]: b+=f'<circle cx="{x}" cy="{600-60*s:.0f}" r="{90*s:.0f}" fill="#fff"/><circle cx="{x}" cy="{600-190*s:.0f}" r="{60*s:.0f}" fill="#fff"/><circle cx="{x-18*s:.0f}" cy="{600-200*s:.0f}" r="6" fill="#1a1a2a"/><circle cx="{x+18*s:.0f}" cy="{600-200*s:.0f}" r="6" fill="#1a1a2a"/><path d="M{x} {600-185*s:.0f} l26 6 l-26 6Z" fill="#ff8a2a"/>'
b+='<path d="M250 460 Q400 500 545 450" stroke="#e8102a" stroke-width="22" fill="none" stroke-linecap="round"/><path d="M400 488 L390 560 M410 488 L424 556" stroke="#e8102a" stroke-width="14" stroke-linecap="round"/>'
I[941]=svg(b,d)

# 962 vestige: a broken mech helmet half-buried in sand under two moons, a single flower growing from a crack
d,b=bg([(0,'#1a1a3a'),(.6,'#5a3a5a'),(1,'#c88a6a')])
b+=moon(600,150,46)+moon(680,230,22)+starsf(30,962,300,'#fff')+'<path d="M-10 640 Q300 580 810 630 L810 810 L-10 810Z" fill="#c8a07a"/>'
b+='<path d="M220 640 L250 420 Q300 340 400 340 Q500 340 550 420 L580 640Z" fill="#8a8aa0"/><path d="M290 470 L510 470 L490 520 L310 520Z" fill="#2a2a44"/><path d="M300 480 L500 480" stroke="#ff4a4a" stroke-width="6" opacity=".6"/><path d="M400 340 L400 260 M380 260 L420 260" stroke="#8a8aa0" stroke-width="14"/>'
b+='<path d="M430 350 L450 420 L420 470" stroke="#2a2a44" stroke-width="6" fill="none"/>'+'<path d="M440 360 Q446 320 440 300" stroke="#4a8a3a" stroke-width="5" fill="none"/>'+flower(440,296,20,5,'#fff','#ffd02a',0,.6)
I[962]=svg(b,d)

# 1369 ガラスを割れ!: a fist smashing through a pane of glass, shards flying against a dark grey background
d,b=bg([(0,'#2a2a34'),(1,'#141418')])
b+='<rect x="120" y="120" width="560" height="560" fill="#8ab8d8" opacity=".25" stroke="#c8d8e8" stroke-width="6"/>'
for a in range(0,360,30): b+=f'<path d="M400 400 L{400+300*math.cos(math.radians(a)):.0f} {400+300*math.sin(math.radians(a)):.0f}" stroke="#e8f0ff" stroke-width="3"/>'
r=R(1369)
for _ in range(18): x,y=r.uniform(100,700),r.uniform(100,700);b+=f'<polygon points="{x:.0f},{y:.0f} {x+r.uniform(10,40):.0f},{y+r.uniform(-30,10):.0f} {x+r.uniform(-10,30):.0f},{y+r.uniform(20,50):.0f}" fill="#c8e0ff" opacity=".8"/>'
b+='<g fill="#d8a888"><rect x="320" y="330" width="160" height="150" rx="40"/><rect x="360" y="470" width="90" height="340"/></g><path d="M330 370 L470 370 M330 410 L470 410 M330 450 L470 450" stroke="#b8886a" stroke-width="7"/>'
I[1369]=svg(b,d)

# 1406 愛にできることはまだあるかい: a girl praying on a Tokyo rooftop as a single patch of sunlight breaks through endless rain
d,b=bg([(0,'#4a5a7a'),(1,'#2a3448')])
b+=rain(120,1406,'#c8d8f0',.4,5)+'<polygon points="460,0 620,0 520,640 380,640" fill="#ffe8a0" opacity=".35"/>'+skyline(700,'#1a2030',1406,60,240,'#ffd27a',30)
b+='<rect x="300" y="620" width="300" height="180" fill="#2a3040"/>'+glow(450,560,110,'#ffe8a0',.5)+figure(450,630,170,'#1a1a2a',hair='#1a1a2a')
b+='<path d="M444 520 L456 520 L450 500Z" fill="#1a1a2a"/>'
I[1406]=svg(b,d)

# 1586 のびしろ: a small sapling next to a tall growth chart on a wall, chalk marks reaching far above it
d,b=bg([(0,'#f4ecd8'),(1,'#e0d4b8')])
b+='<rect x="460" y="60" width="90" height="640" fill="#fff" stroke="#c8b898" stroke-width="4"/>'+''.join(f'<path d="M460 {80+k*40} L{490 if k%5 else 520} {80+k*40}" stroke="#8a7a5a" stroke-width="3"/>' for k in range(16))
b+=''.join(f'<path d="M560 {100+k*60} l60 0" stroke="#e8302a" stroke-width="4" stroke-dasharray="6 6"/>' for k in range(3))+'<path d="M590 280 L590 100 M575 120 L590 100 L605 120" stroke="#e8302a" stroke-width="5" fill="none"/>'
b+='<rect y="700" width="800" height="100" fill="#8a6a4a"/><path d="M300 560 L280 700 L380 700 L360 560Z" fill="#c8704a"/><path d="M330 560 Q326 500 334 440" stroke="#4a8a3a" stroke-width="8" fill="none"/><path d="M332 490 Q280 470 270 440 Q310 450 332 480Z M334 460 Q390 430 400 400 Q350 410 334 450Z" fill="#6ac84a"/>'
I[1586]=svg(b,d)

# 1856 Walking with you: two silhouettes walking hand in hand down a long tree-lined path in autumn light
d,b=bg([(0,'#ffc890'),(1,'#ffe8c8')])
b+='<path d="M340 800 L390 380 L410 380 L460 800Z" fill="#d8b890"/>'
for k in range(6):
    s=1-k*.14;x1=300-k*28;x2=500+k*28;y=760-k*70
    for x in (x1,x2): b+=f'<rect x="{x-6*s:.0f}" y="{y-200*s:.0f}" width="{12*s:.0f}" height="{200*s:.0f}" fill="#5a3a2a"/><circle cx="{x}" cy="{y-220*s:.0f}" r="{70*s:.0f}" fill="#e8802a"/>'
b+=petals(30,1856,'#e8902a',100,760,8,14,.9)+figure(370,700,170,'#2a1a1a')+figure(430,700,160,'#2a1a1a',hair='#2a1a1a')+'<path d="M380 610 L420 610" stroke="#2a1a1a" stroke-width="8"/>'
I[1856]=svg(b,d)

# 794 masquerade!: an ornate Venetian mask with feathers floating above a glittering ballroom floor
d,b=bg([(0,'#2a0a3a'),(1,'#4a1a5a')])
b+=rays(400,380,24,'#ffd8ff',.15,6)+'<rect y="600" width="800" height="200" fill="#1a0a24"/>'+''.join(sparkle(r,620+(r*7)%160,8,'#ffd8ff') for r in range(40,800,70))
b+='<path d="M180 360 Q260 260 400 320 Q540 260 620 360 Q560 460 470 420 Q430 380 400 400 Q370 380 330 420 Q240 460 180 360Z" fill="#d8a838"/><path d="M250 360 Q300 330 350 360 Q300 390 250 360Z M450 360 Q500 330 550 360 Q500 390 450 360Z" fill="#1a0a24"/>'
for k,c in enumerate(['#ff4ab8','#5ae8ff','#aaff4a']): b+=f'<path d="M600 330 Q{680+k*20} {200-k*30} {640+k*40} {120-k*20}" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/>'
I[794]=svg(b,d)

# 865 叙情詩: an old leather-bound book open on a stone balcony at dusk, its pages turning into birds
d,b=bg([(0,'#3a2a5a'),(.6,'#a85a7a'),(1,'#f4b08a')])
b+='<rect y="580" width="800" height="220" fill="#8a7a7a"/>'+''.join(f'<rect x="{k*100+20}" y="500" width="40" height="80" fill="#9a8a8a"/>' for k in range(8))+'<rect y="490" width="800" height="20" fill="#aa9a9a"/>'
b+='<path d="M200 620 L400 600 L600 620 L600 700 L400 680 L200 700Z" fill="#fbf4e4"/><path d="M400 600 L400 680" stroke="#c8b898" stroke-width="4"/><path d="M190 700 L400 690 L610 700 L610 720 L190 720Z" fill="#6a3a2a"/>'
for k,(x,y,s) in enumerate([(420,520,1),(480,440,.9),(540,340,.8),(600,240,.7),(660,150,.6)]): b+=f'<path d="M{x-40*s:.0f} {y} Q{x-15*s:.0f} {y-30*s:.0f} {x} {y} Q{x+15*s:.0f} {y-30*s:.0f} {x+40*s:.0f} {y}" stroke="#fbf4e4" stroke-width="{10*s:.0f}" fill="none" stroke-linecap="round"/>'
I[865]=svg(b,d)

# 1177 Be Free: a bird bursting out of an open cage door into a bright green-and-blue sky
d,b=bg([(0,'#5ad0ff'),(1,'#d8ffd0')])
b+=cloud(600,180,1.3)+'<rect y="640" width="800" height="160" fill="#7ad86a"/>'
b+='<path d="M180 640 L180 380 Q260 300 340 380 L340 640Z" fill="none" stroke="#6a6a7a" stroke-width="6"/>'+''.join(f'<path d="M{200+k*28} 640 L{200+k*28} {360 if 1<k<4 else 390}" stroke="#6a6a7a" stroke-width="4"/>' for k in range(5))
b+='<path d="M340 460 L440 400 L440 560 L340 600Z" fill="none" stroke="#6a6a7a" stroke-width="6"/>'
b+='<g transform="translate(560 320) rotate(-20)"><ellipse rx="40" ry="26" fill="#ffd02a"/><circle cx="40" cy="-14" r="20" fill="#ffd02a"/><path d="M58 -14 L76 -10 L58 -6Z" fill="#e8802a"/><path d="M-10 -10 Q-40 -90 -100 -80 Q-60 -40 -10 4Z" fill="#ffe86a"/><path d="M-40 6 L-80 20 L-70 -4Z" fill="#e8b02a"/></g>'+sparkle(660,240,20,'#fff')
I[1177]=svg(b,d)

# 1232 復活LOVE: a withered rose blooming red again from a cracked vase, petals glowing
d,b=bg([(0,'#1a0a14'),(1,'#3a1424')])
b+=glow(400,300,200,'#ff4a6a',.35)+'<path d="M320 700 Q300 560 350 520 L450 520 Q500 560 480 700Z" fill="#5a5a7a"/><path d="M380 560 L400 620 L380 680" stroke="#1a0a14" stroke-width="5" fill="none"/>'
b+='<path d="M400 520 Q390 420 400 330" stroke="#3a6a2a" stroke-width="10" fill="none"/><path d="M396 440 Q340 420 330 390 Q370 400 396 430Z" fill="#5a8a3a"/><path d="M402 400 Q450 380 470 350 Q430 350 402 390Z" fill="#7a5a3a"/>'
b+=rose(400,280,1.4)+petals(12,1232,'#ff4a6a',120,500,8,14,.9)
I[1232]=svg(b,d)

# 1303 GIVE ME FIVE!: two raised hands meeting in a high five above a graduation stage, cherry petals and guitars
d,b=bg([(0,'#ffb0c8'),(1,'#fff0f4')])
b+=petals(30,1303,'#ff8ab0',0,800,8,14,.9)+'<rect y="620" width="800" height="180" fill="#8a5a3a"/>'
b+=guitar(160,560,1.1,-30,'#e8402a')+guitar(640,560,1.1,30,'#2a8ae8')
b+='<g fill="#e8c0a0"><rect x="280" y="300" width="100" height="120" rx="30" transform="rotate(20 330 360)"/><rect x="420" y="300" width="100" height="120" rx="30" transform="rotate(-20 470 360)"/><rect x="290" y="400" width="50" height="300" transform="rotate(20 315 550)"/><rect x="460" y="400" width="50" height="300" transform="rotate(-20 485 550)"/></g>'+rays(400,320,16,'#fff',.4,6)+sparkle(400,300,40,'#fff')
I[1303]=svg(b,d)

# 1349 僕は僕を好きになる: a girl hugging her own reflection in a mirror, a small heart glowing between them
d,b=bg([(0,'#ffe0e8'),(1,'#f4c8d8')])
b+='<rect x="400" y="80" width="300" height="620" rx="150" fill="#e8f0ff" stroke="#d8a838" stroke-width="14"/>'
b+=figure(320,720,420,'#5a3a5a',hair='#3a2a3a')+f'<g opacity=".55">'+figure(540,720,400,'#5a3a5a',hair='#3a2a3a')+'</g>'+glow(430,420,60,'#ff5a8a',.5)+heart(430,420,30,'#ff3a7a')
I[1349]=svg(b,d)

# 1602 BREAKOUT: nine silhouettes leaping out through a shattered neon wall into a burst of light
d,b=bg([(0,'#0a0a1a'),(1,'#1a0a2a')])
b+=rays(400,420,30,'#5ae8ff',.25,6)+glow(400,420,220,'#fff',.5)
r=R(1602)
for _ in range(20): x,y=r.uniform(100,700),r.uniform(200,640);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{r.uniform(20,60):.0f}" height="{r.uniform(10,30):.0f}" fill="#ff2a8a" transform="rotate({r.uniform(0,90):.0f} {x:.0f} {y:.0f})"/>'
b+='<rect y="680" width="800" height="120" fill="#06060e"/>'+''.join(figure(120+k*70,690-(k%3)*30,140,'#000',pose='up' if k%2 else 'wave') for k in range(9))
I[1602]=svg(b,d)

# 655 ゆるぎないものひとつ: a lone tree standing firm on a cliff edge as a storm bends everything else around it
d,b=bg([(0,'#3a4050'),(1,'#6a7080')])
b+=rain(80,655,'#c8d0e0',.4,4)+bolt([(120,0),(160,120),(130,140),(180,260)],'#fff6c8',6,1)
b+='<path d="M-10 800 L-10 560 L460 520 L500 800Z" fill="#2a2a30"/><rect y="700" width="800" height="100" fill="#2a3a5a"/>'
b+='<path d="M360 540 L360 300" stroke="#1a1414" stroke-width="30"/><path d="M360 380 L280 300 M360 340 L440 260 M360 420 L440 380" stroke="#1a1414" stroke-width="14" stroke-linecap="round"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#2a5a2a"/>' for x,y,r in [(360,260,80),(280,290,60),(440,250,60),(450,370,40)])
b+=''.join(f'<path d="M{560+k*50} 560 Q{600+k*50} 520 {640+k*50} 540" stroke="#4a5a4a" stroke-width="6" fill="none"/>' for k in range(4))
I[655]=svg(b,d)

# 889 これが私の生きる道: two girls on a vintage scooter cruising a winding coastal road, sun hats flapping
d,b=bg([(0,'#5ac8ff'),(1,'#d8f4ff')])
b+=hinomaru_sun(640,140,60,'#fff4c8',.9)+'<rect y="420" width="800" height="380" fill="#2a90d8"/><path d="M-10 800 Q200 600 400 620 Q600 640 810 500 L810 800Z" fill="#e8d8a0"/><path d="M-10 760 Q200 580 400 600 Q600 620 810 480" stroke="#5a5a64" stroke-width="40" fill="none"/>'
b+='<g transform="translate(400 540)"><path d="M-90 0 Q-90 -50 -40 -50 L60 -50 Q90 -50 90 0Z" fill="#ff7ab0"/><circle cx="-60" cy="10" r="30" fill="#1a1a1a"/><circle cx="60" cy="10" r="30" fill="#1a1a1a"/><path d="M80 -50 L90 -110" stroke="#5a5a64" stroke-width="8"/></g>'
b+=figure(380,500,150,'#2a1a2a',hair='#2a1a2a')+figure(330,500,140,'#2a1a2a',hair='#2a1a2a')+'<ellipse cx="380" cy="372" rx="40" ry="10" fill="#ffd02a"/><ellipse cx="330" cy="384" rx="38" ry="10" fill="#fff"/>'
I[889]=svg(b,d)

# 942 solitude: a single umbrella left open on an empty platform bench as a train pulls away in the rain
d,b=bg([(0,'#5a6a7a'),(1,'#3a4450')])
b+=rain(100,942,'#c8d4e0',.4,4)+'<rect y="560" width="800" height="240" fill="#3a3a44"/><rect y="560" width="800" height="16" fill="#ffd02a"/>'
b+='<rect x="-10" y="400" width="300" height="150" rx="20" fill="#8a9aa8"/><rect x="20" y="430" width="70" height="50" fill="#ffe8a0"/><rect x="110" y="430" width="70" height="50" fill="#ffe8a0"/><rect x="200" y="430" width="70" height="50" fill="#ffe8a0"/>'
b+='<rect x="420" y="620" width="260" height="20" fill="#5a3a2a"/><rect x="430" y="640" width="12" height="60" fill="#2a2a2a"/><rect x="660" y="640" width="12" height="60" fill="#2a2a2a"/>'+wagasa(560,560,130,'#2a5ae8',-20)
I[942]=svg(b,d)

# 1180 愛をこめて花束を: a big bouquet of white and pink flowers held out with both hands, warm golden light
d,b=bg([(0,'#ffe8c8'),(1,'#ffd0b0')])
b+=glow(400,340,260,'#fff',.5)+'<path d="M360 520 L400 760 L440 520Z" fill="#c8e0c8"/><path d="M340 520 L460 520 L420 600 L380 600Z" fill="#fff" opacity=".7"/>'
r=R(1180)
for _ in range(16): x,y=r.uniform(280,520),r.uniform(260,500);b+=flower(x,y,r.uniform(26,40),6,r.choice(['#fff','#ffb0c8','#ff7aa8','#fff0f4']),'#ffd02a',r.uniform(0,60),.6)
b+='<g fill="#e8c0a0"><rect x="320" y="600" width="80" height="60" rx="26"/><rect x="400" y="600" width="80" height="60" rx="26"/></g><path d="M370 560 Q400 590 430 560" stroke="#e8302a" stroke-width="10" fill="none"/>'
I[1180]=svg(b,d)

# 1233 I'll be there: a lit window in a tall apartment building at night, a silhouette waving from below with a lantern
d,b=bg([(0,'#0a1438'),(1,'#1a2a5a')])
b+=starsf(40,1233,300,'#fff')+'<rect x="420" y="120" width="300" height="680" fill="#1a1a2a"/>'+''.join(f'<rect x="{450+(k%4)*64}" y="{160+(k//4)*80}" width="40" height="50" fill="{"#ffd27a" if k==9 else "#2a2a3a"}"/>' for k in range(28))+glow(534,345,70,'#ffd27a',.5)
b+='<rect y="700" width="800" height="100" fill="#0a0a14"/>'+figure(220,710,200,'#000',pose='wave')+glow(270,620,40,'#ffd27a',.7)+'<rect x="262" y="604" width="16" height="26" fill="#ffd27a"/>'
I[1233]=svg(b,d)

# 1268 無責任ヒーロー: a cartoonish caped hero napping in a hammock while a cat rescues itself from a tree
d,b=bg([(0,'#5ab8ff'),(1,'#d8f0ff')])
b+=cloud(160,140,1)+'<rect y="620" width="800" height="180" fill="#6ac85a"/>'
b+='<path d="M100 620 L100 340 M700 620 L700 340" stroke="#5a3a1a" stroke-width="18"/><path d="M100 400 Q400 560 700 400" stroke="#e8c88a" stroke-width="10" fill="none"/><path d="M110 410 Q400 580 690 410 Q400 520 110 410Z" fill="#e8402a"/>'
b+='<ellipse cx="400" cy="470" rx="120" ry="34" fill="#2a5ae8"/><circle cx="270" cy="450" r="30" fill="#e8c0a0"/><rect x="250" y="438" width="40" height="10" fill="#1a1a1a"/><text x="250" y="390" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="40" fill="#fff">z z</text>'
b+='<path d="M700 300 Q760 260 790 300" stroke="#5a3a1a" stroke-width="12" fill="none"/><g transform="translate(740 270)"><ellipse rx="22" ry="16" fill="#ff9a2a"/><circle cx="20" cy="-14" r="12" fill="#ff9a2a"/><path d="M12 -24 L16 -34 L22 -24 M24 -24 L30 -32 L32 -22" fill="#ff9a2a"/></g>'
I[1268]=svg(b,d)

# 1304 君はメロディー: a music box with a tiny dancer, notes floating up into a pastel sky
d,b=bg([(0,'#c8d8ff'),(1,'#ffe8f4')])
b+='<rect x="240" y="480" width="320" height="200" rx="10" fill="#c8704a"/><rect x="240" y="480" width="320" height="30" fill="#a85a3a"/><path d="M240 480 L270 300 L590 300 L560 480Z" fill="#d88a5a"/><rect x="290" y="320" width="240" height="140" fill="#ffd8e8"/>'
b+='<ellipse cx="400" cy="480" rx="40" ry="10" fill="#d8a838"/>'+figure(400,480,100,'#ff7ab0',pose='up',hair='#5a3a2a')
b+=''.join(note(300+k*60,260-k*40,18,['#ff5a8a','#5a8aff','#a85aff','#ff8a2a'][k%4],k%2==0) for k in range(5))
I[1304]=svg(b,d)

# 1350 Same numbers: a digital clock showing 22:22 on a bedside table, a hand reaching to make a wish
d,b=bg([(0,'#1a1a3a'),(1,'#2a2a4a')])
b+=glow(400,380,200,'#5ae8ff',.25)+'<rect y="560" width="800" height="240" fill="#3a2a2a"/><rect x="220" y="300" width="360" height="260" rx="30" fill="#141420"/><text x="400" y="470" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-weight="bold" font-size="110" fill="#5ae8ff">22:22</text>'
b+='<g fill="#e8c0a0"><rect x="600" y="440" width="200" height="60" rx="26"/><rect x="580" y="430" width="40" height="22" rx="10"/></g>'+''.join(sparkle(x,y,10,'#fff') for x,y in [(200,240),(600,220),(400,200)])
I[1350]=svg(b,d)

# 1439 crossing field: a lone swordsman silhouette on a glowing digital grid floor stretching to the horizon
d,b=bg([(0,'#0a1a4a'),(1,'#1a3a8a')])
b+=starsf(50,1439,400,'#c8e8ff')+'<rect y="440" width="800" height="360" fill="#0a1430"/>'
for k in range(12): b+=f'<path d="M400 440 L{-400+k*145} 800" stroke="#3ab8ff" stroke-width="2" opacity=".7"/>'
for k in range(7): b+=f'<path d="M0 {460+k*k*8} L800 {460+k*k*8}" stroke="#3ab8ff" stroke-width="2" opacity=".6"/>'
b+=figure(400,660,240,'#000')+'<path d="M440 520 L560 380" stroke="#c8f0ff" stroke-width="8"/>'+glow(560,380,30,'#c8f0ff',.8)
I[1439]=svg(b,d)

# 1440 紅蓮華: a crimson lotus bursting into flame in a night forest, petals of fire scattering
d,b=bg([(0,'#1a0408'),(1,'#2a0a0a')])
for x in range(40,800,90): b+=f'<path d="M{x} 800 L{x+30} 320 L{x+60} 800Z" fill="#0a1a10"/>'
b+=glow(400,480,220,'#ff3a1a',.5)
for a in range(-75,76,25): b+=f'<path d="M400 560 Q{400+a*1.6:.0f} 460 {400+a*2.4:.0f} {400+abs(a)*.8:.0f} Q{400+a*.9:.0f} 500 400 560Z" fill="#e8102a"/>'
b+='<path d="M400 520 Q370 440 400 360 Q430 440 400 520Z" fill="#ffa83a"/>'+petals(18,1440,'#ff5a2a',200,600,8,14,.9)
I[1440]=svg(b,d)

# 1603 STARS: nine stars connected into a constellation over a snowy mountain, each glowing a different colour
d,b=bg([(0,'#04061e'),(1,'#1a2a5a')])
b+=starsf(60,1603,600,'#fff')+'<path d="M-10 800 L200 520 L320 620 L480 460 L810 720 L810 800Z" fill="#e8eef8"/>'
P=[(140,160),(240,120),(340,190),(420,110),(520,170),(600,100),(680,180),(560,280),(300,300)]
b+='<path d="'+'M'+' L'.join(f'{x} {y}' for x,y in P)+'" stroke="#c8d8ff" stroke-width="2" fill="none" opacity=".6"/>'
for (x,y),c in zip(P,['#ff5a8a','#ffd02a','#5ae8ff','#aaff5a','#fff','#c85aff','#ff8a2a','#5a8aff','#ff5a5a']): b+=glow(x,y,26,c,.7)+star5(x,y,14,c)
I[1603]=svg(b,d)

# 1608 Imitation Rain: a neon-lit city street where the falling rain is made of glowing pixels, a figure with a transparent umbrella
d,b=bg([(0,'#0a0a1a'),(1,'#1a0a2a')])
b+=skyline(520,'#14102a',1608,80,320,'#ff5ab8',60)+'<rect y="520" width="800" height="280" fill="#141020"/>'
r=R(1608)
for _ in range(120): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="4" height="12" fill="{r.choice(["#5ae8ff","#ff5ab8","#c8a8ff"])}" opacity=".7"/>'
b+=figure(400,700,220,'#000')+'<path d="M300 480 Q400 380 500 480Z" fill="#c8e8ff" opacity=".35" stroke="#fff" stroke-width="3"/><path d="M400 430 L400 560" stroke="#fff" stroke-width="3"/>'
I[1608]=svg(b,d)

# 227 糸: two threads, one blue and one red, weaving across a loom into a single piece of cloth
d,b=bg([(0,'#f4ece0'),(1,'#e0d4c4')])
b+='<rect x="140" y="420" width="520" height="300" fill="#fff8f0"/>'+''.join(f'<path d="M{160+k*20} 420 L{160+k*20} 720" stroke="#e8dcc8" stroke-width="3"/>' for k in range(26))
for k in range(8): b+=f'<path d="M140 {440+k*36} L660 {440+k*36}" stroke="{"#2a5ae8" if k%2 else "#e8102a"}" stroke-width="10" opacity=".85"/>'
b+='<path d="M80 80 Q240 260 140 440" stroke="#2a5ae8" stroke-width="10" fill="none"/><path d="M720 80 Q560 260 660 440" stroke="#e8102a" stroke-width="10" fill="none"/>'+heart(400,300,30,'#e8102a')
I[227]=svg(b,d)

# 288 ピースとハイライト: a peace-sign hand raised against a bright spotlight, doves flying across it
d,b=bg([(0,'#5ab0ff'),(1,'#e8f6ff')])
b+=rays(400,300,24,'#fff',.4,10)+glow(400,300,160,'#fff',.6)
b+='<g fill="#e8c0a0"><rect x="330" y="420" width="140" height="160" rx="40"/><rect x="360" y="560" width="90" height="260"/><rect x="340" y="220" width="40" height="220" rx="20" transform="rotate(-12 360 430)"/><rect x="420" y="220" width="40" height="220" rx="20" transform="rotate(12 440 430)"/></g>'
for x,y,s in [(170,200,1),(620,180,.9),(660,320,.7)]: b+=f'<path d="M{x-50*s:.0f} {y} Q{x-20*s:.0f} {y-40*s:.0f} {x} {y} Q{x+20*s:.0f} {y-40*s:.0f} {x+50*s:.0f} {y} Q{x} {y+20*s:.0f} {x-50*s:.0f} {y}Z" fill="#fff"/>'
I[288]=svg(b,d)

# 334 悲しみがとまらない: a woman alone at a seaside café table at night, a phone face down and a melting ice drink
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+=starsf(30,334,300,'#fff')+'<rect y="360" width="800" height="200" fill="#0a2a5a"/>'+''.join(f'<rect x="{(k*131)%760}" y="{380+k*14}" width="40" height="3" fill="#5ae8ff" opacity=".5"/>' for k in range(10))
b+='<rect y="560" width="800" height="240" fill="#1a1a2a"/><ellipse cx="560" cy="600" rx="150" ry="30" fill="#e8e8f0"/><rect x="552" y="600" width="16" height="160" fill="#c8c8d0"/>'
b+='<path d="M580 520 L620 520 L612 590 L588 590Z" fill="#8ad0ff" opacity=".7"/><rect x="592" y="540" width="16" height="12" fill="#fff"/><path d="M610 520 L640 470" stroke="#ff5ab8" stroke-width="4"/><rect x="470" y="590" width="60" height="14" rx="4" fill="#1a1a1a"/>'
b+=figure(300,800,380,'#06081a',hair='#06081a')
I[334]=svg(b,d)

# 548 FU-JI-TSU: a broken heart-shaped pendant on a chain dangling from a hand, one half slipping away
d,b=bg([(0,'#3a0a2a'),(1,'#1a0414')])
b+=glow(400,420,200,'#ff3a8a',.3)+'<path d="M400 60 L400 300" stroke="#d8d8e0" stroke-width="4" stroke-dasharray="6 4"/><g fill="#e8c0a0"><rect x="340" y="20" width="120" height="60" rx="26"/></g>'
b+='<path d="M400 360 C340 300 300 300 300 350 C300 400 350 430 400 480 L380 420 L410 380Z" fill="#e8102a"/><g transform="translate(60 80) rotate(25 400 400)"><path d="M400 360 C460 300 500 300 500 350 C500 400 450 430 400 480 L420 420 L390 380Z" fill="#c80a1a"/></g>'
I[548]=svg(b,d)

# 656 FIREBALL: a blazing fireball streaking down across a night sky over a desert highway
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a1a')])
b+=starsf(40,656,400,'#fff')+'<path d="M80 60 L520 380" stroke="url(#fb)" stroke-width="60" stroke-linecap="round"/>'
d+=lg('fb',S((0,'#ff5a1a',0),(1,'#ffd02a',1)),0,0,1,1)
b+=glow(540,400,120,'#ffa82a',.8)+'<circle cx="540" cy="400" r="60" fill="#fff4c8"/>'+'<rect y="580" width="800" height="220" fill="#3a2418"/><path d="M360 580 L440 580 L700 800 L100 800Z" fill="#2a2a2a"/><path d="M400 600 L400 800" stroke="#ffd02a" stroke-width="8" stroke-dasharray="30 30"/>'
I[656]=svg(b,d)

# 657 juice: a glass of orange juice exploding with splashes and citrus slices, energetic sunburst
d,b=bg([(0,'#ffd02a'),(1,'#ff8a1a')])
b+=rays(400,420,24,'#fff',.3,8)+'<path d="M290 300 L510 300 L480 720 L320 720Z" fill="#fff" opacity=".5"/><path d="M300 380 L500 380 L478 712 L322 712Z" fill="#ff9a1a"/>'
for x,y in [(240,300),(560,280),(420,200)]: b+=f'<circle cx="{x}" cy="{y}" r="50" fill="#ff8a1a"/><circle cx="{x}" cy="{y}" r="42" fill="#ffd060"/>'+''.join(f'<path d="M{x} {y} L{x+40*math.cos(math.radians(a)):.0f} {y+40*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="3"/>' for a in range(0,360,45))
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffb03a"/>' for x,y,r in [(300,340,14),(520,330,12),(350,280,8),(470,260,10)])
I[657]=svg(b,d)

# 741 HERO: a father silhouette lifting a small child high up onto his shoulders against a sunrise
d,b=bg([(0,'#5a8ad8'),(.6,'#ffb07a'),(1,'#ffe0b0')])
b+=hinomaru_sun(400,560,120,'#fff4d0',.8)+'<rect y="620" width="800" height="180" fill="#3a2a3a"/>'
b+=figure(400,640,320,'#1a1020')+figure(400,370,120,'#1a1020',pose='up')
I[741]=svg(b,d)

# 816 風の詩を聴かせて: a woman with closed eyes and flowing hair on a grassy hill, wind lines carrying musical notes
d,b=bg([(0,'#8ac8ff'),(1,'#e8f8ff')])
b+='<path d="M-10 620 Q400 520 810 600 L810 810 L-10 810Z" fill="#7ac86a"/>'+''.join(f'<path d="M-10 {200+k*80} Q300 {170+k*80} 500 {210+k*80} T810 {190+k*80}" stroke="#fff" stroke-width="4" fill="none" opacity=".7"/>' for k in range(4))
b+=figure(300,600,300,'#2a2a3a',hair='#2a2a3a')+'<path d="M300 320 Q380 300 460 330 Q400 340 360 360Z" fill="#2a2a3a"/>'+''.join(note(480+k*70,280+(k%2)*60,16,'#3a5a8a',k%2==0) for k in range(4))
I[816]=svg(b,d)

# 1003 fairyland: a tiny glowing fairy door in the roots of a giant tree, sparkles leading inside
d,b=bg([(0,'#1a3a2a'),(1,'#0a1a14')])
b+='<path d="M200 800 Q240 600 260 0 L540 0 Q560 600 600 800Z" fill="#3a2a1a"/><path d="M200 800 Q120 760 60 800 M600 800 Q680 760 740 800" stroke="#3a2a1a" stroke-width="40" fill="none"/>'
b+='<path d="M340 800 L340 640 Q400 580 460 640 L460 800Z" fill="#ffd88a"/>'+glow(400,700,140,'#ffd88a',.6)+'<circle cx="440" cy="720" r="7" fill="#8a5a2a"/>'
b+=''.join(sparkle(x,y,s,'#fff8c8') for x,y,s in [(300,560,14),(500,520,12),(420,460,10),(250,420,8),(560,400,9),(380,360,7)])+''.join(flower(x,780,18,5,c,'#ffd02a',0,.6) for x,c in [(150,'#ff8ab8'),(660,'#a8c8ff'),(720,'#ffd02a')])
I[1003]=svg(b,d)

# 1004 glitter: a disco-glitter high heel on a dance floor, sparkles bursting under a mirrorball
d,b=bg([(0,'#2a0a3a'),(1,'#ff5ab8')])
b+='<circle cx="400" cy="140" r="80" fill="#c8c8e0"/>'+''.join(f'<rect x="{330+(k%8)*18}" y="{70+(k//8)*18}" width="15" height="15" fill="#fff" opacity="{.3+(k*7%5)*.15:.2f}"/>' for k in range(64) if (330+(k%8)*18+8-400)**2+(70+(k//8)*18+8-140)**2<76**2)+rays(400,140,20,'#fff',.15,4)
b+='<path d="M220 620 Q300 420 460 460 L600 520 L600 560 L470 540 Q380 540 330 620Z" fill="#ffd02a"/><path d="M560 540 L580 700 L600 700 L600 540Z" fill="#ffd02a"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(300,520,16),(420,480,12),(520,500,10),(360,580,8),(650,420,20)])
I[1004]=svg(b,d)

# 1047 僕は君に恋をする: a boy holding an umbrella over a girl under falling cherry blossoms, his own shoulder getting wet
d,b=bg([(0,'#ffd0e0'),(1,'#fff4f8')])
b+=petals(40,1047,'#ff8ab0',0,800,8,14,.9)+rain(40,1047,'#c8d8ff',.3,4)+'<rect y="660" width="800" height="140" fill="#c8a8b8"/>'
b+=figure(340,690,280,'#3a2a3a')+figure(460,690,250,'#5a3a4a',hair='#5a3a4a')+wagasa(430,380,170,'#2a5ae8',10)
I[1047]=svg(b,d)

# 1146 奏: a boy waving goodbye at a train station as the train doors close, a girl's hand on the glass
d,b=bg([(0,'#ffb07a'),(1,'#ffe0c0')])
b+='<rect y="560" width="800" height="240" fill="#8a8a94"/><rect y="560" width="800" height="16" fill="#ffd02a"/>'
b+='<rect x="380" y="200" width="460" height="360" rx="30" fill="#e8eef4"/><rect x="420" y="260" width="140" height="160" fill="#8ab8d8"/><rect x="600" y="260" width="140" height="160" fill="#8ab8d8"/><rect x="380" y="480" width="460" height="20" fill="#2a8a4a"/>'
b+=figure(500,420,130,'#2a3a5a',hair='#2a3a5a')+'<rect x="470" y="300" width="22" height="34" rx="10" fill="#e8c0a0"/>'+figure(220,740,260,'#1a1a2a',pose='wave')
I[1146]=svg(b,d)

# 1305 Beginner: a pair of new sneakers stepping onto a starting line drawn in chalk on an empty track
d,b=bg([(0,'#8ad8ff'),(1,'#e0f6ff')])
b+='<rect y="440" width="800" height="360" fill="#d8603a"/>'+''.join(f'<path d="M{-200+k*200} 800 L{300+k*50} 440" stroke="#fff" stroke-width="5"/>' for k in range(5))+'<path d="M0 600 L800 560" stroke="#fff" stroke-width="20"/>'
for x in (300,460): b+=f'<path d="M{x} 640 Q{x} 580 {x+40} 580 L{x+110} 610 Q{x+130} 630 {x+110} 650 L{x} 650Z" fill="#fff"/><path d="M{x} 650 L{x+120} 650" stroke="#2a5ae8" stroke-width="10"/>'
I[1305]=svg(b,d)

# 1351 気づいたら片想い: a girl gazing at a boy's back far ahead on a long school corridor lit by afternoon sun
d,b=bg([(0,'#ffe8c0'),(1,'#f4d8a8')])
b+='<path d="M0 0 L300 300 L500 300 L800 0Z" fill="#fff4e0"/><path d="M0 800 L300 520 L500 520 L800 800Z" fill="#c8a880"/><path d="M0 0 L300 300 L300 520 L0 800Z" fill="#e8d4b0"/><path d="M800 0 L500 300 L500 520 L800 800Z" fill="#f4e4c4"/>'
b+=''.join(f'<polygon points="{560+k*60},{220-k*60} {600+k*80},{180-k*60} {600+k*80},{600+k*60} {560+k*60},{580+k*40}" fill="#fff" opacity=".4"/>' for k in range(3))
b+=figure(400,520,90,'#2a2a3a')+figure(220,800,380,'#3a2a3a',hair='#3a2a3a')+heart(300,460,16,'#ff5a8a')
I[1351]=svg(b,d)

# 1628 街灯: a single streetlight glowing on an empty night street, a figure leaning against it looking up
d,b=bg([(0,'#0a1028'),(1,'#1a1a3a')])
b+=starsf(40,1628,400,'#c8d8ff')+'<rect y="640" width="800" height="160" fill="#14141e"/><rect x="420" y="160" width="14" height="490" fill="#2a2a34"/><path d="M434 170 Q500 150 520 200" stroke="#2a2a34" stroke-width="12" fill="none"/>'
b+='<polygon points="520,210 380,660 680,660" fill="#ffe8a0" opacity=".2"/>'+glow(520,210,60,'#ffe8a0',.8)+'<ellipse cx="520" cy="660" rx="160" ry="24" fill="#ffe8a0" opacity=".25"/>'+figure(470,650,200,'#000')
I[1628]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
