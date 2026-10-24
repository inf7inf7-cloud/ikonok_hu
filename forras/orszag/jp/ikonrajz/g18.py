import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 18. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 106 時の過ぎゆくままに: a pocket watch with its chain hanging over a bar counter, a cigarette smoke curl and dim amber light
d,b=bg([(0,'#2a1a14'),(1,'#140a08')])
b+=glow(400,300,240,'#ffb04a',.3)+'<rect y="560" width="800" height="240" fill="#4a2a1a"/><rect y="550" width="800" height="16" fill="#6a3a2a"/>'
b+='<path d="M400 120 Q380 260 400 330" stroke="#d8b040" stroke-width="5" fill="none" stroke-dasharray="8 4"/><circle cx="400" cy="420" r="110" fill="#d8b040"/><circle cx="400" cy="420" r="94" fill="#fbf4e4"/>'+''.join(f'<path d="M{400+80*math.cos(math.radians(a)):.0f} {420+80*math.sin(math.radians(a)):.0f} L{400+90*math.cos(math.radians(a)):.0f} {420+90*math.sin(math.radians(a)):.0f}" stroke="#3a2a1a" stroke-width="4"/>' for a in range(0,360,30))
b+='<path d="M400 420 L400 350 M400 420 L450 440" stroke="#1a1a1a" stroke-width="6" stroke-linecap="round"/><rect x="560" y="520" width="80" height="12" fill="#f4f0e8"/><path d="M640 520 Q660 470 640 430 Q620 390 650 350" stroke="#c8c8d0" stroke-width="4" fill="none" opacity=".6"/>'
I[106]=svg(b,d)

# 162 雪國: a lone house with a glowing window deep in a snowfield, snow piling on its roof under a grey sky
d,b=bg([(0,'#8a94a8'),(1,'#c8d0dc')])
b+=snow(120,162)+'<path d="M-10 560 Q400 500 810 560 L810 810 L-10 810Z" fill="#f4f6fa"/>'
b+='<rect x="300" y="420" width="220" height="160" fill="#5a3a2a"/><path d="M270 430 L410 320 L550 430Z" fill="#3a2a2a"/><path d="M262 432 Q410 290 558 432 Q410 360 262 432Z" fill="#fff"/><rect x="340" y="470" width="60" height="50" fill="#ffd27a"/>'+glow(370,495,60,'#ffd27a',.5)
b+=''.join(f'<path d="M{x} 600 L{x+20} 520 L{x+40} 600Z" fill="#3a5a4a"/><path d="M{x+6} 560 L{x+20} 520 L{x+34} 560Z" fill="#fff"/>' for x in (80,140,620,680))
I[162]=svg(b,d)

# 362 白いパラソル: a white parasol on a sunny beach, a seagull above and a straw hat on the sand
d,b=bg([(0,'#3ab0f8'),(1,'#c8ecff')])
b+=hinomaru_sun(640,120,60,'#fff8c8',.9)+'<rect y="380" width="800" height="140" fill="#1a90d8"/><path d="M-10 520 Q400 490 810 520 L810 810 L-10 810Z" fill="#f4e0a8"/>'
b+='<path d="M400 300 L380 700" stroke="#8a6a4a" stroke-width="8"/><path d="M200 340 Q390 140 600 300 Q500 280 400 300 Q300 290 200 340Z" fill="#fff"/><path d="M400 300 L400 200 M300 320 L360 210 M500 300 L450 205" stroke="#e8e8f0" stroke-width="4"/>'
b+='<ellipse cx="560" cy="680" rx="90" ry="22" fill="#e8c870"/><ellipse cx="560" cy="664" rx="44" ry="26" fill="#e8c870"/><path d="M516 670 L604 670" stroke="#e8302a" stroke-width="8"/>'+'<path d="M180 160 Q200 140 220 160 Q240 140 260 160" stroke="#fff" stroke-width="6" fill="none"/>'
I[362]=svg(b,d)

# 434 神様ヘルプ!: a boy kneeling with clasped hands under a spotlight beam from the clouds, a heart floating just out of reach
d,b=bg([(0,'#2a2a5a'),(1,'#5a3a7a')])
b+=cloud(400,100,2.4,'#c8c8e8')+'<polygon points="340,140 460,140 560,800 240,800" fill="#fff6c8" opacity=".25"/>'+'<rect y="680" width="800" height="120" fill="#1a1430"/>'
b+='<g fill="#0a0814"><circle cx="400" cy="520" r="36"/><path d="M350 680 Q340 580 400 560 Q460 580 450 680Z"/><path d="M380 560 L400 500 L420 560Z"/></g>'+heart(400,330,40,'#ff4a7a')+sparkle(440,300,14,'#fff')
I[434]=svg(b,d)

