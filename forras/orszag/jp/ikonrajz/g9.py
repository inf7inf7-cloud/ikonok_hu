import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 9. csoport, 2026-10-24
I={}
def rainbow(cx,cy,r,w=18,op=1):
    return ''.join(f'<path d="M{cx-r+k*w} {cy} A{r-k*w} {r-k*w} 0 0 1 {cx+r-k*w} {cy}" stroke="{c}" stroke-width="{w}" fill="none" opacity="{op}"/>' for k,c in enumerate(['#ff4a4a','#ffa82a','#ffe02a','#4ac84a','#2a8aff','#8a4aff']))

# 1300 Everyday、カチューシャ: a white headband with a big bow lying on the sand at the water's edge, waves sparkling
d,b=bg([(0,'#3ac0f8'),(1,'#c8f0ff')])
b+='<rect y="380" width="800" height="180" fill="#1aa8e8"/><path d="M-10 540 Q200 520 400 560 Q600 600 810 560 L810 810 L-10 810Z" fill="#f8e8b8"/><path d="M-10 540 Q200 520 400 560 Q600 600 810 560" stroke="#fff" stroke-width="12" fill="none"/>'
b+='<path d="M220 680 Q400 500 580 680" stroke="#fff" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M400 580 L320 530 L320 640Z M400 580 L480 530 L480 640Z" fill="#ff7ab8"/><circle cx="400" cy="584" r="18" fill="#ff4a9a"/>'
b+=sparkle(200,440,20,'#fff')+sparkle(620,460,26,'#fff')
I[1300]=svg(b,d)

# 1534 ベテルギウス: the red giant Betelgeuse glowing in the shoulder of Orion over a quiet field at night
d,b=bg([(0,'#04061a'),(1,'#141a3a')])
b+=starsf(90,1534,800,'#c8d8ff')
for x,y,r_ in [(300,200,0),(500,260,0),(370,400,0),(410,410,0),(450,420,0),(320,580,0),(500,560,0)]: b+=sparkle(x,y,18,'#e8f0ff')
b+='<path d="M300 200 L370 400 L320 580 M500 260 L450 420 L500 560 M370 400 L450 420" stroke="#8aa8ff" stroke-width="2" fill="none" opacity=".4"/>'
b+=glow(300,200,90,'#ff5a2a',.7)+'<circle cx="300" cy="200" r="22" fill="#ff8a4a"/>'
b+='<path d="M-10 800 L-10 690 Q400 650 810 690 L810 800Z" fill="#06080e"/>'+figure(620,700,110,'#020306')
I[1534]=svg(b,d)

# 1841 お気に召すまま: a glass of red wine on a silver tray offered under a dim cabaret spotlight
d,b=bg([(0,'#2a0a1a'),(1,'#100408')])
b+='<polygon points="400,-20 220,800 580,800" fill="#ffd8a8" opacity=".1"/>'
b+='<ellipse cx="400" cy="620" rx="230" ry="40" fill="#c8c8d8"/><ellipse cx="400" cy="610" rx="210" ry="30" fill="#e8e8f0"/>'
b+='<path d="M320 300 Q320 460 400 470 Q480 460 480 300Z" fill="#f4e8f0" opacity=".3" stroke="#fff" stroke-width="4"/><path d="M326 380 Q336 460 400 466 Q464 460 474 380Z" fill="#a8102a"/><rect x="394" y="470" width="12" height="120" fill="#f4e8f0" opacity=".6"/><ellipse cx="400" cy="600" rx="50" ry="10" fill="#f4e8f0" opacity=".6"/>'
b+=sparkle(460,330,18,'#fff')
I[1841]=svg(b,d)

# 577 愛が止まらない: a heart-shaped spinning top whirling endlessly on a mirrored disco floor
d,b=bg([(0,'#1a0a3a'),(1,'#5a1a6a')])
b+=rays(400,400,20,'#ff8ad8',.2,5)
for k in range(4): b+=f'<ellipse cx="400" cy="620" rx="{120+k*60}" ry="{20+k*10}" fill="none" stroke="#ff8ad8" stroke-width="4" opacity="{.6-k*.13:.2f}"/>'
b+=heart(400,380,150,'#ff2a8a')+'<path d="M400 520 L400 620" stroke="#ff2a8a" stroke-width="16"/><rect x="392" y="200" width="16" height="70" fill="#ffd0f0"/>'
for a in (-30,30): b+=f'<path d="M{400+250*math.cos(math.radians(a+180)):.0f} {380+80*math.sin(math.radians(a)):.0f} q40 -30 80 0" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>'
I[577]=svg(b,d)

# 733 しるし: two hands pressing their palms together against a window from opposite sides, a thumbprint in the fog
d,b=bg([(0,'#8a9ab8'),(1,'#c8d0e0')])
b+='<rect x="100" y="100" width="600" height="600" fill="#d8e0ec" opacity=".6"/>'+''.join(f'<circle cx="{150+(k*91)%500}" cy="{140+(k*137)%520}" r="{3+k%4}" fill="#fff" opacity=".6"/>' for k in range(40))
b+='<g fill="#e8c0a0" opacity=".9"><rect x="250" y="400" width="120" height="260" rx="40"/>'+''.join(f'<rect x="{254+k*28}" y="{250+abs(k-1.5)*16:.0f}" width="24" height="180" rx="12"/>' for k in range(4))+'</g>'
b+='<g fill="#d8a888" opacity=".75"><rect x="430" y="420" width="120" height="260" rx="40"/>'+''.join(f'<rect x="{434+k*28}" y="{270+abs(k-1.5)*16:.0f}" width="24" height="180" rx="12"/>' for k in range(4))+'</g>'
b+='<path d="M100 100 L700 100 L700 700 L100 700Z M400 100 L400 700" stroke="#5a5a6a" stroke-width="18" fill="none"/>'
I[733]=svg(b,d)

