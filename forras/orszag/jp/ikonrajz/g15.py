import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 15. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def lips(x,y,s,c1='#e8102a',c2='#c80a20'): return f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="{c1}"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="{c2}"/></g>'
def bottle(x,y,s,col):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-14 -120 L14 -120 L14 -70 Q50 -50 50 0 L50 90 Q50 110 30 110 L-30 110 Q-50 110 -50 90 L-50 0 Q-50 -50 -14 -70Z" fill="{col}"/><rect x="-16" y="-136" width="32" height="20" rx="4" fill="#d8b040"/></g>'

# 546 くちびるから媚薬: a tiny heart-shaped perfume bottle pressed to glossy red lips, pink mist curling out
d,b=bg([(0,'#3a0a2a'),(1,'#1a0414')])
b+=glow(400,420,240,'#ff3a8a',.35)+lips(340,480,1.3)
b+='<path d="M520 300 C470 260 470 200 510 196 C530 194 540 210 540 220 C540 210 550 194 570 196 C610 200 610 260 560 300Z" fill="#ff8ad0" opacity=".9"/><rect x="530" y="170" width="20" height="30" fill="#d8b040"/>'
for k in range(5): b+=f'<circle cx="{460-k*30}" cy="{300+k*20}" r="{14+k*6}" fill="#ffb0e0" opacity="{.5-k*.08:.2f}"/>'
I[546]=svg(b,d)

# 617 LOVE SONG: a vinyl record whose grooves form a heart, spinning on a turntable under warm light
d,b=bg([(0,'#2a1a2a'),(1,'#1a0e1a')])
b+=glow(400,400,260,'#ffc870',.3)+'<rect x="80" y="160" width="640" height="500" rx="20" fill="#5a3a2a"/><circle cx="380" cy="410" r="210" fill="#141414"/>'
for k in range(6): s=1-k*.13;b+=f'<path d="M380 {520-k*12} C{380-200*s:.0f} {430-k*8} {380-150*s:.0f} {300+k*10} 380 {340+k*10} C{380+150*s:.0f} {300+k*10} {380+200*s:.0f} {430-k*8} 380 {520-k*12}Z" fill="none" stroke="#3a3a3a" stroke-width="3"/>'
b+='<circle cx="380" cy="410" r="50" fill="#e8302a"/><circle cx="380" cy="410" r="6" fill="#f4f4f4"/><path d="M660 200 L640 420 L520 500" stroke="#c8c8d0" stroke-width="10" fill="none"/><rect x="500" y="490" width="40" height="24" rx="4" fill="#3a3a44"/>'
I[617]=svg(b,d)

# 763 ロビンソン: a robin perched on a cherry branch high above a river town at golden hour
d,b=bg([(0,'#ffb07a'),(1,'#ffe0b0')])
b+=hinomaru_sun(560,420,90,'#fff4d0',.8)+skyline(620,'#a86a5a',763,40,140,'#ffe0b0',40)+'<rect y="620" width="800" height="180" fill="#6a8ab8"/>'
b+='<path d="M-10 300 Q260 280 420 340 Q520 380 620 360" stroke="#3a2418" stroke-width="20" fill="none"/>'+''.join(sakura(x,y,22,'#ffc0d4','#fff',x%70,1) for x,y in [(140,270),(230,300),(520,350),(600,340)])
b+='<g transform="translate(380 290)"><ellipse cx="0" cy="0" rx="60" ry="46" fill="#7a5a3a"/><ellipse cx="18" cy="10" rx="34" ry="30" fill="#e8601a"/><circle cx="40" cy="-30" r="30" fill="#7a5a3a"/><circle cx="50" cy="-36" r="5" fill="#1a1a1a"/><path d="M68 -32 L88 -28 L68 -22Z" fill="#3a2a1a"/><path d="M-50 -10 L-100 -30 L-90 10Z" fill="#5a4028"/><path d="M0 44 L-4 62 M14 44 L14 62" stroke="#3a2a1a" stroke-width="4"/></g>'
I[763]=svg(b,d)

# 1000 Days: a wall calendar with its pages flying off one by one into a soft pastel sky
d,b=bg([(0,'#d8e8ff'),(1,'#ffe8f0')])
b+='<rect x="140" y="420" width="260" height="300" fill="#fff" stroke="#c8c8d8" stroke-width="5"/><rect x="140" y="420" width="260" height="60" fill="#ff7aa8"/><text x="270" y="640" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="130" fill="#3a3a5a">24</text><circle cx="200" cy="420" r="10" fill="#8a8a94"/><circle cx="340" cy="420" r="10" fill="#8a8a94"/>'
for k,(x,y,a) in enumerate([(440,360,15),(520,260,-20),(610,170,30),(680,90,-10)]):
    b+=f'<g transform="rotate({a} {x} {y})"><rect x="{x-60}" y="{y-70}" width="{120-k*10}" height="{140-k*14}" fill="#fff" stroke="#e0d8e8" stroke-width="3"/><rect x="{x-60}" y="{y-70}" width="{120-k*10}" height="24" fill="#ff7aa8"/></g>'
I[1000]=svg(b,d)

