import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 8. csoport, 2026-10-24
I={}
def guitar(x,y,s,a,col='#c8702a'):
    return f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><ellipse cx="0" cy="60" rx="70" ry="64" fill="{col}"/><ellipse cx="0" cy="-10" rx="52" ry="50" fill="{col}"/><circle cx="0" cy="30" r="20" fill="#1a1a1a"/><rect x="-8" y="-220" width="16" height="200" fill="#3a2414"/><rect x="-14" y="-260" width="28" height="44" rx="4" fill="#3a2414"/></g>'

# 264 長い夜: a lone guitarist under a single streetlight at deep night, a long trail of stars wheeling overhead
d,b=bg([(0,'#04061a'),(1,'#141a34')])
for k in range(10): b+=f'<circle cx="400" cy="-60" r="{180+k*48}" fill="none" stroke="#c8d8ff" stroke-width="2" stroke-dasharray="{20+k*6} {30+k*4}" opacity=".5"/>'
b+='<rect y="680" width="800" height="120" fill="#0a0c18"/><rect x="590" y="300" width="10" height="400" fill="#0a0c18"/><path d="M560 300 L630 300 L620 284 L570 284Z" fill="#0a0c18"/>'+glow(595,310,50,'#ffd88a',.7)+'<polygon points="595,310 470,690 720,690" fill="#ffe8b0" opacity=".12"/>'
b+=figure(560,690,190,'#020308')+guitar(540,600,.45,-50,'#3a2a1a')
I[264]=svg(b,d)

# 554 ただ泣きたくなるの: a single teardrop falling past a window streaked with rain, city lights blurred behind it
d,b=bg([(0,'#2a3a5a'),(1,'#5a6a8a')])
r=R(554)
for _ in range(26): b+=f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(300,800):.0f}" r="{r.uniform(20,50):.0f}" fill="{r.choice(["#ffd27a","#ff9a7a","#bfe0ff"])}" opacity=".25"/>'
for _ in range(14): x=r.uniform(40,760);y=r.uniform(40,700);b+=f'<path d="M{x:.0f} {y:.0f} q-4 {r.uniform(40,120):.0f} 2 {r.uniform(120,200):.0f}" stroke="#d8e8ff" stroke-width="4" fill="none" opacity=".5"/>'
b+='<path d="M400 240 Q470 360 470 420 A70 70 0 0 1 330 420 Q330 360 400 240Z" fill="#bfe0ff" opacity=".85"/><ellipse cx="375" cy="400" rx="14" ry="26" fill="#fff" opacity=".8"/>'
I[554]=svg(b,d)

# 935 夏の王様: a golden crown sitting on a beach towel under a blazing sun, a watermelon slice beside it
d,b=bg([(0,'#ff9a1a'),(.5,'#ffd04a'),(1,'#ffe8a0')])
b+=rays(400,180,20,'#fff',.3,10)+glow(400,180,110,'#fff8d0',.9)+'<circle cx="400" cy="180" r="70" fill="#fff8d0"/>'
b+='<path d="M-10 460 Q400 430 810 460 L810 810 L-10 810Z" fill="#f4d890"/><path d="M140 520 L660 520 L700 760 L100 760Z" fill="#2a8ae8"/>'+''.join(f'<path d="M{140+k*104} 520 L{100+k*120} 760" stroke="#fff" stroke-width="20"/>' for k in range(0,6,2))
b+='<path d="M270 640 L290 520 L340 580 L400 490 L460 580 L510 520 L530 640Z" fill="#ffd02a" stroke="#c8901a" stroke-width="6"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="12" fill="{c}"/>' for x,y,c in [(290,520,'#e8302a'),(400,490,'#2a8ae8'),(510,520,'#3ac85a')])
b+='<path d="M560 700 A90 90 0 0 0 740 700Z" fill="#3ac85a"/><path d="M574 700 A76 76 0 0 0 726 700Z" fill="#ff4a5a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="7" fill="#1a1a1a"/>' for x,y in [(620,720),(650,740),(680,720),(650,710)])
I[935]=svg(b,d)

# 1391 にんじゃりばんばん: a pop-pastel ninja star spinning through a candy sky full of sweets and sparkles
d,b=bg([(0,'#ffb0e0'),(1,'#b0e8ff')])
b+=rays(400,400,18,'#fff',.35,4)
b+='<g transform="rotate(20 400 400)">'+''.join(f'<path d="M400 400 L{400+220*math.cos(math.radians(a)):.0f} {400+220*math.sin(math.radians(a)):.0f} L{400+70*math.cos(math.radians(a+45)):.0f} {400+70*math.sin(math.radians(a+45)):.0f}Z" fill="{c}"/>' for a,c in [(0,'#ff5ab8'),(90,'#ffe05a'),(180,'#5ae8d8'),(270,'#a87aff')])+'<circle cx="400" cy="400" r="40" fill="#fff"/><circle cx="400" cy="400" r="16" fill="#ff5ab8"/></g>'
for x,y,c in [(130,140,'#ff5a8a'),(660,140,'#5ab8ff'),(120,640,'#ffd02a'),(670,660,'#8ae85a')]: b+=f'<circle cx="{x}" cy="{y}" r="34" fill="{c}"/><path d="M{x-34} {y} l-26 -18 v36Z M{x+34} {y} l26 -18 v36Z" fill="{c}"/>'
I[1391]=svg(b,d)

