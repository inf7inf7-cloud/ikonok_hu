import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 22. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1589 合法的トビ方ノススメ: a figure leaping off a stack of speakers into a crowd of light, mic cord trailing
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a1a')])
b+=rays(400,300,30,'#ffd02a',.12,6)+'<rect x="80" y="520" width="200" height="280" fill="#141414"/>'+''.join(ring(180,600+k*110,40,'#3a3a3a',10) for k in range(2))
b+='<g transform="rotate(-20 420 360)">'+figure(420,460,280,'#000',pose='up')+'</g>'+'<path d="M470 240 Q560 320 520 460 Q480 560 600 640" stroke="#ff4a4a" stroke-width="5" fill="none"/>'
b+=''.join(f'<circle cx="{x}" cy="{740-((x*7)%30)}" r="22" fill="#000"/>' for x in range(320,800,44))
I[1589]=svg(b,d)

# 1616 I promise: two pinky fingers hooked together in a promise, soft pink sunset glow
d,b=bg([(0,'#ffb8c8'),(1,'#fff0f0')])
b+=glow(400,420,220,'#fff',.6)+sparkle(270,250,22,'#fff')+sparkle(540,230,16,'#fff')
b+='<g fill="#f0c8b0" stroke="#c8a088" stroke-width="5"><path d="M-10 520 L240 470 Q300 460 340 440 Q380 420 400 440 Q410 460 380 470 L300 500 L-10 600Z"/><path d="M810 340 L560 380 Q500 390 460 410 Q420 430 400 410 Q392 392 420 380 L500 350 L810 270Z"/></g>'+'<path d="M380 450 Q400 400 420 420" stroke="#c8a088" stroke-width="16" fill="none" stroke-linecap="round"/>'
I[1616]=svg(b,d)

# 1651 オトナブルー: a schoolgirl silhouette with a bob cut posing under a blue spotlight, a retro 80s blue palette
d,b=bg([(0,'#0a1a5a'),(1,'#2a5ab8')])
b+='<polygon points="400,0 260,720 540,720" fill="#8ad8ff" opacity=".25"/><rect y="700" width="800" height="100" fill="#0a1030"/>'
b+=figure(400,710,420,'#05081a',pose='reachL')+'<path d="M368 300 Q370 248 400 246 Q432 248 434 300 L420 300 Q420 272 400 270 Q382 272 380 300Z" fill="#05081a"/><path d="M350 480 L450 480 L470 540 L330 540Z" fill="#1a2a6a"/>'
I[1651]=svg(b,d)

# 1791 Hi-Five: two hands meeting in a high five with a burst of colourful stars
d,b=bg([(0,'#ff8ad8'),(1,'#8ad8ff')])
b+=rays(400,360,24,'#fff',.25,8)+''.join(star5(x,y,s,c) for x,y,s,c in [(400,200,40,'#ffd02a'),(250,260,24,'#fff'),(560,250,28,'#fff'),(300,520,20,'#ffd02a'),(520,540,22,'#ffd02a')])
b+='<g fill="#f0c8b0" stroke="#c8a088" stroke-width="5"><path d="M180 800 L250 500 Q260 400 320 340 L380 330 Q400 360 380 420 L330 520 L300 800Z"/><path d="M620 800 L550 500 Q540 400 480 340 L420 330 Q400 360 420 420 L470 520 L500 800Z"/></g>'
I[1791]=svg(b,d)

# 1872 AM11:00: a bedside alarm clock showing 11:00 with morning sun through curtains and a phone ringing
d,b=bg([(0,'#fff0c8'),(1,'#ffd8a0')])
b+='<path d="M0 0 L240 0 Q200 300 260 600 L0 600Z M800 0 L560 0 Q600 300 540 600 L800 600Z" fill="#f8f4ea"/>'+glow(400,200,240,'#fff',.7)+'<rect y="560" width="800" height="240" fill="#c8a080"/>'
b+='<rect x="250" y="380" width="300" height="200" rx="30" fill="#2a2a34"/><rect x="270" y="400" width="260" height="140" rx="12" fill="#1a1a1a"/>'+txt(400,500,'11:00',90,'#ff4a4a',900)
b+='<rect x="580" y="500" width="70" height="120" rx="10" fill="#1a1a1a" transform="rotate(10 615 560)"/>'+''.join(f'<path d="M{660+k*14} {480+k*6} Q{680+k*14} 500 {660+k*14} 520" stroke="#3a8af8" stroke-width="4" fill="none"/>' for k in range(3))
I[1872]=svg(b,d)

