import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 27. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 596 DAHLIA: a huge crimson dahlia blooming in darkness with sharp petals and a cold blue rim light
d,b=bg([(0,'#05050f'),(1,'#1a0a1a')])
b+=glow(400,400,300,'#3a4aff',.15)
for k,(r2,c) in enumerate([(300,'#6a0a1a'),(230,'#9a0a2a'),(160,'#c8102a'),(90,'#e8304a')]):
    b+=''.join(f'<path d="M400 400 L{400+r2*math.cos(a-.12):.0f} {400+r2*math.sin(a-.12):.0f} L{400+r2*1.08*math.cos(a):.0f} {400+r2*1.08*math.sin(a):.0f} L{400+r2*math.cos(a+.12):.0f} {400+r2*math.sin(a+.12):.0f}Z" fill="{c}" stroke="#2a0008" stroke-width="2"/>' for a in [j*math.pi/8+k*.2 for j in range(16)])
b+='<circle cx="400" cy="400" r="34" fill="#ffd02a"/>'
I[596]=svg(b,d)

# 842 HAPPINESS: a snowy night town with a big lit Christmas-like tree and a couple's silhouettes, warm windows
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+=''.join(f'<circle cx="{(k*131)%800}" cy="{(k*71)%800}" r="{2+k%3}" fill="#fff" opacity=".8"/>' for k in range(60))+'<rect y="620" width="800" height="180" fill="#e8eef8"/>'
b+='<path d="M400 160 L520 420 L460 420 L560 620 L240 620 L340 420 L280 420Z" fill="#1a5a3a"/>'+star5(400,160,30,'#ffd02a')+''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}"/>' for x,y,c in [(360,300,'#ff4a4a'),(440,360,'#ffd02a'),(330,470,'#4ac8ff'),(470,520,'#ff4a4a'),(400,560,'#ffd02a')])
b+=figure(180,700,200,'#1a1a2a')+figure(620,700,200,'#1a1a2a')
I[842]=svg(b,d)

# 905 Lights Down Low: a dimmed dance floor with a single disco ball scattering low light, a dancing silhouette
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=''.join(f'<path d="M400 160 L{x} 800" stroke="#c8a8ff" stroke-width="3" opacity=".25"/>' for x in range(0,820,60))+'<circle cx="400" cy="160" r="60" fill="#a8a8b8"/>'+''.join(f'<rect x="{352+c*16}" y="{112+r2*16}" width="14" height="14" fill="{"#fff" if (c+r2)%3==0 else "#7a7a8a"}"/>' for c in range(6) for r2 in range(6) if (352+c*16-400)**2+(112+r2*16-160)**2<3200)
b+=figure(400,760,340,'#000',pose='reach')
I[905]=svg(b,d)

# 1190 ワンルーム・ディスコ: a tiny one-room apartment with cardboard boxes and a mirror ball, three dancers' silhouettes, neon
d,b=bg([(0,'#0a1a2a'),(1,'#1a3a4a')])
b+='<rect x="100" y="140" width="600" height="520" fill="#1a2a3a" stroke="#4ad8ff" stroke-width="6"/><rect x="100" y="580" width="600" height="80" fill="#2a3a4a"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="70" height="56" fill="#c8a070"/>' for x,y in [(130,524),(200,524),(160,468),(600,524)])+'<path d="M400 140 L400 200" stroke="#888" stroke-width="3"/><circle cx="400" cy="226" r="28" fill="#c8c8d8"/>'
b+=''.join(figure(x,620,200,'#000',pose=p) for x,p in [(320,'reach'),(400,'up'),(480,'reachL')])+''.join(f'<path d="M400 226 L{x} {y}" stroke="#ff4fa0" stroke-width="2" opacity=".5"/>' for x,y in [(160,320),(640,300),(260,460),(560,480)])
I[1190]=svg(b,d)