# 658 MY LONELY TOWN: a single figure on the empty rooftop of an abandoned building, the city lights far away
d,b=bg([(0,'#1a1a2a'),(.7,'#3a3a5a'),(1,'#5a4a6a')])
b+=skyline(640,'#2a2a3a',658,30,120,'#ffd27a',60)+'<rect x="100" y="420" width="380" height="380" fill="#3a3a40"/>'+''.join(f'<rect x="{130+(k%5)*70}" y="{460+(k//5)*80}" width="40" height="50" fill="#14141a"/>' for k in range(15))+'<path d="M230 540 L260 600 L240 640" stroke="#5a5a64" stroke-width="3" fill="none"/>'
b+=figure(300,430,140,'#000')+moon(620,150,40)
I[658]=svg(b,d)

# 875 Ever Free: a pink-haired silhouette guitarist leaping as chains break apart, a blazing red sky
d,b=bg([(0,'#e8102a'),(1,'#3a0a1a')])
b+=rays(400,420,24,'#ffd02a',.2,8)
for x,a in [(160,30),(640,-30)]: b+=f'<g transform="rotate({a} {x} 420)">'+''.join(f'<ellipse cx="{x}" cy="{300+k*40}" rx="14" ry="22" fill="none" stroke="#c8c8d0" stroke-width="6"/>' for k in range(5))+'</g>'
b+=figure(400,640,320,'#0a0408',pose='up',hair='#ff5ab8')+guitar(430,500,.9,-40,'#ff5ab8')
I[875]=svg(b,d)

# 1136 涙のふるさと: a single teardrop falling into a lake, ripples revealing a reflected hometown
d,b=bg([(0,'#5a7ab8'),(1,'#a8c8e8')])
b+=skyline(420,'#5a6a8a',1136,40,120,'#ffd27a',20)+'<rect y="420" width="800" height="380" fill="#3a5a8a"/>'
b+='<g transform="translate(0 840) scale(1 -1)" opacity=".35">'+skyline(420,'#c8d8f0',1136,40,120,'#ffd27a',20)+'</g>'+''.join(ring(400,560,30+k*50,'#e8f0ff',3,.7-k*.12) for k in range(6))
b+='<path d="M400 260 Q430 320 400 340 Q370 320 400 260Z" fill="#c8e8ff" stroke="#fff" stroke-width="3"/>'
I[1136]=svg(b,d)

# 1657 青のすみか: two boys' silhouettes on a school rooftop in a blinding blue summer, cicadas and a soda bottle
d,b=bg([(0,'#1a8af8'),(1,'#a8e0ff')])
b+=cloud(560,160,2.2)+'<rect y="560" width="800" height="240" fill="#c8c8d0"/><rect y="540" width="800" height="24" fill="#8a8a94"/>'+''.join(f'<rect x="{k*50}" y="440" width="6" height="100" fill="#5a6a7a"/>' for k in range(17))+'<rect y="440" width="800" height="8" fill="#5a6a7a"/>'
b+=figure(300,620,240,'#0a1a3a')+figure(480,620,250,'#0a1a3a')+'<rect x="380" y="560" width="22" height="56" rx="6" fill="#8ad8ff" stroke="#fff" stroke-width="3"/>'
I[1657]=svg(b,d)

# 1844 a.m.3:21: a phone screen glowing at 3:21 am in a dark bedroom, a figure curled under the blanket
d,b=bg([(0,'#06081a'),(1,'#141a30')])
b+='<path d="M-10 520 Q400 460 810 520 L810 810 L-10 810Z" fill="#1a2a4a"/><path d="M160 520 Q260 420 380 470 Q480 420 560 520Z" fill="#2a3a5a"/>'
b+=glow(460,520,140,'#8ad0ff',.45)+'<rect x="420" y="430" width="80" height="140" rx="12" fill="#1a1a24" transform="rotate(-14 460 500)"/><rect x="428" y="440" width="64" height="120" rx="6" fill="#c8ecff" transform="rotate(-14 460 500)"/><text x="452" y="510" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-weight="bold" font-size="24" fill="#1a2a4a" transform="rotate(-14 460 500)">3:21</text>'
b+=moon(640,140,36)
I[1844]=svg(b,d)

# 66 恋の季節: a girl in a 60s mini dress with a parasol by the sea in early summer, a big flower in her hair
d,b=bg([(0,'#ffb0c8'),(1,'#fff0d8')])
b+=hinomaru_sun(600,220,80,'#fff6d0',.9)+'<rect y="420" width="800" height="120" fill="#5ab0e8"/><rect y="540" width="800" height="260" fill="#f4e0b0"/>'
b+=figure(360,700,360,'#2a1a2a',hair='#2a1a2a')+'<path d="M300 520 L420 520 L440 600 L280 600Z" fill="#ff5a8a"/>'+flower(400,350,26,6,'#ffd02a','#ff5a2a',0,.6)
I[66]=svg(b,d)

