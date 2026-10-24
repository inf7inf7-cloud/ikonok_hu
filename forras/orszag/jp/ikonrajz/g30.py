import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 30. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1641 LOUD: a megaphone shout cracking a concrete wall into pieces, bold yellow-black
d,b=bg([(0,'#1a1a1a'),(1,'#2a2a2a')])
b+='<rect x="420" y="0" width="380" height="800" fill="#7a7a80"/>'+bolt([(420,0),(470,160),(430,260),(500,400),(450,520),(520,800)],'#1a1a1a',10)+''.join(f'<polygon points="{x},{y} {x+40},{y+10} {x+20},{y+40}" fill="#7a7a80"/>' for x,y in [(360,200),(330,420),(380,560)])
b+='<path d="M80 340 L300 240 L300 560 L80 460Z" fill="#ffd02a"/><rect x="40" y="350" width="50" height="100" fill="#1a1a1a"/>'+''.join(f'<path d="M{320+k*30} {300-k*40} Q{360+k*40} 400 {320+k*30} {500+k*40}" stroke="#ffd02a" stroke-width="10" fill="none"/>' for k in range(3))
I[1641]=svg(b,d)

# 1658 ずうっといっしょ!: a red thread tied tightly in loops around two pinky fingers, dark obsessive pink
d,b=bg([(0,'#2a0a1a'),(1,'#5a1a3a')])
b+='<rect x="150" y="300" width="60" height="260" rx="30" fill="#f4d0c0" transform="rotate(20 180 560)"/><rect x="590" y="300" width="60" height="260" rx="30" fill="#f4d0c0" transform="rotate(-20 620 560)"/>'
b+=''.join(ring(400,420,r,'#e8102a',5,.9) for r in (40,60,80))+'<path d="M260 360 Q330 300 360 400 Q400 520 440 400 Q470 300 540 360" stroke="#e8102a" stroke-width="7" fill="none"/>'
b+=''.join(heart(x,y,16,'#ff3a6a','opacity=".6"') for x,y in [(140,160),(660,180),(400,680)])
I[1658]=svg(b,d)

# 138 夏をあきらめて: an empty beach in rain with a closed parasol and a lone surfboard, giving up on summer, 80s
d,b=bg([(0,'#7a8a9a'),(1,'#c8d0d8')])
b+=rain(90,138,'#ffffff',.4)+'<rect y="440" width="800" height="140" fill="#5a7a8a"/><rect y="580" width="800" height="220" fill="#c8b898"/>'
b+='<path d="M300 300 L320 620" stroke="#3a3a3a" stroke-width="10"/><path d="M290 300 Q310 240 330 300 L330 440 Q310 460 300 440Z" fill="#e8402a"/>'
b+='<ellipse cx="560" cy="500" rx="40" ry="150" fill="#f4f0e8" transform="rotate(12 560 500)"/><path d="M540 360 L590 640" stroke="#2a8ac8" stroke-width="10" transform="rotate(0)"/>'
I[138]=svg(b,d)

# 820 東京: a lonely figure on a pedestrian bridge above Tokyo traffic light trails at night, melancholy
d,b=bg([(0,'#0a0a1a'),(1,'#2a2a4a')])
b+=skyline(460,'#141428',820,80,300,'#ffd27a',90)+tokyo_tower(640,460,280)
b+='<rect y="460" width="800" height="340" fill="#0a0a14"/>'+''.join(f'<path d="M0 {y} Q400 {y-30} 800 {y}" stroke="{c}" stroke-width="5" fill="none" opacity=".8"/>' for y,c in [(640,'#ff3a3a'),(660,'#ff6a3a'),(700,'#ffe8a0'),(720,'#fff')])
b+='<rect x="0" y="540" width="800" height="24" fill="#3a3a4a"/><rect x="0" y="520" width="800" height="6" fill="#5a5a6a"/>'+figure(300,540,150,'#000')
I[820]=svg(b,d)

