import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 16. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 715 夏を待ちきれなくて: a surfboard leaning on a beach hut, the calendar on its wall with July circled, sea sparkling
d,b=bg([(0,'#2ab0f8'),(1,'#bfeaff')])
b+=hinomaru_sun(640,140,70,'#fff6c8',.9)+'<rect y="360" width="800" height="160" fill="#1a8ad8"/>'+''.join(f'<rect x="{(k*157)%760}" y="{380+k*12}" width="40" height="4" fill="#fff" opacity=".7"/>' for k in range(12))+'<path d="M-10 500 Q400 470 810 500 L810 810 L-10 810Z" fill="#f4dca0"/>'
b+='<rect x="120" y="300" width="320" height="400" fill="#e8f4f8"/><path d="M100 300 L280 220 L460 300Z" fill="#e8402a"/><rect x="180" y="380" width="120" height="120" fill="#fff"/><rect x="180" y="380" width="120" height="30" fill="#e8402a"/><text x="240" y="470" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="54" fill="#3a3a5a">7</text>'+ring(240,452,40,'#e8102a',5)
b+='<g transform="rotate(12 540 520)"><ellipse cx="540" cy="520" rx="56" ry="230" fill="#ffd02a"/><path d="M540 300 L540 740" stroke="#e8402a" stroke-width="12"/></g>'
I[715]=svg(b,d)

# 781 生きてる生きてく: a tiny sprout pushing up through a crack in the asphalt, morning sun warming it
d,b=bg([(0,'#ffe0a8'),(1,'#ffcf8a')])
b+=rays(400,180,20,'#fff',.25,10)+hinomaru_sun(400,180,90,'#fff8e0',.9)
b+='<rect y="520" width="800" height="280" fill="#5a5a64"/><path d="M200 520 L260 600 L340 580 L400 700 L460 620 L560 660 L620 520" stroke="#2a2a34" stroke-width="10" fill="none"/><path d="M0 680 L800 680" stroke="#ffd02a" stroke-width="14" stroke-dasharray="80 60"/>'
b+='<path d="M400 640 Q396 560 404 480" stroke="#4aa83a" stroke-width="10" fill="none"/><path d="M402 520 Q340 480 330 440 Q380 450 402 510Z M404 500 Q470 450 490 420 Q430 420 404 490Z" fill="#6ac84a"/>'+glow(404,480,60,'#fff8c8',.4)
I[781]=svg(b,d)

# 793 CRAZY GONNA CRAZY: a strobe-lit dance floor with a silhouette mid-spin, laser lines crossing overhead
d,b=bg([(0,'#1a0a3a'),(1,'#0a0414')])
for k,c in enumerate(['#ff2a8a','#2ae8ff','#aaff2a','#ff2a8a','#2ae8ff']): b+=f'<path d="M{k*200-50} 0 L{800-k*160} 520" stroke="{c}" stroke-width="4" opacity=".8"/>'
for i in range(6):
    for j in range(3): b+=f'<polygon points="{i*140-20+j*30},{560+j*80} {i*140+120+j*30},{560+j*80} {i*140+140+j*40},{640+j*80} {i*140+j*40},{640+j*80}" fill="{["#ff2a8a","#2ae8ff","#aaff2a","#ffd02a"][(i+j)%4]}" opacity=".7"/>'
b+=figure(400,580,320,'#000',pose='up')+'<circle cx="400" cy="120" r="50" fill="#c8c8d8"/>'+''.join(f'<rect x="{360+(k%5)*16}" y="{80+(k//5)*16}" width="12" height="12" fill="#fff" opacity=".7"/>' for k in range(25))
I[793]=svg(b,d)

# 799 Is this love: two shadows on a pier at night almost touching hands, a question-mark shaped crescent moon
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=starsf(50,799,400,'#fff')+moon(600,170,60)+'<circle cx="625" cy="155" r="54" fill="#0a1438"/><rect y="460" width="800" height="340" fill="#0a1a3a"/>'+''.join(f'<rect x="{560+(k%3)*20}" y="{480+k*24}" width="{50-k*3}" height="4" fill="#fff6dc" opacity=".5"/>' for k in range(10))
b+='<rect x="0" y="600" width="800" height="40" fill="#3a2a2a"/>'+figure(300,610,250,'#06081a')+figure(500,610,240,'#06081a',hair='#06081a')+'<path d="M340 470 L460 470" stroke="#ff8ab0" stroke-width="3" stroke-dasharray="4 8"/>'
I[799]=svg(b,d)

# 907 TAKE ME HIGHER: a silhouette hanging from a giant balloon bunch rising above a skyline at dawn
d,b=bg([(0,'#5ab0ff'),(1,'#ffe0b0')])
b+=skyline(640,'#5a6a8a',907,60,200,'#ffe0b0',30)+cloud(160,560,1.2)
for k,(x,y,c) in enumerate([(360,160,'#e8102a'),(440,140,'#ffd02a'),(400,90,'#2a8ae8'),(320,100,'#3ac85a'),(480,90,'#ff5ab8'),(400,200,'#a87aff')]): b+=f'<path d="M{x} {y+40} L400 360" stroke="#fff" stroke-width="2"/><ellipse cx="{x}" cy="{y}" rx="40" ry="48" fill="{c}"/>'
b+=figure(400,520,180,'#1a1a3a',pose='up')
I[907]=svg(b,d)

