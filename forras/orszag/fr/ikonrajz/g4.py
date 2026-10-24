import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 4. csoport (Top 61–80)
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 61 Copines: three phones light up with gossip bubbles around a woman who turns her back on her man's "copines"
d,b=bg([(0,'#ff9ad0'),(.6,'#c85ab0'),(1,'#5a1a6a')])
b+=figure(400,780,440,'#2a0a2a',hair='#2a0a2a')
for x,y,a in [(150,240,-15),(640,200,12),(620,470,-8)]:
    b+=f'<g transform="translate({x} {y}) rotate({a})"><rect x="-48" y="-84" width="96" height="168" rx="14" fill="#1a1a22"/><rect x="-40" y="-70" width="80" height="140" fill="#ffe6f6"/>'
    b+='<rect x="-32" y="-56" width="50" height="18" rx="8" fill="#ff5ab0"/><rect x="-18" y="-30" width="50" height="18" rx="8" fill="#c8c8d8"/><rect x="-32" y="-4" width="40" height="18" rx="8" fill="#ff5ab0"/></g>'
b+=f'<text x="190" y="540" text-anchor="middle" {F} font-size="110" fill="#fff" opacity=".9">✕</text>'
I[61]=svg(b,d)

# 62 Lettre à une femme: a handwritten letter and a red rose on a desk lit by a lamp at night, an envelope sealed with wax
d,b=bg([(0,'#1a0e0a'),(1,'#3a1e14')])
b+=glow(560,220,260,'#ffc86a',.4)
b+='<path d="M520 80 L620 80 L660 200 L480 200Z" fill="#c8302a"/><rect x="560" y="200" width="10" height="200" fill="#2a1a10"/>'
b+='<rect y="460" width="800" height="340" fill="#4a2a1a"/>'
b+='<g transform="translate(330 560) rotate(-8)"><rect x="-200" y="-150" width="320" height="300" fill="#f6efe2"/>'+''.join(f'<path d="M-170 {-110+k*34} Q-60 {-120+k*34} 90 {-110+k*34}" stroke="#2a3a6a" stroke-width="3" fill="none"/>' for k in range(7))+'</g>'
b+='<g transform="translate(600 620) rotate(10)"><rect x="-90" y="-60" width="180" height="120" fill="#e8dcc0"/><path d="M-90 -60 L0 10 L90 -60" stroke="#b8a888" stroke-width="3" fill="none"/><circle cx="0" cy="10" r="22" fill="#a8101a"/></g>'
b+=rose(560,480,1.0,'#d81a3a',stem=False)
I[62]=svg(b,d)

# 63 Bella: a man is hypnotised by a mysterious woman whose eyes glow in the dark, he stands frozen under her spell
d,b=bg([(0,'#05020a'),(.6,'#1a0a2a'),(1,'#3a0a3a')])
for k in range(6): b+=f'<circle cx="400" cy="240" r="{60+k*70}" fill="none" stroke="#c83aff" stroke-width="3" opacity="{.5-k*.07}"/>'
b+='<ellipse cx="340" cy="240" rx="56" ry="26" fill="#ffd0ff"/><ellipse cx="460" cy="240" rx="56" ry="26" fill="#ffd0ff"/><circle cx="340" cy="240" r="18" fill="#8a1aff"/><circle cx="460" cy="240" r="18" fill="#8a1aff"/>'+glow(400,240,160,'#c83aff',.35)
b+=figure(400,800,300,'#000',pose='reach')
I[63]=svg(b,d)

# 64 Ces soirées-là: three young men in 1970s suits strut into a buzzing nightclub with a neon sign
d,b=bg([(0,'#1a0a2a'),(.6,'#4a1a5a'),(1,'#ff6a5a')])
b+='<rect x="140" y="60" width="520" height="140" rx="20" fill="none" stroke="#ffd23f" stroke-width="10"/>'+glow(400,130,200,'#ffd23f',.25)
b+=''.join(f'<circle cx="{180+k*40}" cy="130" r="9" fill="#ffd23f"/>' for k in range(12))
b+='<rect y="660" width="800" height="140" fill="#1a0a14"/>'+''.join(f'<rect x="{k*100}" y="660" width="100" height="140" fill="{["#ff3a8a","#3ad0ff","#ffd23f","#8a3aff"][k%4]}" opacity=".35"/>' for k in range(8))
for x in (260,400,540): b+=figure(x,690,380,'#05020a',pose='wave' if x!=400 else 'up')
I[64]=svg(b,d)

