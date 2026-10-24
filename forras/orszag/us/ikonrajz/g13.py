import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 13. csoport: nagy dalok, amelyekhez még nincs videó (előre rajzolva, 2026-10-24)
I={}

# 46 Superstition (Stevie Wonder, 1972): a clavinet keyboard funk riff, a black cat and a cracked mirror under a broken ladder
d,b=bg([(0,'#2a0a3a'),(1,'#d86a2a')])
b+='<path d="M120 140 L260 640 M260 140 L400 640" stroke="#3a1a0a" stroke-width="16"/>'+''.join(f'<path d="M{150+k*22} {240+k*80} l140 0" stroke="#3a1a0a" stroke-width="12"/>' for k in range(5))
b+='<ellipse cx="560" cy="300" rx="110" ry="150" fill="#cfe0f0" stroke="#c8a04a" stroke-width="14"/><path d="M500 200 L560 300 L520 380 M560 300 L630 260" stroke="#fff" stroke-width="5" fill="none"/>'
b+='<rect y="620" width="800" height="180" fill="#1a0a14"/>'
b+='<g transform="translate(560 640)" fill="#000"><ellipse rx="70" ry="40" cy="-20"/><circle cx="60" cy="-70" r="30"/><path d="M40 -92 L48 -120 L62 -96Z M70 -96 L84 -120 L86 -90Z"/><path d="M-70 -20 Q-140 -60 -110 -140" stroke="#000" stroke-width="12" fill="none"/></g><circle cx="610" cy="574" r="5" fill="#ffd84a"/>'
I[46]=svg(b,d)

# 51 Something in the Orange (Zach Bryan, 2022): a lone man on a porch step watching an orange sunset over a wide country field, guitar beside
d,b=bg([(0,'#5a2a4a'),(.55,'#ff7a2a'),(1,'#ffc06a')])
b+=glow(560,500,150,'#fff0c0',.8)+'<circle cx="560" cy="510" r="70" fill="#ffe0a0"/>'+hills(540,12,'#4a2010',51,5)+'<rect y="560" width="800" height="240" fill="#3a1808"/>'
b+='<rect x="0" y="600" width="400" height="30" fill="#1a0a04"/><rect x="0" y="630" width="420" height="30" fill="#140804"/>'
b+='<g fill="#0a0402"><circle cx="200" cy="500" r="22"/><path d="M182 522 L218 522 L222 600 L178 600Z"/><path d="M180 600 L240 604 L250 660 M220 600 L280 604 L290 660" stroke="#0a0402" stroke-width="16"/></g>'+guitar(120,560,70,'#5a2a10','#2a1008',-12)
I[51]=svg(b,d)

# 56 Peggy Sue (Buddy Holly, 1957): thick black horn-rimmed glasses on a jukebox, a Fender guitar and a 50s soda shop checkerboard
d,b=bg([(0,'#7ad0d8'),(1,'#f2e6c8')])
for i in range(10):
    for j in range(4): b+=f'<rect x="{i*80}" y="{640+j*40}" width="80" height="40" fill="{"#111" if (i+j)%2 else "#f2f2f2"}"/>'
b+=jukebox(400,560,120)
b+='<g transform="translate(400 250)"><rect x="-200" y="-50" width="170" height="100" rx="20" fill="none" stroke="#0a0a0a" stroke-width="24"/><rect x="30" y="-50" width="170" height="100" rx="20" fill="none" stroke="#0a0a0a" stroke-width="24"/><path d="M-30 -20 Q0 -40 30 -20" stroke="#0a0a0a" stroke-width="16" fill="none"/></g>'
I[56]=svg(b,d)

