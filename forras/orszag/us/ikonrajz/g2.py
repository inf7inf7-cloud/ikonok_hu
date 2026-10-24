import sys,math;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 2. csoport: a sikerindex szerinti 21-40. dal (2026-10-24)
I={}

# 21 Let's Stay Together (Al Green, 1971): two hands clasped in a warm velvet soul-club glow, a spinning record behind
d,b=bg([(0,'#2a0a1a'),(1,'#a8402a')])
b+=glow(400,330,260,'#ffb070',.45)+vinyl(400,330,230,'#e8a23a')
b+='<g fill="#5a2a18"><path d="M60 640 Q200 560 330 560 L400 590 L390 640 Q300 680 60 720Z"/></g><g fill="#8a4a2a"><path d="M740 640 Q600 560 470 560 L400 590 L410 640 Q500 680 740 720Z"/></g>'
b+='<g fill="#6a3420"><ellipse cx="372" cy="586" rx="44" ry="30"/></g><g fill="#9a5636"><ellipse cx="430" cy="582" rx="44" ry="30"/></g>'
for k in range(4): b+=f'<path d="M{392+k*14} 560 q8 26 0 50" stroke="#5a2a18" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+=heart(400,470,26,'#ff6a5a','opacity=".85"')
I[21]=svg(b,d)

# 22 Bette Davis Eyes (Kim Carnes, 1981): a pair of smoky movie-star eyes with long lashes under platinum curls, 80s violet haze
d,b=bg([(0,'#1a0a2a'),(1,'#6a3a8a')])
b+='<path d="M80 260 Q200 80 400 120 Q600 80 720 260 Q640 200 400 210 Q160 200 80 260Z" fill="#f2ecd6"/>'
for k in range(9): b+=f'<circle cx="{110+k*72}" cy="{200-abs(k-4)*16}" r="46" fill="#fff6e2" opacity=".85"/>'
for cx in (260,540):
    b+=f'<path d="M{cx-130} 400 Q{cx} 290 {cx+130} 400 Q{cx} 500 {cx-130} 400Z" fill="#f6efe8"/>'
    b+=f'<circle cx="{cx}" cy="400" r="56" fill="#3a6aa8"/><circle cx="{cx}" cy="400" r="26" fill="#0a0a12"/><circle cx="{cx-16}" cy="384" r="10" fill="#fff"/>'
    b+=f'<path d="M{cx-140} 380 Q{cx} 250 {cx+140} 380 Q{cx} 300 {cx-140} 380Z" fill="#3a1a4a" opacity=".85"/>'
    b+=f'<path d="M{cx-132} 398 Q{cx} 284 {cx+132} 398" stroke="#0a0a10" stroke-width="10" fill="none"/>'
    for k in range(9): x=cx-110+k*27;b+=f'<path d="M{x} {392-math.sin(k/8*math.pi)*92:.0f} l{(k-4)*5} -34" stroke="#0a0a10" stroke-width="5" stroke-linecap="round"/>'
b+='<path d="M330 640 Q400 600 470 640 Q400 690 330 640Z" fill="#c8243a"/>'
I[22]=svg(b,d)

# 23 Die with a Smile (Lady Gaga & Bruno Mars, 2024): a duet at a grand piano while the sky at the end of the world burns with falling stars
d,b=bg([(0,'#12061e'),(.5,'#6a1a3a'),(1,'#ff8a3a')])
for k,(x,y) in enumerate([(120,90),(300,60),(520,120),(680,70),(420,200)]): b+=f'<path d="M{x} {y} l120 90" stroke="#ffe0b0" stroke-width="5" opacity=".7" stroke-linecap="round"/>'+glow(x+120,y+90,14,'#fff2c8',.9,'glow2')
b+=glow(400,560,280,'#ff9a4a',.5)+hills(600,20,'#1a0610',3,4)
b+='<g fill="#0e0408"><path d="M230 640 L560 640 Q620 640 620 600 L600 560 Q520 520 420 540 L240 560Z"/><rect x="250" y="640" width="12" height="90"/><rect x="540" y="640" width="12" height="90"/><path d="M380 548 L470 470 L480 478 L400 552Z"/></g>'
b+='<rect x="250" y="600" width="230" height="18" fill="#f2efe6"/>'+''.join(f'<rect x="{252+k*16}" y="600" width="9" height="11" fill="#0e0408"/>' for k in range(14))
b+=figure(320,640,170,'#0e0408',pose='hold',hair='#0e0408')+figure(430,640,180,'#0e0408',pose='hold')
I[23]=svg(b,d)

