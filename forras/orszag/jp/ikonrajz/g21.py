import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 21. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1008 UNITE!: many raised hands joining into one circle under a bright stage sky
d,b=bg([(0,'#1a1a5a'),(1,'#5a3ab8')])
b+=rays(400,300,30,'#fff',.15,6)+glow(400,300,160,'#ffe0ff',.5)+ring(400,300,130,'#fff',12)
b+=''.join(f'<path d="M{400+260*math.cos(math.radians(a)):.0f} 800 L{400+150*math.cos(math.radians(a)):.0f} {300+150*math.sin(math.radians(a))+60:.0f}" stroke="#0a0a2a" stroke-width="26" stroke-linecap="round"/>' for a in range(20,170,25))+'<rect y="700" width="800" height="100" fill="#0a0a2a"/>'
I[1008]=svg(b,d)

# 1070 逢いたい: a lone figure on a night pier looking at the lights of a far shore across dark water
d,b=bg([(0,'#0a1028'),(1,'#1a2a50')])
b+=starsf(40,1070,360)+skyline(420,'#1a2440',1070,40,110,'#ffd27a',60)+'<rect y="420" width="800" height="380" fill="#0a1430"/>'+''.join(f'<rect x="{60+k*90}" y="{440+k%3*20}" width="40" height="3" fill="#ffd27a" opacity=".5"/>' for k in range(8))
b+='<rect x="-10" y="640" width="440" height="20" fill="#2a2a34"/>'+''.join(f'<rect x="{k*100+20}" y="660" width="14" height="140" fill="#2a2a34"/>' for k in range(5))+figure(380,640,220,'#000')
I[1070]=svg(b,d)

# 1257 「生きろ」: a small green sprout breaking through dark asphalt toward a single ray of light
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<polygon points="360,0 440,0 470,600 330,600" fill="#fff6c8" opacity=".25"/><rect y="580" width="800" height="220" fill="#2a2a2e"/>'+bolt([(400,580),(380,640),(420,700),(390,800)],'#141418',8)
b+='<path d="M400 600 Q395 520 400 470" stroke="#4ac84a" stroke-width="10" fill="none"/><path d="M400 520 Q340 480 330 440 Q380 450 400 510Z M400 490 Q460 450 480 410 Q420 420 400 480Z" fill="#5ad85a"/>'
I[1257]=svg(b,d)

# 1373 承認欲求: a figure surrounded by floating like-heart counters and smartphone frames, cold neon
d,b=bg([(0,'#0a0a14'),(1,'#1a1a30')])
r=random.Random(1373)
for _ in range(9):
    x=r.randint(80,720);y=r.randint(80,560)
    b+=f'<rect x="{x-40}" y="{y-24}" width="80" height="48" rx="16" fill="#ff2a6a" opacity=".85"/>'+heart(x-16,y,12,'#fff')+txt(x+16,y+10,str(r.randint(1,99)),26,'#fff')
b+=figure(400,760,380,'#000')+glow(400,500,120,'#6a8aff',.25)
I[1373]=svg(b,d)

# 228 時代: an hourglass with the sand of seasons flowing, sun and moon on either side
d,b=bg([(0,'#d8c8a8'),(1,'#8a7a6a')])
b+=hinomaru_sun(160,200,60,'#e8402a')+moon(640,200,50)
b+='<rect x="280" y="140" width="240" height="24" fill="#5a3a2a"/><rect x="280" y="640" width="240" height="24" fill="#5a3a2a"/><path d="M300 164 L500 164 Q500 300 410 400 Q500 500 500 640 L300 640 Q300 500 390 400 Q300 300 300 164Z" fill="#e8f4fa" opacity=".7" stroke="#8a7a6a" stroke-width="4"/>'
b+='<path d="M330 250 L470 250 Q460 320 400 380 Q340 320 330 250Z" fill="#e8b860"/><path d="M398 400 L402 400 L402 560 L398 560Z" fill="#e8b860"/><path d="M320 640 Q400 540 480 640Z" fill="#e8b860"/>'
I[228]=svg(b,d)

# 273 時間よ止まれ: a frozen splash of a wave on a summer beach with a stopped wristwatch in the sand, 70s sunlight
d,b=bg([(0,'#3aa8e8'),(1,'#b8e8ff')])
b+=hinomaru_sun(620,140,70,'#fff6c8')+'<rect y="400" width="800" height="200" fill="#1a7ab8"/><path d="M-10 600 L810 560 L810 810 L-10 810Z" fill="#f0d8a0"/>'
b+='<path d="M160 520 Q260 300 380 420 Q330 380 300 460 Q260 420 220 520Z" fill="#fff" opacity=".9"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#fff"/>' for x,y,r2 in [(240,300,10),(290,260,7),(340,300,8),(200,340,6)])
b+='<g transform="rotate(-15 480 660)"><rect x="380" y="645" width="200" height="30" rx="8" fill="#3a2a1a"/><circle cx="480" cy="660" r="46" fill="#c8c8d0"/><circle cx="480" cy="660" r="36" fill="#fff"/><path d="M480 660 L480 632 M480 660 L500 668" stroke="#1a1a1a" stroke-width="4"/></g>'
I[273]=svg(b,d)

