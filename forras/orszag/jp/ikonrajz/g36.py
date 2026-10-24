import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 36. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1896 ETERNAL WIND: a white feather riding a sparkling wind current through a blue sky, anime ballad
d,b=bg([(0,'#3a7ad8'),(1,'#d8f0ff')])
b+=''.join(f'<path d="M-20 {y} Q200 {y-80} 400 {y} T820 {y}" stroke="#fff" stroke-width="{w}" fill="none" opacity=".5"/>' for y,w in [(300,6),(420,10),(540,4)])+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(200,250,20),(600,350,26),(320,520,16),(680,520,18)])
b+='<g transform="rotate(-30 420 400)"><path d="M420 240 Q480 340 430 520 Q360 380 420 240Z" fill="#fff"/><path d="M420 250 L430 540" stroke="#c8d8f0" stroke-width="4"/></g>'
I[1896]=svg(b,d)

# 194 Make-up Shadow: a vanity mirror lit by bulbs, a lipstick and a long shadow across the table, 90s noir
d,b=bg([(0,'#1a1414'),(1,'#3a2a2a')])
b+='<rect x="200" y="140" width="400" height="360" fill="#2a2a34" stroke="#c8a24a" stroke-width="14"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="#fff4c8"/>' for x in (200,600) for y in (180,280,380,480))+glow(400,320,160,'#fff4c8',.25)
b+='<rect x="100" y="560" width="600" height="240" fill="#4a3434"/><path d="M380 560 L800 700 L800 800 L500 800Z" fill="#000" opacity=".4"/><rect x="330" y="470" width="44" height="90" fill="#c8a24a"/><path d="M336 470 L336 410 L368 390 L368 470Z" fill="#a8102a"/>'
b+=profile(470,480,.8,'#14101a')
I[194]=svg(b,d)

# 570 さよならの果実たち: ripe red fruits falling from a branch at dusk, 80s idol farewell
d,b=bg([(0,'#5a3a8a'),(1,'#ff9a7a')])
b+='<path d="M0 140 Q300 180 520 130 Q640 100 800 160" stroke="#3a2a2a" stroke-width="18" fill="none"/>'+''.join(f'<path d="M{x} {y} q30 -20 60 0 q-30 20 -60 0Z" fill="#3a7a3a"/>' for x,y in [(120,160),(380,160),(600,130)])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e8203a"/><path d="M{x} {y-r} l4 -16" stroke="#3a2a2a" stroke-width="4"/><ellipse cx="{x-r/3}" cy="{y-r/3}" rx="{r/5}" ry="{r/3}" fill="#fff" opacity=".4"/>' for x,y,r in [(260,220,34),(480,190,30),(330,420,40),(560,560,36),(220,640,30)])
I[570]=svg(b,d)

# 1041 LOVE RAIN: two umbrellas, one blue one pink, tilted together under heart-shaped raindrops
d,b=bg([(0,'#4a5a8a'),(1,'#a8b8d8')])
b+=''.join(heart(x,y,12,'#ffc0d8',' opacity=".7"') for x,y in [(120,120),(300,90),(500,140),(680,100),(200,300),(620,280),(420,240)])+'<rect y="660" width="800" height="140" fill="#3a4060"/>'
b+=wagasa(330,470,120,'#3a6ad8',-14)+wagasa(480,480,115,'#ff6aa0',14)+figure(330,680,180,'#1a1a2a')+figure(470,680,170,'#1a1a2a',hair='#1a1a2a')
I[1041]=svg(b,d)

# 1123 FREAKY: a sultry silhouette clawing through shredded leopard-print fabric, 2007 dance pop
d,b=bg([(0,'#1a0a14'),(1,'#5a0a2a')])
b+='<rect x="0" y="0" width="800" height="800" fill="#c8944a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="16" fill="#4a2a14"/><circle cx="{x}" cy="{y}" r="8" fill="#a8702a"/>' for x,y in [(80,80),(220,140),(640,90),(740,220),(90,600),(700,640),(160,400),(660,420),(260,720),(560,740)])
b+='<path d="M220 0 L300 800 L500 800 L580 0Z" fill="#1a0a14"/>'+''.join(f'<path d="M{x} 100 L{x+40} 700" stroke="#ff4a8a" stroke-width="6"/>' for x in (300,360,420))+figure(460,780,520,'#000',hair='#000')
I[1123]=svg(b,d)

