import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 14. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def lips(x,y,s,c1='#e8102a',c2='#c80a20'): return f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="{c1}"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="{c2}"/></g>'

# 940 カナシミ ブルー: a blue rose wilting in a rain-streaked window, one blue petal sliding down the glass
d,b=bg([(0,'#4a6aa8'),(1,'#8aa0c8')])
b+=rain(60,940,'#a8c0e8',.4,6)+''.join(f'<path d="M{x} {y} q-4 60 2 120" stroke="#c8d8ff" stroke-width="4" fill="none" opacity=".5"/>' for x,y in [(150,100),(620,200),(520,420),(220,460)])
b+='<path d="M400 760 Q420 600 384 420" stroke="#2a4a3a" stroke-width="12" fill="none"/><g transform="rotate(20 380 400) translate(380 400) scale(2.2)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#1a3aa8',1),(60,'#2a4ac8',.9),(-60,'#2a4ac8',.9),(150,'#3a5ae8',.7),(-150,'#3a5ae8',.7)])+'</g>'
b+='<path d="M560 540 C540 530 540 500 560 496 C580 500 580 530 560 540Z" fill="#3a5ae8"/><path d="M560 540 Q562 600 556 660" stroke="#a8c0ff" stroke-width="3" fill="none" opacity=".6"/>'
I[940]=svg(b,d)

# 1224 青空の下、キミのとなり: two bicycles parked side by side on a grassy riverbank under a vast blue sky
d,b=bg([(0,'#1a8ae8'),(1,'#c0e8ff')])
b+=cloud(200,160,1.4)+cloud(600,240,1.0)+'<rect y="460" width="800" height="100" fill="#4ab0e8"/><path d="M-10 540 Q400 500 810 540 L810 810 L-10 810Z" fill="#6ac84a"/>'
for k,(x,c) in enumerate([(280,'#e8302a'),(520,'#3a6ae8')]): b+=f'<circle cx="{x-80}" cy="660" r="52" fill="none" stroke="#1a1a24" stroke-width="9"/><circle cx="{x+80}" cy="660" r="52" fill="none" stroke="#1a1a24" stroke-width="9"/><path d="M{x-80} 660 L{x-20} 590 L{x+60} 590 L{x+80} 660 M{x-20} 590 L{x} 660 L{x+60} 590 M{x-30} 570 L{x} 570 M{x+60} 590 L{x+50} 560" stroke="{c}" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+=heart(400,520,22,'#ff5a7a')
I[1224]=svg(b,d)

# 1484 ハルノヒ: a family's small hands and big hands together holding a single cherry blossom twig, spring sun glowing
d,b=bg([(0,'#ffe0ec'),(1,'#fff6e0')])
b+=glow(400,300,240,'#fff8d8',.8)+petals(30,1484,'#ffb0c8',0,800,8,14,.8)
b+='<path d="M400 600 L420 300" stroke="#5a3a2a" stroke-width="8"/>'+''.join(sakura(x,y,30,'#ffc0d4','#fff',x%60,1) for x,y in [(420,290),(380,340),(450,370),(400,250)])
b+='<g fill="#e8b890"><rect x="300" y="560" width="200" height="60" rx="30"/><rect x="250" y="600" width="140" height="160" rx="50"/><rect x="410" y="600" width="140" height="160" rx="50"/></g><g fill="#f4d0b0"><rect x="360" y="520" width="80" height="40" rx="20"/></g>'
I[1484]=svg(b,d)

# 1485 Naked Heart: a heart without skin, drawn as a bare outline of light in a dark room, beating visibly
d,b=bg([(0,'#1a0a14'),(1,'#0a0408')])
b+=glow(400,400,220,'#ff3a6a',.4)
b+='<path d="M400 600 C230 480 200 300 320 270 C370 260 400 300 400 330 C400 300 430 260 480 270 C600 300 570 480 400 600Z" fill="none" stroke="#ff8aa8" stroke-width="12"/>'
for k in range(1,3): b+=f'<path d="M400 {600+k*30} C{230-k*30} {480+k*10} {200-k*40} {300-k*20} {320-k*10} {270-k*30} C{370} {260-k*30} 400 {300-k*20} 400 {330-k*20} C400 {300-k*20} {430} {260-k*30} {480+k*10} {270-k*30} C{600+k*40} {300-k*20} {570+k*30} {480+k*10} 400 {600+k*30}Z" fill="none" stroke="#ff5a8a" stroke-width="4" opacity="{.5-k*.15:.2f}"/>'
b+='<path d="M140 680 L300 680 L330 620 L370 740 L400 660 L430 680 L660 680" stroke="#ff8aa8" stroke-width="6" fill="none"/>'
I[1485]=svg(b,d)

# 1551 風のゆくえ: a single long ribbon blown across a vast golden wheat field toward a horizon storm
d,b=bg([(0,'#3a4a7a'),(.5,'#c8a0a0'),(1,'#ffe0a0')])
b+='<rect y="460" width="800" height="340" fill="#e8b84a"/>'+''.join(f'<path d="M{x} 800 Q{x+10} 640 {x+30} {480+(x%60)}" stroke="#c8902a" stroke-width="3" fill="none"/>' for x in range(0,800,14))
b+='<path d="M120 600 Q240 380 400 440 Q560 500 640 300 Q680 200 760 180" stroke="#e8102a" stroke-width="24" fill="none" stroke-linecap="round"/>'+cloud(620,200,1.8,'#5a5a7a')
I[1551]=svg(b,d)

