import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 10. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 1210 Beautiful days: a breakfast table by an open window, sunlight on a vase of daisies and two cups of coffee
d,b=bg([(0,'#fff4d8'),(1,'#ffe0b0')])
b+='<rect x="440" y="80" width="300" height="320" fill="#bfe8ff"/>'+cloud(590,200,.9)+'<path d="M440 80 L740 80 L740 400 L440 400Z M590 80 L590 400 M440 240 L740 240" stroke="#fff" stroke-width="14" fill="none"/>'
b+='<polygon points="440,400 740,400 560,800 120,800" fill="#fff8e0" opacity=".5"/><rect y="560" width="800" height="240" fill="#e8c890"/>'
b+='<path d="M300 400 L360 400 L350 560 L310 560Z" fill="#bfe0f0" opacity=".85"/>'+''.join(flower(x,y,40,10,'#fff','#ffd02a',0,.7)+f'<path d="M{x} {y+16} L330 400" stroke="#4a8a3a" stroke-width="4"/>' for x,y in [(290,300),(360,320),(330,260)])
for x in (480,620): b+=f'<path d="M{x-40} 560 L{x+40} 560 L{x+34} 620 L{x-34} 620Z" fill="#fff"/><path d="M{x+40} 574 Q{x+66} 580 {x+38} 606" stroke="#fff" stroke-width="10" fill="none"/><ellipse cx="{x}" cy="630" rx="60" ry="10" fill="#f4f4f4"/>'
I[1210]=svg(b,d)

# 1338 インフルエンサー: a single spotlight hitting a dancer whose shadow multiplies into dozens of shadows on the wall behind
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a4a')])
for k in range(-4,5): b+=figure(400+k*80,640,280-abs(k)*20,'#5a1a7a',pose='up') if k else ''
b+=f'<polygon points="400,-20 280,700 520,700" fill="#ffe8ff" opacity=".18"/>'+figure(400,700,300,'#0a0410',pose='up')
b+='<rect y="700" width="800" height="100" fill="#140820"/><ellipse cx="400" cy="710" rx="120" ry="16" fill="#ffd8ff" opacity=".3"/>'
I[1338]=svg(b,d)

# 1546 逆光: a lone figure standing defiantly against a blinding sunburst, long shadow stretching toward the viewer
d,b=bg([(0,'#ff6a1a'),(.5,'#ffd06a'),(1,'#5a2a1a')])
b+=rays(400,330,26,'#fff',.4,5)+glow(400,330,200,'#fff8d8',1)+'<circle cx="400" cy="330" r="100" fill="#fffbe8"/>'
b+='<rect y="560" width="800" height="240" fill="#3a1a0a"/><path d="M370 600 L430 600 L560 800 L240 800Z" fill="#000" opacity=".5"/>'+figure(400,600,330,'#0a0404',hair='#0a0404')
I[1546]=svg(b,d)

# 1807 君がくれた夏: a pair of sparklers drawing a heart in the warm summer night by the sea
d,b=bg([(0,'#0a1438'),(1,'#1a2a5a')])
b+=starsf(40,1807,400,'#fff')+'<rect y="560" width="800" height="240" fill="#0a1a3a"/><path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#3a3a4a"/>'
b+='<path d="M400 480 C260 380 270 220 360 220 C390 220 400 250 400 270 C400 250 410 220 440 220 C530 220 540 380 400 480Z" fill="none" stroke="#ffd27a" stroke-width="8" stroke-linecap="round" stroke-dasharray="2 12"/>'+glow(400,350,170,'#ffb04a',.3)
for x,a in [(330,-20),(470,20)]: b+=f'<path d="M{x} 640 L{x+(-30 if a<0 else 30)} 500" stroke="#5a5a64" stroke-width="5"/>'+sparkle(x+(-30 if a<0 else 30),495,36,'#fff4c8')
I[1807]=svg(b,d)

# 121 サウスポー: a baseball pitcher's left hand wind-up silhouette on a mound under stadium lights, ball flying from the left
d,b=bg([(0,'#0a1a3a'),(1,'#1a3a5a')])
for x in (120,680): b+=f'<rect x="{x-60}" y="80" width="120" height="60" fill="#fff6d8"/>'+glow(x,110,120,'#fff6d8',.4)+f'<rect x="{x-6}" y="140" width="12" height="300" fill="#2a2a3a"/>'
b+='<rect y="480" width="800" height="320" fill="#3a8a3a"/><ellipse cx="400" cy="640" rx="200" ry="50" fill="#c8905a"/>'
b+='<g fill="#f4f4f4"><circle cx="420" cy="420" r="24"/><path d="M400 450 L440 450 L460 560 L380 560Z"/><path d="M390 560 L340 640 M450 560 L500 620" stroke="#f4f4f4" stroke-width="22" stroke-linecap="round"/><path d="M400 460 Q330 420 290 360" stroke="#f4f4f4" stroke-width="18" fill="none" stroke-linecap="round"/><path d="M440 460 Q490 480 520 520" stroke="#f4f4f4" stroke-width="18" fill="none" stroke-linecap="round"/></g><path d="M400 400 L440 400 L440 410 L396 410Z" fill="#e8102a"/>'
b+='<circle cx="270" cy="340" r="18" fill="#fff"/><path d="M262 328 Q270 340 262 352 M278 328 Q270 340 278 352" stroke="#e8102a" stroke-width="3" fill="none"/>'
I[121]=svg(b,d)