# 1387 行くぜっ!怪盗少女: a girl thief's silhouette leaping across rooftops under a full moon with a heart-shaped jewel
d,b=bg([(0,'#1a0a3a'),(1,'#4a1a6a')])
b+=starsf(60,1387,500)+moon(560,240,120)+skyline(640,'#100a20',1387,60,200,'#ffd27a',40)+'<rect y="640" width="800" height="160" fill="#100a20"/>'
b+='<g transform="rotate(-25 340 400)">'+figure(340,520,220,'#000',pose='up',hair='#000')+'</g>'+heart(560,240,40,'#ff2a6a')+sparkle(600,200,20,'#fff')
I[1387]=svg(b,d)

# 1797 Around The World: a paper plane circling a small globe, a dotted flight path, cheerful pop
d,b=bg([(0,'#5ad0ff'),(1,'#e0f8ff')])
b+='<circle cx="400" cy="440" r="180" fill="#3a8ad8"/><path d="M300 330 Q360 300 380 360 Q340 420 300 400Z M440 460 Q520 420 540 500 Q480 560 440 520Z M260 480 Q300 500 290 540Z" fill="#5ac86a"/>'
b+='<ellipse cx="400" cy="440" rx="290" ry="110" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="14 12" transform="rotate(-20 400 440)"/><polygon points="640,300 720,280 670,340" fill="#fff"/><polygon points="640,300 670,340 660,316" fill="#c8d8e8"/>'
I[1797]=svg(b,d)

# 171 また君に恋してる: an elderly couple's silhouettes sharing a bench under a soft spring dusk, enka ballad
d,b=bg([(0,'#7a6aa8'),(1,'#ffc8a8')])
b+='<circle cx="560" cy="460" r="70" fill="#ffe8c8"/><rect y="560" width="800" height="240" fill="#6a5a7a"/>'+tree(150,580,400,'#4a3a5a',171)
b+='<rect x="280" y="520" width="280" height="16" fill="#3a2a2a"/><rect x="290" y="536" width="12" height="60" fill="#3a2a2a"/><rect x="538" y="536" width="12" height="60" fill="#3a2a2a"/><rect x="280" y="470" width="280" height="12" fill="#3a2a2a"/>'
b+=figure(360,580,190,'#1a1424')+figure(470,580,180,'#1a1424',hair='#1a1424')+heart(415,330,22,'#ff7aa0')
I[171]=svg(b,d)

# 214 Yes-No: a daisy with petals half plucked, petals drifting away, soft 1980 folk pop
d,b=bg([(0,'#d8e8f4'),(1,'#f4eedc')])
b+='<path d="M400 440 Q380 600 420 800" stroke="#4a8a3a" stroke-width="12" fill="none"/><path d="M400 620 q-80 -30 -110 20 q60 20 110 -20Z" fill="#5aa84a"/>'
b+=''.join(f'<ellipse cx="400" cy="340" rx="22" ry="70" fill="#fff" transform="rotate({a} 400 410)"/>' for a in range(-90,120,30))+'<circle cx="400" cy="410" r="44" fill="#ffd02a"/>'
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="36" fill="#fff" transform="rotate({r} {x} {y})"/>' for x,y,r in [(600,300,40),(660,460,80),(560,560,20),(220,240,-30)])
I[214]=svg(b,d)

# 442 マスカレード: an ornate Venetian mask with feathers lying on a dark velvet stage, 80s rock
d,b=bg([(0,'#1a0a1a'),(1,'#3a0a2a')])
b+=glow(400,420,220,'#c8a24a',.25)+'<path d="M190 400 Q240 320 400 360 Q560 320 610 400 Q600 500 480 480 Q400 440 320 480 Q200 500 190 400Z" fill="#c8a24a"/>'
b+='<ellipse cx="310" cy="410" rx="56" ry="30" fill="#1a0a1a"/><ellipse cx="490" cy="410" rx="56" ry="30" fill="#1a0a1a"/>'+''.join(f'<path d="M560 360 Q{600+k*30} {220-k*20} {560+k*50} {160-k*10}" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/>' for k,c in [(0,'#7a1a4a'),(1,'#a82a5a'),(2,'#3a1a6a')])
b+='<rect y="600" width="800" height="200" fill="#5a0a2a"/>'
I[442]=svg(b,d)

