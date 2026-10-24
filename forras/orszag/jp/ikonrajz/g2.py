import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
# Natsumero: 2. csoport (index szerint a következő 40), 2026-10-24
I={}
def cloud(x,y,s,col='#fff',op=.92):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{col}" opacity="{op}"><ellipse cx="0" cy="0" rx="90" ry="34"/><circle cx="-30" cy="-22" r="34"/><circle cx="24" cy="-30" r="42"/><circle cx="62" cy="-8" r="28"/></g>'
def flower(x,y,r,n,col,mid,rot=0,petal=.55):
    o=f'<g transform="translate({x} {y}) rotate({rot})">'
    for k in range(n): o+=f'<ellipse cx="0" cy="{-r*.55:.1f}" rx="{r*petal*.5:.1f}" ry="{r*.5:.1f}" fill="{col}" transform="rotate({k*360/n:.1f})"/>'
    return o+f'<circle r="{r*.25:.1f}" fill="{mid}"/></g>'
def snow(n,seed,op=.85,y1=800):
    r=R(seed);return ''.join(f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(0,y1):.0f}" r="{r.choice([2,3,4,5])}" fill="#fff" opacity="{r.uniform(.4,op):.2f}"/>' for _ in range(n))
def bolt(pts,col,w=8,op=1):
    return f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>'

# 1463 ピースサイン: a hand raised in a peace sign against a bright sunrise, a paper plane gliding past
d,b=bg([(0,'#ffcf5a'),(.5,'#ff8a3a'),(1,'#3a6ac8')],0,1)
b+=rays(400,620,22,'#fff6c8',.25,6)+glow(400,620,220,'#fff2b0',.7)
b+='<g fill="#2a1a3a"><path d="M330 800 L340 560 Q340 520 380 512 L460 512 Q500 520 500 560 L486 800Z"/>'
b+='<rect x="352" y="300" width="50" height="250" rx="25" transform="rotate(-12 377 540)"/><rect x="420" y="300" width="50" height="250" rx="25" transform="rotate(12 445 540)"/>'
b+='<path d="M470 560 Q520 540 530 580 Q520 610 480 600Z"/><path d="M336 600 Q300 560 330 540 L360 560Z"/></g>'
b+='<path d="M560 230 L700 180 L610 260 Z" fill="#fff"/><path d="M610 260 L620 220 L700 180Z" fill="#d8e4f4"/>'
b+='<path d="M560 236 Q480 260 420 240" stroke="#fff" stroke-width="3" stroke-dasharray="8 10" fill="none" opacity=".7"/>'
I[1463]=svg(b,d)

# 1519 アイドル: an idol on a blazing stage, star-shaped spotlights and a sea of glowing penlights below
d,b=bg([(0,'#1a0a3a'),(.6,'#5a1a7a'),(1,'#1a0a2a')])
for a,c in [(250,'#ff6ad8'),(400,'#ffe05a'),(550,'#6ae0ff')]: b+=f'<polygon points="{a},-20 {a-140},640 {a+140},640" fill="{c}" opacity=".14"/>'
b+=glow(400,470,200,'#ff8ae8',.45)
b+='<path d="M120 640 L680 640 L740 700 L60 700Z" fill="#2a0a3a"/>'
b+=figure(400,640,330,'#0a0414',pose='up',hair='#0a0414')
for x,y,s in [(400,200,60),(220,280,30),(590,260,36)]: b+=f'<path d="'+' '.join(f'{"M" if k==0 else "L"}{x+s*(1 if k%2==0 else .42)*math.sin(k*math.pi/5):.1f} {y-s*(1 if k%2==0 else .42)*math.cos(k*math.pi/5):.1f}' for k in range(10))+'Z" fill="#ffe86a"/>'
r=R(1519)
for _ in range(90):
    x=r.uniform(0,800);y=r.uniform(712,800);c=r.choice(['#ff6ad8','#6ae0ff','#ffe05a','#ffffff'])
    b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="5" height="28" rx="2.5" fill="{c}" transform="rotate({r.uniform(-25,25):.0f} {x:.0f} {y:.0f})"/>'
I[1519]=svg(b,d)

# 1489 I LOVE...: a big heart painted in bright mismatched brush strokes, splashes of colour all around
d,b=bg([(0,'#fff8f0'),(1,'#ffe6d8')])
r=R(1489)
for _ in range(26):
    x,y,s=r.uniform(60,740),r.uniform(60,740),r.uniform(6,22);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="{r.choice(["#ff4a6a","#ffb02a","#2ac8a8","#4a8aff","#c84aff"])}" opacity=".7"/>'
for k,c in enumerate(['#ff4a6a','#ffb02a','#2ac8a8','#4a8aff','#c84aff']):
    b+=f'<path d="M400 {640-k*6} C{170+k*10} {470} {200+k*14} {240+k*8} 400 {330+k*10} C{600-k*14} {240+k*8} {630-k*10} 470 400 {640-k*6}Z" fill="none" stroke="{c}" stroke-width="{34-k*3}" stroke-linejoin="round" opacity=".9"/>'
I[1489]=svg(b,d)

# 1490 Subtitle: a quiet snowy night seen through a window, a subtitle bar of words glowing at the bottom like a film
d,b=bg([(0,'#0a1a3a'),(1,'#2a4a7a')])
b+=snow(120,1490)+skyline(560,'#0a1428',1490,60,220,'#ffd88a',50)
b+='<rect y="560" width="800" height="240" fill="#e8f0fa"/><path d="M0 560 Q200 540 400 560 T800 560 L800 580 L0 580Z" fill="#fff"/>'
b+=figure(300,720,160,'#1a2a4a')+figure(350,720,150,'#1a2a4a',hair='#1a2a4a')
b+='<rect x="140" y="736" width="520" height="44" rx="10" fill="#000" opacity=".55"/>'
for k,w in enumerate([120,80,150,60]): b+=f'<rect x="{170+sum([120,80,150,60][:k])+k*14}" y="750" width="{w}" height="16" rx="8" fill="#fff" opacity=".9"/>'
I[1490]=svg(b,d)

