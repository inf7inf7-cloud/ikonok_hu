import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 29. csoport, 2026-10-24 (a Natsumero-projekt folytatása)
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1270 友よ: two friends on a rooftop at dusk, one arm around the other's shoulder, city behind
d,b=bg([(0,'#ff8a4a'),(1,'#ffd8a0')])
b+=skyline(600,'#5a3a4a',1270,80,240,'#ffd27a',60)+'<rect y="600" width="800" height="200" fill="#2a1a24"/>'
b+=figure(340,620,260,'#14080e')+figure(450,620,250,'#14080e')+'<path d="M350 420 Q400 400 455 420" stroke="#14080e" stroke-width="16" fill="none" stroke-linecap="round"/>'
I[1270]=svg(b,d)

# 1323 桜の栞: a pressed cherry blossom tucked as a bookmark in an open book on a school desk
d,b=bg([(0,'#fff0f4'),(1,'#f8e0e8')])
b+='<path d="M80 480 Q240 420 400 470 Q560 420 720 480 L720 720 Q560 660 400 710 Q240 660 80 720Z" fill="#fffaf2"/><path d="M400 470 L400 710" stroke="#d8c8b8" stroke-width="4"/>'
b+=''.join(f'<path d="M120 {y} Q240 {y-40} 370 {y-6}" stroke="#d8d0c8" stroke-width="5" fill="none"/>' for y in (540,580,620,660))
b+='<rect x="470" y="300" width="70" height="300" rx="6" fill="#f4e8d0" transform="rotate(8 505 450)"/>'+sakura(510,380,60,'#ffb0c8','#e86a90',10)+petals(14,1323,'#ffc8d8',0,420)
I[1323]=svg(b,d)