# 644 LADY NAVIGATION: an old compass rose map with a woman's red high heel resting on it as a pointer
d,b=bg([(0,'#e8d8b0'),(1,'#c8b088')])
b+='<circle cx="400" cy="400" r="280" fill="none" stroke="#8a6a3a" stroke-width="4"/>'
for k in range(8): a=math.radians(k*45);L=260 if k%2==0 else 160;b+=f'<path d="M400 400 L{400+L*math.cos(a):.0f} {400+L*math.sin(a):.0f} L{400+30*math.cos(a+.6):.0f} {400+30*math.sin(a+.6):.0f}Z" fill="{["#5a3a1a","#c8a060"][k%2]}"/>'
b+='<path d="M200 520 Q260 520 320 470 Q370 430 420 470 L560 560 L560 600 L330 600 Q270 600 240 640 L220 640 L220 600Z" fill="#e8102a"/><path d="M220 600 L210 700 L226 700 L240 620" fill="#a80a1a"/>'
I[644]=svg(b,d)

# 1211 PIKA★★NCHI DOUBLE: two shining stars doing a high five over a rooftop, a city of lights below
d,b=bg([(0,'#1a1a5a'),(1,'#5a3a8a')])
b+=skyline(640,'#120a2a',1211,80,260,'#ffd27a',80)
b+=glow(310,300,110,'#ffe05a',.4)+star5(310,300,110,'#ffe05a')+glow(490,300,110,'#ff9ad8',.4)+star5(490,300,110,'#ffb0e0')
b+=sparkle(400,220,40,'#fff')
I[1211]=svg(b,d)

# 1339 シンクロニシティ: two strangers' hands reaching from opposite sides of a crowded crossing, their red threads touching
d,b=bg([(0,'#ff9a7a'),(1,'#ffd8b0')])
b+=skyline(480,'#c86a6a',1339,80,300,'#ffe8c0',60)+'<rect y="480" width="800" height="320" fill="#4a4a5a"/>'+''.join(f'<rect x="{k*90}" y="500" width="50" height="300" fill="#f4f4f4" transform="skewX(-20)"/>' for k in range(12))
for x,h in [(80,220),(160,240),(240,200),(560,230),(640,210),(720,250)]: b+=figure(x,760,h,'#1a1a2a')
b+=figure(300,760,280,'#2a2a3a',pose='reach')+figure(500,760,270,'#2a2a3a',pose='reachL',hair='#2a2a3a')+'<path d="M330 570 Q400 660 470 570" stroke="#e8102a" stroke-width="7" fill="none"/>'
I[1339]=svg(b,d)

# 1505 白日: a figure walking alone through a vast white blizzard, footprints trailing back into whiteness
d,b=bg([(0,'#e8ecf4'),(1,'#ffffff')])
b+=snow(150,1505)+'<rect y="560" width="800" height="240" fill="#f4f6fa"/>'
for k in range(8): b+=f'<ellipse cx="{200+k*24+(k%2)*18}" cy="{780-k*24}" rx="{10-k*.8:.0f}" ry="{5-k*.4:.0f}" fill="#c8d0e0"/>'
b+=figure(420,580,200,'#3a4050',hair='#3a4050')
I[1505]=svg(b,d)

# 1527 ハルジオン: a cluster of fleabane daisies swaying by a railway line at dusk, a train's lights passing
d,b=bg([(0,'#3a3a7a'),(.6,'#e88a8a'),(1,'#ffc8a0')])
b+='<rect y="440" width="800" height="40" fill="#2a2a3a"/><rect x="100" y="380" width="600" height="60" rx="10" fill="#1a1a2a"/>'+''.join(f'<rect x="{120+k*70}" y="392" width="50" height="30" fill="#ffd27a"/>' for k in range(8))
b+='<rect y="480" width="800" height="320" fill="#3a5a3a"/>'
r=R(1527)
for _ in range(16):
    x=r.uniform(60,740);y=r.uniform(520,760);b+=f'<path d="M{x:.0f} {y+80:.0f} L{x:.0f} {y:.0f}" stroke="#2a4a2a" stroke-width="3"/>'+flower(x,y,r.uniform(22,36),14,'#fff0f4','#ffd02a',0,.7)
I[1527]=svg(b,d)

# 1597 ブラザービート: drumsticks crossing over a big drum pounding out a beat, sound waves bursting
d,b=bg([(0,'#1a3a8a'),(1,'#0a1a4a')])
b+=rays(400,420,20,'#5ae8ff',.18,8)
for k in range(3): b+=ring(400,500,220+k*60,'#5ae8ff',6,.5-k*.15)
b+='<ellipse cx="400" cy="460" rx="200" ry="60" fill="#f4f4f4"/><path d="M200 460 L200 620 Q400 690 600 620 L600 460 Q400 520 200 460Z" fill="#e8102a"/>'+''.join(f'<path d="M{220+k*60} {480+((k%2)*20)} L{250+k*60} {640-((k%2)*20)}" stroke="#d8b040" stroke-width="6"/>' for k in range(6))
b+='<path d="M200 200 L420 440 M600 200 L380 440" stroke="#e8c890" stroke-width="18" stroke-linecap="round"/><circle cx="420" cy="440" r="14" fill="#e8c890"/><circle cx="380" cy="440" r="14" fill="#e8c890"/>'
I[1597]=svg(b,d)