# 59 エメラルドの伝説: a glowing emerald on a velvet cushion in a misty fairy-tale lake castle, late-60s psychedelic hues
d,b=bg([(0,'#1a3a3a'),(1,'#4a6a5a')])
b+='<path d="M560 420 L560 260 L600 220 L640 260 L640 420Z M660 420 L660 300 L690 270 L720 300 L720 420Z" fill="#2a4a4a"/><rect y="420" width="800" height="380" fill="#1a3a3a"/>'+cloud(300,420,3,'#c8e8d8',.35)
b+='<ellipse cx="380" cy="600" rx="150" ry="40" fill="#8a1a3a"/>'+glow(380,500,140,'#4aff9a',.5)+'<polygon points="380,400 460,460 430,580 330,580 300,460" fill="#1ad86a"/><polygon points="380,400 410,460 380,580 350,460" fill="#7affb0"/>'
I[59]=svg(b,d)

# 190 旅の宿: an old ryokan room with a full moon outside the shoji, a sake cup and a yukata draped on the floor
d,b=bg([(0,'#2a2030'),(1,'#1a1418')])
b+='<rect x="200" y="100" width="400" height="360" fill="#e8dcc0"/>'+moon(400,260,90,'#fff6d8',.2)+''.join(f'<path d="M{200+k*80} 100 L{200+k*80} 460" stroke="#6a4a2a" stroke-width="6"/>' for k in range(6))+''.join(f'<path d="M200 {100+k*90} L600 {100+k*90}" stroke="#6a4a2a" stroke-width="6"/>' for k in range(5))
b+='<rect y="460" width="800" height="340" fill="#b8a870"/>'+''.join(f'<path d="M0 {500+k*70} L800 {500+k*70}" stroke="#a09060" stroke-width="3"/>' for k in range(5))
b+='<path d="M200 640 Q300 600 420 640 Q460 680 380 700 L220 700Z" fill="#3a5a8a"/><path d="M520 620 L512 580 L568 580 L560 620Z" fill="#f4ead8"/>'
I[190]=svg(b,d)

# 229 ヘッドライト・テールライト: a long night highway with streams of white headlights and red taillights flowing past each other
d,b=bg([(0,'#050814'),(1,'#141a30')])
b+=starsf(30,229,300)+'<path d="M370 300 L430 300 L800 800 L0 800Z" fill="#1a1a24"/>'
b+=''.join(f'<path d="M{385-k*30} 300 L{200-k*120} 800" stroke="#ff2a2a" stroke-width="{4+k*3}" opacity=".7"/>' for k in range(3))+''.join(f'<path d="M{415+k*30} 300 L{600+k*120} 800" stroke="#fff6d8" stroke-width="{4+k*3}" opacity=".8"/>' for k in range(3))
I[229]=svg(b,d)

# 338 真夜中のドア〜stay with me: a door ajar at midnight with warm light spilling into a rain-wet city-pop street
d,b=bg([(0,'#1a1430'),(1,'#3a2a5a')])
b+=rain(40,338,'#c8c8ff',.3)+skyline(560,'#140e24',338,60,260,'#ff8ad8',60)+'<rect y="560" width="800" height="240" fill="#1a1428"/>'
b+='<rect x="300" y="280" width="200" height="380" fill="#0a0814"/><polygon points="300,280 380,300 380,640 300,660" fill="#ffd27a"/>'+'<polygon points="300,660 380,640 520,800 200,800" fill="#ffd27a" opacity=".3"/>'+glow(340,460,120,'#ffd27a',.3)
I[338]=svg(b,d)

# 402 迷宮のアンドローラ: a girl's silhouette standing at the centre of a glowing neon maze, mid-80s pink and cyan
d,b=bg([(0,'#1a0a3a'),(1,'#3a1a5a')])
for k in range(5):
    s=60+k*70
    b+=f'<path d="M{400-s} {420-s} L{400+s} {420-s} L{400+s} {420+s} L{400-s+40} {420+s}" stroke="{["#ff4fa0","#4ad8ff"][k%2]}" stroke-width="10" fill="none" opacity=".8"/>'
b+=figure(400,450,110,'#fff')
I[402]=svg(b,d)

