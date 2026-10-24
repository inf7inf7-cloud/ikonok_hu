import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 7. csoport, 2026-10-24
I={}
def phone(x,y,s,col='#1a1a1a'):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-120 -20 Q-130 -60 -90 -60 L90 -60 Q130 -60 120 -20 L80 -20 L70 -40 L-70 -40 L-80 -20Z" fill="{col}"/><path d="M-100 0 L100 0 L120 100 L-120 100Z" fill="{col}"/><circle cx="0" cy="50" r="34" fill="#f4f0e8"/>'+''.join(f'<circle cx="{24*math.cos(math.radians(a)):.0f}" cy="{50+24*math.sin(math.radians(a)):.0f}" r="5" fill="{col}"/>' for a in range(0,360,36))+'</g>'

# 523 LOVE LOVE LOVE: three glowing hearts stacked one above another like a neon sign repeating its single word
d,b=bg([(0,'#1a0a2a'),(1,'#3a0a3a')])
for k,(y,s,c) in enumerate([(230,70,'#ff5a9a'),(400,95,'#ff2a6a'),(600,120,'#e8102a')]): b+=glow(400,y,s*1.4,c,.45)+heart(400,y,s,c)
b+=rain(40,523,'#ffc8e0',.3,4)
I[523]=svg(b,d)

# 635 love me, I love you: two silhouettes holding hands on a hill under a huge heart-shaped pink sun
d,b=bg([(0,'#ff6a9a'),(1,'#ffc08a')])
b+=glow(400,330,220,'#fff2d8',.6)+heart(400,330,170,'#fff2e0')
b+='<path d="M-10 800 L-10 640 Q400 560 810 640 L810 800Z" fill="#3a1a2a"/>'
b+=figure(340,610,180,'#2a1020')+figure(460,610,170,'#2a1020',hair='#2a1020')+'<path d="M360 520 Q400 540 440 520" stroke="#2a1020" stroke-width="12" fill="none"/>'
I[635]=svg(b,d)

# 1097 *~アスタリスク~: a giant glowing asterisk star burning white and orange in a dark sky, sparks shooting off
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a1a')])
b+=glow(400,400,240,'#ff8a1a',.4)
for a in (0,60,120): b+=f'<rect x="370" y="140" width="60" height="520" rx="30" fill="#ff8a1a" transform="rotate({a} 400 400)"/><rect x="386" y="160" width="28" height="480" rx="14" fill="#fff6d8" transform="rotate({a} 400 400)"/>'
r=R(1097)
for _ in range(20): x,y=r.uniform(60,740),r.uniform(60,740);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#ffd27a"/>'
I[1097]=svg(b,d)

# 1203 Believe: a small flag planted on a mountain summit just as the sun breaks over the ridge
d,b=bg([(0,'#3a4a9a'),(.6,'#ff9a7a'),(1,'#ffd8a0')])
b+=rays(560,460,18,'#fff6d8',.25,6)+glow(560,460,140,'#fff2c8',.7)
b+='<path d="M-10 800 L-10 560 L220 360 L400 260 L520 380 L620 330 L810 520 L810 800Z" fill="#2a2a4a"/><path d="M400 260 L440 320 L380 320Z" fill="#f4f4ff"/>'
b+='<rect x="396" y="140" width="8" height="130" fill="#e8e8f0"/><path d="M404 146 Q460 160 500 150 Q470 180 500 210 Q460 214 404 200Z" fill="#e8302a"/>'
I[1203]=svg(b,d)

# 1298 ヘビーローテーション: pillows mid-fight bursting with feathers, a pink heart spinning in the middle
d,b=bg([(0,'#ffd0ec'),(1,'#ff9ad0')])
b+=rays(400,400,16,'#ffffff',.3,9)
for x,y,a,c in [(220,300,-20,'#fff'),(580,330,24,'#ffe8f4')]: b+=f'<rect x="{x-130}" y="{y-80}" width="260" height="160" rx="70" fill="{c}" transform="rotate({a} {x} {y})"/>'
r=R(1298)
for _ in range(24):
    x,y,a=r.uniform(60,740),r.uniform(80,760),r.uniform(0,180)
    b+=f'<path d="M{x:.0f} {y:.0f} q12 -20 30 -24 q-6 20 -30 24Z" fill="#fff" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>'
b+=heart(400,520,90,'#ff2a8a')+'<path d="M300 620 Q400 680 500 620" stroke="#fff" stroke-width="6" fill="none" opacity=".7"/>'
I[1298]=svg(b,d)