# 1324 唇にBe My Baby: glossy red lips blowing a pink bubble heart, pop-art dots
d,b=bg([(0,'#ff6aa8'),(1,'#ffb8d8')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#fff" opacity=".25"/>' for x in range(30,800,60) for y in range(30,800,60))
b+='<path d="M220 520 Q300 440 380 480 Q400 470 420 480 Q500 440 580 520 Q500 640 400 640 Q300 640 220 520Z" fill="#c8102a"/><path d="M240 522 Q400 560 560 522 Q400 540 240 522Z" fill="#6a0010"/>'
b+=heart(560,300,110,'#ff3a8a','opacity=".9"')+'<ellipse cx="520" cy="250" rx="26" ry="14" fill="#fff" opacity=".6"/>'
I[1324]=svg(b,d)

# 1389 君に100パーセント: a candy-colored heart meter filled to 100, bubbly harajuku pastels
d,b=bg([(0,'#ffe46a'),(1,'#ff9ad0')])
b+=confetti(60,1389,['#5ad8ff','#ff5aa8','#fff','#8a5aff'])
b+='<rect x="160" y="300" width="480" height="200" rx="100" fill="#fff"/><rect x="180" y="320" width="440" height="160" rx="80" fill="#ff5aa8"/>'
b+=txt(400,438,'100%',110,'#fff',900)+heart(640,560,70,'#5ad8ff')+star5(170,560,46,'#fff')
I[1389]=svg(b,d)

# 236 あした: an old rotary phone receiver off the hook with a long cord reaching toward a dawn window
d,b=bg([(0,'#2a2a4a'),(1,'#d8a0a0')])
b+='<rect x="440" y="140" width="260" height="320" fill="#ffd8a8"/><rect x="440" y="140" width="260" height="320" fill="none" stroke="#3a2a3a" stroke-width="14"/><path d="M570 140 L570 460 M440 300 L700 300" stroke="#3a2a3a" stroke-width="10"/>'+glow(570,300,120,'#fff0c8',.5)
b+='<rect y="600" width="800" height="200" fill="#3a2a2a"/>'+phone(240,560,1,'#1a1a1a')+'<path d="M140 520 Q60 420 160 380 Q260 340 200 300 Q140 260 260 220" stroke="#1a1a1a" stroke-width="7" fill="none"/>'
I[236]=svg(b,d)

# 448 サファイアの瞳: a large faceted blue sapphire glowing like an eye over a starry night
d,b=bg([(0,'#04081a'),(1,'#10204a')])
b+=starsf(90,448,800)+glow(400,420,220,'#3a7aff',.5)
b+='<polygon points="400,240 560,340 520,560 280,560 240,340" fill="#1a4ac8"/><polygon points="400,240 480,340 400,560 320,340" fill="#3a7aff"/><polygon points="240,340 560,340 400,300" fill="#7ab0ff" opacity=".8"/>'
b+=sparkle(500,300,30,'#fff')+sparkle(300,480,18,'#cfe0ff')
I[448]=svg(b,d)

# 756 ニシエヒガシエ: a compass needle spinning between West and East arrows on a road map
d,b=bg([(0,'#e8e0c8'),(1,'#c8b890')])
b+=''.join(f'<path d="M{x} 0 L{x+40} 800" stroke="#a89870" stroke-width="3" opacity=".5"/>' for x in range(0,800,90))+'<path d="M0 520 Q300 400 800 560" stroke="#c84a2a" stroke-width="12" fill="none"/>'
b+=ring(400,400,190,'#2a2a2a',18)+'<circle cx="400" cy="400" r="180" fill="#f8f4e8"/><polygon points="400,400 180,380 180,420" fill="#2a4ac8"/><polygon points="400,400 620,380 620,420" fill="#c8102a"/><circle cx="400" cy="400" r="18" fill="#2a2a2a"/>'
b+=txt(150,415,'西',70,'#2a4ac8',900)+txt(650,415,'東',70,'#c8102a',900)
I[756]=svg(b,d)

# 757 And I Love You: two hands holding steaming noodle cups touching, a borderless globe in the steam
d,b=bg([(0,'#f8f0e0'),(1,'#e8d8c0')])
b+=ring(400,260,130,'#3a8ac8',8,.6)+'<path d="M290 220 Q400 190 510 220 M280 290 Q400 320 520 290 M400 130 Q330 260 400 390 Q470 260 400 130" stroke="#3a8ac8" stroke-width="6" fill="none" opacity=".6"/>'
for x in (280,520): b+=f'<path d="M{x-80} 470 L{x+80} 470 L{x+60} 690 L{x-60} 690Z" fill="#fff"/><rect x="{x-80}" y="470" width="160" height="30" fill="#c8102a"/><path d="M{x} 460 Q{x-20} 420 {x} 390" stroke="#fff" stroke-width="8" fill="none" opacity=".6"/>'
b+=heart(400,560,40,'#c8102a')
I[757]=svg(b,d)

# 844 時の雫: a single teardrop falling from an hourglass into a ripple, soft blue
d,b=bg([(0,'#0a1a3a'),(1,'#3a6a9a')])
b+='<path d="M300 140 L500 140 L420 300 L500 460 L300 460 L380 300Z" fill="#cfe6ff" opacity=".35" stroke="#e8f0ff" stroke-width="8"/><path d="M330 430 L470 430 L440 380 L360 380Z" fill="#a8d0ff"/>'
b+='<path d="M400 520 Q380 560 400 580 Q420 560 400 520Z" fill="#a8d8ff"/>'+''.join(ring(400,680,r,'#a8d8ff',3,1.2-r/160) for r in (30,70,120))
I[844]=svg(b,d)

# 1125 ORION: the Orion constellation drawn over a winter night above a lone figure
d,b=bg([(0,'#02061a'),(1,'#1a2a5a')])
b+=starsf(120,1125,620)
P=[(300,160),(480,180),(370,300),(400,310),(430,320),(320,460),(500,440)]
b+='<polyline points="300,160 370,300 320,460" stroke="#a8c8ff" stroke-width="3" fill="none" opacity=".6"/><polyline points="480,180 430,320 500,440" stroke="#a8c8ff" stroke-width="3" fill="none" opacity=".6"/><polyline points="370,300 430,320" stroke="#a8c8ff" stroke-width="3" fill="none" opacity=".6"/>'
b+=''.join(sparkle(x,y,16,'#fff')+glow(x,y,20,'#cfe0ff',.5) for x,y in P)+snow(40,1125,.6)+'<rect y="680" width="800" height="120" fill="#e8eef8"/>'+figure(400,700,140,'#0a0a1a')
I[1125]=svg(b,d)

# 1245 RESCUE: a rescue rope with a ring lowered from a helicopter beam into a dark storm
d,b=bg([(0,'#1a1a24'),(1,'#3a3a4a')])
b+=rain(90,1245,'#cfe6ff',.4)+'<polygon points="420,80 200,800 640,800" fill="#fff6c8" opacity=".15"/>'
b+='<rect x="320" y="40" width="200" height="60" rx="30" fill="#c8102a"/><rect x="260" y="30" width="320" height="8" fill="#1a1a1a"/><path d="M420 100 L420 480" stroke="#ffb02a" stroke-width="8"/>'
b+=ring(420,520,50,'#ff6a1a',22)+ring(420,520,50,'#fff',6)+figure(420,760,150,'#000',pose='up')
I[1245]=svg(b,d)

# 1258 希望~Yell~: a volleyball soaring toward the sun, a megaphone in the foreground
d,b=bg([(0,'#3a9aff'),(1,'#d8f0ff')])
b+=rays(560,240,20,'#fff',.18,7)+'<circle cx="560" cy="240" r="90" fill="#fff4b0"/>'
b+='<circle cx="400" cy="360" r="80" fill="#fff"/><path d="M330 320 Q400 380 470 320 M340 420 Q400 360 460 420 M400 280 Q350 360 400 440" stroke="#2a5ac8" stroke-width="7" fill="none"/><path d="M400 280 Q470 360 400 440" stroke="#ffd02a" stroke-width="7" fill="none"/>'
b+='<path d="M120 620 L300 540 L300 720 Z" fill="#e8402a"/><rect x="80" y="610" width="50" height="40" fill="#1a1a1a"/>'
I[1258]=svg(b,d)

# 1325 Green Flash: the green flash on the horizon at sunset over a calm sea
d,b=bg([(0,'#1a2a4a'),(.6,'#ff9a5a'),(1,'#ffd890')])
b+='<ellipse cx="400" cy="480" rx="80" ry="16" fill="#5aff8a"/>'+glow(400,476,120,'#5aff8a',.6)+'<path d="M330 476 Q400 440 470 476Z" fill="#7aff9a"/>'
b+='<rect y="480" width="800" height="320" fill="#1a3a5a"/>'+''.join(f'<rect x="{360+k*7}" y="{500+k*40}" width="{80-k*14}" height="6" fill="#5aff8a" opacity=".5"/>' for k in range(5))
I[1325]=svg(b,d)

# 1633 BUGS LIFE: a tiny glowing ladybug meeting a crowd of fireflies, a miracle encounter in the dark grass
d,b=bg([(0,'#04120a'),(1,'#0a2a1a')])
b+=''.join(glow(x,y,14,'#d8ff6a',.8,'glow2')+f'<circle cx="{x}" cy="{y}" r="5" fill="#f0ffb0"/>' for x,y in [(140,200),(260,140),(620,180),(700,300),(520,120),(330,260),(600,400),(180,380)])
b+=''.join(f'<path d="M{x} 800 Q{x+10} {640-(x%7)*20} {x+30} {600-(x%5)*20}" stroke="#1a4a2a" stroke-width="10" fill="none"/>' for x in range(0,800,45))
b+=glow(400,520,110,'#ff3a3a',.4)+'<ellipse cx="400" cy="530" rx="80" ry="64" fill="#e8202a"/><path d="M400 466 L400 594" stroke="#000" stroke-width="6"/><circle cx="400" cy="470" r="34" fill="#000"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="12" fill="#000"/>' for x,y in [(360,510),(440,510),(370,560),(430,560)])
I[1633]=svg(b,d)

# 1793 愛くださいませ: a girl's gloved hands held out with an empty ribbon-tied gift box, pleading, pastel idol
d,b=bg([(0,'#ffe0ee'),(1,'#d8c8ff')])
b+=''.join(heart(x,y,s,'#ff8ac0','opacity=".6"') for x,y,s in [(140,180,30),(640,140,40),(680,520,26),(120,560,22)])
b+='<path d="M180 800 Q220 640 300 560 L330 600 Q290 680 270 800Z M620 800 Q580 640 500 560 L470 600 Q510 680 530 800Z" fill="#ffd8c8"/><path d="M180 800 Q200 700 240 640 L280 690 Q260 740 260 800Z M620 800 Q600 700 560 640 L520 690 Q540 740 540 800Z" fill="#ff8ab8"/>'
b+='<rect x="300" y="420" width="200" height="160" rx="10" fill="#fff"/><rect x="390" y="420" width="20" height="160" fill="#ff5a9a"/><path d="M400 420 Q340 360 360 350 Q400 360 400 420 Q400 360 440 350 Q460 360 400 420Z" fill="#ff5a9a"/>'
b+='<ellipse cx="320" cy="580" rx="40" ry="22" fill="#ffd8c8"/><ellipse cx="480" cy="580" rx="40" ry="22" fill="#ffd8c8"/>'
I[1793]=svg(b,d)

# 2 愛燦燦: a warm radiant sun embracing a small family's silhouettes on a hillside
d,b=bg([(0,'#ffb04a'),(1,'#fff0c0')])
b+=rays(400,330,24,'#fff',.25,8)+'<circle cx="400" cy="330" r="130" fill="#ffe27a"/>'+hills(600,30,'#c88a3a',2)
b+=figure(330,640,190,'#3a1a0a')+figure(430,640,170,'#3a1a0a',hair='#3a1a0a')+figure(385,640,100,'#3a1a0a')
I[2]=svg(b,d)

# 269 港のヨーコ: a harbour at night with a neon bar sign, a man in a trench coat asking around
d,b=bg([(0,'#0a1028'),(1,'#1a2a4a')])
b+='<rect x="460" y="200" width="300" height="400" fill="#1a1420"/>'+neon(610,300,'YOKO',  '#ff4fa0',80)+chochin(520,440,.6,'#e8402a')
b+='<rect y="600" width="800" height="200" fill="#0a1a2a"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff4fa0" stroke-width="2" opacity=".2"/>' for y in (640,690,740))
b+='<rect x="60" y="420" width="12" height="180" fill="#3a3a4a"/>'+figure(300,600,240,'#000')+'<path d="M260 380 L250 560 L350 560 L340 380Z" fill="#2a2a2a"/>'
I[269]=svg(b,d)