# 622 HEART: a big heart sculpted from glowing red light inside a dark concert hall, beams sweeping out
d,b=bg([(0,'#0a0508'),(1,'#1a0a10')])
b+=''.join(f'<polygon points="400,420 {400+600*math.cos(math.radians(a)):.0f},{420-600*math.sin(math.radians(a)):.0f} {400+600*math.cos(math.radians(a+5)):.0f},{420-600*math.sin(math.radians(a+5)):.0f}" fill="#ff4a6a" opacity=".12"/>' for a in range(0,360,30))
b+=glow(400,420,200,'#ff2a4a',.5)+heart(400,420,150,'#e8102a')+heart(400,420,100,'#ff6a7a')
I[622]=svg(b,d)

# 668 Real Thing Shakes: a heavy guitar amp shaking with shock waves, cracks on the floor
d,b=bg([(0,'#1a1a1a'),(1,'#2a1a10')])
b+=''.join(ring(400,420,180+k*60,'#ff8a2a',6,.5-k*.12) for k in range(4))+'<rect y="640" width="800" height="160" fill="#141414"/>'+bolt([(200,640),(240,700),(200,760),(240,800)],'#3a3a3a',6)+bolt([(600,640),(560,700),(600,760),(560,800)],'#3a3a3a',6)
b+='<g transform="rotate(4 400 460)"><rect x="240" y="280" width="320" height="360" rx="16" fill="#2a2a2a" stroke="#c8a24a" stroke-width="8"/><rect x="270" y="300" width="260" height="40" fill="#1a1a1a"/>'+''.join(f'<circle cx="{300+k*40}" cy="320" r="10" fill="#c8c8c8"/>' for k in range(6))+'<rect x="270" y="360" width="260" height="250" fill="#3a3028"/>'+ring(400,485,90,'#1a1a1a',20)+'</g>'
I[668]=svg(b,d)

# 691 DAN DAN 心魅かれてく: a little boat drifting step by step toward a bright island, the sea in blues
d,b=bg([(0,'#4aa8f0'),(1,'#d8f0ff')])
b+=hinomaru_sun(620,200,70,'#fff6d0')+'<rect y="420" width="800" height="380" fill="#2a7ac8"/><path d="M560 420 Q620 340 700 420Z" fill="#3a8a4a"/>'
b+=''.join(f'<path d="M{80+k*110} {600-k*30} Q{120+k*110} {590-k*30} {160+k*110} {600-k*30}" stroke="#fff" stroke-width="4" fill="none" opacity="{.3+k*.12:.2f}"/>' for k in range(5))
b+='<path d="M240 600 L380 600 L360 640 L260 640Z" fill="#c8302a"/><path d="M310 600 L310 460 L380 590Z" fill="#fff"/>'
I[691]=svg(b,d)

# 947 The Red Light: a single red traffic light glowing on an empty rainy night street, reflections on the asphalt
d,b=bg([(0,'#0a0a14'),(1,'#1a1424')])
b+=rain(70,947,'#c8c8e8',.25)+'<rect y="560" width="800" height="240" fill="#14141c"/>'
b+='<rect x="390" y="200" width="20" height="380" fill="#2a2a2a"/><rect x="340" y="120" width="120" height="260" rx="20" fill="#1a1a1a"/><circle cx="400" cy="180" r="34" fill="#ff1a2a"/>'+glow(400,180,100,'#ff1a2a',.6)+'<circle cx="400" cy="250" r="30" fill="#2a2a2a"/><circle cx="400" cy="320" r="30" fill="#2a2a2a"/>'
b+='<rect x="380" y="600" width="40" height="160" fill="#ff1a2a" opacity=".3"/>'
I[947]=svg(b,d)

# 30 北の旅人: a lone traveller in a long coat on a snowy northern harbour at night, a ship's light far off
d,b=bg([(0,'#0a1430'),(1,'#2a3a5a')])
b+=snow(70,30)+'<rect y="460" width="800" height="200" fill="#1a2a40"/><rect y="660" width="800" height="140" fill="#e8eef8"/><rect x="600" y="440" width="120" height="24" fill="#3a3a44"/><circle cx="640" cy="434" r="6" fill="#ffd27a"/>'
b+=figure(280,680,320,'#05070f')+'<path d="M246 470 L230 620 L330 620 L314 470Z" fill="#05070f"/><path d="M260 360 L300 360 L290 400 L270 400Z" fill="#05070f"/>'
I[30]=svg(b,d)

