import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 19. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 944 Secret Code: a glowing combination padlock with a keyhole of light, binary digits drifting in the dark
d,b=bg([(0,'#0a1020'),(1,'#1a2a4a')])
b+=''.join(f'<text x="{60+(k*97)%700}" y="{140+(k*61)%620}" font-family="monospace" font-size="34" fill="#4ad8ff" opacity=".25">{(k*7)%2}</text>' for k in range(40))
b+='<path d="M300 380 L300 300 Q300 200 400 200 Q500 200 500 300 L500 380" stroke="#c8d0e0" stroke-width="34" fill="none"/><rect x="250" y="370" width="300" height="280" rx="34" fill="#e8b830"/><rect x="250" y="370" width="300" height="40" rx="20" fill="#ffd860"/>'
b+=glow(400,500,90,'#9af0ff',.6)+'<circle cx="400" cy="480" r="30" fill="#0a1020"/><path d="M386 490 L414 490 L424 580 L376 580Z" fill="#0a1020"/>'
I[944]=svg(b,d)

# 1166 My Generation: a girl with an acoustic guitar on a school rooftop at sunrise, a paper plane flying off
d,b=bg([(0,'#ffb27a'),(.6,'#ffe2b0'),(1,'#a8d0f0')])
b+=hinomaru_sun(560,420,110,'#fff4c8',.9)+'<rect y="560" width="800" height="240" fill="#8a8a96"/><rect y="440" width="800" height="8" fill="#4a4a5a"/>'+''.join(f'<rect x="{k*50}" y="440" width="6" height="120" fill="#4a4a5a"/>' for k in range(17))
b+=figure(300,690,280,'#1a1a2a',pose='hold')+guitar(300,560,.8,-20,'#c8702a')+'<path d="M560 200 L660 230 L580 250 Z" fill="#fff"/><path d="M580 250 L600 236" stroke="#c8c8d0" stroke-width="3"/>'
I[1166]=svg(b,d)

# 1380 キュン: a big pink heart giving a single throb, with motion lines and a sky-blue background
d,b=bg([(0,'#8ad8ff'),(1,'#e8f8ff')])
b+=''.join(ring(400,430,190+k*60,'#ff8ab8',6,.5-k*.12) for k in range(4))+heart(400,430,170,'#ff5a9a')+sparkle(560,260,26,'#fff')+sparkle(250,580,18,'#fff')
b+='<text x="400" y="440" text-anchor="middle" font-family="Noto Sans JP" font-weight="700" font-size="72" fill="#fff">キュン</text>'
I[1380]=svg(b,d)

# 1629 Missing: an empty chair by a window at night, a jigsaw puzzle with one piece missing on the table
d,b=bg([(0,'#10142a'),(1,'#2a2e4a')])
b+='<rect x="460" y="120" width="260" height="320" fill="#1a2a5a"/>'+moon(600,230,46)+'<rect x="460" y="120" width="260" height="320" fill="none" stroke="#3a3e5a" stroke-width="14"/><path d="M590 120 L590 440 M460 280 L720 280" stroke="#3a3e5a" stroke-width="10"/>'
b+='<rect y="600" width="800" height="200" fill="#2a2030"/><rect x="100" y="520" width="360" height="24" fill="#6a4a3a"/><rect x="120" y="544" width="16" height="200" fill="#4a3a2a"/><rect x="424" y="544" width="16" height="200" fill="#4a3a2a"/>'
b+=''.join(f'<rect x="{150+(k%4)*64}" y="{470+(k//4)*0}" width="60" height="44" fill="#e8c86a" stroke="#a8884a" stroke-width="3"/>' for k in range(4) if k!=2)+'<rect x="278" y="470" width="60" height="44" fill="none" stroke="#a8884a" stroke-width="3" stroke-dasharray="6 4"/>'
b+='<path d="M560 740 L560 600 L660 600 L660 500 M560 660 L700 660 L700 740" stroke="#7a6a5a" stroke-width="14" fill="none"/>'
I[1629]=svg(b,d)

# 178 なみだの操: a woman in kimono seen from behind under a red paper lantern, one tear-shaped drop of light
d,b=bg([(0,'#3a1020'),(1,'#1a0810')])
b+=chochin(560,250,1.1,'#d8342c','#ffb070','操')+'<rect y="640" width="800" height="160" fill="#2a1418"/>'
b+='<g fill="#0a0408"><ellipse cx="320" cy="300" rx="44" ry="50"/><circle cx="320" cy="245" r="34"/><path d="M250 680 Q240 470 280 360 Q320 340 360 360 Q400 470 390 680Z"/></g><rect x="268" y="470" width="104" height="40" fill="#8a1a2a"/>'
b+='<path d="M420 400 Q440 440 420 456 Q400 440 420 400Z" fill="#c8e8ff" opacity=".9"/>'
I[178]=svg(b,d)

