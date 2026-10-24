import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 2. csoport (Top 21–40)
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 21 La Maladie d'amour: a rain of arrow-pierced hearts falls on a crowd of all ages, the sweet sickness strikes everyone
d,b=bg([(0,'#ff8aa8'),(.6,'#d84a7a'),(1,'#6a1a4a')])
r=R(21)
for k in range(14):
    x,y,s=r.uniform(60,740),r.uniform(80,420),r.uniform(20,40);b+=heart(x,y,s,'#ffe0ea')
    b+=f'<path d="M{x-s*1.6:.0f} {y-s*.6:.0f} L{x+s*1.6:.0f} {y+s*.6:.0f}" stroke="#5a1030" stroke-width="4"/><path d="M{x+s*1.6:.0f} {y+s*.6:.0f} l-12 -10 l2 14Z" fill="#5a1030"/>'
b+='<rect y="640" width="800" height="160" fill="#4a1030"/>'
for x,h,p in [(120,200,'stand'),(220,130,'up'),(330,240,'wave'),(450,170,'hold'),(560,250,'stand'),(680,120,'up')]: b+=figure(x,660,h,'#2a0618',pose=p)
I[21]=svg(b,d)

# 22 Ne me quitte pas: a man on his knees begs a woman walking away into a door of light, his shadow stretching after her
d,b=bg([(0,'#0a0a10'),(1,'#1e1a24')])
b+='<rect x="470" y="140" width="210" height="520" fill="#fff4dc"/>'+glow(575,400,220,'#fff0c8',.4)
b+='<polygon points="470,660 680,660 800,800 300,800" fill="#fff0c8" opacity=".25"/>'
b+=figure(560,660,300,'#0a0806',hair='#0a0806')
b+='<path d="M536 450 Q560 660 586 450Z" fill="#0a0806"/>'
b+='<rect y="660" width="800" height="140" fill="#14101a"/>'
b+='<g transform="translate(250 700)"><ellipse cx="0" cy="-200" rx="22" ry="26" fill="#000"/><path d="M-30 -176 Q0 -184 30 -176 L26 -90 L-26 -90Z" fill="#000"/><path d="M-26 -94 L30 -94 L70 -40 L60 0 L-40 0 L-30 -60Z" fill="#000"/>'
b+='<path d="M26 -170 Q100 -170 170 -200" stroke="#000" stroke-width="15" fill="none" stroke-linecap="round"/><path d="M-26 -170 Q20 -130 60 -140" stroke="#000" stroke-width="15" fill="none" stroke-linecap="round"/></g>'
b+='<path d="M200 712 Q400 760 520 680" stroke="#000" stroke-width="50" opacity=".5" fill="none" stroke-linecap="round"/>'
I[22]=svg(b,d)

# 23 Au DD: two brothers sit at the very top of the Eiffel Tower at night, legs dangling over the glittering city
d,b=bg([(0,'#020818'),(.6,'#0a2048'),(1,'#1a3a70')])
b+=starsf(60,23,400)+moon(640,140,40,'#e8f0ff')
b+=skyline(780,'#06102a',23,20,90,'#ffd36a',160)
b+='<g transform="translate(400 900) scale(1.0)">'+eiffel(0,0,1100,'#0a1430','#ff4a4a').replace('<g fill','<g fill')+'</g>'
b+='<rect x="320" y="300" width="160" height="18" fill="#0a1430"/>'
for x in (360,440):
    b+=f'<ellipse cx="{x}" cy="230" rx="17" ry="20" fill="#000"/><path d="M{x-24} 248 Q{x} 240 {x+24} 248 L{x+20} 304 L{x-20} 304Z" fill="#000"/><path d="M{x-12} 304 L{x-16} 370 M{x+12} 304 L{x+18} 368" stroke="#000" stroke-width="12" stroke-linecap="round"/>'
b+=glow(400,300,120,'#3a8aff',.2)
I[23]=svg(b,d)