# 830 Shine: a car driving into a burst of sunlight on an open coastal road, bright and joyful
d,b=bg([(0,'#4ab0ff'),(1,'#d8f4ff')])
b+=rays(620,200,22,'#fff',.25,7)+'<circle cx="620" cy="200" r="70" fill="#fffbe0"/>'+'<rect y="500" width="800" height="300" fill="#2a8ac8"/>'
b+='<path d="M0 640 Q400 560 800 600 L800 800 L0 800Z" fill="#5a5a5a"/><path d="M0 700 Q400 620 800 660" stroke="#fff" stroke-width="6" stroke-dasharray="40 30" fill="none"/>'
b+='<path d="M200 620 L250 570 L380 566 L430 610 L460 616 L460 650 L200 650Z" fill="#e8202a"/><circle cx="250" cy="652" r="22" fill="#1a1a1a"/><circle cx="410" cy="652" r="22" fill="#1a1a1a"/>'
I[830]=svg(b,d)

# 965 Best Friend: two girls sitting back to back on a beach in Okinawa, sharing earphones
d,b=bg([(0,'#5ad0ff'),(1,'#d0f8ff')])
b+='<rect y="440" width="800" height="160" fill="#2ab8d8"/><rect y="600" width="800" height="200" fill="#f8e8c0"/>'+cloud(200,200,1.2)+'<path d="M640 600 Q660 380 700 300" stroke="#6a4a2a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M700 300 Q{700+70*math.cos(a)} {300+40*math.sin(a)-20} {700+120*math.cos(a)} {300+80*math.sin(a)}" stroke="#2a8a3a" stroke-width="14" fill="none"/>' for a in (0.2,1.3,2.4,3.0,-0.6))
b+='<g fill="#2a2a3a"><circle cx="330" cy="470" r="30"/><path d="M300 500 L360 500 L380 640 L290 640Z"/><circle cx="440" cy="470" r="30"/><path d="M410 500 L470 500 L490 640 L400 640Z"/></g><path d="M350 460 Q385 430 420 460" stroke="#fff" stroke-width="4" fill="none"/>'
I[965]=svg(b,d)