# 435 Song for U.S.A.: a vintage jukebox glowing on a long American highway at dusk, stars above
d,b=bg([(0,'#1a1a4a'),(.6,'#e8603a'),(1,'#ffb060')])
b+=starsf(40,435,300)+'<path d="M0 560 L800 560 L800 800 L0 800Z" fill="#3a2a2a"/><path d="M380 560 L420 560 L560 800 L240 800Z" fill="#2a2228"/><path d="M398 600 L402 600 L408 660 L392 660Z M396 700 L404 700 L412 780 L388 780Z" fill="#ffd860"/>'
b+='<path d="M130 560 L130 360 Q130 260 230 260 Q330 260 330 360 L330 560Z" fill="#c8302a"/><path d="M160 370 Q160 300 230 300 Q300 300 300 370 L300 430 L160 430Z" fill="#ffd27a"/>'+glow(230,370,90,'#ffd27a',.5)+''.join(f'<rect x="{165+k*28}" y="460" width="18" height="70" fill="#2a1a1a"/>' for k in range(5))
b+=star5(620,180,40,'#fff')+star5(700,260,24,'#fff')
I[435]=svg(b,d)

# 827 Desire: a single red rose bursting through cracked black stone, a beam of crimson light
d,b=bg([(0,'#050508'),(1,'#1a0a14')])
b+='<polygon points="340,0 460,0 520,800 280,800" fill="#c8102a" opacity=".2"/><rect y="560" width="800" height="240" fill="#141418"/>'+bolt([(400,560),(360,640),(420,700),(380,800)],'#3a3a44',6)+bolt([(400,560),(480,620),(460,700),(520,800)],'#3a3a44',6)
b+='<path d="M400 560 Q390 470 400 400" stroke="#2a5a2a" stroke-width="10" fill="none"/>'+rose(400,380,1.8,0)+glow(400,380,120,'#ff2a4a',.4)
I[827]=svg(b,d)

# 868 Pieces: a heart made of floating mirror shards reflecting a starlit sky
d,b=bg([(0,'#1a1440'),(1,'#4a3a7a')])
b+=starsf(60,868,800)
import random
r=random.Random(868)
for k in range(48):
    a=r.uniform(0,6.28);rr=r.uniform(0,1)
    x=400+16*math.sin(a)**3*17*(.55+.45*rr);y=400-(13*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)-math.cos(4*a))*17*(.55+.45*rr)
    s=r.uniform(26,50);ang=r.uniform(0,360)
    b+=f'<polygon points="{x:.0f},{y-s:.0f} {x+s*.8:.0f},{y+s*.4:.0f} {x-s*.6:.0f},{y+s*.6:.0f}" fill="#c8d8ff" opacity="{r.uniform(.5,.95):.2f}" stroke="#fff" stroke-width="2" transform="rotate({ang:.0f} {x:.0f} {y:.0f})"/>'
I[868]=svg(b,d)

# 1005 Free & Easy: a figure on a cliff edge with arms spread, a white dove and long scarf flying in the wind
d,b=bg([(0,'#5ab0f0'),(1,'#d8f0ff')])
b+=cloud(250,200,1.8)+cloud(600,320,1.4)+'<path d="M-10 640 L520 600 Q560 640 540 800 L-10 800Z" fill="#4a5a4a"/>'
b+=figure(400,610,270,'#1a1a24',pose='up')+'<path d="M400 380 Q520 360 620 400 Q700 430 780 390" stroke="#f4f4ff" stroke-width="14" fill="none" stroke-linecap="round"/>'+bird(640,220,2.2,'#fff',3)
I[1005]=svg(b,d)