# 1208 Bittersweet: a bar of dark chocolate snapped in two, one half wrapped in a lace ribbon on a plate
d,b=bg([(0,'#f4e0e8'),(1,'#d8b0c0')])
b+='<ellipse cx="400" cy="520" rx="320" ry="90" fill="#fff"/><ellipse cx="400" cy="510" rx="280" ry="70" fill="#f4f0f4"/>'
for x,a in [(270,-8),(520,10)]: b+=f'<g transform="rotate({a} {x} 460)"><rect x="{x-110}" y="380" width="220" height="140" rx="6" fill="#3a1a0a"/>'+''.join(f'<rect x="{x-100+i*72}" y="{390+j*66}" width="64" height="58" rx="4" fill="#4a2414"/>' for i in range(3) for j in range(2))+'</g>'
b+='<path d="M380 420 L360 440 L380 470 L362 500 L380 520" stroke="#f4e0e8" stroke-width="12" fill="none"/><rect x="460" y="380" width="30" height="160" fill="#ff7aa8" transform="rotate(10 520 460)"/>'
I[1208]=svg(b,d)

# 1867 虹 (菅田将暉): an old couple's two pairs of shoes side by side on a step, a rainbow arching in the window above
d,b=bg([(0,'#bfe0f0'),(1,'#f0ece4')])
b+='<rect x="180" y="80" width="440" height="300" fill="#8ad0ff"/>'+rainbow(400,380,200,16)+'<rect x="180" y="80" width="440" height="300" fill="none" stroke="#6a5a4a" stroke-width="16"/>'
b+='<rect y="560" width="800" height="240" fill="#a88a6a"/><rect y="540" width="800" height="30" fill="#c8a880"/>'
b+='<path d="M200 620 Q200 580 250 580 L320 590 Q350 600 350 640 L200 640Z M370 620 Q370 580 420 580 L490 590 Q520 600 520 640 L370 640Z" fill="#3a2a1a"/><path d="M560 640 L560 600 Q570 580 600 590 L640 610 Q660 620 660 640Z" fill="#c84a5a"/><path d="M670 640 L670 600 Q680 580 710 590 L750 610 Q770 620 770 640Z" fill="#c84a5a"/>'
I[1867]=svg(b,d)

# 543 慟哭: a figure collapsed to its knees on a vast dark shore, a storm wave towering above
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+='<path d="M810 120 Q560 100 420 260 Q360 340 420 400 Q500 360 520 300 Q560 420 810 440Z" fill="#2a4a6a"/><path d="M420 260 Q460 240 500 280 Q470 290 450 320" stroke="#e8f0ff" stroke-width="10" fill="none"/>'
b+='<rect y="560" width="800" height="240" fill="#0a0a14"/>'+rain(80,543,'#8a9ab8',.4,6)
b+='<g fill="#000"><circle cx="300" cy="490" r="24"/><path d="M270 510 Q300 500 330 520 L350 590 L250 590 L260 540Z"/><path d="M270 520 Q240 470 230 430 M330 520 Q360 470 370 430" stroke="#000" stroke-width="14" fill="none" stroke-linecap="round"/></g>'
I[543]=svg(b,d)

# 698 運命のルーレット廻して: a roulette wheel spinning with one red number glowing, the ball poised to drop
d,b=bg([(0,'#0a2a1a'),(1,'#041a0e')])
b+=glow(400,420,260,'#ffd27a',.25)
b+='<circle cx="400" cy="420" r="260" fill="#6a3a1a"/><circle cx="400" cy="420" r="230" fill="#1a1a1a"/>'
for k in range(24): b+=f'<path d="M400 420 L{400+230*math.cos(math.radians(k*15)):.0f} {420+230*math.sin(math.radians(k*15)):.0f} A230 230 0 0 1 {400+230*math.cos(math.radians(k*15+15)):.0f} {420+230*math.sin(math.radians(k*15+15)):.0f}Z" fill="{["#c80a1a","#141414"][k%2] if k else "#1a8a3a"}"/>'
b+='<circle cx="400" cy="420" r="120" fill="#a86a2a"/><circle cx="400" cy="420" r="30" fill="#e8c060"/>'+''.join(f'<path d="M400 420 L{400+90*math.cos(math.radians(a)):.0f} {420+90*math.sin(math.radians(a)):.0f}" stroke="#e8c060" stroke-width="10"/>' for a in (0,90,180,270))
b+=glow(560,240,30,'#fff',.6,'glow2')+'<circle cx="560" cy="240" r="16" fill="#fff"/>'
I[698]=svg(b,d)