# 893 出逢った頃のように: a summer night phone call — a cord phone and a firefly-lit window, nostalgic 90s
d,b=bg([(0,'#1a2a5a'),(1,'#5a6aaa')])
b+=starsf(60,893,500)+moon(620,180,50)+'<rect y="560" width="800" height="240" fill="#2a1a2a"/>'
b+='<rect x="120" y="260" width="300" height="300" fill="#ffd890"/><rect x="120" y="260" width="300" height="300" fill="none" stroke="#2a1a2a" stroke-width="14"/>'+profile(300,560,.9,'#3a2a2a')
b+='<path d="M330 420 Q400 500 480 600 Q560 700 640 640" stroke="#f4f4f4" stroke-width="6" fill="none"/>'+phone(640,620,.7,'#f4f4f4')+''.join(glow(x,y,10,'#e8ff8a',.8,'glow2') for x,y in [(520,420),(600,360),(700,460)])
I[893]=svg(b,d)

# 1701 愛は傷つきやすく: a fragile glass heart with a hairline crack held between two hands, duet 1970
d,b=bg([(0,'#d8c8b8'),(1,'#a89888')])
b+=glow(400,380,200,'#fff',.4)+heart(400,380,150,'#ff8aa8','opacity=".55"')+bolt([(400,260),(380,330),(410,380),(390,450)],'#fff',5)
b+='<path d="M140 620 Q220 520 300 500 L320 540 Q260 580 220 680Z" fill="#e8c0a0"/><path d="M660 620 Q580 520 500 500 L480 540 Q540 580 580 680Z" fill="#c89878"/>'
I[1701]=svg(b,d)

# 74 望郷: a man by a train window at night looking at a distant village with one warm light, enka homesickness
d,b=bg([(0,'#0a1020'),(1,'#2a3040')])
b+=starsf(50,74,300)+moon(200,160,36)+hills(460,40,'#141828',74)+'<circle cx="560" cy="440" r="8" fill="#ffd27a"/>'+glow(560,440,40,'#ffd27a',.6)
b+='<rect x="0" y="0" width="800" height="800" fill="none" stroke="#3a2a1a" stroke-width="80"/><rect x="0" y="560" width="800" height="240" fill="#3a2a1a"/>'+profile(240,780,1.2,'#0a0808')
I[74]=svg(b,d)

# 192 夏の終りのハーモニー: two microphones facing each other under a starry late-summer sky
d,b=bg([(0,'#0a0a2a'),(1,'#3a2a5a')])
b+=starsf(120,192,800)+'<path d="M0 600 Q400 540 800 600 L800 800 L0 800Z" fill="#14102a"/>'
b+=enka_mic(290,470,140,'#c8c8d0')+enka_mic(510,470,140,'#c8a24a')+''.join(note(x,y,22,'#fff') for x,y in [(380,260),(440,220),(410,320)])
I[192]=svg(b,d)

# 313 しょっぱい三日月の夜: a salty-tear crescent moon over a dark sea, a man alone on the shore
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
b+=starsf(60,313,450)+'<circle cx="480" cy="220" r="90" fill="#fff4c8"/><circle cx="520" cy="200" r="86" fill="#04081a"/>'+'<path d="M430 300 Q420 330 430 345 Q440 330 430 300Z" fill="#cfe6ff"/>'
b+='<rect y="480" width="800" height="200" fill="#0a1830"/><rect y="680" width="800" height="120" fill="#1a1a1a"/>'+figure(260,700,180,'#000')
I[313]=svg(b,d)

# 412 Broken Sunset: a sunset reflected in a shattered mirror, pastel 80s idol
d,b=bg([(0,'#ff9aa8'),(1,'#ffd8b0')])
b+='<rect x="180" y="160" width="440" height="480" rx="20" fill="#e8e8f0"/><rect x="200" y="180" width="400" height="440" fill="#ff8a6a"/><circle cx="400" cy="420" r="90" fill="#ffd27a"/><rect x="200" y="460" width="400" height="160" fill="#8a5aaa"/>'
b+=bolt([(200,260),(330,330),(400,300),(480,420),(600,380)],'#fff',5)+bolt([(400,300),(380,520),(420,620)],'#fff',5)+bolt([(330,330),(260,560)],'#fff',4)
I[412]=svg(b,d)

