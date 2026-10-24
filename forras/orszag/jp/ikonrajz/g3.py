import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 3. csoport, 2026-10-24
I={}

# 1424 新宝島: an old treasure map unrolled, a red X, a tiny ship and a compass rose on a parchment sea
d,b=bg([(0,'#1a4a6a'),(1,'#0a2a4a')])
b+='<g transform="rotate(-6 400 420)"><rect x="110" y="160" width="580" height="500" rx="10" fill="#f0dca8"/><rect x="110" y="160" width="580" height="500" rx="10" fill="none" stroke="#a8783a" stroke-width="8"/>'
b+='<ellipse cx="140" cy="410" rx="40" ry="260" fill="#d8b878"/><ellipse cx="660" cy="410" rx="40" ry="260" fill="#d8b878"/>'
b+='<path d="M260 300 Q360 220 470 280 Q560 330 520 440 Q470 540 360 520 Q240 500 250 400Z" fill="#b8d88a" stroke="#7a5a2a" stroke-width="5"/>'
b+='<path d="M300 420 q40 -60 80 -10 t80 0" stroke="#8a3a1a" stroke-width="5" stroke-dasharray="12 10" fill="none"/>'
b+='<path d="M440 380 L490 430 M490 380 L440 430" stroke="#d8201a" stroke-width="14" stroke-linecap="round"/>'
b+='<g transform="translate(560 560)"><path d="M0 -50 L10 -10 L50 0 L10 10 L0 50 L-10 10 L-50 0 L-10 -10Z" fill="#5a3a1a"/><circle r="8" fill="#d8201a"/></g>'
b+='<g transform="translate(220 560)"><path d="M-40 0 L40 0 L30 18 L-30 18Z" fill="#5a3a1a"/><path d="M0 0 L0 -50 L30 -10Z" fill="#fff"/></g></g>'
I[1424]=svg(b,d)

# 1581 ビターバカンス: a summer cocktail with a dark chocolate rim on a hot beach, a striped parasol leaning overhead
d,b=bg([(0,'#2ac8e8'),(.6,'#8ae8f8'),(1,'#f8e0a0')])
b+='<rect y="500" width="800" height="300" fill="#f4d890"/><rect y="460" width="800" height="50" fill="#1a9ac8"/>'
b+='<path d="M120 120 Q330 30 560 160Z" fill="#ff5a5a"/><path d="M200 92 Q340 50 420 110 Z" fill="#fff"/><path d="M340 100 L470 640" stroke="#7a5a3a" stroke-width="10"/>'
b+='<path d="M380 440 L620 440 L560 600 L440 600Z" fill="#ffb05a" opacity=".85"/><path d="M380 440 L620 440 L610 466 L390 466Z" fill="#4a2414"/>'
b+='<rect x="490" y="600" width="20" height="110" fill="#e8f4ff" opacity=".8"/><ellipse cx="500" cy="716" rx="70" ry="14" fill="#e8f4ff" opacity=".8"/>'
b+='<circle cx="600" cy="430" r="34" fill="#ffd82a"/><path d="M560 300 L520 470" stroke="#ff4a8a" stroke-width="8"/>'
I[1581]=svg(b,d)

# 1452 シュガーソングとビターステップ: sugar cubes and coffee beans dancing across a black-and-white checkered floor
d,b=bg([(0,'#3a1a10'),(1,'#1a0a08')])
for i in range(10):
    for j in range(5):
        if (i+j)%2: b+=f'<rect x="{i*80}" y="{480+j*64}" width="80" height="64" fill="#f4ece0"/>'
        else: b+=f'<rect x="{i*80}" y="{480+j*64}" width="80" height="64" fill="#2a1a14"/>'
b+=glow(400,300,200,'#ffd8a0',.35)
for x,y,a in [(250,330,-14),(420,240,10),(560,360,-6)]:
    b+=f'<g transform="rotate({a} {x} {y})"><rect x="{x-60}" y="{y-60}" width="120" height="120" rx="12" fill="#fff"/><path d="M{x-60} {y-60} l20 -20 l120 0 l-20 20Z" fill="#f0f0f0"/><path d="M{x+60} {y-60} l20 -20 l0 120 l-20 20Z" fill="#d8d8d8"/></g>'
for x,y,a in [(160,500,30),(340,470,-20),(500,520,40),(660,480,-30)]:
    b+=f'<g transform="rotate({a} {x} {y})"><ellipse cx="{x}" cy="{y}" rx="36" ry="48" fill="#5a2a10"/><path d="M{x} {y-44} Q{x-14} {y} {x} {y+44}" stroke="#2a0a04" stroke-width="6" fill="none"/></g>'
I[1452]=svg(b,d)

# 1094 花: a single pale flower opening in a soft rain, petals catching the light as drops fall
d,b=bg([(0,'#8aa8c8'),(1,'#c8d8e8')])
b+=glow(400,380,220,'#ffffff',.5)+rain(70,1094,'#ffffff',.5,5)
b+='<path d="M400 800 Q390 640 410 470" stroke="#4a7a3a" stroke-width="12" fill="none"/><path d="M402 640 Q330 590 310 540 Q370 560 404 610Z" fill="#5a9a4a"/><path d="M404 580 Q470 540 500 490 Q440 500 404 560Z" fill="#5a9a4a"/>'
b+=flower(410,400,190,6,'#ffe8f0','#ffd84a',8,.7)+flower(410,400,110,6,'#ffc8dc','#ffd84a',38,.7)
b+='<circle cx="410" cy="400" r="34" fill="#ffd84a"/>'
for x,y in [(330,330),(500,350),(440,300)]: b+=f'<ellipse cx="{x}" cy="{y}" rx="7" ry="10" fill="#fff" opacity=".9"/>'
I[1094]=svg(b,d)

