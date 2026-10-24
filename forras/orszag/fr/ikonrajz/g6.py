import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 6. csoport (101–110)
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 101 Je sais pas: a woman sits alone on a staircase holding a question-mark shaped key, unsure how to go on without him
d,b=bg([(0,'#2a2a4a'),(.6,'#5a4a7a'),(1,'#a87aa0')])
b+=''.join(f'<rect x="{120+k*70}" y="{720-k*60}" width="{560-k*70}" height="60" fill="{["#3a2a4a","#4a3a5a"][k%2]}"/>' for k in range(8))
b+=figure(360,600,300,'#0a0610',hair='#0a0610')
b+=f'<text x="560" y="300" text-anchor="middle" {F} font-size="200" fill="#ffd8f0" opacity=".85">?</text>'+glow(560,240,120,'#ffd8f0',.3)
I[101]=svg(b,d)

# 102 Pour le plaisir: a man in a convertible drives along a coastal road at sunset, arm out the window, just for the pleasure
d,b=bg([(0,'#ff7a4a'),(.5,'#ffb86a'),(1,'#3a5a8a')])
b+=sun(600,400,90,'#fff0a0')+'<rect y="420" width="800" height="200" fill="#3a6a9a"/>'+waves(440,'#5a8ab8',5,10,.6)
b+='<rect y="600" width="800" height="200" fill="#4a4a50"/><path d="M0 690 L800 690" stroke="#fff" stroke-width="5" stroke-dasharray="40 30"/>'
b+=car(380,650,1.5,'#d8342c')+figure(380,600,160,'#1a0a0a',pose='wave')
b+=palm(90,600,300,'#2a1a1a',12)
I[102]=svg(b,d)

# 103 Les Champs-Élysées: the Arc de Triomphe at the top of the avenue, a couple strolling under the trees, at noon or midnight
d,b=bg([(0,'#7ab8e8'),(.6,'#c8e0f0'),(1,'#f0e0c0')])
b+='<polygon points="360,420 440,420 800,800 0,800" fill="#c8b8a0"/>'
b+='<g transform="translate(400 420)" fill="#e8dcc0"><rect x="-90" y="-180" width="180" height="180"/><rect x="-100" y="-200" width="200" height="30"/></g><path d="M370 420 L370 330 Q400 290 430 330 L430 420Z" fill="#7ab8e8"/>'
for k in range(5):
    for s in (-1,1): x=400+s*(80+k*70);y=440+k*80;b+=tree(x,y,120+k*40,'#4a7a3a',k*7+(s>0))
b+=figure(380,760,200,'#1a1a24',pose='hold',hair='#1a1a24')+figure(420,760,220,'#1a1a24',pose='hold')
b+=tricolore(388,190,30,20,1)
I[103]=svg(b,d)

# 104 Reine: a man kneels and places a sparkling crown on a woman's head, a gold throne and rose petals around
d,b=bg([(0,'#2a0a3a'),(.6,'#6a1a5a'),(1,'#c84a6a')])
b+='<path d="M310 720 L310 300 Q400 220 490 300 L490 720Z" fill="#c8981a"/><path d="M330 720 L330 320 Q400 260 470 320 L470 720Z" fill="#8a1a3a"/>'
b+=figure(400,720,330,'#0a0208',hair='#0a0208')+crown(400,370,.55)+glow(400,360,90,'#ffd23f',.4)
b+=figure(600,800,260,'#0a0208',pose='reachL')
r=R(104)
for k in range(12): x,y=r.uniform(40,760),r.uniform(560,780);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="12" ry="7" fill="#ff3a5a" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[104]=svg(b,d)

# 105 Tu ne m'as pas laissé le temps: a son holds an old photo of his father up against a sky where a plane draws a fading line
d,b=bg([(0,'#4a6a9a'),(.6,'#a8b8d0'),(1,'#f0d0b0')])
b+='<path d="M60 200 Q400 120 760 240" stroke="#fff" stroke-width="8" fill="none" opacity=".7" stroke-dasharray="60 20 30 20 10 20"/><path d="M760 240 l-30 -6 l10 -14Z" fill="#fff"/>'
b+=hills(640,20,'#4a5a5a',105,4)+'<rect y="680" width="800" height="120" fill="#3a4a4a"/>'
b+=figure(300,780,380,'#0a0a10',pose='reach')
b+='<g transform="translate(520 420) rotate(6)"><rect x="-70" y="-90" width="140" height="180" fill="#f6efe2"/><rect x="-56" y="-76" width="112" height="130" fill="#a89078"/><ellipse cx="0" cy="-30" rx="24" ry="28" fill="#5a4030"/><path d="M-40 54 Q0 0 40 54Z" fill="#5a4030"/></g>'
I[105]=svg(b,d)

# 106 Mafiosa: a femme fatale in a black dress and red lipstick leans on a vintage gangster car under a streetlamp
d,b=bg([(0,'#0a0a0e'),(.6,'#1a1418'),(1,'#3a1a1a')])
b+='<path d="M640 800 L640 140 Q640 100 600 100 L560 100" stroke="#2a2a30" stroke-width="14" fill="none"/><path d="M530 100 L590 100 L580 130 L540 130Z" fill="#2a2a30"/><polygon points="540,130 580,130 700,700 420,700" fill="#ffe8b0" opacity=".14"/>'+glow(560,130,70,'#ffe0a0',.7)
b+='<rect y="700" width="800" height="100" fill="#0a0808"/>'
b+=car(300,700,2.0,'#141416','#3a3a44')
b+=figure(540,720,360,'#000',hair='#000')+'<path d="M524 460 Q540 720 556 460Z" fill="#000"/><path d="M536 342 L548 342" stroke="#d8142a" stroke-width="5"/>'
I[106]=svg(b,d)