# 1565 花: a single small flower pushing up through dry cracked earth, glowing in a beam of light
d,b=bg([(0,'#3a2a2a'),(1,'#2a1a14')])
b+='<polygon points="380,-20 460,-20 520,800 320,800" fill="#fff6d8" opacity=".14"/>'
b+='<rect y="560" width="800" height="240" fill="#8a6a4a"/>'+''.join(f'<path d="M{x} 560 L{x+30} 640 L{x-10} 700 L{x+40} 800" stroke="#5a3a2a" stroke-width="4" fill="none"/>' for x in (80,240,560,700))
b+='<path d="M420 560 Q410 480 420 400" stroke="#4a9a3a" stroke-width="8" fill="none"/><path d="M420 480 Q470 450 500 470 Q460 500 420 490Z" fill="#5ac84a"/>'+glow(420,380,80,'#fff',.4)+flower(420,380,60,6,'#fff','#ffd02a',0,.7)
I[1565]=svg(b,d)

# 287 I AM YOUR SINGER: a vintage stand microphone with a ribbon of rainbow confetti spiralling round it on a sunny beach stage
d,b=bg([(0,'#3ab0f8'),(1,'#ffe0a0')])
b+=rays(400,300,20,'#fff',.3,8)+'<rect y="560" width="800" height="240" fill="#f4d890"/>'
b+='<rect x="394" y="300" width="12" height="400" fill="#c8c8d0"/><path d="M340 700 L460 700 L400 680Z" fill="#c8c8d0"/>'
b+='<rect x="360" y="190" width="80" height="120" rx="40" fill="#3a3a44"/>'+''.join(f'<path d="M{368+k*12} 200 L{368+k*12} 300" stroke="#8a8a94" stroke-width="3"/>' for k in range(6))
for k,c in enumerate(['#e8302a','#ffa82a','#ffe02a','#3ac85a','#2a8ae8']): b+=f'<path d="M{300} {600-k*80} Q400 {560-k*80} 500 {620-k*80}" stroke="{c}" stroke-width="10" fill="none"/>'
I[287]=svg(b,d)

# 361 Rock'n Rouge: a tube of red lipstick twisted up like a rocket, blasting off from a vanity mirror
d,b=bg([(0,'#ff5a8a'),(1,'#ffb0c8')])
b+=rays(400,600,20,'#fff',.25,8)
b+='<rect x="340" y="420" width="120" height="220" rx="10" fill="#d8b040"/><rect x="350" y="300" width="100" height="130" fill="#c8901a"/><path d="M350 300 L350 220 Q400 140 450 220 L450 300Z" fill="#e8102a"/>'
for k in range(5): b+=f'<path d="M{350+k*25} 650 Q{340+k*25} 720 {360+k*25} 780" stroke="#fff" stroke-width="8" fill="none" opacity=".6"/>'
b+=star5(200,200,30,'#fff')+star5(620,280,24,'#fff')
I[361]=svg(b,d)

# 392 Gypsy Queen: a crystal ball glowing violet on a fringed shawl, tarot cards fanned out around it
d,b=bg([(0,'#2a0a3a'),(1,'#1a0420')])
b+='<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#8a1a3a"/>'+''.join(f'<path d="M{k*40} 800 L{k*40+10} 760" stroke="#d8b040" stroke-width="4"/>' for k in range(21))
for k,a in enumerate((-40,-20,20,40)): b+=f'<rect x="{240+k*100}" y="520" width="80" height="130" rx="6" fill="#f4e8d0" stroke="#d8b040" stroke-width="4" transform="rotate({a} {280+k*100} 600)"/>'
b+=glow(400,400,180,'#c87aff',.6)+'<circle cx="400" cy="400" r="130" fill="#a87aff" opacity=".7"/><circle cx="360" cy="360" r="30" fill="#fff" opacity=".5"/><path d="M320 540 L480 540 L460 500 L340 500Z" fill="#d8b040"/>'+sparkle(420,420,30,'#fff')
I[392]=svg(b,d)

# 651 IT'S SHOWTIME!!: a stage curtain flinging open to a blast of spotlights and fireworks over a cheering crowd
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a3a')])
for x,a in [(160,20),(640,-20)]: b+=f'<polygon points="{x},800 {x+a*14},0 {x+a*20},0" fill="#fff6d8" opacity=".2"/>'
b+=firework(400,240,140,'#ffe05a',28,1)+firework(220,180,80,'#ff5ab8',20,2)+firework(580,180,80,'#5ae8ff',20,3)
b+='<path d="M-10 -10 L200 -10 Q180 300 120 800 L-10 800Z M810 -10 L600 -10 Q620 300 680 800 L810 800Z" fill="#c80a2a"/>'
for k in range(9): x=60+k*85;b+=figure(x,830,200,'#0a0410',pose='up' if k%2 else 'wave')
I[651]=svg(b,d)