# 858 DIVE TO BLUE: a diver plunging headfirst into an ocean of impossibly deep blue, bubbles streaming up
d,b=bg([(0,'#7ad0ff'),(.3,'#1a8ae8'),(1,'#041a5a')])
b+='<rect y="180" width="800" height="8" fill="#fff" opacity=".6"/>'+''.join(f'<polygon points="{x},188 {x+80},800 {x+120},800" fill="#fff" opacity=".07"/>' for x in (100,300,520))
b+='<g transform="rotate(170 400 460)"><path d="M380 300 L420 300 L430 420 L420 520 L408 600 L392 600 L380 520 L370 420Z" fill="#0a0a1a"/><circle cx="400" cy="280" r="24" fill="#0a0a1a"/><path d="M380 330 L390 220 M420 330 L410 220" stroke="#0a0a1a" stroke-width="14" stroke-linecap="round"/></g>'
for k in range(14): b+=f'<circle cx="{380+(k*37)%60}" cy="{560+k*14}" r="{4+k%5}" fill="none" stroke="#e8f8ff" stroke-width="3"/>'
I[858]=svg(b,d)

# 1068 虹 (ゆず): two acoustic guitars leaning on a street bench beneath a bright rainbow after rain
d,b=bg([(0,'#8ac8f8'),(1,'#e8f4ff')])
b+=rainbow(400,560,340,22)+cloud(120,560,1.0)+cloud(680,560,1.1)
b+='<rect y="600" width="800" height="200" fill="#a8a8b0"/><rect x="220" y="560" width="360" height="22" fill="#6a4a2a"/><rect x="240" y="580" width="14" height="60" fill="#3a3a44"/><rect x="546" y="580" width="14" height="60" fill="#3a3a44"/>'

for x,a,c in [(330,-14,'#e8a050'),(480,14,'#c87830')]: b+=f'<g transform="translate({x} 520) rotate({a}) scale(.6)"><ellipse cx="0" cy="60" rx="70" ry="64" fill="{c}"/><ellipse cx="0" cy="-10" rx="52" ry="50" fill="{c}"/><circle cx="0" cy="30" r="20" fill="#1a1a1a"/><rect x="-8" y="-220" width="16" height="200" fill="#3a2414"/><rect x="-14" y="-260" width="28" height="44" rx="4" fill="#3a2414"/></g>'
b+=''.join(f'<ellipse cx="{x}" cy="700" rx="40" ry="8" fill="#bfe0ff" opacity=".7"/>' for x in (180,560,700))
I[1068]=svg(b,d)

# 1209 きっと大丈夫: a paper boat sailing safely out of a storm toward a patch of clear blue sky
d,b=bg([(0,'#3a4a5a'),(1,'#6a7a8a')])
b+='<circle cx="620" cy="200" r="200" fill="#8ad0ff"/>'+rays(620,200,14,'#fff',.3,6)+cloud(200,180,1.8,'#4a5a6a')+rain(40,1209,'#c8d8e8',.4,5)
b+='<rect y="540" width="800" height="260" fill="#2a5a8a"/>'+''.join(f'<path d="M-10 {580+k*50} Q100 {560+k*50} 200 {580+k*50} T400 {580+k*50} T600 {580+k*50} T810 {580+k*50}" stroke="#5a8ab8" stroke-width="6" fill="none"/>' for k in range(5))
b+='<path d="M300 560 L500 560 L460 620 L340 620Z" fill="#fff"/><path d="M400 440 L400 560 L320 560Z M400 440 L400 560 L470 560Z" fill="#f4f4f4" stroke="#c8c8d8" stroke-width="3"/>'
I[1209]=svg(b,d)

# 1573 点描の唄: a summer firework blossom painted entirely in pointillist dots over a dotted night river
d,b=bg([(0,'#0a0a2a'),(1,'#1a1a3a')])
r=R(1573)
for _ in range(420):
    a=r.uniform(0,2*math.pi);rr=r.uniform(0,1)**.6*250;x=400+rr*math.cos(a);y=320+rr*math.sin(a)
    b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(5,10):.0f}" fill="{r.choice(["#ffd27a","#ff9aa8","#ff5a8a","#fff0d8"]) if rr>60 else "#fff6d8"}" opacity=".9"/>'
for _ in range(260):
    x,y=r.uniform(0,800),r.uniform(620,800);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(4,8):.0f}" fill="{r.choice(["#2a3a7a","#3a4a9a","#ff9aa8","#ffd27a"])}" opacity=".7"/>'
I[1573]=svg(b,d)

# 1574 ケセラセラ: a yellow umbrella blown inside out, cartwheeling happily away in the wind and rain
d,b=bg([(0,'#7ab0d8'),(1,'#c8e0f0')])
b+=rain(60,1574,'#fff',.5,6)+'<rect y="660" width="800" height="140" fill="#5a6a7a"/>'
b+='<g transform="rotate(30 420 380)"><path d="M260 300 Q300 460 420 470 Q540 460 580 300 Q500 360 420 330 Q340 360 260 300Z" fill="#ffd02a"/><path d="M420 330 L420 520 Q420 570 380 560" stroke="#3a3a44" stroke-width="10" fill="none"/></g>'
for y in (260,560): b+=f'<path d="M80 {y} Q180 {y-30} 260 {y}" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>'
b+=''.join(f'<path d="M{x} 690 q20 -20 40 0" stroke="#bfe0ff" stroke-width="4" fill="none"/>' for x in (160,420,620))
I[1574]=svg(b,d)