# 1234 Power of the Paradise: a golden laurel ring around a rising sun over a stadium, five beams of colour
d,b=bg([(0,'#0a2a5a'),(1,'#3a6ab8')])
b+=rays(400,520,30,'#ffd860',.18,10)+''.join(f'<polygon points="400,520 {400+600*math.cos(math.radians(a-4)):.0f},{520-600*math.sin(math.radians(a-4)):.0f} {400+600*math.cos(math.radians(a+4)):.0f},{520-600*math.sin(math.radians(a+4)):.0f}" fill="{c}" opacity=".35"/>' for a,c in [(30,'#3a8af8'),(60,'#e8302a'),(90,'#2ad86a'),(120,'#ffd02a'),(150,'#b84af8')])
b+=hinomaru_sun(400,520,110,'#ffe080')+'<path d="M-10 640 Q400 560 810 640 L810 810 L-10 810Z" fill="#1a3a2a"/>'
for s in (-1,1): b+=''.join(f'<ellipse cx="{400+s*150*math.cos(math.radians(a)):.0f}" cy="{520-150*math.sin(math.radians(a)):.0f}" rx="12" ry="26" fill="#ffd02a" transform="rotate({s*(90-a)} {400+s*150*math.cos(math.radians(a)):.0f} {520-150*math.sin(math.radians(a)):.0f})"/>' for a in range(-10,80,14))
I[1234]=svg(b,d)

# 1486 Let the Night: a girl lying on a rooftop under a deep violet night, city lights below and one shooting star
d,b=bg([(0,'#100a2a'),(1,'#3a2a6a')])
b+=starsf(70,1486,560)+'<path d="M640 120 L480 230" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'+glow(640,120,30,'#fff',.6)
b+=skyline(700,'#1a1430',1486,40,160,'#ffd27a',80)+'<rect y="560" width="800" height="40" fill="#2a2240"/>'
b+='<g fill="#0a0814"><circle cx="230" cy="535" r="26"/><path d="M256 540 L560 540 Q570 556 560 562 L256 562Z"/></g><path d="M210 540 Q180 560 160 570" stroke="#0a0814" stroke-width="14" stroke-linecap="round"/>'
I[1486]=svg(b,d)

# 1605 HELLO HELLO: a bright yellow vintage telephone receiver with speech bubbles popping out on a teal background
d,b=bg([(0,'#2ad8c8'),(1,'#a8f8e8')])
b+='<path d="M220 560 Q160 420 260 330 L320 380 Q290 440 320 500 L380 470 L430 560 Q340 640 220 560Z" fill="#ffd02a" stroke="#c89a10" stroke-width="8"/>'
b+='<g><rect x="430" y="180" width="300" height="140" rx="70" fill="#fff"/><path d="M480 310 L450 370 L530 318Z" fill="#fff"/><text x="580" y="270" text-anchor="middle" font-family="Noto Sans JP" font-weight="700" font-size="58" fill="#1a8a8a">HELLO</text></g>'
b+='<g><rect x="460" y="400" width="240" height="110" rx="55" fill="#ff6a9a"/><text x="580" y="472" text-anchor="middle" font-family="Noto Sans JP" font-weight="700" font-size="46" fill="#fff">HELLO</text></g>'
I[1605]=svg(b,d)

# 1615 恋降る月夜に君想ふ: a young man in a yukata under a huge full moon, petals of light falling like rain
d,b=bg([(0,'#0a1438'),(1,'#2a3a7a')])
b+=moon(520,260,150,'#fff4d0',.5)+petals(40,1615,'#fff0c8',0,800,6,14,.7)+'<rect y="660" width="800" height="140" fill="#0a0e24"/>'
b+=figure(300,700,330,'#05081a')+'<path d="M272 540 L328 540 L334 600 L266 600Z" fill="#3a4a8a" opacity=".6"/>'
I[1615]=svg(b,d)

# 1630 Spacecraft: a sleek silver spaceship launching from the sea into a starry sky, a long bright trail
d,b=bg([(0,'#020210'),(.7,'#1a1a4a'),(1,'#3a4a8a')])
b+=starsf(80,1630,700)+'<rect y="660" width="800" height="140" fill="#0a1430"/>'+'<path d="M420 660 Q400 520 470 300" stroke="#ffd27a" stroke-width="30" fill="none" opacity=".35"/><path d="M420 660 Q400 520 470 300" stroke="#fff" stroke-width="8" fill="none"/>'
b+='<g transform="rotate(20 500 220)"><path d="M500 80 Q540 150 540 260 L460 260 Q460 150 500 80Z" fill="#d8dce8"/><path d="M460 230 L420 290 L460 270Z M540 230 L580 290 L540 270Z" fill="#8a90a8"/><circle cx="500" cy="170" r="16" fill="#4ad8ff"/></g>'
I[1630]=svg(b,d)

