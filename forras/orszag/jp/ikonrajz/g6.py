import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 6. csoport, 2026-10-24
I={}

# 382 十戒 (1984): two stone tablets of law cracking apart under a red lightning bolt, defiant and dramatic
d,b=bg([(0,'#1a0408'),(1,'#4a0a10')])
b+=bolt([(420,0),(380,160),(440,220),(390,420)],'#ff4a4a',14,.95)+glow(400,260,120,'#ff2a2a',.45)
for x,a in [(270,-8),(530,8)]:
    b+=f'<g transform="rotate({a} {x} 500)"><path d="M{x-110} 700 L{x-110} 380 Q{x-110} 290 {x} 290 Q{x+110} 290 {x+110} 380 L{x+110} 700Z" fill="#8a8a8a"/>'+''.join(f'<rect x="{x-80}" y="{400+k*50}" width="{160-(k%2)*40}" height="12" rx="6" fill="#5a5a5a"/>' for k in range(5))+'</g>'
b+=bolt([(270,320),(250,420),(290,500),(260,620)],'#2a2a2a',6,1)
I[382]=svg(b,d)

# 933 雨のMelody: raindrops running down a window pane, gathering into the shapes of musical notes
d,b=bg([(0,'#3a4a6a'),(1,'#6a7a9a')])
b+=skyline(700,'#2a3448',933,80,300,'#ffd27a',40)
b+='<rect x="60" y="60" width="680" height="680" fill="#a8c0e0" opacity=".25"/>'+rain(60,933,'#ffffff',.5,0)
b+=note(240,330,60,'#e8f4ff',True)+note(520,460,54,'#e8f4ff')+note(380,600,40,'#e8f4ff')
for x,y in [(250,380),(530,510),(390,640)]: b+=f'<path d="M{x} {y} Q{x+6} {y+60} {x} {y+120}" stroke="#e8f4ff" stroke-width="6" fill="none" opacity=".6"/>'
b+='<rect x="60" y="60" width="680" height="680" fill="none" stroke="#e8e0d8" stroke-width="24"/><path d="M400 60 L400 740" stroke="#e8e0d8" stroke-width="14"/>'
I[933]=svg(b,d)

# 282 涙の海で抱かれたい: a couple embracing on a summer beach before a great wave shaped like a falling tear
d,b=bg([(0,'#ff8a5a'),(.5,'#ffc890'),(1,'#3ab0d8')])
b+=hinomaru_sun(600,280,80,'#fff2c8',.9)
b+='<path d="M120 640 Q100 360 300 200 Q260 360 420 460 Q560 560 500 640Z" fill="#1a8ac8"/><path d="M300 200 Q260 360 420 460 Q330 420 300 200Z" fill="#e8f8ff"/>'
b+='<rect y="600" width="800" height="200" fill="#0a8ac8"/><path d="M-10 680 Q400 640 810 700 L810 810 L-10 810Z" fill="#ffe0b0"/>'
b+=figure(560,720,200,'#1a1020')+figure(600,720,186,'#1a1020',hair='#1a1020',pose='hold')
I[282]=svg(b,d)

# 498 OH MY LITTLE GIRL: two young silhouettes on a winter street at night, their breath meeting in a small cloud heart
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a5a')])
b+=snow(70,498)+skyline(620,'#0a1428',498,80,260,'#ffd27a',50)
b+='<rect y="620" width="800" height="180" fill="#d8e0ec"/>'
b+=figure(340,740,280,'#06080e')+figure(450,740,240,'#06080e',hair='#06080e')
b+='<path d="M392 470 Q400 440 410 470" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>'+heart(400,420,30,'#fff')
b+='<path d="M310 540 Q340 560 370 540" stroke="#e8302a" stroke-width="16" fill="none"/>'
I[498]=svg(b,d)

# 522 決戦は金曜日: a wall calendar with Friday circled in lipstick red, high heels ready for the big night
d,b=bg([(0,'#ffe0ec'),(1,'#ffb8d0')])
b+='<rect x="160" y="120" width="480" height="440" rx="16" fill="#fff"/><rect x="160" y="120" width="480" height="90" rx="16" fill="#3a2a5a"/>'
for i in range(7):
    for j in range(4): b+=f'<rect x="{180+i*64}" y="{230+j*80}" width="56" height="70" rx="6" fill="#f4eef4"/>'
b+='<text x="400" y="182" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" font-size="44" fill="#fff">FRIDAY</text>'
b+='<ellipse cx="533" cy="345" rx="50" ry="46" fill="none" stroke="#e8102a" stroke-width="10"/>'+heart(533,345,18,'#e8102a')
b+=f'<g transform="translate(560 640) rotate(-20)"><rect x="-14" y="-60" width="28" height="80" rx="6" fill="#d8b050"/><path d="M-10 -60 L-10 -100 Q0 -120 10 -100 L10 -60Z" fill="#e8102a"/></g>'
I[522]=svg(b,d)