# 385 禁区: a strip of yellow caution tape stretched across a dark doorway, a red rose pushed through the gap
d,b=bg([(0,'#1a1a1a'),(1,'#2a2a2a')])
b+='<rect x="240" y="120" width="320" height="600" fill="#0a0a0a"/><rect x="220" y="100" width="360" height="20" fill="#3a3a3a"/>'
for y,a in [(360,-12),(470,10)]: b+=f'<g transform="rotate({a} 400 {y})"><rect x="60" y="{y-30}" width="680" height="60" fill="#ffd02a"/>'+''.join(f'<path d="M{80+k*80} {y-30} L{120+k*80} {y+30}" stroke="#1a1a1a" stroke-width="26"/>' for k in range(8))+'</g>'
b+='<path d="M380 600 Q400 500 420 420" stroke="#2a5a2a" stroke-width="8" fill="none"/>'+rose(420,410,.9)
I[385]=svg(b,d)

# 386 TANGO NOIR: two black silhouettes locked in a tango dip on a red-and-black checkerboard floor
d,b=bg([(0,'#3a040a'),(1,'#0a0204')])
b+='<polygon points="400,-20 160,600 640,600" fill="#ff3a3a" opacity=".12"/>'
for i in range(10):
    for j in range(4): b+=f'<path d="M{i*80-(j*40)} {600+j*50} L{i*80+80-(j*40)} {600+j*50} L{i*80+80-(j+1)*40} {650+j*50} L{i*80-(j+1)*40} {650+j*50}Z" fill="{["#1a0a0a","#a80a1a"][(i+j)%2]}"/>'
b+='<g fill="#000"><circle cx="330" cy="240" r="30"/><path d="M310 270 L360 270 L380 420 L360 600 L340 600 L340 440 L310 600 L290 600 L310 420Z"/><circle cx="470" cy="360" r="26"/><path d="M360 300 Q420 320 460 380 Q500 440 560 470 Q600 560 540 600 L520 600 Q540 540 500 500 Q440 460 400 420Z"/><path d="M360 290 L460 360" stroke="#000" stroke-width="16"/></g>'
b+=rose(460,330,.4)
I[386]=svg(b,d)

# 736 終わりなき旅: a long winding road disappearing over endless hills toward a distant dawn, a backpack resting by the roadside
d,b=bg([(0,'#3a5aa8'),(.6,'#ffb08a'),(1,'#ffe0b0')])
b+=hinomaru_sun(400,360,60,'#fff4d0',.8)
for k,c in enumerate(['#7a8aa8','#5a7a7a','#4a6a4a','#3a5a3a']): b+=f'<path d="M-10 {400+k*70} Q{200+k*60} {360+k*70} {400} {400+k*70} T810 {380+k*70} L810 810 L-10 810Z" fill="{c}"/>'
b+='<path d="M380 400 Q420 440 360 500 Q260 600 420 680 Q560 740 500 810 L300 810 Q380 740 260 680 Q160 600 300 500 Q370 440 380 400Z" fill="#c8b890"/>'
b+='<path d="M600 700 Q600 620 650 620 Q700 620 700 700 L700 760 L600 760Z" fill="#c84a2a"/><rect x="620" y="680" width="60" height="40" rx="6" fill="#a83a1a"/>'
I[736]=svg(b,d)

# 1212 愛を叫べ: a megaphone blasting a stream of hearts across a sunny wedding garden
d,b=bg([(0,'#ffd8e8'),(1,'#fff4f8')])
b+='<rect y="620" width="800" height="180" fill="#8ad06a"/>'+''.join(f'<path d="M{x} 620 L{x} 520 Q{x+60} 480 {x+120} 520 L{x+120} 620" stroke="#fff" stroke-width="10" fill="none"/>' for x in (560,))
b+='<g transform="rotate(-20 220 460)"><path d="M140 420 L320 340 L320 580 L140 500Z" fill="#e8302a"/><rect x="100" y="420" width="50" height="80" rx="8" fill="#3a3a44"/><path d="M180 500 L200 560 L230 556 L214 492" fill="#3a3a44"/></g>'
for k,(x,y,s) in enumerate([(400,360,40),(500,300,54),(620,250,70),(520,420,34),(680,400,46)]): b+=heart(x,y,s,['#ff2a5a','#ff5a8a','#e8102a','#ff8ab8','#ff4a7a'][k])
I[1212]=svg(b,d)

# 1575 Soranji: a candle flame cupped in two hands, its glow lighting a sky full of tiny drifting embers
d,b=bg([(0,'#0a0a1a'),(1,'#1a1424')])
b+=glow(400,380,260,'#ffc870',.4)
r=R(1575)
for _ in range(30): b+=f'<circle cx="{r.uniform(80,720):.0f}" cy="{r.uniform(60,500):.0f}" r="{r.uniform(2,5):.0f}" fill="#ffd27a" opacity="{r.uniform(.4,.9):.2f}"/>'
b+='<rect x="370" y="420" width="60" height="120" rx="6" fill="#fff6e8"/><path d="M400 330 Q430 380 400 420 Q370 380 400 330Z" fill="#ffd060"/><path d="M400 370 Q412 395 400 414 Q388 395 400 370Z" fill="#fff8d8"/>'
b+='<path d="M220 600 Q220 460 330 440 L360 540 Q330 560 340 640Z M580 600 Q580 460 470 440 L440 540 Q470 560 460 640Z" fill="#e8b890"/><path d="M220 600 Q300 720 400 720 Q500 720 580 600 L460 640 Q400 660 340 640Z" fill="#d8a880"/>'
I[1575]=svg(b,d)