# 76 手紙: a handwritten letter left on a table next to a pair of keys, morning light through lace curtains
d,b=bg([(0,'#f4ece0'),(1,'#e0d0c0')])
b+='<rect x="460" y="40" width="300" height="360" fill="#fff" opacity=".7"/>'+''.join(f'<circle cx="{480+(k%7)*40}" cy="{60+(k//7)*40}" r="10" fill="none" stroke="#e8dcd0" stroke-width="3"/>' for k in range(63))
b+='<rect y="420" width="800" height="380" fill="#a87a5a"/><polygon points="460,400 760,400 640,800 260,800" fill="#fff8e0" opacity=".2"/>'
b+='<g transform="rotate(-6 360 560)"><rect x="220" y="460" width="280" height="200" fill="#fbf8f0"/>'+''.join(f'<path d="M240 {500+k*28} Q{300+k*10} {490+k*28} 470 {500+k*28}" stroke="#3a3a6a" stroke-width="3" fill="none"/>' for k in range(5))+'</g>'
b+='<circle cx="580" cy="600" r="22" fill="none" stroke="#c8c8d0" stroke-width="6"/><rect x="596" y="596" width="70" height="10" fill="#c8c8d0"/><rect x="646" y="606" width="8" height="14" fill="#c8c8d0"/>'
I[76]=svg(b,d)

# 311 激愛: two hands clasped so tightly the knuckles whiten, wrapped in a red thread, against stormy dark
d,b=bg([(0,'#2a0a14'),(1,'#0a0408')])
b+=glow(400,400,220,'#e8102a',.35)+'<g fill="#d8a888"><rect x="120" y="340" width="300" height="110" rx="50"/><rect x="380" y="350" width="300" height="110" rx="50"/></g>'
b+='<path d="M360 330 Q400 300 440 330 L440 470 Q400 500 360 470Z" fill="#c8987a"/>'+''.join(f'<path d="M360 {350+k*30} Q400 {330+k*30} 440 {350+k*30}" stroke="#e8102a" stroke-width="5" fill="none"/>' for k in range(5))
b+='<path d="M440 460 Q520 560 600 520 Q680 480 760 600" stroke="#e8102a" stroke-width="5" fill="none"/>'
I[311]=svg(b,d)

# 556 CATCH ME: a girl tossing a heart-shaped balloon to a boy across a sunny city plaza
d,b=bg([(0,'#5ac8ff'),(1,'#e0f4ff')])
b+=skyline(560,'#a8b8d8',556,60,200,'#fff',20)+'<rect y="560" width="800" height="240" fill="#e8dcc8"/>'
b+=figure(200,720,260,'#3a2a4a',pose='reach',hair='#3a2a4a')+figure(620,720,270,'#2a3a5a',pose='up')
b+='<path d="M400 260 Q420 340 400 400" stroke="#fff" stroke-width="3" fill="none"/>'+heart(400,240,50,'#ff3a7a')+'<path d="M260 420 Q400 280 560 420" stroke="#fff" stroke-width="3" stroke-dasharray="8 8" fill="none"/>'
I[556]=svg(b,d)

# 659 SUPER LOVE SONG: a guitar amp blasting a shockwave of hearts across a concert stage
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a1a')])
b+=''.join(f'<polygon points="{x},0 {x-80},700 {x+80},700" fill="{c}" opacity=".15"/>' for x,c in [(160,'#ff3a6a'),(400,'#ffd02a'),(640,'#5ae8ff')])+'<rect y="660" width="800" height="140" fill="#14141e"/>'
b+='<rect x="120" y="440" width="220" height="240" rx="12" fill="#2a2a2a"/><circle cx="230" cy="560" r="80" fill="#1a1a1a" stroke="#5a5a5a" stroke-width="8"/><rect x="140" y="456" width="180" height="20" fill="#d8b040"/>'
b+=''.join(ring(230,560,100+k*80,'#ff3a6a',6,.5-k*.08) for k in range(5))+''.join(heart(380+k*90,520-k*70,22+k*4,'#ff3a6a') for k in range(4))
I[659]=svg(b,d)

# 742 口笛: two people walking side by side on a riverside path, musical whistle notes drifting up into the evening sky
d,b=bg([(0,'#ffb88a'),(1,'#ffe0c0')])
b+='<rect y="460" width="800" height="120" fill="#5a8ab8"/><path d="M-10 580 Q400 540 810 580 L810 810 L-10 810Z" fill="#8ab86a"/><path d="M-10 680 Q400 640 810 680" stroke="#e8d8b0" stroke-width="40" fill="none"/>'
b+=figure(360,690,220,'#3a2a2a')+figure(440,690,200,'#3a2a2a',hair='#3a2a2a')+''.join(note(320+k*60,400-k*50,16,'#5a3a2a',k%2==0) for k in range(5))
I[742]=svg(b,d)

