import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 11. csoport: a következő videós dalok index szerint (2026-10-24)
I={}

# 283 California Gurls (Katy Perry ft. Snoop Dogg, 2010): a candy-land beach with cupcakes, ice-cream pops and cotton-candy clouds
d,b=bg([(0,'#7ad8ff'),(1,'#ffd0e8')])
for x,y in ((140,140),(420,100),(680,160)): b+=f'<ellipse cx="{x}" cy="{y}" rx="110" ry="46" fill="#ffb0d8"/>'
b+='<rect y="560" width="800" height="240" fill="#ffe0a0"/>'
for x,c in ((200,'#ff6ab0'),(400,'#9ae0ff'),(600,'#c8a0ff')):
    b+=f'<path d="M{x-60} 640 L{x+60} 640 L{x+44} 740 L{x-44} 740Z" fill="#f2c08a"/><path d="M{x-70} 640 Q{x-70} 560 {x} 560 Q{x+70} 560 {x+70} 640Z" fill="{c}"/><circle cx="{x}" cy="550" r="14" fill="#e0102a"/>'
b+='<rect x="690" y="360" width="12" height="120" fill="#e8c890"/><rect x="660" y="260" width="70" height="120" rx="30" fill="#ff8ac0"/>'
I[283]=svg(b,d)

# 284 E.T. (Katy Perry ft. Kanye West, 2011): an alien glowing figure descending in a beam of light over an otherworldly ice planet
d,b=bg([(0,'#04020e'),(1,'#1a0a3a')])
b+=starsf(120,284,600)+'<circle cx="620" cy="160" r="70" fill="#7a4aff" opacity=".6"/>'
b+='<path d="M400 0 L250 700 L550 700Z" fill="#9affe0" opacity=".2"/>'+hills(680,30,'#3a5a8a',284,5)
b+=figure(400,600,280,'#b0fff0',pose='up',hair='#b0fff0')+glow(400,460,120,'#9affe0',.3)
I[284]=svg(b,d)

# 285 Payphone (Maroon 5 ft. Wiz Khalifa, 2012): a lonely payphone booth on a rainy night street, receiver hanging, coins on the ground
d,b=bg([(0,'#04060e'),(1,'#1a2030')])
b+=rain(120,285,'#cfe0ff',.35,6)+'<rect y="640" width="800" height="160" fill="#0a0e14"/>'
b+='<rect x="300" y="220" width="200" height="440" rx="8" fill="#1a3a6a"/><rect x="320" y="260" width="160" height="380" fill="#cfe8ff" opacity=".25"/>'+glow(400,250,40,'#fff2c0',.8)
b+='<rect x="360" y="380" width="80" height="120" rx="6" fill="#3a3a44"/><path d="M420 480 Q460 560 420 600" stroke="#111" stroke-width="5" fill="none"/><rect x="400" y="590" width="44" height="18" rx="8" fill="#111"/>'
for x in (520,550,580): b+=f'<ellipse cx="{x}" cy="690" rx="12" ry="5" fill="#c8c8d0"/>'
I[285]=svg(b,d)

# 288 Havana (Camila Cabello ft. Young Thug, 2018): a pastel Old Havana street with a 50s car, palm and a woman in a flowing dress
d,b=bg([(0,'#ffb07a'),(1,'#ffe0b0')])
for k,c in enumerate(('#7ad0c8','#ffd23a','#ff8ab0','#9ab0ff')): b+=f'<rect x="{k*200}" y="160" width="200" height="440" fill="{c}"/>'+''.join(f'<rect x="{k*200+40+j*70}" y="240" width="40" height="80" fill="#fff" opacity=".6"/>' for j in range(2))
b+='<rect y="600" width="800" height="200" fill="#c8a07a"/>'+car(520,740,130,'#4ad8c8','#f2f2f2')
b+='<g transform="translate(220 760)"><circle cx="0" cy="-300" r="24" fill="#2a1408"/><path d="M-18 -276 L18 -276 L30 -170 Q120 -40 140 0 L-140 0 Q-100 -60 -30 -170Z" fill="#e0102a"/></g>'
I[288]=svg(b,d)

# 289 Mood (24kGoldn ft. Iann Dior, 2021): a moody teen skater on a halfpipe at dusk, pink and blue gradient
d,b=bg([(0,'#3a2a8a'),(1,'#ff8ac0')])
b+='<path d="M0 420 Q0 680 200 680 L600 680 Q800 680 800 420 L800 800 L0 800Z" fill="#2a1a4a"/><path d="M0 420 Q0 680 200 680 L600 680 Q800 680 800 420" stroke="#e8e0f0" stroke-width="10" fill="none"/>'
b+='<g transform="translate(560 520) rotate(20)">'+figure(0,0,230,'#0a0618',pose='up')+'<rect x="-50" y="4" width="100" height="12" rx="6" fill="#0a0618"/></g>'
I[289]=svg(b,d)

