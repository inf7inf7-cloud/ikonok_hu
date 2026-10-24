import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 5. csoport, 2026-10-24
I={}
def ring(x,y,s,gem='#e8102a'):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="0" cy="40" rx="90" ry="40" fill="none" stroke="#e8c050" stroke-width="18"/>'
            f'<path d="M-40 -10 L0 -60 L40 -10 L0 20Z" fill="{gem}"/><path d="M-40 -10 L0 -60 L0 20Z" fill="#fff" opacity=".25"/><path d="M-26 0 L-14 24 L14 24 L26 0" fill="#e8c050"/></g>')

# 1469 春雷: a lightning bolt splitting a violet spring sky above a cherry tree in full blossom
d,b=bg([(0,'#1a0a3a'),(.6,'#5a2a7a'),(1,'#a85a9a')])
b+=bolt([(520,0),(470,140),(530,180),(440,360)],'#fff6ff',12,.95)+glow(470,180,120,'#e8c8ff',.45)
b+='<path d="M300 800 Q310 640 280 520 M290 600 Q220 560 200 500 M300 560 Q380 520 420 470" stroke="#2a1420" stroke-width="22" fill="none"/>'
r=R(1469)
for _ in range(40): b+=f'<circle cx="{280+r.uniform(-200,200):.0f}" cy="{470+r.uniform(-120,80):.0f}" r="{r.uniform(26,50):.0f}" fill="{r.choice(["#ffc0dc","#ffa8cc","#ffd8e8"])}"/>'
b+=petals(30,1469,'#ffd0e4',100,800,8,14,.9)
I[1469]=svg(b,d)

# 1562 死ぬのがいいわ: a grand piano alone on a stage before a heavy red curtain, a single red rose on its lid
d,b=bg([(0,'#3a0408'),(1,'#1a0204')])
for k in range(10): b+=f'<path d="M{k*84} 0 Q{k*84+42} 300 {k*84} 640" stroke="#5a0a14" stroke-width="30" fill="none" opacity=".6"/>'
b+='<polygon points="400,-20 160,700 640,700" fill="#ffe8c8" opacity=".1"/><rect y="640" width="800" height="160" fill="#140204"/>'
b+='<path d="M180 520 Q180 380 360 380 Q500 380 520 300 Q560 240 620 300 L640 520Z" fill="#0a0a0e"/><rect x="180" y="510" width="460" height="40" fill="#141418"/>'
for x in range(200,620,26): b+=f'<rect x="{x}" y="550" width="22" height="30" fill="#f4f4f0"/>'
b+='<path d="M220 580 L220 700 M600 580 L600 700" stroke="#0a0a0e" stroke-width="14"/>'+rose(420,370,.8,30)
I[1562]=svg(b,d)

# 1569 インフェルノ: a firefighter's helmet silhouetted against a roaring wall of flame, embers swirling
d,b=bg([(0,'#1a0200'),(1,'#5a0a00')])
r=R(1569)
for k in range(12):
    x=k*72;h=r.uniform(300,600)
    b+=f'<path d="M{x-70} 800 Q{x-40} {800-h*.5:.0f} {x} {800-h:.0f} Q{x+40} {800-h*.5:.0f} {x+70} 800Z" fill="{r.choice(["#ff6a1a","#ffaa2a","#e8301a","#ffd04a"])}" opacity=".85"/>'
b+='<g transform="translate(400 470)"><path d="M-180 60 Q-170 -140 0 -150 Q170 -140 180 60Z" fill="#141414"/><path d="M-230 60 L230 60 Q240 100 200 110 L-200 110 Q-240 100 -230 60Z" fill="#141414"/><path d="M-30 -150 L30 -150 L20 40 L-20 40Z" fill="#2a2a2a"/><rect x="-60" y="-60" width="120" height="80" rx="10" fill="#d8b040"/></g>'
for _ in range(30): b+=f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(0,400):.0f}" r="{r.choice([2,3,4])}" fill="#ffd27a"/>'
I[1569]=svg(b,d)

# 1197 GUTS!: a fist punching up into a sunrise, a sweatband on the wrist and speed lines bursting outward
d,b=bg([(0,'#ff8a1a'),(1,'#ffe05a')])
b+=rays(400,400,28,'#ffffff',.3,5)
b+='<path d="M330 800 L350 470 L460 470 L480 800Z" fill="#e8a878"/><rect x="340" y="470" width="130" height="60" fill="#e8302a"/><path d="M340 490 L470 490 M340 510 L470 510" stroke="#fff" stroke-width="5"/>'
b+='<rect x="320" y="270" width="170" height="210" rx="50" fill="#e8b890"/>'+''.join(f'<path d="M{344+k*40} 290 L{344+k*40} 360" stroke="#c89070" stroke-width="6"/>' for k in range(4))+'<path d="M320 380 Q290 340 330 320" stroke="#c89070" stroke-width="6" fill="none"/>'
I[1197]=svg(b,d)