# 1595 Step and a step: a staircase of colourful blocks climbing into a sky of stars, sneakers' footprints on each step
d,b=bg([(0,'#3a2a8a'),(1,'#ff8ab8')])
b+=starsf(40,1595,300,'#fff')
for k,c in enumerate(['#ff5a8a','#ffa82a','#ffe02a','#5ac87a','#4aa8ff','#a87aff']):
    x=60+k*110;y=700-k*90
    b+=f'<rect x="{x}" y="{y}" width="120" height="{800-y}" fill="{c}"/><ellipse cx="{x+40}" cy="{y+20}" rx="12" ry="7" fill="#fff" opacity=".7"/><ellipse cx="{x+80}" cy="{y+30}" rx="12" ry="7" fill="#fff" opacity=".7"/>'
b+=sparkle(720,140,40,'#fff')
I[1595]=svg(b,d)

# 206 22才の別れ: twenty-two candles on a cake, one already blown out, smoke curling toward a dim window
d,b=bg([(0,'#2a1a2a'),(1,'#4a2a2a')])
b+=glow(400,420,240,'#ffb850',.4)+'<rect y="620" width="800" height="180" fill="#3a2414"/>'
b+='<ellipse cx="400" cy="640" rx="240" ry="40" fill="#fff"/><rect x="190" y="500" width="420" height="140" fill="#f4e8d8"/><ellipse cx="400" cy="500" rx="210" ry="40" fill="#fff6e8"/><path d="M190 540 Q240 560 290 540 T390 540 T490 540 T610 540" stroke="#ff9ab0" stroke-width="12" fill="none"/>'
for k in range(22):
    a=k*2*math.pi/22;x=400+170*math.cos(a);y=500+28*math.sin(a)
    b+=f'<rect x="{x-4:.0f}" y="{y-50:.0f}" width="8" height="50" fill="{["#ff9ab0","#9ad0ff","#ffe08a"][k%3]}"/>'
    if k!=5: b+=f'<path d="M{x:.0f} {y-68:.0f} Q{x+6:.0f} {y-58:.0f} {x:.0f} {y-50:.0f} Q{x-6:.0f} {y-58:.0f} {x:.0f} {y-68:.0f}Z" fill="#ffd060"/>'
    else: b+=f'<path d="M{x:.0f} {y-54:.0f} Q{x+20:.0f} {y-100:.0f} {x:.0f} {y-140:.0f} Q{x-20:.0f} {y-180:.0f} {x+10:.0f} {y-220:.0f}" stroke="#c8c8d0" stroke-width="5" fill="none" opacity=".6"/>'
I[206]=svg(b,d)

# 1100 お願い!セニョリータ: maracas and a flamenco fan bursting with colour against a hot Latin sunset
d,b=bg([(0,'#ff3a5a'),(1,'#ffb03a')])
b+=rays(400,400,24,'#ffe05a',.25,8)
b+='<g transform="translate(400 380)">'+''.join(f'<path d="M0 60 L{240*math.cos(math.radians(a)):.0f} {240*math.sin(math.radians(a)):.0f} A240 240 0 0 1 {240*math.cos(math.radians(a+15)):.0f} {240*math.sin(math.radians(a+15)):.0f}Z" fill="{["#e8102a","#1a1a1a"][k%2]}"/>' for k,a in enumerate(range(-165,-15,15)))+'<circle cx="0" cy="60" r="20" fill="#d8b040"/></g>'
for x,a,c in [(220,-30,'#3ac85a'),(580,30,'#2a8ae8')]: b+=f'<g transform="rotate({a} {x} 600)"><ellipse cx="{x}" cy="560" rx="70" ry="90" fill="{c}"/><rect x="{x-12}" y="640" width="24" height="140" rx="10" fill="#c8901a"/><path d="M{x-50} 540 L{x+50} 540 M{x-40} 580 L{x+40} 580" stroke="#ffe05a" stroke-width="10"/></g>'
I[1100]=svg(b,d)

# 1337 帰り道は遠回りしたくなる: two long shadows walking home along a riverside path at golden hour, a detour arrow on the path
d,b=bg([(0,'#ff9a5a'),(1,'#ffd8a0')])
b+=hinomaru_sun(560,300,110,'#fff4d0',.8)
b+='<path d="M-10 460 Q400 420 810 460 L810 810 L-10 810Z" fill="#c8a870"/><path d="M-10 560 Q400 520 810 560 L810 660 Q400 620 -10 660Z" fill="#5a9ad8"/>'
b+='<path d="M200 800 Q260 620 560 480" stroke="#e8d0a0" stroke-width="40" fill="none"/>'
b+=figure(320,640,120,'#2a1a2a',hair='#2a1a2a')+figure(360,640,130,'#2a1a2a')
b+='<path d="M320 640 L100 760 L120 770 Z M360 640 L130 790 L160 795Z" fill="#000" opacity=".25"/>'
I[1337]=svg(b,d)