# 1572 ダンスホール: a mirror ball scattering coloured light over a polished dance floor
d,b=bg([(0,'#1a0a3a'),(1,'#3a1a5a')])
for k,c in enumerate(['#ff5ab8','#5ae8ff','#ffe05a','#8aff8a','#ff8a3a']): b+=f'<polygon points="400,230 {60+k*170},800 {140+k*170},800" fill="{c}" opacity=".18"/>'
b+='<rect x="396" y="0" width="8" height="120" fill="#c8c8d8"/><circle cx="400" cy="230" r="110" fill="#8a8aa8"/>'
for i in range(-5,6):
    for j in range(-5,6):
        if i*i+j*j<=26: b+=f'<rect x="{400+i*20-9}" y="{230+j*20-9}" width="18" height="18" fill="{["#e8e8ff","#c8c8e8","#ffffff","#a8a8c8"][(i*3+j)%4]}"/>'
b+='<path d="M-10 640 L810 640 L810 810 L-10 810Z" fill="#2a1a3a"/>'+''.join(f'<path d="M{k*100} 640 L{k*160-240} 800" stroke="#5a3a7a" stroke-width="3"/>' for k in range(10))
b+=sparkle(250,500,30,'#fff')+sparkle(560,560,24,'#fff')+sparkle(640,380,20,'#fff')
I[1572]=svg(b,d)

# 1741 恋、はじめました。: a summer café sign reading the first line of love, a shaved ice with a heart-shaped strawberry on top
d,b=bg([(0,'#bfeaff'),(1,'#fff4f8')])
b+='<path d="M80 80 L720 80 L720 180 Q400 230 80 180Z" fill="#fff" stroke="#3a7ae8" stroke-width="6"/>'+''.join(f'<path d="M{100+k*100} 120 q30 -26 60 0" stroke="#3a7ae8" stroke-width="10" fill="none"/>' for k in range(6))
b+='<path d="M260 480 L540 480 L480 720 L320 720Z" fill="#d8f4ff" opacity=".85"/><path d="M240 480 Q260 330 400 300 Q540 330 560 480Z" fill="#fff"/><path d="M290 420 Q400 360 510 430 Q500 470 400 470 Q300 470 290 420Z" fill="#ff7aa8" opacity=".8"/>'
b+=heart(400,340,60,'#ff2a5a')+''.join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="5" fill="#ffe8a0"/>' for x,y in [(390,330),(410,340),(400,355)])
I[1741]=svg(b,d)

# 1785 Velonica: a red bicycle racing downhill along a coastal road, wind lines streaming behind it
d,b=bg([(0,'#1a80e8'),(1,'#a8e0ff')])
b+='<rect y="420" width="800" height="120" fill="#0a6ad8"/><path d="M-10 540 L810 400 L810 810 L-10 810Z" fill="#5ab84a"/><path d="M-10 640 L810 480 L810 560 L-10 720Z" fill="#8a8a94"/>'
b+='<g transform="rotate(-10 400 560)"><circle cx="300" cy="600" r="70" fill="none" stroke="#1a1a24" stroke-width="12"/><circle cx="500" cy="600" r="70" fill="none" stroke="#1a1a24" stroke-width="12"/><path d="M300 600 L380 500 L480 500 L500 600 M380 500 L410 600 L480 500 M460 470 L500 470" stroke="#e8302a" stroke-width="14" fill="none" stroke-linejoin="round"/></g>'
b+=figure(420,520,160,'#1a1a2a',pose='stand')
for y in (380,430,480): b+=f'<path d="M{60+y%3*40} {y} L{240} {y-20}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
I[1785]=svg(b,d)

# 637 ギリギリchop: a rope stretched to its last strand, frayed fibres snapping over a red-hot background
d,b=bg([(0,'#e8301a'),(1,'#5a0a0a')])
b+=rays(400,400,24,'#ffd02a',.2,8)
b+='<path d="M-10 380 L320 400 M480 400 L810 380" stroke="#c8a060" stroke-width="54" stroke-linecap="round"/>'+''.join(f'<path d="M{310+k*4} 400 Q{340+k*8} {360+k*14} {360+k*10} {370+k*12}" stroke="#e8c880" stroke-width="5" fill="none"/>' for k in range(5))+''.join(f'<path d="M{490-k*4} 400 Q{460-k*8} {440-k*14} {440-k*10} {430-k*12}" stroke="#e8c880" stroke-width="5" fill="none"/>' for k in range(5))
b+='<path d="M330 400 Q400 410 470 400" stroke="#e8c880" stroke-width="5" fill="none"/>'+bolt([(400,140),(370,250),(420,280),(390,360)],'#ffe05a',12,1)
I[637]=svg(b,d)

# 1205 マイガール: a bunch of wildflowers held behind someone's back, a girl's silhouette waiting at a park bench
d,b=bg([(0,'#ffd8b0'),(1,'#ffb090')])
b+=hinomaru_sun(400,360,90,'#fff2d8',.7)+'<rect y="620" width="800" height="180" fill="#8ab86a"/>'
b+='<rect x="460" y="560" width="240" height="20" fill="#5a3a2a"/><rect x="470" y="580" width="12" height="60" fill="#5a3a2a"/><rect x="678" y="580" width="12" height="60" fill="#5a3a2a"/>'+figure(580,600,160,'#3a2030',hair='#3a2030')
b+=figure(200,680,280,'#1a1a2a')+''.join(flower(x,y,30,5,c,'#ffd02a',x%40,.7) for x,y,c in [(130,520,'#ff7aa8'),(110,560,'#ffffff'),(150,550,'#ffd02a'),(130,580,'#a87aff')])
I[1205]=svg(b,d)