# 1842 いのちの食べ方: a knife and fork laid out beside an empty plate holding only a beating heart-shaped apple
d,b=bg([(0,'#2a2a34'),(1,'#141418')])
b+='<polygon points="400,-20 200,800 600,800" fill="#fff" opacity=".05"/><ellipse cx="400" cy="480" rx="220" ry="90" fill="#f4f4f4"/><ellipse cx="400" cy="476" rx="170" ry="66" fill="#e0e0e8"/>'
b+=heart(400,440,90,'#c80a1a')+'<path d="M400 360 Q404 330 420 316" stroke="#3a2a1a" stroke-width="8" fill="none"/>'
b+='<path d="M120 380 L120 600 M100 380 L100 440 Q100 460 120 460 Q140 460 140 440 L140 380" stroke="#c8c8d8" stroke-width="10" fill="none"/><path d="M680 380 Q700 420 690 470 L680 600" stroke="#c8c8d8" stroke-width="14" fill="none"/>'
for x,y in [(300,300),(510,560)]: b+=f'<path d="M{x} {y} q10 -20 0 -40 q-10 -20 0 -40" stroke="#ff2a3a" stroke-width="5" fill="none" opacity=".5"/>'
I[1842]=svg(b,d)

# 387 難破船: a broken sailing ship half-sunk in a stormy sea, a single lantern still burning on its mast
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
b+=rain(60,387,'#8a8aa8',.35,6)+bolt([(620,60),(580,180),(620,200),(560,320)],'#e8f0ff',6,1)
b+='<g transform="rotate(-24 380 520)"><path d="M200 520 L560 520 L500 620 L260 620Z" fill="#3a2414"/><rect x="370" y="240" width="14" height="290" fill="#3a2414"/><path d="M384 260 L500 420 L384 420Z" fill="#c8c0b0" opacity=".7"/><path d="M384 300 L440 330 L420 360 L460 400" stroke="#1a1a1a" stroke-width="4" fill="none"/></g>'
b+=glow(310,260,50,'#ffc860',.7)+'<rect x="298" y="244" width="24" height="32" rx="4" fill="#ffd27a"/>'
b+='<path d="M-10 560 Q100 520 200 560 T400 560 T600 540 T810 560 L810 810 L-10 810Z" fill="#1a3a5a"/><path d="M-10 560 Q100 520 200 560 T400 560 T600 540 T810 560" stroke="#c8d8f0" stroke-width="6" fill="none"/>'
I[387]=svg(b,d)

# 589 惡の華: a black flower with blood-red stamen blooming out of a cracked mirror in a gothic chamber
d,b=bg([(0,'#1a0a14'),(1,'#0a0408')])
b+='<path d="M220 120 Q400 40 580 120 L580 680 L220 680Z" fill="#5a4a5a"/><path d="M240 140 Q400 70 560 140 L560 660 L240 660Z" fill="#2a2a3a"/>'
b+=bolt([(300,180),(380,320),(340,360),(420,520)],'#8a8aa8',4,1)+bolt([(520,200),(460,330)],'#8a8aa8',4,1)
b+=glow(400,400,160,'#c80a2a',.3)
for k in range(8): a=math.radians(k*45);b+=f'<path d="M400 400 Q{400+90*math.cos(a-.3):.0f} {400+90*math.sin(a-.3):.0f} {400+140*math.cos(a):.0f} {400+140*math.sin(a):.0f} Q{400+90*math.cos(a+.3):.0f} {400+90*math.sin(a+.3):.0f} 400 400Z" fill="#0a0a0a" stroke="#3a1a2a" stroke-width="3"/>'
b+='<circle cx="400" cy="400" r="34" fill="#c80a1a"/>'
I[589]=svg(b,d)

# 645 太陽のKomachi Angel: a winged sun with a halo blazing over a sparkling summer sea
d,b=bg([(0,'#ff8a1a'),(.6,'#ffd04a'),(1,'#1a90d8')])
b+='<rect y="560" width="800" height="240" fill="#1a90d8"/>'+''.join(f'<rect x="{200+(k*97)%400}" y="{580+k*24}" width="{40+k*10}" height="5" fill="#fff" opacity=".7"/>' for k in range(8))
for f in (1,-1): b+=''.join(f'<path d="M{400+f*90} 320 Q{400+f*(200+k*30)} {200+k*40} {400+f*(320-k*10)} {240+k*60} Q{400+f*(220+k*20)} {300+k*40} {400+f*90} {360}Z" fill="#fff" stroke="#ffd8a0" stroke-width="3"/>' for k in range(3))
b+=glow(400,330,140,'#fff6c8',.8)+'<circle cx="400" cy="330" r="100" fill="#ffe05a"/><ellipse cx="400" cy="200" rx="90" ry="20" fill="none" stroke="#fff8c8" stroke-width="12"/>'
I[645]=svg(b,d)