# 1326 サステナブル: a hand holding a green seedling sprouting from a recycled-arrow circle, summer sky
d,b=bg([(0,'#7ad8ff'),(1,'#e8fff0')])
b+=''.join(f'<path transform="rotate({a} 400 400)" d="M400 200 A200 200 0 0 1 573 300" stroke="#3ab85a" stroke-width="26" fill="none"/><polygon transform="rotate({a} 400 400)" points="560,270 600,310 548,322" fill="#3ab85a"/>' for a in (0,120,240))
b+='<path d="M400 520 L400 380" stroke="#2a8a3a" stroke-width="12"/><path d="M400 420 Q340 360 300 380 Q340 440 400 420Z M400 400 Q470 330 510 350 Q470 420 400 400Z" fill="#4ad84a"/>'
b+='<path d="M290 560 Q400 500 510 560 L500 640 L300 640Z" fill="#f0c8a0"/>'
I[1326]=svg(b,d)

# 1327 NO WAY MAN: a figure kicking open a door in a wall onto an untouched glowing field
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
b+='<rect x="0" y="0" width="800" height="800" fill="#3a3a4a"/>'+''.join(f'<rect x="{x}" y="{y}" width="96" height="46" fill="#4a4a5a"/>' for y in range(0,800,52) for x in range(-48*((y//52)%2),800,104))
b+='<rect x="300" y="200" width="260" height="480" fill="#fff4c8"/>'+glow(430,440,240,'#fff4c8',.5)+'<path d="M560 200 L660 160 L660 720 L560 680Z" fill="#6a4a2a"/>'
b+=figure(380,700,300,'#000',pose='reach')
I[1327]=svg(b,d)

# 1876 若者のすべて: summer festival fireworks over a riverbank, a young man alone watching the end of summer
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=firework(260,220,150,'#ffb02a',28,1)+firework(560,180,110,'#ff5aa8',22,2)+firework(640,360,70,'#7ad8ff',18,3)
b+='<rect y="560" width="800" height="240" fill="#0a1020"/><path d="M0 560 L800 560" stroke="#ffb02a" stroke-width="2" opacity=".4"/>'+''.join(chochin(x,520,.35,'#e8402a') for x in (80,160,240))
b+=figure(560,720,170,'#000')
I[1876]=svg(b,d)

# 1880 花束のかわりにメロディーを: a boy with a guitar holding out musical notes like a bouquet
d,b=bg([(0,'#ffe8d0'),(1,'#ffc8b8')])
b+='<path d="M380 560 L420 560 L460 360 L340 360Z" fill="#f8f0e0"/><path d="M370 560 L430 560 L400 600Z" fill="#c8102a"/>'
b+=''.join(note(x,y,40,c) for x,y,c in [(330,330,'#c8102a'),(420,290,'#2a2a6a'),(370,240,'#e86a2a'),(470,340,'#2a8a5a')])
b+=figure(600,760,320,'#3a2a2a',pose='reachL')+guitar(640,600,.7,20,'#8a5a2a')
I[1880]=svg(b,d)

# 131 恋のダイヤル6700: a 70s rotary dial phone in bright orange, the dial spinning, retro TV pattern
d,b=bg([(0,'#ffd04a'),(1,'#ff8a2a')])
b+=''.join(f'<rect x="0" y="{y}" width="800" height="30" fill="#fff" opacity=".12"/>' for y in range(0,800,70))
b+='<path d="M220 640 L260 420 L540 420 L580 640Z" fill="#e8402a"/><path d="M190 410 Q200 330 300 330 L500 330 Q600 330 610 410 L540 420 L520 380 L280 380 L260 420Z" fill="#c8202a"/>'
b+=ring(400,530,90,'#fff',10)+''.join(f'<circle cx="{400+70*math.cos(math.radians(a))}" cy="{530+70*math.sin(math.radians(a))}" r="13" fill="#fff"/>' for a in range(150,420,30))+'<circle cx="400" cy="530" r="34" fill="#fff"/>'
I[131]=svg(b,d)

# 611 RUNNING TO HORIZON: a runner's silhouette sprinting toward a neon city horizon at night, 80s synth grid
d,b=bg([(0,'#0a0420'),(.6,'#4a0a5a'),(1,'#ff4aa0')])
b+='<circle cx="400" cy="440" r="140" fill="#ffb02a"/>'+''.join(f'<rect x="200" y="{440+k*22}" width="400" height="{6+k}" fill="#4a0a5a"/>' for k in range(6))
b+=skyline(500,'#140420',611,40,160,'#ff4aa0',40)+'<rect y="500" width="800" height="300" fill="#0a0420"/>'+''.join(f'<path d="M400 500 L{x} 800" stroke="#ff4aa0" stroke-width="2" opacity=".6"/>' for x in range(-400,1300,120))+''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff4aa0" stroke-width="2" opacity=".6"/>' for y in (530,580,650,740))
b+=figure(260,700,200,'#000',pose='reach')
I[611]=svg(b,d)

# 708 刹那さを消せやしない: a burning love letter curling into embers on a dark wet street
d,b=bg([(0,'#0a0a10'),(1,'#1a1a28')])
b+=rain(70,708,'#9ab0d8',.3)+glow(400,460,170,'#ff6a1a',.5)
b+='<path d="M290 380 L510 360 L520 540 L300 560Z" fill="#f4e8d0"/><path d="M300 560 Q340 500 380 540 Q420 480 470 530 Q500 470 520 540 L520 560 L300 580Z" fill="#ff8a2a"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#ffb02a"/>' for x,y in [(330,320),(450,280),(520,330),(380,250),(560,400)])+''.join(f'<path d="M340 {y} L480 {y-10}" stroke="#8a7a6a" stroke-width="4"/>' for y in (410,440,470))
I[708]=svg(b,d)

# 788 Beautiful Life: two silhouettes on a seaside cliff at golden hour, one reaching to forgive
d,b=bg([(0,'#ff9a6a'),(1,'#ffe6b0')])
b+='<circle cx="400" cy="480" r="110" fill="#fff4c8"/><rect y="480" width="800" height="320" fill="#3a6a8a"/><rect x="340" y="480" width="120" height="320" fill="#ffd890" opacity=".3"/>'
b+='<path d="M0 620 L520 600 L540 800 L0 800Z" fill="#2a1a1a"/>'+figure(260,610,220,'#000',pose='reach')+figure(420,605,210,'#000',hair='#000')
I[788]=svg(b,d)

# 880 球根: a flower bulb underground with roots, a single shoot breaking through to light, cross-section
d,b=bg([(0,'#c8e8ff'),(1,'#ffffff')])
b+='<rect y="320" width="800" height="480" fill="#5a3a2a"/>'+''.join(f'<circle cx="{(k*97)%800}" cy="{360+(k*53)%420}" r="{4+k%3*3}" fill="#4a2a1a"/>' for k in range(40))
b+='<ellipse cx="400" cy="560" rx="90" ry="100" fill="#e8d0a8"/><path d="M400 460 Q380 400 400 320" stroke="#4ab84a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M{380+k*10} 650 Q{340+k*20} 720 {320+k*40} 780" stroke="#c8b088" stroke-width="5" fill="none"/>' for k in range(5))
b+='<path d="M400 320 Q360 260 330 270 Q370 330 400 320Z M400 320 Q440 260 470 270 Q430 330 400 320Z" fill="#4ad84a"/>'+glow(400,200,140,'#fff6c8',.5)
I[880]=svg(b,d)

# 956 会いたい、会いたい、会えない。: two smartphones far apart on a map, a dotted line and a heart between them
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a7a')])
b+=starsf(60,956,800)+'<path d="M200 520 Q400 260 600 300" stroke="#fff" stroke-width="5" stroke-dasharray="14 14" fill="none" opacity=".7"/>'
for x,y in ((200,560),(600,340)): b+=f'<rect x="{x-50}" y="{y-90}" width="100" height="180" rx="16" fill="#0a0a14" stroke="#cfe0ff" stroke-width="5"/><rect x="{x-38}" y="{y-72}" width="76" height="130" fill="#7ab0ff" opacity=".5"/>'
b+=heart(400,380,40,'#ff5a8a')
I[956]=svg(b,d)

# 1064 ストロー: two straws in one glass of soda, bubbles rising, summer cafe pastel
d,b=bg([(0,'#bff0e8'),(1,'#fff6e0')])
b+='<path d="M290 300 L510 300 L480 680 L320 680Z" fill="#cfefff" opacity=".7"/><path d="M296 380 L504 380 L480 680 L320 680Z" fill="#ff9ab0" opacity=".7"/>'
b+='<path d="M370 680 L330 160 L300 140" stroke="#ff4a6a" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M430 680 L470 180 L500 160" stroke="#4a8aff" stroke-width="16" fill="none" stroke-linecap="round"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".7"/>' for x,y,r in [(350,600,8),(400,520,6),(450,620,9),(420,450,5),(370,420,7)])+'<rect x="260" y="680" width="280" height="20" rx="10" fill="#e8c8a8"/>'
I[1064]=svg(b,d)

# 1246 喜びの歌: a sleeper train window with a couple leaning out waving, colorful pennants of joy
d,b=bg([(0,'#7ad0ff'),(1,'#e0f6ff')])
b+=hills(560,40,'#5ab85a',1246)+'<rect x="0" y="380" width="800" height="200" fill="#c8102a"/><rect x="0" y="560" width="800" height="20" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="420" width="120" height="90" rx="10" fill="#cfe8ff"/>' for x in (40,220,580))
b+='<rect x="400" y="420" width="140" height="90" rx="10" fill="#cfe8ff"/>'+figure(440,520,150,'#1a1a1a',pose='wave')+figure(500,520,140,'#1a1a1a',hair='#1a1a1a')
b+='<path d="M0 120 Q400 220 800 120" stroke="#3a3a3a" stroke-width="2" fill="none"/>'+''.join(f'<polygon points="{x},{120+100*(1-((x-400)/400)**2)*.9} {x+40},{120+100*(1-((x-400)/400)**2)*.9} {x+20},{170+100*(1-((x-400)/400)**2)*.9}" fill="{c}"/>' for x,c in zip(range(40,760,80),['#ff4a4a','#ffd02a','#4ab84a','#4a8aff','#ff8ad0','#ff4a4a','#ffd02a','#4ab84a','#4a8aff']))
I[1246]=svg(b,d)

