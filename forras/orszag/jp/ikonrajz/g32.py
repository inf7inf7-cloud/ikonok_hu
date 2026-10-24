import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 32. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 413 BOYのテーマ: a boy and a girl's eyes meeting across a school track at sunset, pastel 80s idol
d,b=bg([(0,'#ffb0c0'),(1,'#ffe8c8')])
b+='<circle cx="400" cy="420" r="100" fill="#fff0d0"/><rect y="460" width="800" height="340" fill="#d8784a"/>'+''.join(f'<path d="M0 {y} Q400 {y-40} 800 {y}" stroke="#fff" stroke-width="4" fill="none" opacity=".7"/>' for y in (540,620,710))
b+=figure(220,620,220,'#3a1a2a')+figure(580,620,210,'#3a1a2a',hair='#3a1a2a')+heart(400,320,30,'#ff5a8a')+'<path d="M260 380 Q400 300 540 380" stroke="#fff" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
I[413]=svg(b,d)

# 514 OH YEAH!: a girl band on stage, a drum kit and fists in the air under confetti, 1990 tour
d,b=bg([(0,'#1a0a3a'),(1,'#5a1a6a')])
b+=confetti(70,514,['#ff3a8a','#ffd02a','#3ad0ff','#fff'])+''.join(f'<polygon points="{x},0 {x-90},560 {x+90},560" fill="#fff" opacity=".08"/>' for x in (180,400,620))
b+='<rect y="560" width="800" height="240" fill="#14082a"/><circle cx="400" cy="520" r="70" fill="#e8e8f0"/><circle cx="400" cy="520" r="56" fill="none" stroke="#c8102a" stroke-width="6"/>'+star5(400,520,30,'#c8102a')
b+=figure(200,560,220,'#000',pose='up',hair='#000')+figure(600,560,220,'#000',pose='wave',hair='#000')
I[514]=svg(b,d)

# 587 JUST ONE MORE KISS: a dark gothic rose with a single blood-red drop on black velvet, decadent
d,b=bg([(0,'#0a0008'),(1,'#1a0a1a')])
b+=glow(400,380,180,'#8a0a3a',.5)+'<path d="M400 560 Q380 680 400 780" stroke="#1a3a1a" stroke-width="10" fill="none"/>'+rose(400,380,1.6)
b+='<path d="M400 470 Q390 500 400 515 Q410 500 400 470Z" fill="#c8001a"/>'+''.join(f'<path d="M{x} 0 L{x+30} 800" stroke="#2a0a2a" stroke-width="40" opacity=".4"/>' for x in (60,700))
I[587]=svg(b,d)

# 709 おさえきれない この気持ち: a strawberry crushed in a fist, juice dripping, early-90s rock
d,b=bg([(0,'#2a0a14'),(1,'#5a1a2a')])
b+='<path d="M300 300 Q400 220 500 300 Q520 420 400 520 Q280 420 300 300Z" fill="#e8102a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="8" fill="#ffe46a"/>' for x,y in [(350,320),(400,300),(450,320),(340,380),(400,370),(460,380),(370,440),(430,440)])
b+='<path d="M360 280 Q400 230 440 280 Q420 260 400 270 Q380 260 360 280Z" fill="#3ab84a"/>'
b+='<path d="M260 380 Q240 520 320 560 L480 560 Q560 520 540 380 L500 380 L500 480 L300 480 L300 380Z" fill="#e8c0a0"/>'+''.join(f'<path d="M{x} 560 Q{x+4} 620 {x} 680" stroke="#c8001a" stroke-width="8" fill="none"/>' for x in (360,420))
I[709]=svg(b,d)

# 758 光の射す方へ: a man walking out of a dark tunnel toward a bright opening of light
d,b=bg([(0,'#0a0a0a'),(1,'#1a1a1a')])
b+='<ellipse cx="400" cy="360" rx="160" ry="200" fill="#fff8d8"/>'+glow(400,360,240,'#fff8d8',.5)+''.join(ring(400,360,r,'#2a2a2a',30) for r in (260,340,420))
b+='<polygon points="400,560 240,800 560,800" fill="#fff8d8" opacity=".25"/>'+figure(400,620,220,'#000')
I[758]=svg(b,d)