# 1001 Endless sorrow: a single white rose on an infinite staircase descending into blue darkness, a petal falling
d,b=bg([(0,'#0a1a3a'),(1,'#000')])
for k in range(10): b+=f'<rect x="{100+k*50}" y="{260+k*50}" width="{600-k*100 if 600-k*100>40 else 40}" height="50" fill="#{(0x2a-k*3):02x}{(0x3a-k*3):02x}{(0x6a-k*4):02x}"/>'
b+=glow(300,220,170,'#c8e0ff',.4)+'<path d="M300 300 Q290 240 300 180" stroke="#3a6a3a" stroke-width="10" fill="none"/><path d="M296 250 Q250 230 240 250 Q270 270 296 258Z" fill="#4a8a4a"/>'+''.join(f'<ellipse cx="{300+34*math.cos(math.radians(a)):.0f}" cy="{150+30*math.sin(math.radians(a)):.0f}" rx="40" ry="34" fill="#f4f4ff" stroke="#c8d0e8" stroke-width="3"/>' for a in range(0,360,72))+'<circle cx="300" cy="150" r="30" fill="#fff" stroke="#c8d0e8" stroke-width="3"/><path d="M286 150 Q300 130 314 150 Q300 166 286 150" fill="none" stroke="#c8d0e8" stroke-width="3"/>'+'<ellipse cx="380" cy="420" rx="20" ry="11" fill="#fff" transform="rotate(30 380 420)"/>'
I[1001]=svg(b,d)

# 1346 ネーブルオレンジ: a halved navel orange glowing like a sun over a citrus grove, schoolgirls' silhouettes walking home
d,b=bg([(0,'#ffb04a'),(1,'#ffe8b0')])
b+=rays(400,300,24,'#fff',.25,8)+'<circle cx="400" cy="300" r="170" fill="#ff8a1a"/><circle cx="400" cy="300" r="150" fill="#ffc04a"/>'+''.join(f'<path d="M400 300 L{400+140*math.cos(math.radians(a)):.0f} {300+140*math.sin(math.radians(a)):.0f}" stroke="#fff4d0" stroke-width="5"/>' for a in range(0,360,36))+'<circle cx="400" cy="300" r="22" fill="#fff4d0"/>'
b+='<path d="M-10 620 Q400 560 810 620 L810 810 L-10 810Z" fill="#4a8a3a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#3a7a2a"/><circle cx="{x-10}" cy="{y}" r="8" fill="#ff9a1a"/>' for x,y,r in [(80,600,50),(720,600,50),(200,620,40),(620,620,40)])
b+=figure(340,740,130,'#2a1a14',hair='#2a1a14')+figure(440,740,124,'#2a1a14',hair='#2a1a14')
I[1346]=svg(b,d)

# 1405 スパークル: a comet streaking across a starry sky, its sparkling tail reflected in a lake below a lone figure
d,b=bg([(0,'#04082a'),(1,'#1a2a6a')])
b+=starsf(90,1405,460,'#fff')+'<path d="M140 120 Q400 200 620 300" stroke="url(#ct)" stroke-width="22" stroke-linecap="round"/>'
d+=lg('ct',S((0,'#5ae8ff',0),(1,'#ffffff',1)),0,0,1,0)
b+=glow(620,300,50,'#fff',.9)+sparkle(620,300,40,'#fff')+'<rect y="480" width="800" height="320" fill="#0a1a4a"/><path d="M-10 480 L230 400 L380 480 L520 420 L810 480Z" fill="#0a102a"/>'
b+='<path d="M620 500 L620 700" stroke="#fff" stroke-width="10" opacity=".3"/>'+''.join(sparkle(600+(k%3)*20,520+k*30,8,'#c8f0ff') for k in range(6))+'<rect y="720" width="800" height="80" fill="#04061a"/>'+figure(260,730,110,'#000')
I[1405]=svg(b,d)

# 1567 Garden: an overgrown greenhouse with sunlight streaming in, a lounge chair surrounded by giant leaves
d,b=bg([(0,'#d0f0c8'),(1,'#8ac87a')])
b+='<path d="M60 800 L60 300 Q400 40 740 300 L740 800" fill="#e8f8e0" opacity=".6" stroke="#5a7a5a" stroke-width="8"/>'+''.join(f'<path d="M{100+k*120} 800 L{100+k*120} {300-(k%3)*40}" stroke="#5a7a5a" stroke-width="4"/>' for k in range(6))
b+='<polygon points="400,60 200,800 600,800" fill="#fffbe0" opacity=".35"/>'
for k,(x,y,a,s) in enumerate([(120,680,-30,1.4),(680,660,30,1.5),(220,520,-50,1),(600,500,40,1.1),(400,720,0,1.2)]): b+=f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><path d="M0 0 Q-60 -80 0 -200 Q60 -80 0 0Z" fill="#2a8a3a"/><path d="M0 0 L0 -190" stroke="#1a6a2a" stroke-width="4"/></g>'
b+='<path d="M300 640 L480 600 L520 660 L340 700Z" fill="#f4e8d0"/><path d="M340 700 L330 760 M520 660 L530 720" stroke="#8a6a4a" stroke-width="8"/>'
I[1567]=svg(b,d)

# 1601 Grandeur: a white marble staircase leading up to a giant golden door under a crystal chandelier
d,b=bg([(0,'#1a1430'),(1,'#3a2a50')])
b+='<rect x="280" y="140" width="240" height="360" rx="120" fill="#d8a838"/><rect x="300" y="160" width="200" height="340" rx="100" fill="#fff4c8"/>'+glow(400,320,200,'#fff4c8',.4)
for k in range(7): b+=f'<rect x="{200-k*30}" y="{500+k*44}" width="{400+k*60}" height="44" fill="{"#f4f0f8" if k%2 else "#e0dce8"}"/>'
b+='<path d="M400 0 L400 60" stroke="#d8a838" stroke-width="4"/>'+''.join(f'<path d="M{400+math.cos(math.radians(a))*80:.0f} 80 l0 30" stroke="#c8e8ff" stroke-width="6"/>' for a in range(0,360,30))+'<ellipse cx="400" cy="80" rx="90" ry="20" fill="#d8a838"/>'+sparkle(400,110,20,'#fff')
I[1601]=svg(b,d)

