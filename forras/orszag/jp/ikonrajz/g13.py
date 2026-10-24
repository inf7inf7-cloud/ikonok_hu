import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 13. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def lips(x,y,s,c1='#e8102a',c2='#c80a20'): return f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="{c1}"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="{c2}"/></g>'

# 1221 Find The Answer: a key of light fitting into a keyhole shaped like a question mark in a dark wall
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
b+='<path d="M330 260 Q330 180 400 180 Q480 180 480 260 Q480 320 420 340 L420 420 L380 420 L380 320 Q440 310 440 260 Q440 220 400 220 Q370 220 370 260Z" fill="#ffe8a0"/><circle cx="400" cy="480" r="26" fill="#ffe8a0"/>'
b+=glow(400,320,160,'#ffe8a0',.5)
b+='<g transform="rotate(-30 560 600)"><circle cx="640" cy="600" r="50" fill="none" stroke="#ffd27a" stroke-width="18"/><rect x="420" y="590" width="180" height="20" fill="#ffd27a"/><rect x="440" y="610" width="20" height="36" fill="#ffd27a"/><rect x="480" y="610" width="20" height="26" fill="#ffd27a"/></g>'+glow(560,620,90,'#ffd27a',.4)
I[1221]=svg(b,d)

# 1531 優しい彗星: a gentle comet arcing over a sleeping town, its tail scattering soft lights onto the rooftops
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=starsf(60,1531,500,'#fff')
b+='<path d="M560 180 Q380 220 120 400" stroke="#bfe8ff" stroke-width="40" fill="none" opacity=".2" stroke-linecap="round"/><path d="M560 180 Q380 220 140 380" stroke="#e8f8ff" stroke-width="10" fill="none" opacity=".6" stroke-linecap="round"/>'+glow(560,180,70,'#fff',.8)+'<circle cx="560" cy="180" r="22" fill="#fff"/>'
b+='<path d="M-10 800 L-10 600 L60 560 L120 600 L120 560 L200 520 L280 560 L280 600 L360 560 L440 600 L440 540 L520 500 L600 540 L600 600 L680 560 L810 600 L810 800Z" fill="#0a0e24"/>'
r=R(1531)
for _ in range(16): b+=f'<rect x="{r.uniform(20,780):.0f}" y="{r.uniform(600,740):.0f}" width="14" height="18" fill="#ffd27a"/>'
I[1531]=svg(b,d)

# 739 Youthful Days: a bicycle with two riders racing down a sunny hill road, school bags flying
d,b=bg([(0,'#3aa8f8'),(1,'#d0f0ff')])
b+=cloud(600,160,1.4)+'<rect y="380" width="800" height="100" fill="#1a90d8"/><path d="M-10 480 L810 380 L810 810 L-10 810Z" fill="#6ac84a"/><path d="M-10 720 L810 520 L810 600 L-10 800Z" fill="#9a9aa4"/>'
b+='<g transform="rotate(-12 400 620)"><circle cx="300" cy="660" r="56" fill="none" stroke="#1a1a24" stroke-width="10"/><circle cx="500" cy="660" r="56" fill="none" stroke="#1a1a24" stroke-width="10"/><path d="M300 660 L370 580 L470 580 L500 660 M370 580 L400 660 L470 580" stroke="#2a8ae8" stroke-width="12" fill="none"/></g>'
b+=figure(420,600,180,'#1a1a2a')+figure(350,620,170,'#1a1a2a',pose='up',hair='#1a1a2a')
b+='<rect x="240" y="440" width="50" height="40" rx="6" fill="#5a3a2a" transform="rotate(-30 265 460)"/>'
I[739]=svg(b,d)

# 1301 真夏のSounds good !: a giant beach ball bouncing over a crowded summer beach, sun blazing overhead
d,b=bg([(0,'#1ab0f8'),(1,'#a8e8ff')])
b+=rays(640,120,18,'#fff',.35,8)+hinomaru_sun(640,120,70,'#fffbd8',1)
b+='<rect y="480" width="800" height="80" fill="#0a90d8"/><path d="M-10 560 Q400 530 810 560 L810 810 L-10 810Z" fill="#f8e0a0"/>'
b+='<circle cx="380" cy="380" r="150" fill="#fff"/>'+''.join(f'<path d="M380 380 L{380+150*math.cos(math.radians(a)):.0f} {380+150*math.sin(math.radians(a)):.0f} A150 150 0 0 1 {380+150*math.cos(math.radians(a+60)):.0f} {380+150*math.sin(math.radians(a+60)):.0f}Z" fill="{c}"/>' for a,c in [(-90,'#e8302a'),(30,'#ffd02a'),(150,'#2a8ae8')])+'<circle cx="380" cy="380" r="20" fill="#fff"/>'
for x,c in [(120,'#ff5a8a'),(680,'#3ac87a')]: b+=f'<path d="M{x} 640 L{x} 520" stroke="#fff" stroke-width="5"/><path d="M{x-80} 540 Q{x} 460 {x+80} 540Z" fill="{c}"/>'
I[1301]=svg(b,d)

