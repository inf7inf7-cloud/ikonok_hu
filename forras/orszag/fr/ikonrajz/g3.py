import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 3. csoport (Top 41–60)
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 41 Je veux: a street singer with a big smile on a Paris cobbled square, refusing a suite at the Ritz and diamonds
d,b=bg([(0,'#ffd08a'),(.6,'#ff9a6a'),(1,'#a84a4a')])
b+=roofs(440,'#6a2a3a',41)
b+='<rect y="600" width="800" height="200" fill="#5a3a3a"/>'+''.join(f'<ellipse cx="{(i*70+(j%2)*35)%840-20}" cy="{620+j*34}" rx="30" ry="12" fill="#6a4a46"/>' for i in range(12) for j in range(6))
b+=figure(400,700,360,'#2a0a14',pose='up',hair='#2a0a14')
b+=guitar(470,560,.9,rot=-30)
b+='<path d="M600 640 L640 600 L680 640 L640 690Z" fill="#dff0ff" opacity=".9"/><path d="M640 600 L640 690" stroke="#9ab8e0" stroke-width="2"/>'
b+='<path d="M560 700 L700 700" stroke="#2a0a14" stroke-width="5"/><path d="M590 680 L680 720" stroke="#2a0a14" stroke-width="8"/>'
I[41]=svg(b,d)