# 65 Alane: an African baby wrapped in a colourful pagne, held up under a golden sky and a baobab
d,b=bg([(0,'#ffb04a'),(.55,'#ff7a3a'),(1,'#8a2a1a')])
b+=sun(400,360,110,'#fff0a0')
b+='<g transform="translate(130 640)" fill="#2a0e08"><rect x="-26" y="-240" width="52" height="240"/><path d="M-26 -230 Q-120 -280 -150 -300 M26 -230 Q120 -280 160 -300 M0 -240 Q0 -300 10 -330" stroke="#2a0e08" stroke-width="22" fill="none"/></g>'
b+='<rect y="640" width="800" height="160" fill="#5a2010"/>'
b+=figure(470,740,320,'#1a0604',pose='up',hair='#1a0604')
b+='<ellipse cx="470" cy="360" rx="60" ry="40" fill="#0aa8a0"/><path d="M420 360 L520 360 M430 340 L510 340 M430 380 L510 380" stroke="#ffd23f" stroke-width="6"/><circle cx="508" cy="346" r="20" fill="#3a1a0a"/>'
I[65]=svg(b,d)

# 66 Petit Papa Noël: Father Christmas's sleigh crosses a starry snowy sky above a village, a child's shoe waits by the fireplace window
d,b=bg([(0,'#0a1438'),(.6,'#1a2a5a'),(1,'#3a4a7a')])
b+=starsf(70,66,500)+moon(620,140,50)
b+='<g transform="translate(280 200)" fill="#000"><path d="M-60 0 L60 0 Q70 30 50 40 L-60 40Z" fill="#d8342c"/><path d="M-70 46 L70 46" stroke="#ffd23f" stroke-width="6"/>'
for k in range(3): b+=f'<path transform="translate({100+k*70} -10)" d="M0 0 L40 0 L44 -14 L50 -10 L48 10 L36 10 L36 26 M4 10 L4 26" stroke="#000" stroke-width="6" fill="#000"/><path transform="translate({100+k*70} -10)" d="M44 -14 L40 -30 M50 -14 L58 -28" stroke="#000" stroke-width="3"/>'
b+='<circle cx="-20" cy="-14" r="18" fill="#d8342c"/><path d="M-60 20 L270 0" stroke="#ffd23f" stroke-width="2"/></g>'
b+='<path d="M-10 640 Q400 560 810 640 L810 800 L-10 800Z" fill="#e8f0ff"/>'
for x,y in [(100,600),(220,590),(540,590),(660,600)]: b+=f'<rect x="{x}" y="{y}" width="80" height="60" fill="#3a2a2a"/><path d="M{x-10} {y} L{x+40} {y-40} L{x+90} {y}Z" fill="#fff"/><rect x="{x+28}" y="{y+16}" width="24" height="22" fill="#ffd36a"/>'
b+=snow(60,66)
I[66]=svg(b,d)

# 67 Africa: a woman runs free across the savannah with zebras and giraffes, under a giant setting sun
d,b=bg([(0,'#ffb03a'),(.55,'#ff6a2a'),(1,'#7a1a14')])
b+=sun(400,420,170,'#ffe07a')
b+='<rect y="560" width="800" height="240" fill="#6a2a10"/>'
b+='<g fill="#1a0604"><rect x="600" y="300" width="14" height="230"/><ellipse cx="640" cy="540" rx="50" ry="30"/><path d="M600 300 L590 290 L620 284Z"/><path d="M610 560 L610 620 M670 560 L670 620" stroke="#1a0604" stroke-width="10"/></g>'
b+='<g fill="#1a0604"><ellipse cx="160" cy="560" rx="70" ry="36"/><path d="M100 540 L70 490 L90 486 L120 530Z"/><path d="M120 580 L118 640 M200 580 L204 640" stroke="#1a0604" stroke-width="12"/></g>'
b+=figure(400,700,300,'#1a0604',pose='up',hair='#1a0604')
I[67]=svg(b,d)

