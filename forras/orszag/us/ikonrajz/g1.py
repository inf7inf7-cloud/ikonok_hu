import sys,math;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 1. csoport: a sikerindex szerinti első 20 dal (2026-10-24)
I={}

# 1 Smooth (Santana ft. Rob Thomas, 1999): a hot Spanish Harlem night, a guitar silhouette in heat haze and a woman in a red dress twirling
d,b=bg([(0,'#3a0a12'),(.55,'#a8261c'),(1,'#f08a2a')])
d+=lg('heat',S((0,'#ffcf6a',.0),(1,'#ffcf6a',.55)))
b+=glow(400,520,300,'#ffb04a',.45)
for k in range(9): b+=f'<path d="M{k*100-40} 800 Q{k*100} 700 {k*100-30} 620 Q{k*100-60} 540 {k*100-20} 470" stroke="#ffd27a" stroke-width="6" fill="none" opacity=".18"/>'
b+=skyline(600,'#24060a',1,80,240,'#ffcb6a',70)+'<rect y="600" width="800" height="200" fill="#1a0408"/>'
b+=eguitar(250,520,105,'#2a0a0a','#1a0606',rot=-18)
b+='<g transform="translate(540 760)"><path d="M0 -330 q-18 -4 -18 -26 q2 -22 20 -22 q18 0 20 22 q0 22 -22 26Z" fill="#14040a"/>'
b+='<path d="M-6 -300 L10 -300 L40 -200 Q120 -60 150 0 L-150 0 Q-70 -90 -26 -200Z" fill="#e01a2a"/><path d="M-150 0 Q-40 -40 150 0 Q30 -22 -150 0Z" fill="#a80e1c"/>'
b+='<path d="M8 -290 Q60 -320 90 -370" stroke="#14040a" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M-4 -288 Q-50 -250 -80 -210" stroke="#14040a" stroke-width="14" fill="none" stroke-linecap="round"/></g>'
I[1]=svg(b,d)

# 2 Closer (The Chainsmokers ft. Halsey, 2016): two young lovers on the hood of an old car at night, city lights far away, warm mattress-pink glow
d,b=bg([(0,'#0b0a2a'),(.6,'#3a1a5a'),(1,'#d96a8a')])
b+=starsf(70,2,420,'#ffe6f2')+moon(620,150,40,'#ffe9f2',.3)
b+=skyline(560,'#1a1238',22,30,110,'#ffd0e6',90)
b+='<rect y="560" width="800" height="240" fill="#0d0a1c"/>'
b+=car(400,720,140,'#e5e1ea','#cfd0dc',glass='#ffc4dc')
b+='<g fill="#0d0a1c"><circle cx="350" cy="565" r="22"/><path d="M325 590 Q350 575 375 590 L380 640 L320 640Z"/><circle cx="420" cy="560" r="21"/><path d="M398 585 Q420 572 444 585 L448 640 L392 640Z"/>'
b+='<path d="M302 640 L470 640 L470 652 L302 652Z"/></g>'+heart(386,520,22,'#ff7aa8','opacity=".9"')
I[2]=svg(b,d)

# 3 Sweet Child o' Mine (Guns N' Roses, 1987): a cherry-sunburst Les Paul against an iris "as blue as the sky", roses at its base
d,b=bg([(0,'#061a3a'),(1,'#0a2c5c')])
d+=rg('iris',S((0,'#000',1),(.22,'#0a0a10',1),(.25,'#1c6fd6',1),(.6,'#6fc6ff',1),(.95,'#1a4ea0',1),(1,'#0a2c5c',0)))
b+='<circle cx="400" cy="380" r="300" fill="url(#iris)"/>'
for k in range(48):
    a=math.radians(k*7.5);b+=f'<line x1="{400+80*math.cos(a):.0f}" y1="{380+80*math.sin(a):.0f}" x2="{400+270*math.cos(a):.0f}" y2="{380+270*math.sin(a):.0f}" stroke="#bfe8ff" stroke-width="3" opacity=".25"/>'