# 843 MERMAID: a mermaid tail splash in a turquoise sea under a blazing summer sun, rock and spray
d,b=bg([(0,'#2ab0ff'),(1,'#a8ecff')])
b+=hinomaru_sun(160,140,60,'#fffbe0')+'<rect y="380" width="800" height="420" fill="#0a90c8"/>'
b+='<path d="M380 560 Q420 440 440 360 Q460 300 420 260 L520 280 Q480 320 470 380 Q450 470 420 560Z" fill="#1ac8a8"/><path d="M420 260 Q360 220 340 260 Q380 260 420 270Z M520 280 Q580 240 600 280 Q560 290 520 285Z" fill="#1ac8a8"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x,y,r in [(340,560,14),(470,570,12),(300,520,8),(520,530,9),(400,600,10)])
I[843]=svg(b,d)

# 1169 にじいろ: a rainbow arcing over a small town on the coast after the rain, Okinawan palette
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+=''.join(f'<path d="M80 600 A320 320 0 0 1 720 600" stroke="{c}" stroke-width="24" fill="none" transform="translate(0 {k*24})"/>' for k,c in enumerate(['#ff5a5a','#ffa82a','#ffe85a','#5ad85a','#5aa8ff','#8a5aff']))
b+='<rect y="600" width="800" height="200" fill="#3ab0d0"/>'+''.join(f'<rect x="{x}" y="{600-h}" width="60" height="{h}" fill="#f4ece0"/><path d="M{x-6} {600-h} L{x+30} {580-h} L{x+66} {600-h}Z" fill="#d8603a"/>' for x,h in [(140,60),(220,80),(520,70),(600,56)])
I[1169]=svg(b,d)

# 1318 ラブラドール・レトリバー: a golden labrador silhouette running along a summer beach chasing a ball
d,b=bg([(0,'#4ac8ff'),(1,'#d8f6ff')])
b+='<rect y="420" width="800" height="140" fill="#2aa8d8"/><rect y="560" width="800" height="240" fill="#f8e0a8"/>'
b+='<g fill="#e8b860"><ellipse cx="380" cy="560" rx="110" ry="46"/><circle cx="490" cy="500" r="42"/><ellipse cx="530" cy="512" rx="34" ry="20"/><path d="M470 480 Q450 520 470 540 Q490 520 480 480Z" fill="#c89040"/><path d="M290 540 Q240 500 220 520" stroke="#e8b860" stroke-width="18" fill="none"/><rect x="300" y="580" width="20" height="70" transform="rotate(-25 310 600)"/><rect x="420" y="580" width="20" height="70" transform="rotate(25 430 600)"/></g>'
b+='<circle cx="620" cy="450" r="24" fill="#ff4a6a"/>'
I[1318]=svg(b,d)

# 1650 KawaiiってMagic: a magic wand casting a burst of pastel hearts, stars and ribbons on a candy-pink sky
d,b=bg([(0,'#ffb8e0'),(1,'#d8c8ff')])
b+='<path d="M180 680 L420 400" stroke="#fff" stroke-width="16" stroke-linecap="round"/>'+star5(440,380,50,'#ffe86a')
r=random.Random(1650)
b+=''.join(heart(r.randint(420,740),r.randint(80,420),r.randint(14,30),r.choice(['#ff6aa8','#fff','#8ad8ff'])) for k in range(10))+''.join(star5(r.randint(420,740),r.randint(80,420),r.randint(10,22),'#fff') for k in range(8))
I[1650]=svg(b,d)

# 1771 Power: a big glowing fist raised over a stage with lightning and a crowd of raised hands
d,b=bg([(0,'#1a0a3a'),(1,'#5a1a6a')])
b+=bolt([(140,40),(200,180),(160,200),(240,340)],'#ffe86a',10)+bolt([(660,40),(600,180),(640,200),(560,340)],'#ffe86a',10)+glow(400,260,180,'#ff4fa0',.4)
b+=figure(400,600,360,'#ff4fa0',pose='up')
b+=''.join(f'<path d="M{x} 800 L{x} 640" stroke="#000" stroke-width="20"/><circle cx="{x}" cy="630" r="16" fill="#000"/>' for x in range(30,800,56))
I[1771]=svg(b,d)