# 559 MIDNIGHT TAXI: a taxi with its roof light glowing on a wet neon street at midnight
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=skyline(500,'#140a24',559,80,280,'#ff8ad0',80)+'<rect y="500" width="800" height="300" fill="#141428"/>'+''.join(f'<rect x="{x}" y="560" width="8" height="160" fill="{c}" opacity=".3"/>' for x,c in [(120,'#ff4fa0'),(240,'#4fd0ff'),(600,'#ffd02a')])
b+='<path d="M180 560 L260 470 L540 470 L620 560 L660 560 L660 640 L140 640 L140 560Z" fill="#ffc82a"/><path d="M280 490 L520 490 L570 556 L230 556Z" fill="#1a1a3a"/><rect x="360" y="440" width="80" height="30" rx="6" fill="#fff4c8"/>'+glow(400,455,60,'#fff4c8',.6)
b+='<circle cx="240" cy="640" r="40" fill="#111"/><circle cx="560" cy="640" r="40" fill="#111"/><ellipse cx="400" cy="720" rx="260" ry="30" fill="#ffc82a" opacity=".2"/>'
I[559]=svg(b,d)

# 580 One Night In Heaven: two angel wings glowing over a midnight city, 80s idol duo
d,b=bg([(0,'#0a0a2a'),(1,'#3a2a5a')])
b+=starsf(70,580,500)+skyline(800,'#0a0a1a',580,60,180,'#8ad0ff',40)
for sx in (-1,1): b+=''.join(f'<ellipse cx="{400+sx*(80+k*36)}" cy="{340+k*30}" rx="{120-k*18}" ry="26" fill="#fff" opacity="{.95-k*.12}" transform="rotate({sx*(-30+k*12)} {400+sx*(80+k*36)} {340+k*30})"/>' for k in range(4))
b+=glow(400,360,120,'#fff4c8',.5)
I[580]=svg(b,d)

# 878 SPARK: an electric spark jumping between two raw cables on a black rock stage
d,b=bg([(0,'#0a0a0a'),(1,'#2a1a0a')])
b+='<path d="M0 520 Q200 500 330 460" stroke="#1a1a1a" stroke-width="40" fill="none"/><path d="M800 300 Q600 340 470 400" stroke="#1a1a1a" stroke-width="40" fill="none"/><path d="M0 520 Q200 500 330 460" stroke="#3a3a3a" stroke-width="30" fill="none"/><path d="M800 300 Q600 340 470 400" stroke="#3a3a3a" stroke-width="30" fill="none"/>'
b+='<path d="M330 460 L350 450 M470 400 L450 410" stroke="#c8702a" stroke-width="10"/>'+bolt([(350,450),(390,400),(400,440),(450,410)],'#fff',8)+glow(400,430,140,'#ffd02a',.8)+''.join(sparkle(x,y,s,'#ffd02a') for x,y,s in [(380,330,24),(470,520,18),(300,380,14),(520,330,16)])
I[878]=svg(b,d)

# 958 Happy Happy Greeting: a big gift box bursting open with streamers and balloons, festive idol duo
d,b=bg([(0,'#ffe0a0'),(1,'#ffc0d0')])
b+=confetti(60,958,['#ff6aa0','#3ab0ff','#ffd02a','#5ad87a'])+'<rect x="260" y="460" width="280" height="240" fill="#e8302a"/><rect x="380" y="460" width="40" height="240" fill="#ffd02a"/><path d="M240 420 L560 420 L560 470 L240 470Z" fill="#c8202a" transform="rotate(-14 400 440)"/>'
b+=''.join(f'<path d="M{x} {y+60} Q{x+10} {y+180} 400 440" stroke="#555" stroke-width="2" fill="none"/><ellipse cx="{x}" cy="{y}" rx="40" ry="50" fill="{c}"/>' for x,y,c in [(260,200,'#3ab0ff'),(400,150,'#ff6aa0'),(540,220,'#5ad87a')])
I[958]=svg(b,d)