b+='<ellipse cx="330" cy="290" rx="40" ry="26" fill="#fff" opacity=".7"/>'
g='<g transform="translate(400 470) rotate(-28)">'
g+='<rect x="-10" y="-330" width="20" height="230" rx="4" fill="#2a1408"/><path d="M-20 -380 L20 -380 L14 -330 L-14 -330Z" fill="#14080a"/>'
g+='<path d="M-60 -110 Q-90 -150 -40 -150 Q0 -120 20 -150 Q90 -160 75 -90 Q110 -40 95 30 Q80 120 0 120 Q-90 120 -100 30 Q-112 -50 -60 -110Z" fill="#b8241a"/>'
g+='<path d="M-40 -90 Q0 -100 60 -80 Q85 -30 70 30 Q55 95 0 95 Q-65 95 -75 30 Q-85 -40 -40 -90Z" fill="#f2a43a" opacity=".75"/>'
g+='<rect x="-30" y="-40" width="60" height="16" rx="5" fill="#ddd"/><rect x="-30" y="10" width="60" height="16" rx="5" fill="#ddd"/><rect x="-24" y="55" width="48" height="10" fill="#222"/></g>'
b+=g
for x,y in [(130,700),(200,740),(620,710),(690,745)]:
    b+=f'<circle cx="{x}" cy="{y}" r="30" fill="#c8102e"/><path d="M{x-16} {y} Q{x} {y-24} {x+16} {y} Q{x} {y+10} {x-16} {y}Z" fill="#8a0a1e"/><path d="M{x} {y+28} L{x} {y+80}" stroke="#1a5a2a" stroke-width="7"/>'
I[3]=svg(b,d)

# 4 How Do I Live (LeAnn Rimes, 1997): a woman at a rain-streaked night window, her reflection hugging a glowing heart
d,b=bg([(0,'#0a1424'),(1,'#1c2c48')])
b+='<rect x="140" y="90" width="520" height="560" rx="10" fill="#0e1a30" stroke="#3a4a6a" stroke-width="16"/>'
b+='<rect x="160" y="110" width="480" height="520" fill="#1a3058"/>'+moon(520,230,46,'#e8eeff',.35)
b+=rain(90,4,'#bcd4ff',.5,4,630).replace('<path','<path clip-path="url(#win)"')
d+='<clipPath id="win"><rect x="160" y="110" width="480" height="520"/></clipPath>'
b+='<rect x="392" y="110" width="16" height="520" fill="#3a4a6a"/><rect x="160" y="362" width="480" height="16" fill="#3a4a6a"/>'
b+='<rect x="100" y="650" width="600" height="30" rx="8" fill="#2a3450"/>'
b+='<g fill="#070c18"><circle cx="300" cy="470" r="44"/><path d="M240 520 Q300 495 360 520 L390 650 L210 650Z"/><path d="M262 450 Q300 400 340 450 Q350 520 360 560 L330 540 Q320 480 300 470 Q280 480 270 540 L240 560 Q252 500 262 450Z"/></g>'
b+=glow(330,600,60,'#ff6a8a',.7)+heart(330,598,34,'#ff4f7a')
I[4]=svg(b,d)

# 5 Lose Yourself (Eminem, 2002): one shot — a lone hooded figure facing a single microphone in a hard white spotlight, Detroit factory stacks behind
d,b=bg([(0,'#050506'),(1,'#1a1a20')])
b+='<g fill="#16161c"><rect x="40" y="260" width="50" height="420"/><rect x="120" y="200" width="40" height="480"/><rect x="640" y="230" width="46" height="450"/><rect x="710" y="290" width="40" height="390"/></g>'
b+=spotlight(400,0,250,'#ffffff',.18,800)+glow(400,560,170,'#ffffff',.18)
b+=mic(400,250,100,'#d9d9e2')
b+='<g fill="#030304"><path d="M180 800 Q190 640 300 610 Q330 600 340 560 Q330 470 400 455 Q470 470 460 560 Q470 600 500 610 Q610 640 620 800Z"/></g>'
b+='<path d="M352 560 Q400 520 448 560" stroke="#2a2a30" stroke-width="5" fill="none"/>'
b+='<rect y="740" width="800" height="60" fill="#0a0a0c"/>'
I[5]=svg(b,d)

