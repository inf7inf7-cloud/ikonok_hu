import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 11. csoport, 2026-10-24
I={}
def butterfly(x,y,s,c1,c2,a=0):
    return f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><path d="M0 0 Q-70 -90 -110 -50 Q-120 0 0 0Z M0 0 Q70 -90 110 -50 Q120 0 0 0Z" fill="{c1}"/><path d="M0 0 Q-60 70 -80 40 Q-80 10 0 0Z M0 0 Q60 70 80 40 Q80 10 0 0Z" fill="{c2}"/><rect x="-5" y="-40" width="10" height="80" rx="5" fill="#1a1a1a"/><path d="M0 -40 L-20 -70 M0 -40 L20 -70" stroke="#1a1a1a" stroke-width="3"/></g>'
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'

# 1483 君はロックを聴かない: a pair of earphones shared between two cans of soda on a bedroom floor, one bud dangling unused
d,b=bg([(0,'#f4e0c8'),(1,'#e8c8a8')])
b+='<rect y="480" width="800" height="320" fill="#c89a7a"/><rect x="460" y="80" width="260" height="300" fill="#bfe0f0"/><path d="M460 80 L720 80 L720 380 L460 380Z M590 80 L590 380" stroke="#fff" stroke-width="12" fill="none"/>'
b+='<rect x="140" y="160" width="220" height="220" fill="#1a1a1a"/><circle cx="250" cy="270" r="80" fill="#2a2a2a"/><circle cx="250" cy="270" r="20" fill="#e8302a"/>'+''.join(ring(250,270,30+k*12,'#3a3a3a',2) for k in range(4))
for x,c in [(260,'#e8302a'),(540,'#2a8ae8')]: b+=f'<rect x="{x-36}" y="540" width="72" height="120" rx="12" fill="{c}"/><rect x="{x-36}" y="580" width="72" height="30" fill="#fff" opacity=".8"/><ellipse cx="{x}" cy="542" rx="34" ry="8" fill="#c8c8d0"/>'
b+='<path d="M260 540 Q300 440 400 460 Q500 480 540 540" stroke="#f4f4f4" stroke-width="5" fill="none"/><path d="M400 460 Q420 560 380 640" stroke="#f4f4f4" stroke-width="5" fill="none"/><ellipse cx="380" cy="650" rx="12" ry="16" fill="#f4f4f4"/>'
I[1483]=svg(b,d)

# 1511 ただ君に晴れ: an empty bus stop by a summer field under a sky that has just cleared, a straw hat left on the bench
d,b=bg([(0,'#3aa8f0'),(1,'#d8f0ff')])
b+=cloud(160,140,1.2)+cloud(620,220,1.6)+'<rect y="520" width="800" height="280" fill="#7ac84a"/><rect y="600" width="800" height="60" fill="#9a9aa4"/>'
b+='<rect x="400" y="300" width="12" height="300" fill="#5a5a64"/><circle cx="406" cy="290" r="40" fill="#3a8ae8"/><circle cx="406" cy="290" r="28" fill="#fff"/>'
b+='<rect x="180" y="540" width="200" height="18" fill="#a8703a"/><rect x="190" y="556" width="10" height="44" fill="#5a3a1a"/><rect x="360" y="556" width="10" height="44" fill="#5a3a1a"/>'
b+='<ellipse cx="260" cy="534" rx="60" ry="14" fill="#e8c870"/><path d="M226 534 Q230 500 260 496 Q290 500 294 534Z" fill="#e8c870"/><rect x="226" y="522" width="68" height="8" fill="#3a8ae8"/>'
I[1511]=svg(b,d)

# 1536 レオ: a small dog sitting faithfully in a pet-shop window, a lead hanging on the hook behind it
d,b=bg([(0,'#f4e8d8'),(1,'#e8d0b8')])
b+='<rect x="120" y="120" width="560" height="520" rx="20" fill="#bfe0f0" opacity=".6"/><rect x="120" y="120" width="560" height="520" rx="20" fill="none" stroke="#8a6a4a" stroke-width="16"/>'
b+='<path d="M540 160 L540 200 Q540 300 600 360" stroke="#e8302a" stroke-width="10" fill="none"/><circle cx="540" cy="160" r="12" fill="#5a5a64"/>'
b+='<g fill="#d8a060"><ellipse cx="360" cy="540" rx="110" ry="90"/><circle cx="360" cy="380" r="90"/><ellipse cx="280" cy="350" rx="34" ry="70" transform="rotate(20 280 350)" fill="#a8703a"/><ellipse cx="440" cy="350" rx="34" ry="70" transform="rotate(-20 440 350)" fill="#a8703a"/></g>'
b+='<circle cx="330" cy="370" r="12" fill="#1a1a1a"/><circle cx="390" cy="370" r="12" fill="#1a1a1a"/><ellipse cx="360" cy="410" rx="18" ry="12" fill="#1a1a1a"/><rect x="290" y="450" width="140" height="18" rx="8" fill="#e8302a"/>'
b+='<rect x="120" y="600" width="560" height="40" fill="#8a6a4a"/>'
I[1536]=svg(b,d)