# 1516 お勉強しといてよ: a desk lamp lighting an open textbook scribbled with doodles at midnight, a half-eaten gyoza on a plate
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<polygon points="480,240 220,700 700,700" fill="#fff6d8" opacity=".14"/><rect y="640" width="800" height="160" fill="#3a2a1a"/>'
b+='<path d="M600 640 L600 400 L480 240" stroke="#2a2a34" stroke-width="16" fill="none"/><path d="M420 220 L540 220 L520 280 L440 280Z" fill="#2a2a34" transform="rotate(30 480 250)"/>'+glow(470,280,50,'#fff6d8',.8)
b+='<path d="M180 640 L380 600 L400 610 L420 600 L620 640 L620 660 L180 660Z" fill="#fbf8f0"/><path d="M220 630 L360 606 M440 606 L580 630" stroke="#a8a8c8" stroke-width="4"/>'
b+='<path d="M240 618 q20 -20 40 0 q20 20 40 0" stroke="#e8302a" stroke-width="4" fill="none"/><circle cx="500" cy="620" r="10" fill="none" stroke="#3a8ae8" stroke-width="4"/>'
b+='<ellipse cx="160" cy="700" rx="80" ry="20" fill="#fff"/><path d="M110 690 Q140 660 170 690 Z M160 690 Q190 660 210 690Z" fill="#e8c890"/>'
I[1516]=svg(b,d)

# 123 渚のシンドバッド: a sailor's striped shirt flapping on a laundry line over a sunny shore, a little sailboat behind
d,b=bg([(0,'#2ab0f8'),(1,'#bfeaff')])
b+='<rect y="440" width="800" height="140" fill="#1a90d8"/><path d="M-10 580 Q400 550 810 580 L810 810 L-10 810Z" fill="#f8e0a0"/>'
b+='<path d="M560 440 L560 300 L640 420Z M560 300 L500 420 L560 420Z" fill="#fff"/><path d="M520 440 L620 440 L610 460 L530 460Z" fill="#e8302a"/>'
b+='<path d="M60 160 Q400 220 740 160" stroke="#5a3a1a" stroke-width="4" fill="none"/>'
b+='<path d="M260 190 L300 180 L330 200 L360 190 L400 200 L440 260 L410 280 L400 260 L400 400 L280 400 L280 260 L250 280 L230 250Z" fill="#fff"/>'+''.join(f'<rect x="280" y="{220+k*36}" width="120" height="14" fill="#1a3a8a"/>' for k in range(5))
b+='<path d="M520 200 L600 210 L600 300 L520 300Z" fill="#e8302a"/>'
I[123]=svg(b,d)

# 432 星屑のステージ: a microphone stand on an empty stage, stardust falling like confetti in the spotlight
d,b=bg([(0,'#0a0a2a'),(1,'#1a1a3a')])
b+='<polygon points="400,-20 200,700 600,700" fill="#fff6d8" opacity=".14"/><ellipse cx="400" cy="680" rx="230" ry="40" fill="#fff6d8" opacity=".2"/><rect y="680" width="800" height="120" fill="#2a1a3a"/>'
r=R(432)
for _ in range(50): x=r.uniform(220,580);y=r.uniform(40,660);b+=sparkle(x,y,r.uniform(5,14),'#fff6d8')
b+='<rect x="396" y="360" width="8" height="320" fill="#c8c8d0"/><path d="M360 680 L440 680 L400 660Z" fill="#c8c8d0"/><ellipse cx="400" cy="340" rx="22" ry="34" fill="#3a3a44"/>'
I[432]=svg(b,d)

# 544 MUGO・ん・・・色っぽい: a red manicured finger pressed to a pair of lips in a silent shush, smoky purple light
d,b=bg([(0,'#3a1a4a'),(1,'#1a0a2a')])
b+=glow(400,420,240,'#c85ab8',.35)+lips(400,440,1.6)
b+='<rect x="380" y="200" width="44" height="300" rx="22" fill="#e8c0a0"/><rect x="384" y="196" width="36" height="46" rx="18" fill="#e8102a"/>'
I[544]=svg(b,d)

# 545 黄砂に吹かれて: a lone figure in a long coat bracing against a wind full of yellow sand under a hazy sun
d,b=bg([(0,'#d8b060'),(1,'#a87a3a')])
b+=hinomaru_sun(560,240,80,'#fff4c8',.5)
r=R(545)
for _ in range(180): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<path d="M{x:.0f} {y:.0f} l{r.uniform(20,60):.0f} -6" stroke="#ffe8a0" stroke-width="3" opacity=".5"/>'
b+='<path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#8a5a2a"/>'
b+='<g transform="rotate(-10 340 640)">'+figure(340,650,260,'#3a2414')+'<path d="M330 450 Q280 520 220 560 Q300 560 350 520Z" fill="#3a2414"/></g>'
I[545]=svg(b,d)