# 347 energy flow: a single grand piano key sending ripples across still water, soft morning mist
d,b=bg([(0,'#d8e4ee'),(1,'#a8bccc')])
b+='<rect y="400" width="800" height="400" fill="#7a94a8"/>'+''.join(ring(400,560,40+k*60,'#e8f0f8',4,.7-k*.1) for k in range(7))
b+='<g transform="translate(400 560) scale(1 .35)">'+''.join(ring(0,0,40+k*60,'#fff',3,.0) for k in range(1))+'</g>'
b+='<rect x="320" y="440" width="160" height="80" fill="#fbfbfb"/><rect x="380" y="440" width="40" height="54" fill="#141414"/><path d="M320 440 L480 440" stroke="#1a1a1a" stroke-width="4"/>'+glow(400,480,140,'#fff',.25)
b+='<rect y="360" width="800" height="80" fill="#fff" opacity=".35"/>'
I[347]=svg(b,d)

# 610 1990: two sharp silhouettes back to back on a neon-lit Tokyo rooftop, the year blazing on a billboard
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a2a')])
b+=skyline(560,'#140a1e',610,80,320,'#ff5ab8',60)+neon(400,180,'1990','#ff2a6a',140,'DejaVu Sans,sans-serif')
b+='<rect y="640" width="800" height="160" fill="#0a0410"/>'+figure(340,650,260,'#000')+figure(460,650,280,'#000',pose='hold')
I[610]=svg(b,d)

# 620 僕はこの瞳で嘘をつく: a face mask held up beside a single honest eye, half the face in shadow
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a3a')])
b+='<rect x="400" y="0" width="400" height="800" fill="#0a0a14"/>'
b+='<path d="M210 360 Q300 290 390 360 Q300 430 210 360Z" fill="#fff"/><circle cx="300" cy="360" r="36" fill="#3a2a1a"/><circle cx="300" cy="360" r="16" fill="#000"/><circle cx="310" cy="348" r="7" fill="#fff"/>'
b+='<g transform="rotate(10 520 380)"><path d="M420 280 Q520 230 620 280 Q650 380 600 470 Q520 520 440 470 Q390 380 420 280Z" fill="#f4f0e8"/><path d="M450 350 Q490 330 520 350 Q490 370 450 350Z M540 350 Q570 330 600 350 Q570 370 540 350Z" fill="#0a0a14"/><path d="M480 430 Q520 450 560 430" stroke="#c8102a" stroke-width="6" fill="none"/><path d="M520 470 L520 640" stroke="#8a6a4a" stroke-width="8"/></g>'
I[620]=svg(b,d)

# 800 Joy to the love: a Christmas tree of glowing hearts on a snowy rooftop terrace, the city lit up below
d,b=bg([(0,'#1a1a4a'),(1,'#3a2a5a')])
b+=snow(70,800)+skyline(700,'#1a1430',800,40,160,'#ffd27a',40)
for k in range(5):
    for j in range(k+1): b+=heart(400-k*40+j*80,200+k*90,30,['#e8102a','#ff5a8a','#ffd02a','#5ae8a8'][(k+j)%4])
b+=star5(400,130,40,'#ffd02a')+'<rect x="380" y="620" width="40" height="60" fill="#5a3a1a"/>'
I[800]=svg(b,d)

# 1135 Happy: a birthday cake with one candle on an empty table, the flame dancing as if blowing out a wish
d,b=bg([(0,'#2a1a3a'),(1,'#4a2a4a')])
b+=glow(400,280,200,'#ffc870',.35)+'<rect y="560" width="800" height="240" fill="#6a3a2a"/>'
b+='<rect x="260" y="420" width="280" height="180" rx="14" fill="#fff4e8"/><path d="M260 470 Q300 500 340 470 Q380 500 420 470 Q460 500 500 470 Q520 490 540 470" stroke="#ff8ab0" stroke-width="14" fill="none"/><ellipse cx="400" cy="420" rx="140" ry="24" fill="#fff"/>'+''.join(f'<circle cx="{300+k*40}" cy="418" r="7" fill="{["#e8102a","#3ac85a","#2a8ae8"][k%3]}"/>' for k in range(6))
b+='<rect x="392" y="320" width="16" height="96" fill="#5ab8ff"/><path d="M400 260 Q380 300 400 320 Q420 300 400 260Z" fill="#ffd02a"/><path d="M400 280 Q392 300 400 312 Q408 300 400 280Z" fill="#fff"/>'
I[1135]=svg(b,d)

# 1230 ナイスな心意気: a red-and-white headband tied around a pair of drumsticks crossed over a festival taiko drum
d,b=bg([(0,'#ffd02a'),(1,'#ff8a1a')])
b+=rays(400,420,24,'#fff',.25,8)+''.join(chochin(x,120,34) for x in (120,680))
b+='<ellipse cx="400" cy="460" rx="220" ry="200" fill="#8a3a1a"/><ellipse cx="400" cy="460" rx="180" ry="166" fill="#f4e4c0"/>'+''.join(f'<circle cx="{400+200*math.cos(math.radians(a)):.0f}" cy="{460+186*math.sin(math.radians(a)):.0f}" r="7" fill="#2a1a0a"/>' for a in range(0,360,20))
b+='<path d="M220 200 L520 520 M580 200 L280 520" stroke="#e8c88a" stroke-width="22" stroke-linecap="round"/><rect x="330" y="300" width="140" height="40" rx="8" fill="#fff"/><circle cx="400" cy="320" r="16" fill="#e8102a"/><path d="M470 320 L530 290 L520 340Z" fill="#fff"/>'
I[1230]=svg(b,d)