# 812 KNOCKIN' ON YOUR DOOR: a fist knocking on a bright orange door, sound waves, 90s pop
d,b=bg([(0,'#3ad0ff'),(1,'#d8f8ff')])
b+='<rect x="260" y="120" width="300" height="600" rx="8" fill="#ff7a2a"/><rect x="290" y="160" width="240" height="240" rx="6" fill="#ff9a4a"/><rect x="290" y="440" width="240" height="240" rx="6" fill="#ff9a4a"/><circle cx="510" cy="420" r="16" fill="#ffd02a"/>'
b+='<path d="M100 330 L240 330 Q260 330 260 350 L260 410 Q260 430 240 430 L100 430Z" fill="#f0c8a8"/>'+''.join(f'<path d="M{620+k*40} {300-k*20} Q{660+k*50} 380 {620+k*40} {460+k*20}" stroke="#fff" stroke-width="8" fill="none"/>' for k in range(3))
I[812]=svg(b,d)

# 1182 覚醒: a giant blazing flame-mech fist rising from fire, neon pink and cyan flames
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a3a')])
b+=''.join(f'<path d="M{x} 800 Q{x-40} {600-(x%5)*20} {x+20} {460-(x%7)*20} Q{x+30} {560} {x+60} 800Z" fill="{c}" opacity=".85"/>' for x,c in zip(range(-20,800,80),['#ff3aa8','#3ae8ff','#ff3aa8','#3ae8ff','#ff3aa8','#3ae8ff','#ff3aa8','#3ae8ff','#ff3aa8','#3ae8ff','#ff3aa8']))
b+=glow(400,300,180,'#3ae8ff',.4)+'<path d="M320 420 L330 220 Q340 180 380 180 L460 180 Q500 180 500 220 L490 420Z" fill="#e8f0ff"/>'+''.join(f'<rect x="{x}" y="160" width="36" height="80" rx="16" fill="#e8f0ff"/>' for x in (330,372,414,456))
I[1182]=svg(b,d)

# 1892 メロディー: an old upright piano in an empty room with sunlight through the window, melody notes floating
d,b=bg([(0,'#d8c8a8'),(1,'#a8987a')])
b+='<polygon points="560,0 700,0 520,800 260,800" fill="#fff4d0" opacity=".3"/>'+'<rect y="620" width="800" height="180" fill="#7a5a3a"/>'
b+='<rect x="160" y="320" width="380" height="300" fill="#2a1a10"/><rect x="180" y="470" width="340" height="50" fill="#f4f0e8"/>'+''.join(f'<rect x="{x}" y="470" width="14" height="30" fill="#1a1a1a"/>' for x in range(196,510,34))
b+=''.join(note(x,y,26,'#fff') for x,y in [(560,320),(620,250),(680,330),(600,180)])
I[1892]=svg(b,d)

# 375 ボーイの季節: a penguin in a scarf standing on a quiet beach at dusk, nostalgic 80s pastel
d,b=bg([(0,'#9ab0e8'),(1,'#ffd0c0')])
b+='<circle cx="560" cy="440" r="80" fill="#fff0d0"/><rect y="460" width="800" height="140" fill="#6a8ac8"/><rect y="600" width="800" height="200" fill="#e8d8c0"/>'
b+='<ellipse cx="300" cy="560" rx="70" ry="110" fill="#1a1a2a"/><ellipse cx="300" cy="580" rx="46" ry="80" fill="#fff"/><circle cx="300" cy="440" r="50" fill="#1a1a2a"/><circle cx="318" cy="430" r="7" fill="#fff"/><polygon points="340,446 372,452 340,460" fill="#ffb02a"/>'
b+='<path d="M250 480 Q300 500 350 480 L350 500 Q300 520 250 500Z" fill="#e8402a"/><rect x="320" y="490" width="22" height="70" fill="#e8402a"/>'
I[375]=svg(b,d)

# 846 SURVIVAL: a lone guitarist on top of a ruined city tower, sunrise behind, 90s rock
d,b=bg([(0,'#3a1a1a'),(.6,'#ff6a2a'),(1,'#ffd08a')])
b+=rays(400,560,22,'#fff',.15,6)+'<circle cx="400" cy="560" r="90" fill="#ffe0a0"/>'+skyline(800,'#1a0a0a',846,200,520)
b+='<path d="M320 800 L340 420 L460 400 L480 800Z" fill="#0a0404"/><path d="M340 420 L360 380 L380 410 L420 370 L460 400Z" fill="#0a0404"/>'+figure(400,410,170,'#000',pose='up')+guitar(400,330,.4,-30,'#1a1a1a')
I[846]=svg(b,d)

