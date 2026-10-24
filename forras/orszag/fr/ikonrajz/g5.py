import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 5. csoport (Top 81–100)
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 81 Chocolat: a big melting chocolate heart dripping onto a dance floor where a couple dances a sultry raï step
d,b=bg([(0,'#3a1a0a'),(.6,'#6a3a1a'),(1,'#c87a3a')])
b+='<path d="M400 140 C330 60 180 90 190 220 C200 330 330 380 400 440 C470 380 600 330 610 220 C620 90 470 60 400 140Z" fill="#5a2a10"/>'
b+=''.join(f'<path d="M{x} {y} L{x} {y+l} a10 10 0 0 0 20 0 L{x+20} {y}" fill="#5a2a10"/>' for x,y,l in [(250,300,90),(320,370,120),(450,370,70),(530,300,110)])
b+='<path d="M300 140 Q340 110 380 140" stroke="#8a4a20" stroke-width="12" fill="none" stroke-linecap="round"/>'
b+='<rect y="660" width="800" height="140" fill="#2a1006"/>'+figure(370,700,240,'#1a0804',pose='hold')+figure(430,700,220,'#1a0804',pose='up',hair='#1a0804')
I[81]=svg(b,d)

# 82 Le téléphone pleure: an old red telephone weeping big tears, a little girl's voice coming from the receiver
d,b=bg([(0,'#3a4a7a'),(.6,'#6a7aa8'),(1,'#a8b0d0')])
b+=phone(400,480,1.6,'#d8342c')
for x,y in [(280,330),(520,310),(300,600),(520,620)]: b+=f'<path d="M{x} {y} Q{x-18} {y+30} {x} {y+44} Q{x+18} {y+30} {x} {y}Z" fill="#9ad0ff"/>'
b+=heart(640,170,30,'#ff8aa8')+f'<path d="M590 220 Q520 250 500 300" stroke="#fff" stroke-width="4" fill="none" stroke-dasharray="8 8"/>'
I[82]=svg(b,d)

# 83 Emmenez-moi: a dock worker gazes at a big ocean liner sailing toward a tropical sunset, dreaming of far lands
d,b=bg([(0,'#ff8a4a'),(.5,'#ffc07a'),(1,'#2a5a8a')])
b+=sun(560,380,80,'#fff0a0')+'<rect y="400" width="800" height="400" fill="#2a5a8a"/>'+waves(420,'#4a7aa8',5,12,.6)
b+=palm(700,410,180,'#2a1a2a',-10)
b+='<g transform="translate(470 400)"><path d="M-160 -10 L160 -10 L130 30 L-140 30Z" fill="#1a1a2a"/><rect x="-110" y="-50" width="200" height="40" fill="#f6efe2"/><rect x="-80" y="-80" width="130" height="30" fill="#f6efe2"/><rect x="-40" y="-130" width="30" height="50" fill="#d8342c"/><rect x="10" y="-130" width="30" height="50" fill="#d8342c"/></g>'
b+='<rect y="600" width="800" height="200" fill="#3a2a2a"/><rect x="60" y="500" width="80" height="100" fill="#5a3a2a"/><rect x="160" y="530" width="70" height="70" fill="#6a4a2a"/>'
b+=figure(320,610,260,'#0a0608',pose='reach')
I[83]=svg(b,d)

# 84 Petit génie: a young genius lifts off a lamp's magic smoke that forms a crown and stars over a city at dusk
d,b=bg([(0,'#1a0a4a'),(.6,'#5a2a8a'),(1,'#ff8a6a')])
b+=skyline(760,'#140828',84,40,160,'#ffd36a',80)
b+='<path d="M300 640 Q400 600 500 640 L480 670 L320 670Z" fill="#ffd23f"/><path d="M500 640 Q560 620 580 600" stroke="#ffd23f" stroke-width="12" fill="none"/><rect x="380" y="670" width="40" height="20" fill="#c8981a"/>'
b+='<path d="M400 600 Q340 500 420 440 Q500 380 420 300 Q360 250 420 200" stroke="#bfe8ff" stroke-width="40" fill="none" opacity=".45" stroke-linecap="round"/>'
b+=crown(420,170,.9)+''.join(sparkle(x,y,16,'#fff') for x,y in [(320,240),(520,300),(300,420),(540,160)])
I[84]=svg(b,d)

