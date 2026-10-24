import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 3. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 41 Jump (Van Halen, 1984): a spandex rocker frozen mid-air in a split jump above a stage, big synth-pink lights
d,b=bg([(0,'#12062a'),(1,'#ff4a9a')])
b+=rays(400,800,30,'#ffe0f0',.12,10)+'<rect y="660" width="800" height="140" fill="#14061a"/>'
b+='<g transform="translate(400 330)" fill="#0a0410"><circle cx="0" cy="-120" r="30"/><path d="M-28 -150 Q-60 -130 -50 -90 M28 -150 Q60 -130 50 -90" stroke="#0a0410" stroke-width="14"/>'
b+='<path d="M-30 -92 L30 -92 L24 0 L-24 0Z"/><path d="M-20 -4 L-240 30 L-236 52 L-10 22Z"/><path d="M20 -4 L240 30 L236 52 L10 22Z"/>'
b+='<path d="M-26 -84 Q-90 -150 -110 -200" stroke="#0a0410" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M26 -84 Q90 -150 110 -200" stroke="#0a0410" stroke-width="16" fill="none" stroke-linecap="round"/></g>'
b+='<path d="M180 370 L620 370" stroke="#ffd84a" stroke-width="4" stroke-dasharray="6 14" opacity=".7"/>'
for x in (120,680): b+=f'<rect x="{x-50}" y="560" width="100" height="100" fill="#0a0410"/><circle cx="{x}" cy="610" r="34" fill="#2a1a3a"/>'
I[41]=svg(b,d)