# 24 Fallin' (Alicia Keys, 2001): piano keys tumbling down through a deep blue night, a braided-hair silhouette at the keyboard below
d,b=bg([(0,'#050a1e'),(1,'#1a3a6a')])
b+=starsf(60,24,500,'#cfe0ff')
import random;r=random.Random(24)
for k in range(14):
    x,y,a=r.uniform(60,740),r.uniform(40,460),r.uniform(-50,50);w=r.choice([1,1,0])
    b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{34 if w else 22}" height="{150 if w else 96}" rx="4" fill="{"#f6f6f2" if w else "#0a0a10"}" stroke="#9ab" stroke-width="2" transform="rotate({a:.0f} {x:.0f} {y:.0f})" opacity=".92"/>'
b+='<rect x="0" y="640" width="800" height="160" fill="#06081a"/><rect x="120" y="620" width="560" height="40" fill="#f2f2ee"/>'+''.join(f'<rect x="{134+k*34}" y="620" width="18" height="24" fill="#06081a"/>' for k in range(16) if k%7 not in (2,6))
b+=figure(400,640,230,'#06081a',pose='hold',hair='#06081a')
I[24]=svg(b,d)

# 25 Flowers (Miley Cyrus, 2023): a woman alone holding a big bouquet bought for herself, golden-hour sun, gold dress
d,b=bg([(0,'#f5c26a'),(.6,'#f08a5a'),(1,'#7a3a4a')])
b+=glow(560,260,180,'#fff2c0',.8)+'<circle cx="560" cy="260" r="80" fill="#fff6d8"/>'
b+=hills(620,20,'#5a2a3a',25,4)
b+=figure(360,780,420,'#2a1018',pose='hold',hair='#2a1018')
r=random.Random(25)
for k in range(16):
    x,y=360+r.uniform(-70,70),480+r.uniform(-90,30);c=r.choice(['#ff4a6a','#ffd23a','#ff8ac0','#fff','#ff6a2a'])
    b+=f'<path d="M360 560 L{x:.0f} {y:.0f}" stroke="#2a6a2a" stroke-width="5"/>'
    for p in range(5): a=p*1.2566;b+=f'<circle cx="{x+15*math.cos(a):.0f}" cy="{y+15*math.sin(a):.0f}" r="12" fill="{c}"/>'
    b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#fff2a0"/>'
b+='<path d="M330 548 L390 548 L376 600 L344 600Z" fill="#e8d2a0"/>'
I[25]=svg(b,d)

# 26 Bad Guy (Billie Eilish, 2019): a bob-haired figure in oversized clothes, acid green and black, a big sly grin of light
d,b=bg([(0,'#0a0a0a'),(1,'#1a2a0a')])
b+=glow(400,420,320,'#b6ff2a',.35)
b+='<g fill="#b6ff2a"><path d="M240 800 Q230 560 300 500 Q400 460 500 500 Q570 560 560 800Z"/></g>'
b+='<ellipse cx="400" cy="380" rx="92" ry="110" fill="#0a0a0a"/><path d="M300 400 Q290 250 400 250 Q510 250 500 400 L480 340 Q400 300 320 340Z" fill="#b6ff2a"/>'
b+='<path d="M300 400 Q300 470 330 480 L330 380Z M500 400 Q500 470 470 480 L470 380Z" fill="#b6ff2a"/>'
b+='<path d="M350 430 Q400 470 450 430" stroke="#b6ff2a" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="365" cy="380" r="9" fill="#b6ff2a"/><circle cx="435" cy="380" r="9" fill="#b6ff2a"/>'
b+='<text x="640" y="720" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="64" fill="#0a0a0a" text-anchor="middle">duh</text>'
I[26]=svg(b,d)