# 797 FACE: a face in profile made of mirror shards, each piece reflecting a different colour of the night
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=glow(400,420,240,'#5a8aff',.3)+profile(420,720,2.3,'#c8d8ff')
r=R(797)
for k in range(22):
    x,y=r.uniform(280,600),r.uniform(160,700);s=r.uniform(30,70)
    b+=f'<polygon points="{x:.0f},{y:.0f} {x+s:.0f},{y+r.uniform(-20,20):.0f} {x+r.uniform(0,s):.0f},{y+s:.0f}" fill="{r.choice(["#ff5ab8","#5ae8ff","#ffe05a","#8a7aff","#ffffff"])}" opacity=".35"/>'
b+=bolt([(300,250),(400,330),(360,450),(470,540)],'#fff',3,.8)
I[797]=svg(b,d)

# 798 Can't Stop Fallin' in Love: a figure tumbling headlong through a pink sky full of floating hearts
d,b=bg([(0,'#ff8ac8'),(1,'#ffd0e8')])
r=R(798)
for _ in range(18): x,y,s=r.uniform(40,760),r.uniform(40,760),r.uniform(12,40);b+=heart(x,y,s,r.choice(['#ff3a7a','#ff7aa8','#ffffff']))
b+=f'<g transform="rotate(150 400 420)">{figure(400,560,300,"#3a0a2a",pose="up",hair="#3a0a2a")}</g>'
for k in range(4): b+=f'<path d="M{330+k*40} 160 l0 -100" stroke="#fff" stroke-width="5" opacity=".6"/>'
I[798]=svg(b,d)

# 1199 ワイルド アット ハート: a roaring lion's head silhouette with a wild mane, a red heart glowing at its core
d,b=bg([(0,'#ff8a1a'),(1,'#a8301a')])
b+=rays(400,420,20,'#ffe05a',.25,8)
r=R(1199)
for k in range(24):
    a=k*15;L=r.uniform(230,290)
    b+=f'<path d="M400 420 L{400+L*math.cos(math.radians(a-6)):.0f} {420+L*math.sin(math.radians(a-6)):.0f} L{400+L*1.05*math.cos(math.radians(a)):.0f} {420+L*1.05*math.sin(math.radians(a)):.0f} L{400+L*math.cos(math.radians(a+6)):.0f} {420+L*math.sin(math.radians(a+6)):.0f}Z" fill="#3a1408"/>'
b+='<circle cx="400" cy="420" r="170" fill="#5a2410"/><circle cx="340" cy="380" r="16" fill="#ffd82a"/><circle cx="460" cy="380" r="16" fill="#ffd82a"/><path d="M370 470 L400 500 L430 470Z" fill="#1a0804"/>'
b+=heart(400,560,40,'#e8102a')
I[1199]=svg(b,d)

# 1296 恋するフォーチュンクッキー: a fortune cookie cracked open, a slip of paper with a pink heart poking out
d,b=bg([(0,'#ffe8b8'),(1,'#ffc878')])
b+=confetti(30,1296,['#ff5aa8','#ffffff','#ffd82a'])
b+='<path d="M180 480 Q200 300 360 300 Q420 380 380 520 Q280 560 180 480Z" fill="#e8a040"/><path d="M620 480 Q600 300 440 300 Q380 380 420 520 Q520 560 620 480Z" fill="#d89030"/>'
b+='<path d="M200 470 Q220 340 350 330" stroke="#ffc870" stroke-width="12" fill="none" opacity=".7"/>'
b+='<g transform="rotate(-20 400 380)"><rect x="300" y="340" width="260" height="80" rx="6" fill="#fff"/>'+heart(500,382,22,'#ff3a7a')+'<rect x="320" y="370" width="130" height="10" rx="5" fill="#d8c8d0"/></g>'
I[1296]=svg(b,d)

# 980 Wait & See -Risk-: a pair of dice tumbling mid-roll above a green felt table, the outcome still unknown
d,b=bg([(0,'#0a2a1a'),(1,'#1a4a2a')])
b+=glow(400,400,220,'#ffffff',.2)
def die(x,y,a,n,s=1):
    pips={1:[(0,0)],2:[(-1,-1),(1,1)],3:[(-1,-1),(0,0),(1,1)],4:[(-1,-1),(1,-1),(-1,1),(1,1)],5:[(-1,-1),(1,-1),(0,0),(-1,1),(1,1)],6:[(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1)]}[n]
    return f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><rect x="-90" y="-90" width="180" height="180" rx="30" fill="#fbfbf6"/>'+''.join(f'<circle cx="{px*48}" cy="{py*48}" r="16" fill="{"#e8102a" if n==1 else "#1a1a1a"}"/>' for px,py in pips)+'</g>'
b+=die(290,360,-20,5)+die(520,470,24,3,.85)
b+='<ellipse cx="400" cy="680" rx="260" ry="30" fill="#000" opacity=".25"/>'
I[980]=svg(b,d)