# 1299 ポニーテールとシュシュ: a ponytail tied with a pink scrunchie swinging in the sea breeze on a sunlit beach
d,b=bg([(0,'#4ac0f8'),(1,'#d0f4ff')])
b+='<rect y="460" width="800" height="120" fill="#1aa0e0"/><path d="M-10 580 Q400 550 810 580 L810 810 L-10 810Z" fill="#f4e0a8"/>'
b+='<circle cx="300" cy="380" r="140" fill="#2a1a10"/><path d="M420 340 Q560 300 640 400 Q700 500 620 620 Q600 520 540 470 Q480 430 420 420Z" fill="#2a1a10"/>'
b+='<ellipse cx="430" cy="380" rx="34" ry="54" fill="#ff7ab8"/>'+''.join(f'<path d="M{430+30*math.cos(math.radians(a)):.0f} {380+48*math.sin(math.radians(a)):.0f} q6 6 0 12" stroke="#ff4a9a" stroke-width="5" fill="none"/>' for a in range(0,360,40))
I[1299]=svg(b,d)

# 1497 ミックスナッツ: a bowl of mixed nuts where one peanut has cracked open to reveal a tiny glowing heart
d,b=bg([(0,'#3a2a5a'),(1,'#1a1a3a')])
b+='<ellipse cx="400" cy="560" rx="300" ry="80" fill="#c84a3a"/><path d="M100 560 Q120 740 400 760 Q680 740 700 560Z" fill="#e85a4a"/>'
r=R(1497)
for _ in range(26):
    x,y=r.uniform(150,650),r.uniform(470,560);a=r.uniform(0,180);c=r.choice(['#c8904a','#a8703a','#e8c080','#8a5a2a'])
    b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r.uniform(20,30):.0f}" ry="16" fill="{c}" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+='<g transform="rotate(-20 400 330)"><path d="M300 330 Q300 260 360 270 Q400 280 400 330 Q400 380 360 390 Q300 400 300 330Z" fill="#e8c080"/><path d="M500 330 Q500 260 440 270 Q400 280 400 330 Q400 380 440 390 Q500 400 500 330Z" fill="#d8b070"/></g>'+glow(400,330,60,'#ff5a8a',.7)+heart(400,330,38,'#ff2a6a')
I[1497]=svg(b,d)

# 1744 明日への扉: a door standing alone in an open field, swung open onto a bright tomorrow beyond
d,b=bg([(0,'#3a3a7a'),(1,'#8a7aaa')])
b+='<rect y="600" width="800" height="200" fill="#3a5a3a"/><rect x="300" y="200" width="200" height="420" fill="#fff6d8"/>'+glow(400,410,200,'#fff6d8',.5)+'<rect x="310" y="210" width="180" height="400" fill="#fffbe8"/>'
b+='<path d="M300 200 L220 230 L220 650 L300 620Z" fill="#7a4a2a"/><circle cx="235" cy="430" r="8" fill="#d8b040"/>'
b+='<polygon points="310,610 490,610 620,800 180,800" fill="#fff6d8" opacity=".35"/>'+starsf(30,1744,500,'#fff')
I[1744]=svg(b,d)

# 994 monochrome: a single red rose standing out in an entirely black-and-white winter scene
d,b=bg([(0,'#d8d8d8'),(1,'#9a9a9a')])
b+=snow(60,994)+'<rect y="620" width="800" height="180" fill="#eaeaea"/>'
for x,h in [(140,360),(660,400),(260,300),(560,320)]: b+=f'<path d="M{x} 640 L{x} {640-h}" stroke="#3a3a3a" stroke-width="12"/><path d="M{x} {640-h*.6:.0f} L{x-60} {640-h*.85:.0f} M{x} {640-h*.4:.0f} L{x+70} {640-h*.7:.0f}" stroke="#3a3a3a" stroke-width="6"/>'
b+='<path d="M400 700 Q404 600 400 500" stroke="#2a2a2a" stroke-width="8" fill="none"/>'+rose(400,480,1.1)
I[994]=svg(b,d)

# 1523 勇者: a sword planted in a grassy hilltop at the end of a long journey, a cape draped over its hilt
d,b=bg([(0,'#5ab0f0'),(.6,'#ffd8a0'),(1,'#ffb07a')])
b+=cloud(160,160,1.0)+cloud(620,220,.8)+'<path d="M-10 800 L-10 620 Q400 520 810 620 L810 800Z" fill="#6ab84a"/>'
b+='<rect x="390" y="260" width="20" height="340" fill="#d8e0f0"/><path d="M390 260 L400 220 L410 260Z" fill="#d8e0f0"/><rect x="340" y="580" width="120" height="18" rx="6" fill="#c89a40"/><rect x="392" y="596" width="16" height="70" fill="#5a3a2a"/>'
b+='<path d="M410 590 Q470 600 520 650 Q600 700 700 680 Q620 720 540 720 Q470 700 430 660Z" fill="#c82a2a"/><path d="M410 590 Q440 640 430 690 L450 700 Q470 640 430 594Z" fill="#8a1a1a"/>'+petals(14,1523,'#fff',0,800,6,10,.7)
I[1523]=svg(b,d)