# 27 Beat It (Michael Jackson, 1983): a dancer in a red zip jacket mid-move in a wet night alley, lit from one lamp
d,b=bg([(0,'#06060c'),(1,'#20202e')])
b+=spotlight(400,0,260,'#ffe8b0',.22)+glow(400,60,70,'#fff0c0',.8)
b+='<rect x="0" y="0" width="140" height="800" fill="#0c0c14"/><rect x="660" y="0" width="140" height="800" fill="#0c0c14"/>'
for k in range(6): b+=f'<rect x="20" y="{120+k*100}" width="90" height="10" fill="#1a1a26"/><rect x="690" y="{90+k*100}" width="90" height="10" fill="#1a1a26"/>'
b+='<ellipse cx="400" cy="730" rx="220" ry="34" fill="#ffe0a0" opacity=".14"/>'
b+='<g transform="translate(400 730)"><path d="M-40 -330 Q-46 -360 -20 -366 Q6 -370 10 -340 Q14 -310 -14 -306Z" fill="#14080a"/>'
b+='<path d="M-50 -300 Q-10 -312 40 -300 L56 -170 L-40 -170Z" fill="#d8121e"/><path d="M-4 -300 L-2 -172" stroke="#ffcf6a" stroke-width="4"/>'
b+='<path d="M40 -290 Q110 -300 150 -350" stroke="#d8121e" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M-46 -290 Q-100 -250 -130 -210" stroke="#d8121e" stroke-width="30" fill="none" stroke-linecap="round"/>'
b+='<path d="M-40 -172 L52 -172 L70 -6 L40 -6 L8 -120 L-10 -6 L-46 -6Z" fill="#14080a"/><rect x="-54" y="-14" width="40" height="14" rx="5" fill="#111"/><rect x="34" y="-14" width="44" height="14" rx="5" fill="#111"/>'
b+='<rect x="-14" y="-14" width="22" height="8" fill="#fff"/></g>'
I[27]=svg(b,d)

# 28 I Will Always Love You (Whitney Houston, 1992): a lone singer in a single white spotlight on a vast dark stage, one red rose on the boards
d,b=bg([(0,'#04040a'),(1,'#141024')])
b+=spotlight(400,0,300,'#f2f0ff',.3)+'<ellipse cx="400" cy="700" rx="200" ry="34" fill="#fff" opacity=".2"/>'
b+=mic(470,420,70,'#d8d8e0')+figure(380,700,380,'#0a0a14',pose='hold',hair='#0a0a14')
b+='<g transform="translate(560 720) rotate(-10)"><path d="M0 0 L120 -6" stroke="#2a6a2a" stroke-width="5"/><circle cx="0" cy="0" r="16" fill="#d4142a"/><path d="M-10 -6 Q0 -16 10 -6" stroke="#8a0a1a" stroke-width="3" fill="none"/></g>'
I[28]=svg(b,d)

# 29 Gangsta's Paradise (Coolio feat. L.V., 1995): a lone figure walking through a smoky valley at dusk, church-window light and palm silhouettes
d,b=bg([(0,'#1a1408'),(.6,'#7a4a1a'),(1,'#c88a3a')])
b+=glow(400,420,240,'#ffcf7a',.4)
b+='<path d="M300 560 L300 360 Q400 240 500 360 L500 560Z" fill="#2a1a08"/><path d="M330 560 L330 380 Q400 290 470 380 L470 560Z" fill="#ffd27a" opacity=".55"/><path d="M400 300 L400 560 M330 440 L470 440" stroke="#2a1a08" stroke-width="10"/>'
b+=palm(110,640,330,'#140c04',10)+palm(700,640,300,'#140c04',-8)
b+='<rect y="600" width="800" height="200" fill="#120a04"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="200" ry="40" fill="#e8d8c0" opacity=".08"/>' for x,y in ((200,600),(560,620),(400,650)))
b+=figure(400,760,260,'#0a0602',pose='stand')
I[29]=svg(b,d)