# 1416 高嶺の花子さん: a single flower blooming on a high cliff top, far out of reach of the small figure looking up from below
d,b=bg([(0,'#5ab0f8'),(1,'#d8f0ff')])
b+=cloud(200,200,1.0)
b+='<path d="M380 800 L420 240 Q520 200 620 240 L700 800Z" fill="#8a7a6a"/><path d="M420 240 Q520 200 620 240 L610 270 Q520 236 430 270Z" fill="#6ab84a"/>'
b+='<path d="M520 230 L520 160" stroke="#3a8a2a" stroke-width="6"/>'+flower(520,140,80,6,'#ff7aa8','#ffd82a',0,.7)+glow(520,140,60,'#fff',.35)
b+='<rect y="740" width="800" height="60" fill="#6ab84a"/>'+figure(220,760,130,'#1a2a3a',pose='reach')
I[1416]=svg(b,d)

# 1444 明け星: the morning star shining over a calm sea as the first light of dawn spreads along the horizon
d,b=bg([(0,'#0a1440'),(.55,'#5a4a8a'),(1,'#ffb07a')])
b+=starsf(40,1444,320,'#e8f0ff')+glow(400,260,80,'#ffffff',.6)+sparkle(400,260,70,'#fff')+sparkle(400,260,30,'#bfe8ff')
b+='<rect y="560" width="800" height="240" fill="#1a2a5a"/>'+glow(400,570,90,'#ffd8a0',.5)+''.join(f'<rect x="{380-k*16}" y="{580+k*26}" width="{40+k*32}" height="4" fill="#ffd8a0" opacity="{.6-k*.08:.2f}"/>' for k in range(7))
I[1444]=svg(b,d)

# 1473 JANE DOE: a nameless woman's silhouette under a dark umbrella in the rain, a red flower dropped at her feet
d,b=bg([(0,'#0a0a10'),(1,'#1a1a24')])
b+=glow(400,300,300,'#3a3a5a',.6)+rain(120,1473,'#a8a8c8',.55,6)+skyline(560,'#181824',1473,80,320,'#c8c8e8',40)
b+='<rect y="680" width="800" height="120" fill="#0a0a10"/>'+figure(400,700,330,'#020204',hair='#020204')+wagasa(400,380,170,'#3a3a4a',0,'#5a5a6a')
b+=flower(470,700,40,6,'#e8102a','#3a0a0a',20,.7)
I[1473]=svg(b,d)

# 308 しゃぼん玉: soap bubbles drifting upward, their surfaces swirling with rainbow colours against a soft blue sky
d,b=bg([(0,'#7ac0f0'),(1,'#d8f0ff')])
d+=rg('sb2',S((0,'#ffffff',0),(.7,'#bfe8ff',.2),(.84,'#ff9ad8',.7),(.92,'#ffe05a',.8),(1,'#5ae8ff',.95)),.5,.5,.5)
for x,y,r_ in [(380,420,180),(600,220,90),(170,200,70),(620,560,60),(200,620,50)]:
    b+=f'<circle cx="{x}" cy="{y}" r="{r_}" fill="url(#sb2)"/><ellipse cx="{x-r_*.4}" cy="{y-r_*.45}" rx="{r_*.2}" ry="{r_*.1}" fill="#fff" opacity=".8" transform="rotate(-35 {x-r_*.4} {y-r_*.45})"/>'
I[308]=svg(b,d)

# 421 聖母たちのララバイ: a mother cradling a sleeping baby in moonlight by a window, lullaby notes floating
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a5a')])
b+=moon(600,200,60,'#fff6d8')+'<rect x="440" y="80" width="300" height="300" fill="none" stroke="#2a1a3a" stroke-width="20"/>'
b+='<g fill="#0a0814"><circle cx="320" cy="360" r="50"/><path d="M220 800 Q200 520 300 430 Q360 410 400 450 Q470 520 460 800Z"/></g>'
b+='<ellipse cx="380" cy="540" rx="90" ry="50" fill="#f4e8f0"/><circle cx="440" cy="520" r="32" fill="#f4e0d8"/>'
b+=note(560,460,26,'#fff6d8')+note(620,540,22,'#fff6d8',True)+note(520,560,18,'#fff6d8')
I[421]=svg(b,d)

# 993 evolution: a glowing double helix twisting upward out of darkness, every rung a different colour
d,b=bg([(0,'#04081a'),(1,'#0a1a3a')])
b+=glow(400,400,220,'#5ae0ff',.3)
for k in range(22):
    y=60+k*32;a=k*.55;x1=400+150*math.sin(a);x2=400-150*math.sin(a)
    b+=f'<path d="M{x1:.0f} {y} L{x2:.0f} {y}" stroke="{["#ff5ab8","#5ae8ff","#ffe05a","#8aff8a"][k%4]}" stroke-width="8" opacity=".8"/><circle cx="{x1:.0f}" cy="{y}" r="14" fill="#e8f8ff"/><circle cx="{x2:.0f}" cy="{y}" r="14" fill="#8ad0ff"/>'
I[993]=svg(b,d)