# 863 自由への招待: a birdcage door swung open on a windowsill, a bird flying out into a blue sky
d,b=bg([(0,'#3ab0f8'),(1,'#c8ecff')])
b+=cloud(600,200,1.4)+'<rect y="600" width="800" height="200" fill="#e8d8c0"/>'
b+='<path d="M200 600 L200 360 Q200 200 340 200 Q480 200 480 360 L480 600Z" fill="none" stroke="#c8a040" stroke-width="8"/>'+''.join(f'<path d="M{220+k*30} {600} L{220+k*30} {260+abs(k-4.5)*14:.0f}" stroke="#c8a040" stroke-width="5"/>' for k in range(9))
b+='<path d="M480 460 L600 420 L600 580 L480 600Z" fill="none" stroke="#c8a040" stroke-width="6"/>'
b+='<g transform="translate(620 240) rotate(-20)"><path d="M-30 10 Q0 -10 40 0 Q60 10 70 -10 Q60 30 30 30 Q-10 40 -30 10Z" fill="#ffd02a"/><path d="M0 0 Q-40 -80 -110 -70 Q-60 -30 -10 10Z M10 0 Q60 -90 130 -90 Q90 -40 20 10Z" fill="#ffe05a"/><circle cx="54" cy="-4" r="4" fill="#1a1a1a"/></g>'
I[863]=svg(b,d)

# 1723 アシンメトリー: a face split down the middle into two mismatched halves, one smiling in pink, one cool in blue
d,b=bg([(0,'#ffd0e8'),(1,'#d0e8ff')])
b+='<rect x="0" y="0" width="400" height="800" fill="#ffb0d0" opacity=".5"/><rect x="400" y="0" width="400" height="800" fill="#a0c8ff" opacity=".5"/>'
b+='<path d="M400 160 Q240 160 230 380 Q240 620 400 640Z" fill="#ff8ab8"/><path d="M400 160 Q560 160 570 380 Q560 620 400 640Z" fill="#5a8ae8"/>'
b+='<circle cx="320" cy="360" r="20" fill="#fff"/><path d="M460 360 L520 360" stroke="#fff" stroke-width="10" stroke-linecap="round"/><path d="M320 500 Q360 540 400 520" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M400 520 L480 520" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'
I[1723]=svg(b,d)

# 1863 はいよろこんで: a desk at midnight piled with work, a coffee cup and a glowing monitor flashing a signal of three short and long lights
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<rect x="200" y="200" width="400" height="260" rx="12" fill="#2a2a34"/><rect x="220" y="220" width="360" height="220" fill="#1a3a5a"/>'+glow(400,330,200,'#5ab8ff',.3)
for k,(w,c) in enumerate([(24,'#ffe05a'),(24,'#ffe05a'),(24,'#ffe05a'),(60,'#ff5a5a'),(60,'#ff5a5a'),(60,'#ff5a5a')]): b+=f'<rect x="{240+sum([36,36,36,72,72,72][:k])}" y="320" width="{w}" height="24" rx="10" fill="{c}"/>'
b+='<rect x="380" y="460" width="40" height="60" fill="#2a2a34"/><rect y="520" width="800" height="280" fill="#4a3a2a"/>'
for k in range(6): b+=f'<rect x="{40+k*4}" y="{520-k*24}" width="140" height="24" fill="{["#fff","#f4ecd8"][k%2]}" stroke="#c8c0b0"/>'
b+='<path d="M620 460 L700 460 L690 540 L630 540Z" fill="#f4f0e8"/><path d="M640 440 Q650 420 640 400 M670 440 Q680 420 670 400" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>'
I[1863]=svg(b,d)

# 393 Fin: the word FIN fading on an old movie screen, a lone woman's silhouette walking into the projector beam
d,b=bg([(0,'#0a0a0a'),(1,'#1a1414')])
b+='<polygon points="400,800 160,140 640,140" fill="#ffffff" opacity=".06"/><rect x="120" y="100" width="560" height="340" fill="#d8d0c0"/>'
b+='<text x="400" y="320" text-anchor="middle" font-family="DejaVu Serif,serif" font-style="italic" font-size="130" fill="#3a3030">Fin</text>'
b+=figure(400,760,260,'#000',hair='#000')
I[393]=svg(b,d)

# 652 熱き鼓動の果て: a heart made of molten metal glowing orange as it's hammered on an anvil, sparks flying
d,b=bg([(0,'#1a0a04'),(1,'#0a0402')])
b+=glow(400,420,240,'#ff6a1a',.5)
b+='<path d="M200 560 L600 560 L560 620 L480 620 L520 720 L280 720 L320 620 L240 620Z" fill="#3a3a44"/>'+heart(400,470,110,'#ff7a1a')+heart(400,470,70,'#ffd06a')
b+='<g transform="rotate(-40 560 260)"><rect x="520" y="120" width="80" height="120" rx="8" fill="#5a5a64"/><rect x="550" y="240" width="20" height="200" fill="#8a5a2a"/></g>'
r=R(652)
for _ in range(24): a=r.uniform(-math.pi,0);rr=r.uniform(80,260);b+=f'<path d="M{400+rr*.4*math.cos(a):.0f} {440+rr*.4*math.sin(a):.0f} L{400+rr*math.cos(a):.0f} {440+rr*math.sin(a):.0f}" stroke="#ffd06a" stroke-width="4" stroke-linecap="round"/>'
I[652]=svg(b,d)

# 714 夏を抱きしめて: a giant tube wave curling over a surfer, sun blazing through the water
d,b=bg([(0,'#1ab0f8'),(1,'#bfeaff')])
b+=hinomaru_sun(620,140,60,'#fffbd8',1)
b+='<path d="M-10 800 L-10 400 Q200 200 480 240 Q680 280 700 420 Q620 340 520 360 Q400 400 400 520 Q420 640 560 700 L810 700 L810 800Z" fill="#0a78c8"/><path d="M480 240 Q680 280 700 420 Q640 360 560 370" stroke="#fff" stroke-width="16" fill="none"/>'
b+='<path d="M-10 400 Q200 200 480 240" stroke="#5ad0ff" stroke-width="30" fill="none" opacity=".5"/>'+''.join(f'<circle cx="{700-k*24}" cy="{420-k*10+(k%2)*14}" r="{8-k%3*2}" fill="#fff"/>' for k in range(6))
b+='<rect x="460" y="600" width="140" height="18" rx="9" fill="#ffd02a" transform="rotate(-10 530 610)"/>'+figure(530,600,140,'#0a1a2a',pose='up')
I[714]=svg(b,d)