# 594 Rusty Nail: a rusty nail driven through a blood-red rose against a cracked concrete wall
d,b=bg([(0,'#5a5a5a'),(1,'#3a3a3a')])
b+=bolt([(100,0),(160,200),(120,240),(200,420)],'#2a2a2a',6,1)+bolt([(700,120),(640,300),(680,340),(620,520)],'#2a2a2a',6,1)
b+='<path d="M400 720 Q404 600 400 440" stroke="#2a4a2a" stroke-width="10" fill="none"/>'+rose(400,420,1.4)
b+='<path d="M220 380 L560 460" stroke="#8a4a2a" stroke-width="18" stroke-linecap="round"/><ellipse cx="220" cy="380" rx="14" ry="34" fill="#6a3a1a" transform="rotate(14 220 380)"/>'+''.join(f'<circle cx="{260+k*60}" cy="{392+k*14}" r="5" fill="#c8601a"/>' for k in range(5))
I[594]=svg(b,d)

# 701 永遠: an infinity symbol drawn in light over a calm sea at twilight, its reflection doubling it
d,b=bg([(0,'#3a3a7a'),(.55,'#c88aa8'),(1,'#ffd0b0')])
b+='<rect y="460" width="800" height="340" fill="#4a4a8a"/>'
inf='<path d="M400 {y} C340 {a} 220 {a} 220 {y} C220 {b} 340 {b} 400 {y} C460 {a} 580 {a} 580 {y} C580 {b} 460 {b} 400 {y}Z" fill="none" stroke="{c}" stroke-width="{w}" opacity="{o}"/>'
b+=glow(400,300,220,'#fff4d8',.4)+inf.format(y=300,a=200,b=400,c='#fff4d8',w=16,o=1)+inf.format(y=620,a=700,b=540,c='#fff4d8',w=12,o=.35)
I[701]=svg(b,d)

# 861 New World: a doorway in the sky opening onto a vivid new planet with rings, a figure stepping through
d,b=bg([(0,'#1a0a3a'),(1,'#3a1a5a')])
b+=starsf(60,861,800,'#e8d8ff')
b+='<rect x="280" y="180" width="240" height="420" fill="#ffb07a"/><circle cx="400" cy="380" r="90" fill="#5ac8a8"/><ellipse cx="400" cy="380" rx="150" ry="30" fill="none" stroke="#fff4d8" stroke-width="10" transform="rotate(-15 400 380)"/>'
b+='<rect x="280" y="180" width="240" height="420" fill="none" stroke="#f4e8ff" stroke-width="10"/><path d="M180 700 L280 600 L520 600 L620 700Z" fill="#ffb07a" opacity=".3"/>'+figure(400,620,180,'#0a0414')
I[861]=svg(b,d)

# 1083 出会いのかけら: two jigsaw puzzle pieces fitting together in mid-air above a city crossing at sunset
d,b=bg([(0,'#ff8a6a'),(1,'#ffd0a0')])
b+=skyline(640,'#8a4a5a',1083,80,300,'#ffe8c0',60)+'<rect y="640" width="800" height="160" fill="#6a3a4a"/>'
pz='<path d="M{x} {y} h60 a30 30 0 1 1 60 0 h60 v60 a30 30 0 1 0 0 60 v60 h-180Z" fill="{c}" transform="rotate({a} {cx} {cy})"/>'
b+=pz.format(x=200,y=260,c='#3a8ae8',a=-8,cx=290,cy=350)+'<path d="M400 260 h180 v180 h-180 v-60 a30 30 0 1 1 0 -60Z" fill="#ffd02a" transform="rotate(6 490 350)"/>'+sparkle(390,330,30,'#fff')
I[1083]=svg(b,d)

# 1222 Breathless: a figure sprinting through a tunnel of light, glowing streaks rushing past
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
for k in range(18): a=k*20;b+=f'<path d="M400 400 L{400+600*math.cos(math.radians(a)):.0f} {400+600*math.sin(math.radians(a)):.0f}" stroke="{["#5ae8ff","#fff","#a87aff"][k%3]}" stroke-width="{4+k%3*3}" opacity=".5"/>'
b+=glow(400,400,120,'#fff',.8)+'<g>'+figure(400,560,260,'#000',pose='wave')+'</g>'
I[1222]=svg(b,d)

# 1365 不協和音: a single grey figure standing still while a wall of marching grey figures moves around it, one red note between
d,b=bg([(0,'#3a3a44'),(1,'#1a1a24')])
for row,(y,h,n) in enumerate([(380,120,11),(520,160,9),(700,220,7)]):
    for k in range(n):
        x=40+k*(720/(n-1))
        if row==2 and k==3: continue
        b+=f'<g transform="translate({x} 0) scale(-1 1) translate({-x} 0)">'+figure(x,y,h,'#5a5a64')+'</g>'
b+=figure(400,700,240,'#0a0a10')+note(470,420,30,'#e8102a')
I[1365]=svg(b,d)