# 180 うそ: a lipstick-marked cigarette in an ashtray with smoke curling into a broken heart, mid-70s bar
d,b=bg([(0,'#1a0a14'),(1,'#3a1a24')])
b+='<rect y="560" width="800" height="240" fill="#3a2010"/><ellipse cx="400" cy="580" rx="140" ry="34" fill="#8a8a94"/><ellipse cx="400" cy="574" rx="110" ry="22" fill="#5a5a64"/>'
b+='<rect x="380" y="556" width="140" height="14" fill="#f4f0e8" transform="rotate(-10 450 563)"/><rect x="380" y="556" width="30" height="14" fill="#e8102a" opacity=".7" transform="rotate(-10 450 563)"/>'
b+='<path d="M510 540 Q480 460 520 400 Q560 340 510 280" stroke="#ccc" stroke-width="4" fill="none" opacity=".5"/>'+heart(500,230,40,'#c8102a')+'<path d="M500 200 L490 225 L506 240 L496 268" stroke="#1a0a14" stroke-width="5" fill="none"/>'
I[180]=svg(b,d)

# 244 真夏の夜の夢: a midsummer night with a huge moon over a tropical shore, fireworks and a dancing silhouette
d,b=bg([(0,'#0a0a3a'),(1,'#5a1a5a')])
b+='<circle cx="560" cy="220" r="120" fill="#fff4c8"/>'+firework(200,200,90,'#ff4fa0',seed=244)+'<rect y="480" width="800" height="320" fill="#1a1a4a"/><rect x="460" y="480" width="200" height="320" fill="#fff4c8" opacity=".15"/>'
b+=figure(300,740,300,'#000',pose='up')
I[244]=svg(b,d)

# 245 Destiny: a woman's silhouette in a car watching a man's silhouette walk off with another, in dusty shoes, late 70s
d,b=bg([(0,'#8a6a5a'),(1,'#e8c8a0')])
b+=skyline(500,'#5a4a4a',245,60,200,'#ffd27a',20)+'<rect y="500" width="800" height="300" fill="#8a8a8a"/>'
b+='<path d="M60 640 L100 560 L300 550 L360 600 L380 660 L60 660Z" fill="#c8302a"/><rect x="120" y="566" width="160" height="40" fill="#a8c8e8" opacity=".7"/><circle cx="200" cy="584" r="14" fill="#1a1a1a"/>'+ring(120,670,24,'#1a1a1a',12)+ring(320,670,24,'#1a1a1a',12)
b+=figure(560,660,220,'#1a1a1a')+figure(640,660,200,'#3a1a2a')
I[245]=svg(b,d)

# 373 Pearl-White Eve: a strand of white pearls on snow under a starry Christmas Eve sky, a candle in a window
d,b=bg([(0,'#0a1a3a'),(1,'#3a4a7a')])
b+=starsf(80,373,500)+'<rect y="560" width="800" height="240" fill="#e8eef8"/><rect x="560" y="300" width="140" height="180" fill="#ffd27a"/><rect x="620" y="380" width="20" height="60" fill="#fff"/>'
b+=''.join(f'<circle cx="{200+260*t:.0f}" cy="{640+60*math.sin(t*math.pi*2):.0f}" r="12" fill="#fff" stroke="#c8c8d8" stroke-width="2"/>' for t in [k/18 for k in range(19)])
I[373]=svg(b,d)

# 520 やさしいキスをして: two silhouettes about to kiss inside a soft circle of light on a quiet street at night
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a4a')])
b+=glow(400,400,220,'#ffd8a0',.35)+'<rect y="620" width="800" height="180" fill="#1a1a24"/>'
b+='<g fill="#000"><circle cx="360" cy="320" r="34"/><circle cx="440" cy="330" r="32"/><path d="M320 360 L390 360 L400 620 L320 620Z"/><path d="M410 370 L480 370 L490 620 L410 620Z"/></g>'
I[520]=svg(b,d)