# 1363 最後に階段を駆け上がったのはいつだ?: a girl running up a long staircase toward bright sky
d,b=bg([(0,'#5ab0ff'),(1,'#e8f6ff')])
b+=cloud(600,160,1.2)+''.join(f'<rect x="{80+k*60}" y="{720-k*56}" width="{720-k*60}" height="56" fill="{"#c8c8d0" if k%2 else "#d8d8e0"}"/>' for k in range(10))
b+=figure(380,512,200,'#1a1a2a',pose='reach',hair='#1a1a2a')+'<path d="M330 470 L300 500" stroke="#1a1a2a" stroke-width="14"/>'
I[1363]=svg(b,d)

# 1390 PONPONPON: a candy-colored harajuku explosion of eyeballs-free shapes — bows, donuts, stars bouncing
d,b=bg([(0,'#ffe0f0'),(1,'#d8f0ff')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x,y,r,c in [(180,200,70,'#ff8ac0'),(620,180,60,'#8ad8ff'),(200,600,60,'#ffe46a'),(620,600,80,'#b88aff')])
b+='<path d="M300 360 Q400 300 400 400 Q400 300 500 360 L500 440 Q400 500 400 400 Q400 500 300 440Z" fill="#ff3a8a"/><circle cx="400" cy="400" r="26" fill="#ff8ac0"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="34" fill="none" stroke="{c}" stroke-width="18"/>' for x,y,c in [(200,600,'#fff'),(620,180,'#fff')])+star5(180,200,40,'#fff')+star5(620,600,46,'#fff')+confetti(40,1390,['#ff3a8a','#3ad0ff','#ffd02a'])
I[1390]=svg(b,d)

# 1825 タッチ: a baseball resting on the pitcher's mound under a summer sky, a hand reaching to touch it
d,b=bg([(0,'#3a9aff'),(1,'#c8ecff')])
b+=cloud(200,180,1.3)+cloud(620,140,1)+'<rect y="460" width="800" height="340" fill="#4aa84a"/><ellipse cx="400" cy="600" rx="300" ry="90" fill="#c89a5a"/>'
b+='<circle cx="400" cy="540" r="60" fill="#fff"/><path d="M360 500 Q380 540 360 580 M440 500 Q420 540 440 580" stroke="#e8202a" stroke-width="5" fill="none" stroke-dasharray="8 6"/>'
b+='<path d="M560 800 L520 640 Q510 600 540 590 L600 580 L640 800Z" fill="#f0c8a8"/><rect x="520" y="560" width="22" height="70" rx="11" fill="#f0c8a8" transform="rotate(-30 530 600)"/>'
I[1825]=svg(b,d)

# 300 セクシャルバイオレットNo.1: a violet lipstick with a glam rock shine, late-70s sparkle
d,b=bg([(0,'#2a0a3a'),(1,'#6a1a8a')])
b+=rays(400,400,24,'#c88aff',.12,6)+glow(400,360,160,'#c86aff',.5)
b+='<rect x="340" y="420" width="120" height="260" rx="10" fill="#e8c86a"/><rect x="350" y="360" width="100" height="70" fill="#c8a24a"/><path d="M360 360 L360 220 Q400 170 440 240 L440 360Z" fill="#9a2ad8"/>'
b+=sparkle(500,220,30,'#fff')+sparkle(290,300,20,'#fff')+txt(400,620,'No.1',50,'#6a1a8a',900)
I[300]=svg(b,d)

# 591 Say Anything: a single white rose lying on a grand piano under a spotlight, X JAPAN ballad
d,b=bg([(0,'#0a0a0a'),(1,'#1a1a24')])
b+='<polygon points="400,0 200,620 600,620" fill="#fff" opacity=".1"/>'
b+='<path d="M120 520 Q120 440 260 440 L600 440 Q720 440 720 560 L720 600 L120 600Z" fill="#050505"/><rect x="120" y="600" width="600" height="20" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="560" width="22" height="40" fill="#f4f4f4"/>' for x in range(140,700,26))
b+='<path d="M300 470 L520 450" stroke="#2a6a2a" stroke-width="6"/>'+''.join(f'<path d="M0 0 C-40 -10 -36 -56 0 -60 C36 -56 40 -10 0 0Z" fill="#f4f4f4" transform="translate(540 450) rotate({a}) scale({k})"/>' for a,k in [(0,1),(60,.85),(-60,.85),(180,.6)])
I[591]=svg(b,d)