# 1384 絶対的第六感: a glowing third eye of intuition between a boy and a girl, cosmic sparkles
d,b=bg([(0,'#2a0a4a'),(1,'#6a3aaa')])
b+=starsf(80,1384,800)+glow(400,300,160,'#c8a0ff',.6)
b+='<path d="M300 300 Q400 220 500 300 Q400 380 300 300Z" fill="#fff"/><circle cx="400" cy="300" r="40" fill="#8a3aff"/><circle cx="400" cy="300" r="16" fill="#000"/>'+rays(400,300,16,'#fff',.15,4)
b+=profile(220,760,1.1,'#0a0a1a')+profile(580,760,1.0,'#0a0a1a',True)
I[1384]=svg(b,d)

# 267 HERO: a lone rock singer silhouette on a stage with one fist raised, hard spotlight, late-70s
d,b=bg([(0,'#100808'),(1,'#2a1010')])
b+='<polygon points="400,0 220,700 580,700" fill="#fff4c8" opacity=".18"/>'+glow(400,120,100,'#fff4c8',.6)
b+='<rect y="700" width="800" height="100" fill="#1a0a0a"/>'+figure(400,700,380,'#000',pose='wave')+'<path d="M390 560 L380 700" stroke="#3a3a3a" stroke-width="6"/>'
b+=''.join(f'<circle cx="{x}" cy="{760+(x%3)*10}" r="22" fill="#0a0404"/>' for x in range(40,800,70))
I[267]=svg(b,d)