# 683 ガラガラヘビがやってくる: a comic rattlesnake rising from desert sand with rattle shaking, cacti and sunset
d,b=bg([(0,'#ff8a3a'),(1,'#ffd88a')])
b+=hinomaru_sun(600,200,70,'#fff0c0')+'<rect y="560" width="800" height="240" fill="#e8b870"/>'+''.join(f'<rect x="{x}" y="{560-h}" width="30" height="{h}" rx="15" fill="#3a8a3a"/><rect x="{x-24}" y="{560-h*.7}" width="24" height="16" fill="#3a8a3a"/><rect x="{x-24}" y="{560-h*.9}" width="16" height="40" rx="8" fill="#3a8a3a"/>' for x,h in [(120,180),(680,140)])
b+='<path d="M300 640 Q400 680 460 620 Q500 560 440 520 Q380 480 420 400 Q440 360 480 360" stroke="#8a6a2a" stroke-width="40" fill="none" stroke-linecap="round"/><circle cx="490" cy="350" r="34" fill="#8a6a2a"/><circle cx="500" cy="340" r="7" fill="#000"/><path d="M520 360 L560 370 L550 360 L560 350Z" fill="#e8102a"/>'
b+=''.join(f'<ellipse cx="{280-k*16}" cy="{640+k*4}" rx="12" ry="16" fill="#c8a05a"/>' for k in range(4))
I[683]=svg(b,d)

# 873 Spirit dreams inside: a glowing spirit-like orb rising out of an open hand into a cosmic swirl
d,b=bg([(0,'#050514'),(1,'#1a1a3a')])
b+=starsf(90,873,800)+''.join(f'<ellipse cx="400" cy="300" rx="{60+k*50}" ry="{20+k*16}" fill="none" stroke="#8ab8ff" stroke-width="2" opacity="{.6-k*.1:.1f}" transform="rotate(-20 400 300)"/>' for k in range(5))
b+=glow(400,320,90,'#c8e0ff',.8)+'<circle cx="400" cy="320" r="30" fill="#fff"/><path d="M-10 700 Q400 640 810 700 L810 810 L-10 810Z" fill="#0a0a1a"/>'+figure(400,700,200,'#000',pose='reach')
I[873]=svg(b,d)

# 911 Believe Your Smile: six silhouettes jumping in front of a giant smiling sun on a bright blue sky
d,b=bg([(0,'#3ab0ff'),(1,'#d8f2ff')])
b+=hinomaru_sun(400,240,120,'#ffd02a')+'<circle cx="360" cy="220" r="12" fill="#5a3a1a"/><circle cx="440" cy="220" r="12" fill="#5a3a1a"/><path d="M350 270 Q400 320 450 270" stroke="#5a3a1a" stroke-width="10" fill="none"/>'
b+='<rect y="620" width="800" height="180" fill="#6ac84a"/>'+''.join(figure(x,y,180,'#1a2a4a',pose='up') for x,y in [(120,680),(240,640),(360,690),(480,650),(600,690),(700,650)])
I[911]=svg(b,d)

# 1121 stay with me: a woman's silhouette pressing a hand on a fogged window, a man walking away in the rain below
d,b=bg([(0,'#2a3a5a'),(1,'#5a6a8a')])
b+='<rect x="80" y="80" width="640" height="640" fill="#8a9ab8" opacity=".5"/>'+rain(80,1121,'#e8f0ff',.4)+figure(560,640,150,'#1a1a2a')
b+=figure(260,820,500,'#000')+'<g fill="#f0c8b0" opacity=".85"><ellipse cx="380" cy="400" rx="30" ry="40"/></g>'
I[1121]=svg(b,d)

# 1360 走れ!Bicycle: a schoolgirl's silhouette pedalling fast downhill with the sea ahead, skirt and hair flying
d,b=bg([(0,'#4ac0ff'),(1,'#d8f4ff')])
b+=cloud(600,140,1.3)+'<rect y="380" width="800" height="160" fill="#2aa8d8"/><path d="M-10 480 L810 700 L810 810 L-10 810Z" fill="#9a9aa0"/>'
b+='<g transform="rotate(15 400 600)">'+ring(320,640,46,'#1a1a1a',10)+ring(480,640,46,'#1a1a1a',10)+'<path d="M320 640 L380 570 L480 640 M380 570 L460 570 L480 640 M460 570 L470 540" stroke="#1a1a1a" stroke-width="8" fill="none"/><g fill="#1a2a4a"><circle cx="420" cy="440" r="24"/><path d="M400 466 L440 466 L430 560 L380 560Z"/><path d="M380 540 L360 580 L420 580Z"/></g><path d="M400 430 Q360 420 340 440" stroke="#1a2a4a" stroke-width="10" fill="none"/></g>'
I[1360]=svg(b,d)