# 306 とんぼ: a dragonfly hovering above the Tokyo skyline at a dusty orange sunset
d,b=bg([(0,'#5a2a3a'),(.5,'#e86a3a'),(1,'#ffc86a')])
b+=hinomaru_sun(400,560,110,'#ffe8a0',.9)+skyline(620,'#2a1018',306,80,300,'#ffd27a',50)
b+=tokyo_tower(640,620,300,'#3a1418','#3a1418')
b+='<g transform="translate(360 300) rotate(-12)" fill="#1a0a0a"><rect x="-8" y="-20" width="16" height="200" rx="8"/><circle cy="-30" r="22"/>'
for sx in (-1,1):
    for k,(w,a) in enumerate([(200,-8),(180,10)]):
        b+=f'<ellipse cx="{sx*w/2+sx*6}" cy="{k*30}" rx="{w/2}" ry="22" fill="#fff6e0" opacity=".55" transform="rotate({sx*a} 0 {k*30})" stroke="#1a0a0a" stroke-width="4"/>'
b+='</g>'
I[306]=svg(b,d)

# 975 COLORS: a fan of colour swatch cards spread open, every card a bold saturated hue
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
cols=['#e8202a','#ff7a1a','#ffd21a','#3ac84a','#1a9ae8','#3a3ae8','#9a2ae8','#ff3a9a']
for k,c in enumerate(cols):
    a=-70+k*20
    b+=f'<g transform="rotate({a} 400 640)"><rect x="350" y="200" width="100" height="440" rx="14" fill="{c}"/><rect x="350" y="560" width="100" height="80" rx="14" fill="#fff" opacity=".9"/></g>'
b+='<circle cx="400" cy="640" r="22" fill="#d8d8e0"/>'
I[975]=svg(b,d)

# 1476 Karasu: a single crow perched on a power line against a blood-orange dusk, wires crossing the sky
d,b=bg([(0,'#2a1a3a'),(.55,'#c84a3a'),(1,'#ffb05a')])
b+=hinomaru_sun(560,560,100,'#ffd890',.8)+skyline(700,'#1a0a14',1476,40,160)
b+='<path d="M-10 300 Q400 380 810 280 M-10 340 Q400 430 810 330" stroke="#140a0a" stroke-width="4" fill="none"/><rect x="680" y="200" width="18" height="600" fill="#140a0a"/><rect x="640" y="250" width="100" height="10" fill="#140a0a"/>'
b+='<g fill="#08040a"><path d="M330 356 Q300 300 340 270 Q370 250 400 270 L440 262 L410 284 Q440 320 420 360 Q380 380 330 356Z"/><path d="M330 356 L270 400 L300 360Z"/><path d="M370 360 L366 380 M390 362 L392 382" stroke="#08040a" stroke-width="5"/></g><circle cx="402" cy="276" r="4" fill="#ffd27a"/>'
I[1476]=svg(b,d)

# 1174 キセキ: a baseball soaring into a dawn sky above a diamond, its red stitches trailing a streak of light
d,b=bg([(0,'#2a5ac8'),(.6,'#ffb07a'),(1,'#ffe8b0')])
b+='<path d="M-10 620 Q400 560 810 620 L810 810 L-10 810Z" fill="#3a8a3a"/><path d="M400 560 L620 680 L400 800 L180 680Z" fill="#c8945a"/><rect x="390" y="660" width="20" height="20" fill="#fff" transform="rotate(45 400 670)"/>'
b+='<path d="M200 520 Q350 300 470 250" stroke="#fff8e0" stroke-width="20" fill="none" opacity=".5" stroke-linecap="round"/>'
b+=glow(520,220,100,'#ffffff',.6)+'<circle cx="520" cy="220" r="70" fill="#fbfbf6"/><path d="M470 170 Q500 220 470 270 M570 170 Q540 220 570 270" stroke="#d81a2a" stroke-width="5" fill="none" stroke-dasharray="6 6"/>'
I[1174]=svg(b,d)

# 1582 breakfast: a sunny-side-up egg on toast, orange juice and a coffee cup on a table by a bright morning window
d,b=bg([(0,'#fff6e0'),(1,'#ffe0b0')])
b+='<rect x="460" y="80" width="260" height="300" fill="#a8dcff"/><path d="M590 80 L590 380 M460 230 L720 230" stroke="#fff" stroke-width="10"/>'+glow(590,230,140,'#ffffff',.5)
b+='<rect y="480" width="800" height="320" fill="#e8b878"/>'
b+='<rect x="140" y="420" width="260" height="220" rx="30" fill="#d89a4a"/><rect x="160" y="440" width="220" height="180" rx="24" fill="#f4d090"/><ellipse cx="270" cy="530" rx="90" ry="70" fill="#fff"/><circle cx="280" cy="520" r="32" fill="#ffb81a"/>'
b+='<path d="M470 420 L540 420 L530 600 L480 600Z" fill="#ffa81a" opacity=".9"/><path d="M470 420 L540 420 L536 450 L474 450Z" fill="#fff" opacity=".5"/>'
b+='<rect x="580" y="500" width="110" height="100" rx="12" fill="#fff"/><path d="M690 520 Q730 530 724 560 Q718 586 690 580" stroke="#fff" stroke-width="12" fill="none"/>'
I[1582]=svg(b,d)

# 1436 紅蓮の弓矢: a towering stone wall under a crimson sky, a volley of burning arrows arcing over it
d,b=bg([(0,'#3a0408'),(.6,'#a81a14'),(1,'#ff6a2a')])
b+='<rect x="0" y="380" width="800" height="420" fill="#5a4a44"/>'
for j in range(7):
    for i in range(11): b+=f'<rect x="{i*80-(j%2)*40}" y="{380+j*60}" width="76" height="56" fill="#6a5a54" stroke="#3a2a28" stroke-width="3"/>'
