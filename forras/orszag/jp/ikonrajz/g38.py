import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 38. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 851 VERB: a figure sprinting through a burst of motion streaks, action itself, 2009 rock
d,b=bg([(0,'#1a1a3a'),(1,'#e8502a')])
b+=''.join(f'<path d="M{x} {y} L{x-300} {y}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" opacity=".8"/>' for x,y,c,w in [(380,300,'#ffd02a',10),(360,380,'#fff',6),(400,460,'#ffd02a',14),(340,540,'#fff',8),(380,620,'#ffd02a',6)])
b+='<g transform="rotate(12 480 480)">'+figure(480,720,380,'#0a0a14',pose='up')+'</g>'
I[851]=svg(b,d)

# 1187 レーザービーム: crossing green and pink laser beams slicing a dark dancefloor with a mirrored triangle
d,b=bg([(0,'#000008'),(1,'#0a0a20')])
b+=''.join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{c}" stroke-width="5" opacity=".9"/>' for x1,y1,x2,y2,c in [(0,100,800,600,'#3aff8a'),(0,600,800,120,'#ff4fd0'),(400,0,200,800,'#3affe8'),(800,300,0,420,'#3aff8a'),(400,0,640,800,'#ff4fd0')])
b+=glow(400,400,120,'#fff',.5)+'<circle cx="400" cy="400" r="18" fill="#fff"/>'+figure(400,780,300,'#000',pose='up',hair='#000')+'<rect y="660" width="800" height="140" fill="#0a0a14"/>'
I[1187]=svg(b,d)

# 1774 あなたのキスを数えましょう: a string of red lipstick kiss-shaped hearts on a pale letter beside a fading photo
d,b=bg([(0,'#2a2a3a'),(1,'#5a4a5a')])
b+='<rect x="160" y="160" width="480" height="480" fill="#f4ece4" transform="rotate(-4 400 400)"/>'
b+=''.join(heart(x,y,30,'#c8102a',' opacity="%s"'%o) for x,y,o in [(260,280,1),(380,320,.85),(500,280,.7),(300,440,.55),(440,470,.4),(540,420,.25)])
b+='<rect x="460" y="500" width="150" height="120" fill="#c8b8a8" transform="rotate(8 535 560)"/>'+profile(540,620,.35,'#7a6a5a')
I[1774]=svg(b,d)

# 124 ペッパー警部: a police badge with a pepper shaker beside it under disco spotlights, late-70s idol duo
d,b=bg([(0,'#1a1a5a'),(1,'#5a3aa8')])
b+=rays(400,0,10,'#fff',.12,30,40,140)+'<path d="M300 280 L400 240 L500 280 L500 420 Q500 520 400 560 Q300 520 300 420Z" fill="#c8a24a"/><path d="M330 300 L400 270 L470 300 L470 420 Q470 500 400 530 Q330 500 330 420Z" fill="#e8c86a"/>'+star5(400,400,60,'#c8a24a')
b+='<rect x="560" y="440" width="90" height="180" rx="20" fill="#f4f0e8"/><path d="M560 470 Q605 380 650 470Z" fill="#9a9aa8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#3a3a3a"/>' for x,y in [(590,430),(605,420),(620,430)])
I[124]=svg(b,d)

# 136 あの鐘を鳴らすのはあなた: a great temple-style bronze bell swinging in golden light, powerful soul ballad
d,b=bg([(0,'#3a1a0a'),(1,'#c8702a')])
b+=rays(400,300,20,'#ffd02a',.12,14)+'<rect x="180" y="140" width="440" height="24" fill="#3a1a0a"/><rect x="390" y="164" width="20" height="60" fill="#3a1a0a"/>'
b+='<path d="M300 560 Q300 230 400 220 Q500 230 500 560Z" fill="#a8783a"/><rect x="290" y="540" width="220" height="30" rx="8" fill="#8a5a2a"/>'+''.join(f'<rect x="{x}" y="300" width="20" height="200" fill="#8a5a2a"/>' for x in (330,380,430))+glow(400,420,240,'#ffd02a',.3)
b+=''.join(f'<path d="M{x} 600 q{dx} 30 {2*dx} 0" stroke="#ffd02a" stroke-width="5" fill="none"/>' for x,dx in [(260,-40),(540,40),(250,-60),(560,60)])
I[136]=svg(b,d)

