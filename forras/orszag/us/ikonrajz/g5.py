import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 5. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 92 Black or White (Michael Jackson, 1991): a face split half black half white morphing, a globe spinning between two halves
d,b=bg([(0,'#0a0a0a'),(1,'#0a0a0a')])
b+='<rect x="400" width="400" height="800" fill="#f2f2f2"/>'
b+='<path d="M400 160 Q290 170 280 330 Q280 470 400 520Z" fill="#f2f2f2"/><path d="M400 160 Q510 170 520 330 Q520 470 400 520Z" fill="#0a0a0a"/>'
b+='<circle cx="350" cy="320" r="12" fill="#0a0a0a"/><circle cx="450" cy="320" r="12" fill="#f2f2f2"/>'
b+='<circle cx="400" cy="650" r="90" fill="#2a6ab0"/><path d="M360 600 Q400 590 410 630 Q380 670 350 650Z M420 650 Q460 640 470 680 Q440 720 420 700Z" fill="#4ab07a"/>'
I[92]=svg(b,d)

# 93 I Kissed a Girl (Katy Perry, 2008): a cherry-red lipstick tube and a cherry pair on a candy-striped pin-up backdrop
d,b=bg([(0,'#ff8ab8'),(1,'#ffd0e0')])
for k in range(10): b+=f'<rect x="{k*90-30}" width="44" height="800" fill="#fff" opacity=".35" transform="rotate(20 400 400)"/>'
b+='<g transform="translate(330 470) rotate(-14)"><rect x="-60" y="0" width="120" height="200" rx="10" fill="#d8b040"/><rect x="-46" y="-110" width="92" height="120" fill="#e8c860"/><path d="M-40 -110 L-40 -200 Q0 -260 40 -200 L40 -110Z" fill="#d8102a"/></g>'
b+='<path d="M560 330 Q600 220 660 200" stroke="#2a6a2a" stroke-width="8" fill="none"/><path d="M620 380 Q630 260 660 200" stroke="#2a6a2a" stroke-width="8" fill="none"/>'
b+='<circle cx="555" cy="380" r="56" fill="#c8001a"/><circle cx="625" cy="430" r="56" fill="#c8001a"/><circle cx="535" cy="360" r="14" fill="#fff" opacity=".5"/><circle cx="605" cy="410" r="14" fill="#fff" opacity=".5"/>'
I[93]=svg(b,d)

# 95 Savage (Megan Thee Stallion ft. Beyoncé, 2020): a confident woman in a leopard-print bodysuit striking a power pose, Houston skyline in gold
d,b=bg([(0,'#2a1a08'),(1,'#d8902a')])
b+=skyline(560,'#3a2008',95,80,280,'#ffd27a',60)+'<rect y="660" width="800" height="140" fill="#1a0e04"/>'
d+='<pattern id="leo" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" fill="#e8b04a"/><circle cx="15" cy="15" r="9" fill="none" stroke="#2a1404" stroke-width="5"/><circle cx="45" cy="42" r="8" fill="none" stroke="#2a1404" stroke-width="5"/><circle cx="44" cy="12" r="4" fill="#2a1404"/></pattern>'
b+=figure(400,760,480,'url(#leo)',pose='hold',hair='#1a0a04')+'<ellipse cx="400" cy="342" rx="31" ry="37" fill="#5a2a14"/>'
I[95]=svg(b,d)

# 96 Birds of a Feather (Billie Eilish, 2024): two small birds sharing one branch at dusk, soft blue and pastel pink
d,b=bg([(0,'#3a4a7a'),(1,'#f0b8c8')])
b+=glow(560,240,120,'#fff0f4',.7)+'<path d="M0 520 Q300 480 800 540" stroke="#2a1a24" stroke-width="20" fill="none"/>'
for k in range(4): b+=f'<ellipse cx="{120+k*180}" cy="{500+k*8}" rx="30" ry="12" fill="#2a4a2a" transform="rotate(-20 {120+k*180} {500+k*8})"/>'
for x,c in ((350,'#2a3a6a'),(450,'#2a3a6a')):
    f=1 if x<400 else -1
    b+=f'<g transform="translate({x} 460) scale({f} 1)"><ellipse rx="52" ry="40" fill="{c}"/><circle cx="40" cy="-30" r="26" fill="{c}"/><path d="M62 -32 L84 -26 L62 -20Z" fill="#e8a02a"/><circle cx="46" cy="-36" r="5" fill="#fff"/><path d="M-50 -10 L-100 10 L-50 20Z" fill="{c}"/></g>'