# 1081 あなたがここにいたら: an empty chair beside a lit window on a rainy night with two mugs on the sill
d,b=bg([(0,'#1a2030'),(1,'#2a3040')])
b+='<rect x="160" y="120" width="480" height="380" fill="#3a5a7a"/>'+rain(40,1081,'#cfe6ff',.5)+'<rect x="160" y="120" width="480" height="380" fill="none" stroke="#5a4030" stroke-width="20"/><rect x="390" y="120" width="20" height="380" fill="#5a4030"/>'
b+='<rect x="120" y="500" width="560" height="24" fill="#6a4a34"/><rect y="524" width="800" height="276" fill="#2a2020"/>'+''.join(f'<rect x="{x}" y="450" width="40" height="50" rx="6" fill="#f4f0e8"/>' for x in (300,460))
b+='<rect x="480" y="600" width="160" height="16" fill="#8a6a4a"/><rect x="620" y="470" width="16" height="140" fill="#8a6a4a"/><rect x="490" y="616" width="12" height="140" fill="#8a6a4a"/><rect x="620" y="616" width="12" height="140" fill="#8a6a4a"/>'
I[1081]=svg(b,d)

# 1186 Electro World: a glowing wireframe grid planet with neon pulses, electro-pop trio
d,b=bg([(0,'#000814'),(1,'#0a1a3a')])
b+=starsf(50,1186,800)+'<circle cx="400" cy="420" r="200" fill="#001428" stroke="#3affe8" stroke-width="4"/>'+''.join(f'<ellipse cx="400" cy="420" rx="{r}" ry="200" fill="none" stroke="#3affe8" stroke-width="2" opacity=".6"/>' for r in (50,110,160))+''.join(f'<ellipse cx="400" cy="{y}" rx="{(200**2-(y-420)**2)**.5}" ry="12" fill="none" stroke="#3affe8" stroke-width="2" opacity=".6"/>' for y in (280,350,420,490,560))
b+=glow(400,420,240,'#3affe8',.25)+''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="#ff4fd0"/>' for x,y in [(300,330),(480,470),(420,290),(330,520)])
I[1186]=svg(b,d)

# 1261 TEPPEN: a climber's silhouette reaching the summit flag of a steep peak at sunrise
d,b=bg([(0,'#ff8a4a'),(1,'#ffe0a0')])
b+='<circle cx="620" cy="300" r="80" fill="#fff4c8"/><path d="M60 800 L400 220 L740 800Z" fill="#3a2a44"/><path d="M400 220 L450 306 L420 290 L390 320 L360 300 L350 306Z" fill="#f4f4ff"/>'
b+=figure(400,230,120,'#000',pose='up')+'<path d="M440 220 L440 120 L510 140 L440 160" stroke="#000" stroke-width="5" fill="#e8302a"/>'
I[1261]=svg(b,d)

# 1661 もらい泣き: two faces in profile, a tear passing from one cheek to the other, 2002 folk pop
d,b=bg([(0,'#c8e0e8'),(1,'#f0e8d8')])
b+=profile(240,640,1.1,'#3a4a5a')+profile(560,640,1.1,'#4a3a4a',True)
b+='<path d="M330 380 Q336 396 330 404 Q324 396 330 380Z" fill="#5ab0e8"/><path d="M470 420 Q476 436 470 444 Q464 436 470 420Z" fill="#5ab0e8"/><path d="M340 400 Q400 360 460 430" stroke="#5ab0e8" stroke-width="3" stroke-dasharray="6 8" fill="none"/>'
I[1661]=svg(b,d)

# 1669 心よ原始に戻れ: a primal red sun over a dark primordial ocean, sea creatures' silhouettes, anime epic
d,b=bg([(0,'#3a0a0a'),(1,'#a83a1a')])
b+='<circle cx="400" cy="320" r="150" fill="#ff3a1a"/>'+glow(400,320,200,'#ff6a2a',.5)+'<path d="M0 480 Q200 440 400 480 T800 480 L800 800 L0 800Z" fill="#0a1424"/>'
b+='<path d="M200 600 Q260 560 320 600 Q260 620 200 600Z M320 600 L350 580 L350 620Z" fill="#1a3a5a"/><path d="M500 680 Q600 640 680 690 Q600 710 500 680Z M680 690 L720 660 L720 720Z" fill="#1a3a5a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#3a6a8a" opacity=".6"/>' for x,y in [(360,560),(370,530),(560,620)])
I[1669]=svg(b,d)