# 1164 SUMMER SONG: an acoustic guitar leaning against a sunflower field under a hot summer sky
d,b=bg([(0,'#2aa8f8'),(1,'#bfe8ff')])
b+=glow(640,140,100,'#fff6c8',.8)+'<circle cx="640" cy="140" r="50" fill="#fff8d8"/>'
b+='<path d="M-10 520 Q400 480 810 520 L810 810 L-10 810Z" fill="#6ab84a"/>'
r=R(1164)
for _ in range(16): x=r.uniform(40,760);y=r.uniform(440,560);b+=f'<path d="M{x:.0f} {y+20:.0f} L{x:.0f} 800" stroke="#4a8a3a" stroke-width="8"/>'+flower(x,y,70,14,'#ffc81a','#6a3a10',x%30,.4)
b+='<g transform="rotate(-14 400 620)"><ellipse cx="400" cy="660" rx="110" ry="120" fill="#c8783a"/><ellipse cx="400" cy="520" rx="84" ry="90" fill="#c8783a"/><circle cx="400" cy="580" r="34" fill="#3a1a0a"/><rect x="386" y="160" width="28" height="360" fill="#6a3a1a"/><rect x="378" y="120" width="44" height="64" rx="8" fill="#3a2414"/></g>'
I[1164]=svg(b,d)

# 1407 前前前世: a comet splitting in two across a twilight sky above a mountain lake
d,b=bg([(0,'#1a1a5a'),(.55,'#c86a9a'),(1,'#ffb08a')])
b+=starsf(60,1407,360,'#fff')
b+='<path d="M120 60 L460 330" stroke="#bff0ff" stroke-width="16" stroke-linecap="round" opacity=".8"/><path d="M120 60 L460 330" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
b+='<path d="M460 330 L640 420 M460 330 L560 470" stroke="#ffd0f0" stroke-width="8" stroke-linecap="round"/>'+glow(460,330,50,'#fff',.8,'glow2')
b+='<path d="M-10 560 L120 460 L260 540 L400 480 L560 560 L700 470 L810 520 L810 600 L-10 600Z" fill="#2a2a5a"/>'
b+='<ellipse cx="400" cy="660" rx="380" ry="90" fill="#5a5a9a"/><path d="M200 660 L600 660" stroke="#ffd0f0" stroke-width="4" opacity=".6"/>'
I[1407]=svg(b,d)

# 1675 Love Is Over: an empty wine glass and a tipped-over bottle on a bar counter at closing time, one lamp still on
d,b=bg([(0,'#1a1414'),(1,'#2a1e1a')])
b+=glow(400,200,200,'#ffd8a0',.3)+'<path d="M380 0 L380 120 M340 120 L420 120 L410 150 L350 150Z" stroke="#3a2a1a" stroke-width="5" fill="#3a2a1a"/>'
b+='<rect y="520" width="800" height="280" fill="#3a1e14"/><rect y="520" width="800" height="14" fill="#5a3020"/>'
b+='<g transform="rotate(80 520 500)"><rect x="480" y="300" width="80" height="220" rx="20" fill="#2a4a2a" opacity=".9"/><rect x="500" y="250" width="40" height="70" rx="8" fill="#2a4a2a"/></g>'
b+='<path d="M560 520 Q620 540 700 530" stroke="#7a0a1a" stroke-width="10" fill="none"/>'
b+='<path d="M260 300 L380 300 Q390 400 320 430 Q250 400 260 300Z" fill="#f4e8f0" opacity=".35"/><rect x="314" y="430" width="12" height="80" fill="#f4e8f0" opacity=".5"/><ellipse cx="320" cy="512" rx="50" ry="10" fill="#f4e8f0" opacity=".5"/>'
I[1675]=svg(b,d)

# 321 クリスマス・イブ: a snowy station platform at night, a lone figure waiting beside a twinkling tree as rain turns to snow
d,b=bg([(0,'#0a1020'),(1,'#1a2438')])
b+=snow(110,321)+rain(30,321,'#a8c0e0',.3,4,300)
b+='<path d="M0 220 L800 180 L800 230 L0 270Z" fill="#141c2c"/>'+''.join(f'<rect x="{x}" y="{210-x*.05:.0f}" width="12" height="{400}" fill="#141c2c"/>' for x in (120,420,720))
b+='<rect y="600" width="800" height="200" fill="#2a3040"/><rect y="600" width="800" height="16" fill="#ffd82a"/>'
for k in range(4):
    w=40+k*30;y=330+k*70;b+=f'<path d="M{620-w} {y+80} L620 {y-20} L{620+w} {y+80}Z" fill="#1a4a3a"/>'
r=R(21)
for _ in range(20): t=r.random();b+=f'<circle cx="{620+r.uniform(-t*130,t*130):.0f}" cy="{320+t*260:.0f}" r="6" fill="{r.choice(["#ffe05a","#ff5a5a","#fff"])}"/>'
b+=figure(300,720,260,'#06080e')+glow(300,620,150,'#ffd27a',.12)
I[321]=svg(b,d)