# 42 La Boulette: a furious young woman in a hoodie stands before a grey suburb, fist raised, a lit fuse beside her
d,b=bg([(0,'#3a3a44'),(.6,'#6a6a74'),(1,'#d8603a')])
b+='<rect x="40" y="260" width="160" height="440" fill="#2a2a30"/><rect x="560" y="200" width="200" height="500" fill="#24242a"/>'
for x0,w in ((40,160),(560,200)):
    for i in range(w//40):
        for j in range(10): b+=f'<rect x="{x0+12+i*40}" y="{220+(1 if x0==40 else 0)*60+j*44}" width="18" height="22" fill="{"#ffb84a" if (i+j)%5==0 else "#3a3a44"}"/>'
b+='<rect y="700" width="800" height="100" fill="#1a1a1e"/>'
b+=figure(400,720,420,'#0a0a0c',pose='up')
b+='<path d="M366 330 Q400 296 434 330 L440 380 L360 380Z" fill="#0a0a0c"/>'
b+='<circle cx="640" cy="680" r="40" fill="#0a0a0c"/><path d="M660 646 Q680 610 700 600" stroke="#c8a06a" stroke-width="5" fill="none"/>'+sparkle(704,596,22,'#ffd23f')+glow(704,596,50,'#ff8a3a',.6)
I[42]=svg(b,d)

# 43 Andalouse: a flamenco dancer in a red dress swirling under a hot Andalusian sun, a gipsy guitar beside her
d,b=bg([(0,'#ffd23f'),(.55,'#ff8a2a'),(1,'#c8301a')])
b+=sun(400,200,90,'#fff4a0')
b+='<rect y="640" width="800" height="160" fill="#8a2a14"/>'
b+='<ellipse cx="400" cy="300" rx="22" ry="26" fill="#1a0806"/><path d="M380 276 Q400 250 420 276" fill="#1a0806"/><circle cx="414" cy="282" r="9" fill="#d81a3a"/>'
b+='<path d="M380 326 Q400 318 420 326 L426 430 L374 430Z" fill="#1a0806"/><path d="M380 336 Q320 280 300 220 M420 336 Q490 300 520 250" stroke="#1a0806" stroke-width="13" fill="none" stroke-linecap="round"/>'
b+='<path d="M374 420 Q260 520 210 640 Q300 600 330 660 Q380 610 420 670 Q460 610 500 660 Q540 600 600 640 Q540 520 426 420Z" fill="#d81a2a"/><path d="M210 640 Q300 600 330 660 Q380 610 420 670 Q460 610 500 660 Q540 600 600 640" stroke="#1a0806" stroke-width="8" fill="none"/>'
b+=guitar(660,560,1.0,rot=20)
I[43]=svg(b,d)

# 44 Spider: a huge glowing spider web spreads across the night, a man in sunglasses caught in the middle of it
d,b=bg([(0,'#020206'),(.6,'#0a0a20'),(1,'#1a0a30')])
cx,cy=400,360
for k in range(12):
    a=k*math.pi/6;b+=f'<path d="M{cx} {cy} L{cx+math.cos(a)*560:.0f} {cy+math.sin(a)*560:.0f}" stroke="#bfe0ff" stroke-width="2.4" opacity=".7"/>'
for r_ in range(60,560,55):
    pts=' '.join(f'{cx+math.cos(k*math.pi/6)*r_:.0f},{cy+math.sin(k*math.pi/6)*r_:.0f}' for k in range(13));b+=f'<polyline points="{pts}" fill="none" stroke="#bfe0ff" stroke-width="2" opacity=".55"/>'
b+=glow(cx,cy,260,'#4a8aff',.15)
b+=figure(400,640,330,'#000',pose='up')+'<rect x="384" y="350" width="34" height="9" rx="4" fill="#4af0ff"/>'
b+='<g transform="translate(640 160)" fill="#000"><ellipse rx="30" ry="36"/><circle cy="-40" r="20"/>'+''.join(f'<path d="M0 0 Q{s*60} {-30+i*20} {s*90} {-10+i*30}" stroke="#000" stroke-width="7" fill="none"/>' for s in (-1,1) for i in range(4))+'</g>'
b+='<path d="M640 0 L640 120" stroke="#bfe0ff" stroke-width="2"/>'
I[44]=svg(b,d)

# 45 L'Été indien: a couple walks barefoot on a deserted beach in an autumn dawn, the sea glowing orange and gold
d,b=bg([(0,'#f8c07a'),(.5,'#f08a5a'),(1,'#7a4a6a')])
b+=sun(400,420,70,'#fff0b0')
b+='<rect y="420" width="800" height="180" fill="#e8806a"/>'+waves(440,'#f8b07a',6,10,.6)+waves(500,'#d8705a',6,10,.6)
b+='<path d="M0 580 Q400 550 800 580 L800 800 L0 800Z" fill="#e8c8a0"/><path d="M0 580 Q400 550 800 580 L800 600 Q400 570 0 600Z" fill="#fff" opacity=".5"/>'
b+=figure(360,740,260,'#3a1a2a',pose='hold',hair='#3a1a2a')+figure(420,740,280,'#3a1a2a',pose='hold')
for k in range(5): b+=f'<ellipse cx="{300-k*50}" cy="{760+k*6}" rx="8" ry="4" fill="#b89070"/><ellipse cx="{440+k*-10-k*45}" cy="{770+k*5}" rx="8" ry="4" fill="#b89070"/>'
for x,y in [(160,150),(200,180),(600,120)]: b+=bird(x,y,14,'#5a2a3a')
I[45]=svg(b,d)

# 46 Get Lucky: two shining robot helmets (one gold, one chrome) on a disco floor under a glittering mirror ball
d,b=bg([(0,'#1a0a2a'),(.6,'#3a1a4a'),(1,'#0a0a14')])
b+=discoball(400,100,50)+rays(400,100,18,'#ffffff',.06,4)
for i in range(6):
    for j in range(3): b+=f'<polygon points="{-100+i*180+j*60},{620+j*60} {60+i*180+j*60},{620+j*60} {80+i*180+j*80},{680+j*60} {-80+i*180+j*80},{680+j*60}" fill="{["#ff3a8a","#3ad0ff","#ffd23f","#8a3aff"][(i+j)%4]}" opacity=".7"/>'
for x,c,v in [(270,'#e8b43a','#1a1a1a'),(530,'#d8dde8','#1a1a1a')]:
    b+=f'<ellipse cx="{x}" cy="380" rx="115" ry="140" fill="{c}"/><ellipse cx="{x-30}" cy="330" rx="40" ry="60" fill="#fff" opacity=".35"/>'
    b+=f'<rect x="{x-90}" y="350" width="180" height="70" rx="30" fill="{v}"/>'
b+='<rect x="460" y="362" width="140" height="46" rx="20" fill="#ff3a3a" opacity=".85"/>'+''.join(f'<rect x="{200+k*12}" y="372" width="6" height="26" fill="#ffd23f" opacity="{.4+k%3*.2}"/>' for k in range(12))
I[46]=svg(b,d)

# 47 La Vie en rose: Paris seen through rose-tinted glasses: pink sky, pink roofs, a rose and the Eiffel Tower all blush
d,b=bg([(0,'#ffd8e6'),(.6,'#ffa8c8'),(1,'#d8608a')])
b+=glow(400,300,300,'#fff0f6',.5)
b+=eiffel(600,640,460,'#b8406a')
b+=roofs(600,'#a8305a',47)
b+='<g transform="translate(260 360)"><ellipse cx="-120" cy="0" rx="110" ry="80" fill="#ff7aa8" opacity=".55"/><ellipse cx="120" cy="0" rx="110" ry="80" fill="#ff7aa8" opacity=".55"/>'
b+='<ellipse cx="-120" cy="0" rx="110" ry="80" fill="none" stroke="#3a0a1a" stroke-width="12"/><ellipse cx="120" cy="0" rx="110" ry="80" fill="none" stroke="#3a0a1a" stroke-width="12"/><path d="M-12 -10 Q0 -24 12 -10" stroke="#3a0a1a" stroke-width="12" fill="none"/></g>'
b+=rose(200,690,1.3,'#d81a4a',stem=False)
I[47]=svg(b,d)

# 48 La Montagne: a village in the mountains where old folk stay while the young leave on the road down to the city
d,b=bg([(0,'#8ab8e0'),(.6,'#d0e0e8'),(1,'#a8c098')])
b+='<path d="M-10 460 L200 140 L320 300 L470 100 L640 320 L810 200 L810 600 L-10 600Z" fill="#6a7a8a"/><path d="M200 140 L240 200 L200 190 L160 200Z M470 100 L520 170 L470 160 L420 170Z" fill="#fff"/>'
b+=hills(520,30,'#6a9a4a',48,4)+'<rect y="580" width="800" height="220" fill="#4a7a3a"/>'
for x,y in [(150,560),(220,540),(290,570)]:
    b+=f'<rect x="{x}" y="{y}" width="56" height="44" fill="#e8dcc8"/><path d="M{x-6} {y} L{x+28} {y-30} L{x+62} {y}Z" fill="#8a3a2a"/>'
b+='<path d="M380 800 Q420 700 520 640 Q620 600 800 590" stroke="#d8c8a0" stroke-width="30" fill="none"/>'
b+=figure(620,640,110,'#2a2a2a')+figure(660,632,100,'#2a2a2a')
b+=figure(200,720,170,'#2a2a2a')+'<path d="M226 640 L240 720" stroke="#2a2a2a" stroke-width="6"/>'
b+='<rect x="320" y="620" width="20" height="40" fill="#4a3a2a"/>'+''.join(f'<ellipse cx="{x}" cy="680" rx="20" ry="12" fill="#f6f0e6"/>' for x in (100,60))
I[48]=svg(b,d)

# 49 Sois pas timide: a shy man hides behind a bouquet of flowers in front of a glamorous woman who winks at him
d,b=bg([(0,'#ffe0b0'),(.6,'#ffb08a'),(1,'#e86a6a')])
b+=glow(560,360,200,'#fff',.4)
b+=figure(560,760,420,'#3a1424',hair='#3a1424')
b+=figure(240,780,400,'#1a0a14')
for k,(x,y,c) in enumerate([(240,300,'#ff4a6a'),(200,330,'#ffd23f'),(280,330,'#ff8ad0'),(220,280,'#ffffff'),(270,270,'#ff4a6a'),(240,350,'#ffd23f')]):
    b+=''.join(f'<circle cx="{x+math.cos(a)*14:.0f}" cy="{y+math.sin(a)*14:.0f}" r="12" fill="{c}"/>' for a in [i*math.pi/2.5 for i in range(5)])+f'<circle cx="{x}" cy="{y}" r="8" fill="#8a3a1a"/>'
b+='<path d="M220 360 L240 460 L260 360Z" fill="#3a8a3a"/>'
b+='<path d="M570 252 q8 -6 16 0" stroke="#fff" stroke-width="4" fill="none"/>'+heart(640,200,20,'#ff3a6a')+heart(680,240,14,'#ff3a6a')
I[49]=svg(b,d)

# 50 Ella, elle l'a: a jazz singer's silhouette glowing in a spotlight, her big voice painted as golden waves
d,b=bg([(0,'#1a0a2a'),(.6,'#3a1a4a'),(1,'#6a2a3a')])
b+='<polygon points="340,0 460,0 620,800 180,800" fill="#ffe6a0" opacity=".18"/>'
b+=micro(400,520,1.2)
b+=figure(400,800,440,'#0a0408',pose='up',hair='#0a0408')
for k in range(5): b+=f'<path d="M{430+k*40} {300-k*10} Q{500+k*50} {260} {470+k*60} {160-k*20}" stroke="#ffd23f" stroke-width="{8-k}" fill="none" opacity="{.9-k*.15}" stroke-linecap="round"/>'
b+=note(600,180,26,'#ffd23f',True)+note(680,280,20,'#ffd23f')
I[50]=svg(b,d)

# 51 Pour un flirt: two 1970s teenagers on a scooter on a coastal road, her hair and scarf flying in the summer wind
d,b=bg([(0,'#7ad0f0'),(.6,'#c8f0f0'),(1,'#f0d890')])
b+=sun(640,140,50,'#fff4a0')
b+='<rect y="420" width="800" height="120" fill="#2a8ac8"/>'+waves(440,'#5aaae0',5,10,.7)
b+='<path d="M0 540 L800 540 L800 800 L0 800Z" fill="#c8b890"/><rect y="600" width="800" height="90" fill="#6a6a70"/><path d="M0 645 L800 645" stroke="#fff" stroke-width="5" stroke-dasharray="40 30"/>'
b+='<g transform="translate(400 620)"><circle cx="-90" cy="0" r="34" fill="#1a1a1e"/><circle cx="100" cy="0" r="34" fill="#1a1a1e"/><path d="M-130 -20 Q-110 -70 -40 -70 L40 -70 L60 -20 L130 -20 Q140 -60 110 -110 L90 -110 L100 -70 L70 -70 L50 -20Z" fill="#f05a3a"/><path d="M110 -110 L120 -160 L150 -160" stroke="#1a1a1e" stroke-width="8" fill="none"/></g>'
b+=figure(470,560,160,'#2a1a1a',pose='reach')+figure(390,560,150,'#2a1a1a',pose='hold',hair='#2a1a1a')
b+='<path d="M380 410 Q300 390 220 420 Q280 430 300 450 Q340 430 380 430Z" fill="#ff8ad0"/>'
I[51]=svg(b,d)

# 52 Il jouait du piano debout: a man plays a grand piano standing up, leaning in, notes flying out wildly
d,b=bg([(0,'#0a1a3a'),(.6,'#1a3a6a'),(1,'#2a5a8a')])
b+=stage_lights(3,10,['#ffd23f','#ff6ab0','#6ad0ff'],.12)
b+='<rect y="660" width="800" height="140" fill="#0a1020"/>'
b+='<path d="M180 520 L620 520 Q700 520 700 460 Q620 380 480 400 L180 430Z" fill="#050508"/><path d="M180 430 L180 380 Q400 280 520 400" stroke="#050508" stroke-width="10" fill="none"/>'
b+=keys(190,520,320,24,28)
b+='<path d="M220 548 L220 680 M600 548 L600 680 M440 548 L440 680" stroke="#050508" stroke-width="14"/>'
b+=figure(340,690,330,'#000',pose='reach')
for k,(x,y) in enumerate([(460,320),(520,250),(590,200),(660,140),(720,260),(560,140)]): b+=note(x,y,24,'#fff',k%2==1)
I[52]=svg(b,d)

# 53 Dernière danse (Kyo): a broken-hearted young man alone on an empty rainy dance floor, one spotlight left on
d,b=bg([(0,'#050a14'),(1,'#141c2a')])
b+='<polygon points="360,0 440,0 560,720 240,720" fill="#bfd8ff" opacity=".14"/>'
b+=rain(90,53,'#bfd8ff',.35)
b+='<ellipse cx="400" cy="720" rx="200" ry="40" fill="#bfd8ff" opacity=".2"/><rect y="720" width="800" height="80" fill="#0a0e18"/>'
b+=figure(400,720,330,'#000')
b+='<path d="M380 360 L380 320" stroke="#000" stroke-width="0"/>'+'<path d="M150 720 L650 720" stroke="#bfd8ff" stroke-width="2" opacity=".3"/>'
I[53]=svg(b,d)

# 54 Hélène: a young man writes her name with his finger on a frosty window, snowy Quebec forest outside
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+='<rect x="120" y="120" width="560" height="460" fill="#a8c8e8"/>'
b+=''.join(f'<path d="M{150+k*60} 560 L{180+k*60} 420 L{210+k*60} 560Z" fill="#2a4a5a"/><path d="M{165+k*60} 490 L{180+k*60} 440 L{195+k*60} 490Z" fill="#fff" opacity=".8"/>' for k in range(9))
b+='<rect x="120" y="120" width="560" height="460" fill="#fff" opacity=".45"/>'+snow(30,54,op=.6)
b+=f'<text x="400" y="340" text-anchor="middle" {F} font-size="90" fill="#2a4a6a" opacity=".7" font-style="italic">Hélène</text>'
b+='<rect x="120" y="120" width="560" height="460" fill="none" stroke="#4a2a1a" stroke-width="22"/><path d="M400 120 L400 580" stroke="#4a2a1a" stroke-width="14"/>'
b+='<rect x="100" y="580" width="600" height="30" fill="#5a3a2a"/>'+figure(540,800,260,'#0a0a14',pose='reach')
I[54]=svg(b,d)

# 55 Lambada: a couple dances lambada hip to hip on a tropical beach, her flowery skirt flying out
d,b=bg([(0,'#ff6a3a'),(.5,'#ffb04a'),(1,'#2ab0b0')])
b+=sun(400,330,70,'#fff4a0')+'<rect y="400" width="800" height="140" fill="#2a9ab0"/>'
b+=palm(90,620,420,'#1a2a10',14)+palm(720,620,380,'#1a2a10',-14)
b+='<rect y="540" width="800" height="260" fill="#f0d090"/>'
b+=figure(370,720,330,'#2a0a0a',pose='hold')+figure(440,720,300,'#2a0a0a',pose='up',hair='#2a0a0a')
b+='<path d="M410 560 Q340 610 300 650 Q380 630 440 660 Q500 630 560 640 Q520 600 470 560Z" fill="#ff3a6a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#ffd23f"/>' for x,y in [(340,630),(400,640),(470,640),(520,620)])
I[55]=svg(b,d)