# 638 BLOWIN': a highway with a motorbike roaring away into a sunset, wind tearing at the roadside palms
d,b=bg([(0,'#ff6a3a'),(.5,'#ffa84a'),(1,'#5a2a4a')])
b+=hinomaru_sun(400,400,130,'#ffe8a0',.8)+'<rect y="440" width="800" height="360" fill="#3a1a2a"/><path d="M340 440 L460 440 L760 800 L40 800Z" fill="#2a2a34"/>'
b+=''.join(f'<rect x="{396-k*6}" y="{470+k*60}" width="{8+k*12}" height="{20+k*10}" fill="#ffe05a"/>' for k in range(5))
b+='<g transform="translate(400 560)"><circle cx="-60" cy="60" r="40" fill="#0a0a10"/><circle cx="60" cy="60" r="40" fill="#0a0a10"/><path d="M-70 40 L-20 -20 L50 -10 L80 50Z" fill="#0a0a10"/></g>'+figure(400,560,150,'#0a0a10')
for x,f in [(100,1),(700,-1)]: b+=f'<path d="M{x} 440 Q{x+10*f} 300 {x+30*f} 200" stroke="#2a0a1a" stroke-width="14" fill="none"/>'+''.join(f'<path d="M{x+30*f} 200 q{60*f} {a} {120*f} {a+40}" stroke="#2a0a1a" stroke-width="12" fill="none"/>' for a in (-30,0,30))
I[638]=svg(b,d)

# 639 今夜月の見える丘に: two silhouettes sitting on a grassy hill gazing at a giant full moon
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=starsf(60,639,600,'#fff')+moon(400,330,190,'#fff6d8')+glow(400,330,240,'#fff6d8',.25)
b+='<path d="M-10 800 L-10 600 Q400 480 810 600 L810 800Z" fill="#0a1020"/>'
b+='<g fill="#060810"><circle cx="360" cy="470" r="22"/><path d="M330 560 Q330 500 360 490 Q390 500 390 560Z"/><circle cx="440" cy="474" r="20"/><path d="M412 560 Q412 504 440 494 Q468 504 468 560Z"/></g>'
I[639]=svg(b,d)

# 640 ねがい: a paper lantern rising alone into the night sky, carrying a wish written across its side
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a3a')])
b+=starsf(60,640,800,'#fff')
b+=glow(400,340,180,'#ffa83a',.5)+'<path d="M320 220 L480 220 L500 440 Q400 470 300 440Z" fill="#ffb84a"/><path d="M330 250 L470 250 L486 420 Q400 444 314 420Z" fill="#ffd27a"/>'+'<path d="M380 280 L380 400 M420 290 L420 380 M390 330 L440 330" stroke="#c84a1a" stroke-width="6" fill="none"/>'
b+='<path d="M-10 800 L-10 700 Q400 660 810 700 L810 800Z" fill="#0a0a14"/>'+''.join(glow(x,y,10,'#ffa83a',.6,'glow2')+f'<circle cx="{x}" cy="{y}" r="5" fill="#ffd27a"/>' for x,y in [(160,560),(620,520),(260,620)])
I[640]=svg(b,d)

# 982 Be My Last: a single wilting sunflower in a bare white room, the last petal about to fall
d,b=bg([(0,'#f0ece4'),(1,'#d8d2c8')])
b+='<polygon points="520,0 800,0 800,800 360,800" fill="#fff" opacity=".4"/><rect y="640" width="800" height="160" fill="#c8bca8"/>'
b+='<path d="M360 660 L440 660 L430 760 L370 760Z" fill="#8a7a6a"/><path d="M400 660 Q390 500 420 360" stroke="#5a7a3a" stroke-width="10" fill="none"/>'
b+='<g transform="rotate(30 430 340)"><circle cx="430" cy="340" r="44" fill="#5a3a1a"/>'+''.join(f'<ellipse cx="{430+60*math.cos(math.radians(a)):.0f}" cy="{340+60*math.sin(math.radians(a)):.0f}" rx="22" ry="10" fill="#d8a83a" transform="rotate({a} {430+60*math.cos(math.radians(a)):.0f} {340+60*math.sin(math.radians(a)):.0f})"/>' for a in range(30,240,40))+'</g>'
b+='<ellipse cx="520" cy="560" rx="22" ry="10" fill="#d8a83a" transform="rotate(30 520 560)"/>'
I[982]=svg(b,d)

# 995 HEAVEN: a white feather drifting down through a shaft of light breaking through the clouds
d,b=bg([(0,'#c8d8f0'),(1,'#f4f4ff')])
b+=rays(400,-60,14,'#fff',.4,6)+cloud(160,120,1.6,'#fff',.95)+cloud(640,100,1.8,'#fff',.95)
b+='<g transform="rotate(30 400 470)"><path d="M400 300 Q470 360 460 520 Q420 600 400 640 Q380 600 340 520 Q330 360 400 300Z" fill="#fff"/><path d="M400 320 L400 660" stroke="#c8d0e0" stroke-width="5"/>'+''.join(f'<path d="M400 {380+k*40} L{440 if k%2 else 360} {360+k*40}" stroke="#d8e0f0" stroke-width="3"/>' for k in range(6))+'</g>'+glow(400,470,140,'#fff',.4)
I[995]=svg(b,d)