# 792 survival dAnce: a dancer's silhouette in mid-spin on a glowing dance floor grid, laser beams criss-crossing
d,b=bg([(0,'#0a0420'),(1,'#1a0a3a')])
for k in range(6): b+=f'<path d="M{k*160} 0 L{800-k*120} 600" stroke="{["#ff3ab8","#3ae8ff","#ffe05a"][k%3]}" stroke-width="4" opacity=".7"/>'
b+='<path d="M-10 600 L810 600 L810 810 L-10 810Z" fill="#1a0a3a"/>'+''.join(f'<path d="M{400+(k-6)*30} 600 L{400+(k-6)*140} 800" stroke="#ff3ab8" stroke-width="3" opacity=".6"/>' for k in range(13))+''.join(f'<path d="M-10 {620+k*k*8} L810 {620+k*k*8}" stroke="#ff3ab8" stroke-width="3" opacity=".6"/>' for k in range(6))
b+=glow(400,480,140,'#ff3ab8',.4)+figure(400,620,280,'#000',pose='up')
I[792]=svg(b,d)

# 998 LOVE~Destiny~: a red string of fate tied in a bow between two pinky fingers, the string glowing across a starry sky
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a3a')])
b+=starsf(60,998,800,'#fff')
b+='<g fill="#e8c0a0"><rect x="40" y="520" width="200" height="50" rx="25" transform="rotate(-20 140 545)"/><rect x="560" y="300" width="200" height="50" rx="25" transform="rotate(-20 660 325)"/></g>'
b+='<path d="M230 500 Q400 600 400 420 Q400 260 570 330" stroke="#e8102a" stroke-width="6" fill="none"/>'+glow(400,450,120,'#e8102a',.3)
b+='<path d="M400 440 Q360 400 380 380 Q400 400 400 440 Q440 400 420 380 Q400 400 400 440Z" fill="none" stroke="#e8102a" stroke-width="6"/>'
I[998]=svg(b,d)

# 1225 Everything: a world map made entirely of tiny glowing windows, each a home with its own light
d,b=bg([(0,'#0a1028'),(1,'#141a38')])
r=R(1225)
for _ in range(500):
    x,y=r.uniform(40,760),r.uniform(160,640)
    land=((x-220)**2/140**2+(y-340)**2/120**2<1) or ((x-320)**2/80**2+(y-520)**2/120**2<1) or ((x-520)**2/180**2+(y-320)**2/110**2<1) or ((x-620)**2/70**2+(y-540)**2/60**2<1)
    if land: b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="8" height="8" fill="{r.choice(["#ffd27a","#fff4c8","#ffb04a"])}"/>'
b+=glow(400,400,300,'#ffd27a',.15)
I[1225]=svg(b,d)

# 1342 裸足でSummer: bare footprints in wet sand leading into a sparkling summer sea, sandals left behind
d,b=bg([(0,'#1ab0f8'),(1,'#bfeaff')])
b+=hinomaru_sun(160,140,60,'#fffbd8',1)+'<rect y="300" width="800" height="200" fill="#1a90d8"/>'+''.join(f'<rect x="{(k*137)%700}" y="{320+k*16}" width="60" height="4" fill="#fff" opacity=".6"/>' for k in range(10))
b+='<path d="M-10 480 Q400 440 810 500 L810 810 L-10 810Z" fill="#f4d890"/><path d="M-10 480 Q400 440 810 500" stroke="#fff" stroke-width="10" fill="none"/>'
for k in range(6): x=300+k*40+(k%2)*30;y=760-k*48;b+=f'<ellipse cx="{x}" cy="{y}" rx="16" ry="26" fill="#d8b870"/>'+''.join(f'<circle cx="{x-10+j*5}" cy="{y-30}" r="4" fill="#d8b870"/>' for j in range(5))
b+='<path d="M120 700 Q120 660 150 660 Q180 660 180 700 Q180 740 150 740 Q120 740 120 700Z M200 690 Q200 650 230 650 Q260 650 260 690 Q260 730 230 730 Q200 730 200 690Z" fill="#ff7aa8"/><path d="M150 670 L140 700 M150 670 L160 700 M230 660 L220 690 M230 660 L240 690" stroke="#fff" stroke-width="5"/>'
I[1342]=svg(b,d)

# 1423 怪獣: a giant kaiju's shadow looming over a fish market at dawn, a single fish leaping in front of it
d,b=bg([(0,'#3a4a6a'),(.6,'#a88aa8'),(1,'#ffc8a0')])
b+='<path d="M200 800 L220 520 Q200 380 280 300 L300 200 L330 260 L360 180 L390 250 L430 170 L460 260 Q560 300 580 420 L620 520 L700 500 L660 560 L620 560 L600 800Z" fill="#2a2a44"/><circle cx="440" cy="280" r="10" fill="#ffe05a"/>'
b+='<rect y="640" width="800" height="160" fill="#4a4a5a"/>'+''.join(f'<rect x="{40+k*150}" y="600" width="120" height="50" fill="#e8e8f0"/><path d="M{40+k*150} 600 L{100+k*150} 560 L{160+k*150} 600" fill="#3a8ae8"/>' for k in range(5))
b+='<g transform="rotate(-30 420 520)"><path d="M340 520 Q400 480 460 520 Q400 560 340 520Z" fill="#c8d8e8"/><path d="M460 520 L500 490 L500 550Z" fill="#c8d8e8"/><circle cx="360" cy="514" r="4" fill="#1a1a1a"/></g>'
I[1423]=svg(b,d)