# 30 Not Like Us (Kendrick Lamar, 2024): a Compton block party at sunset, a crowd of raised arms below palms and a big red sky
d,b=bg([(0,'#3a0a0a'),(.6,'#d42a1a'),(1,'#ffb03a')])
b+=glow(400,560,240,'#ffe080',.6)+'<circle cx="400" cy="560" r="110" fill="#ffd060"/>'
b+=palm(150,600,360,'#1a0606',8)+palm(260,600,280,'#1a0606',-4)+palm(640,600,340,'#1a0606',-10)
b+='<rect y="600" width="800" height="200" fill="#140404"/>'
r=random.Random(30)
for k in range(22):
    x=r.uniform(10,790);h=r.uniform(120,200)
    b+=f'<circle cx="{x:.0f}" cy="{800-h:.0f}" r="16" fill="#0a0202"/><path d="M{x-10:.0f} {812-h:.0f} L{x+10:.0f} {812-h:.0f} L{x+22:.0f} 800 L{x-22:.0f} 800Z" fill="#0a0202"/>'
    if k%2: b+=f'<path d="M{x+8:.0f} {812-h:.0f} L{x+20+r.uniform(-10,10):.0f} {720-h:.0f}" stroke="#0a0202" stroke-width="9" stroke-linecap="round"/>'
I[30]=svg(b,d)

# 31 Time After Time (Cyndi Lauper, 1984): an old alarm clock and a suitcase on a train platform at night, a flashlight beam through the fog
d,b=bg([(0,'#0a1a2a'),(1,'#3a5a7a')])
b+=glow(620,180,120,'#fff2c8',.5)+spotlight(620,180,160,'#fff2c8',.18)
b+='<rect y="600" width="800" height="200" fill="#121a24"/><path d="M0 650 L800 650" stroke="#e8c84a" stroke-width="6" stroke-dasharray="40 20"/>'
b+='<g transform="translate(350 420)"><circle r="150" fill="#f2e2c0" stroke="#c8902a" stroke-width="18"/><circle cx="-110" cy="-150" r="40" fill="#c8902a"/><circle cx="110" cy="-150" r="40" fill="#c8902a"/>'
for k in range(12): a=math.radians(k*30);b+=f'<line x1="{120*math.cos(a):.0f}" y1="{120*math.sin(a):.0f}" x2="{135*math.cos(a):.0f}" y2="{135*math.sin(a):.0f}" stroke="#3a2a1a" stroke-width="6"/>'
b+='<line x1="0" y1="0" x2="0" y2="-95" stroke="#2a1a0a" stroke-width="10" stroke-linecap="round"/><line x1="0" y1="0" x2="70" y2="30" stroke="#2a1a0a" stroke-width="8" stroke-linecap="round"/><circle r="12" fill="#2a1a0a"/>'
b+='<path d="M-80 140 L-110 190 M80 140 L110 190" stroke="#c8902a" stroke-width="14"/></g>'
b+='<rect x="520" y="560" width="190" height="130" rx="12" fill="#a83a2a"/><path d="M580 560 L580 530 L650 530 L650 560" stroke="#5a1a10" stroke-width="10" fill="none"/><rect x="520" y="610" width="190" height="10" fill="#5a1a10"/>'
I[31]=svg(b,d)

# 32 Wind Beneath My Wings (Bette Midler, 1989): a great white bird soaring high over a sea of sunlit clouds
d,b=bg([(0,'#2a6ab0'),(.7,'#9ad0f0'),(1,'#fff0d0')])
b+=glow(600,200,160,'#fff8e0',.8)
for k in range(7): b+=f'<ellipse cx="{k*130}" cy="{660+(k%2)*30}" rx="170" ry="70" fill="#fff" opacity=".9"/>'
for k in range(6): b+=f'<ellipse cx="{k*160+60}" cy="740" rx="200" ry="80" fill="#f4f0ea"/>'
b+='<g transform="translate(400 380)"><path d="M0 0 Q-120 -140 -330 -110 Q-200 -70 -150 -20 Q-80 10 0 20Z" fill="#fff"/><path d="M0 0 Q120 -140 330 -110 Q200 -70 150 -20 Q80 10 0 20Z" fill="#fff"/>'
b+='<path d="M-330 -110 Q-280 -96 -250 -90 M330 -110 Q280 -96 250 -90" stroke="#3a4a5a" stroke-width="8"/><ellipse cx="0" cy="14" rx="26" ry="60" fill="#fff"/><circle cx="0" cy="-36" r="18" fill="#fff"/><path d="M0 -40 L14 -30 L0 -24Z" fill="#f0a02a"/></g>'
I[32]=svg(b,d)