# 68 Titanium: a figure stands unbroken in a sea of bullets that bounce off a shining metal shield of light
d,b=bg([(0,'#0a0e18'),(.6,'#1a2a3a'),(1,'#3a4a5a')])
b+='<circle cx="400" cy="450" r="230" fill="#d0e0f0" opacity=".08"/><circle cx="400" cy="450" r="230" fill="none" stroke="#e8f4ff" stroke-width="8"/>'+glow(400,450,260,'#bfe0ff',.25)
r=R(68)
for k in range(14):
    a=r.uniform(0,2*math.pi);x,y=400+math.cos(a)*250,450+math.sin(a)*250
    b+=f'<g transform="translate({x:.0f} {y:.0f}) rotate({math.degrees(a)+180:.0f})"><path d="M0 -6 L40 -6 Q56 0 40 6 L0 6Z" fill="#c8a050"/></g>'+sparkle(x,y,10,'#fff')
b+=figure(400,640,330,'#000',pose='up')
I[68]=svg(b,d)

# 69 4 Kampé: a Haitian kompa party on a terrace: couples dancing close, colourful string lights, palm trees
d,b=bg([(0,'#1a0a3a'),(.6,'#6a1a6a'),(1,'#ff5a5a')])
b+=palm(80,700,460,'#0a0410',18)+palm(730,700,420,'#0a0410',-18)
b+='<path d="M0 120 Q400 260 800 120" stroke="#0a0410" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{k*50}" cy="{120+math.sin(k/16*math.pi)*140*0.95:.0f}" r="11" fill="{["#ffd23f","#ff3a8a","#3ad0ff","#6aff6a"][k%4]}"/>' for k in range(1,16))
b+='<rect y="680" width="800" height="120" fill="#1a0614"/>'
for x in (280,520): b+=figure(x-22,700,300,'#0a0410',pose='hold',hair='#0a0410')+figure(x+22,700,320,'#0a0410',pose='hold')
I[69]=svg(b,d)

# 70 Tu m'oublieras: a teenage girl sits on her bed in tears, a torn photo of a boy at her feet, rain on the window
d,b=bg([(0,'#3a4a6a'),(1,'#6a5a7a')])
b+='<rect x="420" y="90" width="300" height="320" fill="#8aa0c0"/>'+rain(40,70,'#fff',.4)
b+='<rect x="420" y="90" width="300" height="320" fill="none" stroke="#2a2a3a" stroke-width="16"/><path d="M570 90 L570 410" stroke="#2a2a3a" stroke-width="10"/>'
b+='<rect x="60" y="520" width="520" height="100" rx="20" fill="#d8b0c8"/><rect x="60" y="620" width="520" height="40" fill="#5a3a4a"/>'
b+=figure(300,760,360,'#1a1424',hair='#1a1424')
b+='<g transform="translate(500 720) rotate(-12)"><rect x="-60" y="-44" width="56" height="88" fill="#f6efe2"/><path d="M-4 -44 L6 -20 L-4 0 L8 20 L-4 44" stroke="#f6efe2" stroke-width="2" fill="none"/><rect x="10" y="-40" width="56" height="88" fill="#f6efe2" transform="rotate(14)"/></g>'
b+='<path d="M310 378 L312 400" stroke="#9ad0ff" stroke-width="5" stroke-linecap="round"/>'
I[70]=svg(b,d)