# 85 La kiffance: a guy chills in a deckchair with sunglasses and a cold drink on a sunny balcony, ice cubes and good vibes
d,b=bg([(0,'#4ad0ff'),(.6,'#9ae8ff'),(1,'#ffe07a')])
b+=sun(620,140,70,'#fff4a0')
b+='<rect y="560" width="800" height="240" fill="#e8805a"/><rect y="540" width="800" height="24" fill="#f6efe2"/>'+''.join(f'<rect x="{k*60}" y="440" width="10" height="100" fill="#f6efe2"/>' for k in range(14))+'<rect y="430" width="800" height="14" fill="#f6efe2"/>'
b+='<path d="M220 700 L300 520 L460 560 L520 700" stroke="#2a3a5a" stroke-width="10" fill="none"/><path d="M300 520 L460 560 L420 640 L270 620Z" fill="#ff5a6a"/>'
b+='<circle cx="320" cy="470" r="34" fill="#2a1a10"/><rect x="290" y="458" width="60" height="16" rx="6" fill="#000"/>'
b+='<path d="M350 520 L470 580 L520 640" stroke="#2a1a10" stroke-width="30" fill="none" stroke-linecap="round"/>'
b+='<rect x="590" y="580" width="54" height="90" rx="6" fill="#bfe8ff" opacity=".8"/><rect x="600" y="600" width="18" height="18" fill="#fff"/><rect x="616" y="624" width="18" height="18" fill="#fff"/><path d="M630 580 L650 530" stroke="#ff5a6a" stroke-width="5"/>'
I[85]=svg(b,d)

# 86 Une belle histoire: two strangers meet on a summer motorway: their two cars side by side, a heart floating between them
d,b=bg([(0,'#7ad0f0'),(.6,'#c8f0e8'),(1,'#f0e0a0')])
b+=sun(140,130,50,'#fff4a0')+hills(460,30,'#8ac06a',86,4)
b+='<polygon points="340,460 460,460 800,800 0,800" fill="#6a6a70"/><path d="M400 470 L400 800" stroke="#fff" stroke-width="6" stroke-dasharray="30 30"/>'
b+=car(250,680,1.0,'#d8342c')+car(560,670,1.0,'#2a6ad0')
b+=heart(405,420,44,'#ff4a6a')+glow(405,420,70,'#fff',.4)
I[86]=svg(b,d)

# 87 Que je t'aime: a rocker on his knees on stage, arms wide, his whole body a cry of love in red flames
d,b=bg([(0,'#1a0204'),(.6,'#5a0a0a'),(1,'#d8341a')])
for k in range(9): b+=f'<path d="M{k*100} 800 Q{k*100+40} 640 {k*100+10} 520 Q{k*100+70} 620 {k*100+90} 800Z" fill="#ff8a1a" opacity=".55"/>'
b+='<rect y="700" width="800" height="100" fill="#0a0204"/>'
b+='<g transform="translate(400 700)" fill="#000"><ellipse cx="0" cy="-330" rx="30" ry="36"/><path d="M-44 -290 Q0 -300 44 -290 L36 -150 L-36 -150Z"/><path d="M-36 -150 L36 -150 L70 -60 L60 0 L20 0 L20 -60 L-20 -60 L-20 0 L-60 0 L-70 -60Z"/>'
b+='<path d="M40 -280 Q140 -320 220 -400 M-40 -280 Q-140 -320 -220 -400" stroke="#000" stroke-width="20" fill="none" stroke-linecap="round"/></g>'
b+=heart(400,200,70,'#ff2a2a')+glow(400,200,120,'#ff5a3a',.5)
I[87]=svg(b,d)