# 1098 ミチシルベ~a road home~: an old wooden signpost at a crossroads at dusk, arrows pointing every way home
d,b=bg([(0,'#3a3a7a'),(.6,'#ff9a6a'),(1,'#ffd0a0')])
b+=hinomaru_sun(400,560,100,'#fff2c8',.8)+'<path d="M-10 600 Q400 570 810 600 L810 810 L-10 810Z" fill="#5a6a3a"/><path d="M300 810 L390 600 L410 600 L500 810Z M-10 700 L400 620 L810 690" stroke="#c8a878" stroke-width="20" fill="#c8a878"/>'
b+='<rect x="390" y="260" width="22" height="420" fill="#5a3a1a"/>'
for y,a,t in [(300,-10,1),(380,8,-1),(460,-4,1)]: b+=f'<g transform="rotate({a} 400 {y})"><path d="M{400 if t>0 else 220} {y-24} L{560 if t>0 else 400} {y-24} L{600 if t>0 else 400} {y} L{560 if t>0 else 400} {y+24} L{400 if t>0 else 220} {y+24} {"" if t>0 else "L180 "+str(y)}Z" fill="#a8703a"/></g>'
I[1098]=svg(b,d)

# 1504 SPECIALZ: a flickering neon Z blazing red over a rain-slicked night city, glitch lines tearing across it
d,b=bg([(0,'#0a0410'),(1,'#1a0a1a')])
b+=skyline(700,'#140a1a',1504,100,420,'#ff3a5a',80)+neon(400,500,'Z','#ff2a4a',420,'DejaVu Sans,sans-serif')
for y in (300,420,560): b+=f'<rect x="{150+(y%7)*20}" y="{y}" width="{300+(y%5)*40}" height="10" fill="#5ae8ff" opacity=".6"/>'
I[1504]=svg(b,d)

# 1840 ドラマツルギー: a comedy mask and a tragedy mask hanging under a stage spotlight before red curtains
d,b=bg([(0,'#3a0408'),(1,'#1a0204')])
for k in range(10): b+=f'<path d="M{k*84} 0 Q{k*84+42} 300 {k*84} 800" stroke="#5a0a14" stroke-width="30" fill="none" opacity=".6"/>'
b+='<polygon points="400,-20 180,800 620,800" fill="#ffe8c8" opacity=".1"/>'
for x,a,c,smile in [(310,-14,'#f4f0e8',True),(490,14,'#d8d8e8',False)]:
    b+=f'<g transform="rotate({a} {x} 420)"><path d="M{x-90} 330 Q{x} 290 {x+90} 330 Q{x+100} 460 {x} 530 Q{x-100} 460 {x-90} 330Z" fill="{c}"/><path d="M{x-50} 390 q20 {-20 if smile else 20} 40 0 M{x+10} 390 q20 {-20 if smile else 20} 40 0" stroke="#1a0a0a" stroke-width="10" fill="none"/>'
    b+=f'<path d="M{x-40} 460 Q{x} {500 if smile else 430} {x+40} 460" stroke="#1a0a0a" stroke-width="10" fill="none"/></g>'
I[1840]=svg(b,d)

# 249 Hello, My Friend: a little red convertible parked on a seaside road on a summer afternoon, a hand waving from it
d,b=bg([(0,'#3ab0f0'),(1,'#c8ecff')])
b+=cloud(600,150,1.0)+'<rect y="400" width="800" height="200" fill="#1a90d0"/><rect y="600" width="800" height="200" fill="#8a8a94"/>'
b+='<path d="M180 560 Q200 500 300 490 L420 460 Q480 450 520 490 L620 500 Q660 510 660 560 L660 600 L180 600Z" fill="#e8302a"/><path d="M420 470 L470 420 L480 470" stroke="#bfe8ff" stroke-width="8" fill="none"/>'
for x in (260,580): b+=f'<circle cx="{x}" cy="600" r="44" fill="#1a1a24"/><circle cx="{x}" cy="600" r="16" fill="#c8c8d0"/>'
b+=figure(360,520,120,'#1a1a2a',pose='wave',hair='#1a1a2a')
I[249]=svg(b,d)

# 283 東京VICTORY: fireworks bursting over the Tokyo skyline, a giant V of light rising over the Sky Tree
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=firework(200,200,110,'#ffd27a',24,1)+firework(600,190,120,'#ff5ab8',24,2)
b+='<path d="M260 120 L400 440 L540 120" stroke="#ffe05a" stroke-width="30" fill="none" stroke-linejoin="round" opacity=".85"/>'
b+=skyline(640,'#0a0a1e',283,80,240,'#ffd27a',80)+'<path d="M392 640 L398 300 L402 300 L408 640Z" fill="#c8d8f0"/><rect x="386" y="420" width="28" height="14" fill="#c8d8f0"/><rect x="388" y="360" width="24" height="10" fill="#c8d8f0"/>'
I[283]=svg(b,d)