# 71 Les Démons de minuit: a deserted city street at midnight, a big clock striking 12, little red devils dancing round a lone walker
d,b=bg([(0,'#05020e'),(.6,'#1a0a2a'),(1,'#2a0a1a')])
b+='<circle cx="400" cy="200" r="120" fill="#f6efe2"/><circle cx="400" cy="200" r="120" fill="none" stroke="#2a1a10" stroke-width="12"/>'+''.join(f'<rect x="396" y="92" width="8" height="18" fill="#2a1a10" transform="rotate({k*30} 400 200)"/>' for k in range(12))
b+='<path d="M400 200 L400 104 M400 200 L400 126" stroke="#2a1a10" stroke-width="10" stroke-linecap="round"/>'+glow(400,200,170,'#fff0c8',.25)
b+=skyline(700,'#0a0410',71,60,240,'#ff5a3a',50)
b+='<rect y="700" width="800" height="100" fill="#0a0410"/>'+figure(400,720,240,'#000')
for x,y in [(240,560),(560,540),(300,420),(520,400)]:
    b+=f'<g transform="translate({x} {y})" fill="#ff2a2a"><circle r="18"/><path d="M-14 -12 L-20 -30 L-6 -16Z M14 -12 L20 -30 L6 -16Z"/><path d="M0 18 L0 50 M0 30 L-18 20 M0 30 L18 20 M0 50 L-12 70 M0 50 L12 70" stroke="#ff2a2a" stroke-width="6"/><path d="M0 50 Q30 60 34 40" stroke="#ff2a2a" stroke-width="3" fill="none"/></g>'
I[71]=svg(b,d)

# 72 L'Aziza: a young Moroccan-Jewish woman in a star-patterned headscarf against a mosaic of crescent and star, a song against hate
d,b=bg([(0,'#0a3a5a'),(.6,'#1a6a8a'),(1,'#e8b04a')])
for i in range(9):
    for j in range(9): b+=f'<path transform="translate({i*100} {j*100}) rotate(45)" d="M0 -30 L30 0 L0 30 L-30 0Z" fill="{["#ffd23f","#fff","#d8342c"][(i+j)%3]}" opacity=".18"/>'
b+=figure(400,800,470,'#140a14',hair='#140a14')
b+='<path d="M340 380 Q400 300 460 380 L480 470 L320 470Z" fill="#d8342c"/>'+''.join(sparkle(x,y,9,'#ffd23f') for x,y in [(360,400),(400,360),(440,410),(390,440)])
b+='<path d="M640 160 a60 60 0 1 0 0 1Z" fill="#ffd23f"/><circle cx="660" cy="150" r="54" fill="#1a6a8a"/>'+sparkle(170,150,40,'#ffd23f')
I[72]=svg(b,d)

# 73 Avec le temps: an hourglass whose falling sand turns into dry autumn leaves and torn love letters
d,b=bg([(0,'#2a2a3a'),(.6,'#4a4048'),(1,'#7a5a4a')])
b+=glow(400,400,240,'#ffd8a0',.18)
b+='<rect x="250" y="120" width="300" height="30" fill="#5a3a1a"/><rect x="250" y="650" width="300" height="30" fill="#5a3a1a"/>'
b+='<path d="M280 150 L520 150 Q520 300 410 400 Q520 500 520 650 L280 650 Q280 500 390 400 Q280 300 280 150Z" fill="#e8f0ff" opacity=".22" stroke="#e8f0ff" stroke-width="5"/>'
b+='<path d="M310 190 L490 190 Q470 300 410 380 L390 380 Q330 300 310 190Z" fill="#e8c88a"/><path d="M400 390 L400 610" stroke="#e8c88a" stroke-width="5"/><path d="M300 640 Q400 560 500 640Z" fill="#e8c88a"/>'
r=R(73)
for k in range(9):
    x,y,a=r.uniform(80,720),r.uniform(500,780),r.uniform(0,360);b+=f'<path transform="translate({x:.0f} {y:.0f}) rotate({a:.0f})" d="M0 -18 Q16 0 0 18 Q-16 0 0 -18Z" fill="{r.choice(["#b8601a","#d88a3a","#8a3a1a"])}"/>'
b+='<rect x="600" y="520" width="80" height="56" fill="#f6efe2" transform="rotate(16 640 548)"/><rect x="90" y="560" width="70" height="50" fill="#f6efe2" transform="rotate(-20 120 590)"/>'
I[73]=svg(b,d)