# 1077 サボテン: a little cactus in a pot on a rainy windowsill, a single bright flower blooming on top
d,b=bg([(0,'#7a8ab0'),(1,'#a8b8d0')])
b+='<rect x="100" y="60" width="600" height="460" fill="#9ab0d0"/>'+rain(50,1077,'#e8f0ff',.5,5)+'<path d="M100 60 L700 60 L700 520 L100 520Z M400 60 L400 520" stroke="#f4f0e8" stroke-width="18" fill="none"/>'
b+='<rect y="520" width="800" height="280" fill="#e8dcc8"/><path d="M320 560 L480 560 L460 700 L340 700Z" fill="#c8704a"/><rect x="310" y="540" width="180" height="30" rx="6" fill="#d8805a"/>'
b+='<rect x="360" y="340" width="80" height="220" rx="40" fill="#5aa84a"/><rect x="290" y="400" width="50" height="100" rx="25" fill="#5aa84a"/><path d="M340 470 L360 470" stroke="#5aa84a" stroke-width="30"/><rect x="460" y="380" width="50" height="90" rx="25" fill="#5aa84a"/><path d="M440 440 L460 440" stroke="#5aa84a" stroke-width="30"/>'
b+=''.join(f'<path d="M{x} {y} l-10 -4 M{x} {y} l10 -4" stroke="#e8f8d8" stroke-width="2"/>' for x,y in [(380,380),(420,420),(380,480),(420,520),(310,430),(480,410)])+flower(400,330,40,6,'#ff4a8a','#ffd02a',0,.65)
I[1077]=svg(b,d)

# 1108 もっと強く: a clenched fist rising out of a stormy sea of grey, lightning striking around it
d,b=bg([(0,'#2a2a3a'),(1,'#4a4a5a')])
b+=bolt([(140,0),(200,140),(160,160),(240,320)],'#fff6c8',8,1)+bolt([(680,0),(620,120),(660,140),(600,280)],'#fff6c8',8,1)
b+='<rect y="600" width="800" height="200" fill="#2a3a4a"/>'+''.join(f'<path d="M-10 {620+k*40} Q100 {600+k*40} 200 {620+k*40} T400 {620+k*40} T600 {620+k*40} T810 {620+k*40}" stroke="#5a6a7a" stroke-width="6" fill="none"/>' for k in range(5))
b+='<g fill="#d8a888"><rect x="340" y="420" width="120" height="240"/><rect x="310" y="260" width="180" height="180" rx="40"/></g><path d="M320 300 L480 300 M320 350 L480 350 M320 400 L480 400" stroke="#b8886a" stroke-width="8"/><rect x="290" y="330" width="60" height="100" rx="24" fill="#c8987a"/>'
b+=glow(400,340,200,'#fff6c8',.2)
I[1108]=svg(b,d)

# 1552 阿修羅ちゃん: a six-armed silhouette dancing in a ring of red neon flames, each hand making a different gesture
d,b=bg([(0,'#1a0408'),(1,'#0a0204')])
b+=glow(400,420,260,'#ff2a2a',.35)+ring(400,420,250,'#ff3a3a',10,.8)
for k in range(12): a=math.radians(k*30);b+=f'<path d="M{400+250*math.cos(a):.0f} {420+250*math.sin(a):.0f} q10 -40 0 -70 q-10 30 0 70Z" fill="#ff6a2a"/>'
b+='<g fill="#000"><circle cx="400" cy="260" r="40"/><path d="M370 300 L430 300 L440 480 L420 640 L400 640 L400 500 L380 640 L360 640 L360 480Z"/></g>'
for a in (-50,-10,30): b+=f'<path d="M370 340 L{370-160*math.cos(math.radians(a)):.0f} {340+160*math.sin(math.radians(a)):.0f}" stroke="#000" stroke-width="18" stroke-linecap="round"/><path d="M430 340 L{430+160*math.cos(math.radians(a)):.0f} {340+160*math.sin(math.radians(a)):.0f}" stroke="#000" stroke-width="18" stroke-linecap="round"/>'
I[1552]=svg(b,d)

# 1039 眠れぬ夜は君のせい: a wide-awake alarm clock beside a phone glowing with a heart at 3 a.m., moonlight on the sheets
d,b=bg([(0,'#0a1028'),(1,'#1a1a3a')])
b+='<rect x="500" y="60" width="240" height="280" fill="#1a2a5a"/>'+moon(620,180,50)+'<rect x="500" y="60" width="240" height="280" fill="none" stroke="#06081a" stroke-width="16"/>'
b+='<path d="M-10 520 Q200 480 400 520 T810 520 L810 810 L-10 810Z" fill="#3a3a6a"/><polygon points="500,340 740,340 600,800 300,800" fill="#c8d8ff" opacity=".08"/>'
b+='<circle cx="220" cy="460" r="90" fill="#e8e8f0"/><circle cx="220" cy="460" r="72" fill="#1a1a2a"/><text x="220" y="478" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="42" fill="#5aff8a">3:00</text>'
b+=glow(480,560,90,'#ff8ab8',.5)+'<rect x="430" y="500" width="100" height="160" rx="14" fill="#1a1a24" transform="rotate(10 480 580)"/><rect x="440" y="512" width="80" height="134" rx="6" fill="#ffd0e8" transform="rotate(10 480 580)"/>'+heart(482,580,24,'#ff2a6a')
I[1039]=svg(b,d)

# 1088 小さな恋のうた: a tiny guitar with a heart-shaped soundhole on an Okinawan beach, hibiscus and a starry sky
d,b=bg([(0,'#0a1a4a'),(1,'#2a3a7a')])
b+=starsf(60,1088,500,'#fff')+'<rect y="460" width="800" height="120" fill="#0a3a6a"/><path d="M-10 560 Q400 530 810 560 L810 810 L-10 810Z" fill="#e8d8b0"/>'
b+='<g transform="translate(400 560) rotate(-20) scale(1.1)"><ellipse cx="0" cy="60" rx="70" ry="64" fill="#e8a050"/><ellipse cx="0" cy="-10" rx="52" ry="50" fill="#e8a050"/><rect x="-8" y="-220" width="16" height="200" fill="#5a3a1a"/><rect x="-14" y="-260" width="28" height="44" rx="4" fill="#5a3a1a"/></g>'+heart(410,600,26,'#3a1a0a')
b+=flower(160,640,56,5,'#e8102a','#ffd02a',10,.6)+flower(660,680,46,5,'#ff5a7a','#ffd02a',30,.6)
I[1088]=svg(b,d)