# 355 Sweet Memories: a little penguin gazing into a glass of amber whisky on a bar counter, lost in a memory
d,b=bg([(0,'#1a2a3a'),(1,'#2a3a4a')])
b+=glow(400,420,220,'#ffc870',.3)+'<rect y="560" width="800" height="240" fill="#3a2414"/>'
b+='<g transform="translate(300 450)"><ellipse cx="0" cy="40" rx="80" ry="110" fill="#1a1a24"/><ellipse cx="0" cy="60" rx="54" ry="80" fill="#fbfbf6"/><circle cx="0" cy="-70" r="56" fill="#1a1a24"/><circle cx="18" cy="-80" r="10" fill="#fff"/><path d="M40 -66 L80 -56 L40 -46Z" fill="#ffa81a"/><path d="M-70 40 Q-110 80 -80 120" stroke="#1a1a24" stroke-width="24" fill="none" stroke-linecap="round"/><path d="M-30 150 L-50 166 L-10 166Z M30 150 L10 166 L50 166Z" fill="#ffa81a"/></g>'
b+='<path d="M480 420 L600 420 L590 560 L490 560Z" fill="#f4e8d8" opacity=".35"/><path d="M486 470 L594 470 L590 556 L490 556Z" fill="#d88a2a"/><rect x="510" y="480" width="40" height="40" rx="6" fill="#fff" opacity=".6"/>'
I[355]=svg(b,d)

# 403 セーラー服と機関銃: a sailor-uniform collar with a red scarf fluttering in the wind, a scatter of brass shells at its feet
d,b=bg([(0,'#c8d8f0'),(1,'#8aa0c8')])
b+='<path d="M220 160 L400 330 L580 160 L640 220 L660 520 L140 520 L160 220Z" fill="#1a2a5a"/><path d="M240 180 L400 330 L560 180" stroke="#fff" stroke-width="10" fill="none"/><path d="M400 330 L300 200 L500 200Z" fill="#fbfbf6"/>'
b+='<path d="M360 340 L440 340 L400 380Z" fill="#e8102a"/><path d="M380 370 Q340 460 300 500 Q340 470 400 380 Q460 470 540 520 Q450 440 420 370Z" fill="#e8102a"/>'
b+='<rect x="140" y="510" width="520" height="290" fill="#1a2a5a"/>'+''.join(f'<rect x="{x}" y="{y}" width="16" height="40" rx="6" fill="#d8b040" transform="rotate({a} {x} {y})"/>' for x,y,a in [(220,680,30),(300,720,-20),(560,700,60),(480,740,10)])
I[403]=svg(b,d)

# 486 KISS ME: a pair of glowing red lips in neon light on a black wall, a single rose beneath them
d,b=bg([(0,'#0a0006'),(1,'#1a0410')])
b+=glow(400,340,200,'#ff2a4a',.45)
b+='<g transform="translate(400 340) scale(2.2)"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="#e8102a"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="#c80a20"/></g>'
b+='<path d="M200 700 Q300 640 400 620" stroke="#2a5a2a" stroke-width="8" fill="none"/>'+rose(410,616,.6,60)
I[486]=svg(b,d)

# 636 Calling: an old black telephone ringing on a table, its receiver trembling and sound rings spreading out
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
for k in range(4): b+=f'<path d="M{200-k*40} {300-k*30} Q{120-k*40} 420 {200-k*40} {540+k*30}" stroke="#ffd27a" stroke-width="8" fill="none" opacity="{.7-k*.15:.2f}"/><path d="M{600+k*40} {300-k*30} Q{680+k*40} 420 {600+k*40} {540+k*30}" stroke="#ffd27a" stroke-width="8" fill="none" opacity="{.7-k*.15:.2f}"/>'
b+='<rect y="600" width="800" height="200" fill="#5a3a2a"/>'+phone(400,480,1.8)
I[636]=svg(b,d)

# 685 クリスマスキャロルの頃には: a Christmas wreath on a front door in the falling snow, a lamp glowing beside it
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=snow(90,685)+'<rect x="230" y="160" width="340" height="560" fill="#7a2a1a"/><rect x="250" y="180" width="300" height="520" fill="#8a3a24"/>'
b+='<circle cx="400" cy="380" r="110" fill="none" stroke="#1a6a3a" stroke-width="54"/>'+''.join(f'<circle cx="{400+110*math.cos(math.radians(a)):.0f}" cy="{380+110*math.sin(math.radians(a)):.0f}" r="10" fill="#e8102a"/>' for a in range(0,360,40))
b+='<path d="M360 480 L400 460 L440 480 L420 540 L400 500 L380 540Z" fill="#e8102a"/><circle cx="510" cy="460" r="12" fill="#d8b040"/>'
b+='<rect x="620" y="300" width="60" height="80" rx="8" fill="#2a2a34"/><rect x="630" y="310" width="40" height="60" fill="#ffd27a"/>'+glow(650,340,60,'#ffd27a',.5)+'<rect y="720" width="800" height="80" fill="#e8eef8"/>'
I[685]=svg(b,d)