# 364 秘密の花園: a garden gate in a hedge half open, roses blooming inside, a pastel early-80s idol palette
d,b=bg([(0,'#ffd8e8'),(1,'#fff4f8')])
b+='<rect y="200" width="800" height="440" fill="#5aa85a"/><rect y="640" width="800" height="160" fill="#a8d88a"/>'
b+='<rect x="280" y="300" width="240" height="340" fill="#ffe8f0"/>'+''.join(rose(x,y,.9,0) for x,y in [(330,560),(400,520),(470,570)])+'<path d="M280 300 Q400 200 520 300" stroke="#fff" stroke-width="14" fill="none"/>'
b+='<path d="M280 300 L230 320 L230 660 L280 640Z" fill="#fff" opacity=".9"/>'+''.join(f'<path d="M{240+k*12} 330 L{240+k*12} 640" stroke="#e8c8d8" stroke-width="3"/>' for k in range(4))+''.join(rose(x,y,.6,0) for x,y in [(120,260),(680,280),(80,420),(720,450)])
I[364]=svg(b,d)

# 818 真夜中のダンディー: a man's silhouette in a hat leaning on a lamp post at midnight, cigarette smoke and a neon bar sign
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+=neon(560,240,'BAR','#ff4fa0',90)+'<rect y="640" width="800" height="160" fill="#14141c"/><rect x="200" y="200" width="12" height="460" fill="#2a2a34"/><circle cx="206" cy="190" r="22" fill="#ffd28a"/>'+glow(206,190,80,'#ffd28a',.5)
b+=figure(320,660,300,'#000')+'<path d="M286 380 L354 380 L344 366 L296 366Z M300 366 L340 366 L336 344 L304 344Z" fill="#000"/><path d="M350 420 Q380 380 360 340 Q340 300 370 260" stroke="#c8c8d0" stroke-width="3" fill="none" opacity=".6"/>'
I[818]=svg(b,d)

# 840 BEAUTIFUL DREAMER: a figure lying in a field of tall grass watching clouds turn into shapes at golden hour
d,b=bg([(0,'#7ab8f0'),(.6,'#ffd8a8'),(1,'#f8b878')])
b+=cloud(260,180,1.8)+cloud(560,140,1.4)+'<path d="M-10 560 Q400 520 810 560 L810 810 L-10 810Z" fill="#8a9a4a"/>'
b+=''.join(f'<path d="M{x} 600 Q{x+10} 540 {x+4} 500" stroke="#a8b85a" stroke-width="4" fill="none"/>' for x in range(0,800,22))+'<g fill="#2a2a1a"><circle cx="300" cy="590" r="22"/><path d="M320 584 L560 584 L560 604 L320 604Z"/></g>'
I[840]=svg(b,d)

# 948 永遠のBLOODS: two crossed swords dripping red over a dark gothic rose window
d,b=bg([(0,'#1a0508'),(1,'#050102')])
b+=ring(400,360,220,'#5a1a2a',14)+''.join(f'<path d="M400 360 L{400+220*math.cos(math.radians(a)):.0f} {360+220*math.sin(math.radians(a)):.0f}" stroke="#5a1a2a" stroke-width="8"/>' for a in range(0,360,30))+glow(400,360,180,'#c8102a',.3)
for s in (-1,1): b+=f'<g transform="rotate({s*35} 400 420)"><rect x="390" y="160" width="20" height="440" fill="#d8dce8"/><rect x="350" y="560" width="100" height="16" fill="#c8a24a"/><rect x="392" y="576" width="16" height="70" fill="#3a1a1a"/></g>'
b+='<path d="M400 300 Q410 330 400 340 Q390 330 400 300Z M380 400 Q390 430 380 440 Q370 430 380 400Z" fill="#e8102a"/>'
I[948]=svg(b,d)

# 1238 瞳の中のGalaxy: a spiral galaxy swirling inside the reflection of an eye, pink-violet stars
d,b=bg([(0,'#0a0420'),(1,'#2a0a40')])
b+=starsf(60,1238,800)+'<path d="M100 420 Q400 160 700 420 Q400 680 100 420Z" fill="#14082a" stroke="#c8a8ff" stroke-width="6"/>'
for k in range(240):
    a=k*.13;r2=a*9
    if r2<170: b+=f'<circle cx="{400+r2*math.cos(a):.0f}" cy="{420+r2*math.sin(a)*.8:.0f}" r="{2+(k%3)}" fill="{["#ff8ad8","#c8a8ff","#fff"][k%3]}" opacity=".8"/>'