# 490 STAY: a leather jacket hung on a chair under a single bulb, a closed door with light leaking beneath
d,b=bg([(0,'#1a1414'),(1,'#2a2020')])
b+='<path d="M400 0 L400 120" stroke="#3a3a3a" stroke-width="4"/><circle cx="400" cy="140" r="22" fill="#ffe8a0"/>'+glow(400,180,240,'#ffd27a',.35)+'<rect y="660" width="800" height="140" fill="#140e0e"/>'
b+='<rect x="540" y="200" width="200" height="460" fill="#2a1e1a" stroke="#3a2a24" stroke-width="10"/><rect x="540" y="652" width="200" height="8" fill="#ffd27a"/>'
b+='<path d="M200 700 L200 520 L360 520 L360 700 M200 420 L200 520 M360 420 L360 520" stroke="#4a3020" stroke-width="16" fill="none"/><path d="M190 420 L370 420 L380 560 L330 600 L280 520 L230 600 L180 560Z" fill="#0a0a0a"/>'
I[490]=svg(b,d)

# 491 VIRGIN BEAT: a motorcycle headlight streak and a heartbeat line racing across a black night road
d,b=bg([(0,'#050508'),(1,'#141420')])
b+='<path d="M0 420 L240 420 L280 300 L330 560 L380 360 L420 420 L800 420" stroke="#ff2a4a" stroke-width="10" fill="none"/>'+glow(330,420,120,'#ff2a4a',.25)
b+='<path d="M0 640 L800 600 L800 800 L0 800Z" fill="#1a1a24"/>'+''.join(f'<path d="M{k*140} {636-k*5} L{k*140+70} {632-k*5}" stroke="#ffd02a" stroke-width="5"/>' for k in range(6))
b+='<polygon points="640,560 80,520 80,600" fill="#fff6d8" opacity=".2"/><circle cx="660" cy="560" r="24" fill="#fff6d8"/>'
I[491]=svg(b,d)

# 549 恋一夜: two silhouettes embracing behind a translucent curtain, a crescent moon and a single lamp
d,b=bg([(0,'#2a0a2a'),(1,'#5a1a4a')])
b+=moon(620,180,60)+glow(400,440,200,'#ff8ab8',.3)
b+='<g fill="#120414"><circle cx="370" cy="330" r="34"/><circle cx="430" cy="320" r="34"/><path d="M320 700 Q320 420 370 380 Q400 370 430 370 Q480 420 480 700Z"/></g>'
b+=''.join(f'<path d="M{x} 0 Q{x+20} 400 {x} 800" stroke="#ffd8f0" stroke-width="40" fill="none" opacity=".12"/>' for x in range(40,800,70))
I[549]=svg(b,d)

# 667 永遠の翼: a pair of great white wings unfurling over a dawn horizon
d,b=bg([(0,'#3a5aa8'),(.6,'#f0a07a'),(1,'#ffe0b8')])
b+=hinomaru_sun(400,560,100,'#fff4d0')+'<rect y="600" width="800" height="200" fill="#5a4a6a"/>'
for s in (-1,1):
    b+=''.join(f'<path d="M400 420 Q{400+s*(120+k*50)} {300-k*30} {400+s*(200+k*55)} {200+k*40} Q{400+s*(140+k*40)} {380-k*10} 400 440Z" fill="#fff" opacity="{.95-k*.12:.2f}"/>' for k in range(5))
I[667]=svg(b,d)

# 728 Another Orion: the Orion constellation drawn in the winter sky over snowy rooftops, a second faint copy beside it
d,b=bg([(0,'#050a24'),(1,'#1a2a50')])
b+=starsf(60,728,560)
P=[(300,160),(420,150),(330,300),(360,305),(390,300),(290,440),(440,430)]
b+=''.join(f'<path d="M{P[a][0]} {P[a][1]} L{P[c][0]} {P[c][1]}" stroke="#a8c8ff" stroke-width="3" opacity=".7"/>' for a,c in [(0,2),(1,4),(2,3),(3,4),(2,5),(4,6)])+''.join(sparkle(x,y,16,'#fff') for x,y in P)
b+=''.join(f'<circle cx="{x+240}" cy="{y+60}" r="4" fill="#fff" opacity=".4"/>' for x,y in P)
b+='<path d="M-10 640 L120 580 L250 640 L380 570 L520 640 L660 580 L810 640 L810 810 L-10 810Z" fill="#e8eef8"/>'+''.join(f'<rect x="{x}" y="{y}" width="30" height="24" fill="#ffd27a"/>' for x,y in [(110,660),(370,650),(650,660)])
I[728]=svg(b,d)