# 675 もうひとつの土曜日: a car parked by the night sea, a man and a woman sitting on the hood, a ring box
d,b=bg([(0,'#0a1028'),(1,'#2a3a5a')])
b+=starsf(60,675,400)+moon(620,160,40)+'<rect y="440" width="800" height="200" fill="#0a1a30"/><rect x="560" y="440" width="120" height="200" fill="#fff6dc" opacity=".2"/><rect y="640" width="800" height="160" fill="#1a1a1a"/>'
b+='<path d="M140 640 L180 560 L420 550 L470 600 L520 610 L520 660 L140 660Z" fill="#3a3a4a"/>'+figure(300,560,150,'#000')+figure(380,560,140,'#000',hair='#000')+'<rect x="330" y="440" width="22" height="18" fill="#c8102a"/>'
I[675]=svg(b,d)

# 806 Hate tell a lie: a girl crossing her fingers behind her back, honest heart shining in front, 90s pop
d,b=bg([(0,'#ffe0a8'),(1,'#ffb0c8')])
b+=glow(400,360,150,'#fff',.5)+heart(400,360,90,'#ff3a6a')+'<path d="M330 330 Q400 300 470 330" stroke="#fff" stroke-width="6" fill="none"/>'
b+=figure(400,800,360,'#3a2a4a',hair='#3a2a4a')+'<circle cx="300" cy="640" r="26" fill="#f0c8a8"/><rect x="290" y="600" width="12" height="40" rx="6" fill="#f0c8a8" transform="rotate(-15 296 620)"/><rect x="302" y="602" width="12" height="40" rx="6" fill="#f0c8a8" transform="rotate(15 308 622)"/>'
I[806]=svg(b,d)

# 985 Addicted To You: a vintage telephone surrounded by dozens of tiny hearts orbiting, late-night purple R&B
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a5a')])
b+=''.join(heart(400+220*math.cos(a),400+220*math.sin(a),18,'#ff4a9a','opacity=".8"') for a in [k*math.pi/8 for k in range(16)])
b+=phone(400,420,1.2,'#e8e0f4')+''.join(heart(400+120*math.cos(a),400+120*math.sin(a),10,'#ffb0d8') for a in [k*math.pi/5 for k in range(10)])
I[985]=svg(b,d)

# 1013 forgiveness: a white dove released from open hands into a pale sunrise
d,b=bg([(0,'#7a9ad8'),(1,'#ffd8b8')])
b+=rays(400,300,18,'#fff',.2,8)+glow(400,300,140,'#fff4d0',.5)
b+='<path d="M400 300 Q340 220 240 230 Q320 260 360 320 Q300 340 280 380 Q360 360 400 340 Q440 360 520 380 Q500 340 440 320 Q480 260 560 230 Q460 220 400 300Z" fill="#fff"/><circle cx="400" cy="300" r="18" fill="#fff"/>'
b+='<path d="M220 680 Q300 540 380 520 L400 560 Q330 600 300 700Z M580 680 Q500 540 420 520 L400 560 Q470 600 500 700Z" fill="#f0d0b8"/>'
I[1013]=svg(b,d)

# 1079 ウィンディング ロード: a winding mountain road snaking up a green valley, a car's headlights
d,b=bg([(0,'#ffb07a'),(1,'#ffe8c0')])
b+=hills(300,50,'#6a8a7a',1079,4)+hills(420,60,'#4a7a5a',1080,5)+hills(560,40,'#2a5a3a',1081,5)
b+='<path d="M400 800 Q100 700 300 600 Q600 520 380 440 Q200 380 420 330 Q560 300 480 260" stroke="#4a4a4a" stroke-width="40" fill="none"/><path d="M400 800 Q100 700 300 600 Q600 520 380 440 Q200 380 420 330 Q560 300 480 260" stroke="#fff" stroke-width="4" stroke-dasharray="20 18" fill="none"/>'
b+=glow(390,445,30,'#fff4b0',.9,'glow2')
I[1079]=svg(b,d)