# 203 赤ちょうちん: a small red paper lantern hanging over an alley in a poor 70s neighbourhood at night
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+='<rect x="0" y="100" width="260" height="700" fill="#2a2024"/><rect x="540" y="100" width="260" height="700" fill="#2a2024"/><path d="M260 800 L360 300 L440 300 L540 800Z" fill="#3a3030"/>'
b+=chochin(250,300,80)+glow(250,340,180,'#ff6a3a',.4)+'<rect x="560" y="360" width="160" height="140" fill="#ffd27a" opacity=".6"/>'+figure(420,640,140,'#000')+figure(370,640,150,'#000',hair='#000')
I[203]=svg(b,d)

# 332 純愛ラプソディ: a red heart pierced by music staff lines flowing like ribbons, 90s ballad
d,b=bg([(0,'#ffe0e8'),(1,'#f4d0f0')])
b+=''.join(f'<path d="M-20 {y} Q200 {y-100} 400 {y} T820 {y}" stroke="#c87aa8" stroke-width="3" fill="none"/>' for y in range(360,460,20))+heart(400,420,110,'#e8203a')
b+=note(180,300,40,'#c87aa8')+note(620,520,40,'#c87aa8',True)
I[332]=svg(b,d)

# 571 ストレンジャーtonight: a woman's silhouette under a streetlamp, a fedora-wearing stranger's shadow nearing
d,b=bg([(0,'#0a0a24'),(1,'#2a1a4a')])
b+='<rect y="620" width="800" height="180" fill="#14142a"/><rect x="300" y="200" width="10" height="420" fill="#3a3a4a"/><path d="M280 200 L330 200 L320 180 L290 180Z" fill="#3a3a4a"/>'+'<path d="M305 210 L180 620 L430 620Z" fill="#fff4c8" opacity=".25"/>'
b+=figure(310,620,220,'#000',hair='#000')+figure(620,620,300,'#000')+'<ellipse cx="620" cy="330" rx="56" ry="12" fill="#000"/><path d="M590 330 Q620 290 650 330Z" fill="#000"/>'+'<path d="M600 620 L340 680" stroke="#000" stroke-width="40" opacity=".5"/>'
I[571]=svg(b,d)

# 1129 FIND THE WAY: a lantern held up in a misty forest revealing a path ahead, 2003 anime ballad
d,b=bg([(0,'#1a2a3a'),(1,'#5a7a8a')])
b+=''.join(f'<rect x="{x}" y="0" width="{w}" height="800" fill="#0a1420" opacity=".8"/>' for x,w in [(40,40),(160,30),(600,50),(720,36)])+'<path d="M300 800 Q380 600 400 440 Q420 600 520 800Z" fill="#8aa0a8" opacity=".5"/>'
b+=figure(400,700,240,'#0a1420')+'<rect x="440" y="470" width="30" height="40" rx="6" fill="#ffd27a"/>'+glow(455,490,140,'#ffd27a',.6)
I[1129]=svg(b,d)

# 1262 星をめざして: a group of silhouettes pointing toward a rising shooting star, hopeful boy group
d,b=bg([(0,'#0a1440'),(1,'#5a3a8a')])
b+=starsf(80,1262,600)+'<path d="M200 500 Q400 300 620 160" stroke="#fff4c8" stroke-width="5" fill="none" opacity=".7"/>'+star5(620,160,40,'#fff4c8')+glow(620,160,70,'#fff4c8',.6)
b+='<rect y="640" width="800" height="160" fill="#0a0a1a"/>'+''.join(figure(x,780,200,'#000',pose=p) for x,p in [(220,'stand'),(320,'up'),(420,'stand'),(520,'up')])
I[1262]=svg(b,d)