# 1466 KICK BACK: a chunky boot kicking through yellow-black hazard stripes, debris and paint splatter flying
d,b=bg([(0,'#ffd800'),(1,'#ffb000')])
for k in range(-4,14): b+=f'<polygon points="{k*90},800 {k*90+45},800 {k*90+445},0 {k*90+400},0" fill="#141414" opacity=".88"/>'
b+='<rect x="0" y="230" width="800" height="340" fill="#ffd800"/>'
b+=glow(430,400,200,'#ff2a2a',.35)
b+='<g transform="rotate(-18 400 420)"><path d="M150 330 L420 330 L440 420 L640 430 Q690 440 690 490 L690 520 L150 520Z" fill="#1a1a1a"/><rect x="150" y="510" width="545" height="34" rx="8" fill="#e82a2a"/><path d="M300 330 L300 430 M360 330 L360 430" stroke="#fff" stroke-width="10"/></g>'
r=R(1466)
for _ in range(14):
    x,y=r.uniform(520,780),r.uniform(200,600);s=r.uniform(14,34);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{s:.0f}" height="{s*.6:.0f}" fill="#e82a2a" transform="rotate({r.uniform(0,90):.0f} {x:.0f} {y:.0f})"/>'
I[1466]=svg(b,d)

# 1467 IRIS OUT: a black screen closing in a film-style iris circle, inside it a red evening sky with a single iris flower
d,b=bg([(0,'#ff4a3a'),(1,'#7a0a2a')])
b+=glow(400,420,180,'#ffb06a',.6)
b+='<path d="M400 700 Q396 560 410 430" stroke="#2a6a3a" stroke-width="10" fill="none"/><path d="M402 640 Q350 560 330 470 Q380 540 404 600Z" fill="#3a8a4a"/>'
b+='<g transform="translate(410 400)">'+''.join(f'<path transform="rotate({a})" d="M0 0 C-50 -20 -40 -120 0 -130 C40 -120 50 -20 0 0Z" fill="{c}"/>' for a,c in [(0,'#6a3ae8'),(120,'#6a3ae8'),(240,'#6a3ae8'),(60,'#a48aff'),(180,'#a48aff'),(300,'#a48aff')])+'<circle r="16" fill="#ffd84a"/></g>'
b+='<path fill-rule="evenodd" d="M0 0 H800 V800 H0Z M400 140 A270 270 0 1 0 400.1 140Z" fill="#050505"/>'
b+='<circle cx="400" cy="410" r="270" fill="none" stroke="#fff" stroke-width="3" opacity=".25"/>'
I[1467]=svg(b,d)

# 1533 ドライフラワー: a bouquet of dried roses hung upside down on a wall in faded afternoon light
d,b=bg([(0,'#f2e2c8'),(1,'#c8a888')])
b+='<polygon points="0,0 380,0 800,520 800,800 520,800" fill="#fff6e0" opacity=".25"/>'
b+='<rect x="360" y="60" width="80" height="18" rx="9" fill="#6a4a3a"/><path d="M400 78 L400 120" stroke="#8a6a50" stroke-width="5"/>'
b+='<path d="M372 120 L428 120 L420 170 L380 170Z" fill="#a8502a"/>'
r=R(1533)
for k in range(9):
    a=-40+k*10;L=r.uniform(260,330);ex=400+L*math.sin(math.radians(a));ey=160+L*math.cos(math.radians(a))
    b+=f'<path d="M400 160 L{ex:.0f} {ey:.0f}" stroke="#7a6a3a" stroke-width="6"/>'
    b+=f'<g transform="translate({ex:.0f} {ey:.0f})"><circle r="34" fill="{r.choice(["#8a3a3a","#a8584a","#6a2a3a","#b07a5a"])}"/><path d="M-20 -10 Q0 -30 20 -10 M-24 8 Q0 -12 24 8 M-14 22 Q0 6 14 22" stroke="#3a1a1a" stroke-width="4" fill="none" opacity=".5"/></g>'
for x,y in [(340,300),(460,300),(400,360)]: b+=f'<path d="M{x} {y} q-24 10 -30 40 q20 -6 30 -40Z" fill="#7a7a4a"/>'
I[1533]=svg(b,d)

# 1468 馬と鹿: a horse and a deer side by side on a muddy rugby field at dusk, an oval ball at their feet
d,b=bg([(0,'#3a2a5a'),(.55,'#c86a4a'),(1,'#5a3a2a')])
b+='<path d="M180 120 L180 560 M620 120 L620 560 M180 360 L620 360" stroke="#f4e8d8" stroke-width="10" opacity=".55"/>'
b+='<rect y="560" width="800" height="240" fill="#3a5a2a"/><path d="M0 610 L800 600" stroke="#fff" stroke-width="5" opacity=".4"/>'
b+=('<g fill="#120a08"><path d="M170 560 L190 430 Q200 380 260 370 L380 368 Q400 330 420 290 L440 250 Q470 240 480 270 L460 310 Q440 340 430 380 L420 440 L410 560 L392 560 L386 460 L280 460 L260 560 L242 560 L240 470 Q220 470 210 500 L194 560Z"/>'
    '<path d="M440 250 L436 226 L452 244Z"/><path d="M380 368 Q360 330 380 300 L400 290Z" opacity=".7"/></g>')
b+=('<g fill="#2a140c"><path d="M520 560 L530 450 Q540 420 580 416 L660 416 Q672 380 680 350 Q700 330 716 346 L706 380 Q694 420 690 450 L684 560 L670 560 L666 470 L590 470 L570 560 L556 560 L550 480 L538 560Z"/>'
    '<path d="M684 346 L670 300 L656 290 M676 316 L690 290 M704 342 L716 296 L730 286 M712 312 L700 290" stroke="#2a140c" stroke-width="6" fill="none"/></g>')
b+='<ellipse cx="460" cy="610" rx="44" ry="26" fill="#a8582a" transform="rotate(-20 460 610)"/><path d="M432 604 L488 616" stroke="#fff" stroke-width="3"/>'
I[1468]=svg(b,d)

# 1570 ライラック: clusters of lilac blossoms in spring wind, a gleaming trumpet resting among them
d,b=bg([(0,'#e8f4ff'),(.6,'#cfe0ff'),(1,'#a8c8f0')])
b+=glow(560,240,200,'#ffffff',.6)
def lilac(x,y,s,c1,c2,seed):
    rr=R(seed);o=''
    for _ in range(46):
        t=rr.random();yy=y-t*220*s;w=(1-t)*70*s+10*s
        o+=flower(x+rr.uniform(-w,w),yy,rr.uniform(12,20)*s,4,rr.choice([c1,c2]),'#fff6ff',rr.uniform(0,90),.9)
    return o