# 876 Pink Spider: a bright pink spider on a web stretched across a window, a blue sky and birds beyond it
d,b=bg([(0,'#3ab0f8'),(1,'#c8ecff')])
b+='<path d="M180 220 Q200 200 220 220 M620 160 Q640 140 660 160" stroke="#1a1a2a" stroke-width="4" fill="none"/>'
for a in range(0,360,30): b+=f'<path d="M400 400 L{400+380*math.cos(math.radians(a)):.0f} {400+380*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="2" opacity=".8"/>'
b+=''.join(f'<polygon points="'+' '.join(f'{400+r*math.cos(math.radians(a)):.0f},{400+r*math.sin(math.radians(a)):.0f}' for a in range(0,360,30))+'" fill="none" stroke="#fff" stroke-width="2" opacity=".7"/>' for r in range(60,360,60))
b+='<ellipse cx="400" cy="420" rx="50" ry="60" fill="#ff4ab8"/><circle cx="400" cy="350" r="30" fill="#ff4ab8"/>'+''.join(f'<path d="M{400+s*40} {400+k*20} Q{400+s*110} {360+k*30} {400+s*140} {420+k*40}" stroke="#ff4ab8" stroke-width="8" fill="none"/>' for s in (-1,1) for k in range(4))
I[876]=svg(b,d)

# 1604 BANG!!: a comic-style explosion burst with a starburst shape, confetti and nine silhouettes leaping
d,b=bg([(0,'#ffd02a'),(1,'#ff5a2a')])
pts=' '.join(f'{400+(300 if k%2==0 else 170)*math.cos(math.radians(k*18)):.0f},{360+(300 if k%2==0 else 170)*math.sin(math.radians(k*18)):.0f}' for k in range(20))
b+=f'<polygon points="{pts}" fill="#fff"/><polygon points="{pts}" fill="#ff2a5a" transform="translate(400 360) scale(.7) translate(-400 -360)"/>'
r=R(1604)
for _ in range(30): x,y=r.uniform(0,800),r.uniform(0,600);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="12" height="20" fill="{r.choice(["#2a5ae8","#3ac85a","#fff","#a85aff"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+='<rect y="700" width="800" height="100" fill="#3a1a0a"/>'+''.join(figure(100+k*75,710-(k%2)*30,130,'#1a0a0a',pose='up') for k in range(9))
I[1604]=svg(b,d)

# 52 恋のしずく: a single raindrop sliding down a window pane, a blurred city and a woman's reflection behind it
d,b=bg([(0,'#5a6a8a'),(1,'#8a9ab8')])
b+=''.join(glow(x,y,40,c,.5) for x,y,c in [(120,500,'#ffd27a'),(300,560,'#ff8a8a'),(560,520,'#8ad0ff'),(700,600,'#ffd27a')])
b+=f'<g opacity=".35">'+figure(400,820,560,'#1a1a2a',hair='#1a1a2a')+'</g>'
b+='<path d="M520 180 Q540 230 520 250 Q500 230 520 180Z" fill="#e8f4ff" stroke="#fff" stroke-width="3"/><path d="M520 250 Q516 330 524 420" stroke="#e8f4ff" stroke-width="4" fill="none" opacity=".6"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e8f4ff" opacity=".6"/>' for x,y,r in [(200,160,6),(300,300,4),(640,240,5),(160,400,4),(680,420,6)])
I[52]=svg(b,d)

# 240 ひこうき雲: a white contrail rising straight up into a clear blue sky from a hilltop, a small figure watching
d,b=bg([(0,'#1a6ad8'),(1,'#c8e8ff')])
b+='<path d="M560 80 Q520 300 440 600" stroke="#fff" stroke-width="16" fill="none" opacity=".9"/><path d="M560 80 Q520 300 440 600" stroke="#fff" stroke-width="40" fill="none" opacity=".25"/><path d="M552 80 L572 60 L568 90Z" fill="#fff"/>'
b+='<path d="M-10 640 Q300 560 810 640 L810 810 L-10 810Z" fill="#5aa84a"/>'+figure(240,620,150,'#1a2a3a',hair='#1a2a3a')
I[240]=svg(b,d)

# 256 雨やどり: a young man and woman sheltering together under a shop awning in sudden rain, laughing
d,b=bg([(0,'#7a8aa0'),(1,'#a8b4c4')])
b+=rain(120,256,'#e8f0ff',.45,5)+'<rect x="80" y="200" width="640" height="600" fill="#e8dcc8"/><rect x="140" y="380" width="200" height="260" fill="#8ab8d8"/><rect x="460" y="380" width="200" height="420" fill="#6a4a3a"/>'
b+=''.join(f'<path d="M{60+k*80} 300 L{140+k*80} 300 L{120+k*80} 360 L{80+k*80} 360Z" fill="{"#e8302a" if k%2 else "#fff"}"/>' for k in range(9))
b+=figure(330,800,320,'#2a2a3a')+figure(450,800,300,'#3a2a3a',hair='#3a2a3a')
I[256]=svg(b,d)