# 1402 すずめ: a weathered white door standing alone in a ruined landscape, a starry sky glittering through it
d,b=bg([(0,'#7ac0f0'),(1,'#d8eef8')])
b+=cloud(600,180,1.4)+'<path d="M-10 800 L-10 600 Q400 560 810 600 L810 800Z" fill="#a89a80"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="18" fill="#7a6a5a" transform="rotate({a} {x} {y})"/>' for x,y,w,a in [(100,640,80,10),(600,620,100,-14),(640,700,60,20),(160,720,90,-8)])
b+='<rect x="280" y="240" width="240" height="420" fill="#f4f0e8"/><rect x="300" y="260" width="200" height="380" fill="#0a1440"/>'+''.join(f'<circle cx="{310+(k*53)%180}" cy="{280+(k*97)%340}" r="{2+k%3}" fill="#fff"/>' for k in range(24))+sparkle(400,380,30,'#bfe8ff')+'<circle cx="490" cy="460" r="8" fill="#c8a040"/>'
I[1402]=svg(b,d)

# 1410 Clock Strikes: a cracked clock face with its hands at midnight, gears bursting out in an explosion of light
d,b=bg([(0,'#1a0a0a'),(1,'#3a1a1a')])
b+=glow(400,400,260,'#ff6a1a',.4)
b+='<circle cx="400" cy="400" r="210" fill="#f4ece0" stroke="#1a1a1a" stroke-width="16"/>'+''.join(f'<rect x="394" y="210" width="12" height="34" fill="#1a1a1a" transform="rotate({a} 400 400)"/>' for a in range(0,360,30))
b+='<path d="M400 400 L400 240 M400 400 L414 270" stroke="#1a1a1a" stroke-width="14" stroke-linecap="round"/><circle cx="400" cy="400" r="14" fill="#c82a1a"/>'
b+=bolt([(560,250),(500,360),(540,420),(470,560)],'#1a1a1a',6,1)
for x,y,s in [(660,180,40),(680,600,30),(130,640,36)]: b+=f'<circle cx="{x}" cy="{y}" r="{s}" fill="none" stroke="#e89a3a" stroke-width="12" stroke-dasharray="10 8"/><circle cx="{x}" cy="{y}" r="{s*.4:.0f}" fill="#e89a3a"/>'
I[1410]=svg(b,d)

# 1866 まちがいさがし: two nearly identical leaves side by side, one with a tiny difference circled in red
d,b=bg([(0,'#f4f8ec'),(1,'#e0ecd0')])
for x,ex in [(250,False),(550,True)]:
    b+=f'<rect x="{x-140}" y="180" width="280" height="440" rx="16" fill="#fff" stroke="#c8d0b8" stroke-width="4"/><path d="M{x} 560 Q{x-110} 440 {x} 240 Q{x+110} 440 {x} 560Z" fill="#5aa84a"/><path d="M{x} 560 L{x} 260" stroke="#3a7a2a" stroke-width="5"/>'
    b+=''.join(f'<path d="M{x} {300+k*60} L{x+(50 if j else -50)} {270+k*60}" stroke="#3a7a2a" stroke-width="3"/>' for k in range(4) for j in (0,1) if not (ex and k==2 and j))
b+='<circle cx="575" cy="400" r="44" fill="none" stroke="#e8102a" stroke-width="8"/>'
I[1866]=svg(b,d)

# 1524 たぶん: a mug of coffee gone cold on a table at dawn beside two keys, one already removed from the ring
d,b=bg([(0,'#5a6a9a'),(1,'#d8a8a0')])
b+='<rect x="460" y="80" width="260" height="300" fill="#ffd8b0" opacity=".5"/><path d="M590 80 L590 380 M460 230 L720 230" stroke="#3a3a5a" stroke-width="12"/>'
b+='<rect y="560" width="800" height="240" fill="#6a4a3a"/><path d="M220 440 L380 440 L370 600 L230 600Z" fill="#f4f0e8"/><path d="M380 480 Q440 480 430 540 Q420 580 374 570" stroke="#f4f0e8" stroke-width="16" fill="none"/><ellipse cx="300" cy="446" rx="78" ry="12" fill="#3a2414"/>'
b+='<circle cx="520" cy="640" r="24" fill="none" stroke="#c8c8d0" stroke-width="8"/><path d="M540 650 L620 680 L616 690 L600 684 L596 694 L586 690" stroke="#d8b040" stroke-width="10" fill="none"/><path d="M640 610 L710 620" stroke="#c8c8d0" stroke-width="10"/><circle cx="640" cy="610" r="14" fill="none" stroke="#c8c8d0" stroke-width="6"/>'
I[1524]=svg(b,d)