# 33 I Need a Girl (Part One) (P. Diddy feat. Usher & Loon, 2002): a man in a white suit on a penthouse terrace holding a single rose, night city below
d,b=bg([(0,'#06061a'),(1,'#2a1a4a')])
b+=starsf(40,33,300)+skyline(560,'#140c2a',33,60,240,'#ffd27a',110)
b+='<rect y="640" width="800" height="160" fill="#0a0814"/><rect y="620" width="800" height="12" fill="#c8c0d8"/>'+''.join(f'<rect x="{k*50}" y="560" width="6" height="64" fill="#c8c0d8"/>' for k in range(17))
b+='<rect y="556" width="800" height="8" fill="#c8c0d8"/>'
b+=figure(400,780,420,'#f6f4f0',pose='hold')+'<ellipse cx="400" cy="413" rx="25" ry="30" fill="#2a1a12"/>'
b+='<path d="M400 520 L400 600" stroke="#2a6a2a" stroke-width="5"/><circle cx="400" cy="512" r="16" fill="#d4142a"/>'
I[33]=svg(b,d)

# 34 Leave the Door Open (Silk Sonic, 2021): a 70s lounge door left ajar, warm amber light and rose petals spilling onto the carpet
d,b=bg([(0,'#2a0a12'),(1,'#5a1a1a')])
b+='<rect x="240" y="120" width="320" height="560" fill="#140406"/>'
b+='<path d="M260 140 L540 140 L540 680 L260 680Z" fill="#ffb84a"/>'+glow(400,420,220,'#ffd080',.6)
b+='<path d="M260 140 L430 180 L430 700 L260 680Z" fill="#6a2a14"/><circle cx="410" cy="440" r="10" fill="#e8c06a"/>'
b+='<path d="M0 680 L800 680 L800 800 L0 800Z" fill="#3a0a10"/><path d="M540 680 L800 800 L430 800 L430 700Z" fill="#ffb84a" opacity=".3"/>'
r=random.Random(34)
for k in range(18): x,y=r.uniform(430,760),r.uniform(700,790);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="12" ry="7" fill="#d4142a" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+=note(150,300,40,'#ffd080')+note(660,260,36,'#ffd080',True)
I[34]=svg(b,d)

# 35 Suspicious Minds (Elvis Presley, 1969): the white-jumpsuit King in a high-collar silhouette on a Vegas stage, caught in a web of spotlights
d,b=bg([(0,'#0a0614'),(1,'#2a0a2a')])
for x in (120,400,680): b+=spotlight(x,0,140,'#ffe8c0',.12)
b+='<ellipse cx="400" cy="720" rx="260" ry="40" fill="#ffd8a0" opacity=".2"/>'
b+=figure(400,730,440,'#f6f2ea',pose='up',hair='#14080a')
b+='<path d="M360 380 L400 400 L440 380 L436 352 Q400 370 364 352Z" fill="#f6f2ea"/><path d="M372 440 L428 440 L400 520Z" fill="#e8b830"/>'
for k in range(10): b+=sparkle(330+k*15,450+(k%3)*30,7,'#ffd84a')
b+=mic(220,560,60,'#d0d0d8')
I[35]=svg(b,d)

# 36 Heart of Glass (Blondie, 1979): a crystal-clear glass heart with a hairline crack, reflecting a spinning disco ball
d,b=bg([(0,'#1a0a2a'),(1,'#0a2a4a')])
b+=disco(400,140,90)+rays(400,140,22,'#fff',.08,6)
d+=lg('gl',S((0,'#e8f8ff',.6),(.5,'#9ad8ff',.25),(1,'#ff9ad8',.5)),0,0,1,1)
b+=heart(400,500,170,'url(#gl)','stroke="#f0faff" stroke-width="8"')
b+='<path d="M400 340 L380 400 L420 450 L390 520 L410 600" stroke="#fff" stroke-width="5" fill="none"/>'
for x,y in ((330,430),(460,410),(420,560)): b+=sparkle(x,y,16,'#fff')
I[36]=svg(b,d)