# 443 じれったい: a phone off the hook and a clock ticking past midnight, impatient 80s rock
d,b=bg([(0,'#1a0a14'),(1,'#4a1a2a')])
b+='<circle cx="560" cy="260" r="140" fill="#f4f0e8" stroke="#c8a24a" stroke-width="12"/><path d="M560 260 L560 150 M560 260 L620 300" stroke="#1a1a1a" stroke-width="10" stroke-linecap="round"/>'+''.join(f'<rect x="557" y="128" width="6" height="18" fill="#1a1a1a" transform="rotate({a} 560 260)"/>' for a in range(0,360,30))
b+='<rect x="100" y="600" width="600" height="200" fill="#3a1a1a"/>'+phone(260,520,1.2,'#e8302a')+'<path d="M300 580 Q340 680 260 700 Q180 720 220 640" stroke="#e8302a" stroke-width="5" fill="none"/>'
I[443]=svg(b,d)

# 468 恋のロープをほどかないで: a pink rope tied in a loose knot between two pinkies, 80s idol
d,b=bg([(0,'#ffe0ee'),(1,'#e8f0ff')])
b+='<path d="M0 600 Q140 560 240 470 L280 500 Q180 590 0 680Z" fill="#f4c8a8"/><path d="M800 600 Q660 560 560 470 L520 500 Q620 590 800 680Z" fill="#e8b494"/>'
b+='<path d="M260 480 Q330 380 400 440 Q460 500 400 520 Q350 520 370 460 Q420 380 540 480" stroke="#ff4a8a" stroke-width="14" fill="none" stroke-linecap="round"/>'+sparkle(400,260,24,'#ff8ab0')
I[468]=svg(b,d)

# 790 Utsukushikihana: a single white lily blooming in a quiet ink-blue night garden, 2006 ballad
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+=moon(620,160,50)+'<path d="M380 800 Q370 600 400 440" stroke="#3a6a3a" stroke-width="12" fill="none"/><path d="M390 620 q-90 -40 -120 20 q70 20 120 -20Z" fill="#3a6a3a"/>'
b+=''.join(f'<path d="M400 430 Q{400+90*math.cos(a)} {430+90*math.sin(a)-40} {400+160*math.cos(a)} {430+160*math.sin(a)} Q{400+70*math.cos(a)} {430+70*math.sin(a)+20} 400 430Z" fill="#f4f4ff"/>' for a in [-math.pi/2+k*2*math.pi/6 for k in range(6)])+'<circle cx="400" cy="430" r="16" fill="#ffd02a"/>'+glow(400,430,160,'#fff',.25)
I[790]=svg(b,d)

# 811 ALICE: a falling pocket watch and a playing card tumbling down a rabbit hole of swirls, 90s pop
d,b=bg([(0,'#2a1a4a'),(1,'#8a6ac8')])
b+=''.join(ring(400,400,r,'#fff',3,.15+r/2000) for r in range(60,520,60))
b+='<g transform="rotate(-20 300 300)"><circle cx="300" cy="300" r="70" fill="#f4f0e8" stroke="#c8a24a" stroke-width="12"/><path d="M300 300 L300 250 M300 300 L330 320" stroke="#1a1a1a" stroke-width="6"/><rect x="290" y="210" width="20" height="20" fill="#c8a24a"/></g>'
b+='<g transform="rotate(25 520 520)"><rect x="460" y="430" width="120" height="170" rx="10" fill="#fff"/>'+heart(520,515,30,'#e8102a')+'</g>'
I[811]=svg(b,d)

# 1263 太陽のナミダ: a glowing sun shedding a single golden tear over a calm ocean
d,b=bg([(0,'#ff7a3a'),(1,'#ffd88a')])
b+='<circle cx="400" cy="300" r="130" fill="#ffe04a"/>'+glow(400,300,180,'#fff4a0',.5)+'<rect y="500" width="800" height="300" fill="#e8803a"/>'+''.join(f'<rect x="{360-k*10}" y="{530+k*40}" width="{80+k*20}" height="8" fill="#ffe04a" opacity=".7"/>' for k in range(6))
b+='<path d="M400 450 Q424 486 400 506 Q376 486 400 450Z" fill="#fff4a0"/>'
I[1263]=svg(b,d)