# 404 Woman "Wの悲劇"より: a stage dressing-room mirror ringed with bulbs, a single white mask and a rose on the counter
d,b=bg([(0,'#2a1a1a'),(1,'#1a0a0a')])
b+='<rect x="180" y="100" width="440" height="460" fill="#3a3044"/><rect x="200" y="120" width="400" height="420" fill="#5a5070"/>'
for k in range(7): b+=f'<circle cx="{200+k*66}" cy="110" r="16" fill="#fff6d8"/><circle cx="190" cy="{120+k*66}" r="16" fill="#fff6d8"/><circle cx="610" cy="{120+k*66}" r="16" fill="#fff6d8"/>'
b+=glow(400,330,240,'#fff6d8',.25)+'<rect y="560" width="800" height="240" fill="#4a2a1a"/>'
b+='<path d="M300 620 Q300 560 360 560 Q420 560 420 620 Q420 680 360 700 Q300 680 300 620Z" fill="#fff"/><ellipse cx="340" cy="610" rx="12" ry="8" fill="#1a1a1a"/><ellipse cx="380" cy="610" rx="12" ry="8" fill="#1a1a1a"/>'
b+='<path d="M460 680 L600 640" stroke="#2a5a2a" stroke-width="6"/>'+rose(610,636,.55)
I[404]=svg(b,d)

# 862 HEAVEN'S DRIVE: a sleek car speeding on a highway that spirals up into the clouds and starlight
d,b=bg([(0,'#1a0a4a'),(.6,'#5a3a8a'),(1,'#ff9aa8')])
b+=starsf(50,862,400,'#fff')+cloud(160,520,2.0,'#ffc8d8')+cloud(640,580,1.8,'#ffc8d8')
b+='<path d="M120 800 Q300 600 560 600 Q720 580 640 440 Q560 320 400 320 Q280 300 300 160" stroke="#2a2a3a" stroke-width="80" fill="none"/><path d="M120 800 Q300 600 560 600 Q720 580 640 440 Q560 320 400 320 Q280 300 300 160" stroke="#ffd02a" stroke-width="4" fill="none" stroke-dasharray="20 20"/>'
b+='<g transform="rotate(-50 620 480)"><rect x="580" y="460" width="90" height="40" rx="14" fill="#e8102a"/></g>'+glow(660,450,40,'#fff4c8',.8)
I[862]=svg(b,d)

# 1132 zero: a heavy armoured knight's helmet abandoned in the snow, a single flower sprouting from its visor
d,b=bg([(0,'#8a9ab8'),(1,'#d0d8e8')])
b+=snow(60,1132)+'<rect y="560" width="800" height="240" fill="#f0f4fa"/>'
b+='<path d="M260 600 Q260 340 400 320 Q540 340 540 600Z" fill="#7a7a8a"/><path d="M280 460 L520 460" stroke="#3a3a44" stroke-width="20"/><path d="M400 330 L400 600" stroke="#5a5a6a" stroke-width="10"/>'
b+='<path d="M440 470 Q460 380 500 300" stroke="#4a8a3a" stroke-width="6" fill="none"/>'+flower(500,290,40,6,'#ff7aa8','#ffd82a',0,.7)
I[1132]=svg(b,d)

# 1133 Only Lonely Glory: a single silver trophy glinting on a dusty attic shelf, a sunbeam picking it out of the shadows
d,b=bg([(0,'#2a2014'),(1,'#1a140a')])
b+='<polygon points="600,0 680,0 480,800 300,800" fill="#ffe8b0" opacity=".2"/><rect y="560" width="800" height="30" fill="#5a3a1a"/>'
r=R(1133)
for _ in range(30): b+=f'<circle cx="{r.uniform(320,620):.0f}" cy="{r.uniform(0,800):.0f}" r="2" fill="#fff4c8" opacity=".7"/>'
b+='<path d="M330 300 L470 300 L460 400 Q440 450 400 460 Q360 450 340 400Z" fill="#c8c8d8"/><path d="M330 320 Q280 320 290 370 Q300 400 340 400 M470 320 Q520 320 510 370 Q500 400 460 400" stroke="#c8c8d8" stroke-width="12" fill="none"/><rect x="390" y="460" width="20" height="50" fill="#c8c8d8"/><rect x="350" y="510" width="100" height="50" fill="#8a8a94"/>'+sparkle(360,340,30,'#fff')
I[1133]=svg(b,d)

# 1550 愛して愛して愛して: three identical red hearts on strings dangling like a marionette from unseen hands
d,b=bg([(0,'#1a0410'),(1,'#3a0a20')])
for x,y in [(220,420),(400,520),(580,420)]: b+=f'<path d="M{x} 0 L{x} {y-70}" stroke="#f4e0e8" stroke-width="3"/>'+glow(x,y,90,'#ff2a5a',.4)+heart(x,y,80,'#e8102a')
b+='<path d="M120 60 L680 60" stroke="#5a3a3a" stroke-width="16"/>'
I[1550]=svg(b,d)