# 647 HOME: a small house with one lit window glowing at the end of a long snowy road
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=starsf(40,647,400,'#fff')+snow(50,647)
b+='<path d="M-10 520 Q400 480 810 520 L810 810 L-10 810Z" fill="#e8eef8"/><path d="M380 520 L420 520 L620 810 L180 810Z" fill="#c8d4e8"/>'
b+='<path d="M310 520 L310 420 L400 360 L490 420 L490 520Z" fill="#7a4a3a"/><path d="M290 424 L400 344 L510 424" stroke="#fff" stroke-width="16" fill="none"/><rect x="380" y="440" width="40" height="40" fill="#ffd27a"/>'+glow(400,460,80,'#ffd27a',.5)+'<rect x="450" y="370" width="20" height="40" fill="#5a3a2a"/>'
I[647]=svg(b,d)

# 779 IT'S ONLY LOVE: a lighthouse beam sweeping across a dark ocean, a heart shape caught in its ray
d,b=bg([(0,'#0a1430'),(1,'#1a2a4a')])
b+=starsf(40,779,400,'#fff')+'<polygon points="200,260 800,120 800,420" fill="#fff6d8" opacity=".18"/>'
b+='<rect y="560" width="800" height="240" fill="#0a1a3a"/><path d="M140 600 L160 260 L240 260 L260 600Z" fill="#f4f4f4"/>'+''.join(f'<rect x="{150+k*2}" y="{320+k*80}" width="{100-k*4}" height="36" fill="#e8302a"/>' for k in range(3))
b+='<rect x="150" y="220" width="100" height="40" fill="#ffe8a0"/><path d="M140 220 L200 170 L260 220Z" fill="#3a3a44"/>'+glow(200,240,60,'#fff6d8',.8)
b+=heart(640,270,60,'#ff5a7a')+'<rect x="80" y="600" width="240" height="40" fill="#2a2a3a"/>'
I[779]=svg(b,d)

# 1042 Swallowtail Butterfly: a swallowtail butterfly fluttering out of a crumbling cityscape of rusted towers
d,b=bg([(0,'#c8a080'),(1,'#5a3a2a')])
b+=skyline(640,'#3a2418',1042,140,420,'#ffb060',40)+'<rect y="640" width="800" height="160" fill="#2a1810"/>'
b+=glow(400,340,140,'#ffe8a0',.4)+butterfly(400,340,1.8,'#ffd02a','#1a1a1a',-10)
b+='<path d="M290 400 L250 470 M510 380 L560 440" stroke="#1a1a1a" stroke-width="10" stroke-linecap="round"/>'
I[1042]=svg(b,d)

# 1214 明日の記憶: a stack of old photographs fading into white at their edges, a forget-me-not lying on top
d,b=bg([(0,'#e8eef4'),(1,'#c8d4e0')])
for k,(x,y,a) in enumerate([(380,440,-12),(420,420,8),(400,400,-2)]): b+=f'<g transform="rotate({a} {x} {y})"><rect x="{x-170}" y="{y-130}" width="340" height="260" fill="#fff"/><rect x="{x-150}" y="{y-110}" width="300" height="190" fill="{["#a8b8c8","#c8b8a8","#8ab0d0"][k]}" opacity="{.5+k*.2}"/></g>'
b+='<path d="M310 440 Q400 360 490 440 L490 470 L310 470Z" fill="#6a9ab8"/><circle cx="460" cy="350" r="24" fill="#fff6d8"/>'
b+=''.join(flower(x,y,26,5,'#5a9aff','#ffe05a',x,.7) for x,y in [(520,560),(560,540),(540,590)])+'<path d="M540 590 L500 660" stroke="#4a8a3a" stroke-width="4"/>'
b+='<rect width="800" height="800" fill="url(#fo)"/>'
d+=rg('fo',S((0,'#ffffff',0),(.7,'#ffffff',0),(1,'#ffffff',.9)),.5,.5,.7)
I[1214]=svg(b,d)

# 1340 サヨナラの意味: a white handkerchief caught in the wind above a quiet station platform at dusk
d,b=bg([(0,'#5a4a8a'),(.6,'#e8907a'),(1,'#ffd0a0')])
b+='<rect y="560" width="800" height="240" fill="#4a4a5a"/><rect y="560" width="800" height="16" fill="#ffd02a"/><rect x="0" y="620" width="800" height="12" fill="#7a7a84"/><rect x="0" y="700" width="800" height="12" fill="#7a7a84"/>'
b+='<rect x="600" y="200" width="16" height="360" fill="#2a2a34"/><rect x="560" y="200" width="180" height="60" fill="#f4f4f4"/>'
b+='<path d="M200 260 Q280 220 340 270 Q400 320 380 380 Q330 340 260 360 Q220 320 200 260Z" fill="#fff"/><path d="M200 260 Q260 300 260 360" stroke="#e0e0e8" stroke-width="3" fill="none"/>'
b+=figure(160,560,160,'#2a1a2a',hair='#2a1a2a')
I[1340]=svg(b,d)

# 1557 napori: a small boat drifting on a still lake at night with a reflection of the Milky Way rippling round it
d,b=bg([(0,'#04061a'),(.5,'#1a1a4a'),(1,'#04061a')])
b+='<path d="M-10 120 Q400 280 810 200" stroke="#d8c8ff" stroke-width="120" fill="none" opacity=".35"/>'+starsf(80,1557,440,'#fff')
b+='<rect y="440" width="800" height="360" fill="#06081e"/><path d="M-10 680 Q400 520 810 600" stroke="#d8c8ff" stroke-width="120" fill="none" opacity=".2"/>'
r=R(1557)
for _ in range(50): b+=f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(450,800):.0f}" r="{r.uniform(1,3):.1f}" fill="#fff" opacity=".6"/>'
b+='<path d="M280 540 L520 540 L480 590 L320 590Z" fill="#e8c890"/><rect x="396" y="420" width="8" height="120" fill="#e8c890"/><path d="M404 430 L470 520 L404 520Z" fill="#fff8e8"/>'+glow(400,500,120,'#fff4d8',.2)+''.join(ring(400,590,80+k*60,'#e8e0ff',3,.6-k*.15) for k in range(3))
I[1557]=svg(b,d)