b+=glow(400,420,50,'#fff',.8)
I[1238]=svg(b,d)

# 1443 ADAMAS: a brilliant diamond splitting light into sharp rays against black, an armoured gauntlet-like edge
d,b=bg([(0,'#050508'),(1,'#141420')])
b+=rays(400,400,32,'#e8f4ff',.2,6)+glow(400,400,180,'#c8e8ff',.4)
b+='<polygon points="280,320 520,320 600,400 400,640 200,400" fill="#e8f4ff"/><polygon points="280,320 340,400 200,400" fill="#c8d8f0"/><polygon points="520,320 460,400 600,400" fill="#a8c0e8"/><polygon points="340,400 460,400 400,640" fill="#d8e8ff"/><polygon points="340,320 460,320 460,400 340,400" fill="#fff"/>'
I[1443]=svg(b,d)

# 1487 愛の花: a single sunflower-orange flower blooming in a cracked old teacup on a sunny wooden table
d,b=bg([(0,'#f8e8c8'),(1,'#f0d0a0')])
b+=glow(560,200,200,'#fff',.6)+'<rect y="560" width="800" height="240" fill="#a86a3a"/>'+''.join(f'<path d="M0 {580+k*50} L800 {580+k*50}" stroke="#8a5a2a" stroke-width="3"/>' for k in range(5))
b+='<path d="M300 560 L320 460 L480 460 L500 560Z" fill="#f4f0e8" stroke="#c8b8a0" stroke-width="5"/><path d="M500 480 Q560 500 500 540" stroke="#c8b8a0" stroke-width="10" fill="none"/>'+bolt([(360,460),(370,500),(355,540)],'#c8b8a0',4)
b+='<path d="M400 460 L400 320" stroke="#3a8a3a" stroke-width="8"/>'+flower(400,280,80,14,'#ff9a2a','#8a4a1a')
I[1487]=svg(b,d)

# 1668 魂のルフラン: a glowing soul orb rising from cupped hands, a ring of light echoing around it like a refrain
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a3a')])
b+=''.join(ring(400,320,80+k*60,'#ffd8a8',4,.6-k*.1) for k in range(5))+glow(400,320,100,'#ffe8c8',.8)+'<circle cx="400" cy="320" r="50" fill="#fff6e0"/>'
b+='<g fill="#e0b098" stroke="#b88a72" stroke-width="5"><path d="M240 640 Q240 520 330 500 Q380 500 390 540 L390 620 Q340 660 240 640Z"/><path d="M560 640 Q560 520 470 500 Q420 500 410 540 L410 620 Q460 660 560 640Z"/></g>'
I[1668]=svg(b,d)

# 232 ひとり上手: a woman alone at a small table with one cup of tea and a book, rain on the window, a quiet room
d,b=bg([(0,'#5a6a7a'),(1,'#8a9aa8')])
b+='<rect x="460" y="120" width="260" height="300" fill="#7a8a9a"/>'+rain(20,232,'#e8f0ff',.5)+'<rect x="460" y="120" width="260" height="300" fill="none" stroke="#3a3a44" stroke-width="12"/><rect y="560" width="800" height="240" fill="#4a3a30"/>'
b+='<rect x="140" y="480" width="360" height="20" fill="#6a4a3a"/><rect x="310" y="500" width="20" height="200" fill="#6a4a3a"/><path d="M380 480 L376 450 L420 450 L416 480Z" fill="#fff"/><rect x="200" y="466" width="90" height="14" fill="#c8302a"/>'
b+='<g fill="#1a1a24"><circle cx="560" cy="380" r="28"/><path d="M528 412 L592 412 L600 560 L520 560Z"/></g>'
I[232]=svg(b,d)

# 365 Strawberry Time: a heap of strawberries and a strawberry-patterned picnic cloth under a pink sky
d,b=bg([(0,'#ffc8d8'),(1,'#fff0f4')])
b+='<path d="M-10 520 L810 480 L810 810 L-10 810Z" fill="#fff"/>'+''.join(f'<rect x="{x}" y="{500+(x//80)%2*0}" width="40" height="40" fill="#ff8aa8" opacity=".5"/>' for x in range(0,800,80))
for x,y,s in [(300,560,1.2),(420,540,1.4),(520,590,1.1),(370,640,1),(470,660,1.1)]:
    b+=f'<path d="M{x-40*s} {y-20*s} Q{x} {y-40*s} {x+40*s} {y-20*s} Q{x+30*s} {y+50*s} {x} {y+60*s} Q{x-30*s} {y+50*s} {x-40*s} {y-20*s}Z" fill="#e8102a"/><path d="M{x-30*s} {y-24*s} L{x} {y-46*s} L{x+30*s} {y-24*s} L{x} {y-14*s}Z" fill="#3aa83a"/>'+''.join(f'<circle cx="{x+dx*s}" cy="{y+dy*s}" r="3" fill="#ffe88a"/>' for dx,dy in [(-15,0),(12,8),(-5,22),(15,-8)])