# 6 When Doves Cry (Prince, 1984): white doves bursting out of a royal purple sky, a purple-hued bathtub glow below
d,b=bg([(0,'#1a0630'),(.6,'#4a127a'),(1,'#8a2ab8')])
b+=rays(400,820,22,'#e6b0ff',.08,6,180,360)+glow(400,650,260,'#d27aff',.35)
def dove(x,y,s,rot):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s/100})"><path d="M-90 0 Q-40 -20 0 0 Q30 -10 60 -30 Q75 -20 70 -6 Q100 0 120 14 Q80 14 60 10 Q20 40 -30 30 Q-70 26 -90 0Z" fill="#fff"/>'
            f'<path d="M-20 -6 Q-60 -110 20 -150 Q10 -80 30 -10Z" fill="#f4eefc"/><path d="M0 0 Q30 -100 110 -110 Q60 -50 40 6Z" fill="#fff"/><circle cx="62" cy="-20" r="3" fill="#2a0a3a"/></g>')
b+=dove(400,360,190,-12)+dove(200,560,110,8)+dove(620,580,100,-20)+dove(250,200,70,-25)+dove(600,190,64,10)
I[6]=svg(b,d)

# 7 Billie Jean (Michael Jackson, 1982): a dark street where each sidewalk tile lights up under a figure's white socks and black loafers
d,b=bg([(0,'#07070c'),(1,'#141420')])
b+=skyline(380,'#0e0e16',7,60,200,'#ffe7a0',40)
for r_ in range(5):
    for c in range(-3,4):
        y0=420+r_**1.5*55;y1=420+(r_+1)**1.5*55;w0=110+r_*40;w1=110+(r_+1)*40
        x0=400+c*w0;x1=400+c*w1
        lit=(r_,c) in [(2,0),(3,1),(1,-1),(4,0),(2,2),(3,-2)]
        col=['#ffffff','#ffd84a','#ff6ad5','#5ae0ff'][(r_+c)%4] if lit else '#1a1a26'
        b+=f'<polygon points="{x0-w0/2+4:.0f},{y0+3:.0f} {x0+w0/2-4:.0f},{y0+3:.0f} {x1+w1/2-4:.0f},{y1-3:.0f} {x1-w1/2+4:.0f},{y1-3:.0f}" fill="{col}" opacity="{.9 if lit else 1}"/>'
b+=glow(400,610,120,'#fff2b0',.35)
b+='<g fill="#050508"><rect x="345" y="380" width="44" height="200" rx="10"/><rect x="408" y="380" width="44" height="200" rx="10" transform="rotate(6 430 380)"/></g>'
b+='<rect x="346" y="560" width="42" height="34" fill="#fff"/><rect x="420" y="560" width="42" height="34" fill="#fff" transform="rotate(6 440 560)"/>'
b+='<path d="M330 594 L392 594 Q404 618 380 622 L330 622Z" fill="#050508"/><path d="M418 600 L478 606 Q490 632 464 634 L414 628Z" fill="#050508"/>'
I[7]=svg(b,d)

# 8 Waterfalls (TLC, 1995): a tall turquoise waterfall plunging into a lagoon, three silhouettes standing on the shimmering water
d,b=bg([(0,'#04121e'),(.5,'#0a3a52'),(1,'#0e6a7a')])
d+=lg('fall',S((0,'#bff6ff'),(1,'#3ac0d8')),0,0,0,1)
b+='<path d="M0 0 L250 0 L270 520 L0 600Z" fill="#06202a"/><path d="M800 0 L540 0 L520 520 L800 600Z" fill="#06202a"/>'
b+='<path d="M260 0 L540 0 L530 520 L270 520Z" fill="url(#fall)"/>'
for k in range(16): b+=f'<line x1="{270+k*17}" y1="0" x2="{276+k*16}" y2="520" stroke="#fff" stroke-width="3" opacity=".35"/>'
b+='<ellipse cx="400" cy="530" rx="210" ry="40" fill="#e8ffff" opacity=".8" filter="url(#glow2)"/>'
b+='<rect y="540" width="800" height="260" fill="#0a4a5a"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="3" fill="#9ff0ff" opacity=".5"/>' for x,y,w in [(80,600,70),(500,620,90),(250,690,60),(620,720,80),(140,760,90),(380,580,50)])
for x,h in [(310,230),(400,250),(490,230)]: b+=figure(x,735,h,'#03141c',hair='#03141c')
I[8]=svg(b,d)