# 633 裸足の女神: a trail of bare footprints across wet sand leading toward the sea at sunrise
d,b=bg([(0,'#ffb88a'),(.5,'#ffe0b0'),(1,'#5ab0d8')])
b+=hinomaru_sun(400,330,90,'#fff6d8',.9)+'<rect y="360" width="800" height="140" fill="#3a90c8"/><path d="M-10 500 Q400 470 810 500 L810 810 L-10 810Z" fill="#e8c890"/>'
for k in range(7):
    x=400+(1 if k%2 else -1)*26+math.sin(k*.6)*30;y=760-k*40;s=1-k*.09
    b+=f'<g transform="translate({x:.0f} {y:.0f}) scale({s:.2f})"><ellipse cx="0" cy="0" rx="16" ry="30" fill="#b8905a"/>'+''.join(f'<circle cx="{-12+j*6}" cy="{-36+abs(j-2)*2}" r="5" fill="#b8905a"/>' for j in range(5))+'</g>'
I[633]=svg(b,d)

# 1200 迷宮ラブソング: a maze seen from above with a glowing heart waiting at its centre
d,b=bg([(0,'#2a1a4a'),(1,'#4a2a6a')])
for k in range(6):
    r_=60+k*50;gap=(k*67)%360
    b+=f'<circle cx="400" cy="400" r="{r_}" fill="none" stroke="#c8b0ff" stroke-width="14" stroke-dasharray="{2*math.pi*r_-60:.0f} 60" transform="rotate({gap} 400 400)"/>'
for a in (30,110,200,290): b+=f'<path d="M{400+110*math.cos(math.radians(a)):.0f} {400+110*math.sin(math.radians(a)):.0f} L{400+160*math.cos(math.radians(a)):.0f} {400+160*math.sin(math.radians(a)):.0f}" stroke="#c8b0ff" stroke-width="14"/>'
b+=glow(400,400,60,'#ff5a9a',.8)+heart(400,400,34,'#ff3a7a')
I[1200]=svg(b,d)

# 614 YAH YAH YAH: a red boxing glove smashing forward through a comic burst, sweat flying
d,b=bg([(0,'#ffd82a'),(1,'#ff8a1a')])
pts=' '.join(f'{400+(320 if k%2==0 else 200)*math.cos(math.radians(k*15)):.0f},{420+(320 if k%2==0 else 200)*math.sin(math.radians(k*15)):.0f}' for k in range(24))
b+=f'<polygon points="{pts}" fill="#fff"/>'
b+='<g transform="rotate(-20 400 420)"><path d="M230 330 Q250 240 380 250 Q520 260 540 380 Q550 500 420 530 Q300 540 250 480Z" fill="#e8102a"/><path d="M250 470 L180 520 L170 600 L270 600 L300 520Z" fill="#fff"/><path d="M300 300 Q340 270 400 280" stroke="#ff7a7a" stroke-width="16" fill="none" opacity=".7"/></g>'
for x,y in [(620,200),(660,300),(150,250)]: b+=f'<ellipse cx="{x}" cy="{y}" rx="12" ry="18" fill="#5ab0ff"/>'
I[614]=svg(b,d)

# 634 ZERO: a giant glowing zero hanging in deep space, a hard-rock lightning streak cutting through it
d,b=bg([(0,'#04040e'),(1,'#141428')])
b+=starsf(80,634,800,'#e8e8ff')+glow(400,400,240,'#3a8aff',.35)
b+='<ellipse cx="400" cy="400" rx="170" ry="250" fill="none" stroke="#5ab0ff" stroke-width="56"/><ellipse cx="400" cy="400" rx="170" ry="250" fill="none" stroke="#e8f4ff" stroke-width="12"/>'
b+=bolt([(220,140),(380,360),(320,420),(560,680)],'#ffe05a',12,.95)
I[634]=svg(b,d)

# 934 ジェットコースター・ロマンス: a roller coaster loop over a sparkling summer sea, a car racing around the top
d,b=bg([(0,'#1ab8f0'),(1,'#a8e8ff')])
b+='<rect y="520" width="800" height="280" fill="#0a98d8"/>'+''.join(f'<rect x="{r_}" y="{560+k*40}" width="40" height="4" fill="#fff" opacity=".5"/>' for k,r_ in enumerate([120,520,300,640]))
b+='<path d="M-10 600 Q200 600 300 480 Q360 380 400 250 A120 120 0 1 1 520 380 Q560 500 810 520" stroke="#e8302a" stroke-width="18" fill="none"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="10" height="{800-y}" fill="#fff"/>' for x,y in [(120,590),(260,520),(560,470),(700,510)])
b+='<g transform="translate(380 230) rotate(-60)"><rect x="-40" y="-20" width="80" height="40" rx="10" fill="#ffd82a"/><circle cx="-20" cy="-26" r="10" fill="#1a1a2a"/><circle cx="14" cy="-26" r="10" fill="#1a1a2a"/></g>'
I[934]=svg(b,d)