b+='<path d="M250 800 Q260 600 300 520 M520 800 Q520 640 560 560" stroke="#5a8a4a" stroke-width="9" fill="none"/>'
b+=lilac(300,560,1.2,'#a888e8','#c8a8ff',1)+lilac(560,600,1.0,'#8a6ad8','#b898f0',2)
b+='<g transform="rotate(-18 430 650)"><rect x="220" y="634" width="300" height="20" rx="10" fill="#e8b830"/><path d="M520 620 L640 570 L640 718 L520 668Z" fill="#f8d050"/><rect x="330" y="610" width="16" height="30" fill="#c8981a"/><rect x="370" y="610" width="16" height="30" fill="#c8981a"/><rect x="410" y="610" width="16" height="30" fill="#c8981a"/><rect x="200" y="628" width="26" height="32" rx="6" fill="#c8981a"/></g>'
I[1570]=svg(b,d)

# 1496 MIXED NUTS: a bowl overflowing with mixed nuts, one shiny peanut tumbling out in front
d,b=bg([(0,'#2a4a3a'),(1,'#0a2a2a')])
b+=glow(400,480,240,'#ffd88a',.35)
b+='<ellipse cx="400" cy="560" rx="260" ry="60" fill="#8a3a2a"/><path d="M140 560 Q160 720 400 730 Q640 720 660 560Z" fill="#b8503a"/>'
r=R(1496)
for _ in range(60):
    x=r.uniform(170,630);y=r.uniform(470,560)-max(0,90-abs(x-400)/3);k=r.randint(0,2);a=r.uniform(0,180)
    c=['#c88a4a','#e8c07a','#8a5a2a'][k]
    b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{[24,18,20][k]}" ry="{[14,16,13][k]}" fill="{c}" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+='<g transform="rotate(-20 560 700)"><path d="M500 700 Q500 660 540 664 Q560 670 580 664 Q620 660 620 700 Q620 740 580 736 Q560 730 540 736 Q500 740 500 700Z" fill="#e8b878"/><path d="M520 690 l10 6 M560 680 l0 12 M590 690 l-8 8" stroke="#a8784a" stroke-width="4"/></g>'
I[1496]=svg(b,d)

# 1417 クリスマスソング: a lone figure under a softly lit Christmas tree in a snowy city square
d,b=bg([(0,'#0a1430'),(1,'#1a2a4a')])
b+=snow(110,1417)+skyline(600,'#0e1a34',1417,80,260,'#ffd88a',60)
b+=glow(400,420,220,'#ffd88a',.35)
for k in range(5):
    w=60+k*44;y=200+k*90
    b+=f'<path d="M{400-w} {y+100} L400 {y-40} L{400+w} {y+100}Z" fill="#1a5a3a"/>'
r=R(17)
for _ in range(40):
    t=r.random();y=170+t*450;w=(t*230)*.9;b+=f'<circle cx="{400+r.uniform(-w,w):.0f}" cy="{y:.0f}" r="6" fill="{r.choice(["#ffe05a","#ff5a5a","#fff6c8","#5ad8ff"])}"/>'
b+=sparkle(400,150,34,'#ffe86a')+'<rect x="380" y="620" width="40" height="50" fill="#3a2414"/>'
b+='<rect y="660" width="800" height="140" fill="#e8f0fa"/>'+figure(600,760,200,'#0a1020')
I[1417]=svg(b,d)

# 1544 うっせぇわ: a megaphone blasting a jagged shout across a grey office, papers and a loosened tie flying
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<path d="M420 400 L800 120 L800 680Z" fill="#e8102a" opacity=".85"/>'
for k in range(4): b+=f'<path d="M{470+k*80} {400-80-k*50} Q{510+k*80} 400 {470+k*80} {400+80+k*50}" stroke="#fff" stroke-width="10" fill="none" opacity=".8"/>'
b+='<g transform="rotate(-10 300 400)"><path d="M140 360 L360 300 L360 500 L140 440Z" fill="#f4f4f4"/><rect x="100" y="356" width="50" height="88" rx="10" fill="#d8d8d8"/><rect x="200" y="436" width="30" height="80" rx="8" fill="#2a2a2a"/><ellipse cx="360" cy="400" rx="24" ry="100" fill="#c8c8c8"/></g>'
r=R(1544)
for _ in range(9):
    x,y=r.uniform(60,760),r.uniform(80,760);a=r.uniform(-40,40)
    if 100<x<480 and 280<y<540: continue
    b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="60" height="78" fill="#fff" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+='<path d="M560 640 L600 600 L640 640 L620 760 L600 790 L580 760Z" fill="#2a4ae8" transform="rotate(30 600 700)"/>'
I[1544]=svg(b,d)

# 1545 New Genesis: a brand-new sun bursting over a calm sea, giant musical notes rising into the morning sky
d,b=bg([(0,'#ff4a6a'),(.5,'#ffb04a'),(1,'#fff2c8')])
b+=rays(400,520,26,'#ffffff',.2,5)+glow(400,520,200,'#fff6d8',.8)+hinomaru_sun(400,520,110,'#fffbe8')
b+='<rect y="540" width="800" height="260" fill="#3a6ac8"/>'
for k in range(8): b+=f'<rect x="{300-k*14}" y="{560+k*28}" width="{200+k*28}" height="6" rx="3" fill="#fff6d8" opacity="{.8-k*.08:.2f}"/>'
b+=note(200,330,46,'#fff',True)+note(560,250,40,'#fff')+note(640,420,30,'#fff6e0',True)+note(150,180,26,'#fff6e0')
I[1545]=svg(b,d)

# 1481 マリーゴールド: a girl in a straw hat standing in a sea of orange marigolds under a high summer sky
d,b=bg([(0,'#3aa0f0'),(.6,'#9ad8ff'),(1,'#e8f6ff')])
b+=cloud(200,180,1.2)+cloud(600,130,.9)
b+='<path d="M-10 480 Q400 430 810 480 L810 810 L-10 810Z" fill="#4a8a2a"/>'
b+=figure(400,640,260,'#3a2a1a',hair='#3a2a1a')+'<ellipse cx="400" cy="382" rx="62" ry="14" fill="#f2d48a"/><path d="M372 382 Q376 344 400 342 Q424 344 428 382Z" fill="#f2d48a"/><rect x="372" y="370" width="56" height="8" fill="#e8502a"/>'
r=R(1481)
for _ in range(140):
    y=r.uniform(470,800);x=r.uniform(-20,820);s=(y-430)/9
    b+=flower(x,y,s,10,r.choice(['#ff8a00','#ffa81a','#f86a00']),'#c84a00',r.uniform(0,40),.5)