# 1344 夜明けまで強がらなくてもいい: a girl curled on a rooftop at the edge of dawn, a warm blanket of sunrise light reaching her
d,b=bg([(0,'#1a1a4a'),(.6,'#8a5a8a'),(1,'#ffb08a')])
b+=hinomaru_sun(600,620,120,'#fff0d0',.7)+skyline(640,'#2a1a3a',1344,60,240,'#ffd27a',30)
b+='<rect x="140" y="540" width="360" height="260" fill="#3a2a4a"/>'+glow(300,500,110,'#ffc88a',.35)+'<g fill="#0a0814"><circle cx="300" cy="440" r="40"/><path d="M240 540 Q240 470 300 476 Q370 480 380 540Z"/><path d="M340 510 Q400 506 410 540 L340 540Z"/></g>'
b+='<polygon points="600,620 300,540 380,540" fill="#ffd8a0" opacity=".25"/>'
I[1344]=svg(b,d)

# 1517 TAIDADA: a lazy cat sprawled across an unfinished homework sheet, a ballpoint pen rolled away, neon purple room
d,b=bg([(0,'#2a1a4a'),(1,'#1a0a2a')])
b+=glow(400,420,240,'#c85aff',.25)+'<rect y="500" width="800" height="300" fill="#3a2a5a"/>'
b+='<rect x="200" y="480" width="360" height="220" fill="#fbf8f0" transform="rotate(-6 380 590)"/>'+''.join(f'<path d="M230 {520+k*30} L520 {490+k*30}" stroke="#a8a8c8" stroke-width="3"/>' for k in range(6))
b+='<g fill="#1a1a24"><ellipse cx="400" cy="560" rx="170" ry="60"/><circle cx="240" cy="540" r="54"/><path d="M200 500 L210 450 L240 490 M260 490 L280 450 L290 500"/></g><path d="M560 560 Q640 600 660 540" stroke="#1a1a24" stroke-width="22" fill="none" stroke-linecap="round"/>'
b+='<path d="M220 540 Q228 534 236 540 M248 540 Q256 534 264 540" stroke="#ffe05a" stroke-width="4" fill="none"/><rect x="600" y="680" width="140" height="16" rx="8" fill="#5ae8ff" transform="rotate(20 670 688)"/>'
b+='<text x="300" y="330" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="60" fill="#c8a8ff" opacity=".7">z z</text>'
I[1517]=svg(b,d)