# 1596 カリスマックス: a glittering crown blazing with nine coloured gems, spotlights and sparkles everywhere
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=rays(400,420,24,'#ffe05a',.12,5)+glow(400,420,220,'#ffd84a',.45)
d+=lg('cr',S((0,'#fff2a0'),(1,'#d89a1a')))
b+='<path d="M180 560 L160 300 L270 420 L330 250 L400 400 L470 250 L530 420 L640 300 L620 560Z" fill="url(#cr)"/><rect x="180" y="540" width="440" height="60" rx="10" fill="#c8901a"/>'
for k,c in enumerate(['#ff3a5a','#3a8aff','#3ac84a','#ffffff','#a84aff','#ff8a1a','#5ae8ff','#ff4ab8','#ffe05a']): b+=f'<circle cx="{200+k*50}" cy="570" r="14" fill="{c}"/>'
for x,y in [(160,300),(330,250),(470,250),(640,300)]: b+=f'<circle cx="{x}" cy="{y}" r="18" fill="#fff"/>'
for x,y,s in [(130,150,30),(680,170,34),(400,140,22),(120,660,24),(690,650,26)]: b+=sparkle(x,y,s,'#fff6c8')
I[1596]=svg(b,d)

# 1103 ただ・・・逢いたくて: a lone figure under a streetlamp in the rain, a phone screen glowing in his hand
d,b=bg([(0,'#0a1020'),(1,'#1a2a3a')])
b+=rain(110,1103,'#a8c0e0',.45,6)
b+='<rect x="520" y="150" width="12" height="600" fill="#05080e"/><path d="M500 150 L560 150 L548 126 L512 126Z" fill="#05080e"/>'+glow(526,170,120,'#ffd88a',.45)+'<polygon points="526,160 380,760 680,760" fill="#ffd88a" opacity=".12"/>'
b+='<rect y="720" width="800" height="80" fill="#0a0e18"/><ellipse cx="420" cy="740" rx="150" ry="14" fill="#ffd88a" opacity=".15"/>'
b+=figure(420,740,320,'#02040a')+'<rect x="440" y="510" width="24" height="40" rx="4" fill="#bfe8ff"/>'+glow(452,530,40,'#bfe8ff',.6,'glow2')
I[1103]=svg(b,d)

# 439 ワインレッドの心: a glass of deep red wine with a heart shimmering on its surface, in a dim bar
d,b=bg([(0,'#1a0610'),(1,'#3a0a1a')])
b+=glow(400,420,220,'#a8102a',.45)
b+='<path d="M260 200 L540 200 Q560 420 400 470 Q240 420 260 200Z" fill="#f4e8f0" opacity=".25"/><path d="M265 280 L535 280 Q540 420 400 466 Q260 420 265 280Z" fill="#7a0418"/>'
b+='<ellipse cx="400" cy="280" rx="135" ry="18" fill="#a8102a"/>'+heart(400,282,26,'#ff4a6a')
b+='<rect x="392" y="466" width="16" height="200" fill="#f4e8f0" opacity=".5"/><ellipse cx="400" cy="672" rx="100" ry="18" fill="#f4e8f0" opacity=".5"/>'
b+='<path d="M300 220 Q290 300 310 380" stroke="#fff" stroke-width="10" fill="none" opacity=".35"/>'
I[439]=svg(b,d)

# 509 DIAMONDS: a huge cut diamond flashing rainbow sparkles against a hot-pink 80s backdrop
d,b=bg([(0,'#ff3a9a'),(1,'#8a1a8a')])
b+=rays(400,400,20,'#ffffff',.2,6)
b+='<path d="M220 300 L300 200 L500 200 L580 300 L400 600Z" fill="#e8f8ff"/><path d="M220 300 L580 300" stroke="#a8d8ff" stroke-width="6"/>'
b+='<path d="M300 200 L350 300 L400 200 L450 300 L500 200" stroke="#a8d8ff" stroke-width="6" fill="none"/><path d="M350 300 L400 600 L450 300" stroke="#a8d8ff" stroke-width="6" fill="none"/>'
b+='<path d="M220 300 L350 300 L400 600Z" fill="#bfe8ff"/><path d="M450 300 L580 300 L400 600Z" fill="#d8f0ff"/>'
for x,y,s,c in [(260,180,30,'#fff'),(560,170,24,'#ffe05a'),(620,380,30,'#5ae8ff'),(170,420,22,'#fff')]: b+=sparkle(x,y,s,c)
I[509]=svg(b,d)

# 631 OCEAN: a lifebuoy floating in the deep blue sea, sunlight streaming down through the water around it
d,b=bg([(0,'#0a5ab8'),(1,'#021a4a')])
b+=rays(400,-80,12,'#bfe8ff',.12,7,60,120)
b+='<rect y="0" width="800" height="180" fill="#3a9ae8"/><path d="M0 180 Q100 160 200 180 T400 180 T600 180 T800 180" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/>'
b+='<g transform="translate(400 180)"><circle r="130" fill="#ff5a2a"/><circle r="64" fill="#3a9ae8"/>'+''.join(f'<path d="M{64*math.cos(math.radians(a)):.0f} {64*math.sin(math.radians(a)):.0f} L{130*math.cos(math.radians(a)):.0f} {130*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="40"/>' for a in (45,135,225,315))+'</g>'
b+='<rect y="180" width="800" height="620" fill="#0a5ab8" opacity=".55"/>'
r=R(631)
for _ in range(14): x,y,s=r.uniform(60,740),r.uniform(340,760),r.uniform(6,18);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="none" stroke="#bfe8ff" stroke-width="3" opacity=".7"/>'
I[631]=svg(b,d)