I[1481]=svg(b,d)

# 1455 アイデア: a glowing light bulb with a green sprout growing inside it, rays of morning light around
d,b=bg([(0,'#fff2c8'),(1,'#ffc86a')])
b+=rays(400,330,18,'#ffffff',.35,7)+glow(400,330,200,'#fffbe0',.8)
b+='<path d="M400 120 C510 120 570 210 560 300 C550 380 490 410 480 470 L320 470 C310 410 250 380 240 300 C230 210 290 120 400 120Z" fill="#fffef4" stroke="#e8c050" stroke-width="8"/>'
b+='<path d="M400 440 Q396 360 410 300" stroke="#3a8a3a" stroke-width="10" fill="none"/><path d="M406 330 Q460 270 500 290 Q470 340 406 330Z M402 360 Q340 310 300 330 Q330 380 402 360Z" fill="#4ab04a"/>'
for k in range(4): b+=f'<rect x="{318+k*2}" y="{476+k*28}" width="{164-k*4}" height="22" rx="8" fill="{["#9aa0b0","#7a8090","#9aa0b0","#5a6070"][k]}"/>'
b+='<path d="M360 588 Q400 620 440 588Z" fill="#5a6070"/>'
I[1455]=svg(b,d)

# 1474 Plazma: a crackling sphere of violet plasma in deep space, lightning arcs reaching out from its core
d,b=bg([(0,'#04020e'),(1,'#120a2a')])
b+=starsf(80,1474,800,'#c8b8ff')+glow(400,400,240,'#8a4aff',.55)
d+=rg('pz',S((0,'#ffffff'),(.3,'#d8b8ff'),(.7,'#7a3ae8',.6),(1,'#3a0a8a',.2)),.5,.5,.5)
b+='<circle cx="400" cy="400" r="200" fill="url(#pz)"/>'
r=R(1474)
for k in range(9):
    a=k*40+r.uniform(-10,10);pts=[(400,400)]
    for j in range(1,6):
        L=j*40;pts.append((round(400+L*math.cos(math.radians(a))+r.uniform(-18,18)),round(400+L*math.sin(math.radians(a))+r.uniform(-18,18))))
    b+=bolt(pts,'#f0e0ff',5,.9)
b+='<circle cx="400" cy="400" r="200" fill="none" stroke="#e8d8ff" stroke-width="4" opacity=".6"/><circle cx="400" cy="400" r="34" fill="#fff"/>'
I[1474]=svg(b,d)

# 1475 M八七: the red star of the M87 galaxy glowing in deep space, a beam of silver light shooting from it
d,b=bg([(0,'#020210'),(1,'#0a0a2a')])
b+=starsf(120,1475,800,'#e8f0ff')
d+=rg('gx',S((0,'#ffe8c8'),(.25,'#ff8a5a',.8),(.6,'#8a2a6a',.35),(1,'#2a0a3a',0)),.5,.5,.5)
b+='<ellipse cx="400" cy="420" rx="330" ry="140" fill="url(#gx)" transform="rotate(-20 400 420)"/>'
b+='<polygon points="400,420 820,20 820,90" fill="#e8f4ff" opacity=".35"/><polygon points="400,420 820,40 820,70" fill="#ffffff" opacity=".6"/>'
b+=glow(400,420,90,'#ff4a3a',.9)+'<circle cx="400" cy="420" r="40" fill="#ff3a2a"/><circle cx="392" cy="410" r="14" fill="#ffd8c8"/>'
I[1475]=svg(b,d)

# 1457 ドラえもん: a bamboo-copter whirring through a blue sky, a stack of dorayaki pancakes floating below it
d,b=bg([(0,'#1a8ae8'),(1,'#9ad8ff')])
b+=cloud(170,620,1.1)+cloud(640,680,1.3)+cloud(620,160,.7)
b+='<ellipse cx="400" cy="220" rx="190" ry="16" fill="#f8d84a"/><rect x="392" y="220" width="16" height="70" fill="#f8d84a"/><ellipse cx="400" cy="296" rx="40" ry="14" fill="#e8b830"/>'
for k in range(3): b+=f'<path d="M{230+k*50} {196-k*6} q30 -20 60 0" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>'
for k in range(3):
    y=470+k*60
    b+=f'<ellipse cx="400" cy="{y+18}" rx="150" ry="40" fill="#a8582a"/><ellipse cx="400" cy="{y}" rx="150" ry="40" fill="#c8783a"/><ellipse cx="400" cy="{y-6}" rx="130" ry="30" fill="#e09a4a"/><rect x="250" y="{y+14}" width="300" height="10" fill="#5a1a1a"/>'
I[1457]=svg(b,d)

# 1585 オトノケ: shadowy yokai with glowing eyes creeping out of a dark alley, sound waves rippling through the night
d,b=bg([(0,'#1a2a3a'),(.6,'#2a3a5a'),(1,'#3a2a4a')])
b+=moon(620,150,50,'#e8f0c8')
b+='<path d="M0 800 L0 200 L180 200 L200 800Z M800 800 L800 160 L600 180 L590 800Z" fill="#06060e"/>'
for k in range(5): b+=f'<path d="M{250+k*20} {300+k*60} q150 -40 300 0" stroke="#7aff9a" stroke-width="4" fill="none" opacity="{.6-k*.1:.1f}"/>'
r=R(1585)
for x,y,s in [(300,560,120),(500,600,90),(410,470,70)]:
    b+=f'<path d="M{x-s} {y+s} Q{x-s*1.1} {y-s*.8} {x} {y-s} Q{x+s*1.1} {y-s*.8} {x+s} {y+s} Q{x+s*.5} {y+s*.6} {x} {y+s} Q{x-s*.5} {y+s*.6} {x-s} {y+s}Z" fill="#5a2a6a"/>'
    b+=glow(x-s*.3,y-s*.3,s*.25,'#ff4a4a',.8,'glow2')+f'<circle cx="{x-s*.3}" cy="{y-s*.3}" r="{s*.12}" fill="#ffe05a"/><circle cx="{x+s*.3}" cy="{y-s*.3}" r="{s*.12}" fill="#ffe05a"/>'