# 1689 Okay: a hand giving an OK sign silhouetted against a bright stadium-rock blue sky
d,b=bg([(0,'#1a5ac8'),(1,'#a8e0ff')])
b+=rays(400,400,16,'#fff',.15,12)+'<circle cx="400" cy="400" r="200" fill="none" stroke="#fff" stroke-width="26"/><path d="M290 410 L370 490 L530 300" stroke="#fff" stroke-width="44" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'+glow(400,400,240,'#fff',.25)
I[1689]=svg(b,d)

# 1697 早送りカレンダー: calendar pages flying off in a fast-forward blur, a girl running past, idol pop
d,b=bg([(0,'#ffe0ea'),(1,'#e0eaff')])
b+=''.join(f'<g transform="rotate({r} {x} {y})"><rect x="{x-50}" y="{y-60}" width="100" height="120" fill="#fff" stroke="#e0c8d0" stroke-width="3"/><rect x="{x-50}" y="{y-60}" width="100" height="26" fill="#ff5a7a"/><text x="{x}" y="{y+40}" text-anchor="middle" font-family="Noto Sans JP" font-weight="700" font-size="50" fill="#3a3a4a">{n}</text></g>' for x,y,r,n in [(200,200,-20,7),(380,150,10,14),(560,220,25,21),(680,380,-10,28),(140,420,15,3)])
b+=''.join(f'<path d="M{x} {y} L{x-160} {y}" stroke="#ff8ab0" stroke-width="5" stroke-linecap="round" opacity=".6"/>' for x,y in [(380,560),(360,620),(400,680)])+figure(480,760,240,'#3a2a3a',hair='#3a2a3a')
I[1697]=svg(b,d)

# 446 にくまれそうなNEWフェイス: a sharp young rocker's silhouette under one hard spotlight, mid-80s
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+='<path d="M360 0 L440 0 L620 700 L180 700Z" fill="#fff" opacity=".18"/><ellipse cx="400" cy="700" rx="230" ry="44" fill="#fff" opacity=".35"/>'+figure(400,700,380,'#000')+'<path d="M330 380 L470 380 L480 520 L320 520Z" fill="#000"/><path d="M360 310 Q400 260 450 300" stroke="#000" stroke-width="18" fill="none"/>'
I[446]=svg(b,d)

# 886 ズルい女: a woman walking away with a man's broken heart dangling from her handbag, 90s pop
d,b=bg([(0,'#ff6a8a'),(1,'#ffd0a0')])
b+='<rect y="640" width="800" height="160" fill="#c84a5a"/>'+figure(460,660,360,'#1a0a14',hair='#1a0a14')+'<rect x="520" y="480" width="80" height="60" rx="10" fill="#1a0a14"/><path d="M530 480 Q560 440 590 480" stroke="#1a0a14" stroke-width="6" fill="none"/>'
b+='<path d="M560 540 L560 580" stroke="#1a0a14" stroke-width="3"/>'+heart(560,610,26,'#e8102a')+'<path d="M560 590 L552 610 L566 620 L558 640" stroke="#ffd0a0" stroke-width="3" fill="none"/>'
I[886]=svg(b,d)

# 720 DAN DAN 心魅かれてく: a glowing dragon-ball-free orb of light pulled through a starry sky toward a heart
d,b=bg([(0,'#0a1a4a'),(1,'#3a6ab8')])
b+=starsf(80,720,800)+'<path d="M120 640 Q300 500 400 420 T680 180" stroke="#fff4c8" stroke-width="4" fill="none" stroke-dasharray="4 14" opacity=".8"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd02a" opacity="{o}"/>' for x,y,r,o in [(180,600,10,.4),(280,530,14,.6),(400,420,20,.8)])+glow(400,420,50,'#ffd02a',.6)+heart(660,190,60,'#ff6aa0')+glow(660,190,80,'#ff6aa0',.4)
I[720]=svg(b,d)

# 874 Rocket Dive: a retro rocket diving down through clouds trailing pink flames, late-90s rock
d,b=bg([(0,'#1a0a3a'),(1,'#ff6aa0')])
b+=starsf(40,874,400)+cloud(160,560,1.4,'#ffd0e8')+cloud(640,640,1.2,'#ffd0e8')
b+='<g transform="rotate(150 400 400)"><path d="M400 180 Q460 260 460 420 L340 420 Q340 260 400 180Z" fill="#e8e8f4"/><circle cx="400" cy="300" r="26" fill="#3ab0ff" stroke="#8a8aa0" stroke-width="6"/><path d="M340 380 L290 460 L340 440Z M460 380 L510 460 L460 440Z" fill="#ff2a8a"/><path d="M360 420 Q400 560 440 420Z" fill="#ffd02a"/><path d="M375 420 Q400 500 425 420Z" fill="#fff"/></g>'
I[874]=svg(b,d)