b+='<rect x="0" y="360" width="800" height="30" fill="#4a3a34"/>'
for k in range(9):
    x=60+k*85;y=120+(k%3)*60
    b+=f'<g transform="rotate(-28 {x} {y})"><path d="M{x-150} {y} L{x-60} {y}" stroke="#ffb02a" stroke-width="12" opacity=".6" stroke-linecap="round"/><rect x="{x-70}" y="{y-5}" width="150" height="10" fill="#1a0804"/><path d="M{x+80} {y-18} L{x+120} {y} L{x+80} {y+18}Z" fill="#1a0804"/><path d="M{x-70} {y} l-20 -16 l30 0Z M{x-70} {y} l-20 16 l30 0Z" fill="#f4e8d8"/></g>'
I[1436]=svg(b,d)

# 627 LOVE PHANTOM: a white phantom mask and a single red rose lying on black velvet under a stage light
d,b=bg([(0,'#0a0004'),(1,'#200410')])
b+='<polygon points="400,-20 160,800 640,800" fill="#ffffff" opacity=".07"/>'+glow(400,420,200,'#a01030',.4)
b+='<path d="M250 300 Q400 230 550 300 Q570 420 500 500 Q440 540 400 520 Q360 540 300 500 Q230 420 250 300Z" fill="#f4f4f0"/>'
b+='<ellipse cx="335" cy="380" rx="40" ry="24" fill="#0a0004"/><ellipse cx="465" cy="380" rx="40" ry="24" fill="#0a0004"/>'
b+='<path d="M200 640 Q350 600 500 540" stroke="#2a5a2a" stroke-width="10" fill="none"/>'
b+='<g transform="translate(520 530)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({s})"/>' for a,c,s in [(0,'#a8081e',1),(60,'#c81028',.9),(-60,'#c81028',.9),(150,'#e01a34',.7),(-150,'#e01a34',.7)])+'</g>'
I[627]=svg(b,d)

# 976 Movin'on without you: red taillights of a car speeding away on a night highway, the city glow behind
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=skyline(420,'#141428',976,60,200,'#ffd27a',80)
b+='<path d="M-10 800 L360 420 L440 420 L810 800Z" fill="#1a1a24"/>'
for k in range(6): b+=f'<rect x="{396-k*2}" y="{440+k*k*10}" width="{8+k*4}" height="{14+k*6}" fill="#ffd27a"/>'
b+='<path d="M60 800 L370 430" stroke="#ff2a3a" stroke-width="10" opacity=".55"/><path d="M180 800 L384 430" stroke="#ff2a3a" stroke-width="7" opacity=".45"/>'
b+='<path d="M740 800 L430 430" stroke="#fff6c8" stroke-width="8" opacity=".35"/>'
b+='<path d="M330 560 L470 560 L490 610 L310 610Z" fill="#14141c"/><rect x="310" y="600" width="180" height="40" rx="8" fill="#1a1a24"/>'+glow(330,615,26,'#ff2a3a',.9,'glow2')+glow(470,615,26,'#ff2a3a',.9,'glow2')+'<rect x="316" y="608" width="34" height="14" rx="4" fill="#ff4a5a"/><rect x="450" y="608" width="34" height="14" rx="4" fill="#ff4a5a"/>'
I[976]=svg(b,d)

# 1163 again: a cracked pocket watch hanging on its chain in front of a sunrise, hands about to turn again
d,b=bg([(0,'#3a2a5a'),(.6,'#e88a5a'),(1,'#ffd8a0')])
b+=rays(400,620,18,'#fff2c8',.2,6)+hinomaru_sun(400,640,120,'#ffe8b0',.9)
b+='<path d="M400 0 L400 200" stroke="#c8a040" stroke-width="8" stroke-dasharray="14 6"/><rect x="380" y="190" width="40" height="40" rx="10" fill="#c8a040"/>'
b+='<circle cx="400" cy="400" r="180" fill="#d8b050"/><circle cx="400" cy="400" r="150" fill="#fbf6e8"/>'
for k in range(12): a=math.radians(k*30);b+=f'<rect x="{400+130*math.sin(a)-4:.0f}" y="{400-130*math.cos(a)-10:.0f}" width="8" height="20" fill="#3a2a1a" transform="rotate({k*30} {400+130*math.sin(a):.0f} {400-130*math.cos(a):.0f})"/>'
b+='<path d="M400 400 L400 300 M400 400 L470 440" stroke="#3a2a1a" stroke-width="10" stroke-linecap="round"/>'
b+=bolt([(330,280),(380,350),(350,420),(400,480)],'#5a4a3a',4,.8)
I[1163]=svg(b,d)

# 628 ultra soul: a clenched fist punching up out of a pool, a huge victory splash bursting around it
d,b=bg([(0,'#0a3a8a'),(1,'#0a6ac8')])
b+=rays(400,420,24,'#ffffff',.12,5)+glow(400,380,220,'#bfe8ff',.5)
b+='<rect y="560" width="800" height="240" fill="#0a8ad8"/>'+''.join(f'<rect x="0" y="{590+k*50}" width="800" height="5" fill="#fff" opacity=".25"/>' for k in range(4))
r=R(628)
for k in range(18):
    a=math.radians(-160+k*8);L=r.uniform(160,300)
    b+=f'<path d="M400 560 Q{400+L*.5*math.cos(a):.0f} {560+L*.6*math.sin(a):.0f} {400+L*math.cos(a):.0f} {560+L*.9*math.sin(a):.0f}" stroke="#e8f8ff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".85"/>'
b+='<path d="M360 600 L370 380 L440 380 L450 600Z" fill="#e8b890"/><rect x="340" y="250" width="130" height="150" rx="40" fill="#e8b890"/>'
for k in range(4): b+=f'<path d="M{350+k*30} 270 L{350+k*30} 330" stroke="#c89070" stroke-width="5"/>'
I[628]=svg(b,d)