I[1585]=svg(b,d)

# 1506 AIZO: a cracked mirror split down the middle, a red heart reflected whole on one side and shattered on the other
d,b=bg([(0,'#12041a'),(1,'#3a0a2a')])
b+=glow(400,400,240,'#c82a6a',.4)
b+='<rect x="200" y="140" width="400" height="520" rx="200" fill="#c8c8d8"/><rect x="220" y="160" width="360" height="480" rx="180" fill="#2a1a3a"/>'
b+=heart(330,400,70,'#e8203a')
b+='<g fill="#e8203a"><path d="M470 360 L500 340 L520 380Z"/><path d="M510 400 L560 380 L540 430Z"/><path d="M450 420 L490 410 L480 460Z"/><path d="M490 470 L530 460 L500 500Z"/></g>'
b+=bolt([(400,160),(380,260),(420,330),(390,420),(430,520),(400,640)],'#ffffff',4,.8)
I[1506]=svg(b,d)

# 1591 晩餐歌: a candle-lit dinner table set for two, empty chair across, warm light in a dark room
d,b=bg([(0,'#1a0e0a'),(1,'#3a2014')])
b+=glow(400,380,240,'#ffb050',.45)
b+='<path d="M80 520 L720 520 L800 800 L0 800Z" fill="#7a2a1a"/><path d="M80 520 L720 520 L730 540 L70 540Z" fill="#f4e8d8"/>'
for x in (360,440):
    b+=f'<rect x="{x-9}" y="350" width="18" height="170" rx="4" fill="#fff6e8"/><path d="M{x} 320 Q{x+12} 340 {x} 352 Q{x-12} 340 {x} 320Z" fill="#ffd060"/>'+glow(x,336,40,'#ffd060',.6,'glow2')
for x in (210,590): b+=f'<ellipse cx="{x}" cy="610" rx="90" ry="30" fill="#f8f4ec"/><ellipse cx="{x}" cy="606" rx="50" ry="16" fill="#e8dcc8"/>'
b+='<path d="M150 600 L150 680 M270 600 L270 680 M530 600 L530 680 M650 600 L650 680" stroke="#c8c8d0" stroke-width="6"/>'
b+='<path d="M520 300 L520 520 M680 300 L680 520 M520 300 Q600 270 680 300" stroke="#2a140c" stroke-width="14" fill="none" opacity=".7"/>'
I[1591]=svg(b,d)

# 970 One Last Kiss: an instant photo of a sunset, stamped with a single red lipstick kiss
d,b=bg([(0,'#1a2a4a'),(1,'#5a3a6a')])
b+=glow(400,400,240,'#ffb0c8',.3)
b+='<g transform="rotate(-6 400 400)"><rect x="170" y="150" width="460" height="540" rx="8" fill="#fbf8f2"/><rect x="200" y="180" width="400" height="400" fill="#ff9a6a"/>'
b+='<rect x="200" y="380" width="400" height="200" fill="#3a5a8a"/><circle cx="400" cy="380" r="80" fill="#ffe0a0"/><rect x="200" y="380" width="400" height="200" fill="#2a4a7a" opacity=".85"/>'
b+='<path d="M200 330 Q300 300 400 330 T600 320 L600 380 L200 380Z" fill="#5a3a6a"/></g>'
b+='<g transform="translate(470 560) rotate(-14)"><path d="M-70 0 Q-40 -40 -6 -18 Q0 -26 6 -18 Q40 -40 70 0 Q36 10 0 6 Q-36 10 -70 0Z" fill="#d81030"/><path d="M-70 4 Q-36 14 0 10 Q36 14 70 4 Q40 50 0 46 Q-40 50 -70 4Z" fill="#b80a28"/></g>'
I[970]=svg(b,d)

# 1477 打上花火: huge fireworks blooming over a seaside town at night, their light scattered on the waves
d,b=bg([(0,'#04062a'),(1,'#121a4a')])
b+=firework(400,250,190,'#ffd27a',34,1)+firework(200,180,110,'#ff6ab8',24,2)+firework(620,170,120,'#6ae0ff',24,3)
b+='<rect y="560" width="800" height="240" fill="#060a24"/>'
r=R(1477)
for _ in range(60): b+=f'<rect x="{r.uniform(0,800):.0f}" y="{r.uniform(570,760):.0f}" width="{r.uniform(10,40):.0f}" height="3" fill="{r.choice(["#ffd27a","#ff6ab8","#6ae0ff"])}" opacity="{r.uniform(.3,.7):.2f}"/>'
b+='<path d="M-10 560 L120 520 L180 540 L260 500 L330 560Z" fill="#03051a"/>'+figure(620,760,150,'#020310')+figure(660,760,140,'#020310',hair='#020310')
I[1477]=svg(b,d)

# 972 Can You Keep A Secret?: a golden padlock with a heart-shaped keyhole, a finger pressed to lips in silhouette behind
d,b=bg([(0,'#2a0a2a'),(1,'#5a1a4a')])
b+=profile(240,760,2.2,'#1a0618')+'<rect x="292" y="370" width="22" height="100" rx="11" fill="#1a0618" transform="rotate(-8 300 420)"/>'
b+=glow(520,470,170,'#ffd86a',.4)
b+='<path d="M440 400 L440 320 Q440 240 520 240 Q600 240 600 320 L600 400" stroke="#c8c8d0" stroke-width="34" fill="none"/>'
d+=lg('lk',S((0,'#ffe68a'),(1,'#c8901a')))
b+='<rect x="400" y="390" width="240" height="210" rx="30" fill="url(#lk)"/>'+heart(520,480,30,'#3a1020')+'<rect x="512" y="500" width="16" height="50" rx="6" fill="#3a1020"/>'
I[972]=svg(b,d)

# 1508 一途: a single silver ring glowing with purple fire on a dark background, a vow kept forever
d,b=bg([(0,'#0a0614'),(1,'#1a0a2a')])
b+=glow(400,420,230,'#8a3aff',.5)
for k in range(10):
    a=k*36;b+=f'<path d="M{400+150*math.cos(math.radians(a)):.0f} {430+70*math.sin(math.radians(a)):.0f} q{20*math.cos(math.radians(a)):.0f} -60 0 -120" stroke="#b07aff" stroke-width="8" fill="none" opacity=".5" stroke-linecap="round"/>'