# 62 Like a Virgin (Madonna, 1984): a white lace wedding veil and a gondola on a Venetian canal, a lion statue, 80s bride
d,b=bg([(0,'#1a2a5a'),(1,'#7a8ab8')])
b+='<rect y="520" width="800" height="280" fill="#1a3a6a"/>'+skyline(520,'#2a2a44',62,80,200,'#ffe0a0',30)
b+='<path d="M180 640 Q400 700 620 640 L640 600 Q600 660 400 670 Q200 660 160 600Z" fill="#06060e"/>'
b+='<g transform="translate(400 640)"><circle cx="0" cy="-260" r="24" fill="#2a1a0a"/><path d="M-24 -280 Q-90 -150 -110 0 L110 0 Q90 -150 24 -280Z" fill="#fff" opacity=".55"/><path d="M-26 -236 L26 -236 L40 -130 Q100 -40 110 -10 L-110 -10 Q-100 -40 -40 -130Z" fill="#fbfaf6"/></g>'
I[62]=svg(b,d)

# 70 I'll Be Missing You (Puff Daddy & Faith Evans ft. 112, 1997): a single candle and a framed crown photo in a rain of soft light, memorial white
d,b=bg([(0,'#1a1a24'),(1,'#4a4a5a')])
b+=rain(80,70,'#e8e8ff',.25,0)+'<rect x="280" y="180" width="240" height="300" fill="#c8a040"/><rect x="300" y="200" width="200" height="260" fill="#2a2a34"/>'
b+='<path d="M350 340 L350 290 L375 315 L400 280 L425 315 L450 290 L450 340Z" fill="#e8c040"/>'
b+='<rect x="380" y="560" width="40" height="120" fill="#f2ead8"/>'+glow(400,540,50,'#ffd27a',.9)+'<ellipse cx="400" cy="540" rx="10" ry="22" fill="#ffe08a"/>'
I[70]=svg(b,d)

# 73 Everyday People (Sly & the Family Stone, 1969): a row of diverse psychedelic silhouettes in many colors holding hands, peace-sign sun
d,b=bg([(0,'#ffd23a'),(1,'#ff6a3a')])
b+='<circle cx="400" cy="230" r="120" fill="#fff2a0"/><circle cx="400" cy="230" r="90" fill="none" stroke="#ff6a3a" stroke-width="14"/><path d="M400 140 L400 320 M400 230 L336 294 M400 230 L464 294" stroke="#ff6a3a" stroke-width="14"/>'
for k,c in enumerate(('#7a3aff','#2ae07a','#e0102a','#3ad8ff','#ff3ab0','#1a1a1a','#f2f2f2')): b+=figure(100+k*100,780,300,c,pose='stand',hair=c)
b+='<path d="M140 560 L660 560" stroke="#3a1a0a" stroke-width="8" opacity=".4"/>'
I[73]=svg(b,d)

# 75 Nuthin' but a 'G' Thang (Dr. Dre ft. Snoop Dogg, 1992): a bouncing lowrider at a Long Beach backyard barbecue, palm trees and haze
d,b=bg([(0,'#f0b06a'),(1,'#f6e0b0')])
b+=palm(110,620,360,'#3a2a1a',8)+palm(700,620,320,'#3a2a1a',-8)+'<rect y="620" width="800" height="180" fill="#8a7a5a"/>'
b+='<g transform="translate(400 690) rotate(-8)">'+car(0,0,150,'#3a8a5a','#e8e8ee',glass='#3a4a5a')+'</g>'
b+='<rect x="560" y="560" width="100" height="70" fill="#1a1a1a"/>'+''.join(f'<path d="M{580+k*20} 550 q-10 -40 4 -80" stroke="#ccc" stroke-width="6" fill="none" opacity=".5"/>' for k in range(4))
I[75]=svg(b,d)

# 78 Hot Stuff (Donna Summer, 1979): a disco queen in a red sequin dress under a giant mirror ball and flames of light
d,b=bg([(0,'#1a0204'),(1,'#7a0a0a')])
b+=disco(400,120,70)+rays(400,120,24,'#ffb04a',.12,8)
for k in range(9): x=80+k*80;b+=f'<path d="M{x} 800 Q{x-30} 700 {x} 620 Q{x+30} 700 {x+20} 800Z" fill="#ff6a1a" opacity=".6"/>'
b+=figure(400,780,460,'#e0102a',pose='up',hair='#2a0a04')
for k in range(20): b+=f'<circle cx="{370+(k%5)*15}" cy="{460+(k//5)*60}" r="3" fill="#ffd8a0"/>'
I[78]=svg(b,d)