# 290 Anti-Hero (Taylor Swift, 2023): a giant looming figure peeking through a tiny house window at a small woman inside, moody indigo
d,b=bg([(0,'#1a1a3a'),(1,'#4a3a6a')])
b+='<path d="M220 800 L220 480 L400 340 L580 480 L580 800Z" fill="#e8d8c0"/><rect x="340" y="540" width="120" height="140" fill="#ffd27a"/>'
b+=figure(400,680,100,'#3a1a2a',pose='stand',hair='#c8a040')
b+='<ellipse cx="700" cy="400" rx="150" ry="180" fill="#0a0a1a"/><circle cx="640" cy="380" r="22" fill="#fff"/><circle cx="636" cy="380" r="10" fill="#0a0a1a"/>'
I[290]=svg(b,d)

# 291 I Had Some Help (Post Malone ft. Morgan Wallen, 2024): two cowboys at a dusty saloon bar each pointing at the other, pickup outside
d,b=bg([(0,'#3a2010'),(1,'#a86a3a')])
b+='<rect x="100" y="80" width="600" height="300" fill="#f2c88a" opacity=".5"/><rect y="520" width="800" height="280" fill="#3a1a08"/><rect y="500" width="800" height="30" fill="#6a3a14"/>'
for x,f in ((260,'reach'),(540,'reachL')): b+=figure(x,520,300,'#1a0a04',pose=f)+hat(x,262,40,'#1a0a04','#5a2a14')
I[291]=svg(b,d)

# 297 I Get Around (The Beach Boys, 1964): a hot-rod and a gang of guys cruising the boulevard with surfboards, palm trees, bright 60s sun
d,b=bg([(0,'#ffb03a'),(1,'#ffe8a0')])
b+=glow(620,160,90,'#fff8d0',.9)+palm(100,600,300,'#3a5a2a',8)+palm(720,600,280,'#3a5a2a',-8)
b+='<rect y="600" width="800" height="200" fill="#5a5a6a"/><path d="M0 700 L800 700" stroke="#fff" stroke-width="6" stroke-dasharray="40 30"/>'
b+=car(400,690,150,'#e0102a','#f2f2f2',glass='#bff0ff')+'<ellipse cx="380" cy="575" rx="170" ry="12" fill="#ffd23a"/>'
I[297]=svg(b,d)

# 306 Play That Funky Music (Wild Cherry, 1976): a funky bass guitar with a sparkly strap, afro pick, 70s orange-brown swirl
d,b=bg([(0,'#7a2a0a'),(1,'#e8902a')])
for k in range(7): b+=f'<circle cx="400" cy="400" r="{60+k*60}" fill="none" stroke="{["#ffd23a","#5a1a04"][k%2]}" stroke-width="30" opacity=".4"/>'
b+=eguitar(400,560,180,'#ffd23a','#3a1a04',rot=-25)
I[306]=svg(b,d)

# 310 Centerfold (The J. Geils Band, 1982): a high-school classroom chalkboard with a magazine center page falling open, desks in rows
d,b=bg([(0,'#3a4a3a'),(1,'#6a5a3a')])
b+='<rect x="80" y="80" width="640" height="300" fill="#1a3a2a" stroke="#8a5a2a" stroke-width="14"/>'+''.join(f'<path d="M{120+k*60} {130+k%3*60} l40 0" stroke="#f2f2e8" stroke-width="5" opacity=".6"/>' for k in range(9))
for i in range(3):
    for j in range(2): b+=f'<rect x="{120+i*220}" y="{500+j*140}" width="140" height="20" fill="#8a5a2a"/><rect x="{130+i*220}" y="{520+j*140}" width="10" height="60" fill="#5a3a1a"/><rect x="{250+i*220}" y="{520+j*140}" width="10" height="60" fill="#5a3a1a"/>'
b+='<g transform="translate(400 420) rotate(-10)"><rect x="-100" y="-70" width="200" height="140" fill="#fff"/><path d="M0 -70 L0 70" stroke="#ccc" stroke-width="3"/><rect x="-90" y="-60" width="80" height="120" fill="#ff8ab0"/><rect x="10" y="-60" width="80" height="120" fill="#ff8ab0"/></g>'
I[310]=svg(b,d)

# 311 I Feel for You (Chaka Khan, 1985): an electric breakdance street scene, a woman with a huge mane of hair, graffiti hearts and boombox
d,b=bg([(0,'#ff2a8a'),(1,'#3a0a6a')])
for k in range(5): b+=heart(100+k*150,150+(k%2)*80,40,['#3affe0','#ffe14a','#fff'][k%3],'opacity=".6"')
b+='<circle cx="400" cy="330" r="120" fill="#2a0a14"/>'+figure(400,780,460,'#1a0410',pose='up')
I[311]=svg(b,d)