# 1104 道: a school path lined with cherry trees, a graduation tube lying on the road as petals fall
d,b=bg([(0,'#bfe0ff'),(1,'#ffe8f0')])
b+='<path d="M-10 520 Q400 490 810 520 L810 810 L-10 810Z" fill="#a8d88a"/><path d="M200 810 L380 500 L420 500 L600 810Z" fill="#e8d8b8"/>'
for x,y,s in [(100,400,1.1),(260,430,.7),(700,400,1.1),(540,430,.7)]:
    b+=f'<rect x="{x-8*s}" y="{y}" width="{16*s}" height="{140*s}" fill="#4a2a1a"/>'
    r=R(int(x))
    for _ in range(18): b+=f'<circle cx="{x+r.uniform(-100,100)*s:.0f}" cy="{y+r.uniform(-120,20)*s:.0f}" r="{r.uniform(30,50)*s:.0f}" fill="{r.choice(["#ffc0d4","#ffd8e4"])}"/>'
b+='<g transform="rotate(-18 400 680)"><rect x="300" y="660" width="200" height="40" rx="18" fill="#1a1a2a"/><rect x="460" y="660" width="40" height="40" rx="8" fill="#c8a040"/></g>'+petals(40,1104,'#ff9ab8',0,800,7,12,.9)
I[1104]=svg(b,d)

# 1740 劇薬中毒: a glowing pink potion bottle with a heart-skull label, sweet poison dripping from its neck
d,b=bg([(0,'#1a0420'),(1,'#3a0a40')])
b+=glow(400,450,220,'#ff4ad8',.45)
b+='<path d="M360 200 L440 200 L440 300 Q560 360 560 500 Q560 660 400 670 Q240 660 240 500 Q240 360 360 300Z" fill="#ff7ae8" opacity=".85"/><rect x="350" y="160" width="100" height="50" rx="10" fill="#8a2a6a"/>'
b+='<rect x="300" y="460" width="200" height="130" rx="16" fill="#fff4fb"/>'+heart(400,512,34,'#2a0a2a')+'<circle cx="388" cy="508" r="6" fill="#fff"/><circle cx="412" cy="508" r="6" fill="#fff"/>'
b+='<path d="M440 220 Q480 240 470 300 Q466 330 480 340" stroke="#ff4ad8" stroke-width="10" fill="none"/><ellipse cx="482" cy="352" rx="9" ry="13" fill="#ff4ad8"/>'
b+='<ellipse cx="300" cy="380" rx="16" ry="40" fill="#fff" opacity=".4" transform="rotate(20 300 380)"/>'
I[1740]=svg(b,d)

# 235 旅人のうた: a traveller with a staff walking a lonely ridge under a huge moon, the road vanishing ahead
d,b=bg([(0,'#0a1430'),(.7,'#2a3a6a'),(1,'#5a5a8a')])
b+=starsf(60,235,500,'#e8f0ff')+moon(560,250,110,'#f4ecc8')
b+='<path d="M-10 640 Q200 560 400 600 Q600 640 810 560 L810 810 L-10 810Z" fill="#0a0e20"/>'
b+=figure(330,600,220,'#0a0e20')+'<path d="M368 400 L380 600" stroke="#0a0e20" stroke-width="8"/><rect x="290" y="440" width="40" height="70" rx="10" fill="#0a0e20"/>'
I[235]=svg(b,d)

# 775 家族になろうよ: a little white chapel on a green hill, three figures and a dog walking toward it in the sun
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+=cloud(160,150,1.0)+'<path d="M-10 560 Q400 480 810 560 L810 810 L-10 810Z" fill="#7ac85a"/>'
b+='<rect x="460" y="360" width="160" height="180" fill="#fff"/><path d="M440 370 L540 290 L640 370Z" fill="#c84a3a"/><rect x="530" y="210" width="20" height="90" fill="#fff"/><rect x="516" y="236" width="48" height="12" fill="#fff"/><path d="M520 460 Q540 430 560 460 L560 540 L520 540Z" fill="#8a5a3a"/>'
b+=figure(230,690,190,'#2a2a4a')+figure(290,690,170,'#5a2a4a',hair='#5a2a4a',pose='hold')+figure(340,690,100,'#2a4a6a')
b+='<g fill="#5a3a1a"><ellipse cx="160" cy="676" rx="28" ry="14"/><circle cx="138" cy="664" r="12"/><rect x="146" y="680" width="6" height="12"/><rect x="172" y="680" width="6" height="12"/></g>'
I[775]=svg(b,d)

# 979 For You: a gift box wrapped in white paper and a big red ribbon, snowflakes catching the light around it
d,b=bg([(0,'#2a3a6a'),(1,'#5a6a9a')])
b+=snow(70,979)+glow(400,450,200,'#ffe8f0',.35)
b+='<rect x="230" y="380" width="340" height="280" rx="12" fill="#fbfbf6"/><rect x="210" y="330" width="380" height="70" rx="12" fill="#ffffff"/>'
b+='<rect x="380" y="330" width="40" height="330" fill="#e8102a"/><rect x="210" y="350" width="380" height="30" fill="#e8102a" opacity="0"/>'
b+='<path d="M400 330 Q320 220 280 280 Q300 340 400 330Z M400 330 Q480 220 520 280 Q500 340 400 330Z" fill="#e8102a"/><circle cx="400" cy="326" r="20" fill="#b80a20"/>'
I[979]=svg(b,d)