# 9 No Scrubs (TLC, 1999): a raised palm saying no in front of a silver-blue sci-fi corridor, a lonely car with a guy hanging out the passenger window
d,b=bg([(0,'#0a0f1e'),(1,'#2a4a7a')])
for k in range(7):
    s=1-k*.13;b+=f'<rect x="{400-360*s:.0f}" y="{400-330*s:.0f}" width="{720*s:.0f}" height="{660*s:.0f}" rx="{40*s:.0f}" fill="none" stroke="#9ad6ff" stroke-width="{6*s+1:.1f}" opacity="{.15+k*.08:.2f}"/>'
b+=glow(400,400,200,'#7ac8ff',.35)
b+='<g transform="translate(400 420)"><path d="M-110 260 L-110 40 Q-150 -40 -140 -60 Q-120 -80 -96 -50 L-80 -10 L-80 -190 Q-80 -215 -58 -215 Q-36 -215 -36 -190 L-36 -60 L-30 -60 L-30 -240 Q-30 -265 -6 -265 Q18 -265 18 -240 L18 -60 L26 -60 L26 -215 Q26 -240 50 -240 Q72 -240 72 -215 L72 -50 L80 -50 L80 -160 Q80 -182 100 -182 Q120 -182 120 -160 L120 60 Q120 160 60 200 L60 260Z" fill="#e7eefc"/>'
b+='<path d="M-110 260 L-110 40 Q-150 -40 -140 -60" fill="none" stroke="#9fb6dc" stroke-width="5"/></g>'
b+='<circle cx="400" cy="420" r="300" fill="none" stroke="#ff3a5a" stroke-width="26" opacity=".9"/><line x1="188" y1="208" x2="612" y2="632" stroke="#ff3a5a" stroke-width="26" opacity=".9"/>'
I[9]=svg(b,d)

# 10 The Twist (Chubby Checker, 1960): two dancers twisting low on a checkered sock-hop floor under a jukebox glow
d,b=bg([(0,'#2a0a3a'),(1,'#ff6a5a')])
b+=glow(400,300,240,'#ffd06a',.4)+jukebox(400,420,90)
for r_ in range(6):
    for c in range(-6,7):
        y0=470+r_*55;x0=400+c*(70+r_*14);w=70+r_*14
        b+=f'<rect x="{x0-w/2:.0f}" y="{y0}" width="{w:.0f}" height="55" fill="{"#111" if (r_+c)%2 else "#f4efe6"}"/>'
def twister(x,y,s,col,flip=1):
    return (f'<g transform="translate({x} {y}) scale({s*flip/100} {s/100})" fill="{col}"><circle cx="10" cy="-300" r="26"/><path d="M-18 -270 Q20 -280 36 -262 L50 -170 Q30 -150 -10 -160 Z"/>'
            f'<path d="M-10 -160 L50 -170 Q70 -120 40 -90 L80 -20 L60 0 L10 -80 L-30 -40 L-20 0 L-50 0 L-60 -60 Z"/>'
            f'<path d="M30 -255 Q90 -250 110 -210" stroke="{col}" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M-10 -255 Q-70 -230 -90 -270" stroke="{col}" stroke-width="16" fill="none" stroke-linecap="round"/></g>')
b+=twister(250,760,120,'#120414')+twister(560,760,120,'#120414',-1)
b+='<g transform="translate(560 760) scale(-1.2 1.2)"><path d="M-60 -60 Q-80 -20 -110 -10 L-40 -10Z" fill="#e8204a"/></g>'
I[10]=svg(b,d)