# 1666 陽のあたる坂道: a sunlit uphill street with a bicycle being pushed toward the bright top
d,b=bg([(0,'#6ac8ff'),(1,'#fff4d8')])
b+='<circle cx="600" cy="140" r="70" fill="#fff8c8"/>'+rays(600,140,16,'#fff',.25,10)+'<path d="M0 800 L0 600 L800 360 L800 800Z" fill="#c8b8a0"/><path d="M0 640 L800 400" stroke="#fff" stroke-width="4" stroke-dasharray="30 20"/>'
b+='<g transform="rotate(-16 400 560)">'+ring(340,580,40,'#1a1a1a',6)+ring(470,580,40,'#1a1a1a',6)+'<path d="M340 580 L400 530 L470 580 M400 530 L430 510" stroke="#1a1a1a" stroke-width="6" fill="none"/></g>'+figure(300,640,200,'#1a1a2a',hair='#1a1a2a')
I[1666]=svg(b,d)

# 1693 落葉が雪に: falling autumn leaves turning into snowflakes halfway down, a 70s ballad
d,b=bg([(0,'#c8784a'),(1,'#d8e4f0')])
b+=''.join(f'<path d="M{x} {y} q20 -30 40 0 q-20 30 -40 0Z" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,c,r in [(120,120,'#c8402a',20),(320,90,'#e8802a',-30),(520,140,'#c8602a',40),(680,100,'#e8a02a',-10),(220,260,'#e8802a',60),(600,300,'#c8402a',0)])
b+=snow(50,1693,.9)+'<rect y="660" width="800" height="140" fill="#f4f8ff"/>'
I[1693]=svg(b,d)

# 1786 貴方の恋人になりたいのです: a girl with an acoustic guitar sitting on a bed, a heart doodle on the wall
d,b=bg([(0,'#ffe8d8'),(1,'#f0d8e8')])
b+='<rect x="100" y="540" width="600" height="160" fill="#f4f4f4"/><rect x="100" y="680" width="600" height="120" fill="#c8a0b0"/>'+heart(560,260,60,'none',' stroke="#e8508a" stroke-width="6"')
b+=figure(380,640,260,'#3a2a3a',hair='#3a2a3a')+guitar(400,540,.7,-30,'#c8702a')
I[1786]=svg(b,d)

# 177 初恋列車: a little local train crossing a countryside bridge at sunset with a heart puff of steam, enka
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=hills(520,60,'#8a6a8a',177,4)+'<rect y="560" width="800" height="240" fill="#5a7a9a"/><rect x="0" y="540" width="800" height="20" fill="#3a2a2a"/>'+''.join(f'<path d="M{x} 560 Q{x+60} 640 {x+120} 560" stroke="#3a2a2a" stroke-width="10" fill="none"/>' for x in range(0,800,120))
b+='<rect x="220" y="450" width="200" height="90" rx="10" fill="#c8302a"/><rect x="430" y="450" width="200" height="90" rx="10" fill="#c8302a"/>'+''.join(f'<rect x="{x}" y="470" width="30" height="30" fill="#ffe8b0"/>' for x in (240,290,340,450,500,550))
b+=heart(240,370,40,'#fff',' opacity=".8"')
I[177]=svg(b,d)

# 216 Yes: a hand holding out a small open ring box toward a sunset window, early-80s ballad
d,b=bg([(0,'#ffb08a'),(1,'#f8e0d0')])
b+='<rect x="440" y="80" width="300" height="400" fill="#ffd0a0"/><rect x="440" y="80" width="300" height="400" fill="none" stroke="#7a5a4a" stroke-width="14"/><circle cx="590" cy="380" r="60" fill="#fff0c0"/>'
b+='<path d="M0 640 Q120 600 220 540 L300 540 L300 620 Q180 640 0 720Z" fill="#3a2a2a"/><rect x="260" y="480" width="140" height="80" rx="8" fill="#8a1a2a"/><path d="M260 480 L280 400 L420 400 L400 480Z" fill="#a82a3a"/>'
b+=ring(330,500,26,'#e8c86a',8)+sparkle(330,470,16,'#fff')
I[216]=svg(b,d)

# 217 愛を止めないで: two hands almost touching as a flock of white birds bursts upward, 1978
d,b=bg([(0,'#7ab0e8'),(1,'#fff0e0')])
b+='<path d="M0 560 Q160 540 300 500 L340 530 Q200 590 0 640Z" fill="#f4c8a8"/><path d="M800 560 Q640 540 500 500 L460 530 Q600 590 800 640Z" fill="#e8b494"/>'
b+=''.join(bird(x,y,s,'#fff') for x,y,s in [(400,420,40),(350,340,30),(450,300,34),(400,220,26),(320,240,22),(500,200,24)])+glow(400,500,80,'#fff',.6)
I[217]=svg(b,d)

# 341 Rydeen: a galloping horse silhouette made of synthesizer waveform lines racing across a neon plain, 1979 techno
d,b=bg([(0,'#0a0a24'),(1,'#1a2a5a')])
b+=''.join(f'<path d="M0 {y} '+' '.join(f'L{x} {y+((x//40)%2)*20-10}' for x in range(0,820,40))+f'" stroke="#3affe8" stroke-width="3" fill="none" opacity="{o}"/>' for y,o in [(600,.8),(650,.5),(700,.3)])
b+=bolt([(420,60),(340,260),(420,280),(330,480)],'#ffd02a',14)+glow(380,280,160,'#ffd02a',.4)+'<rect x="120" y="480" width="560" height="120" rx="10" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="520" width="22" height="70" fill="#f4f4f4"/>' for x in range(140,660,26))+''.join(f'<rect x="{x}" y="520" width="14" height="40" fill="#1a1a1a"/>' for x in range(158,650,52))+''.join(f'<circle cx="{x}" cy="500" r="7" fill="#e8302a"/>' for x in range(160,660,40))
I[341]=svg(b,d)