# 745 Everything: a heart-shaped wreath made of everyday small things (a cup, a key, a flower, a note) on cream
d,b=bg([(0,'#fff4e0'),(1,'#f0dcc0')])
for k in range(24):
    a=k/24*2*math.pi;x=400+16*math.sin(a)**3*14;y=380-(13*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)-math.cos(4*a))*14
    c=['#e8504a','#ffb02a','#5ab85a','#3a8af8','#b85ae8'][k%5]
    b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{c}"/>' if k%3 else flower(x,y,24,5,c,'#fff')
b+=note(370,400,1.4,'#8a5a3a')+heart(440,380,30,'#e8504a')
I[745]=svg(b,d)

# 903 Go! Go! Heaven: four girls' silhouettes jumping on a trampoline-like cloud into a rainbow sky
d,b=bg([(0,'#ff9ae0'),(1,'#9ad8ff')])
b+=''.join(f'<path d="M-50 700 A450 450 0 0 1 850 700" stroke="{c}" stroke-width="28" fill="none" opacity=".7" transform="translate(0 {k*28})"/>' for k,c in enumerate(['#ff4a4a','#ffa02a','#ffe02a','#4ad84a','#3a8af8','#a84af8']))
b+=cloud(400,700,4,'#fff')+''.join(figure(x,y,190,'#2a1a3a',pose='up') for x,y in [(220,500),(340,440),(460,460),(580,510)])
I[903]=svg(b,d)