# 11 American Pie (Don McLean, 1971): a Chevy parked by a dry levee at dusk, a lone guitar on the hood — the day the music died
d,b=bg([(0,'#1a1430'),(.55,'#c0563a'),(1,'#f0b25a')])
b+=glow(560,430,160,'#ffd27a',.55)+'<circle cx="560" cy="440" r="70" fill="#ffd9a0"/>'
b+=hills(470,20,'#5a2a24',11,4)+'<path d="M-10 520 Q200 490 420 520 Q620 548 810 510 L810 800 L-10 800Z" fill="#3a1a1a"/>'
b+='<path d="M-10 600 Q250 560 520 600 Q680 625 810 600 L810 640 Q640 660 500 640 Q250 600 -10 645Z" fill="#a07a5a" opacity=".6"/>'
b+=car(380,700,150,'#d8d3c8','#f0eadf',glass='#f6c08a')
b+=guitar(360,555,45,'#8a3a1a','#2a1408',rot=74)
for x in (120,180,660,720): b+=f'<path d="M{x} 520 L{x+4} 470 L{x+8} 520" stroke="#1a0c0c" stroke-width="3" fill="none"/>'
I[11]=svg(b,d)

# 12 Le Freak (Chic, 1978): a giant disco ball over a Studio 54-style dance floor, light beams and two dancers in freeze-frame
d,b=bg([(0,'#0a0418'),(1,'#3a0a4a')])
for k,c in enumerate(['#ff4fa8','#4fd8ff','#ffe14f','#a86bff','#ff7a3a']): b+=f'<polygon points="400,230 {60+k*170},800 {130+k*170},800" fill="{c}" opacity=".16"/>'
b+=disco(400,230,120)+glow(400,230,180,'#ffffff',.18)
for x,y in [(250,150),(560,140),(150,320),(660,330)]: b+=sparkle(x,y,14,'#fff')
for r_ in range(3):
    for c in range(-5,6): b+=f'<rect x="{400+c*(90+r_*30)-(45+r_*15):.0f}" y="{620+r_*60}" width="{88+r_*30:.0f}" height="58" fill="{["#ff4fa8","#4fd8ff","#ffe14f","#a86bff"][(r_+c)%4]}" opacity=".55"/>'
b+=figure(300,690,230,'#08020e',pose='up',hair='#08020e')+figure(510,690,240,'#08020e',pose='wave')
I[12]=svg(b,d)

# 13 Let's Get It On (Marvin Gaye, 1973): a candlelit velvet room, a vinyl spinning on a turntable, two wine glasses and a red rose
d,b=bg([(0,'#1a0408'),(1,'#5a0a1a')])
b+=glow(400,420,280,'#ff7a3a',.25)
b+='<rect x="90" y="500" width="620" height="200" rx="18" fill="#2a0c06"/><rect x="110" y="480" width="580" height="40" rx="10" fill="#3a1408"/>'
b+='<ellipse cx="380" cy="500" rx="210" ry="56" fill="#0c0c0e"/>'+''.join(f'<ellipse cx="380" cy="500" rx="{200-k*20}" ry="{52-k*5}" fill="none" stroke="#2a2a30" stroke-width="2"/>' for k in range(8))
b+='<ellipse cx="380" cy="500" rx="56" ry="16" fill="#d1201c"/><path d="M600 470 L560 420 L470 470" stroke="#bbb" stroke-width="8" fill="none"/>'
for x in (150,640):
    b+=f'<rect x="{x-14}" y="330" width="28" height="140" rx="6" fill="#f2e3c6"/><path d="M{x} 300 Q{x+14} 318 {x} 332 Q{x-14} 318 {x} 300Z" fill="#ffc04a"/>'+glow(x,310,50,'#ffb04a',.6)
b+=heart(400,250,70,'#c8102e','opacity=".85"')
I[13]=svg(b,d)

