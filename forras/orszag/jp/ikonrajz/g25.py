import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 25. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1241 キミの夢を見ていた: a figure asleep at a window with a dream bubble of a starry meeting place
d,b=bg([(0,'#1a1a4a'),(1,'#4a3a7a')])
b+=starsf(50,1241,500)+moon(620,140,44)+'<rect x="80" y="420" width="640" height="380" fill="#2a2a4a"/><rect x="140" y="520" width="520" height="40" fill="#e8e0f0"/>'
b+='<g fill="#0a0a1a"><circle cx="300" cy="500" r="30"/><path d="M320 500 L560 500 L560 524 L320 524Z"/></g>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85"/>' for x,y,r in [(340,440,10),(370,400,16)])
b+='<ellipse cx="460" cy="300" rx="140" ry="90" fill="#fff" opacity=".9"/>'+figure(420,350,90,'#4a3a7a')+figure(500,350,90,'#4a3a7a')+star5(460,250,14,'#ffd02a')
I[1241]=svg(b,d)

# 1314 ジワるDAYS: a calendar whose pages slowly peel away into a sunset, a girl leaning on a school desk
d,b=bg([(0,'#ffb08a'),(1,'#ffe8c8')])
b+=''.join(f'<g transform="rotate({k*9-20} 520 260)"><rect x="440" y="160" width="160" height="190" fill="#fff" stroke="#c8b8a8" stroke-width="3" opacity="{1-k*.15:.2f}"/><rect x="440" y="160" width="160" height="40" fill="#e8304a" opacity="{1-k*.15:.2f}"/></g>' for k in range(5))
b+='<rect x="100" y="560" width="360" height="24" fill="#a8784a"/><rect x="120" y="584" width="14" height="200" fill="#6a4a2a"/><rect x="426" y="584" width="14" height="200" fill="#6a4a2a"/>'+figure(260,800,360,'#2a1a2a')
I[1314]=svg(b,d)

# 1767 銃爪: a hand-drawn trigger-shaped lightning crack across a red-black rock stage, late-70s rock
d,b=bg([(0,'#1a0404'),(1,'#5a0a0a')])
b+='<polygon points="400,0 240,800 560,800" fill="#ff4a2a" opacity=".2"/>'+bolt([(420,60),(360,260),(440,300),(380,520)],'#ffd02a',12)
b+='<rect y="640" width="800" height="160" fill="#0a0202"/>'+figure(400,660,300,'#000',pose='hold')+'<path d="M330 520 L520 440" stroke="#000" stroke-width="16"/>'
I[1767]=svg(b,d)

# 367 チェリーブラッサム: a single cherry branch in full bloom against a clear spring sky, wind carrying petals
d,b=bg([(0,'#7ac8ff'),(1,'#e8f6ff')])
b+='<path d="M820 180 Q600 220 460 360 Q380 440 300 460" stroke="#5a3a2a" stroke-width="18" fill="none" stroke-linecap="round"/><path d="M560 260 Q520 180 460 160" stroke="#5a3a2a" stroke-width="10" fill="none"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffc2d6"/>' for x,y,r in [(320,450,30),(380,420,34),(460,360,36),(520,310,32),(600,250,34),(470,170,30),(520,210,28),(700,200,30)])+''.join(sakura(x,y,.5) for x,y in [(380,420),(460,360),(600,250),(470,170)])+petals(16,367,'#ffc2d6',100,700)
I[367]=svg(b,d)

# 368 小麦色のマーメイド: a tanned mermaid's silhouette on a rock at a tropical sunset, tail curling into the water
d,b=bg([(0,'#ff8a5a'),(.6,'#ffd08a'),(1,'#3aa8c8')])
b+=hinomaru_sun(560,300,80,'#fff2c8',.8)+'<rect y="460" width="800" height="340" fill="#2a8ab0"/><path d="M180 560 Q300 480 440 560Z" fill="#3a2a2a"/>'
b+='<g fill="#a8682a"><circle cx="300" cy="400" r="26"/><path d="M280 428 Q300 420 320 428 L330 520 L280 520Z"/><path d="M290 520 Q360 560 420 520 Q460 500 470 540 Q440 520 420 550 Q360 590 290 540Z"/></g><path d="M276 392 Q250 440 270 500" stroke="#3a1a0a" stroke-width="12" fill="none"/>'
I[368]=svg(b,d)