# 989 BLUE BIRD: a bright blue bird soaring across a wide orange sky toward the setting sun
d,b=bg([(0,'#ff8a3a'),(.6,'#ffc06a'),(1,'#ffe8b0')])
b+=hinomaru_sun(560,520,120,'#fff2c8',.9)+'<rect y="600" width="800" height="200" fill="#e86a3a" opacity=".5"/>'
b+='<g transform="translate(330 330) rotate(-14)"><path d="M-140 0 Q-60 -40 40 -20 Q100 -10 140 -30 Q110 10 60 20 Q-40 40 -140 0Z" fill="#1a6ae8"/><path d="M-60 -10 Q-40 -140 60 -170 Q30 -90 20 -20Z" fill="#2a8aff"/><path d="M-40 10 Q10 110 100 120 Q60 60 30 10Z" fill="#0a4ac8"/><circle cx="110" cy="-24" r="8" fill="#fff"/><path d="M140 -30 L170 -24 L140 -14Z" fill="#ffb02a"/></g>'
I[989]=svg(b,d)

# 1198 Troublemaker: a cartoon bomb with its fuse fizzing, toys and confetti flying in a burst of mischief
d,b=bg([(0,'#ffe05a'),(1,'#ff9a1a')])
b+=rays(400,420,20,'#ffffff',.3,7)+confetti(40,1198,['#e8302a','#2a8aff','#3ac84a','#ffffff'])
b+='<circle cx="380" cy="470" r="170" fill="#1a1a24"/><ellipse cx="320" cy="400" rx="40" ry="26" fill="#fff" opacity=".3" transform="rotate(-30 320 400)"/><rect x="410" y="280" width="80" height="60" rx="10" fill="#3a3a44" transform="rotate(30 450 310)"/>'
b+='<path d="M470 280 Q520 220 500 170 Q480 130 520 110" stroke="#c8a878" stroke-width="10" fill="none"/>'+sparkle(530,100,46,'#fff')+sparkle(530,100,26,'#ff5a1a')
I[1198]=svg(b,d)

# 351 ルビーの指環: a ruby ring glinting on a café table through a curl of cigarette smoke
d,b=bg([(0,'#1a1414'),(1,'#3a2a24')])
b+=glow(400,450,200,'#ff4a5a',.3)
for k in range(3): b+=f'<path d="M{560+k*10} 600 Q{620+k*20} 480 560 380 Q{500-k*20} 280 {580+k*10} 160" stroke="#d8d0d8" stroke-width="{8-k*2}" fill="none" opacity="{.4-k*.1:.2f}"/>'
b+='<rect y="600" width="800" height="200" fill="#5a3a2a"/>'+ring(360,470,1.6)+glow(360,400,50,'#ff4a5a',.6,'glow2')
I[351]=svg(b,d)

# 381 サザン・ウインド: palm trees bending in a warm southern wind over a pastel tropical beach at sunset
d,b=bg([(0,'#ff8ab8'),(.6,'#ffc89a'),(1,'#5ac8d8')])
b+=hinomaru_sun(560,440,90,'#fff2c8',.9)+'<rect y="470" width="800" height="330" fill="#3ab0c8"/><path d="M-10 640 Q400 600 810 660 L810 810 L-10 810Z" fill="#ffe0b0"/>'
for x,s in [(200,1.1),(330,.8)]:
    b+=f'<path d="M{x} 700 Q{x+40*s} 500 {x+120*s} {380}" stroke="#4a2a1a" stroke-width="{20*s}" fill="none"/>'
    for a in (-60,-20,20,60,100): b+=f'<path d="M{x+120*s} 380 Q{x+120*s+140*s*math.cos(math.radians(a)):.0f} {380+60*s*math.sin(math.radians(a))-40:.0f} {x+120*s+220*s*math.cos(math.radians(a)):.0f} {380+120*s*math.sin(math.radians(a))+40:.0f}" stroke="#1a6a3a" stroke-width="{26*s}" fill="none" stroke-linecap="round"/>'
I[381]=svg(b,d)

# 430 ジュリアに傷心: a cracked red heart set over a bold black-and-white checkerboard, 80s teen-pop style
d,b=bg([(0,'#ffffff'),(1,'#f0f0f0')])
for i in range(10):
    for j in range(10):
        if (i+j)%2: b+=f'<rect x="{i*80}" y="{j*80}" width="80" height="80" fill="#141414"/>'
b+=glow(400,420,200,'#ff2a4a',.4)+heart(400,420,170,'#e8102a')
b+=bolt([(400,300),(370,380),(430,440),(390,520),(410,580)],'#fff',10,1)
I[430]=svg(b,d)

# 1425 ミュージック: a vinyl record spinning in deep blue light, sound waves rippling out from its grooves
d,b=bg([(0,'#04102a'),(1,'#0a2a5a')])
for k in range(6): b+=f'<circle cx="400" cy="400" r="{230+k*40}" fill="none" stroke="#5ab0ff" stroke-width="4" opacity="{.5-k*.07:.2f}"/>'
b+='<circle cx="400" cy="400" r="220" fill="#08080e"/>'+''.join(f'<circle cx="400" cy="400" r="{100+k*20}" fill="none" stroke="#1a1a24" stroke-width="3"/>' for k in range(6))
b+='<circle cx="400" cy="400" r="80" fill="#2a8aff"/><circle cx="400" cy="400" r="10" fill="#08080e"/><path d="M260 260 Q320 220 380 220" stroke="#fff" stroke-width="8" fill="none" opacity=".3"/>'
I[1425]=svg(b,d)

# 281 愛の言霊 ~Spiritual Message~: pale blue spirit flames drifting over a dark summer sea under a full moon
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
b+=moon(400,180,60,'#e8f0ff')+'<rect y="460" width="800" height="340" fill="#06102a"/>'
for x,y,s in [(200,380,1),(400,320,1.3),(600,390,1),(300,500,.7),(520,520,.8)]:
    b+=glow(x,y,60*s,'#7ad8ff',.55)+f'<path d="M{x} {y-60*s} Q{x+40*s} {y-10*s} {x+26*s} {y+20*s} Q{x} {y+40*s} {x-26*s} {y+20*s} Q{x-40*s} {y-10*s} {x} {y-60*s}Z" fill="#bff0ff"/>'