# 14 Crazy in Love (Beyoncé ft. Jay-Z, 2003): a woman strutting down an empty street in white tank top and heels, a car bursting into flames behind her
d,b=bg([(0,'#3a1a08'),(.6,'#e0802a'),(1,'#ffd27a')])
b+=glow(560,420,220,'#ffb02a',.65)
for k in range(12):
    a=math.radians(200+k*12);L=140+(k%3)*40
    b+=f'<path d="M560 470 Q{560+L*.5*math.cos(a):.0f} {470+L*.6*math.sin(a):.0f} {560+L*math.cos(a):.0f} {470+L*math.sin(a):.0f}" stroke="{["#ff4a1a","#ffb02a","#ffe27a"][k%3]}" stroke-width="22" fill="none" stroke-linecap="round" opacity=".85"/>'
b+=car(560,560,110,'#2a1408','#5a3a2a',glass='#ffb04a')
b+='<rect y="560" width="800" height="240" fill="#7a4a2a"/><path d="M0 680 L800 640 L800 660 L0 700Z" fill="#c8a07a" opacity=".5"/>'
b+='<g transform="translate(270 770)"><circle cx="0" cy="-330" r="26" fill="#2a1408"/><path d="M-30 -350 Q0 -400 40 -350 Q70 -300 50 -250 L30 -280 Q20 -330 0 -330Z" fill="#c8862a"/>'
b+='<path d="M-30 -300 L30 -300 L34 -200 L-34 -200Z" fill="#fff"/><path d="M-36 -200 L36 -200 L40 -150 L-40 -150Z" fill="#3a5aa8"/>'
b+='<path d="M-36 -150 L-8 -150 L-40 0 L-58 0Z M10 -150 L38 -150 L60 -20 L42 -16Z" fill="#c07a4a"/><path d="M-62 0 L-30 0 L-34 -10 Z M38 -16 L72 -12 L64 -26Z" fill="#c8102e"/>'
b+='<path d="M-30 -295 Q-60 -250 -70 -200" stroke="#c07a4a" stroke-width="13" fill="none" stroke-linecap="round"/><path d="M30 -295 Q55 -260 60 -210" stroke="#c07a4a" stroke-width="13" fill="none" stroke-linecap="round"/></g>'
I[14]=svg(b,d)

# 15 ...Baby One More Time (Britney Spears, 1998): a school hallway of lockers, a girl with pink-ribboned pigtails in a cardigan mid-dance
d,b=bg([(0,'#2a3a6a'),(1,'#8aa0d8')])
b+='<polygon points="0,0 800,0 520,300 280,300" fill="#e6e9f2"/><polygon points="280,300 520,300 800,800 0,800" fill="#c8b48a"/>'
for side in (-1,1):
    for k in range(6):
        x0=400+side*(130+k*55);x1=400+side*(130+(k+1)*55)
        b+=f'<polygon points="{x0},{300-k*28-60} {x1},{300-(k+1)*28-60} {x1},{480+(k+1)*52} {x0},{480+k*52}" fill="{"#3a7ad8" if k%2 else "#2a62bc"}" stroke="#1a3a7a" stroke-width="3"/>'