# 79 Jack & Diane (John Cougar, 1982): two teenagers eating chili dogs outside a Tastee Freez in the Heartland, 80s sunset and pickup
d,b=bg([(0,'#3a3a7a'),(.6,'#ff8a5a'),(1,'#ffd08a')])
b+=hills(540,10,'#4a3a2a',79,4)+'<rect y="560" width="800" height="240" fill="#6a5a3a"/>'
b+='<rect x="460" y="380" width="280" height="200" fill="#f2f2f2"/><path d="M440 380 L760 380 L740 340 L460 340Z" fill="#e0102a"/>'+''.join(f'<rect x="{460+k*40}" y="340" width="20" height="40" fill="#fff" opacity=".7"/>' for k in range(7))
b+=figure(220,700,240,'#1a1010',pose='hold')+figure(300,700,220,'#1a1010',pose='hold',hair='#1a1010')
I[79]=svg(b,d)

# 87 That'll Be the Day (The Crickets, 1957): a cricket insect playing a tiny electric guitar on a Texas fence post at dusk
d,b=bg([(0,'#2a2a5a'),(1,'#e8a06a')])
b+=hills(600,20,'#3a2a2a',87,4)+'<rect x="340" y="480" width="120" height="320" fill="#5a3a1a"/>'
b+='<g transform="translate(400 420)"><ellipse rx="90" ry="40" fill="#2a3a14"/><circle cx="90" cy="-10" r="30" fill="#2a3a14"/><path d="M110 -30 Q160 -120 200 -140 M100 -36 Q130 -120 160 -160" stroke="#2a3a14" stroke-width="5" fill="none"/>'
b+='<path d="M-60 30 L-100 80 M-20 34 L-40 90 M20 34 L30 90" stroke="#2a3a14" stroke-width="7"/><path d="M-80 -20 Q-140 -100 -60 -60Z" fill="#3a4a1a"/></g>'+eguitar(380,470,60,'#e0102a','#3a2010',rot=-60)
I[87]=svg(b,d)

# 91 Proud Mary (Creedence Clearwater Revival, 1969): a paddle-wheel riverboat rolling down a misty Mississippi at sunset
d,b=bg([(0,'#3a2a4a'),(.6,'#e8805a'),(1,'#f2c08a')])
b+=glow(400,440,150,'#fff0c0',.7)+'<rect y="470" width="800" height="330" fill="#4a3a4a"/>'+''.join(f'<path d="M{k*80} {520+k%3*40} q20 -8 40 0" stroke="#ffd8a0" stroke-width="4" fill="none" opacity=".6"/>' for k in range(10))
b+='<g fill="#1a0e10"><path d="M180 560 L620 560 L600 600 L200 600Z"/><rect x="240" y="480" width="320" height="80"/><rect x="300" y="420" width="200" height="60"/><rect x="340" y="320" width="20" height="100"/><rect x="440" y="320" width="20" height="100"/></g>'
b+='<circle cx="620" cy="560" r="60" fill="none" stroke="#e0102a" stroke-width="10"/>'+''.join(f'<path d="M620 560 l{60*math.cos(k*.785):.0f} {60*math.sin(k*.785):.0f}" stroke="#e0102a" stroke-width="5"/>' for k in range(8))
I[91]=svg(b,d)

# 94 The Power of Love (Huey Lewis and the News, 1985): a DeLorean-like silver car with flaming tire tracks on a night road, a lightning-struck clock tower
d,b=bg([(0,'#04061a'),(1,'#1a1a3a')])
b+='<rect x="560" y="160" width="140" height="440" fill="#2a2a3a"/><circle cx="630" cy="250" r="50" fill="#f2e6c8"/><path d="M630 250 L630 214 M630 250 L656 260" stroke="#111" stroke-width="5"/>'
b+='<path d="M640 0 L600 90 L630 90 L590 170" stroke="#e8f0ff" stroke-width="8" fill="none"/>'+glow(600,100,60,'#cfe0ff',.5)
b+='<rect y="600" width="800" height="200" fill="#0a0a14"/>'+''.join(f'<path d="M0 {690+k*40} L380 {690+k*40}" stroke="#ff6a1a" stroke-width="8" opacity=".8"/>' for k in range(2))
b+='<g transform="translate(440 700) scale(.8)">'+car(0,0,100,'#c8ccd6','#e8e8ee',glass='#3a4a6a')+'</g>'
I[94]=svg(b,d)