# 37 Firework (Katy Perry, 2010): a girl on a rooftop arms wide while fireworks burst from her chest into the night over the city
d,b=bg([(0,'#04061a'),(1,'#1a1a4a')])
b+=firework(220,200,140,'#ff4ab0',seed=1)+firework(580,160,170,'#4ad8ff',seed=2)+firework(420,320,120,'#ffd84a',seed=3)
b+=skyline(600,'#0a0a1e',37,60,200,'#ffd27a',80)+'<rect y="660" width="800" height="140" fill="#06061a"/>'
b+=glow(400,600,120,'#6a6aff',.45)+figure(400,700,240,'#06061a',pose='up',hair='#06061a')+glow(400,560,40,'#fff2c0',.95,'glow2')
b+=''.join(f'<path d="M400 560 l{30*math.cos(a):.0f} {30*math.sin(a):.0f}" stroke="#ffe080" stroke-width="5"/>' for a in [k*0.785 for k in range(8)])
I[37]=svg(b,d)

# 38 I'll Take You There (The Staple Singers, 1972): a dusty road leading to a golden gospel sunrise, a clapping choir silhouette by the roadside
d,b=bg([(0,'#3a1a4a'),(.55,'#ff8a3a'),(1,'#ffe08a')])
b+=glow(400,470,220,'#fff4c0',.8)+'<circle cx="400" cy="480" r="100" fill="#fff6d0"/>'+rays(400,480,26,'#fff8d8',.15,10)
b+=hills(520,18,'#5a2a2a',38,5)
b+=road(400,520,'#3a2418','#ffd84a',560)
for k,x in enumerate((70,130,190,610,670,730)): b+=figure(x,780,200+k%2*20,'#1a0a0a',pose='up' if k%2 else 'wave')
I[38]=svg(b,d)

# 39 Hotel California (Eagles, 1977): a mission-style hotel at the end of a dark desert highway, a shimmering light in the doorway
d,b=bg([(0,'#04060e'),(.7,'#1a2a4a'),(1,'#5a3a4a')])
b+=starsf(90,39,380)+moon(160,130,38)
b+='<rect y="560" width="800" height="240" fill="#1a1414"/>'+road(400,560,'#141010','#e8c84a',500)
b+='<g fill="#2a1c1a"><path d="M220 560 L220 420 L300 420 L300 380 Q400 300 500 380 L500 420 L580 420 L580 560Z"/></g>'
b+='<rect x="380" y="330" width="40" height="40" fill="#2a1c1a"/><path d="M372 330 L400 300 L428 330Z" fill="#2a1c1a"/>'
for x in (245,275,525,555): b+=f'<rect x="{x}" y="450" width="18" height="30" fill="#ffcf6a" opacity=".8"/>'
b+='<path d="M370 560 L370 470 Q400 440 430 470 L430 560Z" fill="#ffd27a"/>'+glow(400,500,60,'#ffe6a0',.7)
b+=palm(150,570,240,'#06080e',12)+palm(660,570,260,'#06080e',-10)
I[39]=svg(b,d)

# 40 Kiss (Prince & the Revolution, 1986): bold red lips over a purple haze, a cloud-shaped guitar shadow and falsetto sparkles
d,b=bg([(0,'#1a0630'),(1,'#5a1a8a')])
b+=glow(400,420,280,'#c86aff',.4)
b+=eguitar(620,600,120,'#f2f2ff','#3a1a5a',rot=24)
b+='<path d="M180 420 Q260 330 330 360 Q400 330 470 360 Q540 330 620 420 Q520 520 400 520 Q280 520 180 420Z" fill="#e0102a"/>'
b+='<path d="M180 420 Q300 440 400 420 Q500 440 620 420" stroke="#7a0010" stroke-width="10" fill="none"/>'
b+='<path d="M270 370 Q330 360 360 380" stroke="#ff8a9a" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>'
for x,y in ((160,220),(640,200),(250,640)): b+=sparkle(x,y,20,'#ffd8ff')
I[40]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