b+='<g transform="translate(400 740)"><circle cx="0" cy="-310" r="30" fill="#f2c9a6"/><path d="M-32 -320 Q0 -360 32 -320 L28 -300 Q0 -320 -28 -300Z" fill="#c8a050"/>'
b+='<path d="M-30 -315 Q-70 -300 -60 -250 L-48 -252 Q-56 -290 -26 -300Z M30 -315 Q70 -300 60 -250 L48 -252 Q56 -290 26 -300Z" fill="#c8a050"/><circle cx="-36" cy="-312" r="9" fill="#ff7ab8"/><circle cx="36" cy="-312" r="9" fill="#ff7ab8"/>'
b+='<path d="M-34 -276 L34 -276 L40 -180 L-40 -180Z" fill="#5a5a6a"/><path d="M-12 -276 L12 -276 L4 -200 L-4 -200Z" fill="#fff"/><path d="M-44 -180 L44 -180 L56 -120 L-56 -120Z" fill="#5a5a6a"/>'
b+='<path d="M-44 -180 L44 -180 L56 -120 L-56 -120Z" fill="none" stroke="#2a2a3a" stroke-width="3"/><rect x="-26" y="-120" width="16" height="104" fill="#f2c9a6"/><rect x="10" y="-120" width="16" height="104" fill="#f2c9a6"/>'
b+='<rect x="-28" y="-50" width="20" height="40" fill="#eee"/><rect x="8" y="-50" width="20" height="40" fill="#eee"/><path d="M-32 -12 L-6 -12 L-6 0 L-36 0Z M6 -12 L32 -12 L36 0 L6 0Z" fill="#111"/>'
b+='<path d="M-34 -268 Q-80 -240 -90 -300" stroke="#5a5a6a" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M34 -268 Q60 -230 50 -200" stroke="#5a5a6a" stroke-width="16" fill="none" stroke-linecap="round"/></g>'
I[15]=svg(b,d)

# 16 Light My Fire (The Doors, 1967): a huge psychedelic flame rising from a single match against swirling purple and orange
d,b=bg([(0,'#1a0420'),(1,'#5a0a2a')])
for k in range(10): b+=f'<circle cx="400" cy="480" r="{380-k*36}" fill="{["#3a0a4a","#5a1250","#8a1a3a","#b0301a","#d8601a"][k%5]}" opacity=".35"/>'
d+=lg('fl',S((0,'#fff6a0'),(.4,'#ffb02a'),(.8,'#ff4a1a'),(1,'#c8102e')),0,0,0,1)
b+='<path d="M400 120 Q520 260 480 380 Q560 340 540 260 Q640 400 560 540 Q520 620 400 630 Q280 620 240 540 Q160 400 260 260 Q240 340 320 380 Q280 260 400 120Z" fill="url(#fl)"/>'
b+='<path d="M400 300 Q460 380 440 460 Q480 440 470 400 Q520 480 470 560 Q440 600 400 600 Q350 600 330 560 Q290 480 340 410 Q340 450 370 460 Q350 380 400 300Z" fill="#fff8c8"/>'
b+='<rect x="388" y="600" width="24" height="190" fill="#e8d0a0"/><ellipse cx="400" cy="604" rx="20" ry="14" fill="#8a1a10"/>'
I[16]=svg(b,d)

# 17 I Will Survive (Gloria Gaynor, 1978): a woman throwing an arm up in a disco spotlight, the front door wide open with the old key on the floor
d,b=bg([(0,'#12041e'),(1,'#5a0a5a')])
b+='<rect x="520" y="200" width="200" height="440" fill="#2a0a2a"/><path d="M520 200 L620 230 L620 670 L520 640Z" fill="#8a3a6a"/><rect x="520" y="200" width="200" height="440" fill="none" stroke="#c8a0c8" stroke-width="8"/>'
b+='<path d="M545 230 L700 230 L700 620 L545 620Z" fill="#ffd2a0" opacity=".25"/>'
b+=spotlight(300,0,220,'#ffe6ff',.22,800)+glow(300,560,180,'#ff7ad8',.3)
b+=figure(300,720,380,'#0a0210',pose='up',hair='#0a0210')
b+='<g transform="translate(560 740) rotate(-20)"><circle cx="0" cy="0" r="18" fill="none" stroke="#ffd04a" stroke-width="8"/><rect x="16" y="-5" width="60" height="10" fill="#ffd04a"/><rect x="58" y="5" width="8" height="12" fill="#ffd04a"/><rect x="70" y="5" width="6" height="8" fill="#ffd04a"/></g>'
b+='<rect y="740" width="800" height="60" fill="#1a041a"/>'
I[17]=svg(b,d)