# 772 スターゲイザー: a small figure on a hilltop gazing up through a telescope at a sky swirling with stars
d,b=bg([(0,'#04061e'),(1,'#1a1a4a')])
for k in range(8): b+=f'<circle cx="560" cy="160" r="{60+k*55}" fill="none" stroke="#a8c8ff" stroke-width="3" stroke-dasharray="{10+k*8} {20+k*6}" opacity=".45"/>'
b+=starsf(60,772,800,'#e8f0ff')+sparkle(560,160,34,'#fff')
b+='<path d="M-10 800 L-10 620 Q300 540 600 620 L810 680 L810 800Z" fill="#06081a"/>'
b+='<path d="M300 600 L340 560 L350 600 Z M320 580 L420 470" stroke="#06081a" stroke-width="14" fill="#06081a"/><rect x="400" y="440" width="90" height="34" rx="10" fill="#06081a" transform="rotate(-40 445 457)"/>'+figure(260,610,140,'#06081a')
I[772]=svg(b,d)

# 859 瞳の住人: a giant eye whose iris holds a tiny house with a lit window, a person waving from inside
d,b=bg([(0,'#d8e0f0'),(1,'#a8b8d8')])
b+='<path d="M60 400 Q400 80 740 400 Q400 720 60 400Z" fill="#fff" stroke="#2a2a3a" stroke-width="12"/>'
b+='<circle cx="400" cy="400" r="190" fill="#3a7ac8"/><circle cx="400" cy="400" r="120" fill="#0a1a3a"/>'
b+='<path d="M340 460 L340 390 L400 340 L460 390 L460 460Z" fill="#f4e8d8"/><rect x="380" y="400" width="40" height="40" fill="#ffd27a"/>'+glow(400,420,50,'#ffd27a',.4)+'<ellipse cx="320" cy="320" rx="30" ry="20" fill="#fff" opacity=".7"/>'
I[859]=svg(b,d)

# 1101 チャンピオーネ: a football bursting through a goal net with confetti and fireworks exploding around it
d,b=bg([(0,'#0a5a2a'),(1,'#0a3a1a')])
b+=firework(160,160,100,'#ffe05a',20,1)+firework(640,160,100,'#ff5a5a',20,2)
for k in range(12): b+=f'<path d="M{80+k*60} 300 L{80+k*60} 720 M80 {300+k*36} L740 {300+k*36}" stroke="#fff" stroke-width="3" opacity=".5"/>'
b+='<circle cx="400" cy="480" r="110" fill="#fff"/>'+''.join(f'<polygon points="{400+40*math.cos(math.radians(a+k*72)):.0f},{480+40*math.sin(math.radians(a+k*72)):.0f}" fill="none"/>' for a in [0] for k in range(5))+'<polygon points="400,440 438,468 424,512 376,512 362,468" fill="#1a1a1a"/>'+''.join(f'<path d="M{400+40*math.cos(math.radians(-90+k*72)):.0f} {480+40*math.sin(math.radians(-90+k*72)):.0f} L{400+110*math.cos(math.radians(-90+k*72)):.0f} {480+110*math.sin(math.radians(-90+k*72)):.0f}" stroke="#1a1a1a" stroke-width="6"/>' for k in range(5))
r=R(1101)
for _ in range(30): x,y=r.uniform(40,760),r.uniform(240,780);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="12" height="20" fill="{r.choice(["#ffe05a","#ff5a5a","#5ab8ff","#fff"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[1101]=svg(b,d)

# 1172 手紙 ～拝啓 十五の君へ～: a letter addressed in neat handwriting sealed with a cherry-blossom sticker, resting on a school desk
d,b=bg([(0,'#e8f0d8'),(1,'#c8d8b0')])
b+='<rect x="460" y="60" width="300" height="200" fill="#3a5a3a"/><rect x="450" y="50" width="320" height="220" fill="none" stroke="#8a6a3a" stroke-width="12"/>'
b+='<rect y="440" width="800" height="360" fill="#c8a070"/><g transform="rotate(-6 400 560)"><rect x="200" y="440" width="400" height="250" fill="#fbf8f0"/><path d="M200 440 L400 580 L600 440" stroke="#d8d0c0" stroke-width="5" fill="none"/>'+sakura(400,580,40,'#ffb0c8','#ffe8f0',0,1)+'<path d="M240 640 L340 640 M240 660 L320 660" stroke="#5a5a7a" stroke-width="5"/></g>'
b+='<rect x="140" y="660" width="200" height="20" fill="#ffd02a" transform="rotate(20 240 670)"/>'
I[1172]=svg(b,d)

# 1624 Boom Boom Back: a giant subwoofer pulsing with shockwaves, the floor cracking and lights flashing
d,b=bg([(0,'#0a0a14'),(1,'#1a1424')])
for k in range(5): b+=ring(400,420,230+k*50,'#ff3a8a',8,.5-k*.09)
b+='<rect x="190" y="160" width="420" height="520" rx="30" fill="#1a1a24" stroke="#3a3a4a" stroke-width="10"/>'
b+='<circle cx="400" cy="300" r="70" fill="#2a2a34"/><circle cx="400" cy="300" r="30" fill="#0a0a10"/><circle cx="400" cy="520" r="130" fill="#2a2a34"/><circle cx="400" cy="520" r="100" fill="#141418"/><circle cx="400" cy="520" r="40" fill="#3a3a44"/>'
b+=bolt([(120,800),(160,720),(140,700),(180,640)],'#ff3a8a',6,1)+bolt([(680,800),(640,720),(660,700),(620,640)],'#ff3a8a',6,1)
I[1624]=svg(b,d)