# 1456 SUN: a huge smiling sun rising over a crowd of hands clapping in rhythm
d,b=bg([(0,'#ffb01a'),(1,'#ffe07a')])
b+=rays(400,320,24,'#fff',.35,9)+'<circle cx="400" cy="320" r="170" fill="#ff7a1a"/><circle cx="400" cy="320" r="140" fill="#ff9a2a"/>'
b+='<circle cx="350" cy="290" r="14" fill="#5a1a0a"/><circle cx="450" cy="290" r="14" fill="#5a1a0a"/><path d="M330 360 Q400 420 470 360" stroke="#5a1a0a" stroke-width="14" fill="none" stroke-linecap="round"/>'
for k in range(7): x=80+k*106;b+=f'<g fill="#3a1a0a"><rect x="{x-20}" y="{640+(k%2)*30}" width="40" height="200" rx="18"/><ellipse cx="{x}" cy="{630+(k%2)*30}" rx="30" ry="40"/></g>'
I[1456]=svg(b,d)

# 1498 TATTOO: a rose-and-swallow tattoo design sketched on paper, the ink still wet and glistening
d,b=bg([(0,'#f4ece0'),(1,'#e0d4c0')])
b+='<rect x="140" y="120" width="520" height="560" fill="#fbf8f0" transform="rotate(-3 400 400)"/>'
b+='<path d="M260 560 Q400 640 540 560" stroke="#1a1a1a" stroke-width="10" fill="none"/><path d="M260 560 L240 540 M260 560 L240 590 M540 560 L560 540 M540 560 L560 590" stroke="#1a1a1a" stroke-width="8"/>'
b+=rose(400,440,1.1)+'<path d="M330 450 Q300 500 330 540 M470 450 Q500 500 470 540" stroke="#2a5a2a" stroke-width="8" fill="none"/>'
b+='<path d="M300 220 Q340 260 400 240 L460 210 Q420 240 430 270 L480 250 Q440 290 380 290 Q320 280 300 220Z" fill="#1a3a8a"/><path d="M300 220 L270 200 L290 236Z" fill="#1a3a8a"/>'
I[1498]=svg(b,d)

# 1525 あの夢をなぞって: a fingertip tracing a shooting star's path across the night sky over a town
d,b=bg([(0,'#0a0a3a'),(1,'#3a2a6a')])
b+=starsf(60,1525,600,'#fff')+'<path d="M80 120 Q400 200 620 420" stroke="#fff6d8" stroke-width="6" fill="none" stroke-dasharray="4 14" stroke-linecap="round"/>'+sparkle(640,440,36,'#fff')+glow(640,440,60,'#ffe8a0',.6)
b+=skyline(700,'#0a0820',1525,60,160,'#ffd27a',60)
b+='<rect x="460" y="540" width="180" height="260" fill="#06051a"/>'+figure(560,540,170,'#06051a',pose='reachL')
I[1525]=svg(b,d)

# 1535 ビリミリオン: a single coin balanced on its edge atop a teetering tower of gold bullion
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a1a')])
b+=glow(400,400,260,'#ffd02a',.3)
for k in range(6):
    w=300-k*40;y=700-k*60
    b+=f'<path d="M{400-w/2} {y} L{400+w/2} {y} L{400+w/2-20} {y-50} L{400-w/2+20} {y-50}Z" fill="#e8b830" stroke="#a8781a" stroke-width="4"/>'
b+='<rect x="380" y="220" width="40" height="120" rx="12" fill="#ffd84a" stroke="#a8781a" stroke-width="6"/>'+sparkle(440,230,26,'#fff')
I[1535]=svg(b,d)

# 495 Thrill: a red electric guitar crackling with lightning against a geometric black-and-white backdrop
d,b=bg([(0,'#141414'),(1,'#2a2a2a')])
for i in range(8):
    for j in range(8):
        if (i+j)%2: b+=f'<path d="M{i*100} {j*100} L{i*100+100} {j*100} L{i*100} {j*100+100}Z" fill="#f4f4f4" opacity=".12"/>'
b+=bolt([(120,120),(220,300),(170,320),(280,520)],'#5ae8ff',14,1)+bolt([(700,160),(600,320),(650,340),(560,520)],'#5ae8ff',14,1)
b+=guitar(400,500,1.2,30,'#e8102a')
I[495]=svg(b,d)

# 734 名もなき詩: a blank notebook page with a single line of crossed-out words and a pencil resting in the margin
d,b=bg([(0,'#6a8aa8'),(1,'#a8b8c8')])
b+='<rect x="140" y="100" width="520" height="620" fill="#fbf8f0" transform="rotate(4 400 400)"/>'+''.join(f'<path d="M160 {200+k*50} L640 {234+k*50}" stroke="#bfd8f0" stroke-width="3" transform="rotate(0)"/>' for k in range(10))
b+='<path d="M200 260 Q300 250 440 270" stroke="#3a3a5a" stroke-width="8" fill="none"/><path d="M190 266 L460 262" stroke="#e8302a" stroke-width="6"/>'
b+='<g transform="rotate(-40 520 560)"><rect x="380" y="540" width="280" height="36" fill="#ffd02a"/><path d="M660 540 L710 558 L660 576Z" fill="#f4d0a0"/><rect x="360" y="540" width="24" height="36" fill="#ff8aa8"/></g>'
I[734]=svg(b,d)