# 18 Lean on Me (Bill Withers, 1972): two friends walking toward a sunrise, one with his arm over the other's shoulder for support
d,b=bg([(0,'#1a2a5a'),(.55,'#e08a5a'),(1,'#ffd88a')])
b+=glow(400,520,200,'#ffe2a0',.7)+'<circle cx="400" cy="540" r="90" fill="#fff0c8"/>'
b+=hills(560,30,'#5a3a4a',18,4)+hills(620,25,'#3a2434',19,3)+'<rect y="660" width="800" height="140" fill="#24161e"/>'
b+='<g fill="#0e080c"><circle cx="350" cy="430" r="26"/><path d="M322 460 Q350 448 378 460 L384 580 L376 690 L360 690 L352 600 L346 690 L330 690 L318 580Z"/>'
b+='<circle cx="450" cy="440" r="25"/><path d="M424 468 Q450 456 476 468 L482 584 L474 690 L458 690 L452 604 L444 690 L428 690 L418 584Z"/>'
b+='<path d="M372 470 Q420 440 470 470" stroke="#0e080c" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M470 470 L480 500" stroke="#0e080c" stroke-width="16" stroke-linecap="round"/>'
b+='<path d="M330 470 Q300 520 310 570" stroke="#0e080c" stroke-width="16" fill="none" stroke-linecap="round"/></g>'
I[18]=svg(b,d)

# 19 Hey Ya! (OutKast, 2003): an instant photo being shaken like a Polaroid picture, motion lines and a bright candy-colored stage
d,b=bg([(0,'#1a6a4a'),(1,'#f0d24a')])
for k in range(12): b+=f'<rect x="{k*70-10}" y="0" width="34" height="800" fill="{["#ff4a6a","#4ad8ff","#ffe14a","#7a4aff"][k%4]}" opacity=".18"/>'
b+='<g transform="translate(400 400) rotate(-12)">'
for k in (3,2,1): b+=f'<rect x="{-170+k*26}" y="-200" width="340" height="400" rx="10" fill="#fff" opacity="{.18*k/3+.05:.2f}"/>'
b+='<rect x="-170" y="-200" width="340" height="400" rx="10" fill="#fbfbf6"/><rect x="-145" y="-175" width="290" height="290" fill="#2a2a3a"/>'
b+='<rect x="-145" y="-175" width="290" height="290" fill="#6a4a8a" opacity=".6"/>'+glow(0,-30,90,'#ffd0f0',.6)+'<circle cx="0" cy="-30" r="40" fill="#ffe6c0" opacity=".8"/></g>'
for k in range(5): b+=f'<path d="M{110-k*6} {200+k*90} q-40 20 -80 0" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".8"/><path d="M{700+k*6} {170+k*90} q40 20 80 0" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".8"/>'
I[19]=svg(b,d)

# 20 Single Ladies (Put a Ring on It) (Beyoncé, 2008): a black-and-white studio, a raised hand flashing a big diamond ring, three dancers in silhouette
d,b=bg([(0,'#f2f2f2'),(1,'#bdbdbd')])
b+='<rect y="600" width="800" height="200" fill="#d8d8d8"/>'
for x in (150,250,350): b+=figure(x,760,210,'#111',pose='up',hair='#111')
b+='<g transform="translate(560 800)"><path d="M-70 0 L-60 -260 Q-80 -320 -60 -330 L-40 -300 L-46 -430 Q-46 -450 -28 -450 Q-10 -450 -10 -430 L-6 -330 L2 -330 L0 -470 Q0 -490 18 -490 Q36 -490 36 -470 L36 -330 L44 -330 L46 -450 Q46 -468 62 -468 Q78 -468 78 -450 L76 -320 L82 -320 L86 -400 Q88 -416 102 -416 Q116 -416 114 -400 L106 -230 Q100 -150 50 -120 L50 0Z" fill="#111"/>'
b+='<rect x="44" y="-372" width="36" height="12" rx="5" fill="#d8d8d8"/></g>'
b+=glow(622,404,46,'#ffffff',.9)
b+='<path d="M622 380 L646 398 L622 428 L598 398Z" fill="#fff" stroke="#9ad" stroke-width="3"/><path d="M600 398 L644 398" stroke="#9ad" stroke-width="2"/>'+sparkle(676,350,22,'#fff')+sparkle(580,345,12,'#fff')
I[20]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