b+='<ellipse cx="400" cy="440" rx="170" ry="80" fill="none" stroke="#d8d8e8" stroke-width="34"/><ellipse cx="400" cy="440" rx="170" ry="80" fill="none" stroke="#ffffff" stroke-width="8" opacity=".6" stroke-dasharray="120 400"/>'
b+='<path d="M400 340 L360 300 L400 240 L440 300Z" fill="#e8d8ff"/><path d="M400 340 L360 300 L440 300Z" fill="#b89aff"/>'
I[1508]=svg(b,d)

# 1578 クスシキ: an apothecary's mortar full of herbs and flowers, steam curling up beside a red palace lantern
d,b=bg([(0,'#3a0a14'),(1,'#1a0a0a')])
b+=chochin(620,220,90,'#d8302a','#ffb070')
b+='<path d="M120 560 Q130 720 340 730 Q550 720 560 560Z" fill="#7a6a5a"/><ellipse cx="340" cy="560" rx="220" ry="46" fill="#a8988a"/><ellipse cx="340" cy="562" rx="190" ry="34" fill="#3a2a1a"/>'
b+=flower(270,550,40,5,'#ffd0e0','#ffe05a',10)+flower(400,546,34,5,'#f8f0d8','#e8a030',30)
b+='<path d="M300 556 q20 -40 60 -30 M330 560 q30 -30 70 -20" stroke="#4a8a3a" stroke-width="8" fill="none"/>'
b+='<rect x="400" y="420" width="30" height="190" rx="14" fill="#c8b8a8" transform="rotate(30 415 515)"/>'
for k in range(3): b+=f'<path d="M{260+k*60} 500 q-20 -40 0 -80 q20 -40 0 -80" stroke="#fff" stroke-width="6" fill="none" opacity=".25"/>'
I[1578]=svg(b,d)

# 1459 不思議: a hand reaching up to a mysterious floating orb, strange little objects drifting weightless around it
d,b=bg([(0,'#1a3a5a'),(.6,'#5a7aa8'),(1,'#c8d8e8')])
b+=glow(400,300,160,'#fff6e0',.7)+'<circle cx="400" cy="300" r="70" fill="#fffbe8"/>'
b+='<g fill="#1a2a3a"><path d="M330 800 L340 560 Q350 520 390 520 L430 520 Q460 530 460 560 L460 800Z"/><rect x="368" y="430" width="22" height="110" rx="11"/><rect x="396" y="414" width="22" height="120" rx="11"/><rect x="424" y="430" width="22" height="110" rx="11"/></g>'
for x,y,s,c in [(200,200,30,'#ffd27a'),(610,190,26,'#ff9ab8'),(240,420,20,'#9ad8ff'),(590,410,24,'#c8a8ff'),(520,130,16,'#fff')]:
    b+=f'<rect x="{x-s}" y="{y-s}" width="{2*s}" height="{2*s}" rx="{s*.3}" fill="{c}" transform="rotate(25 {x} {y})" opacity=".9"/>'
I[1459]=svg(b,d)

# 1075 アゲハ蝶: a large swallowtail butterfly with black-and-yellow wings gliding over a summer field
d,b=bg([(0,'#5ab0e8'),(.6,'#a8e0f8'),(1,'#7ac85a')])
b+=glow(400,380,240,'#ffffff',.4)
b+='<g transform="translate(400 380)">'
for sx in (-1,1):
    b+=f'<g transform="scale({sx} 1)"><path d="M0 -10 C60 -170 230 -200 250 -120 C260 -60 160 -10 0 0Z" fill="#141414"/><path d="M10 -20 C70 -150 200 -170 220 -116 C226 -70 150 -30 10 -10Z" fill="#ffd82a"/>'
    b+='<path d="M60 -60 L180 -150 M80 -30 L210 -100" stroke="#141414" stroke-width="10"/>'
    b+=f'<path d="M0 0 C120 10 190 70 150 140 C130 170 100 150 70 200 L60 150 C40 120 10 60 0 0Z" fill="#141414"/><path d="M10 10 C100 26 150 70 130 120 C110 140 80 110 60 120 C40 90 20 50 10 10Z" fill="#ffd82a"/><circle cx="110" cy="130" r="14" fill="#2a6ae8"/><circle cx="80" cy="150" r="10" fill="#e8402a"/></g>'
b+='<rect x="-8" y="-40" width="16" height="140" rx="8" fill="#141414"/><path d="M-4 -40 Q-30 -100 -50 -120 M4 -40 Q30 -100 50 -120" stroke="#141414" stroke-width="4" fill="none"/></g>'
I[1075]=svg(b,d)

# 1395 Habit: a classroom chair balanced on one leg mid-dance in a spotlight, other chairs stacked in a tilted tower
d,b=bg([(0,'#e8e0d0'),(1,'#a89a88')])
b+='<polygon points="400,-20 220,800 580,800" fill="#fff" opacity=".35"/>'
def chair(x,y,s,rot,c='#2a6ae8'):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-60" y="-160" width="120" height="90" rx="10" fill="{c}"/><rect x="-60" y="-20" width="130" height="24" rx="6" fill="#c89a5a"/><path d="M-54 4 L-54 120 M60 4 L60 120 M-54 -70 L-54 -10 M54 -70 L54 -10" stroke="#5a5a64" stroke-width="10"/></g>'
b+=chair(400,560,1.6,-18)+chair(140,640,.9,10,'#5a5a64')+chair(660,640,.9,-12,'#e8502a')+chair(660,520,.9,8,'#5a5a64')
b+='<rect y="740" width="800" height="60" fill="#7a6a58"/>'
I[1395]=svg(b,d)

# 1446 残響散歌: red lanterns over a night street in an old pleasure district, echo ripples spreading through the air
d,b=bg([(0,'#1a0408'),(1,'#3a0a14')])
for k in range(5): b+=f'<circle cx="400" cy="420" r="{90+k*70}" fill="none" stroke="#ff8a6a" stroke-width="5" opacity="{.45-k*.07:.2f}"/>'
b+='<path d="M0 800 L0 300 L160 260 L200 800Z M800 800 L800 280 L640 250 L600 800Z" fill="#12030a"/>'
b+='<path d="M0 220 Q400 300 800 210" stroke="#2a0a0a" stroke-width="5" fill="none"/>'
for x,y,s in [(120,250,44),(260,290,52),(400,302,60),(540,288,52),(680,240,44)]: b+=chochin(x,y+s,s,'#e8302a','#ffa060')
b+=seigaiha(640,'#ff8a6a',.18,36)
I[1446]=svg(b,d)