# 24 Est-ce que tu m'aimes ?: a hand plucks the petals of a big daisy, petals drifting away, a question still unanswered
d,b=bg([(0,'#2a1a4a'),(.6,'#6a2a6a'),(1,'#c84a6a')])
b+=glow(400,380,220,'#ffd0e0',.3)
for k in range(13):
    if k in (2,5,9): continue
    a=k*360/13;b+=f'<ellipse cx="400" cy="250" rx="34" ry="110" fill="#fbf6ee" transform="rotate({a} 400 360)"/>'
b+='<circle cx="400" cy="360" r="62" fill="#ffc81a"/><circle cx="400" cy="360" r="62" fill="url(#vig)" opacity=".2"/>'
b+='<path d="M400 420 Q420 600 380 800" stroke="#3a8a3a" stroke-width="12" fill="none"/>'
r=R(24)
for k in range(5):
    x,y,a=r.uniform(80,720),r.uniform(500,760),r.uniform(0,180);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="16" ry="48" fill="#fbf6ee" opacity=".85" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+=f'<text x="640" y="200" text-anchor="middle" {F} font-size="120" fill="#ffe0ea">?</text>'
I[24]=svg(b,d)

# 25 En chantant: a man strolls singing down a sunny country road, musical notes trailing behind him like birds
d,b=bg([(0,'#7ac8f0'),(.6,'#c8e8f0'),(1,'#f8e8b0')])
b+=sun(150,150,50,'#fff4a0')
b+=hills(480,40,'#8ac06a',25,4)+hills(560,30,'#5a9a4a',26,3)
b+='<path d="M360 800 Q420 640 520 520 L560 520 Q500 640 520 800Z" fill="#e8d0a0"/>'
for x in (90,680): b+=tree(x,560,200,'#2a5a2a',x)
b+=figure(430,720,300,'#2a1a1a',pose='wave')
for k,(x,y) in enumerate([(500,380),(560,320),(620,280),(680,230),(730,180)]): b+=note(x,y,22+k*2,'#2a3a6a',k%2==0)
I[25]=svg(b,d)

# 26 Aline: her name drawn in the sand of a lonely beach under a stormy sky, a wave about to wash it away
d,b=bg([(0,'#3a4a5a'),(.5,'#6a7a8a'),(1,'#d8c8a8')])
b+=glow(600,200,140,'#fff4dc',.3)
b+=waves(420,'#3a5a6a',14,8)+waves(450,'#4a6a7a',10,6)
b+='<path d="M-10 560 Q200 520 400 540 Q600 560 810 520 L810 800 L-10 800Z" fill="#e8d4a8"/>'
b+='<path d="M-10 560 Q200 520 400 540 Q600 560 810 520 L810 580 Q600 600 400 590 Q200 570 -10 610Z" fill="#fff" opacity=".7"/>'
b+=f'<text x="400" y="720" text-anchor="middle" {F} font-size="120" fill="none" stroke="#a88a5a" stroke-width="7" letter-spacing="8">ALINE</text>'
b+=figure(130,640,180,'#2a2a30')
for x,y in [(520,160),(560,190)]: b+=bird(x,y,14,'#2a3040')
I[26]=svg(b,d)

# 27 Aïcha: a veiled woman on golden desert dunes at sunset, a man's hands offer her pearls and gold she refuses
d,b=bg([(0,'#ff9a3a'),(.5,'#e8603a'),(1,'#6a1a3a')])
b+=sun(560,330,90,'#ffe07a')
b+='<path d="M-10 520 Q200 440 420 500 Q620 560 810 470 L810 800 L-10 800Z" fill="#d89040"/><path d="M-10 640 Q300 560 520 640 Q680 700 810 640 L810 800 L-10 800Z" fill="#b8702a"/>'
b+=figure(470,680,330,'#2a0a1a',hair='#2a0a1a')
b+='<path d="M440 360 Q470 330 500 360 L530 680 L410 680Z" fill="#2a0a1a"/>'
b+='<path d="M80 520 Q160 470 250 500" stroke="#c89070" stroke-width="36" fill="none" stroke-linecap="round"/>'
for k in range(9): b+=f'<circle cx="{200+k*16}" cy="{466+((k-4)**2)*2}" r="7" fill="#fff6e8"/>'
b+='<circle cx="300" cy="500" r="20" fill="none" stroke="#ffd23f" stroke-width="8"/>'
I[27]=svg(b,d)