# 565 秋からも、そばにいて: two silhouettes on a bench under falling maple leaves, 80s idol autumn
d,b=bg([(0,'#e89a5a'),(1,'#f8dcb0')])
b+=tree(620,620,460,'#c8402a',565)+''.join(f'<path d="M{x} {y} q14 -20 28 0 q-14 20 -28 0Z" fill="#c8402a" transform="rotate({x%90} {x} {y})"/>' for x,y in [(120,200),(260,300),(420,180),(180,460),(500,420)])
b+='<rect y="620" width="800" height="180" fill="#a8704a"/><rect x="220" y="560" width="300" height="14" fill="#3a2a2a"/><rect x="230" y="574" width="10" height="50" fill="#3a2a2a"/><rect x="500" y="574" width="10" height="50" fill="#3a2a2a"/>'
b+=figure(320,620,180,'#2a1a1a',hair='#2a1a1a')+figure(420,620,190,'#2a1a1a')
I[565]=svg(b,d)

# 1720 Because of You: a young man dancing in the rain under a single bright streetlight, 2002 pop
d,b=bg([(0,'#1a2440'),(1,'#3a4a6a')])
b+=rain(80,1720,'#cfe6ff',.4)+'<rect x="560" y="160" width="10" height="500" fill="#3a3a4a"/><circle cx="565" cy="160" r="20" fill="#fff4c8"/>'+'<path d="M565 170 L380 660 L760 660Z" fill="#fff4c8" opacity=".2"/>'
b+='<rect y="660" width="800" height="140" fill="#14182a"/>'+figure(480,660,280,'#000',pose='up')+'<ellipse cx="480" cy="680" rx="160" ry="14" fill="#8ab0e8" opacity=".3"/>'
I[1720]=svg(b,d)

# 1761 悲しみよ こんにちは: a girl waving at a small grey raincloud that follows her on a sunny day, 80s idol
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+='<circle cx="660" cy="140" r="60" fill="#fff4a0"/><rect y="600" width="800" height="200" fill="#8ac86a"/>'+cloud(300,260,1.2,'#9a9aa8')+rain(14,1761,'#5a7aa8',.6,0,600)
b+=figure(460,620,260,'#2a2a3a',pose='up',hair='#2a2a3a')
I[1761]=svg(b,d)