# 914 MADE IN JAPAN: a big red rising sun behind Mount Fuji with a bullet train racing past, 90s boy group
d,b=bg([(0,'#fff4e0'),(1,'#ffe0c0')])
fd,fb=fuji(400,560,640,300);d+=fd
b+=hinomaru_sun(400,300,150)+fb+'<rect y="560" width="800" height="240" fill="#3a4a5a"/>'+shinkansen(80,600,130)
I[914]=svg(b,d)

# 1272 浪花いろは節: a giant Osaka-style takoyaki stall with red lanterns and a festive banner
d,b=bg([(0,'#ffd04a'),(1,'#ff8a3a')])
b+='<rect x="140" y="360" width="520" height="300" fill="#8a4a2a"/><path d="M100 360 L400 240 L700 360Z" fill="#c8302a"/><rect x="180" y="440" width="440" height="140" fill="#2a2a2a"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#c8843a"/><path d="M{x-10} {y-4} q10 8 20 0" stroke="#3a2a1a" stroke-width="4" fill="none"/>' for x in range(220,600,60) for y in (480,540))
b+=chochin(180,300,60)+chochin(620,300,60)+'<rect y="660" width="800" height="140" fill="#5a2a1a"/>'
I[1272]=svg(b,d)

# 1691 君は薔薇より美しい: a single perfect red rose before a woman's silhouette, 1979 ballad
d,b=bg([(0,'#2a0a1a'),(1,'#8a2a3a')])
b+=glow(400,400,240,'#ff6a8a',.3)+profile(560,760,1.4,'#1a0a10',True)+rose(320,380,1.3,-10)+'<path d="M320 450 Q300 600 320 800" stroke="#3a7a2a" stroke-width="10" fill="none"/><path d="M314 560 q-60 -20 -80 20 q50 10 80 -20Z" fill="#3a7a2a"/>'
I[1691]=svg(b,d)

# 1884 紋白蝶: a cabbage white butterfly fluttering over a ska-brass trumpet in a meadow
d,b=bg([(0,'#bfe6ff'),(1,'#e8fff0')])
b+='<rect y="580" width="800" height="220" fill="#7ac85a"/>'+''.join(flower(x,600,14,6,'#fff','#ffd02a') for x in (120,260,560,700))
b+='<g transform="rotate(-20 400 520)"><rect x="200" y="500" width="340" height="30" fill="#e8b830"/><path d="M540 470 L660 420 L660 610 L540 560Z" fill="#e8b830"/><rect x="300" y="460" width="20" height="40" fill="#c8982a"/><rect x="340" y="460" width="20" height="40" fill="#c8982a"/><rect x="380" y="460" width="20" height="40" fill="#c8982a"/></g>'
b+='<g transform="translate(420 240)"><ellipse cx="-40" cy="-20" rx="50" ry="40" fill="#fff" stroke="#ccc" stroke-width="2"/><ellipse cx="40" cy="-20" rx="50" ry="40" fill="#fff" stroke="#ccc" stroke-width="2"/><ellipse cx="-30" cy="30" rx="34" ry="28" fill="#fff" stroke="#ccc" stroke-width="2"/><ellipse cx="30" cy="30" rx="34" ry="28" fill="#fff" stroke="#ccc" stroke-width="2"/><circle cx="-46" cy="-24" r="8" fill="#3a3a3a"/><circle cx="46" cy="-24" r="8" fill="#3a3a3a"/><rect x="-5" y="-40" width="10" height="90" rx="5" fill="#3a3a3a"/></g>'
I[1884]=svg(b,d)

# 296 モンキー・マジック: a golden cloud flying through a mythical sky with a long red-banded staff, 1978 rock
d,b=bg([(0,'#3a1a5a'),(1,'#ff9a4a')])
b+=''.join(f'<path d="M{x} {y} l60 -120 l60 120Z" fill="#5a2a4a" opacity=".6"/>' for x,y in [(40,800),(560,800),(660,800)])+'<path d="M200 800 L360 380 L520 800Z" fill="#4a2a4a"/>'
b+=cloud(420,440,2.0,'#ffd86a')+'<g transform="rotate(-30 400 300)"><rect x="390" y="80" width="20" height="440" fill="#c8302a"/><rect x="386" y="80" width="28" height="30" fill="#ffd02a"/><rect x="386" y="490" width="28" height="30" fill="#ffd02a"/></g>'
I[296]=svg(b,d)