# 1722 Doki it: a heart pounding so hard it bursts out of a gift box tied with gold ribbon, sparkles flying
d,b=bg([(0,'#ff8ad0'),(1,'#ffd0f0')])
b+=rays(400,360,20,'#fff',.3,8)
b+='<rect x="230" y="480" width="340" height="240" fill="#3a5ae8"/><rect x="210" y="440" width="380" height="60" fill="#5a7aff"/><rect x="385" y="440" width="30" height="280" fill="#ffd02a"/>'
b+=heart(400,320,120,'#ff2a6a')+''.join(f'<path d="M{400+150*math.cos(math.radians(a)):.0f} {320+130*math.sin(math.radians(a)):.0f} L{400+190*math.cos(math.radians(a)):.0f} {320+170*math.sin(math.radians(a)):.0f}" stroke="#ff2a6a" stroke-width="8" stroke-linecap="round"/>' for a in range(-180,1,30))
b+=sparkle(170,200,30,'#fff')+sparkle(640,220,24,'#fff')
I[1722]=svg(b,d)

# 431 哀しくてジェラシー: a checked-pattern scarf fluttering from a 50s jukebox, a broken heart record spinning inside
d,b=bg([(0,'#1a1a2a'),(1,'#2a1a2a')])
b+='<path d="M200 760 L200 300 Q200 140 400 140 Q600 140 600 300 L600 760Z" fill="#c82a3a"/><path d="M240 740 L240 310 Q240 180 400 180 Q560 180 560 310 L560 740Z" fill="#ffd27a"/>'
b+='<circle cx="400" cy="330" r="110" fill="#1a1a1a"/>'+''.join(ring(400,330,40+k*16,'#3a3a3a',2) for k in range(4))+heart(400,330,40,'#e8102a')+bolt([(400,300),(392,330),(408,340),(400,370)],'#1a1a1a',4,1)
for i in range(6):
    for j in range(4): b+=f'<rect x="{270+i*44}" y="{500+j*44}" width="44" height="44" fill="{["#1a1a1a","#f4f4f4"][(i+j)%2]}"/>'
I[431]=svg(b,d)

# 761 Beautiful Fin: the tail fin of a whale rising out of an evening sea, water streaming off it like light
d,b=bg([(0,'#3a3a7a'),(.6,'#e8a08a'),(1,'#ffd8b0')])
b+=hinomaru_sun(600,460,70,'#fff2d0',.8)+'<rect y="480" width="800" height="320" fill="#2a3a6a"/>'+''.join(f'<rect x="{560-k*10}" y="{500+k*30}" width="{80+k*20}" height="5" fill="#ffd8b0" opacity=".6"/>' for k in range(8))
b+='<path d="M360 520 Q380 420 340 340 Q300 300 200 300 Q280 330 320 400 Q260 360 160 380 Q260 420 330 440 Q350 480 340 520Z" fill="#1a2440"/>'
for k in range(8): b+=f'<path d="M{220+k*16} {390+k*8} Q{230+k*16} {450+k*10} {226+k*16} {500+k*4}" stroke="#bfe0ff" stroke-width="3" fill="none" opacity=".6"/>'
b+=''.join(ring(350,520,40+k*40,'#bfe0ff',3,.5-k*.12) for k in range(3))
I[761]=svg(b,d)

# 1215 A-RA-SHI:Reborn: a whirlwind tornado spinning up from the ground, five coloured streaks of light twisting inside
d,b=bg([(0,'#1a2a4a'),(1,'#4a5a7a')])
for k in range(10): w=60+k*34;y=680-k*60;b+=f'<ellipse cx="{400+math.sin(k*.7)*30:.0f}" cy="{y}" rx="{w}" ry="{18+k*3}" fill="none" stroke="#c8d8f0" stroke-width="10" opacity=".55"/>'
for k,c in enumerate(['#3a8ae8','#e8302a','#ffe05a','#3ac85a','#a87aff']):
    b+=f'<path d="M{400+(k-2)*12} 680 Q{340+k*30} 400 {200+k*100} 100" stroke="{c}" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+='<rect y="680" width="800" height="120" fill="#2a3a2a"/>'
I[1215]=svg(b,d)

# 1216 Step and Go: a pair of sneakers stepping off a kerb onto a road painted with a big yellow forward arrow
d,b=bg([(0,'#c8e8ff'),(1,'#f0f8ff')])
b+='<rect y="420" width="800" height="380" fill="#6a6a74"/><rect y="400" width="800" height="40" fill="#c8c8d0"/>'
b+='<path d="M300 760 L300 640 L220 640 L400 480 L580 640 L500 640 L500 760Z" fill="#ffd02a"/>'
b+='<path d="M200 380 L200 330 Q210 290 240 290 L270 320 Q320 330 330 360 L330 380Z" fill="#e8302a"/><rect x="200" y="370" width="130" height="14" fill="#fff"/>'
b+='<path d="M380 440 L380 390 Q390 350 420 350 L450 380 Q500 390 510 420 L510 440Z" fill="#e8302a"/><rect x="380" y="430" width="130" height="14" fill="#fff"/>'
I[1216]=svg(b,d)