I[365]=svg(b,d)

# 669 RING: a heavy silver ring spinning on a dark table, a boxing-ring rope of light behind
d,b=bg([(0,'#1a1a24'),(1,'#0a0a10')])
b+=''.join(f'<path d="M0 {200+k*60} L800 {200+k*60}" stroke="#e8302a" stroke-width="8" opacity="{.6-k*.15:.2f}"/>' for k in range(3))+'<rect y="560" width="800" height="240" fill="#141418"/>'
b+='<ellipse cx="400" cy="500" rx="150" ry="80" fill="none" stroke="#d8dce8" stroke-width="36"/><ellipse cx="400" cy="500" rx="150" ry="80" fill="none" stroke="#fff" stroke-width="6" opacity=".6"/><ellipse cx="400" cy="620" rx="160" ry="20" fill="#000" opacity=".5"/>'
I[669]=svg(b,d)

# 949 夏模様: a hand-painted summer pattern of morning glories and wind chimes on a pale blue yukata cloth
d,b=bg([(0,'#d8eef8'),(1,'#b8dcf0')])
for x,y in [(160,200),(560,160),(320,420),(640,480),(200,640),(500,700)]: b+=flower(x,y,60,5,'#5a6ae8','#fff',petal=.9)
b+='<path d="M420 0 L420 140" stroke="#5a5a5a" stroke-width="3"/><path d="M380 140 Q420 100 460 140 L460 190 L380 190Z" fill="#e8f4ff" stroke="#8ab8e8" stroke-width="4"/><path d="M420 190 L420 280" stroke="#8a8a8a" stroke-width="2"/><rect x="400" y="280" width="40" height="70" fill="#fff" stroke="#c8302a" stroke-width="3"/>'
I[949]=svg(b,d)

# 1009 Rule: a giant chess queen standing on a cracked black-and-white board under a red sky
d,b=bg([(0,'#5a0a1a'),(1,'#1a0508')])
b+=''.join(f'<polygon points="{400+(c-r)*60},{560+(c+r)*30} {400+(c-r+1)*60},{560+(c+r+1)*30} {400+(c-r)*60},{560+(c+r+2)*30} {400+(c-r-1)*60},{560+(c+r+1)*30}" fill="{"#f4f0e8" if (c+r)%2 else "#1a1a1a"}"/>' for r in range(4) for c in range(4))
b+='<path d="M340 560 Q330 500 360 460 L340 300 L460 300 L440 460 Q470 500 460 560Z" fill="#0a0a0a"/><path d="M340 300 L320 240 L360 270 L380 220 L400 260 L420 220 L440 270 L480 240 L460 300Z" fill="#0a0a0a"/><circle cx="400" cy="210" r="14" fill="#e8102a"/>'
I[1009]=svg(b,d)

# 1188 love the world: a tiny globe wrapped in glowing pixel hearts and a robotic three-figure dance line
d,b=bg([(0,'#0a0a20'),(1,'#1a1a40')])
b+=''.join(f'<rect x="{x}" y="{y}" width="12" height="12" fill="#ff4fd8" opacity=".6"/>' for x in range(0,800,48) for y in range(0,800,48) if (x+y)%96==0)
b+='<circle cx="400" cy="320" r="140" fill="#2a8af8"/><path d="M300 260 Q360 230 400 280 Q380 340 320 330Z M440 300 Q500 260 520 340 Q480 400 440 360Z" fill="#4ad86a"/>'
b+=''.join(heart(400+190*math.cos(a),320+190*math.sin(a),20,'#ff4fd8') for a in [k*math.pi/4 for k in range(8)])+''.join(figure(x,740,200,'#ff4fd8',pose='reach') for x in (280,400,520))
I[1188]=svg(b,d)