# 686 PIECE OF MY WISH: a glass jar holding a single glowing wishing star, held up to a twilight sky
d,b=bg([(0,'#2a2a6a'),(.6,'#8a5a9a'),(1,'#ffb08a')])
b+=starsf(40,686,400,'#fff')
b+='<path d="M290 260 L510 260 L520 300 Q560 340 560 420 L560 620 Q560 680 500 680 L300 680 Q240 680 240 620 L240 420 Q240 340 280 300Z" fill="#d8ecff" opacity=".35" stroke="#fff" stroke-width="6"/><rect x="280" y="230" width="240" height="40" rx="8" fill="#c8a060"/>'
b+=glow(400,480,90,'#ffe05a',.8)+star5(400,480,70,'#ffe86a')
I[686]=svg(b,d)

# 776 虹: a rainbow arching over a swimming pool after a summer shower, splashes leaping from the water
d,b=bg([(0,'#4ab0f0'),(1,'#d8f2ff')])
for k,c in enumerate(['#ff4a4a','#ffa82a','#ffe02a','#4ac84a','#2a8aff','#8a4aff']): b+=f'<path d="M{80+k*20} 560 A{320-k*20} {320-k*20} 0 0 1 {720-k*20} 560" stroke="{c}" stroke-width="20" fill="none"/>'
b+='<rect y="560" width="800" height="240" fill="#2ab0e8"/>'+''.join(f'<rect x="{x}" y="560" width="6" height="240" fill="#fff" opacity=".5"/>' for x in (200,400,600))
for x in (300,500): b+=f'<path d="M{x} 580 Q{x-30} 500 {x-60} 520 M{x} 580 Q{x+30} 500 {x+60} 520 M{x} 580 L{x} 490" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round"/>'
I[776]=svg(b,d)

# 777 桜坂: a gently sloping street lined with cherry trees in full bloom, petals carpeting the pavement
d,b=bg([(0,'#d8e8ff'),(1,'#fff0f4')])
b+='<path d="M-10 800 L-10 540 L810 380 L810 800Z" fill="#c8b8b8"/><path d="M-10 800 L-10 700 L810 470 L810 800Z" fill="#e8c8d0"/>'
for k,(x,y) in enumerate([(80,520),(260,480),(440,440),(620,400)]):
    s=1.2-k*.15;b+=f'<rect x="{x-8}" y="{y}" width="16" height="{200*s:.0f}" fill="#4a2a1a"/>'
    r=R(k*7)
    for _ in range(18): b+=f'<circle cx="{x+r.uniform(-100,100)*s:.0f}" cy="{y+r.uniform(-140,10)*s:.0f}" r="{r.uniform(30,50)*s:.0f}" fill="{r.choice(["#ffc0d4","#ffd8e4","#ffb0c8"])}"/>'
b+=petals(50,777,'#ff9ab8',300,800,6,12,.9)
I[777]=svg(b,d)

# 1364 サイレントマジョリティー: rows of identical grey figures in step, one figure in red turning to face the other way
d,b=bg([(0,'#5a5a64'),(1,'#2a2a34')])
for row,(y,h) in enumerate([(420,120),(560,160),(740,210)]):
    n=[9,7,5][row]
    for k in range(n): x=60+k*(680/(n-1));b+=figure(x,y,h,'#141418' if not (row==2 and k==2) else '#d81a2a',pose='stand')
I[1364]=svg(b,d)

# 337 CAT'S EYE: two glowing cat's eyes staring out of the darkness, a calling card pinned beneath them
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
for x in (270,530):
    b+=glow(x,330,110,'#a8ff4a',.35)+f'<ellipse cx="{x}" cy="330" rx="110" ry="70" fill="#d8ff5a"/><ellipse cx="{x}" cy="330" rx="22" ry="66" fill="#0a0a0a"/><circle cx="{x-30}" cy="306" r="10" fill="#fff"/>'
b+='<g transform="rotate(-8 400 600)"><rect x="300" y="540" width="200" height="120" rx="8" fill="#fbf8f0"/><path d="M340 600 Q400 560 460 600 Q400 640 340 600Z" fill="#1a1a24"/><ellipse cx="400" cy="600" rx="10" ry="18" fill="#a8ff4a"/></g>'
I[337]=svg(b,d)