# 1217 サクラ: a single cherry blossom branch reaching across a moonlit river, petals floating on the dark water
d,b=bg([(0,'#1a1a3a'),(1,'#2a2a4a')])
b+=moon(600,180,60,'#fff6e8')+'<rect y="480" width="800" height="320" fill="#141a34"/><path d="M570 500 L630 500 L620 800 L580 800Z" fill="#fff6e8" opacity=".15"/>'
b+='<path d="M-10 120 Q200 160 360 300 Q420 350 520 360" stroke="#3a2418" stroke-width="22" fill="none"/><path d="M200 170 Q240 100 300 80 M330 280 Q380 220 440 220" stroke="#3a2418" stroke-width="10" fill="none"/>'
r=R(1217)
for _ in range(18): b+=sakura(r.uniform(60,540),r.uniform(80,400),r.uniform(18,30),'#ffc8d8','#fff',r.uniform(0,70),.95)
b+=petals(30,1217,'#ffc8d8',500,780,6,12,.8)
I[1217]=svg(b,d)

# 1218 Endless Game: a chessboard spiralling away into infinity, a single king piece standing at the centre
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
for k in range(10):
    s=700*(.78**k);a=k*12
    b+=f'<rect x="{400-s/2:.0f}" y="{400-s/2:.0f}" width="{s:.0f}" height="{s:.0f}" fill="{["#f4f0e8","#1a1a24"][k%2]}" transform="rotate({a} 400 400)"/>'
b+='<g fill="#c89a40"><rect x="380" y="320" width="40" height="80"/><path d="M360 420 L440 420 L430 400 L370 400Z"/><rect x="394" y="290" width="12" height="36"/><rect x="382" y="300" width="36" height="12"/></g>'
I[1218]=svg(b,d)

# 1502 Universe: a child's telescope pointing out of a bedroom window, the whole galaxy pouring in through it
d,b=bg([(0,'#04061a'),(1,'#1a0a3a')])
b+='<path d="M200 100 Q500 200 700 500" stroke="#c8a8ff" stroke-width="140" fill="none" opacity=".15"/>'+starsf(90,1502,800,'#e8f0ff')
b+='<rect x="80" y="80" width="640" height="560" fill="none" stroke="#3a2a4a" stroke-width="30"/><rect y="640" width="800" height="160" fill="#3a2a4a"/>'
b+='<rect x="220" y="520" width="240" height="44" rx="12" fill="#e8e8f0" transform="rotate(-30 340 540)"/><path d="M340 560 L300 640 M340 560 L380 640" stroke="#e8e8f0" stroke-width="8"/>'+glow(460,460,50,'#fff',.5)
I[1502]=svg(b,d)

# 1507 逆夢: a crimson thread connecting two hands across a shattered night sky full of falling stars
d,b=bg([(0,'#1a0410'),(1,'#0a0410')])
b+=starsf(50,1507,800,'#ffd8e8')
for x,y in [(160,160),(620,120),(480,260)]: b+=f'<path d="M{x} {y} L{x-80} {y+80}" stroke="#fff" stroke-width="3" opacity=".6"/>'
b+='<g fill="#e8c0a0"><rect x="40" y="560" width="200" height="60" rx="30" transform="rotate(-20 140 590)"/><rect x="560" y="420" width="200" height="60" rx="30" transform="rotate(-20 660 450)"/></g>'
b+='<path d="M230 540 Q400 700 570 460" stroke="#e8102a" stroke-width="6" fill="none"/>'+glow(400,560,100,'#e8102a',.3)
I[1507]=svg(b,d)

# 1547 I'm invincible: a black crown floating above a stage, shattering glass shards exploding outward around it
d,b=bg([(0,'#0a0a10'),(1,'#1a0a14')])
b+=glow(400,360,240,'#ff2a4a',.35)
r=R(1547)
for _ in range(30):
    a=r.uniform(0,2*math.pi);rr=r.uniform(180,360);x=400+rr*math.cos(a);y=360+rr*math.sin(a);s=r.uniform(14,40)
    b+=f'<polygon points="{x:.0f},{y-s:.0f} {x+s*.5:.0f},{y+s*.4:.0f} {x-s*.4:.0f},{y+s*.5:.0f}" fill="{r.choice(["#e8e8f8","#ff3a5a","#8a8aa8"])}" opacity=".85" transform="rotate({r.uniform(0,360):.0f} {x:.0f} {y:.0f})"/>'
b+='<path d="M240 460 L260 260 L330 360 L400 220 L470 360 L540 260 L560 460Z" fill="#0a0a0a" stroke="#ff3a5a" stroke-width="6"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="#ff2a4a"/>' for x,y in [(260,260),(400,220),(540,260)])
I[1547]=svg(b,d)

# 1846 シンデレラボーイ: a man's worn sneaker left on a midnight staircase in place of a glass slipper
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a4a')])
b+=moon(620,160,60,'#fff6e8')+starsf(30,1846,300,'#fff')
for k in range(6): b+=f'<rect x="-10" y="{460+k*60}" width="820" height="60" fill="{["#5a4a6a","#4a3a5a"][k%2]}"/>'
b+='<path d="M280 580 L280 520 Q290 480 330 480 L370 510 Q440 520 460 560 L460 580Z" fill="#c8c8d0"/><rect x="280" y="570" width="180" height="14" fill="#f4f4f4"/><path d="M310 510 L350 520 M310 530 L360 540" stroke="#5a5a64" stroke-width="5"/>'
b+='<text x="560" y="420" font-family="DejaVu Sans,sans-serif" font-size="40" fill="#fff6e8" opacity=".6">0:00</text>'
I[1846]=svg(b,d)