# 906 Give me a Shake: a cocktail shaker mid-shake with neon drops flying, dance floor lights
d,b=bg([(0,'#1a0a3a'),(1,'#4a0a5a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="{c}" opacity=".35"/>' for x,y,r2,c in [(120,160,80,'#ff4fa0'),(680,220,100,'#4ad8ff'),(160,640,90,'#ffd02a'),(660,640,70,'#ff4fa0')])
b+='<g transform="rotate(-25 400 420)"><rect x="330" y="300" width="140" height="280" rx="30" fill="#d8dce8"/><path d="M340 300 Q400 230 460 300Z" fill="#c8ccd8"/><rect x="380" y="220" width="40" height="40" rx="10" fill="#c8ccd8"/><rect x="330" y="400" width="140" height="20" fill="#ff4fa0"/></g>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="{c}"/>' for x,y,c in [(560,240,'#4ad8ff'),(600,300,'#ff4fa0'),(220,520,'#ffd02a'),(250,600,'#4ad8ff')])
I[906]=svg(b,d)

# 1067 夏色: a boy riding a bicycle down a long steep slope toward a glittering summer sea, the brakes squeaking
d,b=bg([(0,'#2ab0ff'),(.5,'#a8e8ff'),(1,'#2a8ad8')])
b+=cloud(220,160,1.6)+'<rect y="400" width="800" height="200" fill="#1a8ad8"/>'+''.join(sparkle(x,440+(x*7)%80,12,'#fff') for x in range(60,800,110))
b+='<path d="M-10 420 L810 760 L810 810 L-10 810Z" fill="#8a8a8a"/><path d="M-10 380 L810 720 L810 760 L-10 420Z" fill="#5ab84a"/>'
b+='<g transform="rotate(23 420 560)">'+''.join(ring(x,600,46,'#000',8) for x in (340,500))+'<path d="M340 600 L400 520 L500 600 M400 520 L480 520 L500 600" stroke="#000" stroke-width="8" fill="none"/><g fill="#000"><circle cx="430" cy="420" r="22"/><path d="M410 446 L450 446 L470 520 L400 520Z"/></g></g>'
I[1067]=svg(b,d)

# 1109 VICTORY: a golden V-shaped beam of light rising from a stadium with confetti
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=confetti(50,1109,['#ffd02a','#fff','#e8302a'])+'<polygon points="400,700 140,120 230,120 400,560 570,120 660,120" fill="#ffd02a"/>'+glow(400,420,200,'#ffd02a',.3)
b+='<path d="M-10 700 Q400 640 810 700 L810 810 L-10 810Z" fill="#14141e"/>'+''.join(f'<circle cx="{x}" cy="{700-((x*13)%30)}" r="12" fill="#000"/>' for x in range(20,800,40))
I[1109]=svg(b,d)

# 1236 Your Eyes: a large eye whose iris reflects a starry sky and a small silhouette of two people
d,b=bg([(0,'#1a1a3a'),(1,'#3a3a6a')])
b+='<path d="M80 400 Q400 120 720 400 Q400 680 80 400Z" fill="#f4f0e8"/><circle cx="400" cy="400" r="150" fill="#1a3a7a"/>'+''.join(f'<circle cx="{400+r2*math.cos(a)}" cy="{400+r2*math.sin(a)}" r="3" fill="#fff"/>' for r2,a in [(60,.3),(100,1.2),(120,2.2),(80,3.3),(110,4.4),(40,5.1),(130,5.8)])
b+='<circle cx="400" cy="400" r="50" fill="#0a0a14"/>'+figure(388,430,40,'#ffd27a')+figure(412,430,38,'#ffd27a')+'<ellipse cx="450" cy="350" rx="24" ry="16" fill="#fff" opacity=".8"/>'
I[1236]=svg(b,d)

# 1310 上からマリコ: a tall pedestal under a spotlight with a crown hovering over it, many small silhouettes looking up
d,b=bg([(0,'#2a0a3a'),(1,'#5a1a5a')])
b+='<polygon points="400,0 320,520 480,520" fill="#fff6d8" opacity=".2"/><rect x="330" y="420" width="140" height="300" fill="#e8d8f0"/>'+'<path d="M350 380 L370 330 L400 370 L430 330 L450 380Z" fill="#ffd02a"/>'+glow(400,360,80,'#ffd02a',.5)
b+=''.join(f'<g fill="#140418"><circle cx="{x}" cy="{690-((x*7)%20)}" r="18"/><path d="M{x-20} 800 L{x-16} {714-((x*7)%20)} L{x+16} {714-((x*7)%20)} L{x+20} 800Z"/></g>' for x in list(range(40,320,46))+list(range(500,800,46)))
I[1310]=svg(b,d)

# 1353 ビリヤニ: a steaming pot of spiced rice with saffron colours, dancers' silhouettes in the steam
d,b=bg([(0,'#ffb02a'),(1,'#e8602a')])
b+=''.join(f'<path d="M{x} 380 Q{x-30} 300 {x} 220 Q{x+30} 150 {x} 80" stroke="#fff" stroke-width="10" fill="none" opacity=".4"/>' for x in (320,400,480))
b+='<ellipse cx="400" cy="420" rx="230" ry="50" fill="#f8e070"/>'+''.join(f'<ellipse cx="{240+(k*53)%320}" cy="{405+(k*17)%30}" rx="9" ry="4" fill="{["#fff","#ffa02a","#e8402a"][k%3]}"/>' for k in range(30))
b+='<path d="M170 420 Q170 660 400 680 Q630 660 630 420Z" fill="#8a4a2a"/><path d="M140 420 L660 420" stroke="#6a3a1a" stroke-width="16"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="#4ac84a"/>' for x,y in [(300,410),(470,404),(380,396)])
I[1353]=svg(b,d)

# 1442 再会: two hands reaching to touch fingertips across a field of drifting light petals
d,b=bg([(0,'#2a1a4a'),(1,'#7a5aa8')])
b+=petals(30,1442,'#fff0c8',0,800,6,12,.6)+glow(400,400,90,'#fff2c8',.7)
b+='<g fill="#f0c8b0" stroke="#c8a088" stroke-width="5"><path d="M-10 480 L280 420 Q340 400 380 400 Q392 410 376 420 L300 450 L-10 540Z"/><path d="M810 360 L520 380 Q460 390 420 400 Q408 392 424 382 L500 350 L810 300Z"/></g>'
I[1442]=svg(b,d)

# 1588 よふかしのうた: a figure sitting on a vending machine roof in a sleeping town at 3 a.m., a moon and a cat
d,b=bg([(0,'#0a0a24'),(1,'#1a1a40')])
b+=moon(620,140,60)+starsf(30,1588,400)+skyline(640,'#0e0e22',1588,30,160,'#ffd27a',30)+'<rect y="640" width="800" height="160" fill="#14142a"/>'
b+='<rect x="280" y="420" width="180" height="260" fill="#e8e8f0"/><rect x="300" y="440" width="140" height="120" fill="#9ad8ff"/>'+''.join(f'<rect x="{306+k*34}" y="{450+r2*36}" width="26" height="28" fill="{["#ff4a4a","#ffd02a","#4ac84a","#fff"][k]}"/>' for k in range(4) for r2 in range(3))+glow(370,500,140,'#9ad8ff',.35)
b+='<g fill="#000"><circle cx="370" cy="356" r="20"/><path d="M350 380 L392 380 L400 420 L344 420Z"/><path d="M360 420 L340 470 M384 420 L404 470" stroke="#000" stroke-width="12"/></g><g fill="#000"><ellipse cx="520" cy="670" rx="26" ry="16"/><circle cx="542" cy="650" r="12"/><path d="M534 640 L538 628 L546 638Z M548 640 L554 628 L556 642Z"/></g>'
I[1588]=svg(b,d)