# 690 負けないで: a marathon runner breaking the finish tape at the end of a long road, arms flung wide
d,b=bg([(0,'#4aa8f8'),(.7,'#ffd88a'),(1,'#ffb06a')])
b+=rays(400,560,22,'#fff6d8',.25,6)
b+='<path d="M-10 800 L360 500 L440 500 L810 800Z" fill="#8a8a94"/><path d="M398 520 L402 520 L420 800 L380 800Z" fill="#fff" opacity=".6"/>'
b+='<path d="M80 600 L720 600" stroke="#ff3a3a" stroke-width="10"/><rect x="60" y="560" width="14" height="240" fill="#3a3a44"/><rect x="726" y="560" width="14" height="240" fill="#3a3a44"/>'
b+=figure(400,800,360,'#1a1a2a',pose='up')+'<rect x="372" y="580" width="56" height="36" fill="#fff"/><text x="400" y="607" text-anchor="middle" font-family="DejaVu Sans" font-weight="700" font-size="24" fill="#e8302a">24</text>'
I[690]=svg(b,d)

# 831 HOWEVER: a single red rose resting on a frosted windowsill while snow falls softly outside
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=snow(90,831)+'<rect x="120" y="100" width="560" height="440" fill="#2a3a5a" stroke="#e8e8f0" stroke-width="20"/><path d="M400 100 L400 540 M120 320 L680 320" stroke="#e8e8f0" stroke-width="14"/>'
b+=glow(400,620,200,'#ffd8a0',.35)+'<rect y="540" width="800" height="260" fill="#5a3a2a"/><rect x="100" y="530" width="600" height="30" fill="#f4f0ec"/>'
b+='<path d="M200 600 Q380 590 520 560" stroke="#2a5a2a" stroke-width="10" fill="none"/>'
b+='<g transform="translate(540 556) rotate(70)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({s})"/>' for a,c,s in [(0,'#a8081e',1),(60,'#c81028',.9),(-60,'#c81028',.9),(150,'#e01a34',.7),(-150,'#e01a34',.7)])+'</g>'
I[831]=svg(b,d)

# 813 波乗りジョニー: a surfer carving a sparkling turquoise wave under a blazing summer sun
d,b=bg([(0,'#1aa8e8'),(1,'#9ae8ff')])
b+=glow(640,140,110,'#fff6c8',.8)+'<circle cx="640" cy="140" r="56" fill="#fff8d8"/>'
b+='<path d="M-10 800 L-10 360 Q200 240 420 300 Q600 360 640 520 Q560 420 470 440 Q400 460 430 540 L520 800Z" fill="#0a8ac8"/>'
b+='<path d="M420 300 Q600 360 640 520 Q600 430 520 400 Q460 380 420 300Z" fill="#e8fbff"/>'
b+='<rect y="600" width="800" height="200" fill="#0aa8d8"/>'
b+='<g transform="rotate(-24 380 560)"><ellipse cx="380" cy="580" rx="140" ry="20" fill="#ffd82a"/></g>'+figure(380,560,190,'#1a1a2a',pose='up')
I[813]=svg(b,d)

# 929 硝子の少年: a boy's silhouette reflected in shards of shattered blue glass, the pieces scattering
d,b=bg([(0,'#0a1a3a'),(1,'#1a3a6a')])
b+=glow(400,400,240,'#8ad0ff',.35)
r=R(929)
for k in range(14):
    cx,cy=r.uniform(120,680),r.uniform(120,680);s=r.uniform(40,110)
    pts=' '.join(f'{cx+s*math.cos(a)*r.uniform(.5,1):.0f},{cy+s*math.sin(a)*r.uniform(.5,1):.0f}' for a in [0,2.1,4.2])
    b+=f'<polygon points="{pts}" fill="#bfe6ff" opacity=".22" stroke="#e8f8ff" stroke-width="3"/>'
b+=figure(400,700,380,'#06102a',hair='#06102a')
b+=bolt([(360,200),(420,320),(380,420),(450,560)],'#e8f8ff',4,.9)
I[929]=svg(b,d)

# 881 そばかす: a cheerful freckled sun with round sunglasses pushed up, beaming over a candy-striped sky
d,b=bg([(0,'#ffe0f0'),(1,'#ffd0a0')])
for k in range(-4,12): b+=f'<polygon points="{k*90},800 {k*90+40},800 {k*90+440},0 {k*90+400},0" fill="#fff" opacity=".35"/>'
b+=rays(400,400,16,'#ffb02a',.35,9)
b+='<circle cx="400" cy="400" r="180" fill="#ffc83a"/>'
for x,y in [(330,440),(350,460),(310,460),(470,440),(450,460),(490,460)]: b+=f'<circle cx="{x}" cy="{y}" r="7" fill="#d8782a"/>'
b+='<path d="M330 500 Q400 560 470 500" stroke="#7a3a0a" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="340" cy="390" r="14" fill="#7a3a0a"/><circle cx="460" cy="390" r="14" fill="#7a3a0a"/>'
b+='<circle cx="335" cy="300" r="46" fill="#ff5aa8" stroke="#2a1a3a" stroke-width="8"/><circle cx="465" cy="300" r="46" fill="#ff5aa8" stroke="#2a1a3a" stroke-width="8"/><path d="M381 300 L419 300" stroke="#2a1a3a" stroke-width="8"/>'
I[881]=svg(b,d)