# 28 La vie qu'on mène: a young man in a hoodie on the rooftop of a housing tower at night, the city glowing far below
d,b=bg([(0,'#04060e'),(.6,'#0e1a30'),(1,'#2a2a48')])
b+=starsf(40,28,300)
b+=skyline(640,'#0a1020',28,40,200,'#ffd36a',130)
b+='<rect x="120" y="420" width="560" height="400" fill="#141822"/>'
for i in range(7):
    for j in range(5): b+=f'<rect x="{150+i*76}" y="{470+j*66}" width="40" height="30" fill="{"#ffd36a" if (i*3+j)%4==0 else "#222838"}"/>'
b+=figure(400,424,230,'#000')
b+='<path d="M372 168 Q400 140 428 168 L432 210 L368 210Z" fill="#000"/>'
b+=glow(400,420,240,'#ff8a3a',.12)
I[28]=svg(b,d)

# 29 La Bohème: a young painter at his easel in a Montmartre garret, the white Sacré-Cœur glowing through the window
d,b=bg([(0,'#2a1a14'),(1,'#4a2a1a')])
b+='<rect x="380" y="100" width="340" height="360" fill="#ffd8a0"/><rect x="380" y="100" width="340" height="360" fill="none" stroke="#1a0e08" stroke-width="18"/><path d="M550 100 L550 460 M380 280 L720 280" stroke="#1a0e08" stroke-width="12"/>'
b+='<path d="M400 440 L400 360 L470 340 L470 300 Q520 230 570 300 L570 340 Q600 300 640 330 L640 360 L700 360 L700 440Z" fill="#fff6e8"/><circle cx="520" cy="292" r="10" fill="#fff6e8"/><path d="M518 250 L522 230" stroke="#fff6e8" stroke-width="5"/>'
b+='<path d="M140 760 L200 420 M300 760 L240 420 M220 760 L220 520" stroke="#6a4a2a" stroke-width="12"/><rect x="150" y="380" width="160" height="200" fill="#f6efe2"/>'
b+='<path d="M170 540 Q200 460 240 500 Q270 430 290 470" stroke="#d8342c" stroke-width="8" fill="none"/><circle cx="210" cy="430" r="18" fill="#2a6ad0"/>'
b+=figure(420,780,300,'#0a0604',pose='reachL')
b+='<path d="M380 470 Q420 440 470 470 L456 482 L392 482Z" fill="#0a0604"/>'
I[29]=svg(b,d)

# 30 J't'emmène au vent: a fiddle and a red scarf swept along by the wind with autumn leaves over open fields
d,b=bg([(0,'#5a8ab0'),(.6,'#a8c8d8'),(1,'#e8d8b0')])
b+=hills(600,30,'#8a9a5a',30,4)+'<rect y="640" width="800" height="160" fill="#6a7a3a"/>'
b+='<g transform="translate(400 380) rotate(-30)"><path d="M0 -150 C55 -150 60 -100 40 -70 C70 -50 80 0 50 30 C85 60 80 140 0 150 C-80 140 -85 60 -50 30 C-80 0 -70 -50 -40 -70 C-60 -100 -55 -150 0 -150Z" fill="#a8501a"/>'
b+='<path d="M-10 -40 Q-26 -20 -10 0 M10 -40 Q26 -20 10 0" stroke="#2a0e04" stroke-width="5" fill="none"/><rect x="-12" y="-330" width="24" height="190" fill="#2a0e04"/><circle cx="0" cy="-340" r="20" fill="#2a0e04"/>'
b+=''.join(f'<path d="M{-6+k*4} -320 L{-6+k*4} 100" stroke="#f0e6d0" stroke-width="1.4"/>' for k in range(4))+'</g>'
b+='<path d="M260 190 Q380 160 470 210 Q560 260 700 200 L710 230 Q560 300 470 250 Q370 200 270 220Z" fill="#d8342c"/>'
r=R(30)
for k in range(12):
    x,y,a=r.uniform(40,760),r.uniform(80,620),r.uniform(0,360);b+=f'<path transform="translate({x:.0f} {y:.0f}) rotate({a:.0f})" d="M0 -14 Q12 0 0 14 Q-12 0 0 -14Z" fill="{r.choice(["#d8742a","#e8a83a","#b8401a"])}"/>'