# 1648 BAD LOVE: a black heart wrapped in thorny vines under a magenta spotlight
d,b=bg([(0,'#2a0420'),(1,'#0a0410')])
b+='<polygon points="400,-20 160,800 640,800" fill="#ff2ab8" opacity=".14"/>'+glow(400,420,220,'#ff2ab8',.35)+heart(400,420,170,'#0a0a10')
for k in range(3): b+=f'<path d="M{200} {340+k*70} Q400 {280+k*90} 600 {360+k*60}" stroke="#5a1a3a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{240+j*80} {330+k*72+ (j%2)*-8} l10 -22 l8 20" fill="#5a1a3a"/>' for j in range(5))
I[1648]=svg(b,d)

# 1796 儚くも永久のカナシ: a shattered blade of glass suspended in midair, every shard reflecting a crimson sky
d,b=bg([(0,'#3a040a'),(1,'#0a0204')])
b+=glow(400,400,240,'#e8102a',.35)
r=R(1796)
for _ in range(22):
    x,y=r.uniform(120,680),r.uniform(120,680);s=r.uniform(20,70);a=r.uniform(0,360)
    b+=f'<polygon points="{x:.0f},{y-s:.0f} {x+s*.4:.0f},{y+s*.3:.0f} {x-s*.5:.0f},{y+s*.6:.0f}" fill="{r.choice(["#ff5a6a","#e8e8f8","#c80a2a"])}" opacity=".85" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+='<path d="M390 160 L410 160 L420 600 L400 640 L380 600Z" fill="#e8e8f8" opacity=".9"/>'
I[1796]=svg(b,d)

# 996 No way to say: a wedding veil caught on a branch over a misty lake, left behind and fluttering
d,b=bg([(0,'#c8d0e0'),(1,'#e8ecf4')])
b+='<rect y="520" width="800" height="280" fill="#a8b8c8"/><rect y="500" width="800" height="40" fill="#fff" opacity=".6"/>'
b+='<path d="M-10 200 Q200 220 360 280 Q420 300 460 340" stroke="#3a3a44" stroke-width="20" fill="none"/><path d="M200 220 L170 140 M300 260 L320 180" stroke="#3a3a44" stroke-width="8"/>'
b+='<path d="M440 330 Q520 360 600 500 Q640 600 560 680 Q520 600 470 560 Q430 480 440 330Z" fill="#fff" opacity=".85"/><path d="M450 340 Q500 460 540 640" stroke="#e8ecf4" stroke-width="4" fill="none"/>'+flower(450,340,30,6,'#fff','#ffe8f0',0,.7)
I[996]=svg(b,d)

# 1206 夏疾風: a summer gale sweeping across a green rice field, a straw hat tumbling high on the wind
d,b=bg([(0,'#2a90f0'),(1,'#c8ecff')])
b+=cloud(600,160,1.6)+'<path d="M-10 480 L810 440 L810 810 L-10 810Z" fill="#5ac84a"/>'
for k in range(12): y=500+k*28;b+=f'<path d="M-10 {y} Q200 {y-20} 400 {y} T810 {y}" stroke="#8ae86a" stroke-width="5" fill="none" opacity=".7"/>'
b+='<g transform="rotate(-25 330 280)"><ellipse cx="330" cy="290" rx="130" ry="34" fill="#e8c870"/><path d="M260 290 Q270 220 330 210 Q390 220 400 290Z" fill="#e8c870"/><rect x="262" y="270" width="136" height="16" fill="#e8302a"/></g>'
for y in (220,320,380): b+=f'<path d="M{60} {y} Q160 {y-30} 240 {y}" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" opacity=".85"/>'
I[1206]=svg(b,d)

# 1207 Løve Rainbow: five coloured ribbons braided together into one rainbow heart floating in the sky
d,b=bg([(0,'#bfe8ff'),(1,'#fff4fa')])
b+=cloud(160,620,1.3)+cloud(640,660,1.5)
for k,c in enumerate(['#e8302a','#ffa82a','#ffe02a','#3ac85a','#2a8ae8']):
    s=1-k*.12;b+=f'<path d="M400 {600-k*14} C{400-280*s:.0f} {470-k*14} {400-200*s:.0f} {230+k*20} 400 {320+k*16} C{400+200*s:.0f} {230+k*20} {400+280*s:.0f} {470-k*14} 400 {600-k*14}Z" fill="none" stroke="{c}" stroke-width="22"/>'
I[1207]=svg(b,d)

# 641 Easy Come, Easy Go!: a hand tossing a coin high into the air against a hot pink sky, banknotes fluttering away
d,b=bg([(0,'#ff4a9a'),(1,'#ffa84a')])
b+=rays(400,260,18,'#fff',.2,8)+glow(400,240,70,'#ffe05a',.8)+'<ellipse cx="400" cy="240" rx="56" ry="60" fill="#ffd02a" stroke="#c8901a" stroke-width="8"/><text x="400" y="266" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="70" fill="#c8901a">¥</text>'
b+='<g fill="#e8b890"><rect x="350" y="600" width="100" height="220" rx="40"/><rect x="340" y="520" width="26" height="110" rx="13" transform="rotate(-20 353 575)"/><rect x="430" y="540" width="26" height="90" rx="13" transform="rotate(30 443 585)"/></g>'
for x,y,a in [(160,420,-20),(620,420,24),(700,600,-30),(110,640,30)]: b+=f'<rect x="{x-50}" y="{y-26}" width="100" height="52" rx="4" fill="#d8ecc8" stroke="#6a9a5a" stroke-width="4" transform="rotate({a} {x} {y})"/><circle cx="{x}" cy="{y}" r="14" fill="#6a9a5a" transform="rotate({a} {x} {y})"/>'
I[641]=svg(b,d)