# 88 Mon vieux: an old father's empty armchair by the window, his cap and reading glasses left on the newspaper
d,b=bg([(0,'#3a2a1a'),(1,'#6a4a2a')])
b+='<rect x="500" y="100" width="220" height="320" fill="#ffd8a0"/><rect x="500" y="100" width="220" height="320" fill="none" stroke="#2a1a0a" stroke-width="14"/><path d="M610 100 L610 420 M500 260 L720 260" stroke="#2a1a0a" stroke-width="8"/>'+glow(610,260,220,'#ffd8a0',.3)
b+='<rect y="640" width="800" height="160" fill="#3a2010"/>'
b+='<path d="M160 640 L160 380 Q160 320 230 320 L380 320 Q450 320 450 380 L450 640" fill="#8a3a2a"/><rect x="120" y="480" width="370" height="120" rx="30" fill="#a84a3a"/><rect x="110" y="440" width="60" height="180" rx="24" fill="#7a2a1a"/><rect x="440" y="440" width="60" height="180" rx="24" fill="#7a2a1a"/>'
b+='<path d="M220 470 Q300 430 360 470 L360 480 L220 480Z" fill="#3a3a44"/><path d="M200 480 L380 480" stroke="#2a2a34" stroke-width="6"/>'
b+='<rect x="540" y="590" width="160" height="40" fill="#f6efe2" transform="rotate(-6 620 610)"/><circle cx="590" cy="596" r="16" fill="none" stroke="#1a1a1a" stroke-width="4"/><circle cx="630" cy="592" r="16" fill="none" stroke="#1a1a1a" stroke-width="4"/>'
I[88]=svg(b,d)

# 89 Rockollection: a jukebox glowing in a 1960s café, vinyl records spinning out of it, each a rock'n'roll memory
d,b=bg([(0,'#1a0a2a'),(.6,'#3a1a4a'),(1,'#8a2a4a')])
b+='<path d="M250 760 L250 300 Q250 130 400 130 Q550 130 550 300 L550 760Z" fill="#d8342c"/><path d="M280 740 L280 310 Q280 170 400 170 Q520 170 520 310 L520 740Z" fill="#ffd23f"/>'
b+='<path d="M300 340 Q300 200 400 200 Q500 200 500 340Z" fill="#ff8ad0" opacity=".8"/><rect x="300" y="360" width="200" height="140" fill="#2a1a2a"/>'+''.join(f'<rect x="{310+k*20}" y="380" width="12" height="100" fill="#fff" opacity=".7"/>' for k in range(9))
b+='<rect x="300" y="520" width="200" height="200" fill="#c8202a"/>'+''.join(f'<path d="M310 {540+k*20} L490 {540+k*20}" stroke="#ffd23f" stroke-width="5"/>' for k in range(9))
b+=glow(400,300,240,'#ff8ad0',.25)
b+=vinyl(130,250,70)+vinyl(670,220,60,'#2a6ad0')+vinyl(110,560,50,'#ffd23f')+vinyl(690,520,56,'#2ad07a')
I[89]=svg(b,d)

# 90 Sur ma route: a young man walks alone down a long road into the sunrise, a backpack, a winding path of obstacles behind
d,b=bg([(0,'#ffb06a'),(.5,'#ffd8a0'),(1,'#8a6a5a')])
b+=sun(400,330,100,'#fff4c0')
b+='<path d="M-10 400 L810 400 L810 800 L-10 800Z" fill="#6a5a4a"/><path d="M360 400 L440 400 Q600 560 520 800 L180 800 Q320 560 360 400Z" fill="#3a3030"/><path d="M400 420 Q480 560 360 800" stroke="#ffd23f" stroke-width="6" fill="none" stroke-dasharray="26 22"/>'
b+=figure(420,690,280,'#0a0606')+'<rect x="440" y="470" width="50" height="80" rx="12" fill="#0a0606"/>'
for x,y in [(140,560),(660,540),(100,700),(700,720)]: b+=f'<path d="M{x-40} {y+20} L{x} {y-40} L{x+40} {y+20}Z" fill="#4a3a30"/>'
I[90]=svg(b,d)