b+=heart(400,380,18,'#ff7aa8')
I[96]=svg(b,d)

# 97 What's Going On (Marvin Gaye, 1971): a man in a trench coat standing in the rain under a single streetlamp, early-70s inner-city blues
d,b=bg([(0,'#0a1020'),(1,'#2a3a4a')])
b+=skyline(500,'#141c2a',97,80,280,'#c8d0ff',40)+rain(160,97,'#cfe0ff',.35,6)
b+='<path d="M560 800 L560 200 Q560 160 520 160 L470 160" stroke="#1a1a20" stroke-width="12" fill="none"/>'+glow(470,180,70,'#ffe0a0',.8)+spotlight(470,180,140,'#ffe8b0',.15)
b+='<rect y="680" width="800" height="120" fill="#0a0e18"/>'+figure(400,740,320,'#06080e',pose='stand')+hat(400,420,40,'#06080e','#2a2a2a')
b+='<ellipse cx="400" cy="760" rx="160" ry="16" fill="#ffe0a0" opacity=".12"/>'
I[97]=svg(b,d)

# 100 Ain't No Sunshine (Bill Withers, 1970): an empty house at dawn with drawn curtains, a cold gray sun hidden behind clouds
d,b=bg([(0,'#3a3a44'),(1,'#7a7a84')])
b+='<circle cx="560" cy="200" r="70" fill="#d8d8d8" opacity=".4"/>'
for x,y in ((480,200),(620,190),(560,240)): b+=f'<ellipse cx="{x}" cy="{y}" rx="120" ry="40" fill="#5a5a64"/>'
b+='<rect y="600" width="800" height="200" fill="#2a2a30"/><path d="M200 600 L200 380 L400 240 L600 380 L600 600Z" fill="#3a3a44"/>'
for x in (260,480): b+=f'<rect x="{x}" y="420" width="70" height="90" fill="#6a6a74"/><path d="M{x} 420 Q{x+35} 470 {x} 510Z M{x+70} 420 Q{x+35} 470 {x+70} 510Z" fill="#b8b0a0"/>'
b+='<rect x="370" y="500" width="60" height="100" fill="#1a1a20"/>'
I[100]=svg(b,d)

# 103 Use Somebody (Kings of Leon, 2009): a lonely figure watching a city from a hilltop at night, distant light trails
d,b=bg([(0,'#04060e'),(1,'#1a2a3a')])
b+=starsf(60,103,400)+skyline(600,'#0e1420',103,40,160,'#ffe0a0',140)
for k in range(5): b+=f'<path d="M0 {660+k*14} Q400 {620+k*14} 800 {660+k*14}" stroke="{["#ff4a4a","#fff2c0"][k%2]}" stroke-width="3" fill="none" opacity=".6"/>'
b+=hills(700,30,'#04060a',103,3)+figure(220,720,180,'#000',pose='stand')
I[103]=svg(b,d)

# 105 Empire State of Mind (Jay-Z ft. Alicia Keys, 2009): the Empire State Building lit at night, a grand piano on a rooftop below
d,b=bg([(0,'#06081a'),(1,'#2a2a5a')])
b+=starsf(40,105,300)+skyline(620,'#141428',105,80,240,'#ffd27a',80)
b+='<g fill="#1a1a34"><rect x="350" y="300" width="100" height="340"/><rect x="370" y="240" width="60" height="60"/><rect x="385" y="190" width="30" height="50"/><rect x="396" y="110" width="8" height="80"/></g>'
b+='<rect x="350" y="300" width="100" height="40" fill="#ff3a3a" opacity=".55"/><rect x="370" y="240" width="60" height="30" fill="#fff" opacity=".5"/><rect x="385" y="190" width="30" height="20" fill="#3a8aff" opacity=".6"/>'+glow(400,200,60,'#fff',.4)
b+='<rect y="680" width="800" height="120" fill="#0a0a16"/><path d="M200 680 L420 680 Q470 680 470 650 L450 620 Q380 600 300 610 L210 620Z" fill="#020206"/>'
I[105]=svg(b,d)