# 1361 是非に及ばず: a samurai-era temple burning at night with a lone figure in a kimono standing calmly
d,b=bg([(0,'#1a0404'),(1,'#5a1a0a')])
b+='<path d="M180 460 L400 360 L620 460Z" fill="#1a0a0a"/><rect x="220" y="460" width="360" height="200" fill="#2a1a1a"/>'+''.join(f'<path d="M{x} 460 Q{x+20} {380-k*20} {x+50} 340 Q{x+60} 400 {x+90} 300 Q{x+110} 380 {x+120} 460Z" fill="#ff6a1a" opacity=".85"/>' for k,x in enumerate((160,380,520)))
b+=glow(400,400,300,'#ff6a1a',.3)+'<rect y="660" width="800" height="140" fill="#0a0404"/>'+figure(400,700,200,'#000')
I[1361]=svg(b,d)

# 1713 SEASON'S CALL: a ring of four season motifs (petal, sun, maple leaf, snowflake) around a figure on a hill
d,b=bg([(0,'#3a5a8a'),(1,'#c8d8e8')])
b+='<path d="M-10 620 Q400 520 810 620 L810 810 L-10 810Z" fill="#4a6a4a"/>'+figure(400,600,200,'#0a0a1a')
b+=sakura(200,200,1.2)+hinomaru_sun(600,200,40,'#ffd02a')+'<path d="M600 440 L620 400 L640 440 L680 430 L660 470 L690 500 L640 500 L620 540 L600 500 L550 500 L580 470 L560 430Z" fill="#e8502a"/>'
b+=''.join(f'<path d="M200 460 L{200+40*math.cos(a):.0f} {460+40*math.sin(a):.0f}" stroke="#fff" stroke-width="6"/>' for a in [k*math.pi/3 for k in range(6)])
I[1713]=svg(b,d)

# 1783 ALONES: many separate silhouettes each standing in its own pool of light in a dark grid
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
for c in range(4):
    for r2 in range(3):
        x,y=130+c*180,260+r2*200
        b+=f'<ellipse cx="{x}" cy="{y}" rx="60" ry="14" fill="#c8d8ff" opacity=".3"/>'+figure(x,y,120,'#c8d8ff' if (c,r2)==(1,1) else '#3a3a4a')
I[1783]=svg(b,d)

# 65 ラブユー東京: Tokyo Tower lit red at night with a 60s neon street and a couple
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a3a')])
b+='<path d="M400 80 L470 600 L330 600Z" fill="none" stroke="#ff4a2a" stroke-width="10"/><path d="M360 300 L440 300 M345 420 L455 420 M400 80 L400 600" stroke="#ff4a2a" stroke-width="8"/>'+glow(400,300,160,'#ff4a2a',.2)
b+=skyline(600,'#0a0a1a',65,40,140,'#ffd27a',40)+'<rect y="600" width="800" height="200" fill="#14141f"/>'+neon(160,200,'東京','#ff8ad8',50)+figure(560,760,200,'#000')+figure(620,760,190,'#000')
I[65]=svg(b,d)

# 805 WOW WAR TONIGHT: a crowd of salarymen's silhouettes in ties breaking into dance under strobe lights in a club
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a5a')])
b+=''.join(f'<polygon points="{x},0 {x-80},700 {x+80},700" fill="{c}" opacity=".2"/>' for x,c in [(160,'#ff4fa0'),(400,'#4ad8ff'),(640,'#ffd02a')])
b+=''.join(figure(x,760,h,'#000',pose=p)+f'<path d="M{x} {760-h*.78} L{x} {760-h*.55}" stroke="#e8302a" stroke-width="8"/>' for x,h,p in [(160,280,'up'),(320,300,'reach'),(480,290,'up'),(640,270,'reachL')])
I[805]=svg(b,d)