# 992 SURREAL: a door standing alone in a desert, opening onto a sky full of clouds and a floating moon
d,b=bg([(0,'#ff9a6a'),(.6,'#ffd8a0'),(1,'#d8a060')])
b+='<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#d89a5a"/>'
b+='<rect x="300" y="220" width="200" height="360" fill="#5ab0f8"/>'+cloud(380,330,.6)+cloud(440,470,.5)+'<circle cx="460" cy="270" r="22" fill="#fff6d8"/>'
b+='<path d="M500 220 L590 260 L590 610 L500 580Z" fill="#8a3a2a"/><circle cx="572" cy="430" r="8" fill="#d8b040"/><rect x="290" y="210" width="220" height="380" fill="none" stroke="#3a1a10" stroke-width="12"/>'
b+='<path d="M300 580 L120 760 L520 760 L500 580Z" fill="#000" opacity=".15"/>'
I[992]=svg(b,d)

# 1471 さよーならまたいつか！: a hand waving goodbye from an old train window as cherry petals blow past
d,b=bg([(0,'#ffd8e4'),(1,'#ffb0c8')])
b+='<rect y="300" width="800" height="360" fill="#c8302a"/><rect y="320" width="800" height="12" fill="#f4e8d8"/>'
for x in (60,330,600): b+=f'<rect x="{x}" y="360" width="200" height="200" rx="12" fill="#bfe0f8"/>'
b+='<rect y="660" width="800" height="140" fill="#3a3a44"/><path d="M0 700 L800 700" stroke="#8a8a94" stroke-width="8"/>'
b+='<g fill="#e8b890"><rect x="410" y="340" width="40" height="160" rx="18" transform="rotate(-20 430 500)"/>'+''.join(f'<rect x="{392+k*16}" y="{270+abs(k-1.5)*8:.0f}" width="14" height="70" rx="7" transform="rotate(-20 430 500)"/>' for k in range(4))+'</g>'
b+=petals(50,1471,'#fff0f6',0,800,8,14,.9)
I[1471]=svg(b,d)

# 383 飾りじゃないのよ涙は: a single tear hanging like a diamond earring in the dark, catching one cold glint
d,b=bg([(0,'#0a0a0e'),(1,'#1a1a24')])
b+=glow(400,480,160,'#bfe8ff',.3)
b+='<path d="M400 200 Q420 260 400 300" stroke="#c8c8d0" stroke-width="6" fill="none"/><circle cx="400" cy="300" r="12" fill="#e8e8f0"/>'
d+=lg('tr',S((0,'#ffffff'),(.5,'#bfe8ff'),(1,'#5a9ad8')))
b+='<path d="M400 330 Q470 450 470 510 Q470 590 400 590 Q330 590 330 510 Q330 450 400 330Z" fill="url(#tr)"/><path d="M370 460 Q360 500 372 540" stroke="#fff" stroke-width="10" fill="none" opacity=".7"/>'
b+=sparkle(440,420,26,'#fff')
I[383]=svg(b,d)

# 731 Tomorrow Never Knows: a lone runner on an endless bridge racing toward a sunrise that has not yet broken
d,b=bg([(0,'#1a2a5a'),(.6,'#8a6a9a'),(1,'#ffb08a')])
b+=glow(400,560,240,'#ffd8a0',.6)
b+='<path d="M-10 800 L380 560 L420 560 L810 800Z" fill="#2a2a3a"/><path d="M-10 760 L380 556 M810 760 L420 556" stroke="#4a4a5a" stroke-width="10"/>'
for k in range(8): b+=f'<rect x="{390-k*30}" y="{560+k*8}" width="6" height="{20+k*14}" fill="#4a4a5a"/><rect x="{404+k*30}" y="{560+k*8}" width="6" height="{20+k*14}" fill="#4a4a5a"/>'
b+=figure(400,720,240,'#0a0a14',pose='reach')
I[731]=svg(b,d)

# 1159 YELL: a choir of students in silhouette singing on a school stage, cherry petals and a big cheering banner above
d,b=bg([(0,'#ff9aa8'),(1,'#ffe8c8')])
b+=rays(400,360,18,'#ffffff',.3,8)
b+='<path d="M120 160 Q400 220 680 160 L680 260 Q400 320 120 260Z" fill="#e8302a"/>'+''.join(f'<rect x="{200+k*80}" y="{205+abs(k-2)*-6+ (k-2)**2*4}" width="40" height="16" rx="8" fill="#fff"/>' for k in range(5))
for row,(y,n,h) in enumerate([(760,7,200),(680,6,170)]):
    for k in range(n): b+=figure(100+k*(600/(n-1)) if n>1 else 400,y,h,'#2a1a2a' if row==0 else '#3a2a3a')
b+=petals(30,1159,'#fff0f6',300,640,7,12,.9)
I[1159]=svg(b,d)