# 885 シングルベッド: a narrow single bed by a window at night, one pillow dented, mid-90s loneliness
d,b=bg([(0,'#1a2040'),(1,'#3a4060')])
b+='<rect x="460" y="100" width="260" height="300" fill="#2a3a6a"/>'+moon(600,200,40)+starsf(20,885,380)+'<rect x="460" y="100" width="260" height="300" fill="none" stroke="#14142a" stroke-width="14"/>'
b+='<rect x="100" y="480" width="420" height="140" fill="#e8e8f0"/><rect x="90" y="400" width="30" height="300" fill="#4a3a2a"/><rect x="510" y="520" width="20" height="180" fill="#4a3a2a"/><ellipse cx="190" cy="470" rx="70" ry="30" fill="#fff"/><path d="M220 482 Q400 470 520 500 L520 620 L220 620Z" fill="#7a8ac8"/>'
I[885]=svg(b,d)

# 1623 君を待ってる: a candy-wrapped bus stop at dawn, a figure waiting with an umbrella, colorful candies
d,b=bg([(0,'#ffd8e8'),(1,'#d8f0ff')])
b+='<rect x="140" y="200" width="20" height="440" fill="#5a5a6a"/><rect x="100" y="180" width="100" height="80" rx="40" fill="#ff5a8a"/>'+'<rect y="640" width="800" height="160" fill="#c8c8d0"/>'
b+=figure(400,660,260,'#2a2a4a')+''.join(f'<g transform="translate({x} {y}) rotate({a})"><ellipse rx="30" ry="22" fill="{c}"/><path d="M-30 0 L-50 -16 L-50 16Z M30 0 L50 -16 L50 16Z" fill="{c}"/></g>' for x,y,a,c in [(560,240,20,'#ffd02a'),(660,380,-10,'#3ad0ff'),(520,420,30,'#8ad84a'),(640,160,-25,'#ff8a2a')])
I[1623]=svg(b,d)

# 1643 WMDA: a pair of eyeglasses through which the grey world turns colorful, a new view
d,b=bg([(0,'#7a7a80'),(1,'#5a5a60')])
b+='<rect x="0" y="0" width="800" height="800" fill="#6a6a70"/>'
for x in (260,540): b+=f'<clipPath id="c{x}"><circle cx="{x}" cy="400" r="120"/></clipPath><g clip-path="url(#c{x})"><rect x="{x-130}" y="270" width="260" height="260" fill="#7ad0ff"/><circle cx="{x+40}" cy="360" r="40" fill="#ffd02a"/><rect x="{x-130}" y="440" width="260" height="100" fill="#5ac85a"/></g>'+ring(x,400,120,'#1a1a1a',18)
b+='<path d="M380 390 Q400 370 420 390" stroke="#1a1a1a" stroke-width="16" fill="none"/>'
I[1643]=svg(b,d)

# 238 誘惑: two wine glasses not quite touching on a dark table, a cold blue distance between them
d,b=bg([(0,'#0a0a1a'),(1,'#1a2a3a')])
b+='<rect y="560" width="800" height="240" fill="#14141e"/>'
for x,c in ((280,'#8a0a2a'),(520,'#8a0a2a')): b+=f'<path d="M{x-60} 300 Q{x-60} 440 {x} 450 Q{x+60} 440 {x+60} 300Z" fill="#cfe0ff" opacity=".35"/><path d="M{x-56} 360 Q{x-50} 440 {x} 446 Q{x+50} 440 {x+56} 360Z" fill="{c}"/><rect x="{x-4}" y="450" width="8" height="100" fill="#cfe0ff" opacity=".5"/><ellipse cx="{x}" cy="556" rx="50" ry="10" fill="#cfe0ff" opacity=".5"/>'
b+='<path d="M360 360 L440 360" stroke="#7ab0ff" stroke-width="3" stroke-dasharray="6 8" opacity=".6"/>'
I[238]=svg(b,d)

# 251 埠頭を渡る風: a couple on a night pier in Tokyo harbour, wind blowing her hair and a scarf, cranes behind
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+=starsf(40,251,300)+''.join(f'<path d="M{x} 460 L{x} 260 L{x+80} 240 M{x} 300 L{x+60} 300" stroke="#1a2a4a" stroke-width="10" fill="none"/>' for x in (520,640))+'<rect y="460" width="800" height="340" fill="#0a1428"/>'
b+='<rect x="0" y="560" width="520" height="40" fill="#3a3a4a"/>'+figure(240,560,200,'#000')+figure(310,560,190,'#000',hair='#000')+'<path d="M320 380 Q380 370 420 350" stroke="#000" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x} {y} q40 -10 80 0" stroke="#cfe0ff" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(400,300),(460,360),(420,420)])
I[251]=svg(b,d)