# 378 マラケッシュ: a Moroccan arched doorway with a brass lantern and a desert sunset beyond, 1988
d,b=bg([(0,'#c84a2a'),(1,'#e8a86a')])
b+='<path d="M0 0 L800 0 L800 800 L0 800Z M230 800 L230 340 Q230 160 400 140 Q570 160 570 340 L570 800Z" fill="#e8d0a8" fill-rule="evenodd"/>'
b+='<circle cx="400" cy="520" r="70" fill="#ffd88a"/><path d="M230 600 Q400 560 570 600 L570 800 L230 800Z" fill="#c8843a"/>'+''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#2a6a8a" transform="rotate(45 {x+20} {y+20})"/>' for x in (40,110,670,740) for y in (100,250,400,550))
b+='<path d="M400 180 L400 230" stroke="#6a4a2a" stroke-width="4"/><path d="M370 230 L430 230 L440 300 L400 330 L360 300Z" fill="#c8a24a"/>'+glow(400,280,60,'#ffd88a',.7)
I[378]=svg(b,d)

# 485 Liar Girl: a girl's silhouette with crossed fingers behind her back against a jagged red-black backdrop, 80s rock
d,b=bg([(0,'#0a0a0a'),(1,'#3a0a0a')])
b+='<path d="M0 0 L800 0 L800 300 L600 260 L700 420 L480 360 L520 560 L320 420 L240 620 L180 380 L0 460Z" fill="#a8102a"/>'+figure(400,760,440,'#000',hair='#000')
b+='<path d="M470 560 Q510 560 520 600" stroke="#000" stroke-width="20" fill="none" stroke-linecap="round"/><path d="M518 596 L530 560 M522 600 L512 560" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
I[485]=svg(b,d)

# 541 SUMMER SUSPICION: a car's rear-view mirror reflecting a seaside highway and a woman's silhouette, summer
d,b=bg([(0,'#3ab0e8'),(1,'#f4f0c8')])
b+='<rect y="560" width="800" height="240" fill="#1a7ac8"/><path d="M0 640 Q400 600 800 660 L800 800 L0 800Z" fill="#f0d8a0"/>'+'<circle cx="160" cy="180" r="60" fill="#fff8c8"/>'
b+='<rect x="390" y="0" width="20" height="200" fill="#1a1a1a"/><rect x="200" y="180" width="400" height="160" rx="70" fill="#1a1a1a"/><rect x="220" y="196" width="360" height="128" rx="60" fill="#ffb07a"/><rect x="220" y="270" width="360" height="54" rx="0" fill="#2a7ac8"/>'+figure(460,320,90,'#2a1a2a',hair='#2a1a2a')
I[541]=svg(b,d)

# 850 天使のわけまえ: a single white angel feather falling into an outstretched hand in grey light, 2000s rock
d,b=bg([(0,'#5a6070'),(1,'#c8ccd8')])
b+=glow(400,200,200,'#fff',.5)+'<g transform="rotate(20 420 300)"><path d="M420 180 Q480 270 430 420 Q360 290 420 180Z" fill="#fff"/><path d="M420 190 L430 440" stroke="#c8ccd8" stroke-width="3"/></g>'
b+='<path d="M180 800 L260 620 Q300 560 380 580 L560 580 Q600 590 580 620 L440 630 L520 640 Q560 660 520 680 L340 700 L300 800Z" fill="#2a2a34"/>'
I[850]=svg(b,d)

# 890 サーキットの娘: a racing girl's silhouette with a checkered flag at a racetrack, quirky 90s pop
d,b=bg([(0,'#ffe04a'),(1,'#ff9a4a')])
b+='<path d="M0 560 Q400 480 800 560 L800 800 L0 800Z" fill="#3a3a44"/><path d="M0 610 Q400 530 800 610" stroke="#fff" stroke-width="8" stroke-dasharray="40 30" fill="none"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#111"/>' for i,x in enumerate(range(420,620,40)) for j,y in enumerate(range(160,320,40)) if (i+j)%2==0)+'<rect x="420" y="160" width="200" height="160" fill="none" stroke="#111" stroke-width="4"/><path d="M420 160 L380 560" stroke="#111" stroke-width="10"/>'
b+=figure(340,600,240,'#1a1a2a',pose='up',hair='#1a1a2a')
I[890]=svg(b,d)