# 1170 三日月: a thin crescent moon over a quiet night sea, its reflection trembling on the water
d,b=bg([(0,'#04081e'),(1,'#121a3a')])
b+=starsf(70,1170,520,'#e8f0ff')
b+=glow(430,230,100,'#fff6d8',.4)+'<path d="M400 140 A100 100 0 1 0 500 300 A80 80 0 1 1 400 140Z" fill="#fff6d8"/>'
b+='<rect y="520" width="800" height="280" fill="#08102a"/>'+''.join(f'<path d="M{420-k*6} {550+k*34} q30 -10 60 0" stroke="#fff6d8" stroke-width="5" fill="none" opacity="{.7-k*.1:.1f}"/>' for k in range(7))
I[1170]=svg(b,d)

# 1201 カイト: a kite flying high in a wide blue sky, its long tail dancing, the string running down to a small figure
d,b=bg([(0,'#3a9af0'),(1,'#d8f0ff')])
b+=cloud(160,560,1.1)+cloud(620,620,.9)
b+='<path d="M200 760 Q300 500 460 260" stroke="#fff" stroke-width="3" fill="none"/>'
b+='<path d="M460 140 L560 250 L460 370 L360 250Z" fill="#e8302a"/><path d="M460 140 L460 370 M360 250 L560 250" stroke="#ffd82a" stroke-width="6"/>'
b+='<path d="M460 370 Q430 430 470 480 Q510 530 470 590" stroke="#ffd82a" stroke-width="4" fill="none"/>'+''.join(f'<path d="M{x-14} {y} L{x} {y-10} L{x+14} {y} L{x} {y+10}Z" fill="{c}"/>' for x,y,c in [(450,420,'#3ac84a'),(482,500,'#ff5aa8'),(472,575,'#3a8aff')])
b+='<rect y="760" width="800" height="40" fill="#6ab84a"/>'+figure(200,780,130,'#1a2a3a',pose='wave')
I[1201]=svg(b,d)

# 1297 フライングゲット: a hand leaping up to snatch a falling golden star out of the air before anyone else
d,b=bg([(0,'#ff3a6a'),(1,'#ff9a3a')])
b+=rays(400,260,22,'#ffffff',.25,6)+star5(450,230,110,'#ffe05a',-12)+glow(450,230,100,'#fff6c8',.5)
b+='<path d="M300 800 L330 500 L420 500 L430 800Z" fill="#e8b890"/><rect x="310" y="380" width="140" height="150" rx="40" fill="#e8b890"/>'+''.join(f'<rect x="{316+k*34}" y="{300-abs(k-1.5)*10:.0f}" width="26" height="110" rx="13" fill="#e8b890"/>' for k in range(4))
for k in range(3): b+=f'<path d="M{250-k*20} {500+k*40} l-80 30" stroke="#fff" stroke-width="6" opacity=".6" stroke-linecap="round"/>'
I[1297]=svg(b,d)

# 1843 春を告げる: a single cherry blossom floating through a neon-lit city street at night, telling of spring
d,b=bg([(0,'#0a0a24'),(1,'#2a0a3a')])
b+=skyline(800,'#14102a',1843,200,600,'#ff7ad8',140)
b+=neon(200,260,'春','#ff6ad0',110)+neon(620,360,'夜','#5ae8ff',90)
b+=glow(420,460,90,'#ffd0e4',.5)+sakura(420,460,140,'#ffc0d8','#ff6aa0',10)+petals(16,1843,'#ffc0d8',300,800,6,12,.8)
I[1843]=svg(b,d)

# 440 悲しみにさよなら: a white handkerchief fluttering goodbye from a harbour pier as a ship sails into the sunset
d,b=bg([(0,'#5a3a7a'),(.6,'#ff9a6a'),(1,'#ffd0a0')])
b+=hinomaru_sun(560,440,80,'#fff2c8',.9)+'<rect y="470" width="800" height="330" fill="#3a3a6a"/>'
b+='<path d="M500 470 L640 470 L620 490 L520 490Z" fill="#1a1020"/><path d="M560 470 L560 420 L600 460Z" fill="#fff"/>'
b+='<path d="M-10 620 L400 600 L400 640 L-10 660Z" fill="#3a2a2a"/>'+''.join(f'<rect x="{x}" y="620" width="12" height="120" fill="#2a1a1a"/>' for x in (60,200,340))
b+=figure(220,610,170,'#140a14',pose='wave',hair='#140a14')+'<path d="M262 450 Q300 420 320 450 Q300 470 280 466 Q300 490 270 500Z" fill="#fff"/>'
I[440]=svg(b,d)