I[30]=svg(b,d)

# 31 Je te promets: an engagement ring with a sparkling diamond held up against a starry night, a promise for ever
d,b=bg([(0,'#0a0a24'),(.6,'#1a1a4a'),(1,'#3a1a4a')])
b+=starsf(90,31,800)
b+=glow(400,300,120,'#cfe0ff',.45)
b+='<ellipse cx="400" cy="470" rx="140" ry="150" fill="none" stroke="#ffd23f" stroke-width="30"/><ellipse cx="400" cy="470" rx="140" ry="150" fill="none" stroke="#fff4b0" stroke-width="6" opacity=".6"/>'
b+='<path d="M340 310 L370 270 L430 270 L460 310 L400 380Z" fill="#dff0ff"/><path d="M340 310 L460 310 M370 270 L400 380 L430 270" stroke="#9ab8e0" stroke-width="3" fill="none"/>'
b+=sparkle(460,260,30,'#fff')+sparkle(330,280,16,'#fff',.8)
I[31]=svg(b,d)

# 32 Balance ton quoi: a young woman shouts into a megaphone, sound waves blasting away the sexist cliches
d,b=bg([(0,'#ffc0d8'),(.6,'#ff7ab0'),(1,'#d83a7a')])
b+=figure(250,780,440,'#3a0a2a',pose='reach',hair='#3a0a2a')
b+='<path d="M380 330 L560 240 L560 460 L380 370Z" fill="#fff"/><rect x="350" y="320" width="40" height="60" rx="8" fill="#fff"/><path d="M392 380 L410 440" stroke="#fff" stroke-width="16" stroke-linecap="round"/>'
for k in range(3): b+=f'<path d="M{600+k*50} {250-k*25} Q{640+k*60} 350 {600+k*50} {450+k*25}" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity="{.9-k*.25}"/>'
I[32]=svg(b,d)

# 33 Ego: a dancer looks in a mirror and sees himself crowned like a king, disco lights flashing
d,b=bg([(0,'#1a0a3a'),(.6,'#3a0a6a'),(1,'#7a1a8a')])
b+=stage_lights(3,40,['#ff2a8a','#2ad0ff','#ffd23f'],.12)
b+='<rect x="430" y="160" width="300" height="540" rx="150" fill="#9ad0ff" opacity=".35"/><rect x="430" y="160" width="300" height="540" rx="150" fill="none" stroke="#ffd23f" stroke-width="14"/>'
b+=figure(580,690,330,'#2a0a4a',pose='up')+crown(580,330,.5)
b+=figure(250,720,380,'#0a0214',pose='up')
I[33]=svg(b,d)

# 34 Le vent nous portera: dandelion seeds lifted by the wind from a field at dusk, drifting toward the last light
d,b=bg([(0,'#2a2a5a'),(.55,'#8a5a7a'),(1,'#f0a86a')])
b+=glow(600,560,200,'#ffd08a',.45)
b+=hills(640,20,'#2a2030',34,4)+'<rect y="680" width="800" height="120" fill="#1a1420"/>'
b+='<path d="M220 800 Q230 620 200 500" stroke="#2a3020" stroke-width="7" fill="none"/>'
b+=''.join(f'<path d="M200 500 L{200+math.cos(a)*60:.0f} {500+math.sin(a)*60:.0f}" stroke="#f6f0e0" stroke-width="2"/><circle cx="{200+math.cos(a)*60:.0f}" cy="{500+math.sin(a)*60:.0f}" r="5" fill="#fff"/>' for a in [i*math.pi/9 for i in range(18)] if math.sin(a)<.6)
r=R(34)
for k in range(22):
    x,y=r.uniform(260,780),r.uniform(80,480);s=r.uniform(10,22)
    b+=f'<path d="M{x:.0f} {y:.0f} l{-s*.8:.0f} {s:.0f}" stroke="#f6f0e0" stroke-width="2"/>'+''.join(f'<path d="M{x:.0f} {y:.0f} l{math.cos(a)*s*.6:.0f} {math.sin(a)*s*.6:.0f}" stroke="#fff" stroke-width="1.6" opacity=".9"/>' for a in [j*math.pi/4-math.pi for j in range(5)])