# 662 May: a single green young leaf with a dew drop under fresh May sunlight, carp streamers far behind
d,b=bg([(0,'#9ae0ff'),(1,'#e8fff0')])
b+=hinomaru_sun(640,140,70,'#fff8c8',.9)+'<path d="M140 120 L140 520" stroke="#8a6a4a" stroke-width="6"/>'+''.join(f'<path d="M140 {150+k*70} Q220 {130+k*70} 300 {160+k*70} L280 {180+k*70} Q220 {200+k*70} 140 {190+k*70}Z" fill="{c}"/>' for k,c in enumerate(['#1a3a8a','#e8302a','#ff8ab8']))
b+='<path d="M400 720 Q380 560 470 420 Q560 300 650 330 Q650 470 560 580 Q480 680 400 720Z" fill="#4ac84a"/><path d="M400 720 Q500 520 650 330" stroke="#2a8a2a" stroke-width="6" fill="none"/><ellipse cx="520" cy="520" rx="18" ry="22" fill="#e8fbff" stroke="#fff" stroke-width="3"/>'
I[662]=svg(b,d)

# 1034 アイノカタチ: two hands shaping a heart of warm light, sparkles rising gently
d,b=bg([(0,'#f8d8c8'),(1,'#fff4ea')])
b+=glow(400,400,240,'#ffb08a',.5)+heart(400,400,110,'#ff8a8a')+sparkle(300,240,18,'#fff')+sparkle(520,220,24,'#fff')+sparkle(560,330,14,'#fff')
b+='<g fill="#e8b098" stroke="#c8907a" stroke-width="4"><path d="M220 700 Q200 540 290 470 Q320 440 340 470 Q360 520 330 560 Q300 600 320 700Z"/><path d="M580 700 Q600 540 510 470 Q480 440 460 470 Q440 520 470 560 Q500 600 480 700Z"/></g>'
I[1034]=svg(b,d)

# 1048 思いがかさなるその前に: two shadows on a pavement just about to overlap, cherry petals blowing between
d,b=bg([(0,'#ffd2a8'),(1,'#fff0d8')])
b+='<rect y="480" width="800" height="320" fill="#d8c0a8"/>'+''.join(f'<path d="M0 {500+k*60} L800 {500+k*60}" stroke="#c8ae94" stroke-width="3"/>' for k in range(5))
b+='<path d="M250 500 L380 760 L320 760 Z" fill="#8a6a5a" opacity=".5"/><path d="M550 500 L420 760 L480 760 Z" fill="#8a6a5a" opacity=".5"/>'+figure(250,500,220,'#3a2a2a')+figure(550,500,230,'#3a2a2a')+petals(14,1048,'#ffc2d6',260,560,8,14)
I[1048]=svg(b,d)

# 1087 BLUE BE-BOP: a turntable spinning a blue vinyl record, a microphone and graffiti-style blue stars
d,b=bg([(0,'#0a2a6a'),(1,'#1a5ab8')])
b+=''.join(star5(x,y,s,'#4ad8ff') for x,y,s in [(140,220,30),(660,180,22),(680,600,34)])
b+='<rect x="140" y="320" width="520" height="380" rx="24" fill="#1a1a24"/><circle cx="380" cy="510" r="160" fill="#1a6ae8"/>'+''.join(ring(380,510,60+k*24,'#0a4ab8',2,.8) for k in range(4))+'<circle cx="380" cy="510" r="40" fill="#fff"/><circle cx="380" cy="510" r="8" fill="#1a1a24"/><path d="M600 360 L600 470 L470 560" stroke="#c8c8d0" stroke-width="10" fill="none" stroke-linecap="round"/>'
I[1087]=svg(b,d)

# 1139 遥か彼方: a boy running toward a far horizon along a long road, the sky wide open
d,b=bg([(0,'#3a8af8'),(.6,'#a8d8ff'),(1,'#f8f0d8')])
b+=cloud(200,160,1.6)+cloud(620,220,1.3)+'<rect y="500" width="800" height="300" fill="#8ab84a"/><path d="M396 500 L404 500 L640 800 L160 800Z" fill="#8a8a8a"/><path d="M400 500 L400 800" stroke="#fff" stroke-width="6" stroke-dasharray="30 30"/>'
b+=figure(430,720,200,'#1a1a2a',pose='up')
I[1139]=svg(b,d)

# 1175 愛唄: a young couple's silhouettes sitting on a riverside embankment, music notes drifting over the water
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b8')])
b+=hinomaru_sun(560,360,90,'#fff2c8',.8)+'<rect y="440" width="800" height="120" fill="#e8a070"/><path d="M-10 560 L810 500 L810 810 L-10 810Z" fill="#5a8a3a"/>'
b+='<g fill="#2a1a1a"><circle cx="300" cy="460" r="22"/><path d="M276 480 Q300 470 324 480 L330 560 L270 560Z"/><circle cx="360" cy="456" r="22"/><path d="M336 476 Q360 466 384 476 L390 556 L330 556Z"/></g>'
b+=note(470,300,1.4,'#fff')+note(560,240,1,'#fff',True)+note(640,320,1.2,'#fff')
I[1175]=svg(b,d)