# 555 You're My Only Shinin' Star: one star much brighter than all others reflected in a girl's tear-filled eye
d,b=bg([(0,'#04061e'),(1,'#141a3a')])
b+=starsf(80,555,800,'#c8d0ff')+glow(560,200,90,'#fff4c8',.8)+sparkle(560,200,70,'#fff')
b+='<path d="M120 560 Q400 360 680 560 Q400 760 120 560Z" fill="#f4f0f8"/><circle cx="400" cy="560" r="120" fill="#3a5a9a"/><circle cx="400" cy="560" r="56" fill="#0a0a1a"/><circle cx="440" cy="520" r="22" fill="#fff"/>'+sparkle(370,590,18,'#fff6d8')
b+='<path d="M560 640 Q570 670 570 680 A12 12 0 0 1 546 680 Q546 670 560 640Z" fill="#bfe8ff"/>'
I[555]=svg(b,d)

# 702 この愛に泳ぎ疲れても: a swimmer floating on her back in a vast blue pool, arms spread, watching clouds drift by
d,b=bg([(0,'#2ab0e8'),(1,'#0a78c8')])
r=R(702)
for _ in range(20): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<path d="M{x:.0f} {y:.0f} q30 -20 60 0 q30 20 60 0" stroke="#bff4ff" stroke-width="4" fill="none" opacity=".5"/>'
b+='<g transform="rotate(-20 400 400)"><circle cx="400" cy="260" r="34" fill="#e8c0a0"/><path d="M380 300 L420 300 L430 480 L410 620 L390 620 L370 480Z" fill="#e8302a"/><path d="M380 320 L260 260 M420 320 L540 260" stroke="#e8c0a0" stroke-width="20" stroke-linecap="round"/><path d="M370 260 Q400 200 430 260" fill="#3a2414"/></g>'
b+=''.join(ring(400,400,180+k*60,'#fff',4,.35-k*.1) for k in range(3))
I[702]=svg(b,d)

# 825 TRUE BLUE: a deep blue electric guitar standing alone in a blue spotlight, a blue rose at its base
d,b=bg([(0,'#04081a'),(1,'#0a1430')])
b+='<polygon points="400,-20 200,760 600,760" fill="#3a8aff" opacity=".18"/><ellipse cx="400" cy="740" rx="200" ry="30" fill="#3a8aff" opacity=".3"/>'
b+=guitar(400,500,1.3,0,'#1a4ad8')
b+='<g transform="translate(300 720) scale(.6)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#1a3aa8',1),(60,'#2a4ac8',.9),(-60,'#2a4ac8',.9),(150,'#3a5ae8',.7),(-150,'#3a5ae8',.7)])+'</g>'
I[825]=svg(b,d)

# 1226 a Day in Our Life: a sun drawn as a clock face over a school rooftop, its hands at noon, friends' shadows below
d,b=bg([(0,'#4ab8f8'),(1,'#c8ecff')])
b+=rays(400,240,24,'#fff',.3,8)+'<circle cx="400" cy="240" r="140" fill="#ffd02a"/><circle cx="400" cy="240" r="110" fill="#fff4c8"/>'+''.join(f'<rect x="396" y="140" width="8" height="20" fill="#c8901a" transform="rotate({a} 400 240)"/>' for a in range(0,360,30))+'<path d="M400 240 L400 160 M400 240 L404 170" stroke="#5a3a1a" stroke-width="8" stroke-linecap="round"/>'
b+='<rect y="560" width="800" height="240" fill="#c8c8d0"/><path d="M-10 500 L810 500" stroke="#8a8a94" stroke-width="6"/>'+''.join(f'<path d="M{x} 560 L{x} 500" stroke="#8a8a94" stroke-width="5"/>' for x in range(20,800,60))
for k in range(5): b+=figure(200+k*100,700,180,'#1a2a4a',pose='up' if k%2 else 'stand')
I[1226]=svg(b,d)

# 1254 weeeek: a week-view calendar with every day's square scribbled with a heart, the weekend circled twice
d,b=bg([(0,'#fff0d8'),(1,'#ffd8b0')])
b+='<rect x="80" y="200" width="640" height="400" fill="#fff" stroke="#3a3a44" stroke-width="6"/><rect x="80" y="200" width="640" height="70" fill="#3a8ae8"/>'
for k in range(7):
    x=80+k*91.4;b+=f'<path d="M{x:.0f} 200 L{x:.0f} 600" stroke="#3a3a44" stroke-width="3"/><text x="{x+45:.0f}" y="250" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="32" fill="#fff">{"MTWTFSS"[k]}</text>'+heart(x+45,420,26,["#ff5a8a","#ffa82a","#3ac85a","#3a8ae8","#a87aff","#e8302a","#e8302a"][k])
