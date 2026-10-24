import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 46. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 47 修学旅行: a line of uniformed students' silhouettes before an old temple pagoda on a school trip, 1963
d,b=bg([(0,'#9ad0ff'),(1,'#fff0d8')])
b+=''.join(f'<rect x="{560-w/2}" y="{520-(k+1)*80}" width="{w}" height="80" fill="#5a3a2a"/><path d="M{560-w/2-30} {520-(k+1)*80} L{560+w/2+30} {520-(k+1)*80} L{560+w/2} {520-(k+1)*80-20} L{560-w/2} {520-(k+1)*80-20}Z" fill="#3a2a24"/>' for k,w in enumerate((90,80,70,60,50)))+'<rect x="556" y="80" width="8" height="40" fill="#3a2a24"/>'
b+='<rect y="520" width="800" height="280" fill="#d8c8a8"/>'+''.join(figure(x,700,160,'#1a1a2a',hair='#1a1a2a' if k%2 else None) for k,x in enumerate(range(80,460,60)))+'<rect x="40" y="520" width="8" height="120" fill="#3a3a3a"/><path d="M48 520 L110 540 L48 560Z" fill="#ffd02a"/>'
I[47]=svg(b,d)

# 199 帰れない二人: a couple on a midnight bridge watching the last train lights disappear, 1973 folk
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+=starsf(60,199,400)+'<rect y="440" width="800" height="360" fill="#0a1020"/><path d="M0 500 Q400 420 800 500" stroke="#2a2a3a" stroke-width="20" fill="none"/>'+''.join(f'<rect x="{x}" y="{460+abs(400-x)*.2}" width="6" height="40" fill="#2a2a3a"/>' for x in range(40,800,60))
b+=''.join(f'<rect x="{x}" y="600" width="40" height="16" fill="#ffd27a" opacity="{.8-k*.15}"/>' for k,x in enumerate((560,620,680,740)))+figure(360,470,140,'#000')+figure(410,470,130,'#000',hair='#000')
I[199]=svg(b,d)

# 223 終止符: a final note with a heavy full stop on a torn sheet of music in an empty room, 1979 rock
d,b=bg([(0,'#2a2a3a'),(1,'#4a4a5a')])
b+='<rect x="140" y="200" width="520" height="380" fill="#f4ecd8" transform="rotate(-4 400 390)"/>'+''.join(f'<path d="M170 {y} L630 {y-30}" stroke="#3a3a3a" stroke-width="3" transform="rotate(-4 400 390)"/>' for y in range(320,440,24))
b+=note(300,400,60,'#1a1a1a')+'<circle cx="520" cy="360" r="40" fill="#1a1a1a"/><path d="M620 200 L600 260 L640 300 L610 360 L660 420 L630 580" stroke="#2a2a3a" stroke-width="16" fill="none"/>'
I[223]=svg(b,d)

# 1754 Flower: a single white flower held up toward a bright spring sky by a girl's hand, 2011
d,b=bg([(0,'#9ad8ff'),(1,'#fff4f8')])
b+=rays(400,200,18,'#fff',.35,10)+'<path d="M380 800 L400 520 Q404 480 420 470 L440 480 L430 520 L420 800Z" fill="#f4c8a8"/><path d="M420 480 L420 300" stroke="#4a8a3a" stroke-width="6"/>'+flower(420,260,60,6,'#fff','#ffd02a')+glow(420,260,100,'#fff',.6)
I[1754]=svg(b,d)

# 277 風をあつめて: a figure on a city rooftop at dawn, a sail of wind filling a long white cloth, 1971 folk rock
d,b=bg([(0,'#7ab8e8'),(1,'#ffe8d0')])
b+=skyline(640,'#5a6a8a',277,60,220,'#ffe8a0',30)+'<rect y="640" width="800" height="160" fill="#3a4a6a"/>'+''.join(f'<path d="M-20 {y} Q200 {y-50} 400 {y} T820 {y}" stroke="#fff" stroke-width="5" fill="none" opacity=".6"/>' for y in (200,300,400))
b+=figure(300,660,240,'#1a1a2a')+'<path d="M330 450 Q460 380 560 440 Q500 500 340 480Z" fill="#fff" opacity=".9"/>'
I[277]=svg(b,d)