# 1269 ズッコケ男道: a man in a 70s suit slipping on a banana peel on a bright stage, comic stars around his head
d,b=bg([(0,'#ffd02a'),(1,'#ff8a2a')])
b+=rays(400,400,24,'#fff',.2,10)+'<rect y="640" width="800" height="160" fill="#c8302a"/>'
b+='<g transform="rotate(-25 400 560)">'+figure(400,640,300,'#1a1a3a',pose='up')+'</g>'+'<path d="M470 650 Q500 620 540 650 Q510 640 470 650Z" fill="#ffe04a" stroke="#c8a010" stroke-width="3"/>'
b+=''.join(star5(x,y,20,'#fff') for x,y in [(250,320),(300,280),(350,300)])
I[1269]=svg(b,d)

# 1845 麻痺: a figure dissolving into static and glitch blocks, monochrome with one red line
d,b=bg([(0,'#d8d8dc'),(1,'#8a8a90')])
r=random.Random(1845)
b+=''.join(f'<rect x="{r.randint(0,780)}" y="{r.randint(0,780)}" width="{r.randint(10,60)}" height="{r.randint(3,10)}" fill="#3a3a40" opacity="{r.uniform(.2,.6):.2f}"/>' for _ in range(120))
b+=figure(400,720,520,'#1a1a1e')+''.join(f'<rect x="{400+r.randint(-120,120)}" y="{r.randint(220,700)}" width="{r.randint(20,90)}" height="{r.randint(6,22)}" fill="#d8d8dc"/>' for _ in range(30))+'<rect y="430" width="800" height="8" fill="#e8102a"/>'
I[1845]=svg(b,d)

# 125 S・O・S: a lighthouse sending a rescue beam across a stormy sea, the beam forming three dots
d,b=bg([(0,'#1a2a4a'),(1,'#3a5a7a')])
b+=rain(60,125)+'<path d="M-10 600 Q100 560 200 600 Q300 640 400 600 Q500 560 600 600 Q700 640 810 600 L810 810 L-10 810Z" fill="#1a3a5a"/>'
b+='<path d="M560 600 L580 300 L640 300 L660 600Z" fill="#f4f0e8"/><path d="M566 500 L654 500 L650 540 L570 540Z M574 380 L646 380 L644 420 L576 420Z" fill="#d8342c"/><rect x="570" y="250" width="80" height="56" fill="#ffd860"/><path d="M560 250 L610 210 L660 250Z" fill="#d8342c"/>'
b+='<polygon points="610,278 40,180 40,380" fill="#fff6c8" opacity=".25"/>'+''.join(f'<circle cx="{x}" cy="280" r="18" fill="#fff6c8"/>' for x in (180,250,320))
I[125]=svg(b,d)

# 318 SPARKLE: a summer sea glittering under the sun, a guitar pick-shaped glint and a city-pop palm silhouette
d,b=bg([(0,'#1aa8f8'),(.55,'#8ae0ff'),(1,'#1a7ac8')])
b+=hinomaru_sun(400,250,80,'#fffbe0')+'<rect y="420" width="800" height="380" fill="#1a7ac8"/>'+''.join(sparkle(r2,a2,s2,'#fff') for r2,a2,s2 in [(200,480,22),(330,520,30),(470,470,26),(600,540,20),(400,600,34),(250,640,18),(560,680,24)])
b+='<path d="M120 800 Q140 600 110 420" stroke="#1a2a2a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M110 420 Q{110+dx} {420+dy} {110+dx*2} {440+dy*2}" stroke="#1a2a2a" stroke-width="12" fill="none" stroke-linecap="round"/>' for dx,dy in [(60,-20),(-50,-10),(40,30),(-30,40),(70,10)])
I[318]=svg(b,d)

# 436 俺たちのロカビリーナイト: a chequered dance floor with a pompadour silhouette, a jukebox glow and a 50s car tail fin
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a4a')])
b+=''.join(f'<rect x="{x*80}" y="{560+y*60}" width="80" height="60" fill="{"#f4f0e8" if (x+y)%2 else "#1a1a1a"}"/>' for x in range(10) for y in range(4))
b+=neon(400,200,'ROCK','#ff4fa0',110)+figure(400,600,330,'#0a0410',pose='wave')+'<path d="M378 288 Q400 250 440 270 Q430 290 400 292Z" fill="#0a0410"/>'
I[436]=svg(b,d)