# 1799 GO! GO! MANIAC: a pastel tea set and a bass guitar sharing a school club-room table, a cake slice waiting
d,b=bg([(0,'#ffe8f0'),(1,'#ffd8e8')])
b+='<rect y="520" width="800" height="280" fill="#c89a6a"/>'+guitar(600,420,.9,20,'#3a6ae8')
b+='<path d="M140 440 L300 440 L290 540 L150 540Z" fill="#fff"/><path d="M300 460 Q340 470 320 510 L296 520" stroke="#fff" stroke-width="12" fill="none"/><path d="M140 440 Q220 400 300 440" fill="#f4f4f4"/><circle cx="220" cy="420" r="12" fill="#ffb0c8"/><path d="M150 490 L290 490" stroke="#ffb0c8" stroke-width="8"/>'
b+='<path d="M320 560 L460 560 L440 520 Z" fill="#fff8f0"/><path d="M320 560 L460 560 L460 600 L320 600Z" fill="#fff4e0"/><path d="M320 572 L460 572" stroke="#ff8ab0" stroke-width="8"/><circle cx="430" cy="520" r="14" fill="#e8102a"/>'
b+=note(200,240,30,'#ff5a9a',True)+note(330,180,26,'#ff5a9a')
I[1799]=svg(b,d)

# 285 愛と欲望の日々: a red cocktail and a pearl necklace on a mirrored bar top reflecting the glitter of a decadent night
d,b=bg([(0,'#2a0a14'),(1,'#5a1a2a')])
b+=starsf(30,285,400,'#ffd8a0')+'<rect y="560" width="800" height="240" fill="#1a0a10"/>'
b+='<path d="M280 260 L480 260 L380 420Z" fill="#e8102a" opacity=".9"/><rect x="374" y="420" width="12" height="140" fill="#f4e8f0"/><ellipse cx="380" cy="560" rx="60" ry="12" fill="#f4e8f0"/><circle cx="440" cy="270" r="16" fill="#e8102a" stroke="#3a6a2a" stroke-width="4"/>'
b+=''.join(f'<circle cx="{520+100*math.cos(math.radians(a)):.0f}" cy="{620+30*math.sin(math.radians(a)):.0f}" r="10" fill="#fff8f0"/>' for a in range(0,360,18))
b+='<path d="M280 640 L480 640 L380 760Z" fill="#e8102a" opacity=".2"/>'
I[285]=svg(b,d)

# 646 ミエナイチカラ: a glowing invisible shield deflecting a storm of arrows around a small figure
d,b=bg([(0,'#1a1a3a'),(1,'#3a3a5a')])
b+=glow(400,480,240,'#5ae8ff',.3)+'<path d="M180 640 A220 220 0 0 1 620 640" fill="#5ae8ff" opacity=".15" stroke="#bff8ff" stroke-width="6"/>'
for x,y,a in [(160,240,40),(300,160,70),(500,160,110),(640,240,140),(120,380,20),(680,380,160)]: b+=f'<g transform="rotate({a} {x} {y})"><path d="M{x-60} {y} L{x+40} {y}" stroke="#c8c8d8" stroke-width="6"/><path d="M{x+40} {y-12} L{x+64} {y} L{x+40} {y+12}Z" fill="#c8c8d8"/></g>'
b+='<rect y="640" width="800" height="160" fill="#141428"/>'+figure(400,640,180,'#0a0a14')
I[646]=svg(b,d)

# 824 奇跡の地球: the Earth seen from space, cradled by two enormous hands of light
d,b=bg([(0,'#02040e'),(1,'#0a1430')])
b+=starsf(80,824,800,'#e8f0ff')+glow(400,380,240,'#5ab0ff',.35)
b+='<circle cx="400" cy="380" r="170" fill="#1a5ad8"/><path d="M290 300 Q340 260 400 300 Q380 360 320 360Z M420 420 Q480 380 540 440 Q500 520 440 500Z M300 420 Q330 440 320 480 Q280 470 280 440Z" fill="#3ac87a"/><ellipse cx="340" cy="300" rx="80" ry="40" fill="#fff" opacity=".3"/>'
b+='<path d="M170 520 Q200 640 400 650 Q600 640 630 520" stroke="#ffd27a" stroke-width="22" fill="none" stroke-linecap="round" opacity=".85"/>'+''.join(f'<path d="M{x} 520 L{x+dx} 440" stroke="#ffd27a" stroke-width="18" stroke-linecap="round" opacity=".85"/>' for x,dx in [(170,-10),(190,10),(630,10),(610,-10)])+glow(400,600,200,'#ffd27a',.25)
I[824]=svg(b,d)