# 335 Remember Summer Days: a vintage convertible parked by palm trees on a seaside road, a city-pop pastel sunset
d,b=bg([(0,'#ff8ab8'),(.6,'#ffc8a0'),(1,'#9ae0ff')])
b+=hinomaru_sun(400,400,110,'#fff0c8',.9)+'<rect y="430" width="800" height="120" fill="#5ab8e8"/><rect y="550" width="800" height="250" fill="#4a4a5a"/>'
for x in (100,690): b+=f'<path d="M{x} 560 Q{x+10} 400 {x-10} 260" stroke="#2a1a2a" stroke-width="14" fill="none"/>'+''.join(f'<path d="M{x-10} 260 Q{x-10+dx} {260+dy} {x-10+dx*2} {280+dy*2}" stroke="#2a1a2a" stroke-width="10" fill="none"/>' for dx,dy in [(50,-10),(-50,-10),(40,30),(-40,30)])
b+='<path d="M220 640 L260 590 L420 580 L470 610 L580 620 L590 670 L210 670Z" fill="#e8f0f8"/>'+''.join(f'<circle cx="{x}" cy="672" r="30" fill="#1a1a1a"/>' for x in (290,520))
I[335]=svg(b,d)

# 409 卒業-GRADUATION-: a graduation certificate tube tied with a red ribbon on a classroom desk, cherry petals at the window
d,b=bg([(0,'#d8eef8'),(1,'#f4f0e8')])
b+='<rect x="440" y="80" width="300" height="300" fill="#a8d8f8"/><path d="M590 80 L590 380 M440 230 L740 230" stroke="#fff" stroke-width="12"/>'+petals(14,409,'#ffc2d6',80,380,8,14)
b+='<rect y="480" width="800" height="320" fill="#c8a070"/><g transform="rotate(-15 380 560)"><rect x="200" y="530" width="360" height="60" rx="30" fill="#1a1a2a"/><path d="M380 530 L380 590" stroke="#e8302a" stroke-width="16"/><path d="M380 560 L340 620 M380 560 L420 620" stroke="#e8302a" stroke-width="10"/></g>'
I[409]=svg(b,d)

# 801 Sa Yo Na Ra: a frosted car window with a finger-written goodbye line, city lights blurred behind
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=''.join(f'<circle cx="{(k*97)%800}" cy="{200+(k*61)%400}" r="{20+k%3*14}" fill="{["#ffd27a","#ff8ab8","#9ad8ff"][k%3]}" opacity=".3"/>' for k in range(24))
b+='<rect x="60" y="60" width="680" height="560" rx="40" fill="#e8f0f8" opacity=".35"/><path d="M200 340 Q260 280 320 340 T440 340 T560 330" stroke="#1a2a4a" stroke-width="12" fill="none" opacity=".6" stroke-linecap="round"/>'+''.join(f'<path d="M{x} 350 L{x} {380+(x*3)%40}" stroke="#e8f0f8" stroke-width="4" opacity=".6"/>' for x in (260,380,500))
b+='<rect y="620" width="800" height="180" fill="#0a0a14"/>'
I[801]=svg(b,d)

# 1060 カブトムシ: a rhinoceros beetle on a tree trunk in summer twilight, fireflies around
d,b=bg([(0,'#2a2a5a'),(1,'#7a5a7a')])
b+='<rect x="300" y="0" width="200" height="800" fill="#5a3a2a"/>'+''.join(f'<path d="M{310+k*30} 0 Q{320+k*30} 400 {305+k*30} 800" stroke="#4a2e20" stroke-width="5" fill="none"/>' for k in range(6))
b+='<ellipse cx="400" cy="440" rx="70" ry="100" fill="#3a1a0a"/><ellipse cx="400" cy="320" rx="46" ry="40" fill="#2a1408"/><path d="M400 290 Q390 210 430 180 Q420 230 410 290Z" fill="#2a1408"/><path d="M400 340 L400 540" stroke="#1a0a04" stroke-width="4"/><ellipse cx="380" cy="420" rx="16" ry="40" fill="#5a2a14" opacity=".6"/>'
b+=''.join(f'<path d="M{400+s*60} {y} L{400+s*110} {y+30}" stroke="#2a1408" stroke-width="8"/>' for s in (-1,1) for y in (380,440,500))+''.join(glow(x,y,18,'#e8ff8a',.8)+f'<circle cx="{x}" cy="{y}" r="5" fill="#f4ffb0"/>' for x,y in [(140,300),(660,240),(620,560),(180,600)])
I[1060]=svg(b,d)