# 327 Single Again: a ringing landline at night beside a framed photo turned face down, late-80s
d,b=bg([(0,'#3a2a3a'),(1,'#6a4a5a')])
b+=glow(560,300,160,'#ffd8a0',.4)+'<rect y="560" width="800" height="240" fill="#2a1a1a"/>'+phone(260,520,1.1,'#e8e0d0')
b+=''.join(f'<path d="M{170+k*40} {380-k*10} q-14 -20 0 -40" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>' for k in range(3))
b+='<path d="M480 560 L520 470 L660 470 L620 560Z" fill="#8a6a4a"/><path d="M520 470 L540 430" stroke="#8a6a4a" stroke-width="6"/>'
I[327]=svg(b,d)

# 537 キラキラ: sunlight glittering on a river, two hands nearly holding, sparkles everywhere
d,b=bg([(0,'#7ac8ff'),(1,'#e0f4ff')])
b+='<rect y="420" width="800" height="380" fill="#3a9ad8"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(120,500,22),(260,600,16),(400,520,28),(560,640,18),(680,480,24),(200,720,14),(620,560,12),(340,700,20)])
b+='<path d="M120 380 Q240 330 330 340 L340 370 Q250 380 150 420Z M680 380 Q560 330 470 340 L460 370 Q550 380 650 420Z" fill="#f0c8a8"/>'+sparkle(400,350,40,'#fff4b0')
I[537]=svg(b,d)

# 1031 群青日和: an ultramarine sky with a girl in a sailor-suit silhouette spreading arms on a Tokyo rooftop
d,b=bg([(0,'#0a2a8a'),(1,'#3a7ae8')])
b+=cloud(600,200,1.3,'#fff',.85)+skyline(640,'#0a1a4a',1031,60,260)+'<rect y="640" width="800" height="160" fill="#2a2a3a"/>'
b+=figure(400,660,300,'#0a0a1a',pose='up',hair='#0a0a1a')+'<path d="M350 430 L450 430 L430 470 L370 470Z" fill="#fff"/>'
I[1031]=svg(b,d)

# 1385 Kind of love: two paper cranes facing each other with a thin string heart between them, soft pastel
d,b=bg([(0,'#e8f0ff'),(1,'#ffe8f0')])
def crane(x,y,s,col,flip=False):
    return f'<g transform="translate({x} {y}) scale({-s if flip else s} {s})" fill="{col}"><polygon points="0,0 -90,-60 -20,-10"/><polygon points="0,0 60,-120 20,-10"/><polygon points="-20,-10 20,-10 40,40 -40,40"/><polygon points="40,40 110,-30 90,-40 30,20"/><polygon points="-40,40 -100,10 -40,20"/></g>'
b+=crane(250,420,1.4,'#ff8ab0')+crane(550,420,1.4,'#8ab0ff',True)+heart(400,300,40,'none','stroke="#e8102a" stroke-width="4"')
I[1385]=svg(b,d)