# 955 BRAND NEW SONG: a fresh blank music sheet catching light with the first notes appearing, an open window and blue sky
d,b=bg([(0,'#7ac8ff'),(1,'#f0faff')])
b+='<rect x="160" y="220" width="480" height="380" fill="#fff" stroke="#d8dce8" stroke-width="4" transform="rotate(-4 400 410)"/>'+''.join(f'<path d="M190 {280+k*14+g*90} L610 {280+k*14+g*90-30}" stroke="#8a8a9a" stroke-width="2"/>' for g in range(3) for k in range(5))
b+=''.join(note(x,y,30,'#2a3a6a') for x,y in [(240,330),(300,320),(360,400)])+sparkle(560,240,24,'#ffd02a')
I[955]=svg(b,d)

# 1072 Again2: two friends' silhouettes walking back along a riverside path where they once walked, sunset, guitar on back
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=hinomaru_sun(600,380,70,'#fff2c8',.8)+'<rect y="420" width="800" height="120" fill="#7aa8c8"/><rect y="540" width="800" height="260" fill="#8ab86a"/>'
b+=figure(320,700,240,'#2a1a1a')+figure(430,700,250,'#2a1a1a')+guitar(330,560,.6,20,'#5a3a1a')
I[1072]=svg(b,d)

# 1085 旅人: a traveller's silhouette with a backpack on a mountain path at dawn, a long road curving into the distance
d,b=bg([(0,'#5a8ac8'),(1,'#ffd8a8')])
b+=hills(420,60,'#7a8ab0',1085)+hills(540,40,'#5a7a5a',1086)+'<path d="M380 540 Q500 600 360 680 Q220 760 400 820" stroke="#d8c8a0" stroke-width="40" fill="none"/>'
b+=figure(420,700,220,'#1a1a1a')+'<rect x="384" y="560" width="36" height="60" rx="8" fill="#3a2a1a"/>'
I[1085]=svg(b,d)

# 1319 11月のアンクレット: a thin gold anklet on a bare foot by autumn seaside, maple leaves on the sand
d,b=bg([(0,'#c8a8a0'),(1,'#f0e0d0')])
b+='<rect y="420" width="800" height="160" fill="#7a9ab0"/><rect y="580" width="800" height="220" fill="#e8d0b0"/>'
b+='<path d="M360 300 L360 620 Q360 680 420 690 L520 700 Q540 680 520 660 L440 640 L430 300Z" fill="#f0c8b0"/>'+'<path d="M356 560 Q395 590 434 560" stroke="#d8b040" stroke-width="5" fill="none"/>'+sparkle(400,580,10,'#fff')
b+=''.join(f'<path d="M{x} {y} l12 -24 l12 24 l24 -6 l-12 20 l16 18 l-26 0 l-14 22 l-14 -22 l-26 0 l16 -18 l-12 -20Z" fill="#d8502a"/>' for x,y in [(160,680),(620,720)])
I[1319]=svg(b,d)

# 83 池袋の夜: Ikebukuro night street with neon signs in late-60s style and a woman's silhouette under an umbrella
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+=neon(180,180,'池袋','#ff4fa0',56)+neon(600,240,'BAR','#4ad8ff',48)+rain(50,83,'#c8c8ff',.3)+'<rect y="600" width="800" height="200" fill="#1a1a24"/>'
b+='<path d="M300 420 Q400 320 500 420Z" fill="#c8102a"/><path d="M400 420 L400 520" stroke="#555" stroke-width="4"/>'+figure(400,640,220,'#000')
I[83]=svg(b,d)

# 95 よろしく哀愁: a young man's silhouette leaning on a phone booth at dusk, mid-70s idol colours
d,b=bg([(0,'#ff8a8a'),(1,'#ffe0c0')])
b+='<rect y="600" width="800" height="200" fill="#8a7a7a"/><rect x="420" y="240" width="160" height="360" fill="#e8302a"/><rect x="440" y="280" width="120" height="260" fill="#ffe8b8" opacity=".6"/>'
b+=figure(360,640,320,'#2a1a1a')+'<path d="M410 400 L440 390" stroke="#2a1a1a" stroke-width="14"/>'
I[95]=svg(b,d)