# 1599 オドロウゼ!: a rainbow of paper fans spinning above a festival dance floor, confetti everywhere
d,b=bg([(0,'#ff4a8a'),(1,'#ffa84a')])
b+=rays(400,400,24,'#fff',.25,8)
for k,(x,y,c) in enumerate([(200,260,'#2a8ae8'),(400,200,'#ffe02a'),(600,260,'#3ac85a')]):
    b+=f'<g transform="translate({x} {y}) rotate({k*30-30})">'+''.join(f'<path d="M0 40 L{120*math.cos(math.radians(a)):.0f} {120*math.sin(math.radians(a)):.0f} A120 120 0 0 1 {120*math.cos(math.radians(a+20)):.0f} {120*math.sin(math.radians(a+20)):.0f}Z" fill="{c if j%2 else "#fff"}"/>' for j,a in enumerate(range(-170,-10,20)))+'</g>'
for k in range(9): x=50+k*88;b+=figure(x,800,220,'#5a0a2a',pose='up' if k%2 else 'wave')
r=R(1599)
for _ in range(30): x,y=r.uniform(0,800),r.uniform(0,560);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="12" height="20" fill="{r.choice(["#fff","#ffe05a","#5ab8ff"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[1599]=svg(b,d)

# 1613 HEART: a crown resting on a velvet cushion, a heart-shaped ruby glowing at its centre
d,b=bg([(0,'#2a0a3a'),(1,'#1a0420')])
b+=glow(400,420,240,'#ff3a8a',.3)
b+='<path d="M180 600 Q180 540 400 530 Q620 540 620 600 Q620 660 400 670 Q180 660 180 600Z" fill="#8a0a3a"/><circle cx="190" cy="600" r="14" fill="#d8b040"/><circle cx="610" cy="600" r="14" fill="#d8b040"/>'
b+='<path d="M260 540 L240 320 L330 420 L400 280 L470 420 L560 320 L540 540Z" fill="#ffd02a" stroke="#c8901a" stroke-width="6"/>'+heart(400,450,50,'#e8102a')+sparkle(420,420,20,'#fff')
I[1613]=svg(b,d)

# 1742 ズルいよ ズルいね: a heart-shaped lollipop held behind someone's back, a pink sweet wrapper on the ground
d,b=bg([(0,'#ffd0e8'),(1,'#ffe8f4')])
b+='<rect y="600" width="800" height="200" fill="#c8e8c8"/>'+figure(400,640,420,'#ff8ab8',hair='#c85a8a')
b+='<rect x="440" y="400" width="10" height="180" fill="#fff"/>'+heart(445,370,60,'#ff2a6a')+'<path d="M420 360 Q445 330 470 360" stroke="#fff" stroke-width="6" fill="none"/>'
b+='<path d="M180 680 L240 660 L260 690 L200 710Z" fill="#ff8ab8"/><path d="M180 680 L160 670 L170 700Z M260 690 L280 680 L274 708Z" fill="#ff5a9a"/>'
I[1742]=svg(b,d)

# 1861 Y: a crossroads in the shape of a Y seen from above in autumn, two sets of footprints going separate ways
d,b=bg([(0,'#d8a050'),(1,'#a86a2a')])
r=R(1861)
for _ in range(40): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="18" ry="10" fill="{r.choice(["#e8601a","#c8401a","#ffb03a","#8a3a1a"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+='<path d="M340 810 L340 460 L120 -10 L240 -10 L400 340 L560 -10 L680 -10 L460 460 L460 810Z" fill="#c8b890"/>'
for k in range(5): b+=f'<ellipse cx="{390-k*36}" cy="{400-k*80}" rx="10" ry="16" fill="#5a3a1a"/><ellipse cx="{410+k*36}" cy="{400-k*80}" rx="10" ry="16" fill="#5a3a1a"/>'
for k in range(4): b+=f'<ellipse cx="{390+(k%2)*20}" cy="{760-k*80}" rx="10" ry="16" fill="#5a3a1a"/>'
I[1861]=svg(b,d)

# 182 ふれあい: two hands touching fingertips through a summer screen door, cicada song in the warm evening
d,b=bg([(0,'#ff9a6a'),(1,'#ffd0a0')])
b+='<rect x="140" y="80" width="520" height="640" fill="#8a6a4a"/><rect x="170" y="110" width="460" height="580" fill="#4a6a5a"/>'
b+=''.join(f'<path d="M{170+k*12} 110 L{170+k*12} 690" stroke="#3a5a3a" stroke-width="1" opacity=".35"/>' for k in range(39))+''.join(f'<path d="M170 {110+k*12} L630 {110+k*12}" stroke="#3a5a3a" stroke-width="1" opacity=".35"/>' for k in range(49))
b+='<g fill="#e8b890"><rect x="160" y="380" width="230" height="44" rx="22"/><rect x="410" y="380" width="230" height="44" rx="22" opacity=".8"/></g>'+glow(400,400,40,'#fff',.7)
I[182]=svg(b,d)

# 1413 Stand Out Fit In: one red square block refusing to fit into a neat grid of grey round holes
d,b=bg([(0,'#d8d8e0'),(1,'#b8b8c4')])
for i in range(5):
    for j in range(5):
        if (i,j)==(2,2): continue
        b+=f'<circle cx="{160+i*120}" cy="{160+j*120}" r="44" fill="#6a6a74"/>'