# 286 DIRTY OLD MAN ~さらば夏よ~: a battered surfboard leaning against a beach hut at summer's end, a single seagull overhead
d,b=bg([(0,'#ff9a6a'),(1,'#ffd8a0')])
b+=hinomaru_sun(560,400,90,'#fff2c8',.8)+'<rect y="420" width="800" height="120" fill="#3a6a9a"/><path d="M-10 520 Q400 500 810 520 L810 810 L-10 810Z" fill="#e8c890"/>'
b+='<rect x="120" y="320" width="260" height="280" fill="#8a5a3a"/><path d="M100 330 L250 250 L400 330Z" fill="#5a3a2a"/><rect x="200" y="420" width="80" height="180" fill="#3a2418"/>'
b+='<path d="M430 640 Q400 400 460 260 Q520 400 490 640Z" fill="#f4f4e8" transform="rotate(10 460 450)"/><path d="M460 280 L470 640" stroke="#e8302a" stroke-width="8" transform="rotate(10 460 450)"/>'
b+='<path d="M560 200 Q590 180 610 200 Q630 180 660 200" stroke="#3a3a44" stroke-width="6" fill="none"/>'
I[286]=svg(b,d)

# 455 待つわ: a girl in a long skirt waiting under a lamppost by a park gate, a pocket watch hanging from her hand
d,b=bg([(0,'#2a3a6a'),(1,'#6a5a8a')])
b+=moon(160,140,40)+'<rect y="620" width="800" height="180" fill="#3a4a3a"/><rect x="560" y="200" width="12" height="440" fill="#1a1a2a"/><rect x="540" y="180" width="52" height="40" rx="8" fill="#1a1a2a"/>'+glow(566,200,80,'#ffd88a',.6)
b+='<path d="M60 640 L60 380 M260 640 L260 380" stroke="#1a1a2a" stroke-width="14"/>'+''.join(f'<path d="M{80+k*20} 640 L{80+k*20} 420" stroke="#1a1a2a" stroke-width="4"/>' for k in range(9))
b+=figure(440,640,260,'#14101e',hair='#14101e')+'<path d="M394 520 Q380 560 390 580" stroke="#d8b040" stroke-width="3" fill="none"/><circle cx="390" cy="590" r="14" fill="#d8b040"/>'
I[455]=svg(b,d)

# 774 スカーレット: a field of scarlet poppies swaying under a hazy sun, a bicycle lying in the flowers
d,b=bg([(0,'#ffd8a0'),(1,'#ffb88a')])
b+=hinomaru_sun(400,240,90,'#fff4d8',.8)+'<rect y="420" width="800" height="380" fill="#4a8a3a"/>'
r=R(774)
for _ in range(60): x,y=r.uniform(0,800),r.uniform(430,800);s=8+(y-430)/12;b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="{r.choice(["#e8102a","#ff3a2a","#c80a1a"])}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="{s/3:.0f}" fill="#1a1a1a"/>'
b+='<g transform="rotate(-8 400 560)" opacity=".9"><circle cx="320" cy="580" r="50" fill="none" stroke="#2a2a34" stroke-width="8"/><circle cx="480" cy="580" r="50" fill="none" stroke="#2a2a34" stroke-width="8"/><path d="M320 580 L380 510 L460 510 L480 580 M380 510 L400 580 L460 510" stroke="#3a6ae8" stroke-width="10" fill="none"/></g>'
I[774]=svg(b,d)

# 834 BE WITH YOU: two snowflakes falling close together over a lit winter town, their arms just touching
d,b=bg([(0,'#1a2a5a'),(1,'#3a4a7a')])
b+=snow(40,834)+skyline(640,'#141c3a',834,60,180,'#ffd27a',60)+'<rect y="640" width="800" height="160" fill="#e8eef8"/>'
for x,y,s in [(320,320,1.0),(480,330,.95)]:
    for a in range(0,360,60):
        ca,sa=math.cos(math.radians(a)),math.sin(math.radians(a))
        b+=f'<path d="M{x} {y} L{x+110*s*ca:.0f} {y+110*s*sa:.0f}" stroke="#fff" stroke-width="10" stroke-linecap="round"/><path d="M{x+60*s*ca:.0f} {y+60*s*sa:.0f} L{x+60*s*ca+30*s*math.cos(math.radians(a+40)):.0f} {y+60*s*sa+30*s*math.sin(math.radians(a+40)):.0f} M{x+60*s*ca:.0f} {y+60*s*sa:.0f} L{x+60*s*ca+30*s*math.cos(math.radians(a-40)):.0f} {y+60*s*sa+30*s*math.sin(math.radians(a-40)):.0f}" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
b+=glow(400,325,60,'#fff',.6)
I[834]=svg(b,d)