I[34]=svg(b,d)

# 35 L'Aigle noir: a giant black eagle with wings spread swoops down out of a pale dawn sky over a still lake
d,b=bg([(0,'#c8c0d0'),(.6,'#e8d8d0'),(1,'#a8b0c0')])
b+=glow(400,260,200,'#fff',.6)
b+='<rect y="600" width="800" height="200" fill="#7a8a9a"/><rect y="600" width="800" height="5" fill="#fff" opacity=".6"/>'
b+=hills(600,20,'#4a5060',35,4)
b+='<g fill="#0a0a10" transform="translate(400 330)"><path d="M0 -20 Q-120 -140 -360 -110 Q-250 -70 -230 -30 Q-300 -10 -320 30 Q-200 20 -150 40 Q-200 70 -210 100 Q-100 60 -30 50Z"/>'
b+='<path d="M0 -20 Q120 -140 360 -110 Q250 -70 230 -30 Q300 -10 320 30 Q200 20 150 40 Q200 70 210 100 Q100 60 30 50Z"/>'
b+='<ellipse cx="0" cy="30" rx="44" ry="80"/><circle cx="0" cy="-50" r="30"/><path d="M-8 -36 L0 -10 L10 -36Z" fill="#d8a03a"/><path d="M-40 110 L0 200 L40 110Z"/></g>'
b+='<path d="M0 640 Q400 610 800 640" stroke="#0a0a10" stroke-width="4" opacity=".15" fill="none"/>'
I[35]=svg(b,d)

# 36 Je danse le Mia: Marseille, 1980s: guys with huge shoulder pads dance the Mia around a giant boombox under disco lights
d,b=bg([(0,'#1a0a3a'),(.6,'#5a1a6a'),(1,'#ff5a8a')])
b+=discoball(400,110,50)+rays(400,110,16,'#ffffff',.06,4)
b+='<rect y="640" width="800" height="160" fill="#1a0a20"/>'
b+='<rect x="270" y="520" width="260" height="140" rx="16" fill="#1a1a22"/><circle cx="330" cy="595" r="44" fill="#3a3a44"/><circle cx="470" cy="595" r="44" fill="#3a3a44"/><circle cx="330" cy="595" r="16" fill="#ff5aa8"/><circle cx="470" cy="595" r="16" fill="#ff5aa8"/><rect x="370" y="540" width="60" height="26" fill="#2ad0ff"/><path d="M300 520 Q400 470 500 520" stroke="#1a1a22" stroke-width="10" fill="none"/>'
for x,p in [(120,'wave'),(200,'up'),(600,'up'),(680,'wave')]:
    b+=figure(x,680,280,'#0a0210',pose=p)+f'<path d="M{x-40} 488 L{x+40} 488 L{x+34} 520 L{x-34} 520Z" fill="#0a0210"/>'
I[36]=svg(b,d)

# 37 Macarena: a lone woman in a pink neon-lit room full of smoke, a cracked neon heart above her, cold and broken
d,b=bg([(0,'#0a0208'),(1,'#200814')])
b+='<path d="M280 160 C180 70 100 190 280 320 C460 190 380 70 280 160Z" transform="translate(120 0)" fill="none" stroke="#ff3aa8" stroke-width="14"/>'
b+='<path d="M400 150 L380 210 L420 240 L390 310" stroke="#0a0208" stroke-width="12" fill="none"/>'
b+=glow(400,230,150,'#ff3aa8',.35)
b+='<rect y="0" width="800" height="800" fill="#ff3aa8" opacity=".04"/>'
for k in range(5): b+=f'<ellipse cx="{150+k*130}" cy="{560+k%2*30}" rx="200" ry="40" fill="#ffd0f0" opacity=".06" filter="url(#glow)"/>'
b+=figure(400,760,380,'#050104',hair='#050104')
b+='<path d="M372 468 Q400 700 428 468Z" fill="#050104"/>'
I[37]=svg(b,d)