# 1237 To be free: a birdcage door open on a hilltop, a bird flying out into a wide blue sky
d,b=bg([(0,'#4ab0ff'),(1,'#e0f6ff')])
b+=cloud(560,180,1.6)+'<path d="M-10 640 Q400 580 810 640 L810 810 L-10 810Z" fill="#6ac84a"/>'
b+='<path d="M220 640 L220 440 Q300 340 380 440 L380 640" stroke="#c8a24a" stroke-width="6" fill="none"/>'+''.join(f'<path d="M{x} 640 L{x} {440-int(60*math.sin(math.pi*(x-220)/160))}" stroke="#c8a24a" stroke-width="4"/>' for x in range(244,380,24))+'<path d="M220 640 L380 640" stroke="#c8a24a" stroke-width="10"/><path d="M380 500 L460 470 L460 600 L380 620Z" fill="none" stroke="#c8a24a" stroke-width="5"/>'
b+=bird(560,320,2.6,'#fff',4)+bird(640,260,1.6,'#fff',3)
I[1237]=svg(b,d)

# 1354 今、話したい誰かがいる: a girl on a train-station bench with a phone held to her chest, autumn leaves and a waiting figure across the tracks
d,b=bg([(0,'#f8b880'),(1,'#ffe8c8')])
b+='<rect y="500" width="800" height="300" fill="#8a8a94"/><path d="M0 600 L800 600 M0 640 L800 640" stroke="#5a5a64" stroke-width="6"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="7" fill="#e8602a" transform="rotate(30 {x} {y})"/>' for x,y in [(160,200),(300,140),(520,240),(640,180),(420,320)])
b+='<rect x="120" y="440" width="240" height="20" fill="#6a4a3a"/><rect x="130" y="460" width="10" height="40" fill="#6a4a3a"/><rect x="340" y="460" width="10" height="40" fill="#6a4a3a"/>'+'<g fill="#2a1a2a"><circle cx="240" cy="350" r="24"/><path d="M216 376 L264 376 L272 440 L208 440Z"/></g>'+'<rect x="232" y="390" width="16" height="26" rx="3" fill="#9ad8ff"/>'+figure(600,500,180,'#5a4a5a')
I[1354]=svg(b,d)