# 441 恋の予感: an airplane passing over a star-filled sky, wind lines, a figure looking up from a field
d,b=bg([(0,'#04081a'),(1,'#1a2a5a')])
b+=starsf(140,441,600)+'<path d="M560 200 L700 160 L680 180 L740 170 L720 190 L700 186 L580 216Z" fill="#e8e8f0"/>'+glow(720,175,14,'#ff3a3a',.9,'glow2')
b+=''.join(f'<path d="M{x} {y} q60 -20 120 0" stroke="#cfe0ff" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(80,380),(200,440),(360,400)])+'<path d="M0 640 Q400 600 800 650 L800 800 L0 800Z" fill="#0a0a14"/>'+figure(260,660,140,'#000')
I[441]=svg(b,d)

# 562 吐息でネット: a lip-gloss breath fogging a window and drawing a net of hearts, spring pastel
d,b=bg([(0,'#c8e8ff'),(1,'#ffe0ea')])
b+=glow(400,400,240,'#fff',.6)+''.join(f'<path d="M{x} 200 L{x} 600" stroke="#ff8ab0" stroke-width="3" opacity=".6"/>' for x in range(220,600,40))+''.join(f'<path d="M200 {y} L600 {y}" stroke="#ff8ab0" stroke-width="3" opacity=".6"/>' for y in range(220,600,40))
b+=''.join(heart(x,y,16,'#ff5a8a') for x,y in [(300,300),(460,340),(380,460),(520,500),(260,520)])+profile(160,800,1.2,'#e8a0b0')
I[562]=svg(b,d)

# 579 涙をみせないで: a boy turning away under a pastel spotlight, a single tear hidden, Wink duo dance-pop
d,b=bg([(0,'#2a2a5a'),(1,'#8a6ab8')])
b+=''.join(f'<polygon points="{x},0 {x-120},800 {x+120},800" fill="{c}" opacity=".15"/>' for x,c in [(260,'#ffb0d8'),(540,'#b0e8ff')])
b+=figure(320,720,330,'#0a0a1a',hair='#0a0a1a')+figure(480,720,330,'#0a0a1a',hair='#0a0a1a')+'<path d="M400 330 Q392 350 400 360 Q408 350 400 330Z" fill="#cfe6ff"/>'+sparkle(600,200,24,'#fff')+sparkle(200,240,18,'#fff')
I[579]=svg(b,d)

# 1014 kanariya: a yellow canary in an open birdcage with a red thread, dark ballad
d,b=bg([(0,'#1a1a24'),(1,'#3a3a4a')])
b+=glow(400,420,200,'#ffd02a',.25)+''.join(f'<path d="M{x} 260 Q{x} 200 400 160" stroke="#c8a24a" stroke-width="5" fill="none"/>' for x in (240,300,500,560))+''.join(f'<path d="M{x} 260 L{x} 620" stroke="#c8a24a" stroke-width="5"/>' for x in range(240,580,40))
b+='<rect x="220" y="610" width="360" height="24" fill="#c8a24a"/><path d="M240 260 L560 260" stroke="#c8a24a" stroke-width="6"/><path d="M520 300 L640 260 L640 480 L520 520Z" fill="none" stroke="#c8a24a" stroke-width="5"/>'
b+='<ellipse cx="380" cy="470" rx="60" ry="44" fill="#ffd82a"/><circle cx="430" cy="430" r="30" fill="#ffd82a"/><circle cx="440" cy="424" r="5" fill="#000"/><polygon points="458,432 480,438 458,444" fill="#ff8a2a"/><path d="M320 470 L280 490 L320 500Z" fill="#ffd82a"/>'
b+='<path d="M380 510 Q360 580 400 620 Q440 680 420 760" stroke="#e8102a" stroke-width="4" fill="none"/>'
I[1014]=svg(b,d)

# 1143 3月9日: a spring morning, a window with a calendar circled on March 9 and cherry buds, a green leaf
d,b=bg([(0,'#cfe8ff'),(1,'#fff6ea')])
b+='<rect x="200" y="160" width="400" height="460" rx="12" fill="#fff"/><rect x="200" y="160" width="400" height="90" rx="12" fill="#3a9a5a"/>'+txt(400,230,'3月',60,'#fff',900)
b+=''.join(f'<rect x="{230+(k%7)*52}" y="{280+(k//7)*64}" width="36" height="36" rx="4" fill="#e8eef4"/>' for k in range(35))+ring(230+(8%7)*52+18,280+(8//7)*64+18,34,'#e8402a',7)
b+=''.join(sakura(x,y,s,'#ffc8da','#ff8ab0',r) for x,y,s,r in [(150,180,50,0),(660,620,46,20)])
I[1143]=svg(b,d)

# 239 りばいばる: a 45rpm record spinning in a street-corner jukebox at dusk, music notes drifting, late-70s
d,b=bg([(0,'#5a3a5a'),(1,'#e8a088')])
b+=skyline(600,'#3a2a3a',239,80,260,'#ffd8a0',40)+'<rect y="600" width="800" height="200" fill="#2a1a2a"/>'
b+='<circle cx="400" cy="400" r="200" fill="#111"/>'+''.join(ring(400,400,r,'#2a2a2a',2) for r in range(80,200,16))+'<circle cx="400" cy="400" r="70" fill="#e8402a"/><circle cx="400" cy="400" r="12" fill="#f4e8d8"/>'
b+=''.join(note(x,y,24,'#fff') for x,y in [(600,240),(660,180),(160,260)])
I[239]=svg(b,d)

# 291 Sayonara Baby: a beach bar sign at sunset with a waving hand and a convertible leaving, Southern All Stars summer
d,b=bg([(0,'#ff7a5a'),(1,'#ffd890')])
b+='<circle cx="400" cy="420" r="120" fill="#fff0c8"/><rect y="440" width="800" height="140" fill="#3a6aa8"/><rect y="580" width="800" height="220" fill="#e8c890"/>'
b+='<path d="M560 600 L600 560 L720 556 L760 590 L760 620 L560 620Z" fill="#c8102a"/>'+''.join(f'<path d="M{x} 580 L{x} 380" stroke="#3a2a1a" stroke-width="10"/><path d="M{x} 380 q-50 -10 -80 20 M{x} 380 q50 -10 80 20 M{x} 380 q-20 -40 -50 -50 M{x} 380 q20 -40 50 -50" stroke="#2a4a1a" stroke-width="10" fill="none"/>' for x in (100,))
b+='<path d="M260 700 Q280 600 300 560 L340 560 L330 700Z" fill="#f0c8a8"/>'+''.join(f'<rect x="{x}" y="500" width="14" height="70" rx="7" fill="#f0c8a8" transform="rotate({a} {x+7} 570)"/>' for x,a in [(296,-20),(312,-6),(328,8),(342,22)])
I[291]=svg(b,d)

# 420 デビュー~Fly Me To Love~: an idol stepping onto a glittering stage with a heart-shaped balloon lifting her
d,b=bg([(0,'#ffb0d8'),(1,'#d8c8ff')])
b+=''.join(sparkle(x,y,s,'#fff') for x,y,s in [(120,140,20),(660,120,26),(700,400,16),(100,420,18)])+'<rect y="620" width="800" height="180" fill="#ff8ab8"/>'+''.join(f'<circle cx="{x}" cy="640" r="8" fill="#fff"/>' for x in range(20,800,50))
b+='<path d="M400 560 L460 200" stroke="#fff" stroke-width="3"/>'+heart(460,170,80,'#ff3a8a')+figure(400,620,240,'#4a1a4a',pose='up',hair='#4a1a4a')
I[420]=svg(b,d)

# 453 もしも明日が: three children holding hands on a hill at dawn, simple child-like hope, mid-80s
d,b=bg([(0,'#ffd8a0'),(1,'#fff6e0')])
b+=rays(400,560,20,'#fff',.25,8,180,360)+'<circle cx="400" cy="560" r="100" fill="#ffe46a"/>'+hills(580,30,'#7ab85a',453)
b+=figure(280,620,160,'#3a2a1a')+figure(400,620,180,'#3a2a1a',hair='#3a2a1a')+figure(520,620,150,'#3a2a1a')+'<path d="M300 520 L380 520 M420 520 L500 520" stroke="#3a2a1a" stroke-width="10" stroke-linecap="round"/>'
I[453]=svg(b,d)

# 493 Poison: a skull-shaped glass perfume bottle with green poison glow, sharp guitar edge
d,b=bg([(0,'#0a0a0a'),(1,'#1a1a1a')])
b+=glow(400,420,200,'#3aff6a',.35)+'<rect x="370" y="180" width="60" height="80" fill="#c8c8d0"/><path d="M300 280 L500 280 L540 420 Q540 600 400 620 Q260 600 260 420Z" fill="#3aff6a" opacity=".55"/>'
b+='<circle cx="350" cy="420" r="30" fill="#0a0a0a"/><circle cx="450" cy="420" r="30" fill="#0a0a0a"/><path d="M390 470 L400 490 L410 470Z" fill="#0a0a0a"/>'+''.join(f'<rect x="{x}" y="520" width="16" height="30" fill="#0a0a0a"/>' for x in (360,384,408,432))
b+='<path d="M0 760 L800 640" stroke="#fff" stroke-width="4" opacity=".7"/><path d="M0 780 L800 660" stroke="#fff" stroke-width="2" opacity=".4"/>'
I[493]=svg(b,d)

# 496 Beat Emotion: a geometric black-and-white guitar silhouette with pulse lines, 90s Hotei style
d,b=bg([(0,'#f4f4f4'),(1,'#d8d8d8')])
b+=''.join(f'<rect x="{x}" y="0" width="40" height="800" fill="#111" opacity=".9"/>' for x in range(0,800,80))
b+='<g transform="rotate(-30 400 420)"><path d="M300 380 L500 380 L520 520 L420 600 L380 600 L280 520Z" fill="#e8102a"/><rect x="390" y="80" width="20" height="320" fill="#111"/><rect x="370" y="60" width="60" height="40" fill="#111"/></g>'
b+='<path d="M0 640 L200 640 L240 560 L280 720 L320 600 L360 640 L800 640" stroke="#e8102a" stroke-width="10" fill="none"/>'
I[496]=svg(b,d)

# 716 だって夏じゃない: a surfboard and a beer-free soda bottle on blazing sand, a giant sun and seagull
d,b=bg([(0,'#1ab0ff'),(1,'#a8e8ff')])
b+=rays(620,160,22,'#fff',.25,7)+'<circle cx="620" cy="160" r="80" fill="#fff8c0"/><rect y="420" width="800" height="160" fill="#0a8ad8"/><rect y="580" width="800" height="220" fill="#fff0c0"/>'
b+='<ellipse cx="300" cy="460" rx="60" ry="240" fill="#ff7a2a" transform="rotate(-14 300 460)"/><path d="M250 260 L350 700" stroke="#fff" stroke-width="10" transform="rotate(0)"/>'+bird(500,300,40,'#fff')+bird(580,340,26,'#fff')
I[716]=svg(b,d)

# 1152 Million Films: an old film reel unspooling into a heart shape of photo frames, wedding warmth
d,b=bg([(0,'#f8ead8'),(1,'#e8c8a8')])
b+=ring(200,260,120,'#3a3a3a',30)+''.join(f'<circle cx="{200+70*math.cos(a)}" cy="{260+70*math.sin(a)}" r="22" fill="#f8ead8"/>' for a in [k*math.pi/3 for k in range(6)])+'<circle cx="200" cy="260" r="20" fill="#3a3a3a"/>'
b+='<path d="M300 300 Q560 240 600 380 Q620 520 420 640 Q240 520 280 420" stroke="#3a3a3a" stroke-width="56" fill="none"/>'+''.join(f'<rect x="{x-18}" y="{y-14}" width="36" height="28" fill="#ffd8a0"/>' for x,y in [(380,284),(480,290),(570,330),(600,420),(560,520),(480,590),(360,560),(290,470)])
I[1152]=svg(b,d)

# 1288 この夜を止めてよ: a clock's hands held still by a woman's hand at midnight, rain on the window, deep blue
d,b=bg([(0,'#0a1028'),(1,'#1a2a4a')])
b+=rain(60,1288,'#9ab0d8',.3)+'<circle cx="400" cy="380" r="200" fill="#e8e8f0"/>'+ring(400,380,200,'#3a3a4a',14)+''.join(f'<rect x="396" y="196" width="8" height="24" fill="#3a3a4a" transform="rotate({a} 400 380)"/>' for a in range(0,360,30))
b+='<path d="M400 380 L400 230" stroke="#1a1a1a" stroke-width="10"/><path d="M400 380 L410 260" stroke="#1a1a1a" stroke-width="6"/><path d="M420 240 Q480 200 560 220 L600 260 L460 280Z" fill="#f0c8a8"/>'
I[1288]=svg(b,d)

# 1331 翼はいらない: a girl sitting on grass with a guitar under a big folk-era sky, feathers drifting down, no wings
d,b=bg([(0,'#8ac8f8'),(1,'#f0f6ff')])
b+=cloud(200,160,1.2)+hills(560,30,'#7ab85a',1331)+''.join(f'<path transform="translate({x} {y}) rotate({a})" d="M0 -40 Q20 0 0 40 Q-20 0 0 -40Z M0 -40 L0 50" fill="#fff" stroke="#c8d8e8" stroke-width="2"/>' for x,y,a in [(560,200,30),(640,320,-20),(480,300,60)])
b+=figure(320,680,220,'#2a2a3a',hair='#2a2a3a')+guitar(330,560,.55,-50,'#c8902a')
I[1331]=svg(b,d)

# 1607 SERIOUS: a ghostly translucent figure behind a man reflected in a dark window, eerie teal
d,b=bg([(0,'#04141a'),(1,'#0a2a34')])
b+='<rect x="120" y="100" width="560" height="560" fill="#0a1e26" stroke="#2a4a54" stroke-width="12"/>'+profile(360,660,1.5,'#000')
b+='<g opacity=".35">'+figure(520,620,420,'#7affff')+'</g>'+glow(520,300,140,'#7affff',.25)
I[1607]=svg(b,d)

# 179 夫婦鏡: an old married couple reflected together in a round hand mirror, warm enka sepia
d,b=bg([(0,'#c8a87a'),(1,'#8a6a4a')])
b+='<rect x="380" y="560" width="40" height="200" rx="16" fill="#6a3a1a"/><circle cx="400" cy="380" r="200" fill="#6a3a1a"/><circle cx="400" cy="380" r="176" fill="#e8d8b8"/>'
b+=profile(330,540,.9,'#4a2a1a')+profile(470,540,.85,'#4a2a1a',True)+'<path d="M330 330 Q300 300 320 270" stroke="#e8d8b8" stroke-width="4" fill="none" opacity=".4"/>'
I[179]=svg(b,d)

# 463 バナナの涙: a cartoonish banana with a single big tear and a bow, silly pop idol trio
d,b=bg([(0,'#fff6a0'),(1,'#ffd0e0')])
b+='<path d="M220 300 Q240 560 520 600 Q620 600 640 560 Q440 520 320 300Z" fill="#ffe02a"/><path d="M320 300 L300 260 L330 250Z" fill="#6a4a1a"/><path d="M560 580 Q600 570 630 560" stroke="#c8a02a" stroke-width="6" fill="none"/>'
b+='<path d="M430 470 Q410 520 430 540 Q450 520 430 470Z" fill="#7ad8ff"/><path d="M300 300 Q260 270 270 250 Q300 260 310 290 Q320 250 350 250 Q350 280 300 300Z" fill="#ff5aa0"/>'
I[463]=svg(b,d)

# 696 息もできない: a wok with tossing flames and noodles flying into the air, breathless speed lines
d,b=bg([(0,'#2a0a0a'),(1,'#6a1a0a')])
b+=''.join(f'<path d="M{x} 800 Q{x-30} 640 {x+10} 560" stroke="#ff8a2a" stroke-width="20" fill="none" opacity=".6"/>' for x in range(200,640,60))+glow(400,560,160,'#ffb02a',.5)
b+='<path d="M200 540 Q400 680 600 540Z" fill="#2a2a2a"/><rect x="590" y="520" width="160" height="20" rx="10" fill="#3a2a1a" transform="rotate(-12 600 530)"/>'
b+=''.join(f'<path d="M{x} 520 Q{x+30} {380-k*30} {x+60} {300-k*20}" stroke="#ffe8a0" stroke-width="8" fill="none"/>' for k,x in enumerate((300,340,380,420,460)))
I[696]=svg(b,d)

# 770 Unknown Thread: a single thread unspooling across a quiet grey room toward a window, subtle feelings
d,b=bg([(0,'#d8d8d4'),(1,'#b8b8b0')])
b+='<rect x="460" y="140" width="240" height="320" fill="#f4f0e4"/>'+glow(580,300,120,'#fff',.4)
b+='<circle cx="200" cy="600" r="60" fill="#5a7ab0"/>'+''.join(f'<path d="M150 {580+k*8} L250 {580+k*8}" stroke="#3a5a90" stroke-width="3"/>' for k in range(5))
b+='<path d="M250 580 Q360 420 300 360 Q240 300 420 300 Q560 300 520 220" stroke="#5a7ab0" stroke-width="4" fill="none"/>'
I[770]=svg(b,d)

# 1153 流星: a shooting star over a moonlit seaside town, a man and a woman's silhouettes watching
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
b+=starsf(100,1153,480)+'<path d="M700 80 L360 300" stroke="#fff" stroke-width="5" opacity=".7"/>'+sparkle(360,300,30,'#fff')+glow(360,300,40,'#fff',.6)
b+='<rect y="480" width="800" height="320" fill="#0a1830"/>'+skyline(560,'#0a0a14',1153,20,80,'#ffd27a',20)+'<rect y="560" width="800" height="240" fill="#0a0a14"/>'+figure(340,620,150,'#000')+figure(400,620,140,'#000',hair='#000')
I[1153]=svg(b,d)

# 1259 チェリッシュ: a jewelry box with a cherry pendant glowing on velvet, pink-gold sparkle
d,b=bg([(0,'#ffd8e8'),(1,'#ffb8d0')])
b+=glow(400,420,200,'#fff',.6)+'<rect x="250" y="460" width="300" height="180" rx="18" fill="#c83a6a"/><path d="M250 460 L270 330 Q400 300 530 330 L550 460Z" fill="#e8508a"/><rect x="270" y="440" width="260" height="40" fill="#ff8ab0"/>'
b+='<path d="M380 300 Q400 380 370 440 M420 300 Q400 380 430 440" stroke="#2a8a3a" stroke-width="5" fill="none"/><circle cx="370" cy="450" r="30" fill="#e8102a"/><circle cx="430" cy="450" r="30" fill="#e8102a"/>'+sparkle(350,436,10,'#fff')+sparkle(470,320,24,'#fff')
I[1259]=svg(b,d)

# 1294 Love Forever: two microphones with intertwined cables forming an infinity symbol, duet
d,b=bg([(0,'#2a1a3a'),(1,'#6a3a6a')])
b+='<path d="M400 500 C300 380 160 420 200 520 C240 620 340 600 400 500 C460 400 560 380 600 480 C640 580 500 620 400 500Z" stroke="#ff8ac0" stroke-width="12" fill="none"/>'
b+=enka_mic(240,320,90,'#d8d8e0')+enka_mic(560,320,90,'#c8a24a')+glow(400,500,60,'#ff8ac0',.4)
I[1294]=svg(b,d)

# 1378 Lonesome rabbit: a white rabbit silhouette inside a glowing smartphone screen in a dark room
d,b=bg([(0,'#04040a'),(1,'#10101a')])
b+=glow(400,420,220,'#7ab0ff',.3)+'<rect x="260" y="160" width="280" height="520" rx="34" fill="#1a1a24"/><rect x="280" y="190" width="240" height="460" rx="10" fill="#3a6ad8"/>'
b+='<ellipse cx="400" cy="520" rx="70" ry="60" fill="#fff"/><circle cx="400" cy="440" r="46" fill="#fff"/><ellipse cx="380" cy="360" rx="14" ry="50" fill="#fff"/><ellipse cx="420" cy="360" rx="14" ry="50" fill="#fff"/><circle cx="414" cy="436" r="6" fill="#e8102a"/>'
I[1378]=svg(b,d)

# 1874 気分上々↑↑: a disco ball with two upward arrows blasting in neon, club party
d,b=bg([(0,'#1a0a3a'),(1,'#3a0a5a')])
b+=rays(400,260,24,'#fff',.1,5)+'<circle cx="400" cy="260" r="120" fill="#c8c8d8"/>'+''.join(f'<rect x="{400+x-12}" y="{260+y-12}" width="22" height="22" fill="{c}" opacity=".85"/>' for x,y,c in [(x,y,['#fff','#8a8aa0','#e8e8f0','#a8a8c0'][(x+y)//24%4]) for x in range(-96,120,24) for y in range(-96,120,24) if x*x+y*y<110*110])
b+=''.join(f'<path d="M{x} 720 L{x} 480 M{x-50} 540 L{x} 480 L{x+50} 540" stroke="{c}" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' for x,c in [(300,'#ff3aa8'),(500,'#3ad0ff')])
I[1874]=svg(b,d)

# 252 卒業写真: an old graduation class photo with one face circled, held in hands, mid-70s nostalgia
d,b=bg([(0,'#d8c8a8'),(1,'#b8a888')])
b+='<rect x="140" y="200" width="520" height="380" fill="#fffaf0" transform="rotate(-4 400 390)"/><rect x="170" y="230" width="460" height="300" fill="#a89a80" transform="rotate(-4 400 390)"/>'
b+='<g transform="rotate(-4 400 390)">'+''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="#3a3028"/><rect x="{x-18}" y="{y+14}" width="36" height="40" fill="#3a3028"/>' for y in (300,380,460) for x in range(220,620,56))+ring(388,380,28,'#e8402a',5)+'</g>'
b+='<path d="M100 700 Q160 580 200 560 L220 600 Q180 640 160 720Z M700 700 Q640 580 600 560 L580 600 Q620 640 640 720Z" fill="#f0c8a8"/>'
I[252]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