# 91 Résiste: a woman stands firm against a stormy wind that bends everything else, her raised fist lit by a ray of light
d,b=bg([(0,'#1a1a2a'),(.6,'#3a3a5a'),(1,'#5a4a6a')])
b+='<polygon points="440,0 520,0 480,800 360,800" fill="#ffe8a0" opacity=".25"/>'
b+=rain(80,91,'#bfd0ff',.35,30)
b+=tree(130,700,300,'#0a0a14',91).replace('<g','<g transform="rotate(20 130 700)"',1)
b+='<rect y="700" width="800" height="100" fill="#0a0a14"/>'
b+=figure(440,720,400,'#000',pose='wave',hair='#000')
for k in range(4): b+=f'<path d="M{40+k*60} {200+k*90} Q{200+k*60} {180+k*90} {300+k*60} {220+k*90}" stroke="#fff" stroke-width="4" opacity=".3" fill="none"/>'
I[91]=svg(b,d)

# 92 Requiem pour un fou: a man stands behind prison bars at dawn, a single white rose lying on the ground outside
d,b=bg([(0,'#1a1414'),(.6,'#3a2a24'),(1,'#7a4a3a')])
b+=glow(400,280,240,'#ffc08a',.3)
b+=figure(400,720,420,'#000')
b+=''.join(f'<rect x="{60+k*76}" y="60" width="16" height="680" fill="#2a2a30"/>' for k in range(10))+'<rect x="40" y="60" width="720" height="20" fill="#2a2a30"/><rect x="40" y="420" width="720" height="16" fill="#2a2a30"/>'
b+='<rect y="720" width="800" height="80" fill="#140c0a"/>'+rose(600,720,1.1,'#fbf6ee',stem=False)
I[92]=svg(b,d)

# 93 One More Time: a crowd of hands under exploding laser lights and confetti at the moment the beat drops again
d,b=bg([(0,'#0a0220'),(.6,'#2a0a5a'),(1,'#ff3a8a')])
for k,c in enumerate(['#ff2a8a','#2ad0ff','#ffd23f','#8aff4a','#ff2a8a','#2ad0ff']): b+=f'<path d="M400 140 L{-100+k*200} 800" stroke="{c}" stroke-width="6" opacity=".55"/>'
b+=glow(400,140,120,'#fff',.6)+'<circle cx="400" cy="140" r="30" fill="#fff"/>'
b+=confetti(50,93,['#ff2a8a','#2ad0ff','#ffd23f','#fff'],0,520)
for k in range(13): x=20+k*64;b+=f'<path d="M{x} 800 L{x+4} 640 L{x-10} 600 M{x+4} 640 L{x+16} 604" stroke="#05020a" stroke-width="16" stroke-linecap="round"/>'
I[93]=svg(b,d)

# 94 Pookie: a stylish woman with a tiny handbag walks past a lineup of admirers, all with cartoon heart eyes
d,b=bg([(0,'#ffd0e8'),(.6,'#ff9ac8'),(1,'#c83a8a')])
b+=figure(420,780,450,'#2a0a2a',pose='wave',hair='#2a0a2a')
b+='<rect x="350" y="560" width="50" height="40" rx="8" fill="#ffd23f"/><path d="M360 560 Q375 530 390 560" stroke="#ffd23f" stroke-width="5" fill="none"/>'
for x in (120,640,720):
    b+=f'<g transform="translate({x} 520)"><circle r="56" fill="#ffe07a"/>'+heart(-20,-10,14,'#ff2a5a')+heart(20,-10,14,'#ff2a5a')+'<path d="M-24 22 Q0 40 24 22" stroke="#7a3a1a" stroke-width="6" fill="none"/></g>'