# 74 Ramenez la coupe à la maison: the football World Cup trophy raised above a jubilant crowd waving French flags, confetti everywhere
d,b=bg([(0,'#0a2a7a'),(.6,'#2a4ab0'),(1,'#d8342c')])
b+=confetti(60,74,['#fff','#d8342c','#3a5ad8','#ffd23f'])
b+='<g transform="translate(400 310)"><path d="M-40 140 L40 140 L56 180 L-56 180Z" fill="#2a6a3a"/><path d="M-30 140 Q-20 60 -70 0 Q-80 -80 0 -110 Q80 -80 70 0 Q20 60 30 140Z" fill="#ffd23f"/><circle cx="0" cy="-110" r="50" fill="#ffe07a"/><path d="M-30 -130 Q0 -100 30 -130 M-40 -100 Q0 -80 40 -100" stroke="#c8981a" stroke-width="5" fill="none"/></g>'+glow(400,250,180,'#fff4b0',.4)
for k in range(15): x=k*56;b+=figure(x,800,180+(k*41%60),'#05081a',pose='up')
b+=tricolore(80,560,90,60,1)+tricolore(640,540,90,60,1)
I[74]=svg(b,d)

# 75 Tous les mêmes: a face split down the middle, half man half woman, a red tie on one side and lipstick on the other
d,b=bg([(0,'#1a1a2a'),(.5,'#3a3a5a'),(1,'#1a1a2a')])
b+='<rect x="0" y="0" width="400" height="800" fill="#2a4a8a" opacity=".5"/><rect x="400" y="0" width="400" height="800" fill="#c84a7a" opacity=".5"/>'
b+='<path d="M400 140 Q280 140 270 300 Q262 440 330 520 L400 560Z" fill="#e8c8a8"/><path d="M400 140 Q520 140 530 300 Q538 440 470 520 L400 560Z" fill="#f0d0b8"/>'
b+='<path d="M400 120 Q280 110 260 280 L280 240 Q330 170 400 170Z" fill="#2a1a10"/><path d="M400 120 Q560 110 580 300 Q590 470 520 560 L520 300 Q500 180 400 170Z" fill="#3a1a14"/>'
b+='<ellipse cx="340" cy="320" rx="20" ry="12" fill="#2a2a3a"/><ellipse cx="460" cy="320" rx="20" ry="12" fill="#2a2a3a"/><path d="M440 304 L484 300" stroke="#000" stroke-width="5"/>'
b+='<path d="M360 440 L400 444" stroke="#8a4a3a" stroke-width="7"/><path d="M400 432 Q430 424 444 440 Q430 456 400 452Z" fill="#d8142a"/>'
b+='<path d="M400 560 L400 800" stroke="#fff" stroke-width="4"/><path d="M330 600 L400 600 L400 800 L280 800 Z" fill="#1a2a4a"/><path d="M380 600 L400 600 L400 720 L370 680Z" fill="#d8142a"/><path d="M400 600 L470 600 L520 800 L400 800Z" fill="#3a0a1a"/>'
I[75]=svg(b,d)

# 76 Je l'aime à mourir: a gardener holds out a single sunflower to a woman, a heart-shaped hedge behind them in golden light
d,b=bg([(0,'#ffe8a0'),(.6,'#ffc06a'),(1,'#c86a3a')])
b+=glow(400,250,240,'#fff',.4)
b+=heart(400,340,150,'#5a8a3a')+heart(400,340,120,'#6a9a4a')
b+='<rect y="620" width="800" height="180" fill="#8a6a3a"/>'
b+=figure(270,700,330,'#2a140a',pose='reach')+figure(540,700,320,'#2a140a',hair='#2a140a')
b+='<path d="M420 460 L380 520" stroke="#3a6a1a" stroke-width="7"/>'+''.join(f'<ellipse cx="{430+math.cos(a)*30:.0f}" cy="{448+math.sin(a)*30:.0f}" rx="14" ry="7" fill="#ffd23f" transform="rotate({math.degrees(a):.0f} {430+math.cos(a)*30:.0f} {448+math.sin(a)*30:.0f})"/>' for a in [i*math.pi/6 for i in range(12)])+'<circle cx="430" cy="448" r="18" fill="#6a3a10"/>'
I[76]=svg(b,d)