b+=''.join(f'<rect x="{360-k*14}" y="{480+k*26}" width="{80+k*28}" height="3" fill="#e8f0ff" opacity="{.5-k*.06:.2f}"/>' for k in range(7))
I[281]=svg(b,d)

# 694 Don't you see!: a pair of binoculars on a sunny sea railing, looking out toward a far bright horizon
d,b=bg([(0,'#3aa8f0'),(1,'#c8ecff')])
b+=cloud(600,140,1.0)+'<rect y="430" width="800" height="200" fill="#1a8ad8"/><rect y="630" width="800" height="170" fill="#e8e0d0"/>'
b+='<path d="M0 600 L800 600" stroke="#fff" stroke-width="14"/>'+''.join(f'<rect x="{x}" y="600" width="10" height="100" fill="#fff"/>' for x in range(40,800,90))
b+='<g transform="rotate(-6 400 520)"><rect x="270" y="440" width="110" height="160" rx="40" fill="#1a1a24"/><rect x="420" y="440" width="110" height="160" rx="40" fill="#1a1a24"/><rect x="370" y="480" width="60" height="50" fill="#2a2a34"/><circle cx="325" cy="450" r="44" fill="#5ab0ff"/><circle cx="475" cy="450" r="44" fill="#5ab0ff"/><circle cx="312" cy="438" r="12" fill="#fff" opacity=".6"/><circle cx="462" cy="438" r="12" fill="#fff" opacity=".6"/></g>'
I[694]=svg(b,d)

# 931 フラワー: a single bright orange flower pushing up through a crack in grey city asphalt
d,b=bg([(0,'#8a8a94'),(1,'#5a5a64')])
b+=glow(400,340,200,'#ffe8b0',.45)
b+='<rect y="560" width="800" height="240" fill="#4a4a54"/>'+bolt([(100,800),(240,680),(360,620),(400,560)],'#2a2a30',10,1)
b+='<path d="M400 600 Q390 480 400 380" stroke="#4a8a3a" stroke-width="12" fill="none"/><path d="M396 500 Q330 460 320 410 Q370 430 400 480Z" fill="#5aa04a"/>'
b+=flower(400,330,140,8,'#ff8a1a','#ffd82a',0,.6)
I[931]=svg(b,d)

# 1520 群青: an easel holding a canvas painted deep ultramarine, brushes and a palette of blues beside it
d,b=bg([(0,'#e8eef8'),(1,'#c8d4e8')])
b+='<path d="M260 760 L340 200 M540 760 L460 200 M400 200 L400 760" stroke="#8a6a4a" stroke-width="16"/>'
d+=lg('gj',S((0,'#0a2a8a'),(.5,'#1a4ac8'),(1,'#0a1a5a')),0,0,1,1)
b+='<rect x="200" y="160" width="400" height="400" fill="url(#gj)"/><path d="M220 420 Q320 360 420 420 T600 400" stroke="#4a8aff" stroke-width="20" fill="none" opacity=".7"/>'
b+='<rect x="190" y="560" width="420" height="20" fill="#7a5a3a"/>'
b+='<ellipse cx="620" cy="680" rx="130" ry="70" fill="#f4e8d0"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}"/>' for x,y,c in [(560,660,'#0a2a8a'),(610,640,'#1a4ac8'),(660,660,'#4a8aff'),(700,690,'#8ac0ff')])
I[1520]=svg(b,d)

# 932 愛されるより 愛したい: two hands passing a red heart-shaped balloon from one to the other under a pink sky
d,b=bg([(0,'#ffb0d0'),(1,'#ffe0ec')])
b+=heart(400,260,120,'#e8203a')+'<path d="M400 360 Q380 460 400 540" stroke="#7a3a4a" stroke-width="3" fill="none"/><ellipse cx="350" cy="220" rx="26" ry="16" fill="#fff" opacity=".5" transform="rotate(-30 350 220)"/>'
b+='<path d="M120 700 Q200 580 330 560 L400 540 L410 590 Q300 640 220 760Z" fill="#e8b890"/><path d="M680 700 Q600 580 470 560 L400 540 L390 590 Q500 640 580 760Z" fill="#d8a880"/>'
I[932]=svg(b,d)

# 1105 Ti Amo: a single red rose and a lit candle in an old Italian church, a stained-glass window glowing behind
d,b=bg([(0,'#1a0a14'),(1,'#2a1420')])
b+='<path d="M260 500 L260 260 Q260 140 400 120 Q540 140 540 260 L540 500Z" fill="#3a1a4a"/>'
for k,c in enumerate(['#e8302a','#2a6ae8','#ffd82a','#3ac84a','#a84aff','#ff8a1a']): b+=f'<path d="M400 300 L{400+150*math.cos(math.radians(-180+k*36)):.0f} {300+150*math.sin(math.radians(-180+k*36)):.0f} L{400+150*math.cos(math.radians(-144+k*36)):.0f} {300+150*math.sin(math.radians(-144+k*36)):.0f}Z" fill="{c}" opacity=".75"/>'
b+='<rect y="560" width="800" height="240" fill="#2a1410"/>'+'<rect x="520" y="420" width="40" height="160" rx="6" fill="#fff6e8"/><path d="M540 390 Q554 410 540 424 Q526 410 540 390Z" fill="#ffd060"/>'+glow(540,400,50,'#ffd060',.7,'glow2')
b+='<path d="M200 640 Q300 620 400 580" stroke="#2a5a2a" stroke-width="10" fill="none"/>'+rose(410,575,.9,70)
I[1105]=svg(b,d)