# 204 22才の別れ: a cake with 22 candles and an empty chair, a farewell in a 70s apartment
d,b=bg([(0,'#3a2a2a'),(1,'#6a4a3a')])
b+='<rect x="100" y="520" width="600" height="30" fill="#8a5a3a"/><rect x="0" y="550" width="800" height="250" fill="#2a1a14"/>'
b+='<rect x="260" y="420" width="220" height="100" rx="10" fill="#f4e8d8"/><rect x="260" y="440" width="220" height="16" fill="#ff8ab0"/>'+''.join(f'<rect x="{x}" y="370" width="6" height="50" fill="#ffc0d0"/><path d="M{x+3} 352 q6 10 0 18 q-6 -8 0 -18Z" fill="#ffd02a"/>' for x in range(276,470,18))+glow(370,360,140,'#ffd27a',.4)
b+='<rect x="560" y="440" width="12" height="160" fill="#8a6a4a"/><rect x="560" y="520" width="100" height="12" fill="#8a6a4a"/><rect x="648" y="532" width="10" height="70" fill="#8a6a4a"/>'
I[204]=svg(b,d)

# 218 眠れぬ夜: a sleepless figure sitting on a windowsill, a clock and a crescent moon, 70s
d,b=bg([(0,'#0a1028'),(1,'#1a2448')])
b+='<rect x="200" y="100" width="400" height="460" fill="#14204a"/>'+starsf(30,218,500)+'<path d="M500 180 A60 60 0 1 0 540 280 A48 48 0 1 1 500 180Z" fill="#fff4c8"/>'
b+='<rect x="200" y="100" width="400" height="460" fill="none" stroke="#3a3a54" stroke-width="18"/><rect x="180" y="560" width="440" height="24" fill="#3a3a54"/>'
b+='<g transform="translate(260 480)">'+figure(0,80,180,'#000')+'</g><circle cx="680" cy="200" r="50" fill="#e8e0d0"/><path d="M680 200 L680 165 M680 200 L705 215" stroke="#1a1a1a" stroke-width="5"/>'
I[218]=svg(b,d)

# 261 関白宣言: a traditional low table with a teacup and a folded declaration scroll, 1979 folk
d,b=bg([(0,'#e8dcc0'),(1,'#c8b890')])
b+='<rect x="0" y="0" width="800" height="400" fill="#f4ecd8"/>'+''.join(f'<rect x="{x}" y="0" width="8" height="400" fill="#a8906a"/>' for x in range(100,800,200))+'<rect y="400" width="800" height="400" fill="#c8b070"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#a89050" stroke-width="3"/>' for y in range(440,800,60))
b+='<rect x="160" y="500" width="480" height="30" fill="#5a3a2a"/><rect x="190" y="530" width="20" height="80" fill="#5a3a2a"/><rect x="590" y="530" width="20" height="80" fill="#5a3a2a"/>'
b+='<path d="M260 500 L270 450 L330 450 L340 500Z" fill="#4a6a5a"/><rect x="400" y="460" width="180" height="40" fill="#f4f0e4"/><circle cx="400" cy="480" r="20" fill="#c8a870"/><circle cx="580" cy="480" r="20" fill="#c8a870"/>'
I[261]=svg(b,d)

# 503 シェリー: a lone youth on a city crosswalk at night beneath a giant blurred neon heart, 80s rock
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=skyline(560,'#14142a',503,100,320,'#ff8ad0',60)+'<rect y="560" width="800" height="240" fill="#14141e"/>'+''.join(f'<rect x="{x}" y="600" width="50" height="140" fill="#3a3a44"/>' for x in range(60,760,90))
b+=glow(400,260,150,'#ff4a8a',.5)+heart(400,260,70,'none',' stroke="#ff4a8a" stroke-width="8"')+figure(400,720,220,'#000')
I[503]=svg(b,d)