# 374 野ばらのエチュード: wild roses tangled on a white fence with piano keys underneath, early-80s pastel
d,b=bg([(0,'#fff0f4'),(1,'#f0f8ff')])
b+=''.join(f'<rect x="{x}" y="300" width="22" height="300" fill="#fff" stroke="#d8d8e0" stroke-width="2"/>' for x in range(60,780,60))+'<rect y="360" width="800" height="16" fill="#fff"/><rect y="500" width="800" height="16" fill="#fff"/>'
b+='<path d="M40 400 Q200 340 300 420 Q420 500 520 400 Q640 320 780 400" stroke="#4a8a3a" stroke-width="6" fill="none"/>'+''.join(flower(x,y,26,5,'#ff8aa8','#ffd02a') for x,y in [(140,370),(300,420),(440,460),(580,360),(700,380)])
b+='<rect y="640" width="800" height="160" fill="#fff"/>'+''.join(f'<rect x="{x}" y="640" width="30" height="90" fill="#1a1a1a"/>' for x in (40,100,220,280,340,460,520,640,700))
I[374]=svg(b,d)

# 521 未来予想図II: a couple on a motorbike with brake lights blinking five times, city lights of the future ahead
d,b=bg([(0,'#1a1a3a'),(1,'#5a4a7a')])
b+=skyline(520,'#1a1a2a',521,60,220,'#ffd27a',50)+'<rect y="520" width="800" height="280" fill="#2a2a34"/>'
b+=ring(280,660,40,'#000',14)+ring(520,660,40,'#000',14)+'<path d="M280 660 L360 580 L480 580 L520 660 M480 580 L500 540" stroke="#000" stroke-width="14" fill="none"/><g fill="#000"><circle cx="380" cy="460" r="24"/><path d="M360 484 L400 484 L420 580 L350 580Z"/><circle cx="440" cy="460" r="22"/><path d="M420 484 L460 484 L470 580 L410 580Z"/></g>'
b+=''.join(f'<circle cx="{180+k*40}" cy="600" r="12" fill="#ff2a2a"/>'+glow(180+k*40,600,22,'#ff2a2a',.4) for k in range(5) if 180+k*40<250)+'<circle cx="250" cy="600" r="14" fill="#ff2a2a"/>'+glow(250,600,40,'#ff2a2a',.6)
I[521]=svg(b,d)

# 754 I'll Be: a figure standing at the edge of a cliff facing a rising sun over clouds, wind
d,b=bg([(0,'#3a5a9a'),(1,'#ffd0a0')])
b+=hinomaru_sun(560,460,90,'#fff2c8')+cloud(420,520,2.2)+cloud(680,560,1.6)+'<path d="M-10 800 L-10 520 L300 540 L340 800Z" fill="#1a1a2a"/>'+figure(260,540,200,'#000')
I[754]=svg(b,d)

# 1028 本能: a shattered glass pane with a hand-shaped impact, red background, nurse-white light
d,b=bg([(0,'#c8102a'),(1,'#5a0a14')])
b+='<rect x="140" y="120" width="520" height="560" fill="#e8f0f8" opacity=".85"/>'+''.join(f'<path d="M400 400 L{400+380*math.cos(a):.0f} {400+380*math.sin(a):.0f}" stroke="#5a0a14" stroke-width="3"/>' for a in [k*.55 for k in range(12)])
b+=''.join(ring(400,400,r2,'#5a0a14',3) for r2 in (40,100))+''.join(f'<polygon points="{x},{y} {x+30},{y+8} {x+8},{y+36}" fill="#e8f0f8"/>' for x,y in [(80,180),(700,240),(700,600),(90,620),(400,740)])
I[1028]=svg(b,d)

# 1320 Teacher Teacher: a chalkboard with a big heart and question mark, a girl's silhouette raising her hand
d,b=bg([(0,'#e8e0d0'),(1,'#d8c8b0')])
b+='<rect x="80" y="100" width="640" height="380" fill="#2a4a3a" stroke="#8a6a4a" stroke-width="14"/>'+heart(300,280,70,'none','stroke="#fff" stroke-width="6"')+txt(540,340,'?',180,'#fff',300)
b+=figure(400,800,320,'#1a1a2a',pose='up')
I[1320]=svg(b,d)