# 706 真っ赤なLip: bold red lips with a lipstick tube against a black-and-white checker background, 2020 rock
d,b=bg([(0,'#1a1a1a'),(1,'#2a2a2a')])
b+=''.join(f'<rect x="{x}" y="{y}" width="100" height="100" fill="#3a3a3a"/>' for x in range(0,800,100) for y in range(0,800,100) if (x+y)//100%2==0)
b+='<g transform="translate(400 400) scale(2.4) translate(-400 -400)"><path d="M340 400 Q370 360 400 385 Q430 360 460 400 Q430 410 400 405 Q370 410 340 400Z M340 400 Q400 450 460 400 Q430 430 400 432 Q370 430 340 400Z" fill="#e8102a"/></g>'
b+='<rect x="560" y="520" width="60" height="160" fill="#c8a24a" transform="rotate(20 590 600)"/><path d="M570 520 L570 440 L610 420 L610 520Z" fill="#e8102a" transform="rotate(20 590 600)"/>'
I[706]=svg(b,d)

# 927 COLORS: six silhouettes each bathed in a different coloured spotlight on a dark stage, 2017 boy group
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=''.join(f'<path d="M{x-20} 0 L{x+20} 0 L{x+70} 680 L{x-70} 680Z" fill="{c}" opacity=".35"/>'+figure(x,690,220,'#000') for x,c in zip(range(100,800,120),['#e8302a','#ff9a2a','#ffd02a','#3ad85a','#3a9aff','#a85aff']))+'<rect y="690" width="800" height="110" fill="#0a0a10"/>'
I[927]=svg(b,d)

# 1702 シンデレラたちへの伝言: a single glass slipper on a clock-struck midnight staircase, 80s idol
d,b=bg([(0,'#1a1a4a'),(1,'#5a4a8a')])
b+=''.join(f'<rect x="{100+k*30}" y="{720-k*60}" width="{600-k*60}" height="20" fill="#c8c0e0" opacity=".7"/>' for k in range(9))+moon(620,140,50)
b+='<path d="M340 680 Q340 620 380 620 L440 640 Q470 650 460 680Z" fill="#cfe6ff" opacity=".9" stroke="#fff" stroke-width="3"/><path d="M440 680 L444 700" stroke="#cfe6ff" stroke-width="8"/>'+sparkle(420,600,20,'#fff')
I[1702]=svg(b,d)

# 1700 バグっていいじゃん: a glitchy pixelated heart with displaced colour blocks on a retro screen, idol pop
d,b=bg([(0,'#1a1a2a'),(1,'#2a1a3a')])
px=[(x,y) for y in range(8) for x in range(9) if (x,y) in [(1,0),(2,0),(6,0),(7,0),(0,1),(1,1),(2,1),(3,1),(5,1),(6,1),(7,1),(8,1),(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(2,4),(3,4),(4,4),(5,4),(6,4),(3,5),(4,5),(5,5),(4,6)]]
b+=''.join(f'<rect x="{220+x*40+(20 if y in (2,5) else 0)}" y="{240+y*40}" width="40" height="40" fill="#ff4a8a"/>' for x,y in px)+''.join(f'<rect x="{220+x*40-14}" y="{240+y*40}" width="40" height="8" fill="#3affe8" opacity=".7"/>' for x,y in px[::5])
b+=''.join(f'<rect x="0" y="{y}" width="800" height="3" fill="#fff" opacity=".05"/>' for y in range(0,800,8))
I[1700]=svg(b,d)

# 1736 いきなりパンチライン: a comic speech burst with a big punch glove popping out of a jack-in-the-box, idol pop
d,b=bg([(0,'#ffd04a'),(1,'#ff8a5a')])
b+=rays(400,300,20,'#fff',.3,12)+'<rect x="300" y="560" width="200" height="180" fill="#3a6ab8"/><path d="M300 560 L280 520 L380 520 L400 560Z" fill="#2a5aa8"/>'
b+='<path d="M400 560 Q360 520 440 480 Q360 440 440 400 Q360 360 420 330" stroke="#c8c8d0" stroke-width="10" fill="none"/>'+'<rect x="330" y="180" width="160" height="150" rx="70" fill="#e8302a"/><ellipse cx="460" cy="300" rx="44" ry="30" fill="#e8302a"/><rect x="370" y="320" width="80" height="30" fill="#fff"/>'+''.join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#fff" stroke-width="10" stroke-linecap="round"/>' for x,y,dx,dy in [(300,180,-40,-30),(520,180,40,-30),(540,260,50,0),(280,260,-50,0)])
I[1736]=svg(b,d)

# 1828 燃えろ! 仮面ライダー: a motorcycle rider's silhouette blasting through a wall of flames, tokusatsu theme
d,b=bg([(0,'#1a0a0a'),(1,'#a82a0a')])
b+=''.join(f'<path d="M{x} 800 Q{x-30} {600-h} {x+20} {500-h} Q{x+40} {620-h} {x+60} 800Z" fill="{c}"/>' for x,h,c in [(0,60,'#ff6a1a'),(100,140,'#ffa82a'),(220,40,'#ff6a1a'),(500,120,'#ffa82a'),(620,60,'#ff6a1a'),(720,100,'#ffa82a')])
b+='<g transform="rotate(-10 400 500)">'+ring(300,580,60,'#0a0a0a',14)+ring(520,580,60,'#0a0a0a',14)+'<path d="M300 580 L400 490 L520 580 M400 490 L480 470 L500 440" stroke="#0a0a0a" stroke-width="16" fill="none"/>'+figure(410,500,190,'#0a0a0a')+'<path d="M400 340 Q300 310 220 350 Q300 350 360 370" fill="#e8102a"/></g>'
I[1828]=svg(b,d)

# 323 CIRCUS TOWN: a striped circus tent glowing in the middle of a night city skyline, 1976 city pop
d,b=bg([(0,'#0a0a2a'),(1,'#3a1a4a')])
b+=skyline(640,'#14142a',323,100,320,'#ffd27a',80)+'<path d="M200 640 L400 320 L600 640Z" fill="#e8302a"/>'+''.join(f'<path d="M400 320 L{x} 640" stroke="#fff4e8" stroke-width="22"/>' for x in (260,360,460,560))
b+='<path d="M400 320 L400 270 L440 285 L400 300" fill="#ffd02a" stroke="#ffd02a" stroke-width="3"/>'+glow(400,520,200,'#ffd27a',.3)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'+''.join(f'<circle cx="{x}" cy="{340+((x-200)/400)*300 if x<400 else 340+((600-x)/200)*300}" r="6" fill="#ffd02a"/>' for x in range(220,600,30))
I[323]=svg(b,d)

# 608 だってそうじゃない!?: a girl with hands on hips standing defiantly on a city crosswalk, 90s band pop
d,b=bg([(0,'#5ac8ff'),(1,'#fff0d8')])
b+=skyline(500,'#8a9ab8',608,60,200,'#fff',20)+'<rect y="500" width="800" height="300" fill="#5a5a64"/>'+''.join(f'<rect x="{x}" y="600" width="50" height="160" fill="#f4f4f4"/>' for x in range(60,760,90))
b+=figure(400,760,380,'#e8302a',hair='#3a1a1a')+'<path d="M350 520 L310 560 L350 600 M450 520 L490 560 L450 600" stroke="#e8302a" stroke-width="20" fill="none" stroke-linejoin="round"/>'
I[608]=svg(b,d)

# 1703 かげろう: a heat-haze shimmering over a summer road with a girl's silhouette half dissolving, 80s idol
d,b=bg([(0,'#ffd88a'),(1,'#fff4d8')])
b+='<rect y="460" width="800" height="340" fill="#c8b8a0"/><path d="M380 460 L120 800 L680 800 L420 460Z" fill="#8a8a8a"/>'+''.join(f'<path d="M100 {y} Q200 {y-10} 300 {y} T500 {y} T700 {y}" stroke="#fff" stroke-width="4" fill="none" opacity=".5"/>' for y in (500,530,560))
b+=figure(400,620,200,'#5a4a5a',hair='#5a4a5a')+''.join(f'<rect x="{360+k*20}" y="{420+k*30}" width="80" height="6" fill="#fff4d8" opacity=".7"/>' for k in range(4))
I[1703]=svg(b,d)

# 1733 超ネバギバDANCE: a line of dancers mid-jump with speed-lines and a bullet-train blur behind them
d,b=bg([(0,'#1a1a4a'),(1,'#ff4a6a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#fff" stroke-width="{w}" opacity=".3"/>' for y,w in [(200,4),(260,10),(330,6),(380,2)])+shinkansen(-100,240,200)
b+='<rect y="660" width="800" height="140" fill="#1a0a1a"/>'+''.join(f'<g transform="translate(0 {-30 if k%2 else 0})">'+figure(x,680,220,'#000',pose='up')+'</g>' for k,x in enumerate(range(100,800,120)))
I[1733]=svg(b,d)

# 24 ふりむかないで: a woman walking away on a 60s city street with a polka-dot dress and a backward glance forbidden
d,b=bg([(0,'#ffe0c8'),(1,'#ffc8a8')])
b+=skyline(560,'#c8a0a0',24,60,220,'#fff4e0',40)+'<rect y="560" width="800" height="240" fill="#b8a0a0"/>'
b+=figure(400,740,400,'#1a1a2a',hair='#1a1a2a')+'<path d="M340 470 L460 470 L520 680 L280 680Z" fill="#e8302a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#fff"/>' for x,y in [(360,520),(420,500),(400,580),(340,620),(460,620),(440,560),(300,660),(500,660)])
I[24]=svg(b,d)

# 1685 君を大好きだ: a boy shouting into the sky from a hilltop with hearts bursting out, 2019 boy group
d,b=bg([(0,'#5ab0ff'),(1,'#fff0e0')])
b+='<path d="M0 640 Q400 520 800 640 L800 800 L0 800Z" fill="#6ab84a"/>'+figure(300,600,240,'#1a2a3a',pose='up')+''.join(heart(x,y,s,'#ff4a8a') for x,y,s in [(420,320,40),(500,240,30),(580,180,24),(640,120,18),(470,180,16)])
I[1685]=svg(b,d)

# 1829 仮面ライダーストロンガーのうた: a motorcycle silhouette charged with electricity and lightning bolts, tokusatsu theme
d,b=bg([(0,'#0a0a2a'),(1,'#1a2a5a')])
b+=bolt([(120,60),(200,240),(150,260),(240,440)],'#8ad0ff',10)+bolt([(680,80),(600,240),(650,260),(560,420)],'#8ad0ff',10)+'<rect y="620" width="800" height="180" fill="#0a0a14"/>'
b+=ring(300,600,60,'#0a0a0a',14)+ring(520,600,60,'#0a0a0a',14)+'<path d="M300 600 L400 510 L520 600 M400 510 L480 490 L500 460" stroke="#0a0a0a" stroke-width="16" fill="none"/>'+figure(410,520,190,'#0a0a0a')+glow(410,450,160,'#8ad0ff',.3)+''.join(f'<path d="M{x} {y} l14 -20 l-6 16 l14 -18" stroke="#8ad0ff" stroke-width="4" fill="none"/>' for x,y in [(250,560),(560,560),(420,380)])
I[1829]=svg(b,d)

# 200 東へ西へ: a crowd of commuters' silhouettes rushing in opposite directions across a station concourse, 1972
d,b=bg([(0,'#d8d0c0'),(1,'#a8a090')])
b+='<rect y="560" width="800" height="240" fill="#8a8274"/>'+''.join(f'<g transform="rotate({12 if k%2 else -12} {x} 640)">'+figure(x,740,200,'#2a2a34')+'</g>' for k,x in enumerate(range(60,800,80)))
b+='<path d="M80 200 L280 200 L280 170 L340 220 L280 270 L280 240 L80 240Z" fill="#3a6ab8"/><path d="M720 300 L520 300 L520 270 L460 320 L520 370 L520 340 L720 340Z" fill="#e8302a"/>'
I[200]=svg(b,d)

# 344 ABSOLUTE EGO DANCE: a robotic dancer silhouette made of geometric shapes under red techno lights, 1979
d,b=bg([(0,'#0a0a0a'),(1,'#3a0a0a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#e8302a" stroke-width="2" opacity=".3"/>' for y in range(40,800,40))
b+='<rect x="360" y="180" width="80" height="80" fill="#e8302a"/><rect x="330" y="270" width="140" height="180" fill="#f4f4f4"/><rect x="250" y="280" width="80" height="24" fill="#f4f4f4" transform="rotate(-30 330 290)"/><rect x="470" y="280" width="80" height="24" fill="#f4f4f4" transform="rotate(40 470 290)"/>'
b+='<rect x="340" y="450" width="40" height="200" fill="#f4f4f4" transform="rotate(10 360 450)"/><rect x="420" y="450" width="40" height="200" fill="#f4f4f4" transform="rotate(-20 440 450)"/>'+glow(400,400,240,'#e8302a',.3)
I[344]=svg(b,d)

# 201 傘がない: a young man standing in the pouring rain without an umbrella, reflected in puddles, 1972 folk
d,b=bg([(0,'#3a4050'),(1,'#6a7080')])
b+=rain(140,201,'#e8f0ff',.45)+'<rect y="620" width="800" height="180" fill="#2a2e3a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="60" ry="10" fill="#8a9ab8" opacity=".3"/>' for x,y in [(200,680),(560,720),(400,660)])
b+=figure(400,640,320,'#0a0a14')+'<g transform="translate(0 1280) scale(1 -1)" opacity=".2">'+figure(400,640,320,'#8a9ab8')+'</g>'
I[201]=svg(b,d)

# 853 ひとひらの自由: a single petal carried freely by the wind over rooftops and a wide sky, 2001 rock
d,b=bg([(0,'#5ab0ff'),(1,'#e8f8ff')])
b+=cloud(600,180,1.2)+''.join(f'<path d="M-20 {y} Q200 {y-60} 400 {y} T820 {y}" stroke="#fff" stroke-width="4" fill="none" opacity=".5"/>' for y in (300,420))+skyline(800,'#6a7a9a',853,60,200,'#fff',20)
b+='<path d="M420 300 Q470 260 500 300 Q470 340 420 300Z" fill="#fff" transform="rotate(-30 460 300)"/>'+'<path d="M200 400 Q300 360 420 300" stroke="#fff" stroke-width="3" stroke-dasharray="6 10" fill="none"/>'
I[853]=svg(b,d)

# 1662 他人の関係: two silhouettes in separate lit windows of the same building, 2012
d,b=bg([(0,'#0a0a1a'),(1,'#2a2a3a')])
b+='<rect x="160" y="100" width="480" height="700" fill="#1a1a24"/>'+''.join(f'<rect x="{x}" y="{y}" width="120" height="100" fill="#0a0a14"/>' for x in (200,480) for y in (140,280,420,560))
b+='<rect x="200" y="280" width="120" height="100" fill="#ffd27a"/><rect x="480" y="420" width="120" height="100" fill="#8ad0ff"/>'+profile(270,380,.35,'#3a2a1a')+profile(530,520,.35,'#1a2a3a',True)
I[1662]=svg(b,d)

# 35 長崎の女: a woman under an umbrella on a hilly Nagasaki slope with a church spire and harbour in the rain
d,b=bg([(0,'#3a3a5a'),(1,'#8a8aa8')])
b+=rain(80,35,'#e8f0ff',.35)+'<rect y="440" width="800" height="200" fill="#4a5a8a"/><path d="M0 800 L0 520 L800 360 L800 800Z" fill="#5a4a4a"/>'
b+='<rect x="580" y="260" width="80" height="140" fill="#e8e0d0"/><path d="M570 260 L620 160 L670 260Z" fill="#5a6a7a"/><path d="M620 160 L620 120 M606 136 L634 136" stroke="#e8e0d0" stroke-width="5"/>'
b+=figure(300,620,240,'#0a0a14',hair='#0a0a14')+wagasa(300,400,100,'#c8302a',-8)
I[35]=svg(b,d)

# 299 月のあかり: moonlight streaming through a window across an empty bed and a guitar, 1978 rock ballad
d,b=bg([(0,'#0a0a24'),(1,'#1a1a3a')])
b+='<rect x="460" y="100" width="260" height="320" fill="#1a2a5a"/>'+moon(590,220,60)+'<rect x="460" y="100" width="260" height="320" fill="none" stroke="#2a2a3a" stroke-width="12"/><path d="M460 420 L120 760 L520 760 L720 420Z" fill="#cfe6ff" opacity=".15"/>'
b+='<rect x="60" y="560" width="440" height="140" fill="#2a2a44"/>'+guitar(560,600,.8,-60,'#3a2a2a')
I[299]=svg(b,d)

# 612 GRAVITY OF LOVE: two glowing planets orbiting each other with a heart at the centre of gravity, synth pop
d,b=bg([(0,'#050520'),(1,'#1a0a3a')])
b+=starsf(80,612,800)+'<ellipse cx="400" cy="400" rx="260" ry="100" fill="none" stroke="#a88ae8" stroke-width="3" transform="rotate(-20 400 400)"/>'+'<circle cx="170" cy="470" r="60" fill="#3a9aff"/><circle cx="630" cy="330" r="50" fill="#ff6aa8"/>'+heart(400,400,40,'#fff')+glow(400,400,80,'#fff',.6)
I[612]=svg(b,d)

# 1711 青春時代 1.2.3!: three schoolgirls' silhouettes jumping on a school track in a bright blue sky
d,b=bg([(0,'#3ab0ff'),(1,'#e0f8ff')])
b+=cloud(160,160,1.2)+'<rect y="580" width="800" height="220" fill="#d86a4a"/>'+''.join(f'<path d="M0 {y} Q400 {y-30} 800 {y}" stroke="#fff" stroke-width="4" fill="none"/>' for y in (640,700,760))
b+=''.join(f'<g transform="translate(0 {-h})">'+figure(x,600,220,'#1a1a3a',pose='up',hair='#1a1a3a')+'</g>' for x,h in [(240,40),(400,80),(560,40)])
I[1711]=svg(b,d)

# 48 君だけを: a young man holding out a single flower under a cherry-free spring sky, 1964 pop
d,b=bg([(0,'#9ad0ff'),(1,'#fff0e0')])
b+='<rect y="620" width="800" height="180" fill="#8ac86a"/>'+figure(320,640,320,'#1a1a2a')+'<path d="M360 460 L460 420" stroke="#1a1a2a" stroke-width="18" stroke-linecap="round"/><path d="M460 420 L470 340" stroke="#3a7a3a" stroke-width="5"/>'+flower(470,320,30,5,'#ff6a8a','#ffd02a')+heart(560,220,30,'#ff8ab0')
I[48]=svg(b,d)

# 80 今日の日はさようなら: children's silhouettes waving goodbye around a dying campfire at dusk, 1967 folk
d,b=bg([(0,'#3a3a6a'),(1,'#ff9a7a')])
b+='<path d="M0 560 Q400 500 800 560 L800 800 L0 800Z" fill="#2a2030"/>'+'<path d="M370 620 L430 620 L400 560Z" fill="#ff8a2a"/>'+glow(400,600,120,'#ff8a2a',.6)
b+=''.join(figure(x,y,s,'#0a0a10',pose='up' if k%2==0 else 'stand',hair='#0a0a10' if k%3 else None) for k,(x,y,s) in enumerate([(200,640,170),(280,600,150),(520,600,150),(600,640,170),(140,690,190),(660,690,190)]))
I[80]=svg(b,d)

# 100 哀しみ本線 日本海: a night train running along a stormy Sea of Japan coast with crashing waves, enka
d,b=bg([(0,'#1a2030'),(1,'#3a4a5a')])
b+=snow(60,100,.6)+'<rect y="420" width="800" height="380" fill="#2a3a4a"/>'+''.join(f'<path d="M{x} {y} q40 -40 80 0" stroke="#e8eef8" stroke-width="6" fill="none" opacity=".7"/>' for x,y in [(60,500),(280,540),(520,480),(160,640),(440,620),(640,600)])
b+='<path d="M0 400 L800 340 L800 380 L0 440Z" fill="#3a3a44"/><rect x="200" y="330" width="400" height="60" rx="10" fill="#4a4a54" transform="rotate(-4 400 360)"/>'+''.join(f'<rect x="{x}" y="{356-(x-200)*0.07}" width="30" height="20" fill="#ffd27a"/>' for x in range(220,600,50))
I[100]=svg(b,d)

# 134 小さな恋の物語: a small girl and boy's silhouettes sharing an umbrella with a tiny heart, 1973 idol
d,b=bg([(0,'#ffe0ea'),(1,'#e8f0ff')])
b+=rain(30,134,'#a8c8e8',.5)+'<rect y="620" width="800" height="180" fill="#c8d8b8"/>'+figure(360,640,200,'#3a2a4a',hair='#3a2a4a')+figure(440,640,210,'#2a3a5a')+wagasa(400,450,120,'#ffd02a',0)+heart(400,330,20,'#ff4a8a')
I[134]=svg(b,d)

# 349 スローバラード: a couple asleep in a parked car under a starry night by the sea, 1976 soul rock
d,b=bg([(0,'#050a24'),(1,'#1a2a4a')])
b+=starsf(90,349,460)+'<rect y="460" width="800" height="160" fill="#0a1430"/><rect y="620" width="800" height="180" fill="#14141e"/>'
b+='<path d="M200 620 L260 540 L520 540 L600 620 L640 630 L640 670 L160 670 L160 630Z" fill="#2a2a3a"/><path d="M280 552 L500 552 L560 616 L240 616Z" fill="#1a2a4a"/>'+profile(360,616,.35,'#000')+profile(420,616,.35,'#000',True)+'<circle cx="230" cy="672" r="26" fill="#0a0a0a"/><circle cx="560" cy="672" r="26" fill="#0a0a0a"/>'
I[349]=svg(b,d)

# 417 ファースト・デイト: a girl waiting by a clock tower with a small bouquet on a bright Sunday, 80s idol
d,b=bg([(0,'#9ad8ff'),(1,'#fff0f4')])
b+='<rect x="540" y="200" width="100" height="440" fill="#e8dcc8"/><circle cx="590" cy="280" r="40" fill="#fff" stroke="#3a3a4a" stroke-width="6"/><path d="M590 280 L590 252 M590 280 L610 290" stroke="#3a3a4a" stroke-width="5"/>'
b+='<rect y="640" width="800" height="160" fill="#c8b8a8"/>'+figure(300,660,280,'#5a2a4a',hair='#5a2a4a')+''.join(flower(x,y,14,5,c,'#ffd02a') for x,y,c in [(340,470,'#ff8ab0'),(360,450,'#fff'),(350,490,'#ffc0d8')])
I[417]=svg(b,d)

# 1816 メランコリー: a woman in a big floppy hat sitting at a café table with an untouched cake, rainy window, 1976
d,b=bg([(0,'#7a7a9a'),(1,'#b8b8c8')])
b+=rain(40,1816,'#fff',.4,8,500)+'<rect y="500" width="800" height="300" fill="#5a4a4a"/><ellipse cx="560" cy="560" rx="100" ry="20" fill="#f4ece0"/><rect x="556" y="560" width="8" height="140" fill="#3a3a3a"/>'
b+='<path d="M530 540 L580 540 L590 520 L540 520Z" fill="#ffd8e8"/>'+profile(340,700,1.0,'#1a1a24')
I[1816]=svg(b,d)

# 78 白い恋人たち: a couple's silhouettes walking through a snowy forest at night under falling snow, 1970
d,b=bg([(0,'#2a3a5a'),(1,'#8a9ab8')])
b+=snow(120,78)+''.join(f'<path d="M{x} 600 L{x-40} 600 L{x} 400 L{x+40} 600Z" fill="#1a2a3a"/><path d="M{x-20} 480 L{x} 420 L{x+20} 480Z" fill="#f4f6ff"/>' for x in (80,180,620,720))
b+='<rect y="600" width="800" height="200" fill="#e8eef8"/>'+figure(370,660,220,'#0a0a14')+figure(440,660,210,'#0a0a14',hair='#0a0a14')
I[78]=svg(b,d)

# 350 トランジスタ・ラジオ: a tiny transistor radio on a school rooftop with a boy lying beside it, 1980 rock
d,b=bg([(0,'#5ab0ff'),(1,'#e8f8ff')])
b+=cloud(220,160,1.4)+cloud(600,200,1.0)+'<rect y="560" width="800" height="240" fill="#a8a8b0"/>'+''.join(f'<rect x="{x}" y="460" width="8" height="100" fill="#6a6a74"/>' for x in range(0,800,50))+'<rect y="460" width="800" height="8" fill="#6a6a74"/>'
b+='<rect x="480" y="560" width="120" height="80" rx="10" fill="#e8302a"/><circle cx="520" cy="600" r="24" fill="#3a3a3a"/><rect x="560" y="580" width="30" height="10" fill="#fff"/><path d="M590 560 L630 480" stroke="#c8c8c8" stroke-width="4"/>'
b+='<g transform="rotate(-88 300 640)">'+figure(300,720,220,'#1a1a2a')+'</g>'+note(560,440,30,'#3a3a5a')+note(620,400,24,'#3a3a5a')
I[350]=svg(b,d)

# 96 哀愁のカサブランカ: palm trees and a white Moorish arch at a melancholy sunset, 1982 ballad
d,b=bg([(0,'#c84a3a'),(1,'#ffc88a')])
b+='<circle cx="400" cy="520" r="90" fill="#fff0b0"/><rect y="560" width="800" height="240" fill="#e8c88a"/>'
b+='<path d="M0 0 L800 0 L800 800 L0 800Z M240 800 L240 380 Q240 220 400 200 Q560 220 560 380 L560 800Z" fill="#f4ece0" fill-rule="evenodd"/>'+''.join(f'<path d="M{x} 640 Q{x+10} 520 {x+30} 440" stroke="#3a2a2a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x+30} 440 Q{x+30+dx} {400} {x+30+dx*1.4} {460}" stroke="#3a2a2a" stroke-width="8" fill="none"/>' for dx in (-50,50,-30,30)) for x in (280,470))
I[96]=svg(b,d)

# 104 夏にご用心: a red warning sign-shaped heart on a sizzling beach with a huge sun, 1976 idol
d,b=bg([(0,'#ffb02a'),(1,'#fff0a0')])
b+=rays(560,180,20,'#fff',.3,12)+'<circle cx="560" cy="180" r="90" fill="#ff6a2a"/><rect y="500" width="800" height="100" fill="#2a8ad8"/><path d="M0 600 Q400 560 800 600 L800 800 L0 800Z" fill="#f4d890"/>'
b+='<rect x="236" y="460" width="10" height="240" fill="#5a5a5a"/><path d="M240 300 L340 460 L140 460Z" fill="#ffd02a" stroke="#e8302a" stroke-width="10" stroke-linejoin="round"/>'+heart(240,420,24,'#e8302a')
I[104]=svg(b,d)

# 1779 王子様と雪の夜: a girl at a frosty window looking out at a lone figure on a horse in snow, 2001 idol
d,b=bg([(0,'#1a2440'),(1,'#5a6a9a')])
b+=snow(80,1779)+'<rect y="600" width="800" height="200" fill="#e8eef8"/>'+moon(160,140,40)
b+='<path d="M480 600 L490 540 L500 500 Q520 470 580 470 L640 470 L660 440 L680 450 L670 490 L660 540 L650 600 L630 600 L630 540 L520 540 L510 600Z" fill="#0a0a14"/>'+figure(570,490,120,'#0a0a14')
b+='<rect x="0" y="200" width="300" height="400" fill="#3a2a2a"/><rect x="60" y="280" width="180" height="200" fill="#ffd27a"/>'+profile(170,480,.45,'#5a3a2a',True)
I[1779]=svg(b,d)

# 202 ジェラシー: a phone off the hook and a lipstick-marked cigarette-free glass on a midnight table, 1981
d,b=bg([(0,'#1a0a14'),(1,'#3a1a24')])
b+=glow(400,300,240,'#ff6a5a',.25)+'<rect y="520" width="800" height="280" fill="#3a2020"/>'+phone(260,460,1.0,'#1a1a1a')+'<path d="M300 500 Q360 600 280 640" stroke="#1a1a1a" stroke-width="5" fill="none"/>'
b+='<path d="M480 400 L560 400 L550 520 L490 520Z" fill="#f4ece0" opacity=".5"/><path d="M500 404 q10 8 20 0" stroke="#c8102a" stroke-width="6" fill="none"/>'+profile(700,520,.7,'#0a0a10',True)
I[202]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