# 526 サンキュ.: a friend's hand passing a warm canned drink on a cold night bench, 90s pop
d,b=bg([(0,'#1a2a4a'),(1,'#4a5a8a')])
b+=starsf(40,526,400)+'<rect x="120" y="560" width="560" height="20" fill="#5a3a2a"/><rect x="140" y="580" width="16" height="220" fill="#5a3a2a"/><rect x="644" y="580" width="16" height="220" fill="#5a3a2a"/>'
b+='<path d="M0 480 Q160 440 300 430 L320 470 Q160 500 0 540Z" fill="#c8a088"/><path d="M800 480 Q640 440 500 430 L480 470 Q640 500 800 540Z" fill="#b89078"/>'
b+='<rect x="370" y="380" width="60" height="110" rx="10" fill="#e8402a"/><rect x="370" y="410" width="60" height="20" fill="#ffd02a"/>'+''.join(f'<path d="M{x} 360 q10 -20 0 -40" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>' for x in (385,415))
I[526]=svg(b,d)

# 539 今日も どこかで: many small lit windows across a hillside town at dusk, each a different life
d,b=bg([(0,'#4a5a9a'),(1,'#ffb88a')])
b+=hills(420,60,'#6a5a7a',539,4)+'<path d="M0 520 Q400 420 800 520 L800 800 L0 800Z" fill="#3a3048"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="40" height="34" fill="#4a3a58"/><rect x="{x+10}" y="{y+8}" width="14" height="14" fill="#ffd27a"/>' for x,y in [(random.Random(539*k).randint(20,740),random.Random(539*k+3).randint(500,760)) for k in range(30)])
I[539]=svg(b,d)

# 1056 アシタヘカエル: a figure walking home along a long road toward a dawn-lit horizon with a backpack, R&B duo
d,b=bg([(0,'#2a3a6a'),(1,'#ffc89a')])
b+='<circle cx="400" cy="500" r="60" fill="#fff0c0"/>'+rays(400,500,20,'#fff',.15,8)+'<rect y="500" width="800" height="300" fill="#4a4a5a"/><path d="M390 500 L200 800 L600 800 L410 500Z" fill="#6a6a7a"/>'
b+=figure(420,700,200,'#0a0a14')+'<rect x="430" y="560" width="40" height="60" rx="10" fill="#0a0a14"/>'
I[1056]=svg(b,d)

# 1762 青空のかけら: a girl holding up a jigsaw puzzle piece of blue sky against a grey overcast day
d,b=bg([(0,'#8a909a'),(1,'#c8ccd4')])
b+='<rect y="640" width="800" height="160" fill="#7a808a"/>'+figure(340,660,300,'#2a2a34',pose='up',hair='#2a2a34')
b+='<path d="M380 160 L480 160 Q470 130 500 120 Q530 130 520 160 L600 160 L600 230 Q630 220 640 250 Q630 280 600 270 L600 340 L380 340Z" fill="#3ab0ff"/>'+cloud(470,250,.6)
I[1762]=svg(b,d)

# 3 真赤な太陽: an enormous crimson sun over a 60s beach with a go-go dancer silhouette
d,b=bg([(0,'#ff6a2a'),(1,'#ffc86a')])
b+='<circle cx="400" cy="400" r="240" fill="#e8102a"/><rect y="520" width="800" height="100" fill="#2a6ab8"/><rect y="620" width="800" height="180" fill="#f0c880"/>'
b+=figure(400,700,300,'#1a0a0a',pose='up',hair='#1a0a0a')
I[3]=svg(b,d)

# 92 GOLDFINGER'99: a golden pointing glove under a mirror ball, Latin pop fever
d,b=bg([(0,'#1a0a2a'),(1,'#a82a4a')])
b+='<line x1="400" y1="0" x2="400" y2="100" stroke="#aaa" stroke-width="3"/><circle cx="400" cy="160" r="60" fill="#d8d8e8"/>'+''.join(f'<rect x="{x}" y="{y}" width="14" height="14" fill="#fff"/>' for x,y in [(370,130),(410,150),(380,180),(420,120)])+rays(400,160,16,'#ffd02a',.12,10)
b+='<circle cx="400" cy="520" r="170" fill="#c8982a"/>'+''.join(ring(400,520,r,'#a87a1a',3) for r in range(80,170,16))+'<circle cx="400" cy="520" r="50" fill="#ffe08a"/>'+glow(400,520,200,'#ffd02a',.35)+sparkle(240,360,24,'#fff4c8')+sparkle(580,400,18,'#fff4c8')
I[92]=svg(b,d)