# 1151 ここにしか咲かない花: a single unique white flower blooming on an island cliff by turquoise sea
d,b=bg([(0,'#4ac8ff'),(1,'#d8f8ff')])
b+='<rect y="420" width="800" height="380" fill="#2ab8d0"/><path d="M0 560 Q200 520 380 560 L420 800 L0 800Z" fill="#6a8a4a"/><path d="M0 600 Q200 570 380 600 L400 800 L0 800Z" fill="#4a6a3a"/>'
b+='<path d="M240 560 Q250 440 260 360" stroke="#2a6a2a" stroke-width="8" fill="none"/>'+flower(260,350,100,6,'#fff','#ffd02a')+cloud(600,180,1.1)
I[1151]=svg(b,d)

# 1160 コイスルオトメ: a schoolgirl's silhouette holding a love letter behind her back in a sunset hallway
d,b=bg([(0,'#ff9a7a'),(1,'#ffd8b0')])
b+=''.join(f'<rect x="{x}" y="120" width="120" height="300" fill="#fff0d0" opacity=".6"/>' for x in (80,280,480,680))+'<rect y="560" width="800" height="240" fill="#a87a5a"/>'+''.join(f'<polygon points="{x},420 {x+120},420 {x+220},800 {x+60},800" fill="#fff0d0" opacity=".2"/>' for x in (80,280,480))
b+=figure(400,600,280,'#2a1a2a',hair='#2a1a2a')+'<rect x="440" y="440" width="60" height="44" fill="#ffb0c8" transform="rotate(10 470 460)"/>'+heart(470,462,12,'#e8102a')
I[1160]=svg(b,d)

# 1328 センチメンタルトレイン: a morning commuter train window with a girl's reflection and a boy far down the carriage
d,b=bg([(0,'#c8e0f8'),(1,'#f8f4e8')])
b+='<rect x="0" y="0" width="800" height="800" fill="#e8e8ec"/><rect x="80" y="120" width="640" height="300" rx="20" fill="#a8d0f0"/>'+hills(360,30,'#7ab88a',1328)+'<rect x="80" y="120" width="640" height="300" rx="20" fill="none" stroke="#9aa0a8" stroke-width="14"/>'
b+=''.join(f'<rect x="{x}" y="60" width="8" height="70" fill="#9aa0a8"/><rect x="{x-16}" y="126" width="40" height="30" rx="8" fill="none" stroke="#9aa0a8" stroke-width="5"/>' for x in (180,400,620))
b+=profile(260,800,1.3,'#2a2a3a')+figure(620,700,170,'#5a5a6a')+'<rect y="700" width="800" height="100" fill="#7a5a6a"/>'
I[1328]=svg(b,d)

# 1611 共鳴: two crossed swords sending out concentric resonance rings under a crescent moon
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=starsf(60,1611,600)+'<circle cx="600" cy="160" r="50" fill="#fff4c8"/><circle cx="625" cy="150" r="48" fill="#0a0a1a"/>'+''.join(ring(400,420,r,'#c8a0ff',4,1-r/320) for r in (60,120,180,240,300))
b+='<g transform="rotate(40 400 420)"><rect x="392" y="160" width="16" height="400" fill="#e8e8f0"/><rect x="360" y="540" width="80" height="14" fill="#c8a24a"/><rect x="392" y="554" width="16" height="70" fill="#3a1a1a"/></g>'
b+='<g transform="rotate(-40 400 420)"><rect x="392" y="160" width="16" height="400" fill="#e8e8f0"/><rect x="360" y="540" width="80" height="14" fill="#c8a24a"/><rect x="392" y="554" width="16" height="70" fill="#3a1a1a"/></g>'
I[1611]=svg(b,d)

# 67 涙の季節: a single teardrop-shaped raindrop on a window over a late-60s city street, sepia
d,b=bg([(0,'#8a7a6a'),(1,'#c8b8a0')])
b+=skyline(600,'#5a4a3a',67,80,280,'#f4d8a0',50)+rain(40,67,'#f4f0e8',.3)+'<rect y="600" width="800" height="200" fill="#4a3a2a"/>'
b+='<path d="M400 220 Q330 340 340 400 Q350 470 400 470 Q450 470 460 400 Q470 340 400 220Z" fill="#cfe6ff" opacity=".75"/><ellipse cx="380" cy="400" rx="14" ry="26" fill="#fff" opacity=".7"/>'
I[67]=svg(b,d)