# 1430 O.R.I.O.N.: the Orion constellation glowing above a winter road, a figure reaching for its belt stars
d,b=bg([(0,'#04061e'),(1,'#1a2a5a')])
b+=starsf(70,1430,600,'#c8d8ff')
O=[(300,130),(500,150),(370,300),(410,290),(450,280),(320,460),(520,440)]
b+=f'<path d="M{O[0][0]} {O[0][1]} L{O[2][0]} {O[2][1]} L{O[5][0]} {O[5][1]} M{O[1][0]} {O[1][1]} L{O[4][0]} {O[4][1]} L{O[6][0]} {O[6][1]} M{O[2][0]} {O[2][1]} L{O[4][0]} {O[4][1]}" stroke="#8ab0ff" stroke-width="2" opacity=".6"/>'
for x,y in O: b+=glow(x,y,20,'#fff',.8)+sparkle(x,y,14,'#fff')
b+='<path d="M300 800 L380 600 L420 600 L500 800Z" fill="#e8eef8"/><rect y="600" width="800" height="12" fill="#c8d0e0"/>'+figure(400,720,180,'#000',pose='reach')
I[1430]=svg(b,d)

# 1667 残酷な天使のテーゼ: a pair of white wings breaking through a dark window as a red sunset floods the room
d,b=bg([(0,'#c80a1a'),(1,'#3a0a14')])
b+='<rect x="140" y="120" width="520" height="460" fill="#ff5a2a"/>'+hinomaru_sun(400,400,120,'#ffd08a',.8)+'<path d="M140 120 L660 120 L660 580 L140 580Z M400 120 L400 580 M140 350 L660 350" stroke="#1a0408" stroke-width="18" fill="none"/>'
for sx in (-1,1): b+=f'<g transform="translate(400 380) scale({sx} 1)">'+''.join(f'<path d="M10 0 Q{120+k*30} {-160+k*40} {260-k*20} {-120+k*60} Q{140+k*20} {-60+k*30} 10 {20+k*10}Z" fill="#fff" opacity="{.95-k*.12:.2f}"/>' for k in range(4))+'</g>'
b+='<rect y="640" width="800" height="160" fill="#1a0408"/>'
I[1667]=svg(b,d)