# 1422 僕の名前を: an envelope with a blank name card and a fountain pen, a name about to be written by hand
d,b=bg([(0,'#d8e0e8'),(1,'#a8b8c8')])
b+='<g transform="rotate(-6 400 420)"><rect x="160" y="260" width="480" height="320" rx="10" fill="#f4ece0"/><path d="M160 270 L400 430 L640 270" fill="none" stroke="#d8c8b0" stroke-width="6"/>'
b+='<rect x="250" y="200" width="300" height="180" rx="8" fill="#fff"/><path d="M290 300 L510 300" stroke="#c8c8d0" stroke-width="4" stroke-dasharray="10 8"/><text x="290" y="290" font-family="Noto Sans JP" font-weight="700" font-size="40" fill="#1a2a5a">ぼく</text></g>'
b+='<g transform="rotate(30 560 520)"><rect x="540" y="340" width="34" height="260" rx="12" fill="#1a2a5a"/><path d="M540 600 L557 660 L574 600Z" fill="#d8b050"/></g>'
I[1422]=svg(b,d)

# 990 Boys & Girls: a ferris wheel glowing against a summer sunset, youth running along the promenade below
d,b=bg([(0,'#3a2a7a'),(.6,'#ff7a8a'),(1,'#ffc87a')])
b+='<circle cx="460" cy="380" r="230" fill="none" stroke="#2a1a3a" stroke-width="12"/>'+''.join(f'<path d="M460 380 L{460+230*math.cos(math.radians(a)):.0f} {380+230*math.sin(math.radians(a)):.0f}" stroke="#2a1a3a" stroke-width="5"/><rect x="{460+230*math.cos(math.radians(a))-18:.0f}" y="{380+230*math.sin(math.radians(a))-14:.0f}" width="36" height="34" rx="6" fill="{["#ffd82a","#5ae8ff","#ff5aa8"][int(a/30)%3]}"/>' for a in range(0,360,30))
b+='<path d="M410 800 L460 380 L510 800" stroke="#2a1a3a" stroke-width="14" fill="none"/><rect y="700" width="800" height="100" fill="#2a1a3a"/>'
for x,p in [(120,'up'),(190,'wave'),(260,'up')]: b+=figure(x,700,120,'#140a1a',pose=p)
I[990]=svg(b,d)

# 1521 怪物: a lone wolf howling on a rock under a giant full moon, its shadow stretched long
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=moon(420,300,170,'#f4ecd8',.45)
b+='<path d="M-10 800 L-10 640 L300 580 L560 640 L810 600 L810 800Z" fill="#06060e"/>'
b+='<g fill="#06060e"><path d="M300 600 L320 470 Q340 420 380 410 L430 340 L440 300 L460 340 L470 300 L480 350 Q500 370 490 400 L520 410 Q500 420 470 420 L450 470 L480 600 L460 600 L440 500 L360 520 L340 600Z"/><path d="M320 500 Q260 520 240 580 Q280 560 320 540Z"/></g>'
I[1521]=svg(b,d)

# 632 ALONE: a solitary figure on an empty bridge at night, one streetlamp, the river black below
d,b=bg([(0,'#0a0e1a'),(1,'#1a2030')])
b+=starsf(30,632,300,'#c8d0e8')
b+='<path d="M-10 520 Q400 440 810 520" stroke="#2a3040" stroke-width="30" fill="none"/><path d="M-10 500 Q400 420 810 500" stroke="#3a4050" stroke-width="6" fill="none"/>'
for x in range(20,800,50): b+=f'<rect x="{x}" y="{460+((x-400)/410)**2*80-40:.0f}" width="5" height="44" fill="#3a4050"/>'
b+='<rect y="560" width="800" height="240" fill="#06080e"/>'+''.join(f'<rect x="{560-k*10}" y="{580+k*30}" width="{40+k*20}" height="3" fill="#ffd88a" opacity="{.5-k*.06:.2f}"/>' for k in range(6))
b+='<rect x="570" y="230" width="8" height="250" fill="#06080e"/>'+glow(574,232,60,'#ffd88a',.55)+'<circle cx="574" cy="232" r="12" fill="#fff0b8"/>'
b+=figure(380,500,230,'#020306')
I[632]=svg(b,d)

# 695 マイ フレンド: a basketball resting under an outdoor hoop by the sea, the summer sun going down
d,b=bg([(0,'#ff8a5a'),(.6,'#ffc890'),(1,'#5ab0d8')])
b+=hinomaru_sun(250,470,90,'#fff2c8',.9)+'<rect y="480" width="800" height="120" fill="#3a90c8"/><rect y="600" width="800" height="200" fill="#c86a4a"/>'
b+='<rect x="580" y="200" width="16" height="420" fill="#2a2a34"/><rect x="460" y="160" width="200" height="130" fill="#fff" stroke="#2a2a34" stroke-width="8"/><rect x="520" y="210" width="80" height="60" fill="none" stroke="#e8302a" stroke-width="6"/>'
b+='<ellipse cx="560" cy="300" rx="50" ry="10" fill="none" stroke="#e8502a" stroke-width="8"/>'+''.join(f'<path d="M{520+k*16} 304 L{530+k*10} 360" stroke="#fff" stroke-width="3"/>' for k in range(6))
b+='<circle cx="360" cy="660" r="70" fill="#e8702a"/><path d="M290 660 L430 660 M360 590 L360 730 M310 610 Q360 660 310 710 M410 610 Q360 660 410 710" stroke="#3a1a0a" stroke-width="5" fill="none"/>'
I[695]=svg(b,d)