# 983 Stay Gold: a golden pocket watch frozen at a sunny moment, light spilling from its open case
d,b=bg([(0,'#3a2a1a'),(1,'#1a1408')])
b+=glow(400,420,260,'#ffd27a',.45)+rays(400,420,20,'#ffe8a0',.15,6)
b+='<path d="M400 230 Q440 200 420 170 Q400 150 380 170 Q360 200 400 230" stroke="#d8b040" stroke-width="10" fill="none"/>'
b+='<circle cx="400" cy="420" r="190" fill="#d8a830"/><circle cx="400" cy="420" r="160" fill="#fff8e0"/>'+''.join(f'<rect x="396" y="270" width="8" height="24" fill="#5a3a1a" transform="rotate({a} 400 420)"/>' for a in range(0,360,30))
b+='<path d="M400 420 L400 320 M400 420 L470 450" stroke="#5a3a1a" stroke-width="10" stroke-linecap="round"/><circle cx="400" cy="420" r="12" fill="#d8a830"/>'+sparkle(520,300,40,'#fff')
I[983]=svg(b,d)

# 1458 喜劇: a dinner table set for a family, a comedic red nose and a party hat on top of the folded napkin
d,b=bg([(0,'#ffe8c8'),(1,'#ffd0a0')])
b+='<rect y="440" width="800" height="360" fill="#fff8ec"/>'+''.join(f'<rect x="{k*80}" y="440" width="40" height="360" fill="#ffd8d0" opacity=".6"/>' for k in range(10))
b+='<ellipse cx="400" cy="560" rx="200" ry="70" fill="#fff"/><ellipse cx="400" cy="556" rx="150" ry="48" fill="#f4f0e8"/>'
b+='<circle cx="400" cy="470" r="44" fill="#e8102a"/><ellipse cx="386" cy="456" rx="12" ry="8" fill="#fff" opacity=".6"/>'
b+='<path d="M560 520 L610 360 L660 520Z" fill="#3a8ae8"/><circle cx="610" cy="356" r="14" fill="#ffd02a"/>'+''.join(f'<circle cx="{590+k*14}" cy="{430+k*24}" r="6" fill="#fff"/>' for k in range(3))
b+='<path d="M160 640 L160 460 M140 460 L140 510 Q140 530 160 530 Q180 530 180 510 L180 460" stroke="#c8c8d0" stroke-width="8" fill="none"/>'
for x,y,c in [(180,200,'#ff5a8a'),(620,180,'#ffd02a'),(360,140,'#3ac87a'),(480,240,'#3a8ae8')]: b+=f'<rect x="{x}" y="{y}" width="14" height="24" fill="{c}" transform="rotate({x%90} {x} {y})"/>'
I[1458]=svg(b,d)

# 1512 晴る: a window flung open after the rain, a single raindrop on a leaf catching the returning sun
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+=rays(640,140,16,'#fff',.4,8)+hinomaru_sun(640,140,70,'#fffbe0',1)+cloud(200,200,1.4,'#d8e4f0')
b+='<path d="M120 800 Q260 500 520 460 Q420 600 340 800Z" fill="#4aa83a"/><path d="M160 780 Q300 560 500 470" stroke="#3a8a2a" stroke-width="6" fill="none"/>'
b+='<path d="M420 470 Q446 520 446 540 A26 26 0 0 1 394 540 Q394 520 420 470Z" fill="#d8f4ff" opacity=".9"/><ellipse cx="412" cy="532" rx="6" ry="10" fill="#fff"/>'+sparkle(430,500,24,'#fff')
I[1512]=svg(b,d)

# 1529 三原色: three overlapping circles of red, green and blue light blending into white at the centre
d,b=bg([(0,'#0a0a10'),(1,'#141418')])
for x,y,c in [(400,300,'#ff2a2a'),(300,470,'#2aff5a'),(500,470,'#2a5aff')]: b+=f'<circle cx="{x}" cy="{y}" r="190" fill="{c}" style="mix-blend-mode:screen" opacity=".9"/>'
I[1529]=svg(b,d)

# 1576 僕のこと: a lone sunflower standing taller than the rest in a field, turned toward the sun
d,b=bg([(0,'#3aa8f0'),(1,'#c8ecff')])
b+=hinomaru_sun(640,140,70,'#fffbe0',1)+'<rect y="560" width="800" height="240" fill="#5aa83a"/>'
for k,x in enumerate(range(40,800,90)):
    if x==400: continue
    y=560+(k%2)*30;b+=f'<path d="M{x} 800 L{x} {y}" stroke="#3a7a2a" stroke-width="8"/>'+f'<circle cx="{x}" cy="{y}" r="22" fill="#5a3a1a"/>'+''.join(f'<ellipse cx="{x+32*math.cos(math.radians(a)):.0f}" cy="{y+32*math.sin(math.radians(a)):.0f}" rx="14" ry="6" fill="#ffd02a" transform="rotate({a} {x+32*math.cos(math.radians(a)):.0f} {y+32*math.sin(math.radians(a)):.0f})"/>' for a in range(0,360,30))
b+='<path d="M400 800 L410 300" stroke="#3a7a2a" stroke-width="14"/><path d="M405 500 Q460 460 500 480 Q460 520 405 510Z" fill="#4a9a3a"/>'
b+='<circle cx="430" cy="270" r="50" fill="#5a3a1a"/>'+''.join(f'<ellipse cx="{430+76*math.cos(math.radians(a)):.0f}" cy="{270+76*math.sin(math.radians(a)):.0f}" rx="32" ry="13" fill="#ffd02a" transform="rotate({a} {430+76*math.cos(math.radians(a)):.0f} {270+76*math.sin(math.radians(a)):.0f})"/>' for a in range(0,360,24))
I[1576]=svg(b,d)