# 689 Miss You: a woman's silhouette at a rain-streaked window holding a telephone, forbidden love, 90s
d,b=bg([(0,'#3a4a6a'),(1,'#7a8aa8')])
b+='<rect x="120" y="100" width="560" height="560" fill="#5a6a8a"/>'+rain(60,689,'#e8f0ff',.4,0,660)+skyline(660,'#2a3a5a',689,60,200,'#ffd27a',40)
b+='<rect x="120" y="100" width="560" height="560" fill="none" stroke="#1a1a24" stroke-width="20"/><path d="M400 100 L400 660" stroke="#1a1a24" stroke-width="12"/>'+profile(560,800,1.4,'#0a0a14',True)
I[689]=svg(b,d)

# 768 魔法のコトバ: honey dripping from a spoon onto a four-leaf clover, sparkles of magic, art school
d,b=bg([(0,'#fff6d0'),(1,'#ffe0a0')])
b+=''.join(sparkle(x,y,s,'#fff') for x,y,s in [(160,200,26),(620,160,20),(680,420,30),(140,520,18)])
b+='<path d="M380 120 L420 120 L430 300 Q400 330 370 300Z" fill="#c8c8d0"/><path d="M400 300 Q390 380 400 440 Q410 380 400 300" fill="#ffb020"/><circle cx="400" cy="450" r="14" fill="#ffb020"/>'
b+=''.join(f'<g transform="rotate({a} 400 580)"><path d="M400 580 Q350 520 375 494 Q400 486 400 526 Q400 486 425 494 Q450 520 400 580Z" fill="#3ab84a"/></g>' for a in (0,90,180,270))+'<path d="M400 580 Q420 660 460 720" stroke="#2a8a3a" stroke-width="8" fill="none"/>'
I[768]=svg(b,d)