b+='<ellipse cx="620" cy="420" rx="100" ry="90" fill="none" stroke="#e8302a" stroke-width="6"/><ellipse cx="626" cy="416" rx="110" ry="100" fill="none" stroke="#e8302a" stroke-width="4"/>'
I[1254]=svg(b,d)

# 1302 ギンガムチェック: a gingham-check picnic blanket on a summer hillside, a straw hat and a bottle of lemonade on it
d,b=bg([(0,'#4ab8f8'),(1,'#c8ecff')])
b+=cloud(600,160,1.4)+'<path d="M-10 420 Q400 360 810 420 L810 810 L-10 810Z" fill="#6ac84a"/>'
b+='<g transform="skewX(-20) translate(140 0)">'+''.join(f'<rect x="{120+i*60}" y="{500+j*50}" width="60" height="50" fill="{["#fff","#ff8ab0","#ffc0d8"][(i%2)+(j%2)]}"/>' for i in range(8) for j in range(5))+'</g>'
b+='<ellipse cx="320" cy="580" rx="100" ry="26" fill="#e8c870"/><path d="M260 580 Q270 520 320 516 Q370 520 380 580Z" fill="#e8c870"/><rect x="262" y="560" width="116" height="12" fill="#ff5a8a"/>'
b+='<path d="M520 640 L520 520 Q520 490 540 480 L540 450 L560 450 L560 480 Q580 490 580 520 L580 640Z" fill="#ffe05a" opacity=".85"/>'
I[1302]=svg(b,d)

# 1388 サラバ、愛しき悲しみたちよ: five coloured paper balloons released into the sky from a rooftop, carrying away grey clouds
d,b=bg([(0,'#5ab8f8'),(1,'#d8f0ff')])
b+=cloud(160,620,1.6,'#a8b0c0')+cloud(640,660,1.4,'#a8b0c0')
for k,(x,y,c) in enumerate([(220,280,'#e8302a'),(330,200,'#ffd02a'),(440,250,'#ff7ab8'),(550,180,'#3ac85a'),(640,300,'#a87aff')]):
    b+=f'<path d="M{x} {y+60} Q{x+10} {y+200} {400+(k-2)*20} 760" stroke="#5a5a64" stroke-width="2" fill="none"/><ellipse cx="{x}" cy="{y}" rx="50" ry="62" fill="{c}"/><path d="M{x-6} {y+60} L{x+6} {y+60} L{x} {y+70}Z" fill="{c}"/><ellipse cx="{x-16}" cy="{y-20}" rx="10" ry="16" fill="#fff" opacity=".5"/>'
b+='<rect y="760" width="800" height="40" fill="#8a8a94"/>'
I[1388]=svg(b,d)

# 1404 夢灯籠: paper lanterns floating on a dark river carrying wishes into the night, a comet passing overhead
d,b=bg([(0,'#04081e'),(1,'#141a3a')])
b+=starsf(60,1404,420,'#fff')+'<path d="M600 80 Q420 140 200 300" stroke="#bfe8ff" stroke-width="24" fill="none" opacity=".2" stroke-linecap="round"/>'+glow(600,80,40,'#fff',.8)
b+='<rect y="440" width="800" height="360" fill="#0a1028"/>'
for k,(x,y,s) in enumerate([(200,520,.7),(360,580,.9),(540,540,.8),(660,640,1.0),(260,700,1.1),(460,720,1.2)]):
    b+=glow(x,y,60*s,'#ffa83a',.5)+f'<path d="M{x-30*s:.0f} {y} L{x+30*s:.0f} {y} L{x+24*s:.0f} {y-50*s:.0f} L{x-24*s:.0f} {y-50*s:.0f}Z" fill="#ffd27a"/><rect x="{x-36*s:.0f}" y="{y}" width="{72*s:.0f}" height="{10*s:.0f}" fill="#8a5a2a"/><ellipse cx="{x}" cy="{y+20*s:.0f}" rx="{40*s:.0f}" ry="{6*s:.0f}" fill="#ffd27a" opacity=".3"/>'
I[1404]=svg(b,d)

# 1566 満ちてゆく: a crescent moon filling up phase by phase across a twilight sky, the last one full and glowing
d,b=bg([(0,'#1a1a4a'),(1,'#5a4a8a')])
b+=starsf(40,1566,600,'#fff')
for k in range(5):
    x=120+k*140;y=420-k*50;f=k/4
    b+=f'<circle cx="{x}" cy="{y}" r="50" fill="#2a2a5a"/>'
    b+=f'<circle cx="{x}" cy="{y}" r="50" fill="#fff6d8"/>' if k==4 else f'<path d="M{x} {y-50} A50 50 0 0 1 {x} {y+50} A{50*(1-2*f):.0f} 50 0 0 {1 if f<.5 else 0} {x} {y-50}Z" fill="#fff6d8"/>'
b+=glow(680,220,80,'#fff6d8',.5)+'<path d="M-10 800 L-10 660 Q400 600 810 660 L810 800Z" fill="#141430"/>'
I[1566]=svg(b,d)