b+='<circle cx="400" cy="400" r="44" fill="#4a4a54"/><rect x="340" y="300" width="120" height="120" fill="#e8102a" transform="rotate(12 400 360)"/>'
I[1413]=svg(b,d)

# 1559 不可幸力: a giant hand-cranked music box gear turning a whole city, tiny people being carried on its teeth
d,b=bg([(0,'#1a2a3a'),(1,'#0a1420')])
b+='<g transform="rotate(10 400 520)">'+''.join(f'<rect x="380" y="200" width="40" height="70" fill="#c89a40" transform="rotate({a} 400 520)"/>' for a in range(0,360,30))+'</g><circle cx="400" cy="520" r="270" fill="#c89a40"/><circle cx="400" cy="520" r="200" fill="#1a2a3a"/>'
b+=skyline(520,'#2a3a4a',1559,40,140,'#ffd27a',30).replace('<rect','<rect clip-path="url(#gc)"')
d+='<clipPath id="gc"><circle cx="400" cy="520" r="200"/></clipPath>'
b+='<circle cx="400" cy="520" r="50" fill="#c89a40"/>'+''.join(figure(400+290*math.cos(math.radians(a)),520+290*math.sin(math.radians(a))-10,60,'#fff') for a in (-120,-90,-60))
I[1559]=svg(b,d)

# 1579 コロンブス: an old wooden sailing ship on a sea of swirling map lines, heading for an unknown horizon
d,b=bg([(0,'#e8d8b0'),(1,'#c8b088')])
for k in range(10): b+=f'<path d="M-10 {460+k*36} Q200 {440+k*36} 400 {460+k*36} T810 {460+k*36}" stroke="#8a6a3a" stroke-width="3" fill="none"/>'
b+='<path d="M220 480 L580 480 L540 560 L260 560Z" fill="#6a3a1a"/><rect x="396" y="200" width="10" height="290" fill="#3a2414"/><path d="M406 220 Q500 280 410 360Z M406 370 Q520 410 410 460Z M396 230 Q300 300 392 380Z" fill="#fbf8f0"/>'
b+='<path d="M406 200 L460 210 L406 222Z" fill="#e8102a"/><circle cx="660" cy="160" r="60" fill="none" stroke="#8a6a3a" stroke-width="4"/><path d="M660 100 L670 160 L660 220 L650 160Z" fill="#8a6a3a"/>'
I[1579]=svg(b,d)

# 360 風立ちぬ: a white parasol tumbling across a green hillside in a sudden gust, the wind visible in the bending grass
d,b=bg([(0,'#7ac8f8'),(1,'#e0f4ff')])
b+=cloud(600,140,1.4)+'<path d="M-10 460 Q400 380 810 460 L810 810 L-10 810Z" fill="#7ac84a"/>'
for k in range(30): x=k*28;b+=f'<path d="M{x} 800 Q{x+20} 700 {x+50} 660" stroke="#5aa83a" stroke-width="5" fill="none"/>'
b+='<g transform="rotate(30 360 300)"><path d="M200 300 Q360 160 520 300Z" fill="#fff"/><path d="M200 300 Q240 316 280 300 Q320 316 360 300 Q400 316 440 300 Q480 316 520 300" fill="none" stroke="#e8e8f0" stroke-width="5"/><path d="M360 300 L360 460 Q360 480 380 480" stroke="#8a6a3a" stroke-width="8" fill="none"/></g>'
for y in (200,420): b+=f'<path d="M60 {y} Q180 {y-30} 300 {y}" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>'
I[360]=svg(b,d)

# 968 冷たい花: a rose encased in a block of ice, frost creeping over its petals in a cold blue light
d,b=bg([(0,'#1a2a4a'),(1,'#0a1428')])
b+=glow(400,400,220,'#8ad0ff',.35)
b+='<path d="M240 220 L560 200 L590 560 L220 590Z" fill="#bfe8ff" opacity=".35" stroke="#e8f8ff" stroke-width="5"/>'
b+='<path d="M400 560 Q404 480 400 420" stroke="#3a6a5a" stroke-width="8" fill="none"/>'+rose(400,400,1.1)
b+='<path d="M240 220 L560 200 L590 560 L220 590Z" fill="#e8f8ff" opacity=".25"/>'+''.join(f'<path d="M{x} {y} l12 12 M{x+12} {y} l-12 12" stroke="#fff" stroke-width="3"/>' for x,y in [(280,260),(500,300),(320,500),(540,480)])
I[968]=svg(b,d)