# 722 TOMORROW: a small seedling pushing up through a crack in the pavement toward the morning sun
d,b=bg([(0,'#ffd8a0'),(1,'#fff4e0')])
b+=rays(560,200,16,'#fff',.4,7)+hinomaru_sun(560,200,80,'#fff2c8',.9)
b+='<rect y="560" width="800" height="240" fill="#8a8a94"/><path d="M-10 640 L810 640 M260 560 L240 800 M560 560 L580 800" stroke="#6a6a74" stroke-width="5"/>'
b+='<path d="M360 800 L380 620 L410 580 L430 640 L460 560 L470 800Z" fill="#5a5a64"/><path d="M410 580 Q400 500 410 420" stroke="#4aa83a" stroke-width="10" fill="none"/>'
b+='<path d="M410 440 Q470 380 530 410 Q480 460 410 440Z M410 470 Q340 420 290 450 Q350 500 410 470Z" fill="#5ac84a"/>'
I[722]=svg(b,d)

# 1594 Take a picture: a vintage instant camera spitting out a photo of a rainbow-coloured sky
d,b=bg([(0,'#ffe0f0'),(1,'#d8f0ff')])
b+='<rect x="190" y="300" width="420" height="300" rx="30" fill="#f4f4f4"/><rect x="190" y="300" width="420" height="80" rx="30" fill="#2a2a34"/><rect x="190" y="540" width="420" height="60" fill="#e8e8e8"/>'
for k,c in enumerate(['#e8302a','#ffa82a','#ffe02a','#3ac85a','#2a8ae8']): b+=f'<rect x="{360+k*12}" y="400" width="12" height="140" fill="{c}"/>'
b+='<circle cx="400" cy="460" r="90" fill="#2a2a34"/><circle cx="400" cy="460" r="60" fill="#1a1a24"/><circle cx="380" cy="440" r="18" fill="#5a5a74"/><rect x="520" y="320" width="60" height="40" rx="6" fill="#4a4a5a"/>'
b+='<rect x="250" y="590" width="300" height="200" fill="#fff"/><rect x="270" y="600" width="260" height="150" fill="url(#rb)"/>'
d+=lg('rb',S((0,'#ff7ab8'),(.5,'#ffe05a'),(1,'#5ae8ff')),0,0,0,1)
I[1594]=svg(b,d)

# 470 My Revolution: a girl's silhouette standing on a rooftop, arms flung wide as the dawn sun breaks out behind the city
d,b=bg([(0,'#2a2a6a'),(.5,'#e8607a'),(1,'#ffc87a')])
b+=rays(400,560,22,'#fff',.25,6)+hinomaru_sun(400,560,140,'#fff2c8',.9)
b+=skyline(620,'#2a1a3a',470,80,260,'#ffd27a',60)+'<rect x="200" y="600" width="400" height="200" fill="#1a0a1a"/>'
b+=figure(400,600,240,'#0a0410',pose='up',hair='#0a0410')
I[470]=svg(b,d)

# 510 世界でいちばん熱い夏: a thermometer exploding past its top over a blazing red sun, heat waves rippling everywhere
d,b=bg([(0,'#ff2a1a'),(1,'#ffa81a')])
b+=hinomaru_sun(400,400,220,'#ffe05a',.6)
for k in range(5): y=150+k*130;b+=f'<path d="M-10 {y} Q100 {y-20} 200 {y} T400 {y} T600 {y} T810 {y}" stroke="#fff" stroke-width="6" fill="none" opacity=".25"/>'
b+='<rect x="360" y="200" width="80" height="400" rx="40" fill="#fff"/><circle cx="400" cy="620" r="70" fill="#fff"/><circle cx="400" cy="620" r="52" fill="#e8102a"/><rect x="380" y="160" width="40" height="460" rx="20" fill="#e8102a"/>'
b+=''.join(f'<circle cx="{400+r_*math.cos(math.radians(a)):.0f}" cy="{150+r_*math.sin(math.radians(a)):.0f}" r="{14-r_//20}" fill="#e8102a"/>' for a,r_ in [(-150,60),(-110,90),(-70,80),(-30,60),(-90,120)])
I[510]=svg(b,d)

# 997 Startin': a pair of high-top sneakers on a starting line, the track stretching toward a bright horizon
d,b=bg([(0,'#3a8ae8'),(1,'#c8e8ff')])
b+='<path d="M300 400 L500 400 L800 800 L0 800Z" fill="#c84a3a"/>'+''.join(f'<path d="M{400+k*25} 400 L{400+k*160} 800" stroke="#fff" stroke-width="5"/>' for k in (-3,-1,1,3))
b+='<rect x="100" y="640" width="600" height="20" fill="#fff"/>'
for x in (300,500): b+=f'<path d="M{x-80} 640 L{x-80} 560 Q{x-70} 500 {x-30} 500 L{x+10} 540 Q{x+70} 560 {x+90} 600 L{x+90} 640Z" fill="#fff"/><rect x="{x-80}" y="620" width="170" height="20" fill="#2a2a34"/><path d="M{x-60} 540 L{x} 560 M{x-60} 570 L{x+10} 580" stroke="#e8302a" stroke-width="6"/>'
I[997]=svg(b,d)