# 1382 ソンナコトナイヨ: a girl shaking her head with a cheerful speech bubble, bright yellow-green pop background
d,b=bg([(0,'#d8f05a'),(1,'#f8ffc8')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" opacity=".7"/>' for x in range(40,800,80) for y in range(40,800,80))
b+='<rect x="420" y="150" width="320" height="150" rx="75" fill="#fff" stroke="#5ab83a" stroke-width="8"/><path d="M470 290 L430 360 L520 296Z" fill="#fff" stroke="#5ab83a" stroke-width="8"/>'+txt(580,250,'NO NO!',60,'#5ab83a',900)
b+=figure(300,760,440,'#2a3a1a',hair='#2a3a1a')+'<path d="M240 300 Q220 290 210 300 M360 300 Q380 290 390 300" stroke="#2a3a1a" stroke-width="6" fill="none"/>'
I[1382]=svg(b,d)

# 1408 DADA: a child's crayon scribble of a raging face and stomping feet, angular red and black strokes
d,b=bg([(0,'#f4f0e8'),(1,'#e0dcd0')])
r=random.Random(1408)
b+=''.join(f'<path d="M{r.randint(40,760)} {r.randint(40,760)} L{r.randint(40,760)} {r.randint(40,760)}" stroke="{["#e8102a","#1a1a1a"][k%2]}" stroke-width="{r.randint(4,12)}" opacity=".5" stroke-linecap="round"/>' for k in range(30))
b+=txt(400,470,'DADA',190,'#1a1a1a',900)+'<path d="M140 520 L660 520" stroke="#e8102a" stroke-width="16"/>'
I[1408]=svg(b,d)

# 116 微笑がえし: three girls' silhouettes waving goodbye on a stage, confetti and an open moving box with a ribbon
d,b=bg([(0,'#ffc8d8'),(1,'#fff0e0')])
b+=confetti(40,116,['#ff6a8a','#ffd02a','#6ac8ff'])+'<rect y="600" width="800" height="200" fill="#d8a080"/>'
b+=figure(260,640,260,'#5a2a3a',pose='wave')+figure(400,640,270,'#5a2a3a',pose='wave')+figure(540,640,260,'#5a2a3a',pose='wave')
b+='<rect x="600" y="620" width="140" height="100" fill="#c89060"/><path d="M600 620 L560 580 L700 580 L740 620Z" fill="#d8a070"/><path d="M670 620 L670 720" stroke="#e8302a" stroke-width="10"/>'
I[116]=svg(b,d)

# 1110 real world: a hand holding a VR headset away to reveal a real sunrise over a city
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b8')])
b+=hinomaru_sun(400,460,110,'#fff2c8')+skyline(560,'#5a3a4a',1110,40,200,None)+'<rect y="560" width="800" height="240" fill="#3a2a3a"/>'
b+='<rect x="160" y="180" width="300" height="140" rx="40" fill="#1a1a24"/><rect x="190" y="210" width="110" height="80" rx="20" fill="#2a8af8" opacity=".6"/><rect x="320" y="210" width="110" height="80" rx="20" fill="#2a8af8" opacity=".6"/><path d="M160 250 L80 300" stroke="#1a1a24" stroke-width="20"/>'
b+='<path d="M80 300 Q40 340 60 400 L140 380 Q120 340 140 320Z" fill="#e8b098"/>'
I[1110]=svg(b,d)

# 1140 Re:Re:: an old mail envelope with a reply arrow looping back, a sunset street of power lines
d,b=bg([(0,'#e88a5a'),(1,'#ffd8a8')])
b+=''.join(f'<path d="M-10 {160+k*24} Q400 {220+k*24} 810 {150+k*24}" stroke="#2a1a1a" stroke-width="3" fill="none"/>' for k in range(3))+'<rect x="120" y="100" width="14" height="500" fill="#2a1a1a"/><rect x="660" y="90" width="14" height="510" fill="#2a1a1a"/>'
b+='<rect x="230" y="380" width="340" height="220" fill="#fbf6ea" stroke="#8a6a4a" stroke-width="5"/><path d="M230 380 L400 500 L570 380" stroke="#8a6a4a" stroke-width="5" fill="none"/>'
b+='<path d="M520 340 Q620 260 560 200 Q500 160 440 220" stroke="#e8302a" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M420 200 L450 250 L470 200Z" fill="#e8302a"/>'
I[1140]=svg(b,d)

# 1871 366日: a wall calendar with one extra square circled in red, a dried flower tucked beside it
d,b=bg([(0,'#e8e4dc'),(1,'#d0c8bc')])
b+='<rect x="160" y="120" width="480" height="560" fill="#fff" stroke="#c8c0b0" stroke-width="5"/><rect x="160" y="120" width="480" height="90" fill="#3a5a8a"/>'+txt(400,190,'366',70,'#fff',900)
b+=''.join(f'<rect x="{190+(k%7)*62}" y="{240+(k//7)*72}" width="52" height="60" fill="#f0eeea"/>' for k in range(35))+ring(190+6*62+26,240+4*72+30,38,'#e8102a',8)
b+='<path d="M600 700 L680 420" stroke="#6a7a4a" stroke-width="5"/>'+flower(680,410,26,6,'#c8a0b0','#e8d0a0')
I[1871]=svg(b,d)

# 159 おもいで酒: a sake bottle and a small cup on a counter in a dim izakaya, a red lantern behind
d,b=bg([(0,'#2a1410'),(1,'#140a08')])
b+=chochin(600,220,1,'#d8342c','#ffb070','酒')+glow(400,500,240,'#ffb070',.2)+'<rect y="560" width="800" height="240" fill="#5a3a20"/><rect y="550" width="800" height="16" fill="#7a4a2a"/>'
b+='<path d="M300 560 L300 400 Q300 360 330 340 L330 290 L370 290 L370 340 Q400 360 400 400 L400 560Z" fill="#f4ead8"/><rect x="310" y="430" width="80" height="80" fill="#2a3a5a"/>'+txt(350,486,'酒',50,'#fff')
b+='<path d="M450 560 L440 500 L520 500 L510 560Z" fill="#f4ead8"/><ellipse cx="480" cy="502" rx="40" ry="8" fill="#e8d8a0"/>'
I[159]=svg(b,d)

# 746 Fake: a smiling theatre mask with a crack revealing darkness behind, a glitchy green tint
d,b=bg([(0,'#0a1410'),(1,'#1a2a20')])
b+=''.join(f'<rect x="0" y="{y}" width="800" height="3" fill="#3aff8a" opacity=".1"/>' for y in range(0,800,12))
b+='<path d="M240 200 Q400 140 560 200 Q600 420 400 620 Q200 420 240 200Z" fill="#f4f0e8"/><path d="M300 320 Q330 290 360 320 M440 320 Q470 290 500 320" stroke="#1a1a1a" stroke-width="12" fill="none"/><path d="M320 440 Q400 520 480 440" stroke="#1a1a1a" stroke-width="12" fill="none"/>'
b+='<path d="M400 160 L380 260 L420 330 L380 420 L410 520 L400 620" stroke="#0a1410" stroke-width="16" fill="none"/>'
I[746]=svg(b,d)

# 802 wanna Be A Dreammaker: a figure building a staircase of glowing blocks into a starry night sky
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a5a')])
b+=starsf(60,802,600)+moon(640,140,40)
for k in range(7): b+=f'<rect x="{80+k*90}" y="{660-k*70}" width="90" height="{140+k*70}" fill="#4ad8ff" opacity="{.25+k*.08:.2f}" stroke="#9af0ff" stroke-width="3"/>'
b+=figure(170+5*90,660-5*70,180,'#000',pose='reach')
I[802]=svg(b,d)

# 1044 瞳をとじて: a woman's profile with eyes closed in a dark room, a single tear of light and a falling star outside
d,b=bg([(0,'#0a0e24'),(1,'#1a2240')])
b+=starsf(30,1044,400)+'<path d="M600 120 L520 200" stroke="#fff" stroke-width="3"/>'+profile(360,420,1.6,'#05070f')+'<path d="M412 400 Q430 420 412 434 Q396 420 412 400Z" fill="#c8e8ff"/>'
I[1044]=svg(b,d)

# 1084 LOVE LOVE Summer: a beach umbrella and two heart-shaped sunglasses on bright sand by turquoise sea
d,b=bg([(0,'#3ad8f8'),(1,'#a8f4ff')])
b+=hinomaru_sun(640,120,60,'#fffbe0')+'<rect y="360" width="800" height="160" fill="#1ab8d8"/><path d="M-10 520 Q400 480 810 520 L810 810 L-10 810Z" fill="#ffe8a8"/>'
b+='<path d="M260 760 L300 380" stroke="#8a6a4a" stroke-width="8"/><path d="M120 420 Q300 220 480 380Z" fill="#ff4a8a"/><path d="M180 400 Q300 260 300 380 M420 390 Q340 250 300 380" stroke="#fff" stroke-width="6" fill="none"/>'
b+=heart(470,650,46,'#ff2a6a')+heart(590,650,46,'#ff2a6a')+'<path d="M510 640 Q530 628 550 640" stroke="#1a1a1a" stroke-width="6" fill="none"/>'
I[1084]=svg(b,d)

# 1124 雪の華: snow crystals blooming like flowers under a streetlight, a couple's silhouette walking away
d,b=bg([(0,'#1a2a50'),(1,'#4a5a8a')])
b+='<rect x="580" y="160" width="10" height="520" fill="#1a1a24"/><path d="M585 160 Q585 120 540 120" stroke="#1a1a24" stroke-width="10" fill="none"/><circle cx="540" cy="140" r="16" fill="#fff6d8"/><polygon points="540,150 420,680 660,680" fill="#fff6d8" opacity=".2"/>'
for x,y,s in [(200,200,40),(340,300,30),(160,420,26),(460,200,24),(300,520,22)]:
    b+=''.join(f'<path d="M{x} {y} L{x+s*math.cos(math.radians(a)):.0f} {y+s*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="4"/>' for a in range(0,360,60))+f'<circle cx="{x}" cy="{y}" r="{s/4}" fill="#fff"/>'
b+=snow(60,1124)+'<rect y="680" width="800" height="120" fill="#e8eef8"/>'+figure(480,700,170,'#0a0e20')+figure(520,700,180,'#0a0e20')
I[1124]=svg(b,d)

# 1156 ブルーバード: a bright blue bird bursting upward out of a cloud sea into an open sky
d,b=bg([(0,'#1a6ae8'),(1,'#9ad8ff')])
b+=cloud(200,620,3,'#fff')+cloud(600,640,3,'#fff')+cloud(400,700,3.4,'#fff')
b+='<path d="M400 300 Q470 260 520 300 Q480 320 460 360 Q430 380 400 360Z" fill="#1a4ab8"/><path d="M420 330 Q360 220 260 200 Q330 280 360 340Z" fill="#2a8af8"/><path d="M450 330 Q560 200 640 180 Q580 270 500 340Z" fill="#2a8af8"/><circle cx="500" cy="296" r="6" fill="#fff"/><path d="M520 300 L550 296 L522 310Z" fill="#ffb02a"/>'
b+='<path d="M400 360 Q360 450 380 560" stroke="#fff" stroke-width="6" fill="none" opacity=".5"/>'
I[1156]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