# 901 My Graduation: a mortarboard cap tossed high into a cherry-blossom sky, a rolled diploma with a ribbon below
d,b=bg([(0,'#bfe0ff'),(1,'#fff0f4')])
b+=petals(40,901,'#ffb0c8',0,800,8,14,.9)+cloud(160,160,1.0)
b+='<g transform="rotate(-14 420 260)"><path d="M280 260 L420 200 L560 260 L420 320Z" fill="#1a1a2a"/><path d="M340 290 L340 340 Q420 370 500 340 L500 290" fill="#1a1a2a"/><path d="M420 260 L520 300 L520 360" stroke="#ffd02a" stroke-width="6" fill="none"/></g>'
b+='<rect y="640" width="800" height="160" fill="#8ad06a"/><g transform="rotate(-10 400 640)"><rect x="240" y="610" width="320" height="60" rx="30" fill="#fbf8f0"/><ellipse cx="560" cy="640" rx="16" ry="30" fill="#e8e0d0"/><rect x="380" y="606" width="30" height="68" fill="#e8102a"/></g>'
I[901]=svg(b,d)

# 1528 もう少しだけ: a hand pressing the snooze button on an alarm clock as morning light spills into the room
d,b=bg([(0,'#ffe0b0'),(1,'#ffc890')])
b+='<polygon points="600,0 800,0 800,800 300,800" fill="#fff8e0" opacity=".5"/><rect y="560" width="800" height="240" fill="#a8806a"/>'
b+='<circle cx="380" cy="420" r="140" fill="#e8302a"/><circle cx="380" cy="420" r="112" fill="#fff"/><path d="M380 420 L380 340 M380 420 L440 440" stroke="#1a1a1a" stroke-width="10" stroke-linecap="round"/>'
b+='<circle cx="280" cy="290" r="40" fill="#e8302a"/><circle cx="480" cy="290" r="40" fill="#e8302a"/><path d="M290 540 L260 580 M470 540 L500 580" stroke="#3a3a3a" stroke-width="12"/>'
b+='<g fill="#e8c0a0"><rect x="320" y="120" width="120" height="160" rx="40"/><rect x="420" y="160" width="160" height="80" rx="40"/></g>'
b+='<text x="600" y="200" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="60" fill="#5a3a2a" opacity=".7">z</text><text x="640" y="140" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="44" fill="#5a3a2a" opacity=".5">z</text>'
I[1528]=svg(b,d)

# 737 innocent world: a paper aeroplane gliding over a green valley toward a clear horizon on a breezy afternoon
d,b=bg([(0,'#3aa8f8'),(1,'#c8ecff')])
b+=cloud(620,160,1.4)+cloud(160,240,.9)+'<path d="M-10 520 Q200 440 400 500 T810 480 L810 810 L-10 810Z" fill="#6ac84a"/><path d="M-10 620 Q300 560 500 620 T810 600 L810 810 L-10 810Z" fill="#4aa83a"/>'
b+='<g transform="rotate(-12 400 340)"><path d="M260 340 L560 300 L380 380Z" fill="#fff"/><path d="M380 380 L560 300 L400 420Z" fill="#e0e8f0"/><path d="M380 380 L400 420 L420 380" fill="#c8d0e0"/></g>'
b+='<path d="M80 420 Q160 390 240 380" stroke="#fff" stroke-width="5" fill="none" stroke-dasharray="10 12"/>'
I[737]=svg(b,d)

# 860 NEO UNIVERSE: a crystal flower blooming in deep space, its petals refracting galaxies
d,b=bg([(0,'#0a0420'),(1,'#1a0a3a')])
b+=starsf(80,860,800,'#e8d8ff')+glow(400,400,240,'#a87aff',.35)
for k in range(10): a=math.radians(k*36);b+=f'<path d="M400 400 L{400+80*math.cos(a-.25):.0f} {400+80*math.sin(a-.25):.0f} L{400+230*math.cos(a):.0f} {400+230*math.sin(a):.0f} L{400+80*math.cos(a+.25):.0f} {400+80*math.sin(a+.25):.0f}Z" fill="{["#bfe8ff","#e8c8ff","#ffd8f0"][k%3]}" opacity=".75" stroke="#fff" stroke-width="2"/>'
b+='<circle cx="400" cy="400" r="40" fill="#fff"/>'+glow(400,400,60,'#fff',.6)
I[860]=svg(b,d)

# 1411 Mighty Long Fall: a figure falling backwards from a cliff edge into an endless sky, arms spread, unafraid
d,b=bg([(0,'#2a4a8a'),(1,'#8ab8e8')])
b+='<path d="M-10 -10 L260 -10 L280 120 L240 300 L-10 300Z" fill="#2a2a3a"/>'+cloud(600,640,2.0)+cloud(200,700,1.6)
b+='<g transform="rotate(150 420 400)">'+figure(420,520,260,'#0a0a1a',pose='up')+'</g>'
for k in range(5): b+=f'<path d="M{400+k*14} {150+k*10} L{400+k*14} {60+k*10}" stroke="#fff" stroke-width="4" opacity=".6"/>'
I[1411]=svg(b,d)

# 1625 Mainstream: a fast river of glowing light cutting through a crowded city, one figure surfing its current
d,b=bg([(0,'#0a0a2a'),(1,'#1a1a4a')])
b+=skyline(560,'#140a30',1625,120,400,'#5ae8ff',80)
b+='<path d="M-10 800 Q300 600 400 560 Q600 480 810 420 L810 520 Q600 580 420 640 Q260 700 160 810Z" fill="#5ae8ff" opacity=".7"/><path d="M60 800 Q300 640 420 600 Q600 530 810 470" stroke="#fff" stroke-width="6" fill="none"/>'
b+='<rect x="380" y="568" width="100" height="16" rx="8" fill="#ffd02a" transform="rotate(-18 430 576)"/>'+figure(430,568,140,'#000',pose='up')
I[1625]=svg(b,d)