# 1355 太陽ノック: a hand knocking on a door of pure sunlight in a summer sky, a seaside town below
d,b=bg([(0,'#3ab0ff'),(1,'#c8f0ff')])
b+='<rect y="600" width="800" height="200" fill="#1a8ad8"/>'+''.join(f'<rect x="{60+k*110}" y="{540-(k*37)%60}" width="90" height="{80+(k*37)%60}" fill="#fff"/>' for k in range(7))
b+='<rect x="320" y="140" width="200" height="320" rx="20" fill="#ffe86a"/>'+glow(420,300,200,'#fff6a0',.6)+'<circle cx="490" cy="300" r="10" fill="#e8a02a"/>'
b+='<g fill="#f0c8b0" stroke="#c8a088" stroke-width="5"><path d="M120 400 L260 330 Q300 310 310 340 Q312 370 280 380 L140 460Z"/></g>'+''.join(f'<path d="M{316+k*8} {300+k*20} Q{330+k*8} {310+k*20} {316+k*8} {320+k*20}" stroke="#fff" stroke-width="4" fill="none"/>' for k in range(2))
I[1355]=svg(b,d)

# 1356 命は美しい: a single heartbeat line turning into a growing flower stem against white light
d,b=bg([(0,'#f4f8ff'),(1,'#d8e4f4')])
b+='<path d="M40 500 L260 500 L300 420 L340 580 L380 460 L420 500 L520 500 Q560 480 560 420 Q560 340 600 300" stroke="#1a1a2a" stroke-width="8" fill="none"/>'+flower(600,260,60,8,'#ff8ab8','#ffd02a')+'<path d="M560 420 Q520 400 510 370 Q550 380 560 410Z" fill="#4ac84a"/>'
I[1356]=svg(b,d)

# 1392 RATATATA: three bold drumsticks hitting a snare in a storm of black and red percussion lines
d,b=bg([(0,'#0a0a0a'),(1,'#1a0505')])
b+=''.join(f'<path d="M{(k*137)%800} 0 L{(k*137)%800-200} 800" stroke="#e8102a" stroke-width="{4+k%3*4}" opacity=".35"/>' for k in range(14))
b+='<ellipse cx="400" cy="560" rx="220" ry="60" fill="#d8dce8"/><path d="M180 560 L180 680 Q400 760 620 680 L620 560" fill="#e8102a"/><ellipse cx="400" cy="560" rx="220" ry="60" fill="none" stroke="#1a1a1a" stroke-width="10"/>'
b+=''.join(f'<path d="M{x} 520 L{x+dx} 200" stroke="#f4e0b8" stroke-width="16" stroke-linecap="round"/>' for x,dx in [(330,-160),(400,0),(470,160)])+txt(400,170,'RA·TA·TA·TA',58,'#fff',900)
I[1392]=svg(b,d)

# 1449 Ref:rain: an umbrella turned up like a cup catching rain, a lone figure without it, cool blue night
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=rain(110,1449,'#c8d8ff',.45)+'<rect y="620" width="800" height="180" fill="#1a2238"/>'
b+='<path d="M200 640 Q300 520 400 640Z" fill="#5a7ad8"/><path d="M300 640 L300 700 Q300 720 280 720" stroke="#2a2a2a" stroke-width="6" fill="none"/>'+figure(560,640,280,'#05070f')+'<ellipse cx="560" cy="650" rx="80" ry="10" fill="#8aa8d8" opacity=".3"/>'
I[1449]=svg(b,d)

# 1851 Shout Baby: a megaphone-shaped speech bubble shouting out in yellow and green, emotion bursting
d,b=bg([(0,'#3ac86a'),(1,'#d8ff8a')])
b+=rays(500,380,20,'#fff',.25,10)+'<path d="M180 340 L320 300 L320 460 L180 420Z" fill="#ffd02a" stroke="#1a1a1a" stroke-width="8"/><path d="M320 300 L560 180 L560 580 L320 460Z" fill="#ffd02a" stroke="#1a1a1a" stroke-width="8"/>'
b+=''.join(f'<path d="M600 {380+dy} L{720} {380+dy*2}" stroke="#1a1a1a" stroke-width="10" stroke-linecap="round"/>' for dy in (-80,0,80))
I[1851]=svg(b,d)

# 174 限界突破×サバイバー: a figure smashing through a wall of red bricks in a burst of fire and light, rock poses
d,b=bg([(0,'#3a0a0a'),(1,'#0a0a0a')])
for r2 in range(10):
    for c in range(9):
        x=c*90-(r2%2)*45;y=r2*80
        if math.hypot(x+45-400,y+40-420)>200: b+=f'<rect x="{x}" y="{y}" width="86" height="76" fill="#8a2a1a" stroke="#4a1a10" stroke-width="4"/>'