# 1321 心のプラカード: a girl's silhouette holding up a blank placard with a heart, in a crowd of placards
d,b=bg([(0,'#ffd8e8'),(1,'#fff8f0')])
b+=''.join(f'<rect x="{x}" y="{y}" width="110" height="80" fill="#fff" stroke="#d8c8c8" stroke-width="4"/><path d="M{x+55} {y+80} L{x+55} {y+180}" stroke="#a88a6a" stroke-width="6"/>' for x,y in [(60,320),(200,360),(520,350),(650,330)])
b+='<rect x="300" y="140" width="200" height="140" fill="#fff" stroke="#ff6a9a" stroke-width="8"/>'+heart(400,210,46,'#ff4a7a')+'<path d="M400 280 L400 420" stroke="#a88a6a" stroke-width="8"/>'+figure(400,800,380,'#2a2a3a',pose='up')
I[1321]=svg(b,d)

# 1322 僕たちは戦わない: a field of flowers where many silhouettes lay down swords and raise flowers instead
d,b=bg([(0,'#7ac8ff'),(1,'#f0f8e8')])
b+='<rect y="520" width="800" height="280" fill="#8ac85a"/>'+''.join(flower(x,y,16,5,c,'#ffd02a') for x,y,c in [(100,620,'#ff8ab8'),(180,700,'#fff'),(300,660,'#ffd02a'),(520,700,'#ff8ab8'),(640,640,'#fff'),(720,720,'#ffd02a')])
b+=''.join(figure(x,600,200,'#2a3a2a',pose='up') for x in (240,400,560))+'<path d="M180 760 L330 740 M460 760 L620 770" stroke="#8a8a9a" stroke-width="10" stroke-linecap="round"/>'
I[1322]=svg(b,d)

# 1362 バレッタ: a hair barrette glinting in a schoolgirl's long hair, seen from behind, classroom window light
d,b=bg([(0,'#e8f0f8'),(1,'#f8f4ec')])
b+='<rect x="520" y="80" width="200" height="360" fill="#d8ecff" stroke="#c8ccd8" stroke-width="10"/>'
b+=''.join(f'<path d="M{300+k*12} 260 Q{290+k*13} 520 {280+k*16} 800" stroke="#2a1e1a" stroke-width="14" fill="none"/>' for k in range(18))+'<rect x="300" y="380" width="220" height="50" rx="24" fill="#f0d8a8" stroke="#c8a870" stroke-width="5"/>'+''.join(f'<circle cx="{x}" cy="405" r="8" fill="#fff"/>' for x in (340,410,480))+sparkle(500,380,22,'#fff')
I[1362]=svg(b,d)

# 1427 Dance My Generation: a gold-sequin stage with a disco grid floor and silhouettes in dramatic poses, flashy
d,b=bg([(0,'#2a1a0a'),(1,'#6a4a1a')])
b+=''.join(f'<rect x="{c*100}" y="{560+r2*60}" width="98" height="58" fill="{["#ff4fa0","#4ad8ff","#ffd02a","#4ad84a"][(c+r2)%4]}" opacity=".7"/>' for c in range(8) for r2 in range(4))
r=random.Random(1427)
b+=''.join(f'<circle cx="{r.randint(0,800)}" cy="{r.randint(0,520)}" r="{r.randint(2,6)}" fill="#ffd870"/>' for k in range(80))+''.join(figure(x,580,260,'#000',pose=p) for x,p in [(160,'up'),(320,'reach'),(480,'reachL'),(640,'up')])
I[1427]=svg(b,d)

# 1794 D-tecnoLife: a futuristic city of glowing data lines with a figure leaping across rooftops, cyan and black
d,b=bg([(0,'#020a14'),(1,'#0a2a3a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#1ad8ff" stroke-width="1" opacity=".2"/>' for y in range(0,800,30))+skyline(800,'#041018',1794,200,500,'#1ad8ff',80)
b+='<g transform="rotate(-20 400 260)">'+figure(400,330,200,'#000',pose='reach')+'</g>'+'<path d="M200 340 Q400 180 600 300" stroke="#1ad8ff" stroke-width="4" fill="none" stroke-dasharray="10 8"/>'
I[1794]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