# 1162 ありがとう: a handwritten thank-you letter beside a small vase of flowers in the warm morning sun
d,b=bg([(0,'#fff6e0'),(1,'#ffe0c0')])
b+='<polygon points="0,0 360,0 800,560 800,800 520,800" fill="#fffbe8" opacity=".5"/>'
b+='<g transform="rotate(-8 330 480)"><rect x="160" y="300" width="340" height="400" rx="8" fill="#fff"/>'+''.join(f'<path d="M190 {380+k*50} Q330 {370+k*50} 460 {380+k*50}" stroke="#7a6a8a" stroke-width="5" fill="none"/>' for k in range(6))+heart(420,650,22,'#ff5a7a')+'</g>'
b+='<path d="M560 520 L640 520 L630 700 L570 700Z" fill="#bfe0f0" opacity=".85"/>'+''.join(flower(x,y,46,5,c,'#ffd82a',x%30,.7)+f'<path d="M{x} {y+20} L600 520" stroke="#4a8a3a" stroke-width="4"/>' for x,y,c in [(560,380,'#ffb0c8'),(640,400,'#ffe05a'),(600,330,'#ff8a8a')])
I[1162]=svg(b,d)

# 1522 祝福: a small blue planet in space wrapped in a ring of blooming flowers, a blessing in the void
d,b=bg([(0,'#04061a'),(1,'#100a2a')])
b+=starsf(90,1522,800,'#e8f0ff')+glow(400,400,220,'#5ab0ff',.35)
b+='<circle cx="400" cy="400" r="150" fill="#2a6ae8"/><path d="M290 340 Q340 300 380 340 Q360 400 300 390Z M420 430 Q480 400 520 450 Q480 500 430 480Z" fill="#3ac87a"/>'
for k in range(14):
    a=math.radians(k*360/14);x=400+230*math.cos(a);y=400+90*math.sin(a)
    b+=flower(x,y,48,5,['#ff7ab8','#ffffff','#ffd82a'][k%3],'#ff4a6a',k*20,.7)
I[1522]=svg(b,d)

# 284 あなただけを ~Summer Heartbreak~: sunglasses lying in the sand beside a cracked red heart on a blazing summer beach
d,b=bg([(0,'#2ab8f0'),(1,'#a8ecff')])
b+=glow(640,140,100,'#fff6c8',.8)+'<rect y="380" width="800" height="120" fill="#1a98d8"/><path d="M-10 480 Q400 450 810 480 L810 810 L-10 810Z" fill="#f4dca0"/>'
b+=heart(300,600,110,'#e8102a')+bolt([(300,500),(280,560),(320,610),(296,680)],'#fff6e0',8,1)
b+='<g transform="rotate(-10 560 640)"><ellipse cx="510" cy="640" rx="56" ry="40" fill="#1a1a24"/><ellipse cx="630" cy="640" rx="56" ry="40" fill="#1a1a24"/><path d="M566 630 Q570 620 574 630" stroke="#1a1a24" stroke-width="10" fill="none"/><ellipse cx="496" cy="626" rx="16" ry="8" fill="#5ab0ff" opacity=".7"/></g>'
I[284]=svg(b,d)

# 857 DAYBREAK'S BELL: a great bronze bell ringing at daybreak on a hilltop, sound waves rolling over the waking land
d,b=bg([(0,'#2a2a6a'),(.6,'#e88a6a'),(1,'#ffd8a0')])
b+=glow(400,600,240,'#fff2c8',.6)
for k in range(4): b+=f'<path d="M{200-k*40} {460} Q400 {220-k*50} {600+k*40} 460" stroke="#fff6d8" stroke-width="6" fill="none" opacity="{.6-k*.12:.2f}"/>'
b+='<rect x="200" y="200" width="400" height="24" fill="#3a2a1a"/><rect x="220" y="200" width="20" height="440" fill="#3a2a1a"/><rect x="560" y="200" width="20" height="440" fill="#3a2a1a"/>'
d+=lg('bl',S((0,'#e8b060'),(1,'#8a5a2a')),0,0,1,0)
b+='<path d="M310 520 Q300 320 400 260 Q500 320 490 520 L520 560 L280 560Z" fill="url(#bl)"/><circle cx="400" cy="580" r="24" fill="#6a4a2a"/><rect x="390" y="224" width="20" height="40" fill="#3a2a1a"/>'
b+='<path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#3a3a5a"/>'
I[857]=svg(b,d)

# 966 長い間: a stack of old love letters tied with ribbon beside a candle that has burned almost down
d,b=bg([(0,'#2a1a14'),(1,'#4a2a1a')])
b+=glow(560,380,180,'#ffc870',.45)+'<rect y="600" width="800" height="200" fill="#5a3420"/>'
for k in range(5): b+=f'<rect x="{180+k*6}" y="{560-k*34}" width="280" height="40" rx="4" fill="{["#f4ecd8","#fff4e8","#ece0c8"][k%3]}" transform="rotate({(k%2)*4-2} 320 {580-k*34})"/>'
b+='<path d="M320 400 L320 610 M190 500 L450 500" stroke="#e8302a" stroke-width="10"/>'
b+='<rect x="540" y="540" width="44" height="70" rx="6" fill="#fff6e8"/><path d="M562 500 Q578 524 562 542 Q546 524 562 500Z" fill="#ffd060"/><path d="M540 600 Q520 610 530 630 L600 630 Q610 610 584 600Z" fill="#fff6e8"/>'
I[966]=svg(b,d)