# 98 California Love (2Pac ft. Dr. Dre & Roger Troutman, 1996): a Mad Max-style desert party, dune buggies and flames beneath a burning sky
d,b=bg([(0,'#3a0a04'),(.6,'#e8601a'),(1,'#ffc04a')])
b+='<path d="M0 600 Q200 520 400 600 Q600 520 800 600 L800 800 L0 800Z" fill="#c8802a"/>'
for x in (160,640): b+=f'<path d="M{x-30} 600 Q{x-40} 500 {x} 420 Q{x+40} 500 {x+30} 600Z" fill="#ffb03a"/>'+glow(x,520,60,'#ff6a1a',.6)
b+='<g transform="translate(400 690) scale(.9)">'+car(0,0,100,'#3a2a1a','#8a8a8a',glass='#1a1a1a')+'</g>'+cactus(560,620,100,'#3a2a10')
I[98]=svg(b,d)

# 101 Upside Down (Diana Ross, 1980): a glamorous figure in a flowing gown dancing upside down on a mirrored ceiling, disco glitter
d,b=bg([(0,'#f2d8e8'),(1,'#9a6aa8')])
b+='<rect width="800" height="160" fill="#c8b0d8"/>'+''.join(f'<rect x="{k*60}" y="0" width="56" height="156" fill="#e8d8f0" opacity=".6"/>' for k in range(14))
b+='<g transform="translate(400 160) scale(1 -1)"><path d="M0 -10 L-20 -10 L-30 -150 Q-120 -330 -150 -400 L150 -400 Q120 -330 30 -150 L20 -10Z" fill="#fbf6fa"/><circle cx="0" cy="-470" r="30" fill="#2a0a1a"/><path d="M-30 -490 Q0 -540 30 -490 Q60 -460 30 -440 L-30 -440 Q-60 -460 -30 -490Z" fill="#2a0a1a"/></g>'
for k in range(16): b+=sparkle(120+k*36,640+(k%3)*40,8,'#fff')
I[101]=svg(b,d)

# 102 Hurts So Good (John Cougar, 1982): a leather jacket and a lit match on the hood of a muscle car at a dusty Indiana crossroads
d,b=bg([(0,'#5a3a2a'),(1,'#d8a06a')])
b+=road(400,480,'#3a2a20','#e8d080',500)+'<path d="M0 560 L800 560" stroke="#3a2a20" stroke-width="80"/>'
b+='<path d="M640 480 L640 280 M600 300 L680 340 M600 340 L680 300" stroke="#2a1a10" stroke-width="10"/>'
b+=car(400,720,160,'#1a1a1a','#c8c8d0',glass='#5a4a3a')+'<path d="M320 600 L470 600 L480 650 L310 650Z" fill="#3a1a0a"/>'
I[102]=svg(b,d)

# 104 Little Red Corvette (Prince, 1983): a sleek little red sports car under a purple night sky with a crescent moon and neon
d,b=bg([(0,'#1a0630'),(1,'#5a1a6a')])
b+=starsf(60,104,420)+moon(620,140,40)+'<rect y="600" width="800" height="200" fill="#0e0418"/>'
b+='<g transform="translate(400 690)"><path d="M-230 0 L-220 -40 Q-120 -60 -60 -100 L80 -100 Q140 -60 220 -50 L240 0Z" fill="#e0102a"/><path d="M-50 -92 L70 -92 L110 -56 L-90 -56Z" fill="#3a2a5a"/>'
for cx in (-140,140): b+=f'<circle cx="{cx}" cy="0" r="40" fill="#0a0a0a"/><circle cx="{cx}" cy="0" r="18" fill="#c8c8d0"/>'
b+='</g>'
I[104]=svg(b,d)