# 1460 ファミリーソング: a little house with warm lit windows, laundry of every size flapping on the line on a sunny day
d,b=bg([(0,'#7ac8f8'),(1,'#e8f6ff')])
b+=cloud(600,140,.9)+'<path d="M-10 620 Q400 560 810 620 L810 810 L-10 810Z" fill="#7ac85a"/>'
b+='<path d="M80 600 L80 380 L210 290 L340 380 L340 600Z" fill="#f4e0c0"/><path d="M60 390 L210 270 L360 390" stroke="#c84a3a" stroke-width="28" fill="none"/>'
b+='<rect x="120" y="440" width="60" height="56" fill="#ffd27a"/><rect x="240" y="440" width="60" height="56" fill="#ffd27a"/><rect x="180" y="520" width="56" height="80" fill="#8a5a3a"/>'
b+='<path d="M380 360 Q560 400 760 350" stroke="#5a5a5a" stroke-width="4" fill="none"/>'
for x,w,h,c in [(410,60,90,'#ff7a7a'),(490,90,110,'#5a9aff'),(600,46,70,'#ffd84a'),(670,70,96,'#8ad87a')]:
    yy=365+ (x-380)*0.05
    b+=f'<path d="M{x} {yy:.0f} L{x+w} {yy:.0f} L{x+w-6} {yy+h:.0f} L{x+6} {yy+h:.0f}Z" fill="{c}"/>'
I[1460]=svg(b,d)

# 973 Goodbye Happiness: a yellow smiley balloon drifting away out of an open window into a bright blue sky
d,b=bg([(0,'#4aa8f8'),(1,'#c8e8ff')])
b+=cloud(200,600,1.0)+cloud(600,700,1.2)
b+='<rect x="0" y="420" width="300" height="380" fill="#f4e8d8"/><rect x="40" y="460" width="220" height="200" fill="#8ac8f0"/><path d="M40 460 L150 520 L150 660 L40 660Z" fill="#fff" opacity=".6"/><rect x="0" y="660" width="300" height="20" fill="#c8b8a8"/>'
b+='<path d="M180 640 Q300 500 420 400 Q480 340 470 300" stroke="#5a5a5a" stroke-width="3" fill="none"/>'
b+='<circle cx="490" cy="220" r="110" fill="#ffd82a"/><path d="M470 330 L490 314 L510 330Z" fill="#ffd82a"/><circle cx="455" cy="195" r="12" fill="#3a2a0a"/><circle cx="525" cy="195" r="12" fill="#3a2a0a"/><path d="M440 250 Q490 290 540 250" stroke="#3a2a0a" stroke-width="10" fill="none" stroke-linecap="round"/><ellipse cx="450" cy="160" rx="24" ry="14" fill="#fff" opacity=".5"/>'
I[973]=svg(b,d)

# 764 空も飛べるはず: a paper airplane soaring high above a school rooftop fence into a clear blue sky
d,b=bg([(0,'#2a7ae8'),(.7,'#8ac8f8'),(1,'#e0f2ff')])
b+=cloud(160,560,1.0,'#fff',.8)+cloud(640,520,.8,'#fff',.7)
b+='<path d="M0 700 L800 700" stroke="#3a4a5a" stroke-width="6"/>'+''.join(f'<path d="M{x} 640 L{x} 800" stroke="#3a4a5a" stroke-width="4"/>' for x in range(0,800,30))+'<path d="M0 640 L800 640" stroke="#3a4a5a" stroke-width="6"/><rect y="740" width="800" height="60" fill="#8a8a8a"/>'
b+='<g transform="translate(470 260) rotate(-20)"><path d="M-170 40 L170 0 L-110 -60Z" fill="#fff"/><path d="M-110 -60 L170 0 L-60 0Z" fill="#dce8f8"/><path d="M-170 40 L170 0 L-60 10Z" fill="#c8d8ec"/></g>'
b+='<path d="M290 330 Q200 380 120 360" stroke="#fff" stroke-width="4" stroke-dasharray="10 12" fill="none" opacity=".7"/>'
I[764]=svg(b,d)

# 1420 オールドファッション: an old-fashioned doughnut beside a steaming cup of coffee on a café table
d,b=bg([(0,'#f2e4cc'),(1,'#c8a07a')])
b+='<rect y="520" width="800" height="280" fill="#7a4a2a"/><rect y="520" width="800" height="16" fill="#5a341a"/>'
b+='<ellipse cx="300" cy="560" rx="200" ry="44" fill="#f8f4ec"/>'
b+='<path d="M140 520 Q150 380 300 370 Q450 380 460 520 Q300 560 140 520Z" fill="#d8984a"/><ellipse cx="300" cy="470" rx="160" ry="70" fill="#e8b060"/><ellipse cx="300" cy="470" rx="54" ry="24" fill="#a8683a"/>'
for k in range(8): b+=f'<path d="M{170+k*34} {430+abs(k-3.5)*8:.0f} q14 -16 28 0" stroke="#c87a3a" stroke-width="5" fill="none"/>'
b+='<rect x="520" y="400" width="160" height="150" rx="14" fill="#fff"/><path d="M680 430 Q740 440 730 490 Q720 530 680 520" stroke="#fff" stroke-width="18" fill="none"/><ellipse cx="600" cy="404" rx="76" ry="14" fill="#4a2410"/>'
for k in range(3): b+=f'<path d="M{570+k*30} 380 q-16 -30 0 -60 q16 -30 0 -60" stroke="#fff" stroke-width="6" fill="none" opacity=".5"/>'
I[1420]=svg(b,d)

# 580 lulu.: a meadow of small blue flowers opening under a starry night sky, a lone traveller's staff planted among them
d,b=bg([(0,'#0a1438'),(.7,'#2a3a7a'),(1,'#5a6aa8')])
b+=starsf(110,1580,520,'#e8f0ff')+moon(620,150,40,'#f4f8ff')
b+='<path d="M-10 520 Q400 470 810 520 L810 810 L-10 810Z" fill="#1a2a4a"/>'
r=R(1580)
for _ in range(120):
    y=r.uniform(520,800);x=r.uniform(-20,820);s=(y-480)/12
    b+=flower(x,y,s,5,r.choice(['#8ac8ff','#b8e0ff','#ffffff']),'#ffe680',r.uniform(0,70),.6)