# 1223 SUNRISE日本: the rising sun bursting over a wave-washed Japanese shore, a flock of cranes crossing it
d,b=bg([(0,'#ff7a3a'),(.5,'#ffc85a'),(1,'#ffe8b0')])
b+=rays(400,520,24,'#fff',.3,8)+hinomaru_sun(400,520,160,'#e8102a',1)
b+='<rect y="520" width="800" height="280" fill="#1a5aa8"/>'+''.join(f'<path d="M{x} {y} q30 -24 60 0" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/>' for x in range(-30,800,60) for y in range(560,800,40))
for k,(x,y,s) in enumerate([(200,260,1),(270,230,.8),(340,210,.7),(560,250,.9),(620,220,.7)]): b+=f'<path d="M{x-40*s:.0f} {y} Q{x-16*s:.0f} {y-30*s:.0f} {x} {y} Q{x+16*s:.0f} {y-30*s:.0f} {x+40*s:.0f} {y}" stroke="#1a1a24" stroke-width="{7*s:.0f}" fill="none" stroke-linecap="round"/>'
I[1223]=svg(b,d)

# 1341 Monopoly: a board-game dice tumbling across a city made of game houses, a top hat and car token watching
d,b=bg([(0,'#c8e8d0'),(1,'#a8d8b8')])
for i in range(8):
    for j in range(3): b+=f'<path d="M{60+i*90} {500+j*90} L{60+i*90} {460+j*90} L{90+i*90} {430+j*90} L{120+i*90} {460+j*90} L{120+i*90} {500+j*90}Z" fill="{["#3ac85a","#e8102a"][(i+j)%3==0]}"/>'
for x,y,a in [(320,280,-15),(480,250,20)]:
    b+=f'<g transform="rotate({a} {x} {y})"><rect x="{x-70}" y="{y-70}" width="140" height="140" rx="20" fill="#fff" stroke="#c8c8d0" stroke-width="4"/>'+''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="13" fill="#1a1a1a"/>' for dx,dy in ([(-35,-35),(35,35),(0,0)] if x<400 else [(-35,-35),(35,-35),(-35,35),(35,35)]))+'</g>'
I[1341]=svg(b,d)

# 1414 Cry out: a megaphone-shaped mountain peak roaring sound waves across a stormy sky, a figure on top
d,b=bg([(0,'#2a2a4a'),(1,'#5a4a6a')])
b+='<path d="M-10 800 L-10 600 L300 340 L360 380 L560 600 L810 520 L810 800Z" fill="#1a1a2a"/>'
for k in range(5): b+=f'<path d="M{400+k*60} {200-k*40} Q{460+k*80} 340 {400+k*60} {480+k*40}" stroke="#ffd27a" stroke-width="{10-k}" fill="none" opacity="{.8-k*.14:.2f}"/>'
b+=figure(320,350,140,'#000',pose='up')+bolt([(120,60),(160,180),(130,190),(180,300)],'#fff',6,1)
I[1414]=svg(b,d)

# 1532 アンコール: a single light bulb still glowing in an emptied concert hall, a hand reaching to switch it off
d,b=bg([(0,'#0a0a14'),(1,'#1a1424')])
for k in range(5): b+=f'<path d="M-10 {560+k*50} Q400 {520+k*50} 810 {560+k*50}" stroke="#3a2a3a" stroke-width="30" fill="none"/>'
b+='<path d="M400 0 L400 260" stroke="#3a3a44" stroke-width="4"/><path d="M370 260 L430 260 L440 300 Q460 330 450 370 Q430 410 400 410 Q370 410 350 370 Q340 330 360 300Z" fill="#fff4c8"/>'+glow(400,350,140,'#ffd27a',.6)
b+='<g fill="#e8b890" opacity=".85"><rect x="560" y="380" width="200" height="50" rx="25" transform="rotate(-20 660 405)"/><rect x="530" y="360" width="60" height="26" rx="13" transform="rotate(-30 560 373)"/></g>'
I[1532]=svg(b,d)

# 1600 タペストリー: a woven tapestry of colourful threads showing a sun and a moon, a loose thread trailing down
d,b=bg([(0,'#3a2a1a'),(1,'#1a140a')])
b+='<rect x="140" y="100" width="520" height="560" fill="#e8d8b0"/><rect x="120" y="80" width="560" height="24" rx="12" fill="#8a5a2a"/>'
for k in range(28): b+=f'<path d="M140 {110+k*20} L660 {110+k*20}" stroke="{["#c8a870","#d8c090"][k%2]}" stroke-width="10"/>'
b+='<circle cx="290" cy="300" r="80" fill="#ffa82a"/>'+''.join(f'<path d="M290 300 L{290+120*math.cos(math.radians(a)):.0f} {300+120*math.sin(math.radians(a)):.0f}" stroke="#ffa82a" stroke-width="8"/>' for a in range(0,360,30))
b+='<circle cx="510" cy="420" r="80" fill="#2a3a8a"/><circle cx="540" cy="400" r="70" fill="#e8d8b0"/>'+''.join(f'<rect x="{150+k*40}" y="560" width="30" height="60" fill="{["#e8302a","#3a8ae8","#3ac85a","#ffd02a"][k%4]}"/>' for k in range(13))
b+='<path d="M420 660 Q440 720 400 780" stroke="#e8302a" stroke-width="6" fill="none"/>'
I[1600]=svg(b,d)