b+=glow(400,420,220,'#ffb02a',.6)+rays(400,420,24,'#ffe86a',.3,8)+figure(400,600,330,'#000',pose='up')
I[174]=svg(b,d)

# 416 くちびるNetwork: glossy pink lips with sparkly telephone lines connecting little heart nodes, mid-80s pop
d,b=bg([(0,'#ff8ac8'),(1,'#ffe0f0')])
N=[(120,140),(680,160),(140,660),(660,640),(400,120)]
b+=''.join(f'<path d="M400 420 L{x} {y}" stroke="#fff" stroke-width="4" stroke-dasharray="10 8"/>'+heart(x,y,30,'#ff2a8a') for x,y in N)
b+='<path d="M240 420 Q300 340 360 370 Q400 350 440 370 Q500 340 560 420 Q480 520 400 520 Q320 520 240 420Z" fill="#e8104a"/><path d="M240 420 Q400 460 560 420" stroke="#8a0a2a" stroke-width="6" fill="none"/><ellipse cx="460" cy="470" rx="30" ry="10" fill="#fff" opacity=".5"/>'
I[416]=svg(b,d)

# 536 たしかなこと: a pair of footprints on a quiet beach at dawn leading to a bench, gentle waves
d,b=bg([(0,'#a8c8e8'),(.6,'#f8e0c8'),(1,'#f0d8b8')])
b+=hinomaru_sun(400,360,70,'#fff4d8',.8)+'<rect y="400" width="800" height="120" fill="#8ab0d8"/><path d="M-10 520 Q400 500 810 520 L810 810 L-10 810Z" fill="#f0dcb8"/>'
b+=''.join(f'<ellipse cx="{300+(k%2)*30+k*12}" cy="{780-k*40}" rx="9" ry="16" fill="#c8b090"/>' for k in range(7))+'<rect x="440" y="520" width="180" height="16" fill="#8a6a4a"/><rect x="450" y="536" width="10" height="40" fill="#8a6a4a"/><rect x="600" y="536" width="10" height="40" fill="#8a6a4a"/><rect x="440" y="480" width="180" height="12" fill="#8a6a4a"/>'
I[536]=svg(b,d)

# 829 Gravity: an apple and a figure both falling slowly through a dark void, curved space lines
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=''.join(f'<path d="M0 {200+k*80} Q400 {340+k*80} 800 {200+k*80}" stroke="#5a6aa8" stroke-width="3" fill="none" opacity=".5"/>' for k in range(6))
b+='<g transform="rotate(170 300 380)">'+figure(300,480,220,'#c8d0e8')+'</g>'+'<circle cx="540" cy="300" r="40" fill="#e8302a"/><path d="M540 260 L548 236" stroke="#5a3a1a" stroke-width="5"/><path d="M548 246 Q570 230 580 248 Q560 254 548 246Z" fill="#4ac84a"/>'
I[829]=svg(b,d)

# 897 FOREVER YOURS: two wedding rings interlocked on a soft white satin cloth, warm light
d,b=bg([(0,'#fff8f0'),(1,'#f0e0d0')])
b+=glow(400,400,240,'#fff',.7)+''.join(f'<path d="M0 {500+k*60} Q400 {460+k*60} 800 {520+k*60}" stroke="#e8dcd0" stroke-width="20" fill="none"/>' for k in range(5))
b+=ring(350,420,90,'#e8b830',24)+ring(450,420,90,'#d8dce8',24)+'<path d="M420 340 L440 320 L460 340 L440 370Z" fill="#fff"/>'+sparkle(452,330,18,'#fff')
I[897]=svg(b,d)

# 950 好きになってく愛してく: a heart-shaped hot-air balloon slowly rising over a pastel town at dawn
d,b=bg([(0,'#ffc8d8'),(1,'#fff2e0')])
b+=skyline(700,'#e8b8c8',950,40,140,'#fff6d8',30)+'<rect y="700" width="800" height="100" fill="#d8a8b8"/>'+cloud(200,200,1.2)+cloud(620,300,1)
b+=heart(400,300,140,'#ff4a7a')+'<path d="M340 420 L370 520 M460 420 L430 520" stroke="#8a5a3a" stroke-width="4"/><rect x="360" y="520" width="80" height="50" fill="#8a5a3a"/>'
I[950]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