# 317 さよなら夏の日: a couple's silhouettes on a seaside hill watching the last fireworks of summer, rain clouds clearing
d,b=bg([(0,'#1a1a4a'),(1,'#4a3a6a')])
b+=firework(260,220,110,'#ffd02a',26,317)+firework(560,160,90,'#ff5a8a',22,3170)+'<rect y="480" width="800" height="120" fill="#1a2a5a"/><path d="M-10 640 Q400 560 810 640 L810 810 L-10 810Z" fill="#0a1020"/>'
b+=figure(380,620,160,'#000')+figure(440,620,150,'#000',hair='#000')
I[317]=svg(b,d)

# 621 めぐり逢い: two winding paths through a starry valley converging at a single lamp-lit crossroad
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=starsf(60,621,400,'#fff')+'<path d="M-10 500 Q400 420 810 500 L810 810 L-10 810Z" fill="#1a2a3a"/>'
b+='<path d="M60 800 Q200 640 400 560" stroke="#c8b890" stroke-width="24" fill="none"/><path d="M740 800 Q600 640 400 560" stroke="#c8b890" stroke-width="24" fill="none"/>'+'<rect x="396" y="440" width="8" height="120" fill="#2a2a34"/>'+glow(400,440,50,'#ffe8a0',.8)
b+=figure(180,720,90,'#000')+figure(620,720,86,'#000',hair='#000')
I[621]=svg(b,d)

# 660 SPLASH!: a figure cannonballing into a turquoise pool, a giant splash crown erupting
d,b=bg([(0,'#1ac8f8'),(1,'#a8f0ff')])
b+=hinomaru_sun(660,120,60,'#fff8c8',.9)+'<rect y="460" width="800" height="340" fill="#1ab0d8"/>'+''.join(f'<path d="M{k*100-40} {520+(k%3)*80} Q{k*100} {500+(k%3)*80} {k*100+40} {520+(k%3)*80}" stroke="#bff4ff" stroke-width="5" fill="none"/>' for k in range(9))
for a in range(-80,81,20): b+=f'<path d="M{400+a*.8:.0f} 470 Q{400+a*2:.0f} {300-abs(a)} {400+a*3:.0f} {380+abs(a)}" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round"/>'
b+=''.join(f'<circle cx="{400+r*math.cos(math.radians(a)):.0f}" cy="{300+r*.6*math.sin(math.radians(a)):.0f}" r="10" fill="#fff"/>' for a,r in [(200,260),(240,220),(300,240),(340,280),(260,300)])+'<ellipse cx="400" cy="470" rx="180" ry="30" fill="#fff"/>'
I[660]=svg(b,d)

# 519 大阪LOVER: a woman with a suitcase on a bullet-train platform, the Osaka skyline and its tower glowing at dusk
d,b=bg([(0,'#ff8a6a'),(1,'#ffd0a0')])
b+=skyline(520,'#7a4a5a',519,60,200,'#ffd27a',30)+'<rect x="540" y="200" width="30" height="320" fill="#7a4a5a"/><rect x="520" y="260" width="70" height="30" fill="#7a4a5a"/>'+glow(555,275,40,'#ffd27a',.6)
b+='<rect y="580" width="800" height="220" fill="#8a8a94"/><rect y="580" width="800" height="14" fill="#ffd02a"/><path d="M-10 440 L380 440 Q440 440 460 500 L460 560 L-10 560Z" fill="#f4f4f8"/><path d="M-10 500 L450 500" stroke="#2a5ae8" stroke-width="10"/>'
b+=figure(620,740,240,'#2a1a2a',hair='#2a1a2a')+'<rect x="660" y="660" width="60" height="80" rx="8" fill="#e8302a"/><path d="M676 660 L676 640 L704 640 L704 660" stroke="#3a3a3a" stroke-width="4" fill="none"/>'
I[519]=svg(b,d)

# 528 晴れたらいいね: two hikers on a mountain ridge under a clearing sky, a rainbow forming and backpacks on
d,b=bg([(0,'#7ac0ff'),(1,'#e0f4ff')])
for k,c in enumerate(['#e8302a','#ff8a2a','#ffd02a','#3ac85a','#2a8ae8','#7a5ae8']): b+=f'<path d="M100 600 A320 320 0 0 1 740 600" stroke="{c}" stroke-width="16" fill="none" opacity=".6" transform="translate(0 {k*16})"/>'
b+=cloud(120,180,1.2)+'<path d="M-10 800 L200 520 L380 640 L560 460 L810 700 L810 800Z" fill="#5a8a4a"/>'+figure(470,560,140,'#1a2a1a',pose='wave')+figure(540,530,130,'#1a2a1a',hair='#1a2a1a')
I[528]=svg(b,d)