# 1769 ESCAPE: a figure leaping off a skyscraper rooftop into a vast moonlit sky, a trail of light behind them
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=moon(600,200,90,'#f4f0ff')+glow(600,200,140,'#d8d0ff',.3)+starsf(40,1769,500,'#fff')
b+='<rect x="0" y="480" width="300" height="320" fill="#0a0a18"/>'+''.join(f'<rect x="{30+i*60}" y="{520+j*60}" width="20" height="30" fill="#ffd27a" opacity=".7"/>' for i in range(4) for j in range(4) if (i+j)%3)
b+='<path d="M300 480 Q380 340 460 360" stroke="#bfe0ff" stroke-width="6" fill="none" stroke-dasharray="4 10"/><g transform="rotate(40 470 360)">'+figure(470,440,180,'#000',pose='up')+'</g>'
I[1769]=svg(b,d)

# 1809 明日への手紙: a letter folded into a paper bird flying out over a calm sea toward the sunrise
d,b=bg([(0,'#8ab0e8'),(.6,'#ffd8b0'),(1,'#ffe8c8')])
b+=hinomaru_sun(400,520,110,'#fff4d8',.9)+'<rect y="520" width="800" height="280" fill="#5a8ac8"/>'+''.join(f'<rect x="{360-k*14}" y="{540+k*30}" width="{80+k*28}" height="5" fill="#fff4d8" opacity=".6"/>' for k in range(8))
b+='<g transform="translate(360 280) rotate(-10)"><path d="M-100 0 L0 -20 L120 -60 L20 10Z" fill="#fff"/><path d="M0 -20 L20 10 L-20 50Z" fill="#e8e0f0"/><path d="M-60 -4 L40 -24 M-40 4 L50 -16" stroke="#8a8ab8" stroke-width="2"/></g>'
I[1809]=svg(b,d)

# 1858 Overdose: a cocktail glass overflowing with neon pink liquid, bubbles spilling onto a dark bar under a disco haze
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a3a')])
b+=glow(400,400,240,'#ff3ab8',.35)
b+='<path d="M240 240 L560 240 L420 440 L380 440Z" fill="#ff5ad8" opacity=".85"/><path d="M240 240 Q260 300 230 380 Q210 420 240 460 M560 240 Q540 310 570 380" stroke="#ff5ad8" stroke-width="16" fill="none" stroke-linecap="round"/>'
b+='<rect x="392" y="440" width="16" height="180" fill="#e8d8f0"/><ellipse cx="400" cy="620" rx="80" ry="16" fill="#e8d8f0"/><rect y="640" width="800" height="160" fill="#140818"/>'
r=R(1858)
for _ in range(16): b+=ring(r.uniform(260,540),r.uniform(120,400),r.uniform(6,16),'#ffd0f8',3,.8)
I[1858]=svg(b,d)

# 225 銀の龍の背に乗って: a silver dragon soaring over storm clouds, a tiny figure riding on its back toward the light
d,b=bg([(0,'#3a4a6a'),(1,'#8a9ab8')])
b+=rays(640,120,16,'#fff',.35,6)+cloud(160,560,2.0,'#5a6a84')+cloud(600,640,2.2,'#5a6a84')
b+='<path d="M60 520 Q200 380 340 440 Q460 500 560 380 Q620 300 700 280" stroke="#c8d0e0" stroke-width="54" fill="none" stroke-linecap="round"/><path d="M60 520 Q200 380 340 440 Q460 500 560 380 Q620 300 700 280" stroke="#e8eef8" stroke-width="20" fill="none" stroke-linecap="round" stroke-dasharray="20 18"/>'
b+='<path d="M700 280 L760 250 L740 290 L780 300 L720 310Z" fill="#c8d0e0"/><circle cx="720" cy="276" r="6" fill="#1a1a2a"/><path d="M720 260 L740 220 M710 262 L716 220" stroke="#c8d0e0" stroke-width="6"/>'
b+=figure(470,470,80,'#1a1a2a')
I[225]=svg(b,d)

# 487 JEALOUSYを眠らせて: a green-eyed black cat curled asleep on a velvet chair under a dim lamp
d,b=bg([(0,'#1a1a24'),(1,'#2a1a24')])
b+=glow(600,200,180,'#ffc870',.4)+'<path d="M560 200 L640 200 L660 120 L540 120Z" fill="#a83a3a"/><rect x="596" y="200" width="8" height="300" fill="#3a2a1a"/>'
b+='<path d="M140 680 L140 380 Q140 300 240 300 L440 300 Q540 300 540 380 L540 680Z" fill="#6a0a1a"/><rect x="120" y="500" width="440" height="160" rx="30" fill="#8a1a2a"/>'
b+='<ellipse cx="340" cy="490" rx="130" ry="60" fill="#0a0a0a"/><circle cx="240" cy="470" r="44" fill="#0a0a0a"/><path d="M210 440 L220 400 L240 430 M260 430 L276 400 L280 444" fill="#0a0a0a"/><path d="M220 470 Q228 466 236 470 M248 470 Q256 466 264 470" stroke="#5ae85a" stroke-width="3" fill="none"/>'
b+='<path d="M460 500 Q520 520 480 560 Q440 580 420 540" stroke="#0a0a0a" stroke-width="18" fill="none" stroke-linecap="round"/>'
I[487]=svg(b,d)