# 56 Là-bas: a young man on a wooden pier looks toward a ship on the horizon, a woman holds his hand back on the shore
d,b=bg([(0,'#3a4a6a'),(.5,'#8a7a8a'),(1,'#f0b080')])
b+=glow(560,420,140,'#ffd8a0',.5)
b+='<rect y="430" width="800" height="370" fill="#3a5a7a"/>'+waves(450,'#5a7a9a',4,12,.6)
b+=boat(600,425,.5,'#f6efe2','#fff','#1a2a3a')
b+='<path d="M0 560 L420 560 L420 580 L0 580Z" fill="#4a2a1a"/>'+''.join(f'<rect x="{20+k*80}" y="580" width="12" height="160" fill="#3a1a10"/>' for k in range(6))
b+=figure(380,564,200,'#0a0a14',pose='reachL')+figure(150,564,180,'#0a0a14',pose='reach',hair='#0a0a14')
I[56]=svg(b,d)

# 57 Amsterdam: sailors drinking and singing in a smoky port tavern, a ship's lantern and the harbour behind
d,b=bg([(0,'#0e1a2a'),(.6,'#2a3a4a'),(1,'#4a3a2a')])
b+='<rect x="440" y="80" width="300" height="260" fill="#1a3a5a"/><rect x="440" y="80" width="300" height="260" fill="none" stroke="#2a1a10" stroke-width="16"/>'
b+='<path d="M540 300 L540 150 M520 300 L640 300 L620 320 L540 320Z" stroke="#0a1420" stroke-width="6" fill="#0a1420"/><path d="M545 160 L620 260 L545 260Z" fill="#c8d0d8" opacity=".6"/>'
b+='<rect y="560" width="800" height="240" fill="#2a1a10"/><rect y="540" width="800" height="30" fill="#5a3a1a"/>'
b+='<path d="M160 0 L160 90" stroke="#1a1a1a" stroke-width="4"/><rect x="130" y="90" width="60" height="80" rx="8" fill="#ffb84a"/>'+glow(160,130,140,'#ffb84a',.4)
for x,p in [(120,'up'),(260,'wave'),(400,'up'),(560,'hold'),(680,'wave')]: b+=figure(x,560,240,'#0a0604',pose=p)
for x in (148,428): b+=f'<rect x="{x}" y="300" width="22" height="34" fill="#ffd27a" opacity=".85"/><rect x="{x}" y="296" width="22" height="8" fill="#fff"/>'
I[57]=svg(b,d)