# 782 Message: a message in a bottle washing ashore at sunrise, the paper inside glowing
d,b=bg([(0,'#ff9a7a'),(1,'#ffe0b0')])
b+=hinomaru_sun(400,400,110,'#fff6d0',.8)+'<rect y="420" width="800" height="160" fill="#4a8ac8"/><path d="M-10 580 Q400 540 810 580 L810 810 L-10 810Z" fill="#f4dca0"/><path d="M-10 590 Q200 560 400 590 T810 580" stroke="#fff" stroke-width="10" fill="none"/>'
b+='<g transform="rotate(-20 400 660)"><path d="M300 640 L460 640 Q500 640 500 680 L500 680 Q500 700 460 700 L300 700 Q280 700 280 670 Q280 640 300 640Z" fill="#8ad0c8" opacity=".75"/><rect x="500" y="656" width="40" height="28" fill="#8ad0c8" opacity=".75"/><rect x="540" y="652" width="20" height="36" fill="#a87a4a"/><rect x="320" y="652" width="140" height="36" rx="10" fill="#fbf4e4"/></g>'+glow(390,660,60,'#fff4c8',.5)
I[782]=svg(b,d)

# 837 ここではない、どこかへ: a commuter's silhouette stepping off a crowded grey platform onto a road that leads to an open green horizon
d,b=bg([(0,'#5a8ac8'),(1,'#d8ecff')])
b+='<rect x="0" y="0" width="400" height="800" fill="#6a6a74"/>'+''.join(figure(40+k*60,700,180,'#3a3a44') for k in range(6))
b+='<rect x="400" y="520" width="400" height="280" fill="#7ac86a"/><path d="M400 700 Q600 620 800 540" stroke="#e8d8b0" stroke-width="40" fill="none"/>'+hinomaru_sun(700,300,60,'#fff8d0',.8)
b+=figure(460,700,200,'#1a1a2a',pose='wave')
I[837]=svg(b,d)

# 866 snow drop: white snowdrop flowers pushing through snow beside a lonely bench, a gentle snowfall
d,b=bg([(0,'#a8b8d0'),(1,'#e0e8f4')])
b+=snow(70,866)+'<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#f8faff"/>'+'<rect x="440" y="500" width="260" height="20" fill="#5a3a2a"/><rect x="450" y="520" width="12" height="60" fill="#3a2a1a"/><rect x="680" y="520" width="12" height="60" fill="#3a2a1a"/>'
for x in (160,250,330): b+=f'<g transform="translate({x} 640) scale(2) translate({-x} -640)"><path d="M{x} 640 Q{x-4} 560 {x+20} 520" stroke="#4a8a3a" stroke-width="6" fill="none"/><path d="M{x+20} 520 Q{x} 540 {x+6} 570 Q{x+20} 560 {x+20} 520Z M{x+20} 520 Q{x+40} 540 {x+34} 570 Q{x+20} 560 {x+20} 520Z" fill="#fff" stroke="#c8d8e8" stroke-width="2"/></g>'
I[866]=svg(b,d)

# 1441 ReawakeR: a sword stuck in the ground bursting with blue light as a figure rises behind it
d,b=bg([(0,'#0a1438'),(1,'#1a0a2a')])
b+=rays(400,400,24,'#5ae8ff',.25,6)+glow(400,400,180,'#5ae8ff',.6)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'
b+=figure(400,640,320,'#000',pose='up')+'<path d="M400 640 L400 360" stroke="#e8f8ff" stroke-width="16"/><rect x="360" y="620" width="80" height="16" fill="#d8b040"/><rect x="392" y="636" width="16" height="40" fill="#5a3a2a"/>'
I[1441]=svg(b,d)

# 1447 LAST STARDUST: a single star-shaped sword hilt glowing amid falling golden dust in a ruined field of swords
d,b=bg([(0,'#3a1a1a'),(1,'#8a4a2a')])
b+=hinomaru_sun(400,260,140,'#ffb04a',.5)+'<rect y="560" width="800" height="240" fill="#4a2a1a"/>'
r=R(1447)
for _ in range(22): x=r.uniform(20,780);y=r.uniform(560,780);a=r.uniform(-20,20);b+=f'<path d="M{x:.0f} {y:.0f} L{x+math.sin(math.radians(a))*120:.0f} {y-120:.0f}" stroke="#2a1a14" stroke-width="6"/><path d="M{x-14+math.sin(math.radians(a))*100:.0f} {y-100:.0f} l28 0" stroke="#2a1a14" stroke-width="6"/>'
b+=''.join(f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(0,600):.0f}" r="3" fill="#ffd27a" opacity=".8"/>' for _ in range(50))+figure(400,600,200,'#140808')
I[1447]=svg(b,d)