# 1399 炎と森のカーニバル: a striped circus tent glowing in a dark forest, fire torches and lanterns lighting the carnival
d,b=bg([(0,'#0a1a14'),(1,'#1a2a1a')])
for x in (60,160,640,740): b+=tree(x,700,360,'#06120c',x)
b+=glow(400,480,240,'#ff9a3a',.4)
b+='<path d="M200 640 L400 300 L600 640Z" fill="#e8302a"/>'+''.join(f'<path d="M400 300 L{200+k*80+40} 640 L{200+k*80+80} 640Z" fill="#fff6e8"/>' for k in range(0,5,2))
b+='<path d="M400 300 L400 250 L440 262 L400 274" fill="#ffd82a"/><path d="M360 640 Q400 560 440 640Z" fill="#2a0a0a"/>'
for x in (150,650): b+=f'<rect x="{x-6}" y="520" width="12" height="160" fill="#3a2a1a"/><path d="M{x} 470 Q{x+24} 500 {x} 524 Q{x-24} 500 {x} 470Z" fill="#ffaa2a"/>'+glow(x,500,50,'#ffaa2a',.6)
b+='<rect y="680" width="800" height="120" fill="#0a140c"/>'
I[1399]=svg(b,d)

# 1495 115万キロのフィルム: a strip of film unrolling across the sky and turning into a long road toward the horizon
d,b=bg([(0,'#4aa0f0'),(1,'#ffe0b0')])
b+='<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#8ac86a"/><path d="M300 810 L390 560 L410 560 L500 810Z" fill="#8a8a94"/>'
b+='<path d="M80 140 Q300 60 520 200 Q620 300 420 400 Q390 470 400 560" stroke="#1a1a24" stroke-width="80" fill="none"/>'
b+='<path d="M80 140 Q300 60 520 200 Q620 300 420 400 Q390 470 400 560" stroke="#fff" stroke-width="8" stroke-dasharray="10 20" fill="none" transform="translate(0 -28)"/>'
for x,y in [(160,120),(300,110),(440,160),(540,260)]: b+=f'<rect x="{x-24}" y="{y-20}" width="48" height="40" fill="#ffd8a0" opacity=".9"/>'
I[1495]=svg(b,d)

# 613 SAY YES: an open ring box with a diamond ring catching candlelight on a table, a proposal moment
d,b=bg([(0,'#2a0a14'),(1,'#4a1424')])
b+=glow(400,440,220,'#ffd8a0',.4)
for x in (200,600): b+=f'<rect x="{x-12}" y="320" width="24" height="200" rx="4" fill="#fff6e8"/><path d="M{x} 290 Q{x+14} 310 {x} 324 Q{x-14} 310 {x} 290Z" fill="#ffd060"/>'+glow(x,300,46,'#ffd060',.7,'glow2')
b+='<rect y="520" width="800" height="280" fill="#3a1410"/>'
b+='<path d="M280 380 L520 380 L520 300 Q400 240 280 300Z" fill="#a8102a"/><rect x="280" y="380" width="240" height="160" rx="10" fill="#c8182e"/><rect x="300" y="390" width="200" height="120" rx="8" fill="#f4ece8"/>'
b+=ring(400,430,.8,'#e8f8ff')+sparkle(430,370,24,'#fff')
I[613]=svg(b,d)

# 796 DEPARTURES: a jet taking off over snowy mountains into a pale winter sky, a contrail stretching behind
d,b=bg([(0,'#5a8ae8'),(1,'#e8f0ff')])
b+='<path d="M-10 620 L160 420 L300 560 L460 360 L640 540 L810 440 L810 810 L-10 810Z" fill="#f4f8ff"/><path d="M160 420 L200 470 L130 470Z M460 360 L510 420 L420 420Z" fill="#c8d4f0"/>'
b+='<path d="M-10 640 Q400 600 810 660 L810 810 L-10 810Z" fill="#fff"/>'
b+='<path d="M60 420 Q300 300 470 230" stroke="#fff" stroke-width="12" fill="none" opacity=".8"/>'
b+='<g transform="translate(520 210) rotate(-24)"><path d="M-90 0 L80 -8 Q110 -6 110 4 Q110 12 80 12 L-90 8Z" fill="#fff"/><path d="M-10 0 L-60 -60 L-30 -60 L30 0Z M-10 6 L-60 60 L-30 60 L30 6Z" fill="#d8e0f0"/><path d="M-90 2 L-110 -30 L-90 -30 L-70 0Z" fill="#e8302a"/></g>'
I[796]=svg(b,d)

# 991 Moments: a dandelion seed head releasing its seeds into the wind against a soft evening sky
d,b=bg([(0,'#8a7ab8'),(1,'#ffc8a8')])
b+='<path d="M400 800 Q390 640 400 470" stroke="#5a8a4a" stroke-width="10" fill="none"/>'
for k in range(30):
    a=math.radians(k*12);b+=f'<path d="M400 420 L{400+100*math.cos(a):.0f} {420+100*math.sin(a):.0f}" stroke="#fff" stroke-width="3" opacity=".9"/><circle cx="{400+100*math.cos(a):.0f}" cy="{420+100*math.sin(a):.0f}" r="10" fill="#fff" opacity=".8"/>'