# 590 ENDLESS RAIN: rain falling endlessly on a grand piano in an empty dark hall, a single violet light
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=rain(90,590,'#a8a8ff',.45)+'<polygon points="400,0 240,700 560,700" fill="#8a6aff" opacity=".12"/>'
b+='<path d="M220 560 Q220 420 380 420 L580 420 Q620 420 620 480 L620 560Z" fill="#000"/><rect x="220" y="560" width="400" height="30" fill="#1a1a1a"/>'+''.join(f'<rect x="{230+k*20}" y="562" width="16" height="26" fill="#ddd"/>' for k in range(19))+'<path d="M250 590 L250 720 M590 590 L590 720" stroke="#000" stroke-width="12"/>'
I[590]=svg(b,d)

# 784 誕生日には真白な百合を: a bouquet of pure white lilies on a table by a window, a small birthday card
d,b=bg([(0,'#e8eef8'),(1,'#f8f4f0')])
b+='<rect x="500" y="80" width="220" height="320" fill="#d8e8f8" stroke="#b8c0d0" stroke-width="8"/><rect y="600" width="800" height="200" fill="#c8a888"/>'
b+='<path d="M360 600 L340 480 L460 480 L440 600Z" fill="#c8d8e8" opacity=".8"/>'+''.join(f'<path d="M400 480 L{x} {y}" stroke="#4a8a3a" stroke-width="6"/>' for x,y in [(320,320),(400,280),(480,330)])
for x,y in [(320,320),(400,280),(480,330)]: b+=''.join(f'<path d="M{x} {y} Q{x+40*math.cos(a):.0f} {y+40*math.sin(a):.0f} {x+70*math.cos(a):.0f} {y+70*math.sin(a):.0f} Q{x+40*math.cos(a+.5):.0f} {y+40*math.sin(a+.5):.0f} {x} {y}Z" fill="#fff" stroke="#d8d8e0" stroke-width="2"/>' for a in [k*1.05-1.6 for k in range(6)])
b+='<rect x="500" y="560" width="110" height="70" fill="#fff" transform="rotate(-8 555 595)"/>'+heart(555,595,14,'#e8607a')
I[784]=svg(b,d)

# 785 はつ恋: a boy's and girl's shadows almost touching on an evening school path, with a single cherry petal between them
d,b=bg([(0,'#f8b8a8'),(1,'#fff0e0')])
b+=hinomaru_sun(640,320,70,'#fff4d8',.7)+'<rect y="520" width="800" height="280" fill="#d8b8a0"/>'
b+=figure(320,560,260,'#3a2a3a')+figure(480,560,250,'#3a2a3a')+'<path d="M300 560 L120 740 L160 760 L320 570Z M470 560 L340 760 L380 770 L480 570Z" fill="#3a2a3a" opacity=".3"/>'+sakura(400,420,.6)
I[785]=svg(b,d)

# 871 LOVE FLIES: two white doves flying up into a shining sky over a cityscape at dawn
d,b=bg([(0,'#5aa8f0'),(1,'#ffe8c8')])
b+=glow(400,180,200,'#fff',.5)+skyline(600,'#4a5a7a',871,60,200,'#ffe8a0',30)
for x,y,s in [(320,340,1),(470,260,.85)]: b+=f'<g transform="translate({x} {y}) scale({s})" fill="#fff"><ellipse cx="0" cy="0" rx="50" ry="20"/><path d="M-10 -10 Q-60 -110 -120 -80 Q-60 -40 -20 0Z M10 -10 Q60 -110 120 -80 Q60 -40 20 0Z"/><circle cx="46" cy="-8" r="14"/></g>'
I[871]=svg(b,d)