# 1692 シクラメンのかほり: a pot of pale pink cyclamen on a windowsill in winter light, a faded love letter beside it
d,b=bg([(0,'#d8d0e0'),(1,'#f0e8f0')])
b+='<rect x="100" y="60" width="600" height="420" fill="#c8d8ec"/><path d="M100 60 L700 60 L700 480 L100 480Z M400 60 L400 480" stroke="#fff" stroke-width="16" fill="none"/>'+snow(20,1692)
b+='<rect y="480" width="800" height="320" fill="#e8dcc8"/><path d="M320 520 L480 520 L460 680 L340 680Z" fill="#a85a4a"/>'
for x,y,a in [(340,420,-20),(400,380,0),(460,420,20),(370,460,-10),(430,460,10)]: b+=f'<path d="M400 520 Q{x} 480 {x} {y+30}" stroke="#3a6a3a" stroke-width="5" fill="none"/><path d="M{x} {y+30} Q{x-30} {y-20} {x-10} {y-40} Q{x} {y} {x+10} {y-40} Q{x+30} {y-20} {x} {y+30}Z" fill="#ffb8d0" transform="rotate({a} {x} {y})"/>'
b+='<rect x="540" y="620" width="160" height="100" fill="#fbf4e4" transform="rotate(8 620 670)"/>'
I[1692]=svg(b,d)

# 294 銀河鉄道999: a steam locomotive flying up a spiral track into the starry galaxy
d,b=bg([(0,'#04041a'),(1,'#1a1440')])
b+=starsf(120,294,800,'#fff')+'<ellipse cx="520" cy="200" rx="260" ry="60" fill="#c8a8ff" opacity=".25" transform="rotate(-20 520 200)"/>'
b+='<path d="M-10 760 Q300 700 400 560 Q500 400 700 260" stroke="#c8c8e8" stroke-width="6" fill="none" stroke-dasharray="14 8"/>'
b+='<g transform="translate(420 520) rotate(-40)"><rect x="-120" y="-40" width="200" height="70" rx="10" fill="#1a1a2a"/><rect x="40" y="-90" width="40" height="60" fill="#1a1a2a"/><rect x="-100" y="-80" width="30" height="40" fill="#1a1a2a"/>'+''.join(f'<circle cx="{-90+k*50}" cy="36" r="20" fill="#3a3a4a" stroke="#d8b040" stroke-width="4"/>' for k in range(4))+'<rect x="-60" y="-26" width="60" height="30" fill="#ffd27a"/></g>'+''.join(f'<circle cx="{460+k*40}" cy="{420-k*50}" r="{20+k*10}" fill="#fff" opacity="{.5-k*.1:.1f}"/>' for k in range(4))
I[294]=svg(b,d)

# 363 天国のキッス: two silhouettes kissing on a cloud bathed in pink-golden heavenly light
d,b=bg([(0,'#ffb0d8'),(1,'#ffe8c0')])
b+=rays(400,300,24,'#fff',.35,9)+cloud(400,600,3.4,'#fff',.98)+figure(370,560,240,'#5a2a4a')+figure(430,560,224,'#5a2a4a',hair='#5a2a4a')+heart(400,320,28,'#ff3a7a')
I[363]=svg(b,d)

# 661 BANZAI: a crowd of arms raised in a cheer before a giant rising sun, ticker tape raining down
d,b=bg([(0,'#ffd02a'),(1,'#ff8a2a')])
b+=hinomaru_sun(400,360,180,'#e8102a',1)+rays(400,360,24,'#fff',.25,8)
r=R(661)
for _ in range(40): x,y=r.uniform(0,800),r.uniform(0,600);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="8" height="24" fill="#fff" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+='<rect y="640" width="800" height="160" fill="#3a1a0a"/>'+''.join(figure(60+k*70,700+(k%2)*20,160,'#2a0a0a',pose='up') for k in range(11))
I[661]=svg(b,d)

# 682 一番偉い人へ: a tiny man in a suit bowing before a giant empty throne with a crown on it, humorous scale
d,b=bg([(0,'#5a3a7a'),(1,'#2a1a4a')])
b+='<rect y="640" width="800" height="160" fill="#8a1a2a"/><path d="M200 640 L200 200 Q400 120 600 200 L600 640Z" fill="#d8a838"/><rect x="250" y="380" width="300" height="260" fill="#a8102a"/>'
b+='<path d="M330 200 L350 140 L380 180 L400 120 L420 180 L450 140 L470 200Z" fill="#ffd02a"/>'
b+='<g fill="#0a0a14"><circle cx="350" cy="676" r="24"/><path d="M370 690 Q420 660 450 700 L440 790 L410 790 L400 720 Q380 720 370 700Z"/><rect x="360" y="690" width="16" height="70" rx="8" transform="rotate(20 368 690)"/></g>'
I[682]=svg(b,d)