# 718 熱くなれ: an Olympic-style torch blazing high in a packed stadium at night
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a3a')])
b+='<path d="M-10 560 Q400 400 810 560 L810 810 L-10 810Z" fill="#1a1a34"/>'
r=R(718)
for _ in range(220): b+=f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(470,800):.0f}" r="2.5" fill="{r.choice(["#fff","#ffd27a","#5ae8ff"])}" opacity="{r.uniform(.3,.9):.2f}"/>'
b+=glow(400,280,170,'#ff8a1a',.6)
b+='<path d="M360 340 L440 340 L420 520 L380 520Z" fill="#d8b040"/><ellipse cx="400" cy="340" rx="56" ry="16" fill="#e8c860"/>'
b+='<path d="M400 120 Q470 220 440 300 Q420 340 400 340 Q380 340 360 300 Q330 220 400 120Z" fill="#ff6a1a"/><path d="M400 190 Q440 260 420 310 Q400 330 380 310 Q360 260 400 190Z" fill="#ffd04a"/>'
I[718]=svg(b,d)

# 769 渚: gentle waves rolling onto a quiet beach in the clear morning, a single seashell glinting in the foam
d,b=bg([(0,'#9ad8ff'),(1,'#e8f8ff')])
b+='<rect y="300" width="800" height="200" fill="#4ab0e0"/><path d="M-10 500 Q400 470 810 500 L810 810 L-10 810Z" fill="#f4dcb0"/>'
b+='<path d="M-10 470 Q100 520 200 480 T400 490 T600 480 T810 500 L810 540 Q600 520 400 540 T-10 530Z" fill="#fff" opacity=".85"/>'
b+='<g transform="translate(420 640)"><path d="M-70 30 Q-80 -60 0 -70 Q80 -60 70 30 Q0 50 -70 30Z" fill="#ffd8d0"/>'+''.join(f'<path d="M0 40 L{x} -60" stroke="#e8a8a0" stroke-width="5"/>' for x in (-50,-25,0,25,50))+'</g>'
I[769]=svg(b,d)

# 898 White Love: a snow globe holding a tiny couple under a lamp-post, snow swirling inside the glass
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=glow(400,380,220,'#bfe0ff',.35)
b+='<circle cx="400" cy="380" r="230" fill="#bfe0ff" opacity=".35"/><circle cx="400" cy="380" r="230" fill="none" stroke="#fff" stroke-width="6" opacity=".7"/>'
b+='<path d="M200 480 Q400 440 600 480 L560 560 L240 560Z" fill="#fff"/>'+figure(380,520,150,'#1a2a4a')+figure(420,520,140,'#1a2a4a',hair='#1a2a4a')
b+='<rect x="490" y="330" width="6" height="190" fill="#2a2a34"/><circle cx="493" cy="326" r="12" fill="#ffd27a"/>'+''.join(f'<circle cx="{400+r_*math.cos(k*2.4):.0f}" cy="{380+r_*math.sin(k*2.4):.0f}" r="4" fill="#fff" opacity=".9"/>' for k,r_ in enumerate(R(898).uniform(20,210) for _ in range(40)))
b+='<path d="M220 560 L580 560 L620 680 L180 680Z" fill="#8a3a2a"/><rect x="180" y="670" width="440" height="30" rx="6" fill="#6a2a1a"/>'
b+='<ellipse cx="320" cy="260" rx="40" ry="70" fill="#fff" opacity=".3" transform="rotate(30 320 260)"/>'
I[898]=svg(b,d)

# 1119 you: a heart-shaped pendant hanging on a fine chain, a single snowflake resting on it in the winter light
d,b=bg([(0,'#d8e4f4'),(1,'#a8bcd8')])
b+=glow(400,460,200,'#ffffff',.6)+snow(30,1119,.9)
b+='<path d="M200 0 Q400 380 600 0" stroke="#c8c8d0" stroke-width="5" fill="none"/>'
d+=lg('hp',S((0,'#ffe0f0'),(1,'#e8608a')))
b+=heart(400,460,110,'url(#hp)')+'<path d="M400 360 L400 330" stroke="#c8c8d0" stroke-width="6"/><circle cx="400" cy="324" r="10" fill="none" stroke="#c8c8d0" stroke-width="5"/>'
b+='<g transform="translate(450 440)" stroke="#fff" stroke-width="5" stroke-linecap="round">'+''.join(f'<path d="M0 0 L{30*math.cos(math.radians(a)):.0f} {30*math.sin(math.radians(a)):.0f}"/>' for a in range(0,360,60))+'</g>'
I[1119]=svg(b,d)

# 1429 R.Y.U.S.E.I.: a meteor shower raining down over a night city, a dancer mid-step on a rooftop below
d,b=bg([(0,'#04061e'),(1,'#1a1a4a')])
r=R(1429)
for _ in range(16):
    x,y=r.uniform(100,800),r.uniform(0,400);L=r.uniform(80,200)
    b+=f'<path d="M{x:.0f} {y:.0f} l{-L:.0f} {L*.6:.0f}" stroke="#fff" stroke-width="{r.choice([2,3,4])}" opacity=".8" stroke-linecap="round"/>'+f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#fff6d8"/>'
b+=skyline(640,'#0a0a24',1429,60,240,'#5ae8ff',60)+'<rect y="640" width="800" height="160" fill="#06061a"/>'
b+=figure(400,640,220,'#020210',pose='wave')
I[1429]=svg(b,d)