# 984 Fight The Blues: a pair of boxing gloves hanging on a nail in a blue room, sun breaking through a window
d,b=bg([(0,'#1a3a6a'),(1,'#3a5a9a')])
b+='<rect x="480" y="100" width="220" height="280" fill="#ffe8a0"/>'+'<polygon points="480,100 700,100 800,800 300,800" fill="#ffe8a0" opacity=".12"/>'
b+='<circle cx="300" cy="200" r="8" fill="#888"/><path d="M300 200 L250 300 M300 200 L360 300" stroke="#eee" stroke-width="4"/>'
b+=''.join(f'<path d="M{x-50} 300 Q{x-60} 400 {x-20} 430 L{x+40} 430 Q{x+60} 360 {x+40} 300Z" fill="#e8302a"/><rect x="{x-40}" y="430" width="70" height="40" fill="#fff"/>' for x in (250,370))
I[984]=svg(b,d)

# 1058 Stay by my side: two silhouettes sitting side by side on a harbour wall at dusk, ships' lights in the water
d,b=bg([(0,'#3a3a6a'),(1,'#d89a8a')])
b+='<rect y="500" width="800" height="300" fill="#2a3a5a"/>'+''.join(f'<circle cx="{x}" cy="490" r="5" fill="#ffd27a"/><rect x="{x-2}" y="500" width="4" height="40" fill="#ffd27a" opacity=".4"/>' for x in (120,560,700))
b+='<rect x="160" y="560" width="480" height="240" fill="#4a4a5a"/>'+''.join(f'<g fill="#0a0a1a"><circle cx="{x}" cy="490" r="24"/><path d="M{x-24} 514 L{x+24} 514 L{x+28} 560 L{x-28} 560Z"/></g>' for x in (360,430))
I[1058]=svg(b,d)

# 86 星影のワルツ: a couple waltzing as silhouettes under a huge starry sky, late-60s soft blue
d,b=bg([(0,'#0a0a3a'),(1,'#3a4a8a')])
b+=starsf(160,86,600)+'<path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#0a0a2a"/>'
b+='<g fill="#000"><circle cx="370" cy="400" r="26"/><circle cx="440" cy="390" r="24"/><path d="M350 430 L400 430 L410 640 L360 640Z"/><path d="M420 420 L470 420 L520 640 L400 640Z"/><path d="M390 450 L450 430" stroke="#000" stroke-width="12"/></g>'
I[86]=svg(b,d)

# 672 GO FOR IT, BABY: a range of mountains drawn like memories (photo frames) with a runner charging up a ridge
d,b=bg([(0,'#4aa8ff'),(1,'#e8f4ff')])
b+='<path d="M-10 600 L160 340 L300 520 L460 260 L620 480 L810 300 L810 810 L-10 810Z" fill="#5a6a7a"/><path d="M420 320 L460 260 L500 320Z M780 340 L810 300 L810 350Z" fill="#fff"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="60" height="44" fill="#fff" stroke="#ddd" stroke-width="3" transform="rotate({a} {x+30} {y+22})"/>' for x,y,a in [(200,420,-8),(380,380,6),(560,440,-5)])+figure(460,262,120,'#1a1a1a',pose='up')
I[672]=svg(b,d)

# 750 優しい歌: a guitar leaning on a sunny wooden wall with a soft flower in a jar
d,b=bg([(0,'#f8e8c8'),(1,'#e8c898')])
b+=''.join(f'<rect x="{k*100}" y="0" width="96" height="620" fill="#d8a870" opacity=".5"/>' for k in range(8))+'<rect y="620" width="800" height="180" fill="#a8784a"/>'
b+=guitar(340,480,1.3,12,'#c8803a')+'<rect x="520" y="540" width="70" height="80" fill="#d8e8f0" opacity=".8"/>'+flower(555,470,30,6,'#ffd02a','#c87a1a')+'<path d="M555 480 L555 540" stroke="#4a8a3a" stroke-width="5"/>'
I[750]=svg(b,d)

# 766 春の歌: a lone figure walking along a railway with spring fields and a few blossoms, a soft green-blue palette
d,b=bg([(0,'#a8d8ff'),(1,'#f0f8e8')])
b+='<rect y="460" width="800" height="340" fill="#a8d888"/><path d="M360 460 L440 460 L700 800 L100 800Z" fill="#8a7a6a"/>'+''.join(f'<rect x="{400-(40+k*36)}" y="{480+k*44}" width="{80+k*72}" height="10" fill="#5a4a3a"/>' for k in range(7))
b+=''.join(f'<circle cx="{x}" cy="{y}" r="28" fill="#ffc2d6"/>' for x,y in [(120,420),(680,400),(720,440)])+figure(420,600,160,'#2a3a2a')
I[766]=svg(b,d)