# 1117 PEACH: a ripe peach split open with a heart-shaped stone, pink petals swirling around it
d,b=bg([(0,'#ffe0e8'),(1,'#ffc0d0')])
b+=petals(30,1117,'#ff9ab8',0,800,8,14,.8)
b+='<path d="M400 280 Q560 240 600 420 Q620 600 400 640 Q180 600 200 420 Q240 240 400 280Z" fill="#ffa88a"/><path d="M400 280 Q380 460 400 640" stroke="#ff7a7a" stroke-width="10" fill="none"/>'
b+='<path d="M400 290 Q520 290 540 420 Q550 540 400 600 Q250 540 260 420 Q280 290 400 290Z" fill="#ffd8a0"/>'+heart(400,430,70,'#c85a3a')
b+='<path d="M400 280 Q420 200 470 180" stroke="#5a3a1a" stroke-width="10" fill="none"/><path d="M420 220 Q480 180 540 210 Q480 250 420 220Z" fill="#5ab84a"/>'
I[1117]=svg(b,d)

# 1482 愛を伝えたいだとか: a hand holding a love letter half out of a jacket pocket on a slow walk home at dusk
d,b=bg([(0,'#5a5a8a'),(1,'#e8a890')])
b+='<rect x="140" y="160" width="520" height="640" rx="40" fill="#3a3a4a"/><path d="M400 160 L400 800" stroke="#2a2a34" stroke-width="6"/><rect x="200" y="460" width="180" height="20" fill="#2a2a34"/>'
b+='<rect x="210" y="360" width="150" height="110" rx="6" fill="#fff8f0" transform="rotate(-10 285 415)"/>'+heart(285,410,24,'#ff5a7a')
b+='<g fill="#e8c0a0"><rect x="320" y="330" width="40" height="120" rx="20" transform="rotate(30 340 390)"/><rect x="290" y="320" width="34" height="90" rx="17" transform="rotate(20 307 365)"/></g>'
I[1482]=svg(b,d)

# 1515 秒針を噛む: a clock's second hand bitten in two by a row of sharp teeth, gears spilling out in purple light
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=glow(400,400,240,'#a87aff',.35)+'<circle cx="400" cy="400" r="200" fill="#e8e0f0"/><circle cx="400" cy="400" r="200" fill="none" stroke="#2a1a3a" stroke-width="14"/>'
b+='<path d="M400 400 L400 260" stroke="#2a1a3a" stroke-width="14" stroke-linecap="round"/><path d="M400 400 L520 300" stroke="#e8302a" stroke-width="6"/><path d="M540 280 L600 230" stroke="#e8302a" stroke-width="6"/>'
b+='<path d="M490 260 L620 260 L604 296 L588 262 L572 300 L556 262 L540 300 L524 262 L508 296Z" fill="#fff"/><path d="M490 330 L620 330 L604 296 L588 330 L572 292 L556 330 L540 292 L524 330 L508 296Z" fill="#fff" transform="translate(0 6)"/>'
for x,y,s in [(180,640,30),(640,620,40),(200,200,24)]: b+=f'<circle cx="{x}" cy="{y}" r="{s}" fill="none" stroke="#a87aff" stroke-width="10" stroke-dasharray="8 6"/>'
I[1515]=svg(b,d)

# 329 カムフラージュ: a red lipstick mark on a white coffee cup, half-hidden behind a newspaper on a café table
d,b=bg([(0,'#e8dcc8'),(1,'#c8b8a0')])
b+='<rect y="540" width="800" height="260" fill="#8a6a4a"/>'
b+='<path d="M140 180 L460 160 L480 600 L160 620Z" fill="#f4f0e4"/>'+''.join(f'<rect x="{170+(k%2)*150}" y="{220+(k//2)*60}" width="130" height="10" fill="#9a9a9a" transform="rotate(-3 300 400)"/>' for k in range(10))+'<rect x="170" y="190" width="280" height="30" fill="#3a3a3a" transform="rotate(-3 300 200)"/>'
b+='<path d="M480 480 L640 480 L630 620 L490 620Z" fill="#fff"/><path d="M640 510 Q700 510 690 560 Q680 600 634 590" stroke="#fff" stroke-width="16" fill="none"/><ellipse cx="560" cy="626" rx="110" ry="14" fill="#f4f4f4"/>'
b+='<path d="M500 492 Q516 480 530 490 Q544 480 556 492 Q530 506 500 492Z" fill="#e8102a"/>'
I[329]=svg(b,d)

# 642 愛のバクダン: a cartoon bomb with a heart-shaped body, its fuse sparkling as it rolls across the floor
d,b=bg([(0,'#ff4a6a'),(1,'#ff9a5a')])
b+=rays(400,420,20,'#ffe05a',.25,8)+heart(400,450,170,'#1a1a24')+'<ellipse cx="340" cy="380" rx="30" ry="18" fill="#fff" opacity=".4" transform="rotate(-30 340 380)"/>'
b+='<rect x="460" y="270" width="40" height="40" rx="8" fill="#3a3a44" transform="rotate(30 480 290)"/><path d="M490 270 Q540 200 600 210" stroke="#c8a060" stroke-width="10" fill="none"/>'+sparkle(610,206,50,'#ffe05a')+glow(610,206,40,'#fff',.7)
I[642]=svg(b,d)