# 307 乾杯: two foaming beer mugs clinking together in a warm golden glow, droplets flying
d,b=bg([(0,'#3a1a0a'),(1,'#7a3a12')])
b+=glow(400,380,240,'#ffc860',.5)
for x,a in [(300,-16),(500,16)]:
    b+=f'<g transform="rotate({a} {x} 500)"><rect x="{x-80}" y="320" width="160" height="300" rx="18" fill="#ffb81a" opacity=".92"/><path d="M{x+80} 380 Q{x+150} 390 {x+140} 470 Q{x+130} 540 {x+80} 540" stroke="#ffe8a0" stroke-width="22" fill="none" opacity=".8"/>'
    b+=f'<path d="M{x-90} 330 Q{x-80} 260 {x-30} 280 Q{x} 240 {x+40} 276 Q{x+90} 260 {x+90} 330Z" fill="#fffaf0"/><rect x="{x-60}" y="360" width="16" height="230" rx="8" fill="#fff" opacity=".3"/></g>'
for x,y in [(400,250),(370,210),(440,220),(410,170)]: b+=f'<ellipse cx="{x}" cy="{y}" rx="8" ry="12" fill="#fff6d8" opacity=".9"/>'
b+=sparkle(400,300,30,'#fff')
I[307]=svg(b,d)

# 629 イチブトゼンブ: a red heart made of puzzle pieces, the very last piece floating in to complete it
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a7a')])
b+=glow(400,420,220,'#ff7a9a',.35)+heart(380,440,170,'#d81a3a')
b+='<path d="M380 280 L380 640 M220 440 L540 440" stroke="#8a0a1a" stroke-width="6"/>'
for x,y in [(380,360),(300,440),(460,440),(380,540)]: b+=f'<circle cx="{x}" cy="{y}" r="18" fill="#8a0a1a"/>'
b+='<g transform="translate(560 210) rotate(18)"><rect x="-60" y="-60" width="120" height="120" rx="6" fill="#ff3a5a"/><circle cx="0" cy="66" r="20" fill="#ff3a5a"/><circle cx="-66" cy="0" r="20" fill="#3a4a7a"/></g>'
b+='<path d="M520 270 q-30 40 -60 60" stroke="#fff" stroke-width="4" stroke-dasharray="8 8" fill="none" opacity=".6"/>'
I[629]=svg(b,d)

# 986 SEASONS: a circle split into four seasons, sakura, summer sun, maple leaves and snow turning together
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
for k,(c,a) in enumerate([('#ffc8dc',-90),('#5ac8ff',0),('#ff8a3a',90),('#e8f0ff',180)]):
    a0,a1=math.radians(a),math.radians(a+90)
    b+=f'<path d="M400 400 L{400+300*math.cos(a0):.0f} {400+300*math.sin(a0):.0f} A300 300 0 0 1 {400+300*math.cos(a1):.0f} {400+300*math.sin(a1):.0f}Z" fill="{c}"/>'
b+=sakura(520,260,80)+'<circle cx="520" cy="540" r="60" fill="#ffd82a"/>'+''.join(f'<path d="M{280+k*30} {500+k*24} l20 -30 l20 30 l-20 -8Z" fill="#c8301a"/>' for k in range(3))
for x,y in [(280,240),(320,280),(250,300),(300,200)]: b+=f'<circle cx="{x}" cy="{y}" r="9" fill="#9ab8e8"/>'
b+='<circle cx="400" cy="400" r="300" fill="none" stroke="#fff" stroke-width="8"/><circle cx="400" cy="400" r="40" fill="#2a2a3a"/>'
I[986]=svg(b,d)

# 243 春よ、来い: a plum branch in blossom shaking off the last snow, warm spring light breaking through
d,b=bg([(0,'#c8d8f0'),(.6,'#f8e8e0'),(1,'#ffe0c8')])
b+=glow(560,240,220,'#fff6d8',.8)
b+='<path d="M0 520 Q220 470 400 430 Q520 400 640 300 M300 450 Q340 380 330 300 M480 410 Q560 420 640 460" stroke="#4a2a1a" stroke-width="16" fill="none" stroke-linecap="round"/>'
for x,y in [(640,300),(560,380),(330,300),(420,430),(640,460),(250,470),(500,340)]:
    b+=flower(x,y,46,5,'#ff7aa0','#ffe08a',x%60,.9)
b+='<path d="M260 470 q30 -14 60 -6 M450 420 q30 -10 50 -4" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'
b+=snow(30,243,.7,500)
I[243]=svg(b,d)

# 1192 Happiness: five little figures leaping along a sunny road under a bright rainbow
d,b=bg([(0,'#5ac0ff'),(1,'#c8f0ff')])
for k,c in enumerate(['#ff4a4a','#ffa82a','#ffe02a','#4ac84a','#2a8aff','#8a4aff']): b+=f'<path d="M{60+k*22} 560 A{340-k*22} {340-k*22} 0 0 1 {740-k*22} 560" stroke="{c}" stroke-width="22" fill="none"/>'
b+='<rect y="560" width="800" height="240" fill="#7ad86a"/><path d="M-10 800 L340 560 L460 560 L810 800Z" fill="#e8d0a0"/>'
for x,y,c,p in [(220,700,'#2a8aff','up'),(320,660,'#ffd82a','wave'),(400,640,'#e8302a','up'),(480,660,'#4ac84a','wave'),(580,700,'#8a4aff','up')]: b+=figure(x,y,140,c,pose=p)
I[1192]=svg(b,d)

# 1462 アイネクライネ: a tiny music box opened under a lamp, a little paper star spinning on top, notes drifting up
d,b=bg([(0,'#2a2a4a'),(1,'#4a3a5a')])
b+=glow(400,420,220,'#ffd8a0',.45)
b+='<path d="M220 480 L580 480 L560 640 L240 640Z" fill="#8a4a2a"/><path d="M220 480 L580 480 L560 360 L240 360Z" fill="#a8603a"/><rect x="250" y="490" width="300" height="20" fill="#d8a85a"/>'
b+='<rect x="390" y="380" width="20" height="100" fill="#d8b85a"/><g transform="translate(400 330)"><path d="'+' '.join(f'{"M" if k==0 else "L"}{60*(1 if k%2==0 else .42)*math.sin(k*math.pi/5):.1f} {-60*(1 if k%2==0 else .42)*math.cos(k*math.pi/5):.1f}' for k in range(10))+'Z" fill="#ffe86a"/></g>'
b+=note(250,250,26,'#fff6d8')+note(560,200,22,'#fff6d8',True)+note(620,330,18,'#fff6d8')
I[1462]=svg(b,d)