# 106 Paint the Town Red (Doja Cat, 2023): a devil-horned figure walking a street drenched in red paint, splatters everywhere
d,b=bg([(0,'#3a0004'),(1,'#a80010')])
r=random.Random(106)
for k in range(30): x,y,s=r.uniform(0,800),r.uniform(0,800),r.uniform(10,50);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="#ff1a2a" opacity=".6"/>'
b+=skyline(600,'#2a0004',106,60,200)+'<rect y="660" width="800" height="140" fill="#1a0002"/>'
b+=figure(400,760,420,'#0a0002',pose='stand',hair='#0a0002')+'<path d="M370 340 Q360 300 380 290 Q378 320 388 334Z M430 340 Q440 300 420 290 Q422 320 412 334Z" fill="#0a0002"/>'
I[106]=svg(b,d)

# 107 Espresso (Sabrina Carpenter, 2024): a steaming espresso cup on a saucer on a sunlit retro beach-club table, cream and baby blue
d,b=bg([(0,'#9ad8f0'),(1,'#fff0d8')])
for k in range(8): b+=f'<rect x="{k*100}" y="0" width="50" height="300" fill="#fff" opacity=".5"/>'
b+='<rect y="520" width="800" height="280" fill="#f6e0c0"/><ellipse cx="400" cy="560" rx="200" ry="40" fill="#fff"/>'
b+='<path d="M290 360 L510 360 L490 540 Q400 570 310 540Z" fill="#fff"/><path d="M510 400 Q580 400 570 460 Q560 510 500 500" stroke="#fff" stroke-width="22" fill="none"/><ellipse cx="400" cy="362" rx="110" ry="20" fill="#5a2a10"/>'
for k in range(3): b+=f'<path d="M{360+k*40} 330 q-20 -40 0 -80 q20 -40 0 -80" stroke="#fff" stroke-width="10" fill="none" opacity=".75" stroke-linecap="round"/>'
I[107]=svg(b,d)

# 108 I Don't Want to Miss a Thing (Aerosmith, 1998): an astronaut's helmet visor reflecting Earth and a falling asteroid, deep space
d,b=bg([(0,'#000'),(1,'#0a0a1a')])
b+=starsf(140,108,800)
b+='<circle cx="400" cy="420" r="230" fill="#e8e8ee"/><circle cx="400" cy="420" r="180" fill="#0a1020"/>'
b+='<clipPath id="vz"><circle cx="400" cy="420" r="180"/></clipPath><g clip-path="url(#vz)"><circle cx="460" cy="540" r="150" fill="#2a6ab0"/><path d="M380 470 Q440 440 470 490 Q430 560 390 530Z" fill="#4ab07a"/>'
b+='<path d="M270 300 L360 380" stroke="#ffb04a" stroke-width="10" stroke-linecap="round"/><circle cx="360" cy="380" r="16" fill="#ffd27a"/></g>'
b+='<path d="M260 340 Q300 280 360 260" stroke="#fff" stroke-width="12" fill="none" opacity=".3" stroke-linecap="round"/><rect x="300" y="640" width="200" height="60" rx="10" fill="#c8c8d0"/>'
I[108]=svg(b,d)

# 109 Time in a Bottle (Jim Croce, 1973): an old glass bottle holding a tiny hourglass, a golden-sunset beach behind
d,b=bg([(0,'#3a2a5a'),(.6,'#e8905a'),(1,'#f6d0a0')])
b+='<rect y="580" width="800" height="220" fill="#d8b080"/>'
b+='<g transform="translate(400 520) rotate(-60)"><path d="M-90 -230 L90 -230 L90 120 Q90 160 50 160 L30 160 L30 230 L-30 230 L-30 160 L-50 160 Q-90 160 -90 120Z" fill="#9ad8c0" opacity=".45" stroke="#e8fff6" stroke-width="5"/><rect x="-34" y="220" width="68" height="30" fill="#8a5a2a"/>'
b+='<path d="M-50 -180 L50 -180 L6 -40 L50 100 L-50 100 L-6 -40Z" fill="none" stroke="#c8902a" stroke-width="8"/><path d="M-30 100 L30 100 L0 50Z" fill="#f2d090"/></g>'
I[109]=svg(b,d)