# 1150 桜: a full cherry tree with a few people's silhouettes walking beneath it, petals over a riverbank
d,b=bg([(0,'#c8e0ff'),(1,'#fff0f4')])
b+='<rect x="380" y="380" width="40" height="300" fill="#5a3a2a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffc2d6"/>' for x,y,r in [(400,260,150),(270,330,100),(530,330,100),(330,190,90),(480,190,90)])
b+=''.join(sakura(x,y,.6) for x,y in [(340,260),(460,240),(400,320),(270,330),(530,330)])+'<rect y="660" width="800" height="140" fill="#b8d898"/>'+petals(18,1150,'#ffb8cc',300,780)+figure(220,720,160,'#2a2a3a')+figure(600,720,170,'#2a2a3a')
I[1150]=svg(b,d)

# 1315 UZA: a flashing industrial grid with sharp red slashes and a dancing silhouette mid-move
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a0a')])
b+=''.join(f'<path d="M{k*100} 0 L{k*100} 800 M0 {k*100} L800 {k*100}" stroke="#3a1a1a" stroke-width="2"/>' for k in range(9))
b+=''.join(f'<path d="M{x} {y} L{x+180} {y-120}" stroke="#ff1a3a" stroke-width="16" stroke-linecap="round"/>' for x,y in [(80,300),(500,260),(560,660)])
b+='<g transform="rotate(-12 400 600)">'+figure(400,740,400,'#fff',pose='reachL')+'</g>'
I[1315]=svg(b,d)

# 1359 ハルジオンが咲く頃: little white daisy-like fleabane flowers along a spring roadside, a girl's back walking away
d,b=bg([(0,'#d8ecff'),(1,'#fdf8f0')])
b+='<rect y="560" width="800" height="240" fill="#a8d888"/>'+figure(560,620,200,'#5a5a7a')
for x,y in [(120,620),(200,680),(300,640),(160,740),(380,720),(260,760),(460,760)]:
    b+=f'<path d="M{x} {y} L{x} 800" stroke="#5a9a4a" stroke-width="4"/>'+''.join(f'<ellipse cx="{x+18*math.cos(a):.0f}" cy="{y+18*math.sin(a):.0f}" rx="14" ry="4" fill="#fff" transform="rotate({math.degrees(a):.0f} {x+18*math.cos(a):.0f} {y+18*math.sin(a):.0f})"/>' for a in [k*.52 for k in range(12)])+f'<circle cx="{x}" cy="{y}" r="9" fill="#ffd02a"/>'
I[1359]=svg(b,d)

# 1375 I want tomorrow to come: a long night corridor of windows, the last one glowing with dawn and a figure reaching
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<path d="M0 0 L300 260 L500 260 L800 0Z M0 800 L300 540 L500 540 L800 800Z" fill="#14141f"/>'+'<rect x="300" y="260" width="200" height="280" fill="url(#dw)"/>'+glow(400,400,180,'#ffb88a',.4)
b+=figure(360,640,220,'#000',pose='reach')
d+=lg('dw',[(0,'#ff8a5a',1),(1,'#ffe8b8',1)])
I[1375]=svg(b,d)

# 1433 HAPPY: confetti and balloons bursting over seven dancing silhouettes in a sunny plaza
d,b=bg([(0,'#ffd02a'),(1,'#fff4c8')])
r=random.Random(1433)
b+=''.join(f'<rect x="{r.randint(0,780)}" y="{r.randint(0,500)}" width="14" height="8" fill="{r.choice(["#ff4a6a","#4ac8ff","#4ad84a","#a84aff"])}" transform="rotate({r.randint(0,180)} 400 300)"/>' for k in range(60))
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="34" ry="42" fill="{c}"/><path d="M{x} {y+42} L{x} {y+120}" stroke="#666" stroke-width="2"/>' for x,y,c in [(120,160,'#ff4a6a'),(680,140,'#4ac8ff')])
b+=''.join(figure(100+k*100,760,200,'#1a1a1a',pose=p) for k,p in enumerate(['up','wave','up','stand','up','wave','up']))
I[1433]=svg(b,d)