# 77 Le Temps: a tall man in a white suit sings to a giant pocket watch whose hands have stopped, roses in the night
d,b=bg([(0,'#0a0a1a'),(.6,'#1a1a3a'),(1,'#3a1a2a')])
b+='<circle cx="460" cy="320" r="200" fill="#e8d8b0"/><circle cx="460" cy="320" r="200" fill="none" stroke="#c8981a" stroke-width="22"/><circle cx="460" cy="320" r="170" fill="none" stroke="#5a4a2a" stroke-width="3"/>'
b+=''.join(f'<rect x="456" y="140" width="8" height="24" fill="#3a2a1a" transform="rotate({k*30} 460 320)"/>' for k in range(12))
b+='<path d="M460 320 L460 190 M460 320 L560 380" stroke="#3a2a1a" stroke-width="10" stroke-linecap="round"/><circle cx="460" cy="320" r="12" fill="#3a2a1a"/><rect x="440" y="90" width="40" height="40" rx="8" fill="#c8981a"/>'
b+=figure(200,780,430,'#f6efe2')
b+=rose(560,700,.9,'#d81a3a',stem=False)+rose(660,730,.8,'#d81a3a',stem=False)
I[77]=svg(b,d)

# 78 Je t'aime: a woman with arms flung wide sings a huge "je t'aime" into the night, a burst of red hearts rising
d,b=bg([(0,'#1a0414'),(.6,'#4a0a2a'),(1,'#a81a3a')])
b+=rays(400,320,20,'#ff8ab0',.1,5)
b+=figure(400,800,430,'#0a0206',pose='up',hair='#0a0206')
r=R(78)
for k in range(16):
    x,y,s=r.uniform(80,720),r.uniform(60,420),r.uniform(14,40);b+=heart(x,y,s,r.choice(['#ff3a5a','#ff6a8a','#d81a3a']))
I[78]=svg(b,d)

# 79 Sapés comme jamais: a sharply dressed duo in designer suits strike poses on a fashion runway lit by camera flashes
d,b=bg([(0,'#0a0a10'),(.6,'#1a1a24'),(1,'#3a3a4a')])
b+='<polygon points="300,300 500,300 760,800 40,800" fill="#2a2a34"/><path d="M400 300 L400 800" stroke="#ffd23f" stroke-width="3" opacity=".4"/>'
for x,y in [(80,380),(720,360),(120,620),(680,640),(60,180),(740,160)]: b+=sparkle(x,y,30,'#fff')+glow(x,y,60,'#fff',.5)
for x in (330,470):
    b+=figure(x,700,400,'#000')+f'<path d="M{x-8} 400 L{x} 470 L{x+8} 400Z" fill="#d8342c"/><path d="M{x-40} 326 L{x+40} 326 L{x+28} 296 L{x-28} 296Z" fill="#000"/><rect x="{x-22}" y="340" width="44" height="10" rx="4" fill="#ffd23f"/>'
I[79]=svg(b,d)

# 80 Mwaka Moon: two rappers on the surface of the moon, a huge Earth rising behind them, a party in zero gravity
d,b=bg([(0,'#020208'),(1,'#0a0a1e')])
b+=starsf(120,80,800)
b+='<circle cx="560" cy="250" r="140" fill="#2a6ad0"/><path d="M480 170 Q540 200 520 260 Q560 300 600 280 Q640 220 620 160Z M600 330 Q650 330 670 300" fill="#3aa04a"/><circle cx="560" cy="250" r="140" fill="url(#vig)" opacity=".4"/>'+glow(560,250,180,'#6ab0ff',.25)
b+='<path d="M-10 600 Q400 540 810 600 L810 800 L-10 800Z" fill="#9a9aa8"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r_}" ry="{r_/3:.0f}" fill="#7a7a88"/>' for x,y,r_ in [(120,680,50),(560,720,70),(700,640,30)])
b+=figure(300,640,280,'#0a0a14',pose='up')+figure(440,610,260,'#0a0a14',pose='wave')
for x,y in [(220,300),(260,240),(360,280)]: b+=f'<circle cx="{x}" cy="{y}" r="8" fill="#ffd23f"/>'
I[80]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