# 113 Golden (Huntrix / KPop Demon Hunters, 2025): three animated idol-heroines with glowing weapons silhouetted against a giant golden sun burst
d,b=bg([(0,'#1a0a3a'),(.6,'#c86aff'),(1,'#ffd84a')])
b+=glow(400,440,220,'#ffe880',.9)+'<circle cx="400" cy="440" r="130" fill="#ffe060"/>'+rays(400,440,30,'#fff2a0',.2,10)
for x in (260,400,540): b+=figure(x,780,340,'#14062a',pose='up' if x==400 else 'stand',hair='#14062a')
b+='<path d="M560 520 L640 330" stroke="#9affff" stroke-width="10" stroke-linecap="round"/>'+glow(640,330,20,'#9affff',.9,'glow2')
I[113]=svg(b,d)

# 114 Losing My Religion (R.E.M., 1991): a winged man fallen in a sepia Renaissance-painting room, a pitcher of milk and saints' halos
d,b=bg([(0,'#3a2a1a'),(1,'#a8804a')])
b+=glow(400,200,160,'#ffe0a0',.5)
b+='<g transform="translate(400 560)"><path d="M0 -60 Q-160 -200 -300 -140 Q-180 -100 -100 -40Z" fill="#f2e6d0"/><path d="M0 -60 Q160 -200 300 -140 Q180 -100 100 -40Z" fill="#f2e6d0"/><ellipse rx="50" ry="90" fill="#6a4a2a"/><circle cy="-110" r="30" fill="#6a4a2a"/></g>'
b+='<path d="M620 640 L680 640 L670 560 Q690 530 650 520 L630 520 Q610 540 630 560Z" fill="#f6f2e8"/>'
for x in (160,640): b+=f'<circle cx="{x}" cy="220" r="40" fill="none" stroke="#e8c040" stroke-width="8" opacity=".6"/>'
I[114]=svg(b,d)

# 115 Be My Baby (The Ronettes, 1963): a girl-group trio with towering beehive hairdos and winged eyeliner, a wall of sound behind
d,b=bg([(0,'#1a0a2a'),(1,'#8a2a5a')])
for k in range(10): b+=f'<rect x="{k*80}" y="0" width="70" height="800" fill="#ff6aa8" opacity="{.05+k%3*.04:.2f}"/>'
for x in (240,400,560):
    b+=figure(x,780,340,'#0a0410',pose='stand')+f'<ellipse cx="{x}" cy="440" rx="30" ry="46" fill="#0a0410"/>'
b+=heart(400,140,30,'#ff3a8a')
I[115]=svg(b,d)

# 125 Monster Mash (Bobby 'Boris' Pickett, 1962): a green Frankenstein-style monster dancing in a mad-scientist lab, lightning and bubbling flasks
d,b=bg([(0,'#0a1a0a'),(1,'#2a3a2a')])
b+='<path d="M120 0 L80 120 L110 120 L70 240" stroke="#cfe8ff" stroke-width="6" fill="none"/>'+glow(100,120,60,'#cfe8ff',.4)
for x,c in ((620,'#9aff3a'),(700,'#ff3ab0')): b+=f'<path d="M{x-20} 520 L{x-20} 460 L{x+20} 460 L{x+20} 520 L{x+50} 620 L{x-50} 620Z" fill="{c}" opacity=".7"/>'+''.join(f'<circle cx="{x-10+k*10}" cy="{440-k*20}" r="{6-k}" fill="{c}" opacity=".6"/>' for k in range(3))
b+='<rect y="620" width="800" height="180" fill="#0a140a"/>'+figure(340,760,420,'#3a8a3a',pose='up')+'<rect x="310" y="316" width="60" height="16" fill="#0a1a0a"/><rect x="300" y="380" width="12" height="20" fill="#888"/><rect x="368" y="380" width="12" height="20" fill="#888"/>'
I[125]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