# 1660 ハナミズキ: a dogwood tree with pink-white four-petal flowers against a clear blue sky
d,b=bg([(0,'#5ab0ff'),(1,'#e8f6ff')])
b+='<path d="M400 800 L400 480 Q380 400 300 340 M400 480 Q440 380 540 320" stroke="#5a3a2a" stroke-width="22" fill="none" stroke-linecap="round"/>'
for x,y,c in [(260,300,'#ffd0dc'),(330,240,'#fff'),(420,300,'#ffd0dc'),(520,250,'#fff'),(600,320,'#ffd0dc'),(470,180,'#ffd0dc'),(200,400,'#fff'),(560,420,'#fff'),(350,380,'#ffd0dc')]:
    b+=''.join(f'<ellipse cx="{x+22*math.cos(a):.0f}" cy="{y+22*math.sin(a):.0f}" rx="24" ry="16" fill="{c}" stroke="#e8a8b8" stroke-width="2" transform="rotate({math.degrees(a):.0f} {x+22*math.cos(a):.0f} {y+22*math.sin(a):.0f})"/>' for a in [k*1.5708+.785 for k in range(4)])+f'<circle cx="{x}" cy="{y}" r="8" fill="#8ab84a"/>'
I[1660]=svg(b,d)

# 369 渚のバルコニー: a seaside balcony at dawn with a white railing and a pair of sandals, early 80s pastels
d,b=bg([(0,'#ffc8d8'),(1,'#d8f0ff')])
b+=hinomaru_sun(560,300,60,'#fff8e0')+'<rect y="360" width="800" height="200" fill="#6ac8e8"/>'+'<rect y="560" width="800" height="240" fill="#f4ece0"/>'
b+='<rect y="520" width="800" height="14" fill="#fff"/>'+''.join(f'<rect x="{x}" y="534" width="10" height="90" fill="#fff"/>' for x in range(20,800,50))+'<rect y="620" width="800" height="14" fill="#fff"/>'
b+='<ellipse cx="320" cy="720" rx="40" ry="16" fill="#ff8ab8"/><ellipse cx="400" cy="730" rx="40" ry="16" fill="#ff8ab8"/>'
I[369]=svg(b,d)

# 497 I LOVE YOU: a dim small room with a mattress and a single lamp, two silhouettes holding each other by the window
d,b=bg([(0,'#1a1424'),(1,'#3a2a3a')])
b+='<rect x="460" y="120" width="220" height="300" fill="#3a4a7a"/>'+moon(600,200,30)+glow(200,420,140,'#ffb870',.4)+'<path d="M180 420 L220 420 L240 480 L160 480Z" fill="#ffd8a0"/><rect x="196" y="480" width="8" height="120" fill="#5a4a3a"/>'
b+='<rect y="600" width="800" height="200" fill="#1a1018"/><g fill="#000"><circle cx="520" cy="430" r="28"/><circle cx="580" cy="440" r="26"/><path d="M490 460 L610 460 L620 640 L480 640Z"/></g>'
I[497]=svg(b,d)

# 512 ジュリアン: a girl's silhouette writing a farewell letter by a window in rainy night, purple neon city
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a5a')])
b+='<rect x="120" y="100" width="560" height="380" fill="#2a1a4a"/>'+skyline(480,'#140a24',512,40,220,'#ff8ad8',40)+rain(40,512,'#c8a8ff',.4)
b+='<rect x="80" y="560" width="640" height="20" fill="#5a3a5a"/>'+figure(300,800,300,'#000')+'<rect x="420" y="540" width="120" height="20" fill="#fff" transform="rotate(-6 480 550)"/>'
I[512]=svg(b,d)

# 952 心に夢を君には愛を: two hands offering a glowing heart and a star to each other across a night sky
d,b=bg([(0,'#1a2a5a'),(1,'#4a5a9a')])
b+=starsf(80,952,800)+heart(330,380,60,'#ff6a8a')+star5(470,380,60,'#ffd02a')+glow(330,380,90,'#ff6a8a',.4)+glow(470,380,90,'#ffd02a',.4)
b+='<g fill="#f0c8b0"><path d="M120 560 Q220 480 330 470 L340 500 Q240 520 160 600Z"/><path d="M680 560 Q580 480 470 470 L460 500 Q560 520 640 600Z"/></g>'
I[952]=svg(b,d)