# 977 誰かの願いが叶うころ: a shooting star streaking over a sleeping snowy town, one window still lit
d,b=bg([(0,'#04081e'),(1,'#1a2a4a')])
b+=starsf(90,977,520,'#e8f0ff')+'<path d="M180 120 L560 300" stroke="#fff" stroke-width="6" opacity=".7"/>'+glow(570,305,40,'#fff6d8',.9,'glow2')+sparkle(570,305,30,'#fff')
b+='<path d="M-10 600 Q400 560 810 600 L810 810 L-10 810Z" fill="#e8f0fa"/>'
for x,h in [(120,120),(260,150),(420,130),(580,160)]:
    b+=f'<rect x="{x}" y="{600-h+40}" width="110" height="{h}" fill="#1a2238"/><path d="M{x-10} {600-h+44} L{x+55} {600-h-10} L{x+120} {600-h+44}Z" fill="#f4f8ff"/>'
b+='<rect x="460" y="540" width="30" height="30" fill="#ffd27a"/>'+glow(475,555,40,'#ffd27a',.6,'glow2')
I[977]=svg(b,d)

# 978 Flavor Of Life: a ripe strawberry half-dipped in white chocolate, sweet and a little sour, on a pink plate
d,b=bg([(0,'#ffe8ee'),(1,'#ffc8d4')])
b+='<ellipse cx="400" cy="640" rx="260" ry="50" fill="#fff"/>'
d+=rg('sb',S((0,'#ff7a7a'),(.6,'#e8102a'),(1,'#8a0010')),.4,.35,.7)
b+='<path d="M400 660 Q250 600 250 420 Q260 300 400 300 Q540 300 550 420 Q550 600 400 660Z" fill="url(#sb)"/>'
b+='<path d="M250 420 Q260 300 400 300 Q540 300 550 420 Q500 470 400 440 Q300 470 250 420Z" fill="#fffaf0"/>'
r=R(978)
for _ in range(16): x,y=r.uniform(290,510),r.uniform(470,610);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="5" ry="8" fill="#ffe08a"/>'
b+='<path d="M400 300 L340 250 L380 270 L400 220 L420 270 L460 250Z" fill="#3a9a3a"/>'
I[978]=svg(b,d)

# 1082 さくら: a riverside path under cherry trees in full bloom, petals blowing in a pink blizzard
d,b=bg([(0,'#bfe0ff'),(1,'#ffe8f0')])
b+='<path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#7aba6a"/><path d="M300 810 Q380 700 420 640 L480 640 Q460 720 520 810Z" fill="#7ac0e8"/>'
for x,y,s in [(120,380,1.3),(660,360,1.4),(330,300,1.0)]:
    b+=f'<path d="M{x} 660 Q{x+10} {y+80} {x-10} {y}" stroke="#4a2a1a" stroke-width="{26*s}" fill="none"/>'
    r=R(int(x))
    for _ in range(30): b+=f'<circle cx="{x+r.uniform(-140,140)*s:.0f}" cy="{y+r.uniform(-110,60)*s:.0f}" r="{r.uniform(30,56)*s:.0f}" fill="{r.choice(["#ffc0d4","#ffd8e4","#ffaac4"])}"/>'
b+=petals(60,1082,'#ff9ab8',0,800,8,14,.9)
I[1082]=svg(b,d)

# 810 Hello, Again: an old wooden bus stop on a seaside road at dusk, waiting for someone from long ago
d,b=bg([(0,'#3a3a6a'),(.6,'#e8907a'),(1,'#ffc89a')])
b+=hinomaru_sun(560,440,80,'#ffe0a8',.85)+'<rect y="460" width="800" height="340" fill="#3a4a7a"/><rect y="460" width="800" height="6" fill="#ffe0a8" opacity=".6"/>'
b+='<path d="M-10 620 L810 580 L810 810 L-10 810Z" fill="#5a4a4a"/>'
b+='<path d="M140 400 L420 380 L430 410 L140 430Z" fill="#7a4a2a"/><rect x="150" y="420" width="14" height="200" fill="#5a3a1a"/><rect x="400" y="400" width="14" height="210" fill="#5a3a1a"/><rect x="170" y="540" width="220" height="16" fill="#8a5a3a"/>'
b+='<rect x="520" y="420" width="10" height="200" fill="#3a3a44"/><circle cx="525" cy="410" r="34" fill="#e8302a"/><circle cx="525" cy="410" r="22" fill="#fff"/>'
b+=figure(290,600,150,'#1a1420',hair='#1a1420')
I[810]=svg(b,d)

# 814 白い恋人達: a couple walking under falling snow through a street of white Christmas illuminations
d,b=bg([(0,'#0a1430'),(1,'#2a3a5a')])
b+=snow(140,814)
r=R(814)
for k in range(5):
    y=180+k*40
    b+=f'<path d="M-10 {y} Q400 {y+60} 810 {y}" stroke="#2a3a5a" stroke-width="2" fill="none"/>'
    for j in range(16): x=j*52+k*10;yy=y+60*(1-((x-400)/410)**2)*.9;b+=glow(x,yy,10,'#fff6d8',.8,'glow2')+f'<circle cx="{x}" cy="{yy:.0f}" r="4" fill="#fff"/>'