# 58 Foule sentimentale: a crowd holds up a giant heart above a sea of shopping bags and price tags, longing for more than things
d,b=bg([(0,'#8ac8f0'),(.6,'#c8e0f0'),(1,'#f0c8a0')])
b+=heart(400,220,110,'#ff4a6a')+glow(400,220,160,'#fff',.4)
for k in range(18): b+=figure(30+k*44,800,170+(k*37%50),['#2a3a5a','#3a2a4a','#2a4a4a'][k%3],pose='up' if k%3 else 'stand')
r=R(58)
for k in range(9):
    x,y=r.uniform(40,740),r.uniform(560,700);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="40" height="46" fill="#f6efe2"/><path d="M{x+10:.0f} {y:.0f} Q{x+20:.0f} {y-18:.0f} {x+30:.0f} {y:.0f}" stroke="#f6efe2" stroke-width="4" fill="none"/>'
I[58]=svg(b,d)

# 59 L'Envie d'aimer: a big rising sun in the shape of a heart over hands reaching upward from a musical stage
d,b=bg([(0,'#2a1a4a'),(.5,'#c84a7a'),(1,'#ffb06a')])
b+=rays(400,420,24,'#fff4c0',.12,6)
b+=heart(400,380,140,'#ffd23f')+glow(400,380,220,'#ffe0a0',.5)
b+='<rect y="620" width="800" height="180" fill="#1a0a20"/>'
for k in range(11): x=40+k*72;b+=f'<path d="M{x} 800 L{x+6} 650 L{x-6} 620 M{x+6} 650 L{x+18} 620" stroke="#1a0a20" stroke-width="14" stroke-linecap="round"/>'
I[59]=svg(b,d)

# 60 Tous les garçons et les filles: a lonely girl walks alone past couples holding hands in a 1960s park
d,b=bg([(0,'#c8d8e8'),(.6,'#e8e0d8'),(1,'#b8c0a0')])
b+=tree(110,560,300,'#4a6a4a',60)+tree(690,560,280,'#4a6a4a',61)
b+='<rect y="560" width="800" height="240" fill="#8aa07a"/><path d="M300 800 Q380 650 400 560 L440 560 Q470 650 560 800Z" fill="#d8ccb0"/>'
for x in (200,600): b+=figure(x-18,600,200,'#4a4a5a',pose='hold',hair='#4a4a5a')+figure(x+18,600,220,'#4a4a5a',pose='hold')
b+=heart(200,360,16,'#ff8aa8')+heart(600,360,16,'#ff8aa8')
b+=figure(430,780,320,'#1a1a24',hair='#1a1a24')
I[60]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