# 1850 花になって: a girl's hand slowly turning into petals that drift upward from her fingertips into a bright sky
d,b=bg([(0,'#a8e0ff'),(1,'#fff0f8')])
b+=glow(400,300,220,'#fff',.6)
b+='<g fill="#e8c0a0"><rect x="300" y="520" width="140" height="300" rx="50"/><rect x="304" y="400" width="26" height="140" rx="13"/><rect x="336" y="380" width="26" height="160" rx="13"/><rect x="368" y="390" width="26" height="150" rx="13"/><rect x="400" y="420" width="24" height="120" rx="12"/></g>'
r=R(1850)
for k in range(26): x=340+r.uniform(-80,140);y=380-k*14+r.uniform(-20,20);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{10+k%4*3}" ry="6" fill="{r.choice(["#ff8ab8","#ffd02a","#ffb0c8","#a8e05a"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[1850]=svg(b,d)

# 302 大都会: a tiny figure standing at the bottom of a canyon of towering skyscrapers, a sliver of sky above
d,b=bg([(0,'#5a7ab8'),(1,'#1a1a2a')])
b+='<path d="M-10 -10 L260 -10 L330 800 L-10 800Z" fill="#2a2a3a"/><path d="M810 -10 L540 -10 L470 800 L810 800Z" fill="#3a3a4a"/>'
for k in range(14): b+=f'<rect x="{40+(k%3)*70}" y="{40+k*50}" width="40" height="24" fill="#ffd27a" opacity="{.4+(k%3)*.2:.1f}"/><rect x="{580+(k%3)*70}" y="{40+k*50}" width="40" height="24" fill="#ffd27a" opacity="{.4+((k+1)%3)*.2:.1f}"/>'
b+='<rect y="720" width="800" height="80" fill="#14141e"/>'+figure(400,730,90,'#000')
I[302]=svg(b,d)

# 394 BLONDE: long flowing blonde hair seen from behind, whipping in the wind against a deep red sunset
d,b=bg([(0,'#c80a2a'),(1,'#3a0a14')])
b+=hinomaru_sun(560,300,110,'#ffd08a',.7)
b+='<path d="M300 800 Q300 600 340 520 Q380 440 400 420 Q440 440 470 520 Q500 600 500 800Z" fill="#1a0a0a"/>'
b+='<path d="M360 300 Q400 240 450 290 Q520 340 600 360 Q700 380 760 460 Q660 430 600 440 Q660 500 720 600 Q600 520 520 500 Q480 560 470 640 Q420 560 400 480 Q340 440 340 360Z" fill="#f4d070"/><path d="M420 300 Q500 360 600 380 M440 360 Q540 420 640 500 M430 420 Q480 480 500 560" stroke="#d8a838" stroke-width="5" fill="none"/>'
I[394]=svg(b,d)

# 433 あの娘とスキャンダル: a tabloid newspaper with a big red headline and a lipstick kiss, paparazzi flash bursts behind
d,b=bg([(0,'#1a1a24'),(1,'#2a2a34')])
for x,y in [(140,160),(640,200),(700,560)]: b+=rays(x,y,12,'#fff',.25,4)+glow(x,y,70,'#fff',.7)
b+='<g transform="rotate(-8 400 440)"><rect x="180" y="200" width="440" height="500" fill="#f4f0e4"/><rect x="200" y="220" width="400" height="80" fill="#e8102a"/><text x="400" y="282" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="62" fill="#fff">SCANDAL!</text>'
b+='<rect x="210" y="320" width="180" height="200" fill="#8a8a94"/>'+''.join(f'<rect x="410" y="{330+k*30}" width="170" height="10" fill="#8a8a8a"/>' for k in range(6))+''.join(f'<rect x="210" y="{540+k*30}" width="370" height="10" fill="#8a8a8a"/>' for k in range(5))+'</g>'
b+=lips(330,430,.45)
I[433]=svg(b,d)

# 653 MOTEL: a roadside motel neon sign buzzing in pink and blue at night, one window lit
d,b=bg([(0,'#0a0a2a'),(1,'#1a1030')])
b+=starsf(30,653,300,'#fff')+'<rect y="600" width="800" height="200" fill="#14141e"/>'
b+='<rect x="80" y="440" width="640" height="180" fill="#2a2a3a"/>'+''.join(f'<rect x="{110+k*100}" y="480" width="60" height="90" fill="{"#ffd27a" if k==3 else "#1a1a24"}"/>' for k in range(6))+glow(440,525,60,'#ffd27a',.4)
b+='<rect x="560" y="140" width="16" height="300" fill="#3a3a44"/>'+neon(560,260,'MOTEL','#ff5ab8',110,'DejaVu Sans,sans-serif')
b+='<path d="M440 330 L470 290 L500 330" stroke="#5ae8ff" stroke-width="8" fill="none"/>'
I[653]=svg(b,d)

# 711 瞳そらさないで: two pairs of eyes locked across a crowded summer beach, a bold line of sight connecting them
d,b=bg([(0,'#3ab0f8'),(1,'#c8ecff')])
b+='<rect y="380" width="800" height="140" fill="#1a90d8"/><path d="M-10 520 Q400 490 810 520 L810 810 L-10 810Z" fill="#f4d890"/>'
for x,c in [(180,'#5a3a1a'),(620,'#1a3a6a')]: b+=f'<path d="M{x-90} 260 Q{x} 180 {x+90} 260 Q{x} 340 {x-90} 260Z" fill="#fff" stroke="#2a2a3a" stroke-width="6"/><circle cx="{x}" cy="260" r="40" fill="{c}"/><circle cx="{x}" cy="260" r="18" fill="#000"/><circle cx="{x+12}" cy="248" r="8" fill="#fff"/>'
b+='<path d="M280 260 L520 260" stroke="#ff5a7a" stroke-width="6" stroke-dasharray="14 10"/>'+heart(400,260,24,'#ff2a5a')
I[711]=svg(b,d)

# 836 とまどい: a figure standing at a fork where a path splits into a sunny road and a misty forest, hesitant
d,b=bg([(0,'#a8c0d8'),(1,'#e8eef4')])
b+='<rect x="0" y="0" width="400" height="800" fill="#ffd8a0" opacity=".4"/><rect y="460" width="800" height="340" fill="#7aa86a"/>'
for x in (520,600,680,760): b+=f'<path d="M{x} 470 L{x+40} 330 L{x+80} 470Z" fill="#3a5a4a" opacity=".7"/>'
b+='<path d="M360 800 L380 620 L180 460 L260 460 L400 580 L520 460 L600 460 L420 620 L440 800Z" fill="#d8c8a0"/><rect y="0" width="800" height="800" fill="url(#ms)"/>'
d+=lg('ms',S((0,'#fff',0),(.5,'#fff',0),(1,'#fff',.6)),0,0,1,0)
b+=figure(400,660,170,'#2a2a3a')+'<text x="420" y="440" font-family="DejaVu Sans,sans-serif" font-weight="bold" font-size="60" fill="#5a5a6a">?</text>'
I[836]=svg(b,d)

# 864 MY HEART DRAWS A DREAM: a glowing pen nib drawing a line of light that becomes a flying bird across a night sky
d,b=bg([(0,'#0a1438'),(1,'#2a2a5a')])
b+=starsf(60,864,800,'#fff')
b+='<path d="M180 640 Q260 520 360 520 Q460 520 520 420 Q560 340 600 300" stroke="#ffe8a0" stroke-width="6" fill="none"/>'+glow(600,300,40,'#ffe8a0',.7)
b+='<g transform="translate(620 260) rotate(-20)"><path d="M-30 10 Q0 -10 40 0 Q60 10 70 -10 Q60 30 30 30 Q-10 40 -30 10Z" fill="#ffe8a0"/><path d="M0 0 Q-40 -80 -110 -70 Q-60 -30 -10 10Z M10 0 Q60 -90 130 -90 Q90 -40 20 10Z" fill="#fff4c8"/></g>'
b+='<g transform="rotate(30 160 680)"><path d="M140 600 L180 600 L180 760 L140 760Z" fill="#2a2a4a"/><path d="M140 600 L160 540 L180 600Z" fill="#d8b040"/></g>'+glow(170,620,40,'#ffe8a0',.6)
I[864]=svg(b,d)

# 1553 Tot Musica: a sheet of music bursting into dark crimson flames, notes turning into black smoke birds
d,b=bg([(0,'#1a0408'),(1,'#0a0204')])
b+=glow(400,480,260,'#e8302a',.4)
b+='<g transform="rotate(-6 400 500)"><rect x="220" y="360" width="360" height="300" fill="#f4ecd8"/>'+''.join(f'<path d="M240 {400+k*50} L560 {400+k*50} M240 {408+k*50} L560 {408+k*50} M240 {416+k*50} L560 {416+k*50}" stroke="#8a7a6a" stroke-width="2"/>' for k in range(5))+''.join(note(260+j*70,420+(j%3)*50,16,'#1a1a1a',j%2==0) for j in range(5))+'</g>'
b+='<path d="M220 380 Q260 300 300 350 Q320 260 380 330 Q420 220 460 320 Q500 260 540 350 Q580 300 600 380 Z" fill="#e8302a"/><path d="M260 370 Q300 320 330 360 Q370 300 400 350 Q440 290 480 350 Q520 320 560 380Z" fill="#ffa83a"/>'
for k,(x,y,s) in enumerate([(300,200,1),(420,140,.8),(540,190,.9),(620,110,.6)]): b+=f'<path d="M{x-40*s:.0f} {y} Q{x-16*s:.0f} {y-30*s:.0f} {x} {y} Q{x+16*s:.0f} {y-30*s:.0f} {x+40*s:.0f} {y}" stroke="#0a0a0a" stroke-width="{10*s:.0f}" fill="none" stroke-linecap="round"/>'
I[1553]=svg(b,d)

# 297 魅せられて: a white gown billowing in the wind like a giant sail on a Mediterranean terrace at sunset
d,b=bg([(0,'#3a6ab8'),(.6,'#ff9a7a'),(1,'#ffd0a0')])
b+=hinomaru_sun(640,440,80,'#fff2d0',.8)+'<rect y="460" width="800" height="120" fill="#2a5aa8"/><rect y="580" width="800" height="220" fill="#f4ece0"/>'
b+='<path d="M300 280 Q260 380 200 580 Q340 520 560 600 Q640 460 760 380 Q560 400 420 300Z" fill="#fff" opacity=".95"/><path d="M300 280 Q400 380 560 600 M330 320 Q300 460 260 570" stroke="#e8e8f0" stroke-width="4" fill="none"/>'
b+=figure(320,600,320,'#1a0a14',pose='up',hair='#1a0a14')
I[297]=svg(b,d)

# 780 蛍: fireflies rising from a dark riverbank into a summer night, their lights reflected in the slow water
d,b=bg([(0,'#04081a'),(1,'#0a1a2a')])
b+=starsf(30,780,400,'#c8d8ff')+'<rect y="520" width="800" height="280" fill="#06101e"/>'
b+='<path d="M-10 540 Q200 500 400 540 T810 520 L810 560 L-10 560Z" fill="#0a1a10"/>'+''.join(f'<path d="M{x} 560 L{x+(x%3-1)*10} {460-(x%50)}" stroke="#1a3a1a" stroke-width="4"/>' for x in range(10,800,22))
r=R(780)
for _ in range(40):
    x,y=r.uniform(40,760),r.uniform(160,520);b+=glow(x,y,14,'#c8ff5a',.6,'glow2')+f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#e8ff8a"/>'
    if y>360: b+=f'<circle cx="{x:.0f}" cy="{1120-y:.0f}" r="3" fill="#c8ff5a" opacity=".4"/>'
I[780]=svg(b,d)

# 1560 花占い: a daisy losing its petals one by one, the last petal floating in a heart-shaped breeze
d,b=bg([(0,'#c8f0d8'),(1,'#fff8e0')])
b+='<path d="M400 800 Q390 600 410 420" stroke="#4a9a3a" stroke-width="12" fill="none"/><path d="M400 620 Q460 580 500 600 Q460 640 400 630Z" fill="#5ac84a"/>'
b+='<circle cx="410" cy="380" r="50" fill="#ffd02a"/>'+''.join(f'<ellipse cx="{410+90*math.cos(math.radians(a)):.0f}" cy="{380+90*math.sin(math.radians(a)):.0f}" rx="44" ry="16" fill="#fff" transform="rotate({a} {410+90*math.cos(math.radians(a)):.0f} {380+90*math.sin(math.radians(a)):.0f})"/>' for a in range(200,420,30))
for k,(x,y,a) in enumerate([(220,300,20),(160,200,-30),(260,160,60),(560,200,-10),(620,120,40)]): b+=f'<ellipse cx="{x}" cy="{y}" rx="40" ry="14" fill="#fff" transform="rotate({a} {x} {y})"/>'
b+='<path d="M180 260 C120 210 140 140 190 150 C210 155 220 170 220 180 C220 170 230 155 250 150 C300 140 320 210 260 260" stroke="#ff8ab0" stroke-width="4" fill="none" stroke-dasharray="6 8"/>'
I[1560]=svg(b,d)

# 1743 さよならをするために: two coffee cups on a café table by a rain-streaked window, one already pushed away
d,b=bg([(0,'#8a8a9a'),(1,'#5a5a6a')])
b+='<rect x="60" y="60" width="680" height="380" fill="#a8b4c4"/>'+rain(50,1743,'#e8f0ff',.4,5)+'<rect x="60" y="60" width="680" height="380" fill="none" stroke="#3a3030" stroke-width="16"/>'
b+='<rect y="460" width="800" height="340" fill="#6a4a3a"/>'
for x,y in [(300,560),(560,520)]: b+=f'<ellipse cx="{x}" cy="{y+70}" rx="80" ry="14" fill="#f4f0e8"/><path d="M{x-50} {y} L{x+50} {y} L{x+44} {y+64} L{x-44} {y+64}Z" fill="#f4f0e8"/><path d="M{x+50} {y+14} Q{x+76} {y+20} {x+48} {y+46}" stroke="#f4f0e8" stroke-width="10" fill="none"/><ellipse cx="{x}" cy="{y+4}" rx="46" ry="8" fill="#3a2414"/>'
b+='<path d="M300 540 Q310 510 300 480" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>'
I[1743]=svg(b,d)

# 654 有頂天: a figure leaping with joy on top of a cloud as it rises into a dazzling sky full of confetti
d,b=bg([(0,'#ff5a8a'),(1,'#ffd04a')])
b+=rays(400,300,24,'#fff',.3,9)+cloud(400,560,3.0,'#fff',.98)
b+=figure(400,470,260,'#3a0a1a',pose='up')
r=R(654)
for _ in range(40): x,y=r.uniform(0,800),r.uniform(0,500);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="12" height="20" fill="{r.choice(["#fff","#5ab8ff","#3ac85a","#a87aff"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
I[654]=svg(b,d)

# 826 Storm: a lone lighthouse beam fighting a hurricane, enormous waves crashing against the rocks
d,b=bg([(0,'#1a2030'),(1,'#3a4050')])
b+=rain(140,826,'#a8b4c8',.45,7)+bolt([(600,0),(560,140),(600,160),(540,320)],'#e8f0ff',6,1)
b+='<polygon points="350,240 -20,120 -20,360" fill="#fff6d8" opacity=".2"/>'
b+='<path d="M300 620 L320 260 L380 260 L400 620Z" fill="#e8e8f0"/><rect x="310" y="220" width="80" height="40" fill="#ffe8a0"/><path d="M300 220 L350 180 L400 220Z" fill="#2a2a34"/>'+glow(350,240,60,'#fff6d8',.7)
b+='<path d="M-10 800 L-10 640 Q100 520 200 620 Q300 480 460 560 Q560 440 680 560 Q740 520 810 560 L810 800Z" fill="#2a4a6a"/><path d="M200 620 Q240 560 300 580 M460 560 Q500 500 560 520 M680 560 Q700 520 740 530" stroke="#fff" stroke-width="10" fill="none"/>'
I[826]=svg(b,d)

# 896 恋文: a love letter sealed with red wax, tied with a ribbon and tucked among autumn leaves
d,b=bg([(0,'#e8c8a0'),(1,'#c89a6a')])
r=R(896)
for _ in range(20): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="30" ry="16" fill="{r.choice(["#e8601a","#c8401a","#ffb03a"])}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+='<g transform="rotate(-8 400 420)"><rect x="180" y="280" width="440" height="280" fill="#fbf4e4"/><path d="M180 280 L400 440 L620 280" stroke="#e0d4c0" stroke-width="5" fill="none"/><rect x="180" y="410" width="440" height="20" fill="#ff8ab0" opacity=".8"/><circle cx="400" cy="440" r="40" fill="#c80a1a"/>'+heart(400,440,18,'#8a0a10')+'</g>'
I[896]=svg(b,d)

# 1016 LOVEマシーン: a glittering retro machine with a big lever, a heart dropping out of its slot like a prize
d,b=bg([(0,'#ff4ab8'),(1,'#ffb0e0')])
b+=rays(400,400,24,'#fff',.3,8)
b+='<rect x="220" y="160" width="360" height="480" rx="40" fill="#ffd02a"/><rect x="260" y="200" width="280" height="220" rx="20" fill="#d8f0ff"/>'+''.join(heart(300+(k%4)*60,260+(k//4)*60,20,['#ff2a6a','#ff8ab0','#e8102a'][k%3]) for k in range(12))
b+='<rect x="320" y="470" width="160" height="60" rx="10" fill="#3a3a44"/><path d="M580 300 L660 220" stroke="#c8c8d0" stroke-width="14"/><circle cx="670" cy="210" r="26" fill="#e8102a"/>'+heart(400,600,40,'#e8102a')+sparkle(470,560,24,'#fff')
I[1016]=svg(b,d)

# 1227 Dear Snow: a snowman holding a letter at a quiet bus stop, snow falling gently under a single streetlight
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=snow(80,1227)+'<rect y="620" width="800" height="180" fill="#e8eef8"/><rect x="600" y="260" width="10" height="380" fill="#1a1a2a"/>'+glow(605,260,80,'#ffd88a',.6)
b+='<circle cx="380" cy="560" r="100" fill="#fff"/><circle cx="380" cy="410" r="70" fill="#fff"/><circle cx="356" cy="400" r="7" fill="#1a1a1a"/><circle cx="400" cy="400" r="7" fill="#1a1a1a"/><path d="M380 420 L420 428 L380 432Z" fill="#ff8a2a"/><path d="M320 460 Q380 480 440 460" stroke="#e8302a" stroke-width="20" fill="none"/>'
b+='<rect x="440" y="500" width="90" height="64" fill="#fbf4e4" transform="rotate(-10 485 532)"/>'+heart(486,532,14,'#ff5a7a')+'<path d="M450 520 L480 500" stroke="#5a3a1a" stroke-width="6"/>'
I[1227]=svg(b,d)

# 1228 アオゾラペダル: a bicycle pedal spinning in front of a wide clear blue sky, the wheel leaving a trail of clouds
d,b=bg([(0,'#1a90f8'),(1,'#c8ecff')])
b+=''.join(cloud(x,y,s) for x,y,s in [(160,200,.8),(300,260,1.0),(460,320,1.2)])
b+='<circle cx="560" cy="540" r="180" fill="none" stroke="#1a1a24" stroke-width="16"/>'+''.join(f'<path d="M560 540 L{560+170*math.cos(math.radians(a)):.0f} {540+170*math.sin(math.radians(a)):.0f}" stroke="#c8c8d0" stroke-width="3"/>' for a in range(0,360,20))
b+='<circle cx="560" cy="540" r="40" fill="#3a3a44"/><path d="M560 540 L460 620" stroke="#3a3a44" stroke-width="18"/><rect x="400" y="606" width="100" height="30" rx="6" fill="#ffd02a"/>'
I[1228]=svg(b,d)

# 1229 We can make it !: many hands stacked together in the centre of a circle, a sports field under bright lights
d,b=bg([(0,'#1a5a2a'),(1,'#0a3a1a')])
b+=glow(400,400,240,'#fff6d8',.3)
for k,c in enumerate(['#e8c0a0','#d8a888','#c8987a','#f4d0b0','#b8886a']):
    a=math.radians(k*72-90);x=400+260*math.cos(a);y=400+260*math.sin(a)
    b+=f'<path d="M{x:.0f} {y:.0f} L{400+40*math.cos(a):.0f} {400+40*math.sin(a):.0f}" stroke="{c}" stroke-width="70" stroke-linecap="round"/>'
b+='<circle cx="400" cy="400" r="70" fill="#e8c0a0"/>'+sparkle(400,400,40,'#fff')
I[1229]=svg(b,d)

# 1345 ジコチューで行こう!: a girl in a sun hat stretching with open arms on a Mediterranean pier, the sea glittering around her
d,b=bg([(0,'#1aa0f8'),(1,'#c8f0ff')])
b+='<rect y="380" width="800" height="420" fill="#0a88d8"/>'+''.join(f'<rect x="{(k*131)%740}" y="{400+k*24}" width="50" height="4" fill="#fff" opacity=".7"/>' for k in range(14))
b+='<path d="M280 800 L360 520 L440 520 L520 800Z" fill="#c8a070"/>'+''.join(f'<path d="M{360-k*16} {520+k*56} L{440+k*16} {520+k*56}" stroke="#a8804a" stroke-width="4"/>' for k in range(6))
b+=figure(400,560,260,'#2a1a2a',pose='up',hair='#2a1a2a')+'<ellipse cx="400" cy="300" rx="60" ry="14" fill="#fff"/><path d="M370 300 Q380 270 400 268 Q420 270 430 300Z" fill="#fff"/>'
I[1345]=svg(b,d)

# 1396 The Peak: a climber's flag planted on a jagged summit above a sea of clouds under a vast starry sky
d,b=bg([(0,'#04061e'),(.6,'#2a2a6a'),(1,'#8a6aa8')])
b+=starsf(80,1396,500,'#fff')+cloud(160,640,2.4,'#c8b8e8')+cloud(640,660,2.4,'#c8b8e8')
b+='<path d="M120 800 L340 300 L400 240 L460 320 L680 800Z" fill="#1a1a34"/><path d="M340 300 L400 240 L460 320 L420 300 L400 330 L370 300Z" fill="#f4f4ff"/>'
b+='<rect x="398" y="140" width="6" height="110" fill="#e8e8f0"/><path d="M404 146 L470 166 L404 186Z" fill="#ffd02a"/>'
I[1396]=svg(b,d)

# 1435 心臓を捧げよ!: a glowing heart held up in two raised hands before a colossal stone wall at dawn
d,b=bg([(0,'#3a3a5a'),(.6,'#c88a6a'),(1,'#ffc890')])
b+='<rect x="-10" y="200" width="820" height="420" fill="#7a6a5a"/>'+''.join(f'<rect x="{(k%8)*100+(k//8%2)*50-50}" y="{200+(k//8)*50}" width="96" height="46" fill="#8a7a6a"/>' for k in range(64))
b+='<rect y="600" width="800" height="200" fill="#3a2a2a"/>'
b+='<g fill="#d8a888"><rect x="300" y="520" width="60" height="300" rx="26" transform="rotate(10 330 670)"/><rect x="440" y="520" width="60" height="300" rx="26" transform="rotate(-10 470 670)"/></g>'
b+=glow(400,430,140,'#ff3a3a',.6)+heart(400,440,90,'#e8102a')
I[1435]=svg(b,d)

# 1514 花に亡霊: a ghostly translucent figure standing in a field of summer flowers, petals passing straight through her
d,b=bg([(0,'#bfe8ff'),(1,'#fff4e0')])
b+=cloud(600,140,1.4)+'<rect y="480" width="800" height="320" fill="#8ac86a"/>'
r=R(1514)
for _ in range(60): x,y=r.uniform(0,800),r.uniform(500,800);b+=flower(x,y,r.uniform(14,26),5,r.choice(['#fff','#ffd02a','#ff8ab0','#a8c8ff']),'#ffd02a',0,.6)
b+=f'<g opacity=".45">'+figure(400,700,380,'#ffffff',hair='#ffffff')+'</g>'+petals(16,1514,'#ff8ab0',200,700,8,14,.9)
I[1514]=svg(b,d)

# 1561 裸の勇者: a cardboard sword and a paper crown left by a child's bedside, the night light casting a heroic shadow on the wall
d,b=bg([(0,'#1a1a3a'),(1,'#2a2a4a')])
b+='<g fill="#000" opacity=".4"><path d="M500 80 L530 120 L530 420 L470 420 L470 120Z"/><rect x="410" y="420" width="180" height="30" rx="8"/><rect x="482" y="450" width="36" height="110"/></g><path d="M440 60 L470 20 L500 50 L530 10 L560 50 L590 20 L620 60Z" fill="#000" opacity=".35"/>'
b+=glow(160,600,120,'#ffd88a',.6)+'<rect x="130" y="560" width="60" height="80" rx="12" fill="#ffe8a0"/>'
b+='<rect y="640" width="800" height="160" fill="#3a3a5a"/><g transform="rotate(-30 440 620)"><rect x="300" y="600" width="260" height="30" fill="#c8a070"/><rect x="280" y="590" width="30" height="50" fill="#a87a4a"/><rect x="250" y="604" width="40" height="22" fill="#a87a4a"/></g>'
b+='<path d="M560 700 L580 640 L610 680 L640 620 L670 680 L700 640 L720 700Z" fill="#ffd02a"/>'
I[1561]=svg(b,d)

# 183 心の色: a painter's palette with a heart-shaped thumb hole, every colour swirled together in the middle
d,b=bg([(0,'#f4ece0'),(1,'#e0d4c4')])
b+='<path d="M400 160 Q620 160 660 360 Q680 520 560 600 Q500 640 460 600 Q430 560 380 600 Q260 680 180 560 Q120 440 180 300 Q240 160 400 160Z" fill="#c89a60"/>'+heart(300,470,34,'#f4ece0')
for k,(x,y,c) in enumerate([(300,280,'#e8302a'),(420,240,'#ffd02a'),(540,300,'#3ac85a'),(580,430,'#2a8ae8'),(480,520,'#a87aff')]): b+=f'<circle cx="{x}" cy="{y}" r="40" fill="{c}"/>'
b+='<path d="M380 380 Q420 340 460 380 Q480 420 440 440 Q400 450 380 420Z" fill="#ff8ab0"/><path d="M600 120 L460 380" stroke="#8a5a2a" stroke-width="12"/><path d="M450 390 L470 360 L480 400Z" fill="#3a3a44"/>'
I[183]=svg(b,d)

# 221 チャンピオン: a boxing glove raised in victory in a spotlit ring, the other glove hanging from the ropes
d,b=bg([(0,'#1a1a24'),(1,'#2a1a1a')])
b+='<polygon points="400,-20 180,800 620,800" fill="#fff6d8" opacity=".12"/>'+''.join(f'<path d="M-10 {540+k*50} L810 {500+k*50}" stroke="{["#e8102a","#fff","#2a5ae8"][k]}" stroke-width="10"/>' for k in range(3))
b+=rays(400,280,16,'#ffd02a',.15,8)+glow(400,300,160,'#fff6d8',.35)+'<rect y="700" width="800" height="100" fill="#3a3a44"/>'
b+='<g transform="rotate(-10 400 320)"><rect x="340" y="420" width="130" height="300" fill="#c8987a"/><rect x="330" y="390" width="150" height="70" rx="10" fill="#f4f4f4"/><path d="M320 300 Q310 160 410 160 Q510 160 500 290 Q495 390 440 400 L370 400 Q320 390 320 300Z" fill="#e8102a"/><path d="M330 330 Q280 320 285 270 Q292 230 340 250 Q350 290 330 330Z" fill="#c80a1a"/><path d="M360 200 Q410 180 460 200" stroke="#ff6a6a" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M380 410 L430 410" stroke="#e8102a" stroke-width="6"/></g>'
I[221]=svg(b,d)

# 395 SOLITUDE: a single chair in the middle of a vast empty white room, a long shadow cast by a high window
d,b=bg([(0,'#e8e4dc'),(1,'#c8c4bc')])
b+='<rect x="520" y="80" width="140" height="200" fill="#fff"/><polygon points="520,280 660,280 400,740 120,740" fill="#fff" opacity=".4"/><rect y="600" width="800" height="200" fill="#b8b4ac"/>'
b+='<rect x="360" y="380" width="14" height="260" fill="#3a2a1a"/><rect x="450" y="460" width="14" height="180" fill="#3a2a1a"/><rect x="360" y="490" width="104" height="18" fill="#5a3a1a"/><rect x="360" y="380" width="14" height="110" fill="#5a3a1a"/>'
b+='<path d="M374 640 L280 760 L340 760 L464 640Z" fill="#000" opacity=".15"/>'
I[395]=svg(b,d)

# 578 淋しい熱帯魚: a single bright tropical fish swimming alone in a big round fishbowl on a dark windowsill
d,b=bg([(0,'#0a1a3a'),(1,'#1a2a4a')])
b+='<circle cx="400" cy="440" r="220" fill="#5ab0e8" opacity=".35" stroke="#bfe8ff" stroke-width="6"/><path d="M200 380 Q400 360 600 380" stroke="#bfe8ff" stroke-width="4" fill="none"/>'
b+='<g transform="translate(400 460)"><path d="M-80 0 Q-20 -60 60 0 Q-20 60 -80 0Z" fill="#ffa82a"/><path d="M-20 -40 L-30 -40 L-40 40 L-20 40" fill="#fff"/><path d="M60 0 L110 -40 L100 0 L110 40Z" fill="#ff5a2a"/><circle cx="-50" cy="-8" r="8" fill="#1a1a1a"/></g>'
b+=''.join(ring(320-k*10,400-k*40,6+k*2,'#fff',2,.7) for k in range(4))+'<rect y="660" width="800" height="140" fill="#3a2a2a"/>'
I[578]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