# 856 winter fall: snow falling past a tall gothic window, a single candle flickering on the sill inside
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<path d="M220 700 L220 300 Q220 120 400 100 Q580 120 580 300 L580 700Z" fill="#2a3a5a"/>'+snow(50,856,.9,700)
b+='<path d="M400 100 L400 700 M220 380 L580 380" stroke="#14141e" stroke-width="12"/><path d="M220 700 L220 300 Q220 120 400 100 Q580 120 580 300 L580 700" stroke="#3a3a4a" stroke-width="30" fill="none"/>'
b+='<rect y="700" width="800" height="100" fill="#2a2a34"/><rect x="380" y="610" width="40" height="100" rx="6" fill="#f4ece0"/><path d="M400 570 Q416 594 400 612 Q384 594 400 570Z" fill="#ffd060"/>'+glow(400,590,70,'#ffd060',.6)
I[856]=svg(b,d)

# 1091 さくら(独唱): one cherry tree alone on a gentle hill, petals drifting quietly in the soft spring air
d,b=bg([(0,'#e8f0f8'),(1,'#ffe8f0')])
b+='<path d="M-10 640 Q400 520 810 640 L810 810 L-10 810Z" fill="#a8d08a"/>'
b+='<path d="M400 600 Q390 480 400 400 M400 470 Q340 420 300 380 M400 450 Q460 400 500 370" stroke="#4a2a1a" stroke-width="22" fill="none"/>'
r=R(1091)
for _ in range(42): b+=f'<circle cx="{400+r.uniform(-200,200):.0f}" cy="{330+r.uniform(-120,90):.0f}" r="{r.uniform(30,54):.0f}" fill="{r.choice(["#ffc8dc","#ffd8e8","#ffb8d0"])}"/>'
b+=petals(26,1091,'#ffb8d0',350,800,7,12,.9)
I[1091]=svg(b,d)

# 1202 果てない空: an endless open sky of drifting clouds with a single bird soaring high toward the sun
d,b=bg([(0,'#1a7ae8'),(.7,'#8ac8f8'),(1,'#e0f4ff')])
b+=glow(600,200,140,'#fff6d8',.7)+'<circle cx="600" cy="200" r="50" fill="#fffbe8"/>'
for x,y,s in [(150,500,1.4),(450,620,1.8),(700,520,1.2),(300,360,.8)]: b+=cloud(x,y,s)
b+=bird(360,300,150,'#1a2a4a')
I[1202]=svg(b,d)

# 1472 海の幽霊: the glowing ghost of a giant whale swimming through a deep sea full of stars
d,b=bg([(0,'#020a2a'),(1,'#041a3a')])
b+=starsf(120,1472,800,'#bfe8ff')+glow(400,400,240,'#5ae0ff',.3)
b+='<path d="M120 420 Q200 260 420 280 Q600 300 660 380 L760 320 Q740 400 760 480 L660 430 Q600 520 420 520 Q220 530 120 420Z" fill="#7ad8ff" opacity=".55"/>'
b+='<path d="M140 440 Q300 500 520 480" stroke="#e8faff" stroke-width="4" fill="none" opacity=".7"/><circle cx="220" cy="380" r="10" fill="#fff"/>'
for k in range(5): b+=f'<path d="M{260+k*40} 470 L{270+k*40} 510" stroke="#e8faff" stroke-width="3" opacity=".6"/>'
I[1472]=svg(b,d)

# 1792 爆裂愛してる: a hot-pink heart exploding in a comic-book burst of stars and sparks
d,b=bg([(0,'#ffe05a'),(1,'#ff5aa8')])
pts=' '.join(f'{400+(340 if k%2==0 else 220)*math.cos(math.radians(k*12)):.0f},{420+(340 if k%2==0 else 220)*math.sin(math.radians(k*12)):.0f}' for k in range(30))
b+=f'<polygon points="{pts}" fill="#fff"/>'+heart(400,420,150,'#ff2a8a')+'<path d="M330 330 Q350 300 390 310" stroke="#fff" stroke-width="16" fill="none" opacity=".7" stroke-linecap="round"/>'
for x,y,s in [(170,170,40),(640,180,34),(650,660,40),(160,640,30)]: b+=star5(x,y,s,'#ffd82a')
I[1792]=svg(b,d)

# 384 セカンド・ラブ: two umbrellas side by side in the evening snow, one red and one dark, closer than before
d,b=bg([(0,'#3a4a6a'),(1,'#7a8aa8')])
b+=snow(80,384,.8)+'<rect y="640" width="800" height="160" fill="#e8eef8"/>'
b+=figure(320,740,240,'#1a1a2a')+figure(470,740,220,'#1a1a2a',hair='#1a1a2a')
b+=wagasa(320,480,120,'#2a2a3a',-10,'#5a5a6a')+wagasa(480,500,120,'#c8182a',10)
I[384]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