# 38 Hymne à l'amour: two lovers embrace on a hilltop while the blue sky cracks and stars fall around them
d,b=bg([(0,'#0a1a4a'),(.6,'#2a4a8a'),(1,'#8a6aa0')])
b+='<path d="M120 0 L200 140 L170 220 L260 360 M600 0 L560 120 L620 230" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>'
r=R(38)
for k in range(10):
    x,y=r.uniform(50,750),r.uniform(60,400);b+=f'<path d="M{x:.0f} {y:.0f} l-40 -60" stroke="#fff6c0" stroke-width="3" opacity=".7"/>'+sparkle(x,y,10,'#fff6c0')
b+='<path d="M-10 800 L-10 640 Q400 540 810 640 L810 800Z" fill="#14102a"/>'
b+=figure(375,620,300,'#05040c',pose='hold',hair='#05040c')+figure(430,620,320,'#05040c',pose='hold')
b+=heart(402,250,40,'#ff5a8a')+glow(402,250,60,'#ff8ab0',.5)
I[38]=svg(b,d)

# 39 Les Lacs du Connemara: wild Irish lakes under a moody sky, green hills, a little white church by the water
d,b=bg([(0,'#5a6a7a'),(.5,'#a8b0b0'),(1,'#d8d0b0')])
b+='<ellipse cx="200" cy="140" rx="200" ry="60" fill="#8a9098"/><ellipse cx="600" cy="110" rx="240" ry="70" fill="#7a808a"/>'
b+=hills(400,50,'#4a7a4a',39,4)+hills(440,40,'#3a6a3a',40,3)
b+='<rect y="480" width="800" height="320" fill="#4a6a80"/>'
b+='<path d="M0 480 Q400 520 800 480 L800 520 Q400 560 0 520Z" fill="#fff" opacity=".15"/>'
b+='<rect x="520" y="390" width="80" height="80" fill="#f6f0e6"/><path d="M510 394 L560 350 L610 394Z" fill="#3a3a40"/><rect x="540" y="320" width="20" height="60" fill="#f6f0e6"/><path d="M536 324 L550 290 L564 324Z" fill="#3a3a40"/>'
b+='<path d="M0 620 Q200 580 400 640 L400 800 L0 800Z" fill="#2a4a2a"/>'
for x in (90,170,260): b+=f'<path d="M{x} 640 Q{x+10} 560 {x+4} 520" stroke="#5a7a3a" stroke-width="5" fill="none"/>'
I[39]=svg(b,d)

# 40 Marie: a tender candle-lit window where a single white rose waits, a love song to a mother
d,b=bg([(0,'#1a1020'),(1,'#3a2030')])
b+='<rect x="220" y="100" width="360" height="460" rx="180" fill="#2a3a6a"/><rect x="220" y="100" width="360" height="460" rx="180" fill="none" stroke="#0a060a" stroke-width="20"/>'
b+=starsf(30,40,500,'#fff6e0').replace('<circle','<circle clip-path="url(#w40)"')
b+='<rect x="160" y="560" width="480" height="40" fill="#4a2a1a"/>'
b+='<rect x="460" y="460" width="34" height="100" fill="#f6efe2"/><path d="M477 460 Q462 430 477 400 Q492 430 477 460Z" fill="#ffd27a"/>'+glow(477,430,90,'#ffd27a',.5)
b+='<path d="M330 560 Q320 480 340 400" stroke="#3a6a3a" stroke-width="8" fill="none"/>'+rose(340,370,1.1,'#fbf6ee',stem=False)
I[40]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