# 845 夏音: a wind chime (furin) ringing on a summer veranda with a blue sky and cicada sound lines
d,b=bg([(0,'#3aa0ff'),(1,'#d8f0ff')])
b+=cloud(560,220,1.4)+'<rect x="0" y="0" width="800" height="70" fill="#5a3a2a"/>'
b+='<path d="M400 70 L400 240" stroke="#3a3a3a" stroke-width="3"/><path d="M330 330 Q330 230 400 230 Q470 230 470 330Z" fill="#e8f4ff" opacity=".85"/><path d="M340 300 Q370 270 400 300 Q430 330 460 300" stroke="#e8402a" stroke-width="6" fill="none"/>'
b+='<path d="M400 330 L400 450" stroke="#3a3a3a" stroke-width="3"/><rect x="370" y="450" width="60" height="140" fill="#fff" transform="rotate(8 400 450)"/>'+''.join(f'<path d="M{x} {y} q12 -10 24 0" stroke="#fff" stroke-width="5" fill="none"/>' for x,y in [(250,260),(510,260),(230,300),(530,300)])
I[845]=svg(b,d)

# 1030 ギブス: a plaster cast on an arm, two hands interlocked over it, raw red and white
d,b=bg([(0,'#f4f0e8'),(1,'#d8d0c8')])
b+='<path d="M100 520 L520 380 L560 480 L140 620Z" fill="#fff" stroke="#c8c0b8" stroke-width="4"/>'+''.join(f'<path d="M{180+k*70} {600-k*24} L{140+k*70} {500-k*24}" stroke="#d8d0c8" stroke-width="4"/>' for k in range(5))
b+='<path d="M540 420 Q620 380 660 420 Q680 460 640 480 L560 490Z" fill="#f0c8a8"/><path d="M600 300 Q660 340 640 420 L590 420 Q600 360 560 330Z" fill="#e8b898"/>'
b+=txt(300,520,'♡',80,'#c8102a',700)
I[1030]=svg(b,d)