# 42 About Damn Time (Lizzo, 2022): a disco-sparkle jumpsuit dancer with a little flute, glitter rain on hot orange
d,b=bg([(0,'#ff6a2a'),(1,'#ffc23a')])
b+=disco(620,140,70)+confetti(60,42,['#fff','#ffe0f0','#ff3a8a'],0,800,.8)
b+=figure(380,760,440,'#7a0a5a',pose='wave',hair='#2a0a1a')
b+='<path d="M460 300 L560 230" stroke="#e8e8f0" stroke-width="10" stroke-linecap="round"/>'+''.join(f'<circle cx="{480+k*18}" cy="{286-k*13}" r="3" fill="#555"/>' for k in range(4))
for k in range(12): b+=sparkle(330+(k%4)*30,420+(k//4)*60,8,'#fff2a0')
I[42]=svg(b,d)

# 43 No Diggity (Blackstreet ft. Dr. Dre, 1996): a smoky 90s back room, a man in a fedora seen from behind, a wall of black-and-white jazz light
d,b=bg([(0,'#0a0a0c'),(1,'#3a3a40')])
b+=spotlight(560,0,180,'#f2f2e8',.2)
for k in range(9): b+=f'<rect x="{k*90}" y="100" width="60" height="420" fill="#f2f2e8" opacity=".05"/>'
b+=figure(400,800,520,'#060608',pose='stand')+hat(400,290,62,'#060608','#3a3a40')
b+='<path d="M560 380 q-30 -60 10 -120 q40 -60 0 -120" stroke="#cfcfd8" stroke-width="10" fill="none" opacity=".25"/>'
I[43]=svg(b,d)

# 44 Livin' on a Prayer (Bon Jovi, 1986): two young lovers on a working-class rooftop at night, a talk box mic stand and stadium beams
d,b=bg([(0,'#06081a'),(1,'#2a2a5a')])
for a in (-30,-10,10,30): b+=f'<path d="M400 800 L{400+a*20} 0 L{440+a*20} 0Z" fill="#cfe0ff" opacity=".07"/>'
b+=skyline(560,'#10122a',44,60,180,'#ffd27a',60)+'<rect y="620" width="800" height="180" fill="#0a0a1a"/>'
b+=figure(340,640,260,'#e8e0d8',pose='stand',hair='#3a2a1a')+figure(430,640,230,'#e8e0d8',pose='stand',hair='#8a5a2a')
b+='<path d="M372 450 Q390 440 408 450" stroke="#e8e0d8" stroke-width="12" fill="none"/>'+heart(390,380,26,'#ff3a5a')
I[44]=svg(b,d)

# 45 Like a Prayer (Madonna, 1989): a field of burning votive candles before a dark church, a gold cross in the glow
d,b=bg([(0,'#0a0404'),(1,'#3a1004')])
b+='<path d="M220 500 L220 220 Q400 60 580 220 L580 500Z" fill="#1a0806"/>'+glow(400,260,90,'#ffd27a',.5)
b+='<path d="M392 180 L408 180 L408 230 L436 230 L436 246 L408 246 L408 320 L392 320 L392 246 L364 246 L364 230 L392 230Z" fill="#e8b84a"/>'
r=random.Random(45)
for k in range(40):
    x,y=r.uniform(20,780),r.uniform(560,780);s=(y-500)/280
    b+=f'<rect x="{x-8*s:.0f}" y="{y-40*s:.0f}" width="{16*s:.0f}" height="{40*s:.0f}" fill="#f2e6c8"/>'+glow(round(x),round(y-50*s),round(20*s),'#ffb84a',.7,'glow2')+f'<ellipse cx="{x:.0f}" cy="{y-48*s:.0f}" rx="{5*s:.1f}" ry="{10*s:.1f}" fill="#ffe08a"/>'
I[45]=svg(b,d)

# 46 is no video yet
# 47 Mr. Brightside (The Killers, 2003): a jealous figure in a velvet theatre box, red curtains and a cold blue spotlight on a couple below
d,b=bg([(0,'#1a0408'),(1,'#4a0a14')])
b+='<path d="M0 0 L180 0 Q120 400 160 800 L0 800Z M800 0 L620 0 Q680 400 640 800 L800 800Z" fill="#a8101e"/>'
for x in (40,90,140,660,710,760): b+=f'<path d="M{x} 0 Q{x-20} 400 {x} 800" stroke="#6a0a14" stroke-width="10" fill="none"/>'
b+=spotlight(400,0,200,'#9ad0ff',.2)+'<ellipse cx="400" cy="720" rx="160" ry="30" fill="#9ad0ff" opacity=".2"/>'
b+=figure(370,720,200,'#060208',pose='hold')+figure(430,720,210,'#060208',pose='hold')
b+='<path d="M220 300 L320 300 L320 360 L220 360Z" fill="#d4a63a"/>'+figure(270,310,130,'#060208',pose='stand')
I[47]=svg(b,d)

# 48 Just the Way You Are (Bruno Mars, 2010): a girl's face in silhouette with stars caught in her eyes and hair, soft pink-gold
d,b=bg([(0,'#2a1a3a'),(1,'#f0a0a0')])
b+=starsf(80,48,800,'#fff2e0')+glow(420,400,220,'#ffd8e0',.5)
b+=profile(330,420,1.3,'#1a0e1a')
for x,y in ((300,300),(260,380),(350,240),(420,270)): b+=sparkle(x,y,18,'#fff2c0')
b+=sparkle(560,330,26,'#fff')
I[48]=svg(b,d)

# 49 We Are the World (USA for Africa, 1985): a choir of many voices with headphones around studio mics, a globe glowing above
d,b=bg([(0,'#04102a'),(1,'#2a4a7a')])
b+=glow(400,220,170,'#9ad8ff',.5)+'<circle cx="400" cy="220" r="120" fill="#2a6ab0"/>'
b+='<path d="M340 150 Q380 130 400 170 Q420 210 380 240 Q350 230 340 150Z M430 180 Q480 170 490 220 Q470 280 440 290 Q420 250 430 180Z" fill="#4ab07a"/>'
for k in range(11):
    x=60+k*68;y=780-(k%2)*40;b+=figure(x,y,220,'#0a0e1a',pose='stand')+f'<path d="M{x-17} {y-198} Q{x} {y-232} {x+17} {y-198}" stroke="#d8d8e0" stroke-width="4" fill="none"/>'
b+=mic(400,520,50,'#c8c8d0',stand=False)
I[49]=svg(b,d)

# 50 Family Affair (Mary J. Blige, 2001): a packed hip-hop-soul dance floor, everybody hands up in purple and gold, a disco floor glowing
d,b=bg([(0,'#1a0630'),(1,'#5a1a6a')])
b+=disco(400,110,60)+rays(400,110,26,'#ffd84a',.1,8)
for i in range(6):
    for j in range(3): b+=f'<path d="M{i*140-40+j*40} {600+j*70} l140 0 l40 70 l-140 0Z" fill="{["#ffd84a","#ff4ab0","#4ad8ff"][(i+j)%3]}" opacity=".35"/>'
for k,x in enumerate((110,230,340,460,570,690)): b+=figure(x,720+(k%2)*30,250+(k%3)*20,'#0e0418',pose='up' if k%2==0 else 'wave',hair='#0e0418')
I[50]=svg(b,d)

# 52 Africa (Toto, 1982): rain falling on a savanna at dusk, Kilimanjaro rising over the Serengeti, a lone acacia
d,b=bg([(0,'#2a2a4a'),(.6,'#c86a3a'),(1,'#f0b05a')])
b+='<path d="M300 520 L470 300 L520 340 L560 310 L700 520Z" fill="#4a3a4a"/><path d="M450 326 L470 300 L520 340 L560 310 L580 340 Q520 360 450 326Z" fill="#f2f2f2"/>'
b+=rain(140,52,'#e0e8ff',.35,10)+'<rect y="560" width="800" height="240" fill="#5a3a1a"/>'
b+='<path d="M180 560 L184 440" stroke="#1a0e08" stroke-width="12"/><ellipse cx="180" cy="430" rx="120" ry="26" fill="#1a0e08"/><ellipse cx="200" cy="410" rx="70" ry="18" fill="#1a0e08"/>'
for x in (560,600,640): b+=f'<path d="M{x} 600 l10 -40 l6 0 l0 -30 l14 0 l-4 30 l20 0 l6 40" fill="#1a0e08"/>'
I[52]=svg(b,d)

# 53 Smells Like Teen Spirit (Nirvana, 1991): a dark gymnasium pep rally with smoke, a cheerleader's pom-poms and a battered guitar, anarchy symbol on the bleachers
d,b=bg([(0,'#0a0a06'),(1,'#3a3a14')])
for k in range(6): b+=f'<rect x="0" y="{200+k*50}" width="800" height="12" fill="#5a4a24" opacity=".6"/>'
b+='<ellipse cx="400" cy="560" rx="400" ry="160" fill="#c8c0a0" opacity=".12" filter="url(#glow)"/>'
b+=eguitar(420,560,140,'#2a2a2e','#1a1206',rot=-20)
for x,c in ((180,'#f2e04a'),(640,'#f2e04a')):
    for k in range(18): a=k*0.35;b+=f'<path d="M{x} 640 l{60*math.cos(a):.0f} {60*math.sin(a):.0f}" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
b+='<circle cx="660" cy="160" r="50" fill="none" stroke="#e8e0c0" stroke-width="8" opacity=".6"/><path d="M630 200 L660 120 L690 200 M638 170 L682 170" stroke="#e8e0c0" stroke-width="8" fill="none" opacity=".6"/>'
I[53]=svg(b,d)

# 54 Oh, Pretty Woman (Roy Orbison, 1964): a pair of black sunglasses reflecting a woman in red walking down a 60s street
d,b=bg([(0,'#f0c06a'),(1,'#c86a3a')])
b+='<rect y="560" width="800" height="240" fill="#6a3a2a"/>'
for cx in (260,540):
    b+=f'<path d="M{cx-140} 330 Q{cx} 300 {cx+140} 330 Q{cx+130} 470 {cx} 470 Q{cx-130} 470 {cx-140} 330Z" fill="#0a0a10"/>'
    b+=f'<path d="M{cx-100} 350 Q{cx-60} 340 {cx-30} 352" stroke="#fff" stroke-width="6" opacity=".4" fill="none"/>'
    b+=figure(cx+20,450,110,'#e0102a',pose='stand',hair='#2a1a0a')
b+='<path d="M400 340 Q400 320 400 340" stroke="#0a0a10" stroke-width="20"/><path d="M380 330 Q400 316 420 330" stroke="#0a0a10" stroke-width="14" fill="none"/>'
I[54]=svg(b,d)

# 55 Since U Been Gone (Kelly Clarkson, 2004): a broken-up apartment scene, a framed photo smashed on the floor, bright pop-punk pink light
d,b=bg([(0,'#2a0a2a'),(1,'#ff4a8a')])
b+='<g transform="translate(400 470) rotate(-8)"><rect x="-200" y="-150" width="400" height="300" fill="#2a1a0a"/><rect x="-176" y="-126" width="352" height="252" fill="#9ad0ff"/>'
b+=figure(-50,120,200,'#2a3a5a',pose='stand')+figure(60,120,210,'#2a3a5a',pose='stand')
b+='<path d="M-176 -126 L-40 -10 L-120 126 M-40 -10 L120 -126 M-40 -10 L176 60 M-40 -10 L30 126" stroke="#fff" stroke-width="5" fill="none"/></g>'
r=random.Random(55)
for k in range(14): x,y=r.uniform(100,700),r.uniform(660,780);b+=f'<path d="M{x:.0f} {y:.0f} l{r.uniform(10,30):.0f} {r.uniform(-12,12):.0f} l{r.uniform(-20,0):.0f} {r.uniform(6,20):.0f}Z" fill="#e8f6ff" opacity=".8"/>'
I[55]=svg(b,d)

# 57 In da Club (50 Cent, 2003): a lab-like club with cold green lights, a big birthday cake with sparklers on a VIP table
d,b=bg([(0,'#020a06'),(1,'#0a3a2a')])
for x in (150,400,650): b+=spotlight(x,0,120,'#6aff9a',.1)
b+='<rect x="160" y="620" width="480" height="40" fill="#1a1a1a"/><rect x="240" y="520" width="320" height="100" rx="10" fill="#f2f0e8"/><rect x="290" y="440" width="220" height="80" rx="10" fill="#f6f4ee"/>'
b+='<path d="M240 560 q40 20 80 0 q40 20 80 0 q40 20 80 0 q40 20 80 0" stroke="#e8c84a" stroke-width="8" fill="none"/>'
for x in (330,400,470):
    b+=f'<rect x="{x-4}" y="380" width="8" height="60" fill="#e8e8e8"/>'+glow(x,370,26,'#fff8c0',.9,'glow2')
    for k in range(8): a=k*0.785;b+=f'<path d="M{x} 370 l{24*math.cos(a):.0f} {24*math.sin(a):.0f}" stroke="#fff2a0" stroke-width="3"/>'
I[57]=svg(b,d)

# 58 Yeah! (Usher ft. Lil Jon & Ludacris, 2004): a laser-filled club, a sharp dancer in a white tank sliding across a glowing floor
d,b=bg([(0,'#04020e'),(1,'#1a0a3a')])
for k in range(10): b+=f'<path d="M{k*80} 0 L{400+(k-5)*20} 560" stroke="{["#4ad8ff","#ff3ab0"][k%2]}" stroke-width="4" opacity=".6"/>'
b+='<path d="M0 560 L800 560 L800 800 L0 800Z" fill="#100620"/>'+''.join(f'<path d="M{400+(k-6)*70} 560 L{400+(k-6)*200} 800" stroke="#4ad8ff" stroke-width="2" opacity=".4"/>' for k in range(13))
b+=glow(400,560,170,'#ff3ab0',.5)+figure(400,720,330,'#0a0414',pose='reach')+'<path d="M374 470 L426 470 L422 560 L378 560Z" fill="#f6f6f6"/>'
I[58]=svg(b,d)

# 59 We Belong Together (Mariah Carey, 2005): a bride-like figure in a long white gown walking away down a dim aisle, an old radio glowing
d,b=bg([(0,'#1a1410'),(1,'#5a4434')])
b+=glow(400,160,120,'#ffe8c0',.3)
b+='<path d="M360 800 L380 300 L420 300 L440 800Z" fill="#8a2a2a" opacity=".6"/>'
b+='<g transform="translate(400 560)"><circle cx="0" cy="-200" r="22" fill="#2a1a10"/><path d="M-20 -200 Q-40 -120 -30 -60" stroke="#2a1a10" stroke-width="20" fill="none"/>'
b+='<path d="M-30 -176 L30 -176 L40 -80 Q120 120 160 220 L-160 220 Q-120 120 -40 -80Z" fill="#f6f2ea"/></g>'
b+='<rect x="590" y="620" width="150" height="100" rx="14" fill="#6a3a1a"/><circle cx="630" cy="670" r="28" fill="#2a1a0a"/><rect x="680" y="646" width="44" height="12" fill="#ffd27a"/>'+note(690,560,26,'#ffe0a0')
I[59]=svg(b,d)

# 60 Old Town Road (Lil Nas X ft. Billy Ray Cyrus, 2019): a cowboy on a horse riding toward a glowing horizon, black cowboy hat, wide western sky
d,b=bg([(0,'#1a2a5a'),(.6,'#e88a4a'),(1,'#f6d27a')])
b+=glow(400,560,180,'#fff2c0',.8)+hills(580,16,'#6a3a2a',60,4)+'<rect y="620" width="800" height="180" fill="#3a2214"/>'+road(400,580,'#5a3a24','#5a3a24',300)
b+=cactus(120,640,160)+cactus(700,640,130)
b+='<g transform="translate(400 620)" fill="#14080a"><path d="M-110 -110 Q-60 -150 40 -140 Q80 -180 110 -160 L100 -120 Q70 -120 70 -90 L60 0 L46 0 L40 -70 L-60 -70 L-80 0 L-94 0 L-90 -80 Q-130 -60 -150 -90Z"/>'
b+='<path d="M-20 -150 L10 -150 L16 -230 L-26 -230Z"/><circle cx="-6" cy="-250" r="18"/></g>'+hat(394,370,40,'#14080a','#2a1a10')
I[60]=svg(b,d)

# 61 Last Night (Morgan Wallen, 2023): a pickup truck tailgate under a porch light at night, a bottle of Jack and a screen door swinging open
d,b=bg([(0,'#04060e'),(1,'#1a2034')])
b+=starsf(60,61,360)+'<rect y="560" width="800" height="240" fill="#0e1218"/>'
b+='<rect x="440" y="260" width="300" height="300" fill="#2a1e14"/><rect x="520" y="340" width="110" height="220" fill="#ffd27a" opacity=".85"/><path d="M520 340 L590 360 L590 580 L520 560Z" fill="#3a2a1a" opacity=".85"/>'+glow(560,300,40,'#ffe0a0',.9)
b+='<g fill="#5a1a14"><path d="M60 640 L60 560 L200 560 L240 500 L360 500 L380 560 L420 560 L420 640Z"/></g><path d="M250 510 L350 510 L360 556 L240 556Z" fill="#9ac0ff" opacity=".4"/>'
for x in (130,350): b+=f'<circle cx="{x}" cy="650" r="36" fill="#0a0a0a"/><circle cx="{x}" cy="650" r="14" fill="#888"/>'
b+='<rect x="96" y="512" width="22" height="48" rx="5" fill="#2a1a0a"/><rect x="102" y="498" width="10" height="16" fill="#2a1a0a"/>'
I[61]=svg(b,d)

# 63 Don't Worry, Be Happy (Bobby McFerrin, 1988): a big whistling smiley sun over a tropical beach, palm trees and calm waves
d,b=bg([(0,'#3ab0e8'),(1,'#bff0ff')])
b+=glow(400,270,180,'#fff2a0',.8)+'<circle cx="400" cy="270" r="130" fill="#ffd23a"/>'
b+='<circle cx="355" cy="240" r="14" fill="#2a1a0a"/><circle cx="445" cy="240" r="14" fill="#2a1a0a"/><path d="M330 300 Q400 360 470 300" stroke="#2a1a0a" stroke-width="12" fill="none" stroke-linecap="round"/>'
b+=note(560,160,30,'#fff')+note(620,220,24,'#fff',True)
b+='<rect y="540" width="800" height="120" fill="#2a8ac8"/>'+''.join(f'<path d="M{k*80} 560 q20 -12 40 0 q20 12 40 0" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>' for k in range(10))
b+='<rect y="640" width="800" height="160" fill="#f6dfa0"/>'+palm(110,700,340,'#1a5a3a',10)+palm(700,700,300,'#1a5a3a',-12)
I[63]=svg(b,d)

# 64 One Sweet Day (Mariah Carey & Boyz II Men, 1995): five singers in silhouette under shafts of heavenly light breaking through clouds
d,b=bg([(0,'#3a4a6a'),(1,'#d8d0c0')])
for k in range(7): b+=f'<path d="M{300+k*30} 120 L{100+k*100} 800 L{150+k*100} 800Z" fill="#fff8e0" opacity=".12"/>'
for k in range(6): b+=f'<ellipse cx="{k*150}" cy="{110+(k%2)*30}" rx="160" ry="60" fill="#f2f0ea" opacity=".85"/>'
b+=glow(400,140,110,'#fff8d8',.9)+'<rect y="700" width="800" height="100" fill="#2a2a34"/>'
for k,x in enumerate((180,290,400,510,620)): b+=figure(x,720,240+(k==2)*20,'#1a1a24',pose='stand',hair='#1a1a24' if k==2 else None)
I[64]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