# 516 Get Wild: a city at night seen from a rooftop, a lone gunman-like trench coat silhouette and a red moon
d,b=bg([(0,'#050a1a'),(1,'#1a2a4a')])
b+=moon(600,200,80,'#ff5a3a',.4)+skyline(660,'#0a1020',516,80,320,'#6ad8ff',140)+'<rect y="660" width="800" height="140" fill="#0a0a14"/>'
b+='<g fill="#000"><circle cx="260" cy="420" r="24"/><path d="M226 450 Q260 440 294 450 L320 680 L200 680Z"/></g><path d="M294 470 L340 520" stroke="#000" stroke-width="12" stroke-linecap="round"/>'
I[516]=svg(b,d)

# 573 Cecile: a French-style café terrace with a single rose in a glass, a pastel 80s idol palette
d,b=bg([(0,'#ffc8e0'),(1,'#fff0f6')])
b+='<path d="M80 200 L720 200 L680 300 L120 300Z" fill="#e8507a"/>'+''.join(f'<path d="M{120+k*80} 300 Q{160+k*80} 330 {200+k*80} 300" fill="#fff"/>' for k in range(7))
b+='<ellipse cx="400" cy="560" rx="200" ry="40" fill="#fff" stroke="#e8c0d0" stroke-width="4"/><rect x="390" y="560" width="20" height="200" fill="#c8c8d0"/>'
b+='<path d="M380 560 L374 440 L426 440 L420 560Z" fill="#e8f8ff" opacity=".8" stroke="#a8c8e8" stroke-width="3"/><path d="M400 440 L400 380" stroke="#2a8a2a" stroke-width="6"/>'+rose(400,370,1,0)
I[573]=svg(b,d)

# 663 さよなら傷だらけの日々よ: a battered guitar case left at a dawn crossroads, the sun breaking through
d,b=bg([(0,'#ff8a4a'),(.6,'#ffd09a'),(1,'#8a9ab8')])
b+=hinomaru_sun(400,440,120,'#fff2c8')+rays(400,440,20,'#fff',.15,8)+'<rect y="500" width="800" height="300" fill="#5a5a6a"/><path d="M0 640 L800 640" stroke="#f4f0e8" stroke-width="10" stroke-dasharray="40 30"/>'
b+='<g transform="rotate(-12 300 640)"><path d="M200 600 Q200 560 250 560 L380 560 Q420 540 440 580 L440 680 Q420 720 380 700 L250 700 Q200 700 200 660Z" fill="#2a1a14"/><path d="M240 600 L280 640 M330 580 L360 610 M300 660 L340 690" stroke="#c8a888" stroke-width="5"/></g>'
I[663]=svg(b,d)

# 743 君が好き: a phone screen glowing in a dark room with an unsent message, a single heart
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=glow(400,420,220,'#6ab8ff',.35)+'<rect x="290" y="180" width="220" height="440" rx="30" fill="#1a1a1a" stroke="#3a3a4a" stroke-width="6"/><rect x="306" y="210" width="188" height="380" rx="12" fill="#e8f4ff"/>'
b+='<rect x="330" y="470" width="140" height="44" rx="20" fill="#3aa0ff"/>'+heart(400,370,50,'#ff4a7a')+'<rect x="330" y="530" width="100" height="10" rx="5" fill="#a8c8e8"/>'
I[743]=svg(b,d)

# 817 君にサヨナラを: an empty station platform at dusk, a departing train's red tail lights and a raised hand
d,b=bg([(0,'#4a3a6a'),(.6,'#e88a6a'),(1,'#ffc8a0')])
b+='<rect y="520" width="800" height="280" fill="#5a5a64"/><rect y="510" width="800" height="14" fill="#ffd02a"/><path d="M0 600 L800 600 M0 640 L800 640" stroke="#3a3a40" stroke-width="6"/>'
b+='<path d="M540 420 L800 420 L800 600 L540 600Z" fill="#3a4a5a"/>'+''.join(f'<circle cx="{x}" cy="560" r="12" fill="#ff2a2a"/>' for x in (570,610))+glow(590,560,50,'#ff2a2a',.5)
b+=figure(260,520,260,'#1a1424',pose='wave')+'<path d="M80 100 L80 520 M80 120 L200 120" stroke="#2a2a30" stroke-width="10"/>'
I[817]=svg(b,d)