# 324 Plastic Love: a retro city-pop night: a mirrorball over a neon dance floor, a cocktail glass with a pink heart
d,b=bg([(0,'#2a0a4a'),(1,'#ff5ab8')])
b+=skyline(640,'#1a0a2a',324,80,260,'#5ae8ff',60)+'<circle cx="400" cy="200" r="100" fill="#c8c8e0"/>'+''.join(f'<rect x="{310+(k%9)*20}" y="{110+(k//9)*20}" width="17" height="17" fill="#fff" opacity="{.3+(k*7%5)*.15:.2f}"/>' for k in range(81) if (310+(k%9)*20+8-400)**2+(110+(k//9)*20+8-200)**2<95**2)
b+=rays(400,200,20,'#fff',.15,4)+'<path d="M300 520 L500 520 L400 620Z" fill="#ffb0e0" opacity=".85"/><path d="M400 620 L400 720 M340 730 L460 730" stroke="#fff" stroke-width="8"/>'+heart(400,560,24,'#ff2a8a')+'<path d="M440 540 L520 440" stroke="#5ae8ff" stroke-width="6"/>'
I[324]=svg(b,d)

# 452 恋におちて: a woman's silhouette holding a wall phone receiver by a rainy window on a Friday night
d,b=bg([(0,'#2a2a4a'),(1,'#4a3a5a')])
b+='<rect x="420" y="80" width="320" height="440" fill="#5a6a9a"/>'+rain(60,452,'#c8d8ff',.4,5)+'<rect x="420" y="80" width="320" height="440" fill="none" stroke="#1a1a2a" stroke-width="16"/>'+skyline(520,'#2a2a4a',452,40,160,'#ffd27a',20)
b+='<rect x="100" y="240" width="80" height="140" rx="10" fill="#e8e0d0"/><path d="M140 380 Q140 520 260 540" stroke="#1a1a1a" stroke-width="4" fill="none"/>'+figure(300,780,520,'#0a0a14',hair='#0a0a14')+'<rect x="230" y="370" width="30" height="80" rx="12" fill="#e8e0d0"/>'
I[452]=svg(b,d)

# 547 嵐の素顔: a calm face-shaped mask cracking open to reveal a swirling storm inside, lightning in the gaps
d,b=bg([(0,'#1a2a3a'),(1,'#0a1018')])
b+='<ellipse cx="400" cy="400" rx="200" ry="260" fill="#3a4a6a"/>'+''.join(f'<path d="M400 400 Q{400+k*30} {300-k*20} {460+k*20} {400}" stroke="#8ab0d8" stroke-width="6" fill="none" opacity=".6" transform="rotate({k*60} 400 400)"/>' for k in range(6))
b+='<path d="M200 400 Q200 140 400 140 L380 260 L420 330 L360 420 L410 520 L380 660 Q200 640 200 400Z" fill="#f4ece4"/><path d="M260 330 Q290 310 320 330" stroke="#3a2a2a" stroke-width="8" fill="none"/><path d="M290 520 Q320 530 350 520" stroke="#c84050" stroke-width="8" fill="none"/>'
b+=bolt([(500,240),(470,330),(510,350),(470,450)],'#fff6c8',6,1)
I[547]=svg(b,d)

# 1231 Lotus: a pink lotus blooming on a dark pond, five beams of light rising from its centre
d,b=bg([(0,'#0a1a2a'),(1,'#0a2a2a')])
for k,c in enumerate(['#3a8ae8','#e8302a','#3ac85a','#ffd02a','#a85aff']): b+=f'<polygon points="400,460 {300+k*50},0 {330+k*50},0" fill="{c}" opacity=".35"/>'
b+='<rect y="480" width="800" height="320" fill="#0a2a2a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="90" ry="24" fill="#2a6a3a"/>' for x,y in [(160,600),(640,640),(280,720)])
for a in range(-60,61,30): b+=f'<path d="M400 500 Q{400+a*1.5:.0f} 420 {400+a*2.6:.0f} {380+abs(a)} Q{400+a*1.1:.0f} 460 400 500Z" fill="#ff8ab8"/>'
b+='<ellipse cx="400" cy="500" rx="100" ry="24" fill="#2a6a3a"/>'+glow(400,440,80,'#fff',.5)
I[1231]=svg(b,d)

# 1347 歩道橋: a pedestrian overpass at sunset, a girl leaning on its rail as traffic lights streak below
d,b=bg([(0,'#5a4a8a'),(.5,'#ff8a6a'),(1,'#ffc890')])
b+=skyline(440,'#5a3a5a',1347,40,180,'#ffd27a',30)+'<rect y="560" width="800" height="240" fill="#2a2a34"/>'
for k in range(6): b+=f'<path d="M-10 {640+k*24} L810 {620+k*24}" stroke="{"#ff3a2a" if k%2 else "#fff4c8"}" stroke-width="4" opacity=".7"/>'
b+='<rect x="-10" y="440" width="820" height="40" fill="#3a5a8a"/><rect x="-10" y="400" width="820" height="10" fill="#4a6a9a"/>'+''.join(f'<rect x="{k*60}" y="400" width="6" height="44" fill="#4a6a9a"/>' for k in range(14))+'<rect x="80" y="480" width="40" height="320" fill="#3a5a8a"/><rect x="680" y="480" width="40" height="320" fill="#3a5a8a"/>'
b+=figure(420,440,160,'#1a1020',hair='#1a1020')
I[1347]=svg(b,d)

# 1367 アンビバレント: a figure split down the middle, one half in a sunny beach, the other in a grey city, a frown and a smile
d,b=bg([(0,'#3ab0f8'),(1,'#f4dca0')])
b+='<rect x="400" y="0" width="400" height="800" fill="#6a6a7a"/>'+skyline(560,'#4a4a5a',1367,60,260,'#a8a8b8',30).replace('<','<g clip-path="url(#rh)"><',1)[:0]
b+=f'<g clip-path="url(#rh)">{skyline(560,"#4a4a5a",1367,60,260,"#a8a8b8",30)}</g>'+hinomaru_sun(180,160,60,'#fff6c8',.9)+'<rect y="440" width="400" height="120" fill="#1a8ad8"/><rect y="560" width="400" height="240" fill="#f4dca0"/><rect x="400" y="560" width="400" height="240" fill="#4a4a54"/>'
d+='<clipPath id="rh"><rect x="400" y="0" width="400" height="800"/></clipPath>'
b+='<circle cx="400" cy="380" r="140" fill="#ffd02a"/><path d="M400 240 A140 140 0 0 1 400 520Z" fill="#a8a8b8"/><circle cx="350" cy="350" r="14" fill="#1a1a1a"/><circle cx="450" cy="350" r="14" fill="#1a1a1a"/><path d="M330 420 Q365 460 400 430" stroke="#1a1a1a" stroke-width="8" fill="none"/><path d="M400 430 Q435 400 470 440" stroke="#1a1a1a" stroke-width="8" fill="none"/>'
I[1367]=svg(b,d)

# 1431 Summer Madness: a pool party seen from above, a flamingo float and splashes under a blazing sun
d,b=bg([(0,'#2ad8f8'),(1,'#1ab0e8')])
b+=''.join(f'<path d="M{k*90-40} 0 Q{k*90} 400 {k*90-40} 800" stroke="#bff4ff" stroke-width="5" fill="none" opacity=".5"/>' for k in range(11))
b+='<rect x="0" y="0" width="800" height="60" fill="#f4f0e8"/><rect x="0" y="740" width="800" height="60" fill="#f4f0e8"/>'
b+='<circle cx="360" cy="440" r="130" fill="#ff7ab0"/><circle cx="360" cy="440" r="60" fill="#2ad8f8"/><path d="M440 340 Q520 200 480 160 Q440 140 430 190" stroke="#ff7ab0" stroke-width="40" fill="none" stroke-linecap="round"/><path d="M430 180 L400 200 L430 210Z" fill="#1a1a1a"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x,y,r in [(600,300,20),(630,330,12),(580,340,10),(160,620,18),(190,650,10)])+'<rect x="560" y="560" width="100" height="70" rx="10" fill="#ffd02a" transform="rotate(20 610 595)"/>'
I[1431]=svg(b,d)

# 1539 かくれんぼ: a child's hand covering eyes against a tree trunk at dusk, counting, leaves drifting
d,b=bg([(0,'#ffb07a'),(1,'#8a5a8a')])
b+='<rect x="300" y="0" width="200" height="800" fill="#5a3a2a"/><path d="M320 0 L330 800 M440 0 L450 800" stroke="#4a2a1a" stroke-width="6"/>'
b+='<path d="M0 0 Q200 120 300 60 L300 0Z M800 0 Q600 140 500 80 L500 0Z" fill="#3a6a2a"/><rect y="700" width="800" height="100" fill="#3a2a2a"/>'
b+='<g fill="#e8c0a0"><rect x="200" y="380" width="120" height="70" rx="30"/><rect x="290" y="360" width="30" height="100" rx="14"/></g><path d="M230 400 L310 400 M230 420 L310 420" stroke="#c8987a" stroke-width="4"/>'
b+='<text x="640" y="280" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="64" fill="#fff" opacity=".9">1, 2,</text><text x="640" y="360" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="64" fill="#fff" opacity=".9">3…</text>'+petals(14,1539,'#ffb03a',100,700,10,16,.9)
I[1539]=svg(b,d)

# 1800 君に届け: a paper airplane carrying a heart flying from one school window to another across a sunny courtyard
d,b=bg([(0,'#8ad8ff'),(1,'#e0f6ff')])
for x in (-20,560): b+=f'<rect x="{x}" y="100" width="260" height="700" fill="#f4ece0"/>'+''.join(f'<rect x="{x+40}" y="{160+k*150}" width="180" height="100" fill="#8ab8d8"/>' for k in range(4))
b+='<path d="M200 380 Q400 200 600 330" stroke="#fff" stroke-width="5" fill="none" stroke-dasharray="10 10"/><g transform="translate(420 260) rotate(10)"><path d="M-60 0 L60 -30 L0 30Z" fill="#fff"/><path d="M-60 0 L60 -30 L-10 10Z" fill="#e0e8f0"/></g>'+heart(430,240,18,'#ff3a6a')+''.join(sakura(x,y,18,'#ffc0d4','#fff',x%70,1) for x,y in [(320,560),(460,620),(380,700)])
I[1800]=svg(b,d)

# 310 RUN: a lone runner on an endless highway into a burning sunset, heat shimmer on the road
d,b=bg([(0,'#3a1a4a'),(.5,'#e84a2a'),(1,'#ffb04a')])
b+=hinomaru_sun(400,440,140,'#ffd890',.8)+'<rect y="460" width="800" height="340" fill="#2a1a1a"/><path d="M360 460 L440 460 L760 800 L40 800Z" fill="#4a3a3a"/>'+''.join(f'<rect x="{396-k*6}" y="{480+k*k*6}" width="{8+k*12}" height="{10+k*6}" fill="#ffd02a"/>' for k in range(1,8))
b+=figure(400,700,240,'#000',pose='wave')
I[310]=svg(b,d)

# 315 恋人よ: a lone white chair under a bare tree on a windswept autumn hill, leaves swirling past
d,b=bg([(0,'#8a7a8a'),(1,'#d8c8b8')])
b+='<path d="M-10 640 Q400 520 810 620 L810 810 L-10 810Z" fill="#7a6a4a"/><path d="M560 600 L560 300 M560 400 L640 300 M560 360 L480 260 M640 300 L680 240 M480 260 L440 230" stroke="#2a1a14" stroke-width="16" stroke-linecap="round" fill="none"/>'
b+='<rect x="260" y="520" width="10" height="100" fill="#f4f4f4"/><rect x="330" y="560" width="10" height="70" fill="#f4f4f4"/><rect x="256" y="550" width="90" height="14" fill="#f4f4f4"/><rect x="260" y="460" width="10" height="90" fill="#f4f4f4"/>'
b+=petals(30,315,'#c8601a',60,620,10,18,.9)
I[315]=svg(b,d)

# 584 風に吹かれて: a schoolgirl's skirt and long scarf billowing on a windy hilltop, a dandelion clock blowing apart
d,b=bg([(0,'#5ab0f8'),(1,'#c8ecff')])
b+=cloud(600,160,1.2)+cloud(200,240,.8)+'<path d="M-10 600 Q400 520 810 580 L810 810 L-10 810Z" fill="#6ac85a"/>'
b+=figure(300,600,300,'#1a2a4a',hair='#1a2a4a')+'<path d="M310 360 Q420 340 520 380 Q440 380 400 400Z" fill="#e8302a"/>'
b+='<path d="M560 600 L560 460" stroke="#4a8a3a" stroke-width="6"/>'+''.join(f'<path d="M560 450 L{560+40*math.cos(math.radians(a)):.0f} {450+40*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="2"/>' for a in range(0,360,25))+''.join(f'<path d="M{620+k*30} {420-k*16} l10 -10" stroke="#fff" stroke-width="2"/><circle cx="{630+k*30}" cy="{410-k*16}" r="5" fill="#fff"/>' for k in range(5))
I[584]=svg(b,d)

# 740 himawari: one sunflower turned toward a faint sun in a stormy sky, standing in a field of drooping ones
d,b=bg([(0,'#4a5a6a'),(1,'#a8a8a0')])
b+=glow(620,140,120,'#fff6c8',.5)+'<rect y="560" width="800" height="240" fill="#5a6a3a"/>'
for x in (100,220,560,700): b+=f'<path d="M{x} 800 Q{x} 640 {x+30} 600" stroke="#4a6a2a" stroke-width="8" fill="none"/><circle cx="{x+40}" cy="610" r="30" fill="#8a7a2a"/>'
b+='<path d="M400 800 L400 360" stroke="#4a8a2a" stroke-width="14"/><path d="M400 560 Q460 520 500 540 Q460 580 400 570Z" fill="#5aa83a"/>'+''.join(f'<ellipse cx="{400+110*math.cos(math.radians(a)):.0f}" cy="{300+110*math.sin(math.radians(a)):.0f}" rx="50" ry="18" fill="#ffd02a" transform="rotate({a} {400+110*math.cos(math.radians(a)):.0f} {300+110*math.sin(math.radians(a)):.0f})"/>' for a in range(0,360,24))+'<circle cx="400" cy="300" r="70" fill="#5a3a1a"/>'
I[740]=svg(b,d)

# 888 渚にまつわるエトセトラ: a beach spread from above: crab, shells, sunglasses, a melon slice and a beach ball
d,b=bg([(0,'#f4dca0'),(1,'#e8c890')])
b+='<path d="M-10 -10 L810 -10 L810 180 Q400 260 -10 160Z" fill="#2ab0e8"/><path d="M-10 160 Q400 260 810 180" stroke="#fff" stroke-width="10" fill="none"/>'
b+='<g transform="translate(220 420)"><ellipse rx="70" ry="50" fill="#e8402a"/><circle cx="-24" cy="-50" r="10" fill="#1a1a1a"/><circle cx="24" cy="-50" r="10" fill="#1a1a1a"/><path d="M-70 -10 Q-120 -60 -90 -90 M70 -10 Q120 -60 90 -90" stroke="#e8402a" stroke-width="14" fill="none"/></g>'
b+='<circle cx="560" cy="380" r="80" fill="#fff"/><path d="M480 380 A80 80 0 0 1 560 300 L560 380Z" fill="#e8102a"/><path d="M560 460 A80 80 0 0 1 480 380 L560 380Z" fill="#2a8ae8"/><path d="M640 380 A80 80 0 0 1 560 460 L560 380Z" fill="#ffd02a"/>'
b+='<path d="M300 640 A110 110 0 0 0 520 640Z" fill="#3ac85a"/><path d="M314 640 A96 96 0 0 0 506 640Z" fill="#ff5a5a"/>'+''.join(f'<ellipse cx="{360+k*30}" cy="{660+(k%2)*10}" rx="4" ry="7" fill="#1a1a1a"/>' for k in range(4))
b+='<g transform="translate(640 620) rotate(-20)"><circle cx="-40" cy="0" r="34" fill="#1a1a2a"/><circle cx="40" cy="0" r="34" fill="#1a1a2a"/><path d="M-6 0 L6 0" stroke="#1a1a2a" stroke-width="8"/></g>'+''.join(f'<path d="M{x-20} {y} Q{x} {y-30} {x+20} {y}Z" fill="#fff0e0" stroke="#e8b8a0" stroke-width="3"/>' for x,y in [(110,640),(680,240),(420,520)])
I[888]=svg(b,d)

# 1002 NEVER EVER: a cracked hourglass whose sand flows upward into a pale star, black-and-white with one red accent
d,b=bg([(0,'#2a2a2a'),(1,'#0a0a0a')])
b+='<path d="M280 140 L520 140 L420 400 L520 660 L280 660 L380 400Z" fill="#e8e8f0" opacity=".25" stroke="#e8e8f0" stroke-width="8"/><rect x="250" y="120" width="300" height="24" fill="#e8e8f0"/><rect x="250" y="656" width="300" height="24" fill="#e8e8f0"/>'
b+='<path d="M300 650 L500 650 L420 560 L380 560Z" fill="#c8c8c8"/><path d="M400 560 L400 200" stroke="#c8c8c8" stroke-width="5" stroke-dasharray="6 8"/>'+star5(400,240,40,'#fff')+'<path d="M440 280 L470 330 L450 360 L480 420" stroke="#e8102a" stroke-width="6" fill="none"/>'
I[1002]=svg(b,d)

# 1348 逃げ水: a mirage shimmering on a hot summer road, a girl's reflection wavering in the fake water
d,b=bg([(0,'#3ab0f8'),(1,'#e0f4ff')])
b+=cloud(600,180,1.6)+'<rect y="440" width="800" height="360" fill="#8a8a8a"/><path d="M360 440 L440 440 L780 800 L20 800Z" fill="#5a5a64"/><path d="M400 460 L400 800" stroke="#fff" stroke-width="8" stroke-dasharray="40 30"/>'
b+='<rect y="460" width="800" height="70" fill="#8ad0ff" opacity=".55"/>'+figure(400,460,160,'#1a1a2a',hair='#1a1a2a')+'<g transform="translate(0 920) scale(1 -1)" opacity=".35">'+figure(400,460,160,'#1a1a2a',hair='#1a1a2a')+'</g>'
I[1348]=svg(b,d)

# 1368 黒い羊: one black sheep standing in a crowd of white sheep, staring straight ahead under a grey sky
d,b=bg([(0,'#8a8a94'),(1,'#5a5a64')])
b+='<rect y="480" width="800" height="320" fill="#5a6a4a"/>'
def sheep(x,y,s,col,face):
    return f'<g transform="translate({x} {y}) scale({s})"><ellipse rx="70" ry="50" fill="{col}"/>'+''.join(f'<circle cx="{c}" cy="{-30+(c%3)*6}" r="26" fill="{col}"/>' for c in (-40,0,40))+f'<ellipse cx="74" cy="-10" rx="26" ry="32" fill="{face}"/><path d="M-40 40 L-40 80 M40 40 L40 80" stroke="{face}" stroke-width="10"/></g>'
r=R(1368)
for k in range(12): b+=sheep(r.uniform(60,740),r.uniform(500,760),r.uniform(.6,.9),'#f4f4f4','#2a2a2a')
b+=glow(400,600,120,'#fff',.15)+sheep(400,620,1.3,'#141414','#000')+'<circle cx="490" cy="600" r="6" fill="#fff"/>'
I[1368]=svg(b,d)

# 1554 レディメイド: a shop-window mannequin silhouette tagged with a price label, a single real tear falling from it
d,b=bg([(0,'#2a2a3a'),(1,'#1a1a24')])
b+='<rect x="140" y="80" width="520" height="620" fill="#3a3a54"/>'+glow(400,200,240,'#c8d8ff',.3)
b+='<g fill="#d8d4cc"><ellipse cx="400" cy="230" rx="60" ry="74"/><rect x="380" y="300" width="40" height="40"/><path d="M300 340 L500 340 Q520 460 470 520 L330 520 Q280 460 300 340Z"/><rect x="392" y="520" width="16" height="140"/></g><rect x="340" y="660" width="120" height="16" fill="#8a8a94"/>'
b+='<path d="M480 360 L560 420" stroke="#fff" stroke-width="3"/><path d="M550 400 L620 400 L640 430 L620 460 L550 460Z" fill="#fff"/><text x="590" y="440" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="22" fill="#e8102a">¥</text>'
b+='<path d="M380 250 Q372 270 380 280 Q388 270 380 250Z" fill="#8ad0ff"/>'
I[1554]=svg(b,d)

# 1627 Gifted.: a golden gift box bursting open with beams of light, seven silhouettes in a line before it
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+=rays(400,320,28,'#ffd27a',.25,8)+glow(400,320,200,'#ffd27a',.5)+'<rect x="300" y="300" width="200" height="160" fill="#d8a838"/><rect x="390" y="300" width="20" height="160" fill="#fff4c8"/><path d="M290 280 L510 220 L520 260 L300 320Z" fill="#e8b848"/>'
b+='<rect y="640" width="800" height="160" fill="#06060e"/>'+''.join(figure(130+k*90,650,150+(k%2)*10,'#000') for k in range(7))
I[1627]=svg(b,d)

# 1777 明日があるさ: a commuter's tie and briefcase tossed in the air on a station platform at sunrise, a train arriving
d,b=bg([(0,'#ffb07a'),(1,'#ffe8c0')])
b+=hinomaru_sun(160,360,90,'#fff6d0',.9)+'<rect y="480" width="800" height="320" fill="#8a8a94"/><rect y="560" width="800" height="20" fill="#ffd02a"/>'
b+='<rect x="460" y="300" width="400" height="260" rx="40" fill="#3ac85a"/><rect x="500" y="340" width="100" height="80" fill="#c8ecff"/><rect x="640" y="340" width="100" height="80" fill="#c8ecff"/><rect x="460" y="470" width="400" height="20" fill="#f4f4f4"/>'
b+=figure(300,720,220,'#1a1a2a',pose='up')+'<g transform="rotate(-20 240 220)"><rect x="200" y="180" width="90" height="64" rx="8" fill="#5a3a1a"/><rect x="230" y="166" width="30" height="16" fill="none" stroke="#5a3a1a" stroke-width="6"/></g><path d="M380 180 L400 260 L390 300 L370 260Z" fill="#e8102a"/>'
I[1777]=svg(b,d)

# 54 人形の家: a pale doll sitting alone inside an open dollhouse, a cold blue light through its tiny window
d,b=bg([(0,'#3a2a3a'),(1,'#1a1420')])
b+='<path d="M160 300 L400 120 L640 300Z" fill="#8a3a4a"/><rect x="180" y="300" width="440" height="420" fill="#f4e8e0"/><rect x="200" y="320" width="400" height="380" fill="#e8d8d0"/><rect x="200" y="500" width="400" height="10" fill="#c8b8b0"/>'
b+='<rect x="460" y="350" width="90" height="90" fill="#8ab8e8"/><path d="M505 350 L505 440 M460 395 L550 395" stroke="#f4e8e0" stroke-width="6"/><polygon points="460,440 550,440 520,500 400,500" fill="#c8e0ff" opacity=".35"/>'
b+='<circle cx="320" cy="580" r="30" fill="#f8e8e0"/><path d="M290 570 Q320 530 350 570" fill="#5a3a2a"/><path d="M280 700 Q290 610 320 610 Q350 610 360 700Z" fill="#ffb0c8"/><circle cx="310" cy="582" r="4" fill="#1a1a1a"/><circle cx="330" cy="582" r="4" fill="#1a1a1a"/>'
I[54]=svg(b,d)

# 703 こんなにそばに居るのに: two coffee-shop seats back to back separated by a thin glass wall, two hands pressed on each side
d,b=bg([(0,'#c8d8e8'),(1,'#e8eef4')])
b+='<rect x="390" y="60" width="20" height="740" fill="#bfe8ff" opacity=".7"/><rect x="396" y="60" width="4" height="740" fill="#fff"/>'
b+='<g fill="#e8c0a0"><rect x="300" y="300" width="80" height="110" rx="30"/><rect x="420" y="320" width="80" height="110" rx="30"/></g>'+''.join(f'<rect x="{x}" y="{y}" width="16" height="60" rx="8" fill="#e8c0a0"/>' for x,y in [(306,250),(326,240),(346,244),(364,256),(424,270),(444,260),(464,256),(484,264)])
b+=figure(180,800,400,'#3a3a5a')+figure(620,800,380,'#5a3a4a',hair='#5a3a4a')
I[703]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