# 1046 ノンフィクション: a person standing alone at a crossing under a streetlamp, real city grey, a single warm light
d,b=bg([(0,'#3a3a44'),(1,'#6a6a74')])
b+=skyline(500,'#2a2a34',1046,60,240,'#c8c8a0',30)+'<rect y="500" width="800" height="300" fill="#4a4a54"/>'+''.join(f'<rect x="{80+k*90}" y="620" width="60" height="120" fill="#e8e8e8" opacity=".6"/>' for k in range(8))
b+='<rect x="600" y="200" width="10" height="400" fill="#2a2a2a"/><rect x="560" y="190" width="70" height="16" fill="#2a2a2a"/>'+glow(580,220,120,'#ffd27a',.4)+figure(400,640,240,'#000')
I[1046]=svg(b,d)

# 1437 二千年... 若しくは... 二万年後の君へ: a vast ancient wall in ruins under a far-future sky, a tiny figure looking up
d,b=bg([(0,'#c8a080'),(1,'#f0e0c8')])
b+='<rect x="0" y="180" width="800" height="440" fill="#a8988a"/>'+''.join(f'<rect x="{(k%8)*100+(50 if (k//8)%2 else 0)}" y="{180+(k//8)*55}" width="96" height="51" fill="#b8a898"/>' for k in range(64))
b+='<path d="M300 180 L360 280 L330 380 L400 460 L380 620 L520 620 L480 480 L520 360 L470 260 L500 180Z" fill="#f0e0c8"/>'+'<rect y="620" width="800" height="180" fill="#8a7a6a"/>'+figure(440,700,90,'#1a1010')
I[1437]=svg(b,d)

# 1451 コイワズライ: a girl's silhouette lying on a bed tangled in a red string, a phone glowing beside her
d,b=bg([(0,'#2a1a2a'),(1,'#4a2a3a')])
b+='<rect x="80" y="480" width="640" height="200" rx="20" fill="#d8c8d8"/><g fill="#1a0a1a"><circle cx="200" cy="460" r="30"/><path d="M220 450 L560 470 L560 500 L220 490Z"/></g>'
b+='<path d="M240 470 Q300 380 360 470 Q420 560 480 450 Q540 360 600 480 Q620 520 660 500" stroke="#e8102a" stroke-width="5" fill="none"/><rect x="600" y="420" width="40" height="70" rx="6" fill="#4ad8ff"/>'+glow(620,455,70,'#4ad8ff',.4)
I[1451]=svg(b,d)

# 1592 ひゅるりらぱっぱ: a playful whirl of wind carrying a kite and leaves over a hill, cheerful flat colours
d,b=bg([(0,'#8ad8ff'),(1,'#f8fff0')])
b+='<path d="M-10 640 Q400 560 810 640 L810 810 L-10 810Z" fill="#6ac84a"/>'+''.join(f'<path d="M{100+k*60} {500-k*30} q60 -80 120 0 q30 40 -10 50" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round"/>' for k in range(4))
b+='<path d="M520 120 L600 200 L520 280 L440 200Z" fill="#ff6a4a"/><path d="M520 120 L520 280 M440 200 L600 200" stroke="#fff" stroke-width="3"/><path d="M520 280 Q480 360 520 420 Q560 480 400 640" stroke="#555" stroke-width="2" fill="none"/>'+figure(400,700,140,'#1a3a1a',pose='up')
I[1592]=svg(b,d)

# 157 心のこり: a lone woman's silhouette on an evening pier, gulls flying off over a grey sea, mid-70s enka
d,b=bg([(0,'#8a8aa0'),(1,'#d8c8c0')])
b+='<rect y="460" width="800" height="340" fill="#6a7a8a"/><rect x="-10" y="560" width="440" height="24" fill="#4a3a3a"/>'+figure(300,560,220,'#1a1a1a')
b+=''.join(f'<path d="M{x-20} {y} q10 -12 20 0 q10 -12 20 0" stroke="#fff" stroke-width="4" fill="none"/>' for x,y in [(520,240),(600,200),(660,260)])
I[157]=svg(b,d)