# 1204 WISH: a stone wishing well in a moonlit garden, a coin spinning in the air above it
d,b=bg([(0,'#0a1430'),(1,'#2a3a5a')])
b+=starsf(60,1204,400,'#fff')+moon(600,150,40)
b+='<ellipse cx="400" cy="480" rx="180" ry="50" fill="#5a5a6a"/><path d="M220 480 L220 640 Q400 690 580 640 L580 480 Q400 530 220 480Z" fill="#6a6a7a"/>'+''.join(f'<rect x="{230+k*60}" y="{500+((k%2)*40)}" width="54" height="34" fill="#7a7a8a"/>' for k in range(6))
b+='<ellipse cx="400" cy="480" rx="150" ry="36" fill="#0a1020"/><path d="M240 480 L240 260 M560 480 L560 260 M220 260 L400 200 L580 260" stroke="#5a3a2a" stroke-width="16" fill="none"/>'
b+=glow(400,360,40,'#ffd27a',.8,'glow2')+'<ellipse cx="400" cy="360" rx="16" ry="24" fill="#ffd27a"/>'
I[1204]=svg(b,d)

# 1418 ハッピーエンド: a cinema screen glowing with the word END, a lone seat and a crumpled tissue in the dark theatre
d,b=bg([(0,'#0a0a14'),(1,'#1a1a24')])
b+='<polygon points="400,800 160,140 640,140" fill="#ffffff" opacity=".05"/><rect x="120" y="120" width="560" height="320" fill="#f4f0e8"/>'
b+='<text x="400" y="320" text-anchor="middle" font-family="DejaVu Serif,serif" font-style="italic" font-size="120" fill="#2a2a34">END</text>'
for x in range(40,800,110): b+=f'<path d="M{x} 800 L{x} 620 Q{x+45} 590 {x+90} 620 L{x+90} 800Z" fill="#5a0a14"/>'
b+='<path d="M490 600 Q470 560 500 540 Q530 550 520 590 Q540 610 510 620Z" fill="#fff"/>'
I[1418]=svg(b,d)

# 1555 怪獣の花唄: a small friendly kaiju singing with a flower in its claw, musical notes rising into a pastel sky
d,b=bg([(0,'#ffd0e0'),(1,'#c8e8ff')])
b+='<path d="M220 760 Q200 520 300 440 Q360 380 440 400 Q500 300 580 330 Q640 360 620 430 Q600 470 560 470 Q600 560 560 760Z" fill="#5ab86a"/>'
b+='<path d="M300 440 L280 400 L320 420 L320 370 L350 400 L370 350 L390 390" fill="#3a9a4a"/><circle cx="570" cy="390" r="14" fill="#1a2a1a"/><path d="M580 430 Q610 450 620 430" stroke="#1a2a1a" stroke-width="6" fill="none"/>'
b+='<path d="M500 520 Q560 520 600 480" stroke="#5ab86a" stroke-width="40" fill="none" stroke-linecap="round"/><path d="M610 470 L640 380" stroke="#3a8a2a" stroke-width="6"/>'+flower(642,360,60,6,'#ff7aa8','#ffd82a',10,.7)
b+=note(680,250,30,'#3a3a5a',True)+note(520,200,26,'#3a3a5a')+note(640,140,20,'#3a3a5a')
I[1555]=svg(b,d)

# 676 悲しみは雪のように: snow drifting down through the cone of a single streetlamp on an empty winter road
d,b=bg([(0,'#0a1020'),(1,'#1a2030')])
b+='<polygon points="400,180 200,760 600,760" fill="#ffe8b0" opacity=".14"/>'+snow(120,676)
b+='<rect x="394" y="180" width="12" height="600" fill="#06080e"/><path d="M370 184 L430 184 L420 160 L380 160Z" fill="#06080e"/>'+glow(400,196,70,'#ffd88a',.6)
b+='<rect y="740" width="800" height="60" fill="#d8e0ec"/><ellipse cx="400" cy="752" rx="200" ry="14" fill="#ffe8b0" opacity=".35"/>'
I[676]=svg(b,d)