# 110 Bodak Yellow (Cardi B, 2017): a pair of red-bottom stiletto heels on a bright yellow floor, sharp shadows
d,b=bg([(0,'#ffe12a'),(1,'#f0b800')])
for x in (290,490):
    b+=f'<g transform="translate({x} 520)"><path d="M-110 60 Q-120 0 -80 -20 Q-20 -40 40 -110 L80 -120 Q100 -80 90 -40 L90 60 L80 60 L70 -10 Q-20 40 -40 60Z" fill="#0a0a0a"/><path d="M80 -10 L80 160 L92 160 L92 -10Z" fill="#0a0a0a"/>'
    b+='<path d="M-40 60 Q-20 40 70 -10 L76 4 Q-10 50 -30 66Z" fill="#e0102a"/></g>'
b+='<ellipse cx="400" cy="700" rx="280" ry="24" fill="#a07800" opacity=".4"/>'
I[110]=svg(b,d)

# 111 WAP (Cardi B ft. Megan Thee Stallion, 2020): a long mansion hallway of leopard and tiger print walls with a big cat prowling
d,b=bg([(0,'#2a1a08'),(1,'#5a3a10')])
d+='<pattern id="leo2" width="70" height="70" patternUnits="userSpaceOnUse"><rect width="70" height="70" fill="#d89a3a"/><circle cx="18" cy="18" r="10" fill="none" stroke="#2a1404" stroke-width="6"/><circle cx="52" cy="50" r="9" fill="none" stroke="#2a1404" stroke-width="6"/></pattern>'
b+='<path d="M0 0 L300 260 L300 540 L0 800Z M800 0 L500 260 L500 540 L800 800Z" fill="url(#leo2)"/><rect x="300" y="260" width="200" height="280" fill="#ff6aa8"/>'
b+='<path d="M0 800 L300 540 L500 540 L800 800Z" fill="#f2e0c8"/>'
b+='<g transform="translate(400 640)" fill="#1a0e04"><ellipse rx="110" ry="40"/><circle cx="110" cy="-30" r="38"/><path d="M90 -60 L100 -84 L110 -64Z M130 -60 L140 -82 L146 -58Z"/><path d="M-110 0 Q-180 -20 -200 -80" stroke="#1a0e04" stroke-width="14" fill="none"/>'
b+='<rect x="-90" y="20" width="16" height="50"/><rect x="60" y="20" width="16" height="50"/></g><circle cx="520" cy="606" r="5" fill="#ffd84a"/>'
I[111]=svg(b,d)

# 112 Hypnotize (The Notorious B.I.G., 1997): a hypnotic black-and-white spiral behind a Brooklyn kingpin in a crown, gold glinting
d,b=bg([(0,'#f2f2f2'),(1,'#f2f2f2')])
p='M400 400 '+' '.join(f'L{400+t*3*math.cos(t/6):.0f} {400+t*3*math.sin(t/6):.0f}' for t in range(1,190))
b+=f'<path d="{p}" stroke="#0a0a0a" stroke-width="24" fill="none"/>'
b+=figure(400,800,440,'#0a0a0a',pose='stand')+'<ellipse cx="400" cy="415" rx="34" ry="40" fill="#0a0a0a"/>'
b+='<path d="M362 378 L362 340 L380 360 L400 330 L420 360 L438 340 L438 378Z" fill="#e8b830"/>'
I[112]=svg(b,d)

# 116 You Give Love a Bad Name (Bon Jovi, 1986): a heart shot through with a bullet hole, smoking, against an 80s hair-metal stage glow
d,b=bg([(0,'#1a0414'),(1,'#7a0a3a')])
b+=rays(400,800,24,'#ff8ac0',.12,8)
b+=heart(400,400,170,'#e0102a')+'<circle cx="440" cy="360" r="26" fill="#1a0414"/>'
for k in range(10): a=k*.628;b+=f'<path d="M440 360 l{50*math.cos(a):.0f} {50*math.sin(a):.0f}" stroke="#1a0414" stroke-width="4"/>'
b+='<path d="M450 330 q30 -40 0 -80 q-30 -40 10 -90" stroke="#e8e0e8" stroke-width="10" fill="none" opacity=".5"/>'
I[116]=svg(b,d)