b+='<circle cx="400" cy="420" r="20" fill="#d8c8a8"/>'
r=R(991)
for _ in range(12):
    x,y=r.uniform(480,760),r.uniform(80,360);a=r.uniform(0,60)
    b+=f'<g transform="rotate({a:.0f} {x:.0f} {y:.0f})"><path d="M{x:.0f} {y:.0f} L{x:.0f} {y+30:.0f}" stroke="#fff" stroke-width="2"/>'+''.join(f'<path d="M{x:.0f} {y:.0f} L{x+14*math.cos(math.radians(t)):.0f} {y-14*math.sin(math.radians(t)):.0f}" stroke="#fff" stroke-width="2"/>' for t in range(20,180,30))+'</g>'
I[991]=svg(b,d)

# 1051 PIECES OF A DREAM: jigsaw pieces of a starry night sky drifting apart, a crescent moon on one of them
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a5a')])
d+=lg('pz2',S((0,'#0a1a5a'),(1,'#3a2a8a')))
for x,y,a,s in [(250,260,-14,1.1),(500,230,10,1.0),(320,520,8,1.0),(560,500,-10,1.1)]:
    b+=f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><path d="M-90 -90 L-20 -90 Q-20 -120 0 -120 Q20 -120 20 -90 L90 -90 L90 -20 Q120 -20 120 0 Q120 20 90 20 L90 90 L-90 90Z" fill="url(#pz2)" stroke="#8ab0ff" stroke-width="4"/>'+''.join(f'<circle cx="{px}" cy="{py}" r="4" fill="#fff"/>' for px,py in [(-50,-40),(30,-60),(40,40),(-30,50)])+'</g>'
b+='<path d="M490 210 A40 40 0 1 0 530 260 A32 32 0 1 1 490 210Z" fill="#fff6c8"/>'
I[1051]=svg(b,d)

# 1096 ラヴ・パレード: a parade float piled with balloons and hearts rolling down a street under confetti
d,b=bg([(0,'#5ad0ff'),(1,'#ffe8f8')])
b+=confetti(60,1096,['#ff4a8a','#ffd82a','#3ac84a','#8a4aff','#ff7a1a'])
b+='<rect y="640" width="800" height="160" fill="#8a8a94"/>'
b+='<rect x="160" y="480" width="480" height="140" rx="20" fill="#ff5aa8"/><path d="M160 520 L640 520" stroke="#fff" stroke-width="10"/>'+heart(400,420,90,'#ff2a6a')
for x,c in [(220,'#ffd82a'),(300,'#3ac84a'),(520,'#8a4aff'),(590,'#ff7a1a')]: b+=f'<path d="M{x} 480 L{x} 300" stroke="#fff" stroke-width="3"/><ellipse cx="{x}" cy="270" rx="40" ry="50" fill="{c}"/>'
for x in (220,580): b+=f'<circle cx="{x}" cy="630" r="34" fill="#2a2a34"/><circle cx="{x}" cy="630" r="12" fill="#c8c8d0"/>'
I[1096]=svg(b,d)

# 1409 The Beginning: a katana drawn across a huge rising sun, its blade catching a single streak of light
d,b=bg([(0,'#1a0a0a'),(1,'#3a0a0a')])
b+=hinomaru_sun(400,400,250,'#d8201a')
b+='<g transform="rotate(-24 400 420)"><path d="M90 410 L620 400 Q700 404 720 420 Q690 424 620 424 L90 430Z" fill="#e8ecf4"/><path d="M90 410 L620 400 Q700 404 720 420 L90 416Z" fill="#fff"/>'
b+='<rect x="60" y="400" width="36" height="40" rx="6" fill="#d8b040"/><rect x="-80" y="408" width="150" height="26" rx="10" fill="#1a1a1a"/>'+''.join(f'<path d="M{-70+k*24} 408 l12 26" stroke="#c8a040" stroke-width="5"/>' for k in range(6))+'</g>'
I[1409]=svg(b,d)

# 1470 パプリカ: a shiny red and a yellow paprika pepper side by side with flowers and confetti like a summer festival
d,b=bg([(0,'#8ae0ff'),(1,'#e8faff')])
b+=confetti(40,1470,['#ff4a4a','#ffd82a','#3ac84a','#ff8ad8'])
for x,c1,c2 in [(300,'#e8201a','#ff6a5a'),(510,'#ffc81a','#fff07a')]:
    b+=f'<path d="M{x-110} 380 Q{x-140} 560 {x-60} 640 Q{x} 680 {x+60} 640 Q{x+140} 560 {x+110} 380 Q{x} 330 {x-110} 380Z" fill="{c1}"/><path d="M{x-80} 420 Q{x-90} 540 {x-50} 600" stroke="{c2}" stroke-width="18" fill="none" stroke-linecap="round" opacity=".7"/>'
    b+=f'<path d="M{x-40} 350 Q{x} 330 {x+40} 350 L{x+20} 370 L{x-20} 370Z" fill="#3a8a2a"/><path d="M{x} 340 Q{x+10} 290 {x+40} 270" stroke="#3a8a2a" stroke-width="14" fill="none" stroke-linecap="round"/>'
for x,y in [(150,200),(660,220),(130,640),(680,660)]: b+=flower(x,y,60,5,'#ff7ab8','#ffd82a',x%40,.8)
I[1470]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