# 643 さまよえる蒼い弾丸: a blue bullet of light streaking through a dark canyon, a trail of sparks behind it
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
b+='<path d="M-10 800 L-10 300 L120 260 L200 400 L180 800Z M810 800 L810 260 L680 300 L620 420 L640 800Z" fill="#141a2a"/>'
b+='<path d="M100 700 Q300 500 560 300" stroke="#2a8aff" stroke-width="30" fill="none" opacity=".3" stroke-linecap="round"/><path d="M200 620 Q360 470 560 300" stroke="#5ac8ff" stroke-width="14" fill="none" stroke-linecap="round"/>'
b+=glow(580,280,90,'#5ae0ff',.7)+'<g transform="rotate(-40 580 280)"><path d="M540 260 L610 260 Q650 280 610 300 L540 300Z" fill="#bff4ff"/></g>'
r=R(643)
for _ in range(16): t=r.uniform(0,1);x=100+t*460;y=700-t*400;b+=f'<circle cx="{x+r.uniform(-30,30):.0f}" cy="{y+r.uniform(-30,30):.0f}" r="3" fill="#bff4ff"/>'
I[643]=svg(b,d)

# 735 シーソーゲーム: a seesaw in a park at sunset, a big heart on one end and a small one flying up on the other
d,b=bg([(0,'#ffa86a'),(1,'#ffd8a0')])
b+=hinomaru_sun(400,320,100,'#fff2d0',.7)+'<rect y="600" width="800" height="200" fill="#6ab84a"/>'
b+='<path d="M360 620 L400 540 L440 620Z" fill="#c84a2a"/><g transform="rotate(-18 400 540)"><rect x="100" y="530" width="600" height="22" rx="10" fill="#e8b030"/></g>'
b+=heart(170,560,70,'#e8102a')+heart(620,260,40,'#ff7aa8')+'<path d="M640 340 L640 400 M610 330 L600 390 M670 330 L680 390" stroke="#fff" stroke-width="4" opacity=".7"/>'
I[735]=svg(b,d)

# 1499 Laughter: a pair of wings unfolding from a hospital-white window, sunlight pouring through
d,b=bg([(0,'#d8f0ff'),(1,'#fff8e0')])
b+=rays(400,400,20,'#fff',.5,8)+glow(400,400,200,'#fff4c8',.6)
for f in (1,-1): b+=''.join(f'<path d="M{400+f*40} 400 Q{400+f*(160+k*30)} {260+k*40} {400+f*(300-k*10)} {300+k*60} Q{400+f*(200+k*20)} {360+k*40} {400+f*40} {440}Z" fill="#fff" stroke="#d8e0ec" stroke-width="3"/>' for k in range(4))
b+='<rect x="360" y="340" width="80" height="140" rx="40" fill="#ffe8a0"/>'
I[1499]=svg(b,d)

# 1500 Stand By You: two umbrellas side by side in the rain, one tilted to shelter the other
d,b=bg([(0,'#5a6a8a'),(1,'#9aa8c0')])
b+=rain(90,1500,'#e8f0ff',.45,6)+'<rect y="660" width="800" height="140" fill="#3a4a5a"/>'
b+=wagasa(300,400,150,'#2a8ae8',0,'#5ab0ff')+wagasa(510,430,140,'#ffd02a',-18,'#ffe87a')
b+=figure(300,680,230,'#141a24')+figure(500,680,210,'#141a24',hair='#141a24')
I[1500]=svg(b,d)

# 1501 ホワイトノイズ: a TV screen full of white static, a blood-red hand print pressed on the glass
d,b=bg([(0,'#1a1a1a'),(1,'#0a0a0a')])
b+='<rect x="100" y="140" width="600" height="460" rx="40" fill="#3a3a3a"/><rect x="140" y="180" width="520" height="380" rx="20" fill="#d8d8d8"/>'
r=R(1501)
for _ in range(500): x,y=r.uniform(150,650),r.uniform(190,550);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{r.uniform(4,14):.0f}" height="4" fill="{r.choice(["#fff","#888","#444","#bbb"])}"/>'
b+='<g fill="#c80a1a" opacity=".85"><ellipse cx="430" cy="420" rx="56" ry="66"/>'+''.join(f'<rect x="{384+k*24}" y="{290+abs(k-1.5)*12:.0f}" width="20" height="100" rx="10"/>' for k in range(4))+'<rect x="360" y="400" width="20" height="80" rx="10" transform="rotate(-40 370 440)"/></g>'
b+='<rect x="340" y="600" width="120" height="80" fill="#2a2a2a"/>'
I[1501]=svg(b,d)

# 1526 UNDEAD: a black rose blooming from a cracked gravestone under a blood-red full moon
d,b=bg([(0,'#1a0408'),(1,'#0a0204')])
b+=moon(400,220,120,'#e8302a')+glow(400,220,180,'#e8102a',.35)
b+='<path d="M280 720 L280 440 Q280 360 400 360 Q520 360 520 440 L520 720Z" fill="#5a5a64"/>'+bolt([(400,370),(380,450),(420,500),(390,580)],'#2a2a34',8,1)
b+='<rect y="700" width="800" height="100" fill="#140a0a"/><path d="M460 700 Q470 600 460 540" stroke="#1a3a1a" stroke-width="8" fill="none"/>'+'<g transform="translate(460 520) scale(.8)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#0a0a0a',1),(60,'#1a1a1a',.9),(-60,'#1a1a1a',.9),(150,'#2a0a0a',.7),(-150,'#2a0a0a',.7)])+'</g>'
I[1526]=svg(b,d)