# 1069 飛べない鳥: a small bird standing on a fence looking up at a flock flying across a wide sky
d,b=bg([(0,'#7ac0f0'),(1,'#e0f4ff')])
b+=cloud(520,200,1.8)+''.join(bird(x,y,1.2,'#2a3a4a',3) for x,y in [(500,140),(560,120),(600,160),(660,130),(440,170)])+'<rect y="620" width="800" height="180" fill="#8ac06a"/>'
b+='<rect x="0" y="520" width="800" height="14" fill="#8a6a4a"/>'+''.join(f'<rect x="{k*100+40}" y="500" width="16" height="140" fill="#8a6a4a"/>' for k in range(8))
b+='<g fill="#5a4030"><ellipse cx="300" cy="490" rx="40" ry="30"/><circle cx="330" cy="460" r="20"/></g><path d="M346 456 L366 452 L348 466Z" fill="#ffa02a"/><circle cx="336" cy="456" r="4" fill="#fff"/><path d="M290 518 L290 522 M306 518 L306 522" stroke="#ffa02a" stroke-width="4"/>'
I[1069]=svg(b,d)

# 1120 夢のうた: a girl asleep on a crescent moon, dream bubbles with stars rising from her
d,b=bg([(0,'#1a1440'),(1,'#5a3a8a')])
b+=starsf(60,1120,800)+'<path d="M250 560 A220 220 0 1 0 560 300 A170 170 0 1 1 250 560Z" fill="#ffe8a0"/>'
b+='<g fill="#2a1a4a"><circle cx="400" cy="420" r="22"/><path d="M420 430 Q480 420 520 450 L500 470 Q460 450 420 452Z"/></g>'+''.join(ring(x,y,r2,'#e8d8ff',3,.8) for x,y,r2 in [(460,330,18),(500,270,26),(560,200,34)])+star5(560,200,16,'#fff')
I[1120]=svg(b,d)

# 1235 君のために僕がいる: an umbrella held over another figure in the rain, the holder getting wet
d,b=bg([(0,'#4a5a7a'),(1,'#8a9ab0')])
b+=rain(90,1235,'#e8f0ff',.4)+'<rect y="640" width="800" height="160" fill="#3a4050"/>'
b+=figure(340,660,290,'#1a1a24')+figure(470,660,300,'#1a1a24',pose='reachL')+'<path d="M200 330 Q340 220 480 330Z" fill="#3a8af8"/><path d="M340 330 L320 480" stroke="#2a2a2a" stroke-width="6"/>'
I[1235]=svg(b,d)

# 1255 さくらガール: a girl twirling in a school uniform skirt under a cherry tree in full bloom
d,b=bg([(0,'#ffd8e8'),(1,'#fff4f8')])
b+='<path d="M620 800 Q600 500 640 300" stroke="#6a4a3a" stroke-width="40" fill="none"/>'+'<g>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#ffb8d0"/>' for x,y,r2 in [(560,220,110),(700,180,100),(640,330,90),(480,300,70),(760,320,70)])+'</g>'+''.join(sakura(x,y,s) for x,y,s in [(540,200,1.2),(690,250,1.1),(620,340,1),(730,150,.9),(480,290,.8)])+petals(30,1255)
b+='<rect y="680" width="800" height="120" fill="#e8c8d0"/>'+figure(320,700,320,'#2a2a4a',pose='up')+'<path d="M270 570 Q320 540 370 570 L400 620 L240 620Z" fill="#2a2a4a"/>'
I[1255]=svg(b,d)

# 1381 ドレミソラシド: a sunny staircase of piano keys climbing into a summer sky, each step a colour
d,b=bg([(0,'#4ac8ff'),(1,'#e0faff')])
b+=cloud(600,160,1.6)+hinomaru_sun(160,160,60,'#fff8c8')
for k,c in enumerate(['#ff5a5a','#ffa02a','#ffd82a','#5ad85a','#3aa0ff','#6a6aff','#c85aff']):
    b+=f'<rect x="{80+k*92}" y="{680-k*60}" width="88" height="{120+k*60}" fill="#fff" stroke="#c8d0d8" stroke-width="4"/><rect x="{80+k*92}" y="{680-k*60}" width="88" height="16" fill="{c}"/>'
I[1381]=svg(b,d)