# 129 カルメン'77: a flamenco dancer silhouette with a red rose and a swirling ruffled skirt, disco lights
d,b=bg([(0,'#3a0a1a'),(1,'#8a1a2a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="#ffd02a" opacity=".8"/>' for x,y in [(100,100),(200,160),(600,120),(700,200),(160,300),(660,320)])
b+='<path d="M400 360 Q300 520 200 640 Q320 620 400 700 Q480 620 600 640 Q500 520 400 360Z" fill="#e8102a"/><path d="M220 640 Q320 600 400 680 Q480 600 580 640" stroke="#fff" stroke-width="6" fill="none"/>'
b+=figure(400,420,220,'#000',pose='up',hair='#000')+rose(440,180,.5)
I[129]=svg(b,d)

# 246 リフレインが叫んでる: a convertible parked at an empty seaside road at dusk, waves crashing, a woman remembering
d,b=bg([(0,'#3a2a5a'),(.6,'#e87a6a'),(1,'#ffc890')])
b+='<rect y="440" width="800" height="160" fill="#3a4a7a"/>'+''.join(f'<path d="M{x} 520 q30 -30 60 0" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>' for x in range(20,800,120))+'<rect y="600" width="800" height="200" fill="#2a2a2a"/>'
b+='<path d="M160 640 L200 590 L420 584 L480 620 L540 626 L540 670 L160 670Z" fill="#f4f0e8"/><circle cx="220" cy="672" r="22" fill="#1a1a1a"/><circle cx="480" cy="672" r="22" fill="#1a1a1a"/>'+figure(640,640,150,'#14080e',hair='#14080e')
I[246]=svg(b,d)

# 247 恋人がサンタクロース: a lover dressed as Santa skiing down a snowy slope under the night sky with a gift bag
d,b=bg([(0,'#0a1a4a'),(1,'#3a5a9a')])
b+=starsf(60,247,400)+snow(70,247)+'<path d="M0 400 L800 700 L800 800 L0 800Z" fill="#f4f8ff"/>'+tree(120,420,140,'#1a4a3a')+tree(700,700,120,'#1a4a3a')
b+='<g transform="rotate(20 400 540)">'+figure(400,560,200,'#c8102a')+'<path d="M380 340 L400 310 L420 340Z" fill="#c8102a"/><circle cx="400" cy="306" r="8" fill="#fff"/><rect x="300" y="560" width="200" height="8" fill="#3a3a3a"/></g>'
b+='<ellipse cx="470" cy="470" rx="40" ry="50" fill="#a8603a"/>'
I[247]=svg(b,d)

# 551 千流の雫: a thousand streams converging into a single shining droplet, deep teal
d,b=bg([(0,'#0a2a3a'),(1,'#1a5a6a')])
b+=''.join(f'<path d="M{x} 0 Q{x+(400-x)*.4} 300 400 {460}" stroke="#7ae8ff" stroke-width="3" fill="none" opacity=".45"/>' for x in range(-200,1000,50))
b+=glow(400,520,100,'#a8f4ff',.6)+'<path d="M400 420 Q350 510 360 540 Q370 590 400 590 Q430 590 440 540 Q450 510 400 420Z" fill="#cff8ff"/>'
I[551]=svg(b,d)

# 821 ONE DAY: a sunrise over a highway with an open-top jeep and surfboard, mid-80s band freedom
d,b=bg([(0,'#ff9a5a'),(1,'#ffe6a0')])
b+='<circle cx="400" cy="460" r="110" fill="#fff4c8"/>'+''.join(f'<rect x="290" y="{400+k*20}" width="220" height="{4+k}" fill="#ff9a5a"/>' for k in range(5))+'<rect y="500" width="800" height="300" fill="#4a4a5a"/>'
b+='<polygon points="400,500 340,800 460,800" fill="#6a6a7a"/>'+''.join(f'<rect x="396" y="{540+k*60}" width="8" height="{20+k*8}" fill="#fff"/>' for k in range(4))+''.join(f'<path d="M{x} 500 L{x} 380" stroke="#1a1a1a" stroke-width="8"/><path d="M{x} 380 q-30 -10 -50 10 M{x} 380 q30 -10 50 10 M{x} 380 q-10 -30 -30 -40 M{x} 380 q10 -30 30 -40" stroke="#1a1a1a" stroke-width="7" fill="none"/>' for x in (120,690))
I[821]=svg(b,d)

# 1050 Ring: a silver ring lying in a dark puddle reflecting a streetlight, rainy night, sad ballad
d,b=bg([(0,'#0a0a14'),(1,'#1a1a28')])
b+=rain(80,1050,'#9ab0d8',.35)+'<rect x="580" y="80" width="10" height="400" fill="#2a2a3a"/>'+glow(560,100,80,'#ffd27a',.6)
b+='<ellipse cx="400" cy="620" rx="280" ry="70" fill="#1a2a3a"/><ellipse cx="460" cy="610" rx="30" ry="10" fill="#ffd27a" opacity=".4"/>'+ring(380,580,46,'#e8e8f0',12)+'<path d="M370 540 L380 520 L390 540Z" fill="#cfe6ff"/>'+sparkle(390,526,14,'#fff')
I[1050]=svg(b,d)

# 1621 Mazy Night: young friends running down a neon alley maze at midnight, police-light red and blue
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<rect x="0" y="0" width="220" height="800" fill="#141420"/><rect x="580" y="0" width="220" height="800" fill="#141420"/>'+neon(110,300,'夜',  '#ff3a6a',90)+neon(690,240,'BAR','#3ad0ff',60)
b+=glow(150,100,100,'#ff2a2a',.4)+glow(650,100,100,'#2a6aff',.4)+'<polygon points="220,800 580,800 460,360 340,360" fill="#2a2a3a"/>'
b+=figure(360,720,200,'#000',pose='reach')+figure(450,690,170,'#000',pose='reachL')
I[1621]=svg(b,d)

# 1622 What We Got ~奇跡はきみと~: two hands holding a glowing shooting star together, sparkling night
d,b=bg([(0,'#0a0a2a'),(1,'#2a3a6a')])
b+=starsf(100,1622,800)+'<path d="M760 80 L460 360" stroke="#fff" stroke-width="6" opacity=".4"/>'
b+=glow(420,400,100,'#fff4c8',.7)+star5(420,400,60,'#fff4c8')
b+='<path d="M220 720 Q260 540 360 470 L390 500 Q320 580 300 720Z M620 720 Q580 540 480 470 L450 500 Q520 580 540 720Z" fill="#f0c8a8"/>'
I[1622]=svg(b,d)

# 1727 夜明けの停車場: a small country railway station at dawn with a single lamp, a man with a suitcase
d,b=bg([(0,'#3a3a6a'),(.7,'#e8a08a'),(1,'#ffd8a8')])
b+=hills(500,30,'#3a3a5a',1727)+'<rect y="560" width="800" height="240" fill="#5a5048"/><rect y="560" width="800" height="14" fill="#c8b898"/>'
b+='<path d="M80 560 L80 320 L380 300 L380 560Z" fill="#4a3a2a"/><path d="M60 330 L230 240 L400 310Z" fill="#2a1a1a"/><rect x="140" y="160" width="10" height="160" fill="#2a1a1a"/>'+glow(145,170,40,'#ffd27a',.8)
b+=figure(560,580,200,'#1a1010')+'<rect x="590" y="500" width="60" height="44" fill="#6a3a2a"/>'
I[1727]=svg(b,d)

# 1865 死ぬな!: a bright little flower stubbornly growing through cracked asphalt, warm hopeful light
d,b=bg([(0,'#ffd08a'),(1,'#fff0d0')])
b+=rays(400,120,20,'#fff',.25,8)+'<rect y="460" width="800" height="340" fill="#5a5a60"/>'+bolt([(100,460),(240,560),(400,520),(520,640),(700,600),(800,700)],'#2a2a30',8)
b+='<path d="M400 560 Q390 470 400 380" stroke="#3a9a3a" stroke-width="10" fill="none"/><path d="M400 480 Q350 440 330 460 Q360 500 400 480Z" fill="#4ad84a"/>'+flower(400,360,90,8,'#ffb02a','#e8402a')
I[1865]=svg(b,d)

import os
os.makedirs('/tmp/jprajz/svg',exist_ok=True)
for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
print(len(I))