# 289 勝手にシンドバッド: a sun-blasted Shonan beach with a surfboard and a wild dancer, late-70s
d,b=bg([(0,'#ff8a2a'),(1,'#ffe08a')])
b+=hinomaru_sun(400,220,110,'#fff4c8')+rays(400,220,24,'#fff',.25,8)+'<rect y="440" width="800" height="120" fill="#2ab0d8"/><rect y="560" width="800" height="240" fill="#f4d8a0"/>'
b+='<rect x="560" y="420" width="50" height="260" rx="25" fill="#ff4a6a" transform="rotate(14 585 550)"/>'+figure(360,740,300,'#2a1a0a',pose='up')
I[289]=svg(b,d)

# 370 ハートのイアリング: a single heart-shaped earring glinting on a pale pink background with soft sparkles
d,b=bg([(0,'#ffd8e4'),(1,'#fff4f8')])
b+='<path d="M400 160 L400 320" stroke="#d8b878" stroke-width="6"/>'+ring(400,150,22,'#d8b878',6)+heart(400,420,110,'#ff4a7a')+heart(400,420,80,'#ff8aa8')
b+=sparkle(480,360,22,'#fff')+sparkle(300,520,16,'#fff')+sparkle(560,560,12,'#ffd02a')
I[370]=svg(b,d)

# 673 ARIGATO: a bouquet handed over a stage edge to a guitarist silhouette, warm stage lights
d,b=bg([(0,'#3a1a0a'),(1,'#8a4a1a')])
b+=''.join(f'<polygon points="{x},0 {x-120},640 {x+120},640" fill="#ffd27a" opacity=".15"/>' for x in (200,600))+'<rect y="640" width="800" height="160" fill="#1a0a04"/>'
b+=figure(400,640,320,'#000',pose='hold')+guitar(400,500,.9,-25,'#c83a2a')+''.join(flower(x,y,26,6,c,'#c87a1a') for x,y,c in [(200,660,'#ff6a8a'),(240,640,'#ffd02a'),(270,670,'#fff')])+'<path d="M180 800 L240 680" stroke="#4a8a3a" stroke-width="10"/>'
I[673]=svg(b,d)

# 751 祈り ～涙の軌道: a teardrop falling in an orbit around a small planet in deep space, a faint trail
d,b=bg([(0,'#050514'),(1,'#141a3a')])
b+=starsf(90,751,800)+'<ellipse cx="400" cy="420" rx="300" ry="90" fill="none" stroke="#8ab8ff" stroke-width="3" opacity=".5" transform="rotate(-15 400 420)"/>'
b+='<circle cx="400" cy="420" r="90" fill="#3a5a9a"/><path d="M340 380 Q380 360 420 400 Q460 440 440 470" stroke="#5a8ac8" stroke-width="14" fill="none"/>'+'<path d="M650 330 Q630 370 650 390 Q670 370 650 330Z" fill="#c8e8ff"/>'+glow(650,370,40,'#c8e8ff',.6)
I[751]=svg(b,d)