# 1089 あなたに: an Okinawan sanshin leaning on a stone wall, hibiscus and turquoise sea behind
d,b=bg([(0,'#4ad0ff'),(1,'#c8f4ff')])
b+='<rect y="420" width="800" height="120" fill="#1ab8c8"/><rect y="540" width="800" height="260" fill="#c8b890"/>'+''.join(f'<rect x="{x}" y="{y}" width="110" height="58" rx="10" fill="#d8c8a0" stroke="#a89870" stroke-width="3"/>' for y in range(540,800,62) for x in range(-55*((y//62)%2),800,114))
b+='<g transform="rotate(-18 380 470)"><rect x="370" y="110" width="22" height="300" fill="#1a1a1a"/><path d="M362 110 L400 110 L396 70 L366 70Z" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="{y}" width="30" height="8" rx="4" fill="#d8b070"/>' for x,y in [(340,80),(392,90),(340,100)])
b+='<rect x="300" y="400" width="162" height="170" rx="28" fill="#2a2a2a"/><rect x="314" y="414" width="134" height="142" rx="20" fill="#e8dcc0"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#3a3a3a" opacity=".5"/>' for x,y in [(340,440),(420,450),(360,500),(410,520),(330,530)])
b+=''.join(f'<path d="M{376+k*5} 110 L{376+k*5} 540" stroke="#f4f0e8" stroke-width="2"/>' for k in range(3))+'<rect x="366" y="520" width="34" height="10" fill="#c8a060"/></g>'
b+=flower(640,620,70,5,'#e8202a','#ffd02a')
I[1089]=svg(b,d)

# 1287 やさしさで溢れるように: a cup overflowing with warm light pouring like water, cozy evening
d,b=bg([(0,'#3a2a3a'),(1,'#8a5a5a')])
b+=glow(400,400,240,'#ffd8a0',.45)+'<path d="M290 360 L510 360 L490 560 Q400 600 310 560Z" fill="#f4e8d8"/><path d="M510 400 Q580 400 570 460 Q560 510 500 510" stroke="#f4e8d8" stroke-width="18" fill="none"/>'
b+='<path d="M296 360 Q250 480 230 700 L270 700 Q290 520 320 380Z M504 360 Q560 480 580 700 L540 700 Q520 520 490 380Z" fill="#ffd27a" opacity=".85"/><ellipse cx="400" cy="362" rx="110" ry="18" fill="#ffe8a0"/>'
b+=''.join(heart(x,y,14,'#fff','opacity=".7"') for x,y in [(360,300),(430,260),(400,210)])+'<ellipse cx="400" cy="720" rx="300" ry="30" fill="#ffd27a" opacity=".5"/>'
I[1287]=svg(b,d)

# 1620 Magic Touch: a gloved hand with a glowing fingertip touching and making a spark burst, hip-hop dance lights
d,b=bg([(0,'#0a0a1a'),(1,'#1a0a2a')])
b+=''.join(f'<polygon points="{x},0 {x-120},800 {x+120},800" fill="{c}" opacity=".12"/>' for x,c in [(160,'#ff3aa8'),(400,'#3ad8ff'),(640,'#ffd02a')])
b+=glow(470,300,130,'#ffd8ff',.6)+rays(470,300,18,'#fff',.2,4)+sparkle(470,300,60,'#fff')
b+='<g fill="#f4f4f8"><path d="M250 800 L230 600 Q230 540 290 520 L380 500 Q410 496 410 520 L400 560 L330 580 Z"/>'
b+='<rect x="330" y="340" width="34" height="200" rx="17" transform="rotate(32 347 540)"/><rect x="300" y="420" width="32" height="130" rx="16" transform="rotate(10 316 550)"/><rect x="262" y="450" width="30" height="110" rx="15" transform="rotate(-6 277 560)"/><rect x="228" y="480" width="28" height="90" rx="14" transform="rotate(-18 242 570)"/><rect x="380" y="500" width="30" height="90" rx="15" transform="rotate(70 395 545)"/></g>'
I[1620]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