# 1398 Dragon Night: a dragon-shaped festival lantern parade under a night sky full of flags and fireworks
d,b=bg([(0,'#0a0820'),(1,'#2a1a4a')])
b+=firework(200,180,90,'#ff5ad8',seed=1)+firework(620,150,110,'#5ad8ff',seed=2)+'<rect y="640" width="800" height="160" fill="#1a1428"/>'
b+='<path d="M60 520 Q200 420 340 520 Q480 620 620 500 Q700 440 760 480" stroke="#3ad86a" stroke-width="56" fill="none" stroke-linecap="round"/><path d="M60 520 Q200 420 340 520 Q480 620 620 500 Q700 440 760 480" stroke="#ffd02a" stroke-width="8" fill="none" stroke-dasharray="20 22"/>'
b+='<circle cx="770" cy="470" r="44" fill="#3ad86a"/><circle cx="784" cy="456" r="8" fill="#ffd02a"/>'+''.join(f'<path d="M{x} 640 L{x} 560" stroke="#8a6a4a" stroke-width="5"/><path d="M{x} 560 L{x+50} 575 L{x} 590Z" fill="{c}"/>' for x,c in [(120,'#ff4a4a'),(300,'#4ad8ff'),(480,'#ffd02a')])
I[1398]=svg(b,d)

# 1587 堕天: a dark angel falling with one torn wing, black feathers spiralling in a red-black sky
d,b=bg([(0,'#a8202a'),(1,'#2a0508')])
r=random.Random(1587)
b+=''.join(f'<ellipse cx="{r.randint(40,760)}" cy="{r.randint(40,760)}" rx="8" ry="26" fill="#1a0a0a" transform="rotate({r.randint(0,180)} 400 400)" opacity=".8"/>' for _ in range(28))
b+='<g transform="rotate(160 400 420)">'+figure(400,560,300,'#000',pose='up')+'</g>'
b+='<path d="M420 420 Q560 300 700 340 Q620 380 640 420 Q560 420 560 470Z" fill="#141414"/><path d="M380 420 Q300 360 230 380 Q280 400 270 430" fill="#141414"/>'
I[1587]=svg(b,d)

# 149 北の宿から: a snowed-in inn window at night, a woman knitting a sweater by lamplight
d,b=bg([(0,'#1a2440'),(1,'#3a4a6a')])
b+=snow(90,149)+'<rect x="180" y="200" width="440" height="400" fill="#2a1a14"/><rect x="220" y="240" width="360" height="300" fill="#ffd28a"/>'+glow(400,390,200,'#ffd28a',.4)
b+='<path d="M220 340 L580 340 M400 240 L400 540" stroke="#5a3a2a" stroke-width="10"/><g fill="#5a3a2a"><circle cx="320" cy="400" r="24"/><path d="M290 540 Q290 430 320 424 Q360 430 360 540Z"/></g><path d="M340 470 L420 440 M340 476 L420 470" stroke="#8a2a2a" stroke-width="5"/><rect x="330" y="470" width="50" height="30" fill="#c8302a"/>'
b+='<path d="M160 200 Q400 150 640 200 L640 220 L160 220Z" fill="#fff"/><rect y="640" width="800" height="160" fill="#f4f6fa"/>'
I[149]=svg(b,d)

# 603 Silent Eve: a lone figure watching snow fall on a Christmas Eve street, a lit tree far away
d,b=bg([(0,'#0a1430'),(1,'#2a3a6a')])
b+=snow(110,603)+'<path d="M600 560 L660 400 L720 560Z" fill="#1a5a3a"/>'+''.join(f'<circle cx="{620+(k*37)%90}" cy="{430+(k*53)%120}" r="5" fill="{c}"/>' for k,c in enumerate(['#ff4a4a','#ffd02a','#4ad8ff','#fff','#ff8ad8','#ffd02a','#fff','#ff4a4a']))+star5(660,392,16,'#ffd02a')
b+='<rect y="560" width="800" height="240" fill="#e8eef8"/>'+figure(260,620,280,'#0a0e20')+'<path d="M0 580 L800 580" stroke="#c8d0e0" stroke-width="4"/>'
I[603]=svg(b,d)

# 744 箒星: a bright comet with a long sweeping tail over a dark hill, two small figures watching
d,b=bg([(0,'#050a20'),(1,'#1a2a50')])
b+=starsf(70,744,600)+'<path d="M640 160 Q400 260 120 300" stroke="#c8e8ff" stroke-width="40" fill="none" opacity=".25" stroke-linecap="round"/><path d="M640 160 Q400 250 140 290" stroke="#fff" stroke-width="10" fill="none" opacity=".7" stroke-linecap="round"/>'+glow(640,160,50,'#fff',.8)+'<circle cx="640" cy="160" r="16" fill="#fff"/>'
b+=hills(620,60,'#0a1020',744)+figure(360,640,150,'#000')+figure(420,640,140,'#000',pose='reach')
I[744]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