# 117 Vampire (Olivia Rodrigo, 2023): a bat silhouette crossing a full moon over a purple Hollywood hill, a broken heart below
d,b=bg([(0,'#12061e'),(1,'#4a1a5a')])
b+=starsf(60,117,500)+moon(400,300,150,'#f6ecf6',.4)
b+='<path d="M400 290 Q340 230 260 260 Q300 280 300 310 Q340 290 360 320 Q380 300 400 330 Q420 300 440 320 Q460 290 500 310 Q500 280 540 260 Q460 230 400 290Z" fill="#12061e"/>'
b+=hills(620,40,'#1a0a24',117,4)+heart(400,690,40,'#c8102a')+'<path d="M400 650 L388 690 L410 710 L400 740" stroke="#1a0a24" stroke-width="6" fill="none"/>'
I[117]=svg(b,d)

# 118 All I Want for Christmas Is You (Mariah Carey, 1994): a snowy night window with a glowing Christmas tree, gifts and a single red ribbon heart
d,b=bg([(0,'#0a1a3a'),(1,'#2a4a7a')])
b+=starsf(60,118,800,'#fff')
b+='<path d="M400 140 L560 600 L240 600Z" fill="#1a6a3a"/><path d="M400 140 L500 420 L300 420Z" fill="#2a8a4a"/>'+star5(400,140,34,'#ffd84a')
r=random.Random(118)
for k in range(24): x=r.uniform(270,530);y=r.uniform(240,590);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="{r.choice(["#ff3a3a","#ffd84a","#fff","#3ad8ff"])}"/>' if abs(x-400)<(y-140)*.33 else ''
b+='<rect y="640" width="800" height="160" fill="#e8f0ff"/>'
for x,c in ((220,'#e0102a'),(330,'#f2d040'),(480,'#e0102a'),(580,'#2a8ad8')): b+=f'<rect x="{x}" y="590" width="90" height="70" fill="{c}"/><rect x="{x+38}" y="590" width="14" height="70" fill="#fff"/>'
b+=heart(400,520,22,'#ff1a3a')
I[118]=svg(b,d)

# 119 Texas Hold 'Em (Beyoncé, 2024): a white cowboy hat and a banjo on a rodeo fence at a Texas sunset, a lone star
d,b=bg([(0,'#3a1a3a'),(.6,'#e86a3a'),(1,'#f6c06a')])
b+=glow(400,560,200,'#fff0c0',.8)+hills(600,14,'#5a2a1a',119,4)+'<rect y="620" width="800" height="180" fill="#3a2010"/>'
b+=''.join(f'<rect x="{x}" y="520" width="20" height="200" fill="#5a3a1a"/>' for x in (80,280,500,700))+'<rect x="0" y="560" width="800" height="18" fill="#6a4a2a"/><rect x="0" y="620" width="800" height="18" fill="#6a4a2a"/>'
b+=hat(300,530,90,'#f6f2ea','#c8a04a')
b+='<g transform="translate(560 540) rotate(25)"><circle r="70" fill="#f2e6c8" stroke="#8a6a3a" stroke-width="10"/><rect x="-10" y="-300" width="20" height="240" fill="#5a3a1a"/></g>'+star5(640,160,40,'#fff6d0')
I[119]=svg(b,d)

# 99 Teenage Dream (Katy Perry, 2010): a teenage couple on a car hood under a cotton-candy sunset, a convertible by the beach
d,b=bg([(0,'#ff8ac0'),(.6,'#ffc08a'),(1,'#9ad8f0')])
b+=glow(400,420,180,'#fff2c0',.8)+'<circle cx="400" cy="440" r="90" fill="#fff0c8"/>'
for x,y in ((140,180),(660,150),(400,110)): b+=f'<ellipse cx="{x}" cy="{y}" rx="130" ry="44" fill="#ffd8ec"/>'
b+='<rect y="500" width="800" height="100" fill="#4ab0d8"/><rect y="600" width="800" height="200" fill="#f6dca8"/>'
b+=car(400,740,150,'#ff4a8a','#f2f2f2',glass='#bff0ff')
b+='<g fill="#2a0a2a"><circle cx="360" cy="570" r="20"/><path d="M338 594 Q360 582 382 594 L386 640 L334 640Z"/><circle cx="430" cy="566" r="20"/><path d="M408 590 Q430 578 452 590 L456 640 L404 640Z"/></g>'+heart(396,530,20,'#ff3a7a')
I[99]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