# 1556 踊り子: a dancer's red skirt swirling into a perfect circle, petals spinning off its hem
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=glow(400,480,240,'#ff5a7a',.3)
b+='<path d="M400 380 Q160 520 220 640 Q400 700 580 640 Q640 520 400 380Z" fill="#e8102a"/><path d="M400 380 Q260 520 300 640 M400 380 Q400 540 400 680 M400 380 Q540 520 500 640" stroke="#a80a1a" stroke-width="5" fill="none"/>'
b+='<g fill="#0a0a14"><circle cx="400" cy="220" r="34"/><path d="M372 260 L428 260 L420 390 L380 390Z"/><path d="M380 270 Q320 220 290 160 M420 270 Q480 240 520 200" stroke="#0a0a14" stroke-width="14" fill="none" stroke-linecap="round"/></g>'
b+=petals(14,1556,'#ff7a8a',500,800,8,14,.8)
I[1556]=svg(b,d)

# 1563 きらり: sunlight glinting off the windscreen of a car driving along a coastal highway at full speed
d,b=bg([(0,'#4ab0f8'),(1,'#d8f0ff')])
b+='<rect y="360" width="800" height="160" fill="#1a90d8"/><path d="M-10 520 L810 480 L810 810 L-10 810Z" fill="#8a8a94"/><path d="M-10 640 L810 590" stroke="#fff" stroke-width="10" stroke-dasharray="60 40"/>'
b+='<path d="M200 600 Q210 540 280 530 L360 480 Q420 460 500 470 L560 520 Q620 530 630 580 L630 620 L200 620Z" fill="#f4f4f4"/><path d="M370 490 L420 474 L490 480 L530 520 L340 530Z" fill="#5ab0e8"/>'
for x in (280,560): b+=f'<circle cx="{x}" cy="620" r="40" fill="#1a1a24"/><circle cx="{x}" cy="620" r="14" fill="#c8c8d0"/>'
b+=sparkle(470,490,90,'#fff')+glow(470,490,60,'#fff',.7)
I[1563]=svg(b,d)

# 1612 シンデレラガール: a glass slipper on a palace staircase at midnight, a clock tower striking twelve behind it
d,b=bg([(0,'#1a1a5a'),(1,'#3a2a7a')])
b+=starsf(40,1612,400,'#fff')+'<rect x="520" y="80" width="140" height="400" fill="#2a2a5a"/><circle cx="590" cy="200" r="50" fill="#f4ecd8"/><path d="M590 200 L590 160 M590 200 L594 162" stroke="#1a1a2a" stroke-width="6"/>'
for k in range(6): b+=f'<rect x="{-10}" y="{500+k*50}" width="820" height="50" fill="{["#e8e0f4","#d0c8e8"][k%2]}"/>'
b+='<path d="M300 580 Q300 520 340 520 Q380 530 400 560 L480 580 Q500 590 490 600 L300 600Z" fill="#d8f0ff" opacity=".85" stroke="#fff" stroke-width="5"/><path d="M310 600 L314 640 L330 640 L326 600" fill="#d8f0ff" opacity=".85"/>'+sparkle(360,540,30,'#fff')
I[1612]=svg(b,d)

# 303 め組のひと: a firemen's matoi standard twirling above a summer crowd, sunglasses glinting on a tanned beach
d,b=bg([(0,'#ff8a1a'),(1,'#ffd04a')])
b+=rays(400,300,20,'#fff',.25,9)+'<rect y="560" width="800" height="240" fill="#f4d890"/>'
b+='<rect x="390" y="300" width="20" height="420" fill="#5a3a1a"/><path d="M340 200 L460 200 L470 300 L330 300Z" fill="#fff"/><circle cx="400" cy="170" r="40" fill="#e8102a"/>'+''.join(f'<rect x="{336+k*16}" y="300" width="10" height="120" fill="#fff"/>' for k in range(8))
b+='<g transform="translate(400 600)"><ellipse cx="-90" cy="0" rx="76" ry="50" fill="#1a1a24"/><ellipse cx="90" cy="0" rx="76" ry="50" fill="#1a1a24"/><path d="M-20 -10 Q0 -24 20 -10" stroke="#1a1a24" stroke-width="12" fill="none"/><ellipse cx="-110" cy="-16" rx="20" ry="10" fill="#fff" opacity=".6"/></g>'
I[303]=svg(b,d)

# 937 情熱: a flamenco-red flame leaping from a single match struck in total darkness
d,b=bg([(0,'#0a0404'),(1,'#1a0808')])
b+=glow(400,340,240,'#ff3a1a',.45)
b+='<path d="M400 140 Q520 300 470 420 Q450 480 400 500 Q350 480 330 420 Q280 300 400 140Z" fill="#e8301a"/><path d="M400 260 Q460 360 440 430 Q420 470 400 476 Q380 470 360 430 Q340 360 400 260Z" fill="#ffa82a"/><path d="M400 360 Q430 420 400 460 Q370 420 400 360Z" fill="#fff4c8"/>'
b+='<rect x="390" y="500" width="20" height="260" fill="#e8c890"/><ellipse cx="400" cy="506" rx="18" ry="22" fill="#5a1a0a"/>'
I[937]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