# 674 それが大事: a hand-written list of four promises pinned with a red push pin, one word circled
d,b=bg([(0,'#c8a880'),(1,'#a8885a')])
for k in range(30): b+=f'<circle cx="{(k*137)%800}" cy="{(k*91)%800}" r="3" fill="#8a6a4a"/>'
b+='<rect x="200" y="140" width="400" height="520" fill="#fffbe8" transform="rotate(3 400 400)"/>'
for k in range(4): b+=f'<circle cx="260" cy="{260+k*100}" r="10" fill="#3a3a5a"/><path d="M290 {260+k*100} Q400 {250+k*100} {520-k*20} {262+k*100}" stroke="#3a3a5a" stroke-width="8" fill="none"/>'
b+='<ellipse cx="410" cy="560" rx="140" ry="40" fill="none" stroke="#e8102a" stroke-width="6"/><circle cx="400" cy="150" r="22" fill="#e8102a"/>'
I[674]=svg(b,d)

# 835 口唇: a pair of glossy lips with a single drop of rain on them, under an electric-blue light
d,b=bg([(0,'#0a1a3a'),(1,'#04081a')])
b+=glow(400,420,240,'#2a8aff',.4)
b+='<g transform="translate(400 420) scale(2.4)"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="#c80a3a"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="#a80a2a"/><ellipse cx="-40" cy="40" rx="24" ry="8" fill="#fff" opacity=".4"/></g>'
b+='<path d="M520 360 Q540 400 540 416 A20 20 0 0 1 500 416 Q500 400 520 360Z" fill="#bfe8ff"/>'+rain(30,835,'#5aa8ff',.3,5)
I[835]=svg(b,d)

# 1403 グランドエスケープ: a hot-air balloon rising through the clouds toward a sky bursting with stars
d,b=bg([(0,'#04061e'),(.5,'#2a2a6a'),(1,'#ff9a7a')])
b+=starsf(60,1403,400,'#fff')+cloud(160,620,2.0,'#ffb8a0')+cloud(620,680,2.2,'#ffb8a0')
b+='<path d="M400 160 Q540 160 540 300 Q540 400 440 470 L360 470 Q260 400 260 300 Q260 160 400 160Z" fill="#e8302a"/>'+''.join(f'<path d="M400 160 Q{400+dx} 300 {400+dx*.5:.0f} 470" stroke="#ffd02a" stroke-width="12" fill="none"/>' for dx in (-100,0,100))
b+='<path d="M370 470 L380 520 M430 470 L420 520" stroke="#5a3a1a" stroke-width="4"/><rect x="370" y="520" width="60" height="44" fill="#8a5a2a"/>'
I[1403]=svg(b,d)

# 1419 ヒロイン: a pair of mittens on a snowy station bench, one bare hand reaching to warm another in the cold
d,b=bg([(0,'#c8d8ec'),(1,'#f0f4fa')])
b+=snow(80,1419)+'<rect y="600" width="800" height="200" fill="#e8eef8"/>'
b+='<rect x="140" y="480" width="520" height="24" fill="#8a5a3a"/><rect x="150" y="500" width="14" height="100" fill="#3a3a44"/><rect x="636" y="500" width="14" height="100" fill="#3a3a44"/><rect x="140" y="470" width="520" height="12" fill="#fff"/>'
for x,c in [(300,'#e8302a'),(480,'#3a6ae8')]: b+=f'<path d="M{x-40} 470 L{x-40} 400 Q{x-40} 360 {x} 360 Q{x+40} 360 {x+40} 400 L{x+40} 470Z" fill="{c}"/><path d="M{x+40} 420 Q{x+70} 400 {x+64} 380 Q{x+54} 370 {x+40} 390" fill="{c}"/><rect x="{x-44}" y="450" width="88" height="20" fill="#fff"/>'
b+=heart(390,300,30,'#ff7a9a')
I[1419]=svg(b,d)

# 1445 カタオモイ: a single guitar pick and a love note slipped into a school locker, left slightly ajar
d,b=bg([(0,'#8a9ab0'),(1,'#5a6a80')])
for x in (60,260,460,660): b+=f'<rect x="{x}" y="60" width="180" height="700" fill="#a8b4c4" stroke="#6a7a8a" stroke-width="6"/>'+''.join(f'<rect x="{x+40}" y="{100+k*16}" width="100" height="6" fill="#6a7a8a"/>' for k in range(4))
b+='<path d="M460 60 L380 100 L380 720 L460 760Z" fill="#8a96a8"/><rect x="470" y="70" width="160" height="680" fill="#2a3040"/>'
b+='<rect x="480" y="420" width="120" height="80" fill="#fff8f0" transform="rotate(-10 540 460)"/>'+heart(540,456,18,'#ff5a7a')+'<path d="M520 560 Q560 556 580 580 Q570 620 550 640 Q520 600 520 560Z" fill="#ffd02a"/>'
I[1445]=svg(b,d)

# 309 順子: a long-haired woman's silhouette walking away down a rainy street, an acoustic guitar case left standing in the rain
d,b=bg([(0,'#6a7a9a'),(1,'#a8b0c8')])
b+=rain(100,309,'#e8f0ff',.5,6)+skyline(560,'#4a5470',309,80,300,'#ffd27a',40)+'<rect y="560" width="800" height="240" fill="#3a4258"/>'
for x in (200,500): b+=f'<rect x="{x}" y="580" width="60" height="200" fill="#ffd27a" opacity=".15"/>'
b+=figure(560,620,200,'#0a0c14',hair='#0a0c14')+'<path d="M534 438 Q520 520 530 560" stroke="#0a0c14" stroke-width="16" fill="none"/>'
b+=guitar(240,700,.7,-8,'#a8602a')
I[309]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