# 72 港町ブルース: a harbour at night with fishing boats bobbing, one red lantern and a seagull on a mooring post
d,b=bg([(0,'#0a1438'),(1,'#1a2a4a')])
b+=moon(620,140,40)+'<rect y="460" width="800" height="340" fill="#0a1a3a"/>'+''.join(f'<rect x="{560+(k%2)*20}" y="{480+k*30}" width="{60+k*8}" height="4" fill="#fff6d8" opacity=".4"/>' for k in range(8))
for x,s in [(200,1),(420,.8)]: b+=f'<path d="M{x-90*s} 480 L{x+90*s} 480 L{x+70*s} 520 L{x-70*s} 520Z" fill="#3a2a2a"/><rect x="{x-4}" y="{480-140*s}" width="8" height="{140*s}" fill="#3a2a2a"/><rect x="{x-30*s}" y="{450-50*s}" width="{60*s}" height="{40*s}" fill="#2a2a34"/>'
b+=chochin(200,330,28)+'<rect x="660" y="420" width="30" height="200" fill="#3a2a1a"/><path d="M650 400 Q670 380 690 400 L700 420 L640 420Z" fill="#f4f4f4"/><path d="M690 392 L710 396 L690 402Z" fill="#ffa83a"/>'
I[72]=svg(b,d)

# 422 ロマンス: a pair of ballet slippers with long pink ribbons tied into a heart on a polished floor
d,b=bg([(0,'#ffe0ec'),(1,'#ffc8dc')])
b+='<rect y="520" width="800" height="280" fill="#e8c8a0"/>'
for x,a in [(320,-12),(480,12)]: b+=f'<g transform="rotate({a} {x} 600)"><path d="M{x-40} 640 Q{x-50} 560 {x} 540 Q{x+50} 560 {x+40} 640 Q{x} 670 {x-40} 640Z" fill="#ffb0c8"/><ellipse cx="{x}" cy="590" rx="24" ry="34" fill="#e88aa8"/></g>'
b+='<path d="M320 560 C200 420 260 260 360 300 C390 312 400 340 400 360 C400 340 410 312 440 300 C540 260 600 420 480 560" stroke="#ff8ab0" stroke-width="10" fill="none"/>'
I[422]=svg(b,d)

# 489 SUMMER GAME: a dice and a roulette chip on a sizzling hot beach towel under a blazing sun, sunglasses reflecting it
d,b=bg([(0,'#ff8a1a'),(1,'#ffd04a')])
b+=rays(400,160,20,'#fff',.3,8)+hinomaru_sun(400,160,80,'#fff8d0',1)
b+='<path d="M-10 420 Q400 380 810 420 L810 810 L-10 810Z" fill="#f4d890"/><path d="M160 480 L640 480 L700 760 L100 760Z" fill="#1a1a24"/>'+''.join(f'<path d="M{160+k*80} 480 L{100+k*100} 760" stroke="#e8302a" stroke-width="16"/>' for k in range(0,7,2))
b+='<g transform="rotate(15 320 600)"><rect x="250" y="530" width="140" height="140" rx="20" fill="#fff"/>'+''.join(f'<circle cx="{320+dx}" cy="{600+dy}" r="13" fill="#e8102a"/>' for dx,dy in [(-35,-35),(35,35),(0,0),(35,-35),(-35,35)])+'</g>'
b+='<ellipse cx="520" cy="620" rx="56" ry="56" fill="#e8102a"/><circle cx="520" cy="620" r="36" fill="none" stroke="#fff" stroke-width="8" stroke-dasharray="14 10"/>'
I[489]=svg(b,d)

# 999 CAROLS: a candle-lit window of a snowy church, the silhouettes of a choir singing inside
d,b=bg([(0,'#0a1438'),(1,'#1a2a5a')])
b+=snow(70,999)+'<path d="M160 800 L160 380 L400 220 L640 380 L640 800Z" fill="#3a3a54"/><path d="M380 220 L380 100 L420 100 L420 220Z M360 140 L440 140" stroke="#3a3a54" stroke-width="20"/>'
b+='<path d="M280 760 L280 460 Q400 340 520 460 L520 760Z" fill="#ffd27a"/>'+glow(400,560,200,'#ffd27a',.4)
for k in range(5): b+=f'<g fill="#3a2a1a"><circle cx="{310+k*45}" cy="{620+(k%2)*10}" r="18"/><path d="M{292+k*45} {650+(k%2)*10} L{328+k*45} {650+(k%2)*10} L{334+k*45} 760 L{286+k*45} 760Z"/></g>'
b+='<rect y="760" width="800" height="40" fill="#e8eef8"/>'
I[999]=svg(b,d)

# 1118 SMILY: a yellow smiley sun peeking out from behind a rain cloud, its rays turning the raindrops into sparkles
d,b=bg([(0,'#7ac8ff'),(1,'#d8f0ff')])
b+=rays(500,320,20,'#fff',.35,8)+'<circle cx="500" cy="320" r="140" fill="#ffd02a"/><circle cx="460" cy="290" r="14" fill="#5a3a1a"/><circle cx="550" cy="290" r="14" fill="#5a3a1a"/><path d="M440 360 Q500 420 560 360" stroke="#5a3a1a" stroke-width="12" fill="none" stroke-linecap="round"/>'
b+=cloud(280,300,2.2,'#e8eef8')
for k in range(8): x=180+k*26;y=440+(k%3)*60;b+=sparkle(x,y,14,'#fff') if k%2 else f'<path d="M{x} {y} q6 16 0 24 q-6 -8 0 -24Z" fill="#5ab0ff"/>'
I[1118]=svg(b,d)