I[94]=svg(b,d)

# 95 Le Pénitencier: a stone prison fortress on a cliff by night, a mother waiting at its gate under a searchlight
d,b=bg([(0,'#050a14'),(.6,'#101a2a'),(1,'#1a2a3a')])
b+=moon(140,130,40)
b+='<polygon points="560,120 600,120 800,520 400,520" fill="#e8f0ff" opacity=".12"/>'
b+='<rect x="220" y="260" width="400" height="300" fill="#3a3a44"/>'+''.join(f'<rect x="{220+k*50}" y="236" width="30" height="30" fill="#3a3a44"/>' for k in range(8))
b+='<rect x="540" y="120" width="80" height="440" fill="#2a2a34"/><rect x="530" y="100" width="100" height="30" fill="#2a2a34"/><circle cx="580" cy="130" r="14" fill="#fff6c0"/>'
b+=''.join(f'<rect x="{260+k*70}" y="320" width="16" height="36" fill="#fff0a0" opacity="{.8 if k%2 else .2}"/>' for k in range(4))
b+='<path d="M360 560 L360 460 Q400 420 440 460 L440 560Z" fill="#0a0a10"/>'+''.join(f'<path d="M{370+k*14} 456 L{370+k*14} 560" stroke="#5a5a64" stroke-width="3"/>' for k in range(6))
b+='<path d="M-10 560 L810 560 L810 800 L-10 800Z" fill="#141820"/>'+figure(300,700,200,'#000',hair='#000')
I[95]=svg(b,d)

# 96 Quand la musique est bonne: a guitar amp turned to max, a crowd of friends dancing and jumping in a sunny backyard party
d,b=bg([(0,'#ffd23f'),(.6,'#ffa83a'),(1,'#e8603a')])
b+=sun(640,130,60,'#fff4a0')
b+='<rect y="620" width="800" height="180" fill="#6a8a3a"/>'
b+='<rect x="320" y="420" width="200" height="220" rx="12" fill="#1a1a1a"/><rect x="340" y="460" width="160" height="160" fill="#3a3a3a"/>'+''.join(f'<path d="M340 {470+k*16} L500 {470+k*16}" stroke="#2a2a2a" stroke-width="5"/>' for k in range(10))+''.join(f'<circle cx="{350+k*22}" cy="440" r="7" fill="#ffd23f"/>' for k in range(7))
b+=guitar(250,500,1.0,rot=-25)
for x,p in [(100,'up'),(170,'wave'),(620,'up'),(700,'wave')]: b+=figure(x,660,250,'#3a1a10',pose=p)
for x,y in [(560,360),(600,300),(480,320)]: b+=note(x,y,24,'#3a1a10')
I[96]=svg(b,d)

# 97 Dur dur d'être bébé !: a toddler in a nappy with a dummy dances to music, wobbly on his chubby legs, toys all around
d,b=bg([(0,'#a8e0ff'),(.6,'#ffe0f0'),(1,'#ffd08a')])
b+='<rect y="620" width="800" height="180" fill="#ffb8d0"/>'
b+='<g transform="translate(400 600)"><ellipse cx="0" cy="-300" rx="90" ry="86" fill="#ffd8b8"/><path d="M-30 -380 Q0 -400 20 -380" stroke="#c88a4a" stroke-width="10" fill="none"/>'
b+='<circle cx="-34" cy="-310" r="10" fill="#2a1a10"/><circle cx="34" cy="-310" r="10" fill="#2a1a10"/><circle cx="0" cy="-262" r="22" fill="#4ab0ff"/><circle cx="0" cy="-262" r="10" fill="#ffd23f"/>'
b+='<ellipse cx="0" cy="-130" rx="90" ry="100" fill="#ffd8b8"/><path d="M-90 -90 Q0 -40 90 -90 L80 -20 Q0 20 -80 -20Z" fill="#fff"/>'
b+='<path d="M-50 -20 L-70 20 M50 -20 L80 10" stroke="#ffd8b8" stroke-width="44" stroke-linecap="round"/><path d="M-80 -170 L-160 -230 M80 -170 L160 -230" stroke="#ffd8b8" stroke-width="36" stroke-linecap="round"/></g>'
b+='<rect x="90" y="560" width="80" height="80" fill="#ff5a5a"/><text x="130" y="620" text-anchor="middle" '+F+' font-size="56" fill="#fff">A</text><rect x="620" y="580" width="70" height="70" fill="#4ab05a"/><text x="655" y="634" text-anchor="middle" '+F+' font-size="50" fill="#fff">B</text>'
for x,y in [(150,200),(660,180)]: b+=note(x,y,26,'#5a3a8a')
I[97]=svg(b,d)