# 1027 夏の夜: a hanging glass wind chime and mosquito-coil smoke on a dark summer veranda, fireflies
d,b=bg([(0,'#0a1424'),(1,'#1a2a3a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#d8ff6a"/>'+glow(x,y,16,'#d8ff6a',.6) for x,y in [(120,500),(200,420),(620,460),(700,380),(560,560)])
b+='<path d="M400 0 L400 140" stroke="#888" stroke-width="3"/><path d="M350 140 Q350 240 400 240 Q450 240 450 140Z" fill="#a8d8ff" opacity=".8"/><path d="M400 240 L400 340" stroke="#ddd" stroke-width="2"/><rect x="380" y="340" width="40" height="80" fill="#fff"/>'
b+='<rect y="620" width="800" height="180" fill="#3a2a1a"/><circle cx="260" cy="600" r="30" fill="#4a7a3a"/><path d="M260 570 Q240 500 270 440 Q300 380 270 320" stroke="#ddd" stroke-width="3" fill="none" opacity=".5"/>'
I[1027]=svg(b,d)

# 1035 逢いたくていま: a woman's silhouette in deep blue holding a faded photo against her chest, snow-like light
d,b=bg([(0,'#0a1a3a'),(1,'#2a4a7a')])
b+=''.join(f'<circle cx="{(k*97)%800}" cy="{(k*61)%800}" r="{2+k%3}" fill="#fff" opacity=".6"/>' for k in range(60))+glow(400,400,250,'#8ab8ff',.25)
b+=figure(400,780,460,'#000')+'<rect x="380" y="420" width="60" height="50" fill="#d8c8b0" transform="rotate(-10 410 445)"/>'
I[1035]=svg(b,d)

# 1059 Winter Bells: golden bells hanging from a snowy fir branch with snow falling and a lit window
d,b=bg([(0,'#1a2a4a'),(1,'#3a5a8a')])
b+=''.join(f'<circle cx="{(k*131)%800}" cy="{(k*73)%800}" r="{3+k%3}" fill="#fff" opacity=".8"/>' for k in range(60))
b+='<path d="M-10 160 Q300 220 600 160" stroke="#2a5a3a" stroke-width="40" fill="none"/><path d="M-10 140 Q300 200 600 140" stroke="#fff" stroke-width="12" fill="none"/>'
b+=''.join(f'<path d="M{x} 200 L{x} 300" stroke="#c83a2a" stroke-width="5"/><path d="M{x-50} 400 Q{x-40} 300 {x} 300 Q{x+40} 300 {x+50} 400Z" fill="#ffc83a"/><circle cx="{x}" cy="410" r="12" fill="#c8902a"/>' for x in (240,420))+'<path d="M200 220 Q330 260 460 220" stroke="#c83a2a" stroke-width="10" fill="none"/>'
I[1059]=svg(b,d)

# 1071 嗚呼、青春の日々: two silhouettes riding bicycles along a seaside road with a guitar case, early-summer blue
d,b=bg([(0,'#3ab0ff'),(1,'#d8f2ff')])
b+=cloud(560,180,1.6)+'<rect y="460" width="800" height="120" fill="#2a98d0"/><rect y="580" width="800" height="220" fill="#b8b8b8"/>'
for x in (250,480):
    b+=ring(x-50,660,36,'#1a1a1a',8)+ring(x+50,660,36,'#1a1a1a',8)+f'<path d="M{x-50} 660 L{x} 600 L{x+50} 660 M{x} 600 L{x+30} 580" stroke="#1a1a1a" stroke-width="8" fill="none"/>'+f'<g fill="#1a1a1a"><circle cx="{x}" cy="500" r="20"/><path d="M{x-16} 520 L{x+16} 520 L{x+10} 600 L{x-12} 600Z"/></g>'
b+='<rect x="210" y="510" width="26" height="80" rx="10" fill="#5a3a2a" transform="rotate(-20 223 550)"/>'
I[1071]=svg(b,d)

# 1113 NEW HORIZON: a vast flat horizon with a rising sun, eight figures on the shore facing it
d,b=bg([(0,'#0a1a3a'),(.6,'#ff8a4a'),(1,'#ffd08a')])
b+=hinomaru_sun(400,480,120,'#fff2c8')+rays(400,480,30,'#fff',.15,10)+'<rect y="480" width="800" height="320" fill="#2a2a3a"/><rect x="0" y="480" width="800" height="6" fill="#ffe8b8"/>'
b+=''.join(figure(80+k*92,760,200,'#000') for k in range(8))
I[1113]=svg(b,d)

# 872 Killing Me: a shattered mirror with sharp shards flying out against a black-red background, a silhouette in the reflection
d,b=bg([(0,'#0a0004'),(1,'#3a0414')])
b+='<rect x="220" y="120" width="360" height="560" fill="#5a6a7a" stroke="#c8c8d0" stroke-width="10"/>'+figure(400,660,420,'#0a0a14')
b+=''.join(f'<path d="M400 360 L{400+400*math.cos(a):.0f} {360+400*math.sin(a):.0f}" stroke="#e8e8f0" stroke-width="3"/>' for a in [k*.7 for k in range(9)])
b+=''.join(f'<polygon points="{x},{y} {x+30},{y+10} {x+10},{y+40}" fill="#c8d8e8" transform="rotate({x%60} {x} {y})"/>' for x,y in [(110,200),(640,160),(680,500),(120,560),(600,700)])+bolt([(560,40),(520,120),(560,140),(500,240)],'#ff2a4a',6)
I[872]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