# 107 Tomber la chemise: a sweaty Toulouse bal crowd swinging their shirts over their heads in the summer night
d,b=bg([(0,'#1a0a2a'),(.6,'#6a1a3a'),(1,'#ff8a3a')])
b+='<path d="M0 120 Q400 220 800 120" stroke="#000" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{k*60}" cy="{120+math.sin(k/13*math.pi)*95:.0f}" r="10" fill="{["#ffd23f","#ff3a8a","#3ad0ff"][k%3]}"/>' for k in range(1,14))
for k in range(9):
    x=60+k*85;b+=figure(x,800,260+(k*31%60),'#0a0410',pose='up')
    c=['#ff3a5a','#3ad0ff','#ffd23f','#fff','#6aff6a'][k%5];y=800-(260+(k*31%60))*1.1-20
    b+=f'<path transform="translate({x} {y:.0f}) rotate({(k%3-1)*25})" d="M-30 -14 L-14 -20 L0 -12 L14 -20 L30 -14 L36 4 L22 6 L20 26 L-20 26 L-22 6 L-36 4Z" fill="{c}"/>'
I[107]=svg(b,d)

# 108 Bolide allemand: a sleek German sports car speeding down a night autobahn, light trails and a rapper leaning out
d,b=bg([(0,'#050510'),(.6,'#10102a'),(1,'#2a1a3a')])
b+=skyline(520,'#0a0a18',108,30,140,'#ffd36a',60)
b+='<polygon points="380,520 420,520 800,800 0,800" fill="#1a1a22"/>'
for k,c in enumerate(['#ff3a3a','#ffd23f','#ff3a3a','#fff']): b+=f'<path d="M400 520 L{-200+k*400} 800" stroke="{c}" stroke-width="5" opacity=".5"/>'
b+='<g transform="translate(400 640)"><path d="M-240 40 Q-230 -20 -150 -36 Q-60 -90 60 -86 Q160 -80 230 -20 Q250 10 240 40Z" fill="#c8ccd8"/><path d="M-120 -40 Q-50 -80 50 -78 Q110 -74 150 -36Z" fill="#1a2030"/>'
b+='<circle cx="-150" cy="40" r="40" fill="#0a0a0e"/><circle cx="150" cy="40" r="40" fill="#0a0a0e"/><circle cx="-150" cy="40" r="18" fill="#8a8a94"/><circle cx="150" cy="40" r="18" fill="#8a8a94"/><rect x="200" y="-10" width="40" height="14" fill="#ff3a3a"/></g>'
b+=glow(640,640,60,'#ff3a3a',.5)
I[108]=svg(b,d)

# 109 Un autre monde: a boy stands on a small planet looking up at another, brighter world floating in a dreamy sky
d,b=bg([(0,'#0a1030'),(.6,'#2a2a6a'),(1,'#6a4a9a')])
b+=starsf(80,109,800)
b+='<circle cx="540" cy="250" r="140" fill="#4ad0b0"/><path d="M440 200 Q520 170 560 230 Q620 260 660 220 L670 260 Q600 320 520 290 Q460 270 430 240Z" fill="#2a9a6a"/><ellipse cx="540" cy="250" rx="230" ry="40" fill="none" stroke="#ffd23f" stroke-width="8" opacity=".7"/>'+glow(540,250,200,'#8affe0',.25)
b+='<circle cx="300" cy="900" r="360" fill="#5a3a6a"/>'
b+=figure(300,560,240,'#05020a',pose='reach')
I[109]=svg(b,d)

# 110 Femme libérée: a modern woman bursts out of a kitchen apron, briefcase in hand, a birdcage door wide open behind her
d,b=bg([(0,'#ffd0a0'),(.6,'#ff9a8a'),(1,'#c85a7a')])
b+='<g transform="translate(220 360)"><path d="M-90 200 L-90 -40 Q0 -200 90 -40 L90 200Z" fill="none" stroke="#5a3a2a" stroke-width="6"/>'+''.join(f'<path d="M{x} 200 L{x} {-40-(1-abs(x)/90)*100:.0f}" stroke="#5a3a2a" stroke-width="4"/>' for x in (-50,-10,30))+'<path d="M90 0 L180 -60 L180 120 L90 160" stroke="#5a3a2a" stroke-width="5" fill="none"/><rect x="-100" y="200" width="200" height="14" fill="#5a3a2a"/></g>'
for x,y in [(380,160),(450,120),(520,170)]: b+=bird(x,y,18,'#3a1a2a')
b+=figure(560,780,420,'#2a0a1a',pose='wave',hair='#2a0a1a')
b+='<rect x="470" y="600" width="60" height="44" rx="6" fill="#3a2a1a"/><path d="M490 600 L490 590 L510 590 L510 600" stroke="#3a2a1a" stroke-width="5" fill="none"/>'
I[110]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