# 98 Désolé: a young man in a hoodie with his back to a grey housing estate, looking at a ticket to leave everything
d,b=bg([(0,'#5a6070'),(.6,'#8a8a90'),(1,'#3a3a44')])
b+='<rect x="60" y="120" width="300" height="580" fill="#4a4a54"/><rect x="420" y="180" width="320" height="520" fill="#40404a"/>'
for x0,y0,w,h in ((60,120,300,580),(420,180,320,520)):
    for i in range(w//50):
        for j in range(h//56): b+=f'<rect x="{x0+14+i*50}" y="{y0+20+j*56}" width="26" height="30" fill="{"#e8c87a" if (i*7+j*3)%9==0 else "#2a2a34"}"/>'
b+='<rect y="700" width="800" height="100" fill="#2a2a30"/>'
b+=figure(400,780,420,'#0a0a0e',pose='hold')
b+='<path d="M368 400 Q400 360 432 400 L440 450 L360 450Z" fill="#0a0a0e"/>'
I[98]=svg(b,d)

# 99 Hey Oh: five boys of a boy band on a city rooftop at sunset, arms in the air, a mic stand and a boombox
d,b=bg([(0,'#ff6a3a'),(.5,'#ffa84a'),(1,'#6a2a5a')])
b+=sun(400,420,90,'#fff0a0')
b+=skyline(600,'#3a1a2a',99,40,200,'#ffd36a',40)
b+='<rect y="600" width="800" height="200" fill="#2a1020"/>'
for k,x in enumerate((180,290,400,510,620)): b+=figure(x,660,300,'#0a0408',pose='up' if k%2==0 else 'wave')
b+=micro(400,720,.7)
I[99]=svg(b,d)

# 100 L'Aventurier: a comic-book adventurer with a fedora and a torch in a jungle temple, a golden idol glowing
d,b=bg([(0,'#0a1a10'),(.6,'#1a3a20'),(1,'#3a2a14')])
b+='<path d="M200 800 L200 300 L400 140 L600 300 L600 800Z" fill="#5a4a30"/><path d="M300 800 L300 420 Q400 340 500 420 L500 800Z" fill="#140c06"/>'
b+=''.join(f'<path d="M200 {320+k*60} L600 {320+k*60}" stroke="#3a3020" stroke-width="5"/>' for k in range(8))
b+='<path d="M380 600 L420 600 L430 560 Q400 520 370 560Z" fill="#ffd23f"/><circle cx="400" cy="530" r="20" fill="#ffd23f"/>'+glow(400,560,110,'#ffd23f',.5)
for x in (60,740): b+=palm(x,800,520,'#0a1a0a',10 if x<400 else -10)
b+=figure(250,780,380,'#000',pose='wave')+'<path d="M216 424 L284 424 L272 398 Q250 376 228 398Z" fill="#000"/><path d="M200 428 L300 428" stroke="#000" stroke-width="10"/>'
b+='<path d="M358 390 L374 330" stroke="#4a2a10" stroke-width="10"/><path d="M374 330 Q364 290 384 270 Q394 300 390 320Z" fill="#ff8a1a"/>'+glow(380,300,60,'#ffb04a',.6)
I[100]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