# 1107 Someday: a lone figure on a cliff edge watching an aeroplane trail cross a vast sunset sky
d,b=bg([(0,'#3a3a8a'),(.5,'#e88a8a'),(1,'#ffc890')])
b+=hinomaru_sun(400,520,110,'#fff4d0',.8)+'<path d="M120 300 Q400 200 700 140" stroke="#fff" stroke-width="5" fill="none" opacity=".8"/><path d="M700 140 L716 132 L712 146Z" fill="#fff"/>'
b+='<rect y="560" width="800" height="240" fill="#5a4a7a"/><path d="M-10 800 L-10 540 L440 540 L480 800Z" fill="#1a1428"/>'+figure(380,540,200,'#0a0814')
I[1107]=svg(b,d)

# 1415 Deeper Deeper: a diver's light sinking into a bottomless trench, glowing deep-sea creatures around it
d,b=bg([(0,'#0a3a6a'),(.4,'#041a3a'),(1,'#000208')])
b+='<polygon points="400,300 300,800 500,800" fill="#bfe8ff" opacity=".12"/>'+glow(400,300,60,'#fff',.8)+'<circle cx="400" cy="300" r="14" fill="#fff"/>'
b+='<path d="M-10 800 L-10 300 L160 400 L200 800Z M810 800 L810 260 L620 380 L600 800Z" fill="#020610"/>'
r=R(1415)
for _ in range(20): x,y=r.uniform(100,700),r.uniform(400,780);c=r.choice(['#5affd8','#ff5ab8','#5ab8ff']);b+=glow(x,y,14,c,.6,'glow2')+f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="{c}"/>'
b+='<path d="M600 520 Q640 480 680 520 Q660 560 640 600 M620 520 L610 580 M660 520 L670 590" stroke="#ff5ab8" stroke-width="4" fill="none" opacity=".8"/>'+''.join(ring(400+(k%3)*8-8,280-k*30,4+k,'#fff',2,.6) for k in range(6))
I[1415]=svg(b,d)

# 1513 だから僕は音楽を辞めた: an acoustic guitar left leaning against a bench at a seaside station, a stack of unsent letters beside it
d,b=bg([(0,'#a8c0d8'),(1,'#e8eef4')])
b+=cloud(200,140,1.4)+'<rect y="420" width="800" height="120" fill="#5a8ab8"/><rect y="540" width="800" height="260" fill="#b8b8c0"/>'
b+='<rect x="140" y="520" width="440" height="20" fill="#8a5a3a"/><rect x="160" y="540" width="14" height="80" fill="#5a5a64"/><rect x="546" y="540" width="14" height="80" fill="#5a5a64"/>'
b+=guitar(460,440,.8,20,'#c8702a')
for k in range(5): b+=f'<rect x="{220+k*3}" y="{500-k*12}" width="120" height="14" fill="{["#fff","#f4ecd8"][k%2]}" stroke="#d8d0c0"/>'
I[1513]=svg(b,d)

# 1564 まつり: festival lanterns strung across a temple path at night, a taiko drum glowing under them
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a2a')])
b+='<path d="M-10 160 Q400 260 810 160" stroke="#3a2a2a" stroke-width="4" fill="none"/><path d="M-10 300 Q400 400 810 300" stroke="#3a2a2a" stroke-width="4" fill="none"/>'
for k in range(8): x=50+k*100;y1=160+100*math.sin(math.pi*x/800)*.9;y2=300+100*math.sin(math.pi*x/800)*.9;b+=chochin(x,y1+40,40)+chochin(x+50,y2+40,34)
b+='<rect y="620" width="800" height="180" fill="#2a1a1a"/><ellipse cx="400" cy="520" rx="140" ry="110" fill="#8a3a1a"/><ellipse cx="400" cy="520" rx="110" ry="90" fill="#f4e8d0"/><path d="M380 500 Q400 480 420 500 Q420 540 380 540Z" fill="#e8102a"/>'
b+='<path d="M300 640 L340 600 M500 640 L460 600" stroke="#5a3a1a" stroke-width="14"/>'
I[1564]=svg(b,d)

# 1614 koi-wazurai: a schoolboy's notebook margin covered with heart doodles, a pen tapping in daydream
d,b=bg([(0,'#d8ecff'),(1,'#f4f8ff')])
b+='<rect x="120" y="100" width="560" height="620" fill="#fff" transform="rotate(-4 400 400)"/>'+''.join(f'<path d="M140 {170+k*44} L660 {134+k*44}" stroke="#bfd8f0" stroke-width="3"/>' for k in range(12))
r=R(1614)
for _ in range(14): b+=heart(r.uniform(200,600),r.uniform(200,620),r.uniform(16,36),r.choice(['#ff5a8a','#ff8ab0','#e8302a']))
b+='<g transform="rotate(30 560 560)"><rect x="440" y="540" width="260" height="30" fill="#2a3a8a"/><path d="M700 540 L740 555 L700 570Z" fill="#c8c8d0"/></g>'
I[1614]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