# 1654 NIGHT DANCER: a lone figure dancing on a rooftop under neon city glow, the moon hanging like a spotlight
d,b=bg([(0,'#0a0420'),(1,'#2a0a3a')])
b+=moon(560,180,70,'#f4e8ff')+glow(560,180,140,'#d8b0ff',.3)+skyline(640,'#140828',1654,100,380,'#ff5ab8',80)
b+='<rect y="640" width="800" height="160" fill="#08040e"/>'+glow(400,560,140,'#a87aff',.35)+figure(400,650,220,'#000',pose='wave')
I[1654]=svg(b,d)

# 1787 Love Forever: two interlocking rings carved into the bark of an old tree, glowing gently in twilight
d,b=bg([(0,'#3a2a5a'),(1,'#a86a7a')])
b+='<path d="M200 800 Q240 400 220 0 L580 0 Q560 400 600 800Z" fill="#5a3a2a"/>'+''.join(f'<path d="M{240+k*40} 0 Q{250+k*40} 400 {230+k*44} 800" stroke="#4a2a1a" stroke-width="6" fill="none"/>' for k in range(9))
b+=glow(400,420,140,'#ffc8e0',.4)+'<circle cx="360" cy="420" r="80" fill="none" stroke="#ffd8e8" stroke-width="16"/><circle cx="440" cy="420" r="80" fill="none" stroke="#ffd8e8" stroke-width="16"/>'
I[1787]=svg(b,d)

# 525 朝がまた来る: a bedroom window at the end of a long night, curtains drawn back as first light floods the empty room
d,b=bg([(0,'#2a2a4a'),(1,'#4a3a5a')])
b+='<rect x="220" y="140" width="360" height="420" fill="#ffd8a0"/>'+glow(400,350,200,'#ffe8c0',.6)+'<path d="M220 140 L580 140 L580 560 L220 560Z M400 140 L400 560 M220 350 L580 350" stroke="#1a1a2a" stroke-width="14" fill="none"/>'
b+='<path d="M120 100 Q180 340 140 600 L220 600 L220 100Z" fill="#7a5a8a"/><path d="M680 100 Q620 340 660 600 L580 600 L580 100Z" fill="#7a5a8a"/>'
b+='<polygon points="220,560 580,560 760,800 40,800" fill="#ffe8c0" opacity=".3"/>'
I[525]=svg(b,d)

# 732 Sign: a hand-drawn sign language gesture in silhouette against an operating theatre's blue-green wall, a heartbeat line beneath
d,b=bg([(0,'#5ab8a8'),(1,'#2a7a7a')])
b+='<g fill="#f4e8e0" transform="rotate(-10 400 360)"><rect x="340" y="320" width="130" height="160" rx="40"/><rect x="340" y="190" width="28" height="150" rx="14"/><rect x="376" y="170" width="28" height="170" rx="14"/><rect x="412" y="200" width="28" height="140" rx="14"/><rect x="448" y="250" width="26" height="100" rx="13"/><rect x="290" y="350" width="80" height="28" rx="14" transform="rotate(-30 330 364)"/><rect x="360" y="460" width="90" height="200" rx="30"/></g>'
b+='<path d="M-10 680 L240 680 L280 600 L320 760 L360 640 L390 680 L810 680" stroke="#e8fff8" stroke-width="10" fill="none" stroke-linejoin="round"/>'
I[732]=svg(b,d)

# 936 全部だきしめて: a big bear hug between two silhouettes inside a giant sunflower-yellow heart
d,b=bg([(0,'#ffd02a'),(1,'#ff9a2a')])
b+=rays(400,400,20,'#fff',.25,8)+heart(400,400,220,'#fff4c8')
b+='<g fill="#5a2a0a"><circle cx="350" cy="300" r="40"/><circle cx="450" cy="300" r="40"/><path d="M290 560 Q280 380 350 350 Q400 340 450 350 Q520 380 510 560Z"/></g><path d="M300 420 Q400 380 500 440 M300 460 Q400 420 500 470" stroke="#3a1a04" stroke-width="18" fill="none" stroke-linecap="round"/>'
I[936]=svg(b,d)

# 1099 キズナ: a tug-of-war rope tied in a heart-shaped knot on a sunlit school field, hands of all sizes grabbing it
d,b=bg([(0,'#4ab8f8'),(1,'#c8ecff')])
b+=cloud(160,140,1.2)+'<rect y="440" width="800" height="360" fill="#5ab84a"/><path d="M-10 440 L810 440" stroke="#fff" stroke-width="10"/>'
b+='<path d="M-10 560 Q200 580 300 560 M500 560 Q600 580 810 560" stroke="#8a5a2a" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M400 640 C300 560 290 470 350 460 C390 455 400 500 400 520 C400 500 410 455 450 460 C510 470 500 560 400 640Z M300 560 C340 560 360 580 380 610 M500 560 C460 560 440 580 420 610" stroke="#8a5a2a" stroke-width="26" fill="none" stroke-linecap="round"/>'
for x,h,c in [(80,200,'#1a2a4a'),(190,160,'#3a1a2a'),(610,170,'#2a1a3a'),(720,210,'#1a3a2a')]: b+=figure(x,720,h,c,pose='reach' if x<400 else 'reachL')
I[1099]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