# 1055 FLOATIN': two silhouettes floating weightless among bubbles in a dreamy indigo space, R&B duo
d,b=bg([(0,'#1a1a4a'),(1,'#5a4a9a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#cfe6ff" stroke-width="3" opacity=".7"/>' for x,y,r in [(140,200,30),(600,140,40),(680,500,24),(200,620,50),(520,680,20),(320,120,16)])
b+='<g transform="rotate(-30 330 420)">'+figure(330,560,240,'#0a0a2a')+'</g><g transform="rotate(25 480 400)">'+figure(480,540,240,'#0a0a2a')+'</g>'+glow(400,420,200,'#8ab0ff',.3)
I[1055]=svg(b,d)

# 1251 僕らの街で: a group of friends' silhouettes on a river embankment overlooking their hometown at dusk
d,b=bg([(0,'#5a6ac8'),(1,'#ffb88a')])
b+=skyline(520,'#4a4060',1251,40,160,'#ffd27a',40)+'<path d="M0 560 Q400 520 800 560 L800 600 L0 600Z" fill="#8ab0d8"/><path d="M0 600 L800 600 L800 800 L0 800Z" fill="#3a5a3a"/>'
b+=''.join(figure(x,700,150+(x%4)*6,'#1a1a24') for x in (220,300,380,460,540))
I[1251]=svg(b,d)

# 1663 Perseus: the Perseus constellation over a dark sea with a meteor shower, 2003 pop
d,b=bg([(0,'#050a24'),(1,'#1a2a5a')])
b+=starsf(90,1663,560)+''.join(f'<path d="M{x} {y} l120 60" stroke="#fff" stroke-width="3" opacity=".7" stroke-linecap="round"/>' for x,y in [(80,120),(220,60),(480,160),(560,80)])
pts=[(400,140),(430,220),(470,300),(440,380),(360,330),(520,440),(400,470)]
b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" stroke="#8ad0ff" stroke-width="3" fill="none" opacity=".7"/>'+''.join(star5(x,y,16,'#fff4c8') for x,y in pts)
b+='<rect y="580" width="800" height="220" fill="#0a1430"/>'+''.join(f'<rect x="{x}" y="{y}" width="40" height="3" fill="#8ad0ff" opacity=".4"/>' for x,y in [(380,600),(420,640),(360,700),(440,740)])
I[1663]=svg(b,d)

# 1715 HELLO: an old-fashioned telephone box glowing at night on an empty street, 2003 rock
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=starsf(40,1715,400)+'<rect y="640" width="800" height="160" fill="#14141e"/><rect x="300" y="260" width="200" height="400" fill="#2a8a4a"/><rect x="320" y="300" width="160" height="320" fill="#fff4c8"/>'+glow(400,460,180,'#fff4c8',.4)
b+=''.join(f'<rect x="320" y="{y}" width="160" height="6" fill="#2a8a4a"/>' for y in (380,460,540))+'<rect x="290" y="240" width="220" height="30" fill="#1a6a3a"/>'+phone(400,440,.6,'#1a1a1a')
I[1715]=svg(b,d)

# 1894 なごり雪: late spring snow falling on an empty station platform as a train departs, 70s folk
d,b=bg([(0,'#b8c0d0'),(1,'#e8ecf0')])
b+=snow(70,1894)+'<rect y="520" width="800" height="280" fill="#7a808c"/><rect y="520" width="800" height="16" fill="#e8e8e8"/><rect x="420" y="380" width="380" height="140" fill="#c8ccd4"/>'+''.join(f'<rect x="{x}" y="410" width="50" height="40" fill="#5a6070"/>' for x in (460,540,620,700))
b+=''.join(f'<rect x="{x}" y="120" width="12" height="400" fill="#5a5a64"/>' for x in (120,360))+'<rect x="100" y="120" width="290" height="14" fill="#5a5a64"/>'+figure(240,560,200,'#2a2a34')
I[1894]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