b+='<rect y="640" width="800" height="160" fill="#e8f0fa"/>'+figure(370,740,240,'#0a1020')+figure(440,740,220,'#0a1020',hair='#0a1020')
b+='<path d="M380 580 Q405 600 430 580" stroke="#e8302a" stroke-width="12" fill="none"/>'
I[814]=svg(b,d)

# 1583 天国: golden gates opening onto soft clouds and a heavenly light pouring down
d,b=bg([(0,'#fff6d8'),(.5,'#ffe0a8'),(1,'#f0c8a8')])
b+=rays(400,300,24,'#ffffff',.4,7)+glow(400,320,220,'#ffffff',.9)
b+='<path d="M220 640 L220 340 Q220 180 400 160 Q580 180 580 340 L580 640" stroke="#d8a830" stroke-width="22" fill="none"/>'
for x in range(250,560,40): b+=f'<rect x="{x}" y="{280 if abs(x-400)<120 else 330}" width="10" height="{360 if abs(x-400)<120 else 310}" fill="#e8b840"/>'
for x,y,s in [(180,680,1.6),(400,720,1.8),(640,690,1.6),(80,600,1.0),(720,600,1.0)]: b+=cloud(x,y,s,'#fffaf4',.98)
I[1583]=svg(b,d)

# 1116 プラネタリウム: two figures looking up inside a planetarium dome full of glowing constellations
d,b=bg([(0,'#04061a'),(1,'#0a1438')])
b+='<path d="M0 640 Q400 -40 800 640Z" fill="#0a1030"/>'+starsf(120,1116,600,'#e8f0ff')
for pts in [[(200,300),(260,260),(330,290),(360,230)],[(450,180),(500,220),(560,190),(600,240),(560,290)],[(300,420),(360,380),(420,420)]]:
    b+=f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" stroke="#8ac8ff" stroke-width="3" fill="none" opacity=".7"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#fff"/>' for x,y in pts)
b+='<rect y="640" width="800" height="160" fill="#05081a"/>'
b+='<g fill="#020410"><circle cx="350" cy="610" r="32"/><path d="M300 800 Q300 660 350 650 Q400 660 400 800Z"/><circle cx="450" cy="620" r="30"/><path d="M405 800 Q405 670 450 660 Q495 670 495 800Z"/></g>'
I[1116]=svg(b,d)

# 1510 CHAMELEON: a vivid chameleon curled on a branch, its skin shifting through a rainbow of colours
d,b=bg([(0,'#1a3a2a'),(1,'#0a2a1a')])
b+=glow(400,400,240,'#8af0a8',.3)
b+='<path d="M60 560 Q400 520 760 600" stroke="#5a3a1a" stroke-width="26" fill="none"/>'
d+=lg('cm',S((0,'#ff5a8a'),(.25,'#ffb02a'),(.5,'#5ae05a'),(.75,'#2ab0ff'),(1,'#9a5aff')),0,0,1,0)
b+='<path d="M200 520 Q210 380 360 360 Q520 350 600 440 L660 470 Q620 500 580 500 Q520 560 400 550 Q260 560 200 520Z" fill="url(#cm)"/>'
b+='<path d="M200 520 Q150 560 160 620 Q180 680 240 660 Q280 640 260 600 Q240 580 220 600" stroke="url(#cm)" stroke-width="26" fill="none"/>'
b+='<circle cx="560" cy="430" r="28" fill="#fff"/><circle cx="566" cy="430" r="12" fill="#1a1a1a"/><path d="M300 360 L320 320 L340 360 L360 318 L380 358 L400 320 L420 360" fill="url(#cm)"/>'
b+='<path d="M330 550 L310 600 M460 550 L480 600" stroke="#5ae05a" stroke-width="16" stroke-linecap="round"/>'
I[1510]=svg(b,d)

# 230 わかれうた: a woman walking away alone under an umbrella along a wet night street lined with 70s lamps
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a3a')])
b+=rain(90,230,'#c8d0e8',.4,6)
for x in (140,660): b+=f'<rect x="{x}" y="240" width="10" height="500" fill="#0a0a12"/>'+glow(x+5,240,60,'#ffd27a',.5)+f'<circle cx="{x+5}" cy="240" r="18" fill="#fff0b8"/>'
b+='<rect y="640" width="800" height="160" fill="#14141e"/>'
for x in (145,665): b+=f'<rect x="{x-20}" y="650" width="50" height="150" fill="#ffd27a" opacity=".18"/>'
b+=figure(420,720,250,'#08080e',hair='#08080e')+wagasa(420,470,130,'#5a1a3a',0)
I[230]=svg(b,d)

# 1193 One Love: two wedding rings intertwined under a bell, white petals drifting
d,b=bg([(0,'#f8f2ec'),(1,'#e8d8d0')])
b+=glow(400,420,220,'#ffffff',.7)+petals(30,1193,'#ffffff',0,800,8,14,.9)
b+='<path d="M360 150 Q400 120 440 150 L460 240 L340 240Z" fill="#e8c860"/><circle cx="400" cy="250" r="12" fill="#c8a040"/>'
b+='<circle cx="350" cy="470" r="110" fill="none" stroke="#e8c050" stroke-width="26"/><circle cx="460" cy="470" r="110" fill="none" stroke="#d8d8e0" stroke-width="26"/>'
b+='<path d="M430 380 A110 110 0 0 1 455 400" stroke="#e8c050" stroke-width="26" fill="none"/>'+sparkle(470,340,24,'#fff')
I[1193]=svg(b,d)