# 765 楓: falling maple leaves over an empty bench by a quiet lake, one red leaf landing on the water
d,b=bg([(0,'#d8b8a0'),(1,'#f4e0c8')])
b+='<rect y="440" width="800" height="360" fill="#8aa0b8"/>'+''.join(f'<path d="M{x} 440 L{x+60} 260 L{x+120} 440Z" fill="#c8601a"/>' for x in (-40,80,520,640))
r=R(765)
for _ in range(16):
    x,y=r.uniform(60,740),r.uniform(60,420);a=r.uniform(0,90)
    b+=f'<path d="M{x:.0f} {y:.0f} l-14 -6 l6 -16 l8 10 l8 -10 l6 16Z" fill="{r.choice(["#e8402a","#e8802a","#c8301a"])}" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+='<rect x="280" y="520" width="240" height="18" fill="#5a3a2a"/><rect x="290" y="538" width="10" height="50" fill="#3a2a1a"/><rect x="500" y="538" width="10" height="50" fill="#3a2a1a"/>'+ring(400,700,40,'#fff',3,.6)+'<path d="M400 700 l-14 -6 l6 -16 l8 10 l8 -10 l6 16Z" fill="#e8102a"/>'
I[765]=svg(b,d)

# 838 Way of Difference: two people walking away from each other on a forked road, their shadows still touching
d,b=bg([(0,'#ffa87a'),(1,'#ffe0c0')])
b+=hinomaru_sun(400,320,90,'#fff2d0',.8)+'<rect y="400" width="800" height="400" fill="#c8a880"/><path d="M400 800 L400 560 L160 400 M400 560 L640 400" stroke="#e8d8b8" stroke-width="40" fill="none"/>'
b+=figure(270,500,140,'#2a1a1a')+figure(530,500,130,'#2a1a1a',hair='#2a1a1a')+'<path d="M270 500 L380 640 L420 640 L530 500" stroke="#000" stroke-width="16" opacity=".25" fill="none"/>'
I[838]=svg(b,d)

# 867 X X X: a pair of lips seen in profile behind a veil of dark lace, red light and three crosses
d,b=bg([(0,'#1a0408'),(1,'#3a0a14')])
b+=glow(400,420,220,'#e8102a',.35)+'<path d="M300 380 Q360 330 400 360 Q440 330 500 380 Q440 410 400 400 Q360 410 300 380Z" fill="#c80a1a"/><path d="M300 384 Q400 470 500 384 Q440 420 400 416 Q360 420 300 384Z" fill="#8a0a14"/>'
b+=''.join(f'<path d="M0 {k*40} L800 {k*40+400}" stroke="#000" stroke-width="2" opacity=".5"/><path d="M800 {k*40} L0 {k*40+400}" stroke="#000" stroke-width="2" opacity=".5"/>' for k in range(-10,20))
b+=''.join(f'<path d="M{x-30} 620 L{x+30} 680 M{x+30} 620 L{x-30} 680" stroke="#ff4a5a" stroke-width="12"/>' for x in (280,400,520))
I[867]=svg(b,d)

# 908 Darling: a boy holding an umbrella for a girl under a streetlamp, a heart-shaped puddle at their feet
d,b=bg([(0,'#2a2a5a'),(1,'#5a4a7a')])
b+=rain(80,908,'#c8d8ff',.35,4)+'<rect y="660" width="800" height="140" fill="#2a2a3a"/><ellipse cx="400" cy="720" rx="130" ry="20" fill="#ff8ab8" opacity=".35"/>'+glow(620,200,60,'#ffe8a0',.7)+'<rect x="616" y="200" width="8" height="460" fill="#1a1a2a"/>'
b+=figure(360,700,260,'#0a0a1a')+figure(450,700,230,'#0a0a1a',hair='#0a0a1a')+wagasa(410,410,150,'#ff5a8a',-6)
I[908]=svg(b,d)

# 943 ビロードの闇: a velvet curtain parting on a dark stage, a single red rose on the floor in a spotlight
d,b=bg([(0,'#0a0408'),(1,'#1a0a10')])
b+='<polygon points="400,0 260,700 540,700" fill="#fff6d8" opacity=".12"/><ellipse cx="400" cy="680" rx="160" ry="30" fill="#fff6d8" opacity=".2"/><rect y="680" width="800" height="120" fill="#2a1414"/>'
for s in (-1,1): b+=f'<path d="M{400+s*400} 0 L{400+s*120} 0 Q{400+s*200} 400 {400+s*170} 800 L{400+s*400} 800Z" fill="#5a0a1a"/>'+''.join(f'<path d="M{400+s*(140+k*40)} 0 Q{400+s*(210+k*40)} 400 {400+s*(180+k*40)} 800" stroke="#3a0410" stroke-width="6" fill="none"/>' for k in range(6))
b+='<path d="M360 690 L460 670" stroke="#2a5a2a" stroke-width="6"/>'+rose(350,688,.8,-30)
I[943]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