# 687 PRIDE: a brass compass pointing steady at the North Star above a dark sea, a quiet certainty
d,b=bg([(0,'#04081e'),(1,'#1a2440')])
b+=starsf(60,687,800,'#e8f0ff')+sparkle(400,130,50,'#fff')+glow(400,130,60,'#fff6d8',.5)
b+='<circle cx="400" cy="500" r="200" fill="#c89a40"/><circle cx="400" cy="500" r="170" fill="#f4ece0"/>'
for k in range(8): a=math.radians(k*45);b+=f'<path d="M{400+150*math.cos(a):.0f} {500+150*math.sin(a):.0f} L{400+170*math.cos(a):.0f} {500+170*math.sin(a):.0f}" stroke="#3a2a1a" stroke-width="6"/>'
b+='<path d="M400 360 L430 500 L400 520 L370 500Z" fill="#e8102a"/><path d="M400 640 L430 500 L400 480 L370 500Z" fill="#3a3a44"/><circle cx="400" cy="500" r="14" fill="#c89a40"/>'
I[687]=svg(b,d)

# 778 HELLO: a window thrown open onto a bright morning, a big hand waving hello to the rising sun
d,b=bg([(0,'#ffd04a'),(1,'#ffa81a')])
b+=rays(560,300,20,'#ffffff',.3,7)+glow(560,300,120,'#fff8d8',.9)+'<circle cx="560" cy="300" r="70" fill="#fff8d8"/>'
b+='<rect x="0" y="0" width="160" height="800" fill="#f4e8d8"/><rect x="0" y="640" width="800" height="160" fill="#f4e8d8"/><path d="M160 0 L60 80 L60 700 L160 640Z" fill="#a8d8f0"/>'
b+='<g fill="#e8b890" transform="rotate(14 330 520)"><rect x="290" y="440" width="90" height="300" rx="30"/>'+''.join(f'<rect x="{282+k*26}" y="{330+abs(k-1.5)*14:.0f}" width="22" height="120" rx="11"/>' for k in range(4))+'<rect x="372" y="430" width="22" height="90" rx="11" transform="rotate(40 383 475)"/></g>'
I[778]=svg(b,d)

# 1571 青と夏: a towering summer thundercloud over a deep blue sky, a cold ramune bottle sweating in the foreground
d,b=bg([(0,'#0a6ae8'),(1,'#7ac8ff')])
for x,y,s in [(400,340,2.8),(260,420,1.8),(560,430,2.0)]: b+=cloud(x,y,s,'#fff',.98)
b+='<rect y="600" width="800" height="200" fill="#1a8ad8"/>'
b+='<path d="M560 760 L560 520 Q560 470 590 450 L590 410 L630 410 L630 450 Q660 470 660 520 L660 760Z" fill="#7ae0d8" opacity=".85"/><circle cx="610" cy="460" r="16" fill="#bff8ff"/><rect x="584" y="380" width="52" height="34" rx="6" fill="#3a9ae8"/>'
for x,y in [(580,600),(640,560),(600,680)]: b+=f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" opacity=".8"/>'
I[1571]=svg(b,d)

# 1804 Preserved Roses: two roses, one red and one blue, sealed under a glass dome lit from opposite sides
d,b=bg([(0,'#0a0a1a'),(1,'#1a0a1a')])
b+=glow(300,420,180,'#ff2a4a',.4)+glow(500,420,180,'#2a6aff',.4)
b+='<path d="M220 640 L220 320 Q220 160 400 150 Q580 160 580 320 L580 640Z" fill="#d8ecff" opacity=".15" stroke="#fff" stroke-width="5"/><rect x="190" y="630" width="420" height="40" rx="10" fill="#3a2a1a"/>'
b+='<path d="M330 630 Q330 520 340 420 M470 630 Q470 520 460 420" stroke="#2a5a2a" stroke-width="8" fill="none"/>'+rose(340,400,.9)+'<g transform="translate(460 400) scale(.9)">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#0a2aa8',1),(60,'#1a3ac8',.9),(-60,'#1a3ac8',.9),(150,'#3a5ae8',.7),(-150,'#3a5ae8',.7)])+'</g>'
I[1804]=svg(b,d)

# 981 SAKURAドロップス: a tin of fruit drops spilling out, every candy pressed into the shape of a cherry blossom
d,b=bg([(0,'#ffe8f0'),(1,'#ffd0e0')])
b+='<ellipse cx="300" cy="560" rx="180" ry="60" fill="#c8c8d0"/><path d="M120 560 L120 420 Q300 360 480 420 L480 560Z" fill="#e8302a"/><ellipse cx="300" cy="420" rx="180" ry="60" fill="#ff5a5a"/><ellipse cx="300" cy="420" rx="150" ry="44" fill="#3a1a1a"/>'
for x,y,c in [(260,410,'#ffc0d8'),(340,400,'#ffe05a'),(500,620,'#ff8ab8'),(580,560,'#ffffff'),(640,660,'#ffb0c8'),(450,700,'#ffd8e8'),(600,450,'#ff9aa8')]:
    b+=sakura(x,y,46,c,'#fff',x%60,.95)
I[981]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