# 265 季節の中で: a single tree shown across four seasons, its crown split into blossom, green, red and snow
d,b=bg([(0,'#d8e8f4'),(1,'#f4f0e8')])
b+='<rect y="620" width="800" height="180" fill="#8ab86a"/><path d="M380 640 L390 400 L410 400 L420 640Z" fill="#5a3a1a"/>'
for k,(a0,c) in enumerate([(180,'#ffb0c8'),(270,'#5ab84a'),(0,'#e8601a'),(90,'#f4f8ff')]):
    a1=a0+90;b+=f'<path d="M400 340 L{400+230*math.cos(math.radians(a0)):.0f} {340+200*math.sin(math.radians(a0)):.0f} A230 200 0 0 1 {400+230*math.cos(math.radians(a1)):.0f} {340+200*math.sin(math.radians(a1)):.0f}Z" fill="{c}"/>'
b+='<path d="M400 140 L400 540 M170 340 L630 340" stroke="#fff" stroke-width="6" opacity=".7"/>'
I[265]=svg(b,d)

# 894 Face the change: a woman's profile silhouette dissolving into a flock of birds taking flight
d,b=bg([(0,'#ffb08a'),(1,'#ffe0c0')])
b+='<path d="M200 800 L200 600 Q180 520 220 480 Q200 420 240 380 Q230 300 300 260 Q380 230 420 300 Q430 340 410 360 Q420 380 400 390 L410 420 Q400 440 380 440 Q390 480 360 500 L360 560 Q440 600 460 800Z" fill="#3a1a2a"/>'
for k,(x,y,s) in enumerate([(460,300,1),(520,260,.9),(580,220,.8),(500,360,.8),(620,300,.7),(680,240,.6),(560,180,.6),(700,160,.5)]): b+=f'<path d="M{x-30*s:.0f} {y} Q{x-12*s:.0f} {y-20*s:.0f} {x} {y} Q{x+12*s:.0f} {y-20*s:.0f} {x+30*s:.0f} {y}" stroke="#3a1a2a" stroke-width="{8*s:.0f}" fill="none" stroke-linecap="round"/>'
I[894]=svg(b,d)

# 895 For the moment: a polaroid snapshot of a summer sky held up against the actual sky, the moment frozen
d,b=bg([(0,'#3ab0f8'),(1,'#bfe8ff')])
b+=cloud(620,500,1.4)+cloud(160,600,1.0)
b+='<g transform="rotate(-8 400 360)"><rect x="240" y="180" width="320" height="380" fill="#fff"/><rect x="264" y="204" width="272" height="260" fill="#5ac0ff"/>'+cloud(400,330,1.0)+'<circle cx="480" cy="250" r="30" fill="#fff6c8"/></g>'
b+='<g fill="#e8c0a0"><rect x="180" y="440" width="80" height="200" rx="34"/><rect x="540" y="430" width="80" height="200" rx="34"/></g>'
I[895]=svg(b,d)

# 961 WHITE BREATH: a white breath of frost curling into a dragon shape across a frozen winter night
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=snow(70,961)+'<rect y="660" width="800" height="140" fill="#e8f0ff"/>'
b+='<path d="M160 560 Q260 480 340 520 Q420 560 500 460 Q560 380 640 400 Q700 420 680 360 Q640 300 560 330" stroke="#e8f4ff" stroke-width="40" fill="none" stroke-linecap="round" opacity=".85"/><path d="M560 330 L520 300 M570 320 L560 270" stroke="#e8f4ff" stroke-width="10" stroke-linecap="round"/><circle cx="600" cy="350" r="8" fill="#0a1438"/>'
b+='<g fill="#0a0e1e"><circle cx="110" cy="520" r="30"/><path d="M80 560 L140 560 L150 680 L70 680Z"/></g>'
I[961]=svg(b,d)

# 1213 Face Down: a white masquerade mask cracked in half lying on a glossy black floor under a red spotlight
d,b=bg([(0,'#0a0a0e'),(1,'#141418')])
b+='<polygon points="400,-20 160,600 640,600" fill="#ff2a3a" opacity=".14"/><ellipse cx="400" cy="560" rx="280" ry="70" fill="#e8102a" opacity=".3"/>'
b+='<path d="M220 440 Q300 360 400 420 Q500 360 580 440 Q560 540 470 540 Q420 520 400 490 Q380 520 330 540 Q240 540 220 440Z" fill="#f4f4f8"/>'
b+='<ellipse cx="320" cy="460" rx="44" ry="26" fill="#0a0a0e"/><ellipse cx="480" cy="460" rx="44" ry="26" fill="#0a0a0e"/>'+bolt([(400,400),(380,450),(420,480),(400,520)],'#0a0a0e',8,1)
b+='<path d="M580 440 Q640 420 660 380 M220 440 Q160 470 150 520" stroke="#e8102a" stroke-width="6" fill="none"/>'+'<ellipse cx="400" cy="600" rx="200" ry="20" fill="#f4f4f8" opacity=".08"/>'
I[1213]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