# 184 元気です: a man sitting on a grassy riverside slope strumming a guitar under a big blue sky, 70s folk
d,b=bg([(0,'#4ab0f0'),(1,'#d8f0ff')])
b+=cloud(180,180,1.2)+cloud(600,140,.9)+'<path d="M0 520 Q400 460 800 540 L800 800 L0 800Z" fill="#6ab84a"/><path d="M0 660 Q400 620 800 680 L800 800 L0 800Z" fill="#4a9ae0"/>'
b+=figure(380,580,170,'#1a2a1a')+guitar(400,520,.5,40,'#c8702a')
I[184]=svg(b,d)

# 527 LAT.43°N: a snowy northern city at night with a compass needle pointing north and a distant phone line
d,b=bg([(0,'#0a1a3a'),(1,'#3a5a8a')])
b+=snow(70,527)+skyline(640,'#1a2a4a',527,60,200,'#ffd27a',50)+'<rect y="640" width="800" height="160" fill="#e8eef8"/>'
b+='<circle cx="400" cy="300" r="140" fill="#f4f0e8" opacity=".9"/><circle cx="400" cy="300" r="140" fill="none" stroke="#c8a24a" stroke-width="10"/><polygon points="400,180 420,300 380,300" fill="#e8302a"/><polygon points="400,420 420,300 380,300" fill="#3a3a4a"/><circle cx="400" cy="300" r="10" fill="#c8a24a"/>'
I[527]=svg(b,d)

# 1737 僕だって泣いちゃうよ: a boy's silhouette from behind, shoulders shaking, rain on a school rooftop
d,b=bg([(0,'#5a6a8a'),(1,'#a8b8cc')])
b+=rain(80,1737,'#e8f0ff',.4)+'<rect y="560" width="800" height="240" fill="#7a8494"/>'+''.join(f'<rect x="{x}" y="440" width="8" height="120" fill="#4a5060"/>' for x in range(0,800,50))+'<rect y="440" width="800" height="10" fill="#4a5060"/>'
b+=figure(400,640,300,'#1a1a24')+'<path d="M330 330 L300 300 M470 330 L500 300" stroke="#1a1a24" stroke-width="6"/>'
I[1737]=svg(b,d)

# 1776 愛のバカやろう: a girl shouting into a megaphone at the sea from a breakwater, comedic 2001 enka-pop
d,b=bg([(0,'#3a8ae8'),(1,'#c8e8ff')])
b+='<rect y="460" width="800" height="340" fill="#2a6ab8"/>'+''.join(f'<path d="M{x} {y} q30 -10 60 0" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>' for x,y in [(500,520),(620,600),(560,700)])+'<rect x="0" y="560" width="440" height="240" fill="#9a9aa0"/>'
b+=figure(280,560,240,'#1a1a2a',hair='#1a1a2a')+'<path d="M320 400 L420 360 L420 460 L320 420Z" fill="#e8302a"/>'+''.join(f'<path d="M{440+k*30} {380-k*10} q20 30 0 60" stroke="#fff" stroke-width="5" fill="none"/>' for k in range(3))+heart(640,220,40,'#ff4a6a')
I[1776]=svg(b,d)

# 1869 My Sweet Darlin': a girl pedalling a bicycle with a giant heart-shaped balloon tied on, bright 2000 pop
d,b=bg([(0,'#ffd04a'),(1,'#fff0c0')])
b+='<rect y="620" width="800" height="180" fill="#5ab84a"/>'+ring(320,620,60,'#1a1a1a',8)+ring(500,620,60,'#1a1a1a',8)+'<path d="M320 620 L400 540 L500 620 M400 540 L440 520" stroke="#1a1a1a" stroke-width="8" fill="none"/>'
b+=figure(410,560,200,'#1a1a2a',hair='#1a1a2a')+'<path d="M300 560 Q260 400 220 280" stroke="#555" stroke-width="3" fill="none"/>'+heart(220,240,70,'#ff3a6a')
I[1869]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