# 1134 花の名: a pressed flower in an old diary, its name written in faded ink beside it
d,b=bg([(0,'#d8c8b0'),(1,'#b8a888')])
b+='<path d="M120 160 L400 200 L680 160 L680 680 L400 720 L120 680Z" fill="#fbf4e4"/><path d="M400 200 L400 720" stroke="#d8c8a8" stroke-width="6"/>'
b+=''.join(f'<path d="M440 {280+k*40} Q540 {270+k*40} 640 {276+k*40}" stroke="#8a7a6a" stroke-width="4" fill="none" opacity=".6"/>' for k in range(10))
b+='<path d="M260 620 Q270 500 250 360" stroke="#7a8a5a" stroke-width="5" fill="none"/>'+flower(250,340,60,5,'#c8a0c8','#e8c86a',0,.75)+'<path d="M260 480 Q300 450 320 470 Q290 500 260 490Z" fill="#8a9a6a"/>'
I[1134]=svg(b,d)

# 1343 Sing Out!: a crowd's raised hands holding glowing pen-lights in a single wave of colour across a dark stadium
d,b=bg([(0,'#0a0420'),(1,'#1a0a3a')])
for k in range(12):
    x=40+k*66;y=500+40*math.sin(k*.7);c=['#ff5ab8','#5ae8ff','#ffe05a','#8aff8a'][k%4]
    b+=f'<path d="M{x} 800 L{x} {y+120} " stroke="#000" stroke-width="30"/><circle cx="{x}" cy="{y+120}" r="20" fill="#000"/>'+f'<rect x="{x-8}" y="{y}" width="16" height="120" rx="8" fill="{c}"/>'+glow(x,y+40,40,c,.6,'glow2')
b+=''.join(f'<polygon points="{x},0 {x-60},360 {x+60},360" fill="{c}" opacity=".15"/>' for x,c in [(160,'#ff5ab8'),(400,'#5ae8ff'),(640,'#ffe05a')])+'<rect x="100" y="300" width="600" height="30" fill="#2a1a4a"/>'
I[1343]=svg(b,d)

# 1366 二人セゾン: two people under one large tree that shows all four seasons, leaves of each colour falling
d,b=bg([(0,'#d8e8f8'),(1,'#f8f0e8')])
b+='<rect y="620" width="800" height="180" fill="#8ab86a"/><path d="M380 640 L390 400 L410 400 L420 640Z" fill="#5a3a1a"/>'
r=R(1366)
for _ in range(170): a=r.uniform(0,2*math.pi);rr=r.uniform(0,1)**.5*210;x=400+rr*math.cos(a);y=300+rr*.75*math.sin(a);c=['#ffb0c8','#5ab84a','#e8601a','#f4f8ff'][int((math.degrees(a)%360)//90)];b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(20,36):.0f}" fill="{c}"/>'
for _ in range(16): x,y=r.uniform(100,700),r.uniform(480,700);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="10" ry="6" fill="{r.choice(["#ffb0c8","#5ab84a","#e8601a","#fff"])}"/>'
b+=figure(300,660,160,'#2a2a3a')+figure(500,660,150,'#2a2a3a',hair='#2a2a3a')
I[1366]=svg(b,d)

# 1626 Masterplan: a blueprint unrolled on a table with a city's skyline rising out of it in glowing lines
d,b=bg([(0,'#0a1a3a'),(1,'#04081a')])
b+='<path d="M100 560 L700 560 L760 760 L40 760Z" fill="#1a4a9a"/>'+''.join(f'<path d="M{100+k*60} 560 L{40+k*72} 760" stroke="#5ab8ff" stroke-width="2" opacity=".5"/>' for k in range(11))+'<ellipse cx="760" cy="660" rx="30" ry="100" fill="#3a6ab8"/>'
for k,(x,h) in enumerate([(200,200),(280,320),(360,240),(440,400),(520,280),(600,180)]): b+=f'<rect x="{x-30}" y="{560-h}" width="60" height="{h}" fill="none" stroke="#5ae8ff" stroke-width="4"/>'+''.join(f'<rect x="{x-20}" y="{580-h+j*40}" width="12" height="16" fill="#5ae8ff" opacity=".6"/><rect x="{x+8}" y="{580-h+j*40}" width="12" height="16" fill="#5ae8ff" opacity=".6"/>' for j in range(h//40-1))
b+=glow(400,400,240,'#5ae8ff',.2)
I[1626]=svg(b,d)

# 279 真夏の果実: a ripe peach and a slice of watermelon melting on hot sand as a pink sunset sinks into the sea
d,b=bg([(0,'#ff6a8a'),(.5,'#ffb07a'),(1,'#ffe0a0')])
b+=hinomaru_sun(400,400,110,'#fff0c8',.8)+'<rect y="420" width="800" height="120" fill="#8a5aa8"/>'+''.join(f'<rect x="{360-k*12}" y="{430+k*18}" width="{80+k*24}" height="4" fill="#fff0c8" opacity=".6"/>' for k in range(6))
b+='<path d="M-10 540 Q400 510 810 540 L810 810 L-10 810Z" fill="#f4c890"/>'
b+='<path d="M200 660 Q260 580 320 660 Q300 720 260 720 Q220 720 200 660Z" fill="#ffa88a"/><path d="M260 600 Q258 640 262 700" stroke="#ff7a7a" stroke-width="5"/><path d="M262 600 Q280 570 300 568" stroke="#5a3a1a" stroke-width="5"/>'
b+='<path d="M420 700 A120 120 0 0 0 660 700Z" fill="#3ac85a"/><path d="M436 700 A104 104 0 0 0 644 700Z" fill="#ff4a5a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="8" fill="#1a1a1a"/>' for x,y in [(500,730),(540,750),(580,730),(540,720),(610,740)])
I[279]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