b+='<rect x="396" y="300" width="10" height="400" rx="4" fill="#c8a878" transform="rotate(6 400 700)"/><circle cx="380" cy="300" r="20" fill="#ff5a6a"/>'+glow(380,300,40,'#ff8a9a',.5,'glow2')
I[1580]=svg(b,d)

# 1721 初心LOVE: a pink envelope sealed with a heart, little hearts fluttering out of it like a first crush
d,b=bg([(0,'#ffe8f2'),(1,'#ffc8de')])
b+=glow(400,450,230,'#ffffff',.6)
b+='<g transform="rotate(-8 400 480)"><rect x="180" y="360" width="440" height="280" rx="16" fill="#ff9ac0"/><path d="M180 376 L400 520 L620 376" fill="#ffb8d4" stroke="#ff7aa8" stroke-width="6"/>'+heart(400,520,42,'#e8205a')+'</g>'
for x,y,s,c in [(330,280,30,'#ff5a8a'),(450,230,40,'#ff7aa8'),(560,300,24,'#ff5a8a'),(400,140,22,'#ffa0c0'),(240,200,18,'#ffa0c0')]: b+=heart(x,y,s,c)
I[1721]=svg(b,d)

# 974 光: a single shaft of light breaking through dark clouds onto a calm sea
d,b=bg([(0,'#1a2a3a'),(.6,'#4a6a8a'),(1,'#1a3a5a')])
b+='<polygon points="360,150 440,150 640,620 160,620" fill="#fff6d8" opacity=".3"/><polygon points="380,150 420,150 520,620 280,620" fill="#fffbe8" opacity=".4"/>'
for x,y,s in [(170,170,1.6),(620,150,1.8),(400,90,1.3)]: b+=cloud(x,y,s,'#2a3a4a',.95)
b+='<rect y="600" width="800" height="200" fill="#1a3a5a"/><ellipse cx="400" cy="620" rx="260" ry="20" fill="#fff6d8" opacity=".55"/>'
for k in range(6): b+=f'<rect x="{330-k*20}" y="{640+k*24}" width="{140+k*40}" height="5" rx="2" fill="#fff6d8" opacity="{.6-k*.08:.2f}"/>'
I[974]=svg(b,d)

# 1076 サウダージ: a lonely seaside at dusk in the rain, an acoustic guitar leaning against a weathered post
d,b=bg([(0,'#3a3a5a'),(.6,'#8a5a6a'),(1,'#2a3a4a')])
b+='<rect y="460" width="800" height="340" fill="#2a3a5a"/><rect y="460" width="800" height="6" fill="#c8a0a0" opacity=".5"/>'
b+='<path d="M-10 640 Q300 600 810 650 L810 810 L-10 810Z" fill="#a8907a"/>'
b+='<rect x="520" y="380" width="30" height="320" fill="#4a3a2a"/>'
b+='<g transform="rotate(-14 460 600)"><ellipse cx="460" cy="640" rx="80" ry="90" fill="#c87a3a"/><ellipse cx="460" cy="540" rx="60" ry="66" fill="#c87a3a"/><circle cx="460" cy="580" r="24" fill="#2a1a0a"/><rect x="450" y="260" width="20" height="260" fill="#5a3a1a"/><rect x="444" y="230" width="32" height="50" rx="6" fill="#3a2414"/></g>'
b+=rain(90,1076,'#d8e0f0',.4,12)
I[1076]=svg(b,d)

# 1438 炎: a steam locomotive thundering through the night, wreathed in roaring flames and sparks
d,b=bg([(0,'#0a0404'),(1,'#3a0a04')])
b+=glow(400,480,280,'#ff5a1a',.45)
r=R(1438)
for k in range(10):
    x=60+k*76;h=r.uniform(200,360)
    b+=f'<path d="M{x-60} 800 Q{x-40} {800-h*.5:.0f} {x} {800-h:.0f} Q{x+40} {800-h*.5:.0f} {x+60} 800Z" fill="{r.choice(["#ff6a1a","#ffaa2a","#e8301a"])}" opacity=".8"/>'
b+='<g fill="#08080a"><rect x="160" y="420" width="420" height="160" rx="20"/><rect x="480" y="320" width="150" height="260" rx="10"/><rect x="230" y="340" width="50" height="90"/><path d="M110 580 L160 500 L160 580Z"/></g>'
for x in (220,330,440,560): b+=f'<circle cx="{x}" cy="600" r="46" fill="#1a1a1e"/><circle cx="{x}" cy="600" r="16" fill="#e8301a"/>'
b+='<rect x="500" y="350" width="60" height="50" fill="#ffd27a"/>'
for _ in range(30): b+=f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(80,420):.0f}" r="{r.choice([2,3,4])}" fill="#ffd27a"/>'
b+='<path d="M255 340 Q240 260 300 220 Q360 180 340 100" stroke="#5a5a64" stroke-width="40" fill="none" opacity=".6" stroke-linecap="round"/>'
I[1438]=svg(b,d)

# 1397 RPG: a party of four tiny adventurers walking a winding path toward a castle on a hill, a treasure chest on the way
d,b=bg([(0,'#5ab0f8'),(1,'#c8ecff')])
b+=cloud(600,160,.9)+hills(420,40,'#6ac86a',1397)+hills(500,40,'#4aa84a',97)
b+='<g fill="#8a8aa8"><rect x="540" y="200" width="140" height="200"/><rect x="520" y="160" width="40" height="240"/><rect x="660" y="160" width="40" height="240"/><path d="M520 160 L540 110 L560 160Z M660 160 L680 110 L700 160Z"/></g><path d="M540 110 L540 80 L570 92 L540 102" fill="#e8302a"/><rect x="590" y="320" width="40" height="80" rx="20" fill="#3a3a4a"/>'
b+='<path d="M80 800 Q200 640 420 600 Q560 560 600 420" stroke="#e8d0a0" stroke-width="44" fill="none"/>'
for x,y,c in [(260,668,'#e8302a'),(300,656,'#2a6ae8'),(340,644,'#e8b02a'),(380,632,'#8a3ae8')]: b+=figure(x,y,100,c)
b+='<rect x="120" y="640" width="90" height="60" rx="8" fill="#a8582a"/><path d="M120 650 Q165 610 210 650Z" fill="#c8783a"/><rect x="156" y="650" width="18" height="20" fill="#ffd82a"/>'
I[1397]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