# 312 Broken Wings (Mr. Mister, 1986): a bird with one torn wing silhouetted against a stormy moonlit sky, feathers drifting
d,b=bg([(0,'#0a0e1a'),(1,'#3a4a6a')])
b+=moon(400,300,110)+''.join(f'<ellipse cx="{x}" cy="{y}" rx="140" ry="40" fill="#1a2234" opacity=".85"/>' for x,y in ((200,220),(620,380),(320,440)))
b+='<g transform="translate(400 330)" fill="#04060c"><ellipse rx="40" ry="22"/><circle cx="36" cy="-10" r="14"/><path d="M0 -10 Q-80 -110 -200 -90 Q-120 -50 -20 0Z"/><path d="M0 -10 Q60 -80 110 -60 L90 -40 L120 -30 L80 -10Z"/></g>'
r=random.Random(312)
for k in range(8): x,y=r.uniform(420,620),r.uniform(380,700);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="16" ry="5" fill="#d8e0f0" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[312]=svg(b,d)

# 314 Miss You Much (Janet Jackson, 1989): a black-and-white militant dance formation, a woman in a black cap and jacket with chair choreography
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<rect y="600" width="800" height="200" fill="#0a0a0a"/>'
for x in (150,650): b+=figure(x,700,300,'#5a5a5a',pose='reach' if x<400 else 'reachL')
b+=figure(400,720,400,'#000',pose='up')+'<path d="M368 330 Q400 300 432 330 L460 336 L368 336Z" fill="#000"/>'
b+='<path d="M360 720 L360 640 L440 640 L440 720 M360 640 L360 580" stroke="#f2f2f2" stroke-width="10" fill="none"/>'
I[314]=svg(b,d)

# 316 Baby-Baby-Baby (TLC, 1992): three girls in baggy colorful overalls and caps striking hip-hop poses, condoms-awareness-era neon
d,b=bg([(0,'#3ad8ff'),(1,'#ff6ac0')])
for x,c in ((250,'#ffd23a'),(400,'#2ae07a'),(550,'#ff3a3a')): b+=figure(x,760,360,c,pose='wave' if x==400 else 'stand',hair='#1a1a1a')
I[316]=svg(b,d)

# 318 Hero (Mariah Carey, 1994): a small figure on a mountain peak with arms open to a radiant sunrise, light pouring out
d,b=bg([(0,'#3a4a8a'),(.6,'#f2a06a'),(1,'#fff0c0')])
b+=glow(400,420,220,'#fff8d8',.9)+rays(400,420,30,'#fff8e0',.2,10)
b+='<path d="M0 800 L0 640 L220 520 L400 360 L560 500 L800 600 L800 800Z" fill="#2a2030"/>'+figure(400,370,120,'#1a1420',pose='up')
I[318]=svg(b,d)

# 319 On Bended Knee (Boyz II Men, 1995): a man kneeling in a rainy street holding up an open ring box, umbrella beside him
d,b=bg([(0,'#0a1020'),(1,'#2a3a5a')])
b+=rain(120,319,'#cfe0ff',.35,4)+'<rect y="640" width="800" height="160" fill="#0a0e18"/>'
b+='<g fill="#04060c" transform="translate(400 700)"><circle cx="0" cy="-250" r="24"/><path d="M-26 -226 L26 -226 L24 -120 L-24 -120Z"/><path d="M-24 -120 L24 -120 L70 -60 L70 0 L50 0 L50 -50 L10 -80 L-30 0 L-60 0Z"/><path d="M20 -214 Q80 -200 110 -200" stroke="#04060c" stroke-width="16" fill="none"/></g>'
b+='<rect x="500" y="480" width="40" height="30" fill="#3a1a2a"/>'+glow(520,478,20,'#fff',.9,'glow2')+'<circle cx="520" cy="476" r="8" fill="none" stroke="#e8c040" stroke-width="4"/>'
I[319]=svg(b,d)

# 320 Always Be My Baby (Mariah Carey, 1996): a rope swing hanging from a big oak over a summer-camp lake at night, a campfire glowing
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
b+=starsf(90,320,500)+moon(620,140,40)+'<rect y="500" width="800" height="300" fill="#0a1a3a"/>'+''.join(f'<path d="M{k*80} {540+k%3*40} q20 -8 40 0" stroke="#cfe0ff" stroke-width="3" fill="none" opacity=".4"/>' for k in range(10))
b+='<path d="M0 520 Q100 160 300 140 Q340 100 420 140" stroke="#06080e" stroke-width="40" fill="none"/><ellipse cx="300" cy="140" rx="200" ry="80" fill="#06080e"/>'
b+='<path d="M340 160 L340 420 M380 160 L380 420" stroke="#c8a070" stroke-width="3"/><rect x="330" y="420" width="60" height="10" fill="#8a5a2a"/>'
b+='<path d="M120 660 L180 660" stroke="#3a2010" stroke-width="10"/>'+glow(150,620,40,'#ff8a2a',.9)+'<path d="M130 650 Q150 590 170 650Z" fill="#ffb03a"/>'
I[320]=svg(b,d)