# 231 悪女: a red high heel kicked off beside a lipstick and a cocktail glass on a dark bar counter
d,b=bg([(0,'#1a0a14'),(1,'#3a0a1a')])
b+=glow(400,420,220,'#ff4a6a',.3)+'<rect y="520" width="800" height="280" fill="#2a1410"/><rect y="520" width="800" height="10" fill="#5a2a1a"/>'
b+='<g transform="translate(0 -40)"><path d="M150 380 Q170 350 200 360 Q260 420 300 470 Q380 500 500 520 Q530 530 520 550 L320 550 Q260 540 220 470 L200 440Z" fill="#d8102a"/><path d="M150 380 L140 560 L160 560 L190 420Z" fill="#a8081e"/><path d="M200 370 Q240 420 280 470" stroke="#ff5a6a" stroke-width="6" fill="none" opacity=".6"/></g>'
b+='<rect x="560" y="420" width="40" height="100" rx="6" fill="#d8b050"/><path d="M566 420 L566 380 Q580 360 594 380 L594 420Z" fill="#c8081e"/>'
b+='<path d="M630 300 L730 300 L680 380Z" fill="#ffd8e0" opacity=".7"/><rect x="676" y="378" width="8" height="120" fill="#f0f0f8"/><ellipse cx="680" cy="500" rx="40" ry="8" fill="#f0f0f8"/><circle cx="700" cy="310" r="10" fill="#e8102a"/>'
I[231]=svg(b,d)

# 630 愛のままにわがままに 僕は君だけを傷つけない: a red rose wrapped in thorny vines, burning with passion against black
d,b=bg([(0,'#0a0006'),(1,'#2a0410')])
b+=glow(400,380,230,'#ff2a3a',.45)
b+='<path d="M400 800 Q380 620 400 460" stroke="#1a4a1a" stroke-width="14" fill="none"/>'
for k in range(6): b+=f'<path d="M{392+((k%2)*16)} {700-k*40} l{-20 if k%2==0 else 20} -10 l{10 if k%2==0 else -10} 14Z" fill="#1a4a1a"/>'
b+='<path d="M200 600 Q300 400 400 560 Q500 720 600 500 Q680 330 560 260" stroke="#2a3a1a" stroke-width="8" fill="none"/>'
b+='<g transform="translate(400 380) scale(1.8)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({s})"/>' for a,c,s in [(0,'#a8081e',1),(60,'#c81028',.9),(-60,'#c81028',.9),(150,'#e01a34',.7),(-150,'#e01a34',.7),(0,'#ff3a4a',.4)])+'</g>'
I[630]=svg(b,d)

# 1646 ROSE: a single hot-pink neon rose glowing against a dark brick wall
d,b=bg([(0,'#140a14'),(1,'#2a1420')])
for j in range(14):
    for i in range(9): b+=f'<rect x="{i*90-(j%2)*45}" y="{j*58}" width="86" height="54" fill="#22121c"/>'
b+=glow(400,360,180,'#ff3ab8',.5)
st='stroke="#ff6ad0" stroke-width="10" fill="none" stroke-linecap="round" filter="url(#glow2)"'
st2='stroke="#ffd8f4" stroke-width="4" fill="none" stroke-linecap="round"'
sp='M400 340 Q430 330 432 360 Q430 392 396 392 Q356 390 356 350 Q360 306 404 304 Q456 306 460 356 Q458 418 400 424 Q332 420 328 352 Q332 280 404 276'
for s in (st,st2):
    b+=f'<path d="{sp} M328 352 Q320 410 360 440 L440 440 Q480 410 470 356 M400 440 L400 650 M400 540 Q350 520 330 490 Q370 480 400 520 M400 580 Q450 560 470 530 Q430 520 400 560" {s}/>'
I[1646]=svg(b,d)

# 815 明日晴れるかな: a teru-teru bozu charm hanging in a window as the rain clears and blue sky breaks through
d,b=bg([(0,'#7ac0f0'),(1,'#d8eeff')])
b+='<path d="M0 0 L800 0 L800 300 Q500 360 0 260Z" fill="#7a8aa0"/>'+rain(40,815,'#e8f0ff',.6,6,300)
b+=glow(620,420,120,'#fff8d8',.7)+'<circle cx="620" cy="420" r="50" fill="#fff6c8"/>'
b+='<rect x="80" y="60" width="640" height="680" fill="none" stroke="#e8dccc" stroke-width="30"/><path d="M400 60 L400 740" stroke="#e8dccc" stroke-width="16"/>'
b+='<path d="M300 75 L300 230" stroke="#c8b8a8" stroke-width="4"/><circle cx="300" cy="290" r="64" fill="#fff"/><path d="M250 330 Q230 430 210 470 L390 470 Q370 430 350 330Z" fill="#fff"/><path d="M250 340 L350 340" stroke="#e8302a" stroke-width="8"/>'
b+='<circle cx="278" cy="284" r="7" fill="#1a1a2a"/><circle cx="322" cy="284" r="7" fill="#1a1a2a"/><path d="M280 310 Q300 326 320 310" stroke="#1a1a2a" stroke-width="5" fill="none"/>'
I[815]=svg(b,d)

# 724 ロマンスの神様: a pair of crossed skis planted in a snowy slope, a big heart glowing in the winter sky above
d,b=bg([(0,'#3a8ae8'),(1,'#c8e8ff')])
b+='<path d="M-10 500 L200 260 L380 460 L560 220 L810 520 L810 810 L-10 810Z" fill="#f4f8ff"/><path d="M200 260 L240 320 L180 330Z M560 220 L600 290 L520 300Z" fill="#c8d8f0"/>'
b+='<path d="M-10 560 Q400 520 810 600 L810 810 L-10 810Z" fill="#fff"/>'
b+='<rect x="380" y="400" width="26" height="380" rx="12" fill="#e8302a" transform="rotate(-16 393 590)"/><rect x="410" y="400" width="26" height="380" rx="12" fill="#2a6ae8" transform="rotate(16 423 590)"/>'
b+=glow(400,200,100,'#ff8ab0',.6)+heart(400,210,70,'#ff3a7a')
b+=snow(50,724,.9)
I[724]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