# 322 Everything You Want (Vertical Horizon, 2000): a man reaching for a floating light just out of reach on a gray city rooftop
d,b=bg([(0,'#2a3a4a'),(1,'#8a9aa8')])
b+=skyline(600,'#2a3440',322,60,200,None)+'<rect y="620" width="800" height="180" fill="#1a2028"/>'
b+=figure(340,740,330,'#0a0e14',pose='reach')+glow(560,380,50,'#fff2c0',.9)+'<circle cx="560" cy="380" r="20" fill="#fffbe0"/>'
I[322]=svg(b,d)

# 323 I'm Real (Jennifer Lopez ft. Ja Rule, 2001): a woman in a velour tracksuit and hoop earrings on a Bronx stoop, sunset brick
d,b=bg([(0,'#8a3a1a'),(1,'#e8905a')])
for i in range(12):
    for j in range(16): b+=f'<rect x="{i*70+(j%2)*35-35}" y="{j*36}" width="66" height="32" fill="#a84a2a" opacity=".6"/>'
b+='<rect x="200" y="560" width="400" height="40" fill="#5a3a2a"/><rect x="160" y="600" width="480" height="40" fill="#4a2a1a"/><rect y="640" width="800" height="160" fill="#3a2010"/>'
b+=figure(400,560,320,'#e8d8f0',pose='stand',hair='#3a1a0a')+'<circle cx="378" cy="340" r="10" fill="none" stroke="#e8c040" stroke-width="3"/><ellipse cx="400" cy="250" rx="21" ry="25" fill="#c88a5a"/>'
I[323]=svg(b,d)

# 324 Wherever You Will Go (The Calling, 2002): a lone guitarist on a cliff overlooking a stormy sea, a lighthouse beam sweeping
d,b=bg([(0,'#0a1420'),(1,'#3a4a5a')])
b+='<rect y="560" width="800" height="240" fill="#1a2a3a"/>'+''.join(f'<path d="M{k*80} {600+k%3*40} q20 -12 40 0" stroke="#cfe0ff" stroke-width="4" fill="none" opacity=".5"/>' for k in range(10))
b+='<rect x="640" y="300" width="40" height="260" fill="#e8e0d8"/><rect x="636" y="280" width="48" height="30" fill="#2a2a3a"/>'+glow(660,290,30,'#fff2c0',.9)+'<path d="M660 290 L0 160 L0 260Z" fill="#fff2c0" opacity=".15"/>'
b+='<path d="M0 800 L0 580 L300 560 Q340 640 300 800Z" fill="#0a0e14"/>'+figure(180,580,220,'#04060a',pose='hold')
I[324]=svg(b,d)

# 325 When I'm Gone (3 Doors Down, 2003): a soldier's dog tags and a folded letter on a duffel bag, an American flag faintly behind
d,b=bg([(0,'#2a2a2a'),(1,'#5a5040')])
b+=flagstripes(100,500,.15)
b+='<path d="M120 640 Q120 520 400 520 Q680 520 680 640 Q680 720 400 720 Q120 720 120 640Z" fill="#5a5a3a"/><path d="M200 560 L600 560" stroke="#3a3a24" stroke-width="10"/>'
b+='<rect x="300" y="420" width="200" height="120" fill="#f2ead8" transform="rotate(-8 400 480)"/>'
b+='<path d="M440 360 Q480 480 520 560" stroke="#c8c8d0" stroke-width="3" fill="none"/><rect x="490" y="540" width="60" height="36" rx="12" fill="#c8c8d0"/><rect x="510" y="560" width="60" height="36" rx="12" fill="#a8a8b0"/>'
I[325]=svg(b,d)

# 326 The Way You Move (OutKast, 2004): a vintage Cadillac bouncing on hydraulics under spotlights, a swing-dance couple beside it
d,b=bg([(0,'#1a0a2a'),(1,'#7a2a4a')])
for x in (200,600): b+=spotlight(x,0,140,'#ffe0c0',.14)
b+='<rect y="640" width="800" height="160" fill="#0e0410"/>'+car(500,700,140,'#7a4aff','#f2f2f2')+''.join(f'<path d="M{x} 720 l0 20" stroke="#ffd84a" stroke-width="4"/>' for x in (330,670))
b+=figure(160,740,260,'#0a0410',pose='reach')+figure(250,740,250,'#0a0410',pose='up',hair='#0a0410')
I[326]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
