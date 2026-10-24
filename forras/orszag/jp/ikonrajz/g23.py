import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 23. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1371 世界には愛しかない: a girl's silhouette running across a rain-soaked summer field with arms open, a rainbow forming
d,b=bg([(0,'#7a9ab8'),(1,'#d8e8f0')])
b+=''.join(f'<path d="M-50 640 A450 450 0 0 1 850 640" stroke="{c}" stroke-width="20" fill="none" opacity=".5" transform="translate(0 {k*20})"/>' for k,c in enumerate(['#ff6a6a','#ffb02a','#ffe86a','#6ad86a','#6aa8ff']))+rain(30,1371,'#fff',.4)
b+='<path d="M-10 600 Q400 560 810 600 L810 810 L-10 810Z" fill="#6aa84a"/>'+figure(400,660,300,'#1a2a1a',pose='up')
I[1371]=svg(b,d)

# 1450 SPARK-AGAIN: a sword striking a blade, an explosion of orange sparks in the dark
d,b=bg([(0,'#0a0a14'),(1,'#1a0a0a')])
r=random.Random(1450)
b+=''.join(f'<path d="M400 400 L{400+r.randint(80,340)*math.cos(a):.0f} {400+r.randint(80,340)*math.sin(a):.0f}" stroke="{r.choice(["#ffb02a","#ffe86a","#ff6a2a"])}" stroke-width="{r.randint(2,6)}" stroke-linecap="round"/>' for a in [r.uniform(0,6.28) for _ in range(50)])
b+=glow(400,400,120,'#ffd02a',.8)+'<path d="M120 680 L420 380 L440 400 L140 700Z M680 680 L380 380 L360 400 L660 700Z" fill="#d8dce8"/>'
I[1450]=svg(b,d)

# 1610 僕が僕じゃないみたいだ: a figure looking into a mirror where the reflection is a different colour and pose
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+='<rect x="400" y="120" width="300" height="560" rx="20" fill="#8a9ab8" stroke="#c8a24a" stroke-width="12"/>'+figure(550,640,420,'#ff4a8a',pose='up')
b+=figure(240,680,440,'#05050a')+'<rect y="680" width="800" height="120" fill="#141420"/>'
I[1610]=svg(b,d)

# 397 水に挿した花: a single flower stem standing in a clear glass of water, light refracting, a moody night window
d,b=bg([(0,'#1a1430'),(1,'#3a2a50')])
b+=moon(620,160,40)+'<rect y="560" width="800" height="240" fill="#2a2030"/>'
b+='<path d="M340 560 L330 360 L470 360 L460 560Z" fill="#c8e8ff" opacity=".35" stroke="#e8f4ff" stroke-width="4"/><rect x="334" y="420" width="132" height="140" fill="#8ac8ff" opacity=".3"/>'
b+='<path d="M400 560 L400 240" stroke="#3a8a5a" stroke-width="6"/><path d="M400 470 L404 470" stroke="#3a8a5a" stroke-width="10"/>'+flower(400,220,46,6,'#f4f0ff','#e8c8f0')
I[397]=svg(b,d)

# 398 AL-MAUJ: a huge curling wave under a desert-gold moon, Arabian-style arches as silhouettes
d,b=bg([(0,'#1a0a2a'),(1,'#5a2a3a')])
b+=moon(600,180,70,'#ffd28a',.4)+''.join(f'<path d="M{x} 520 L{x} 420 Q{x+40} 360 {x+80} 420 L{x+80} 520Z" fill="#140818"/>' for x in (60,180,300))
b+='<path d="M-10 800 L-10 560 Q300 420 520 480 Q700 540 660 380 Q620 280 760 300 Q820 420 810 800Z" fill="#1a4a8a"/><path d="M520 480 Q700 540 660 380 Q640 320 700 300" stroke="#e8f4ff" stroke-width="10" fill="none"/>'
I[398]=svg(b,d)

# 550 禁断のテレパシー: two profiles facing each other with waves of violet light passing between them, a lock in the middle
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=profile(200,420,1.4,'#05020a')+profile(600,420,1.4,'#05020a',flip=True)
b+=''.join(f'<path d="M{300+k*40} {360} Q{320+k*40} 400 {300+k*40} 440" stroke="#c88aff" stroke-width="5" fill="none" opacity="{.4+k*.1:.2f}"/>' for k in range(5))
I[550]=svg(b,d)

# 783 化身: a man's shadow on a wall that turns into a wolf's shape, a single bulb
d,b=bg([(0,'#2a2018'),(1,'#1a1410')])
b+='<circle cx="140" cy="140" r="22" fill="#ffe8a0"/>'+glow(140,140,200,'#ffd27a',.35)+'<rect y="640" width="800" height="160" fill="#14100c"/>'
b+=figure(260,660,300,'#000')+'<path d="M420 640 Q440 460 540 420 L560 360 L590 410 L640 400 Q700 440 720 520 Q740 600 720 640Z" fill="#0a0806" opacity=".85"/><path d="M560 360 L570 320 L590 410Z" fill="#0a0806" opacity=".85"/>'
I[783]=svg(b,d)

# 1026 心中: two red camellia flowers floating together on a dark river, joined by a red thread
d,b=bg([(0,'#0a0a14'),(1,'#141424')])
b+=''.join(f'<path d="M0 {420+k*60} Q400 {400+k*60} 800 {430+k*60}" stroke="#2a2a44" stroke-width="3" fill="none"/>' for k in range(6))
b+=flower(330,480,60,5,'#c8102a','#ffd02a')+flower(480,500,60,5,'#c8102a','#ffd02a')+'<path d="M370 500 Q410 560 440 520" stroke="#e8102a" stroke-width="4" fill="none"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="6" fill="#c8102a" opacity=".6"/>' for x,y in [(220,600),(600,640),(520,380)])
I[1026]=svg(b,d)

# 1061 花火: a single firework bursting above a riverbank, a girl in a yukata watching alone
d,b=bg([(0,'#0a0a24'),(1,'#1a1a40')])
b+=firework(460,240,170,'#ffb02a',seed=1061)+'<rect y="560" width="800" height="240" fill="#0e1430"/><path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#0a0a18"/>'
b+=figure(260,640,220,'#000')+'<rect x="238" y="520" width="44" height="14" fill="#ff8ab8" opacity=".7"/>'
I[1061]=svg(b,d)

# 1147 全力少年: a boy sprinting with a school bag flying, motion lines, a bright blue summer sky
d,b=bg([(0,'#2a9af8'),(1,'#c8ecff')])
b+=cloud(600,160,1.6)+''.join(f'<path d="M{60+k*20} {380+k*40} L{220+k*20} {380+k*40}" stroke="#fff" stroke-width="6" stroke-linecap="round"/>' for k in range(5))+'<rect y="620" width="800" height="180" fill="#d8a060"/>'
b+='<g transform="rotate(15 420 500)">'+figure(420,640,320,'#1a1a3a',pose='reach')+'</g>'+'<rect x="300" y="420" width="70" height="50" rx="10" fill="#c8302a" transform="rotate(-25 335 445)"/>'
I[1147]=svg(b,d)

# 1183 Wildflower: a wild flower pushing up through a crack in concrete, wind-blown and bright yellow
d,b=bg([(0,'#c8d0d8'),(1,'#8a9098')])
b+='<rect y="500" width="800" height="300" fill="#6a6a70"/>'+bolt([(260,500),(300,580),(340,620),(320,700),(380,800)],'#3a3a40',10)
b+='<path d="M320 640 Q330 520 400 400" stroke="#3a8a3a" stroke-width="8" fill="none"/><path d="M340 560 Q280 520 280 480 Q330 500 345 545Z" fill="#4ac84a"/>'+flower(400,380,60,10,'#ffd02a','#8a5a1a',rot=15)
I[1183]=svg(b,d)

# 1189 Spring Of Life: a mechanical spring-coil uncoiling into blooming blossom petals, neon pink and white
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a4a')])
b+=''.join(f'<ellipse cx="400" cy="{620-k*44}" rx="{90-k*4}" ry="18" fill="none" stroke="#c8c8e0" stroke-width="10"/>' for k in range(7))
b+=''.join(sakura(400+dx,240+dy,s,'#ff8ad8','#fff') for dx,dy,s in [(0,0,1.2),(-90,30,.9),(90,40,1),(-50,-70,.8),(60,-80,.9)])+petals(20,1189,'#ff8ad8',0,500)
I[1189]=svg(b,d)

# 1590 二度寝: a person buried under a fluffy duvet as the alarm clock is knocked over, morning sun ignored
d,b=bg([(0,'#fff0c8'),(1,'#ffd8a8')])
b+=glow(660,140,180,'#fff',.7)+'<rect y="520" width="800" height="280" fill="#8a6a5a"/>'
b+='<path d="M80 600 Q120 420 300 440 Q480 400 620 460 Q720 500 740 600Z" fill="#f8f4ff" stroke="#d8d0e8" stroke-width="6"/><ellipse cx="180" cy="500" rx="90" ry="40" fill="#e8e0f8"/><path d="M150 480 Q180 460 210 480" stroke="#5a3a2a" stroke-width="20" fill="none" stroke-linecap="round"/>'
b+='<g transform="rotate(70 640 650)"><circle cx="640" cy="650" r="50" fill="#e8302a"/><circle cx="640" cy="650" r="38" fill="#fff"/></g>'+txt(400,300,'Zzz',80,'#8a7a9a')
I[1590]=svg(b,d)

# 366 Eighteen: a girl's silhouette in a summer dress on a swing at a seaside park, the number 18 in the clouds
d,b=bg([(0,'#7ac8ff'),(1,'#e8f8ff')])
b+=cloud(560,170,2)+'<rect y="460" width="800" height="120" fill="#3a9ad8"/><rect y="580" width="800" height="220" fill="#a8d88a"/>'
b+='<path d="M180 580 L240 220 L560 220 L620 580" stroke="#c8302a" stroke-width="10" fill="none"/><path d="M360 220 L330 470 M440 220 L470 470" stroke="#5a5a5a" stroke-width="4"/><rect x="320" y="468" width="160" height="12" fill="#8a5a3a"/>'
b+='<g fill="#2a1a3a"><circle cx="400" cy="380" r="22"/><path d="M380 404 L420 404 L450 470 L350 470Z"/></g>'
I[366]=svg(b,d)

# 719 永遠の夢に向かって: a figure on a mountain summit planting a flag toward a sunrise, rays fanning out
d,b=bg([(0,'#3a4aa8'),(.6,'#ff9a6a'),(1,'#ffd8a8')])
b+=hinomaru_sun(400,520,90,'#fff2c8')+rays(400,520,26,'#fff',.15,8)+'<path d="M-10 800 L300 440 L400 380 L500 440 L810 800Z" fill="#2a2a44"/>'
b+=figure(400,390,170,'#000',pose='up')+'<path d="M460 260 L460 380" stroke="#000" stroke-width="5"/><path d="M460 260 L530 280 L460 300Z" fill="#ff4a4a"/>'
I[719]=svg(b,d)

# 747 Any: many small paper boats on a river, each carrying a tiny light, heading into the dusk
d,b=bg([(0,'#3a3a6a'),(.6,'#c88a8a'),(1,'#f8c8a0')])
b+='<rect y="440" width="800" height="360" fill="#3a4a6a"/>'
for k in range(9):
    x=80+(k*83)%640;y=480+k*36;s=.6+k*.07
    b+=f'<path d="M{x-40*s} {y} L{x+40*s} {y} L{x+24*s} {y+20*s} L{x-24*s} {y+20*s}Z M{x} {y} L{x} {y-30*s} L{x+20*s} {y}Z" fill="#f4f0e8"/><circle cx="{x}" cy="{y-36*s}" r="{5*s}" fill="#ffd27a"/>'
I[747]=svg(b,d)

# 748 掌: an open palm holding a small glowing sphere of light, warm on a dark ground
d,b=bg([(0,'#1a1410'),(1,'#2a1e14')])
b+=glow(400,340,180,'#ffd28a',.6)+'<circle cx="400" cy="340" r="50" fill="#fff4d0"/>'
b+='<path d="M220 520 Q260 420 330 420 L470 420 Q540 420 580 520 Q560 560 520 560 L280 560 Q240 560 220 520Z" fill="#e0b098" stroke="#b88a72" stroke-width="5"/>'+''.join(f'<path d="M{x} 420 Q{x+4} {380+(x%3)*6} {x+20} 380 Q{x+36} {380+(x%3)*6} {x+40} 420" fill="#e0b098" stroke="#b88a72" stroke-width="5"/>' for x in (280,330,380,430))+'<path d="M300 480 Q400 500 500 470" stroke="#b88a72" stroke-width="3" fill="none"/>'
I[748]=svg(b,d)

# 870 SEVENTH HEAVEN: seven glowing tiers of clouds stacked into the sky with a stairway of light
d,b=bg([(0,'#2a1a6a'),(1,'#8a6ab8')])
for k in range(7): b+=cloud(400,700-k*90,3.2-k*.35,'#fff',.35+k*.08)
b+=glow(400,80,120,'#fff6d8',.8)+'<polygon points="380,700 420,700 404,80 396,80" fill="#fff6d8" opacity=".6"/>'
I[870]=svg(b,d)

# 891 Time goes by: a pocket watch half sunk in the sand on a beach, waves washing over it
d,b=bg([(0,'#a8c8e8'),(1,'#f0e0c8')])
b+='<rect y="360" width="800" height="140" fill="#6a9ac8"/><path d="M-10 500 Q200 460 400 500 Q600 540 810 500 L810 810 L-10 810Z" fill="#f0dcb8"/><path d="M-10 500 Q200 460 400 500 Q600 540 810 500" stroke="#fff" stroke-width="10" fill="none"/>'
b+='<circle cx="420" cy="620" r="90" fill="#c8a24a"/><circle cx="420" cy="620" r="74" fill="#fbf4e4"/>'+''.join(f'<circle cx="{420+60*math.cos(math.radians(a)):.0f}" cy="{620+60*math.sin(math.radians(a)):.0f}" r="4" fill="#3a2a1a"/>' for a in range(0,360,30))+'<path d="M420 620 L420 570 M420 620 L460 640" stroke="#1a1a1a" stroke-width="5"/><path d="M330 680 Q420 640 510 680 L510 720 L330 720Z" fill="#f0dcb8"/><path d="M420 530 Q400 480 430 440" stroke="#c8a24a" stroke-width="5" fill="none"/>'
I[891]=svg(b,d)

# 1010 ourselves: many paper cutout figures holding hands in a circle seen from above, pastel colours
d,b=bg([(0,'#f8e8f0'),(1,'#e8d8f0')])
for k in range(12):
    a=k*30;x=400+200*math.cos(math.radians(a));y=400+200*math.sin(math.radians(a))
    b+=f'<g transform="rotate({a+90} {x:.0f} {y:.0f})">'+figure(x,y+60,120,["#ff8ab8","#8ab8ff","#ffd06a","#8ad8a8"][k%4],pose='reach')+'</g>'
b+=heart(400,400,50,'#ff6a9a')
I[1010]=svg(b,d)

# 1011 is this LOVE?: a question-mark shaped ribbon tied around a gift box, petals of pink falling
d,b=bg([(0,'#ffd8e8'),(1,'#fff4f8')])
b+=petals(20,1011,'#ff9ac0')+'<rect x="250" y="420" width="300" height="240" fill="#ff6a9a"/><rect x="230" y="380" width="340" height="60" fill="#ff4a8a"/><rect x="380" y="380" width="40" height="280" fill="#fff"/>'
b+='<path d="M330 380 Q300 200 400 200 Q500 200 480 290 Q460 340 400 360" stroke="#fff" stroke-width="30" fill="none" stroke-linecap="round"/><circle cx="400" cy="380" r="18" fill="#fff"/>'
I[1011]=svg(b,d)

# 1102 チェスト: a group of high school boys' silhouettes shouting with raised fists on a Okinawan beach at sunset
d,b=bg([(0,'#ff6a3a'),(1,'#ffc87a')])
b+=hinomaru_sun(400,400,110,'#ffe0a0')+'<rect y="440" width="800" height="120" fill="#e85a3a"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#f0c890"/>'
b+=''.join(figure(x,660,h,'#3a1010',pose=p) for x,h,p in [(160,240,'up'),(290,250,'wave'),(420,260,'up'),(550,240,'wave'),(670,250,'up')])+'<path d="M80 560 Q100 400 70 300" stroke="#3a1010" stroke-width="12" fill="none"/>'+''.join(f'<path d="M70 300 Q{70+dx} {300+dy} {70+dx*2} {320+dy*2}" stroke="#3a1010" stroke-width="9" fill="none"/>' for dx,dy in [(40,-10),(-30,0),(30,30)])
I[1102]=svg(b,d)

# 1141 リライト: an eraser rubbing out handwritten lines on a page as new bold lines appear, electric orange
d,b=bg([(0,'#ff8a2a'),(1,'#ffc86a')])
b+='<rect x="140" y="140" width="520" height="520" fill="#fffbea" transform="rotate(-4 400 400)"/>'+''.join(f'<path d="M180 {220+k*60} L{600-(k%3)*60} {210+k*60}" stroke="#1a1a1a" stroke-width="{3 if k<4 else 10}" opacity="{.3 if k<4 else 1}"/>' for k in range(7))
b+='<g transform="rotate(30 520 300)"><rect x="440" y="260" width="180" height="80" rx="10" fill="#ff6a9a"/><rect x="440" y="260" width="60" height="80" rx="10" fill="#3a8af8"/></g>'+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#c8b8a0"/>' for x,y in [(460,380),(480,400),(440,410)])
I[1141]=svg(b,d)

# 1638 Love seeker: a figure with a flashlight searching a dark city, the beam finding a glowing heart on a rooftop
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a30')])
b+=skyline(640,'#141424',1638,80,300,'#5a5a8a',60)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'
b+='<polygon points="240,520 640,240 680,320" fill="#fff6d8" opacity=".25"/>'+heart(640,280,40,'#ff2a6a')+glow(640,280,70,'#ff2a6a',.5)+figure(220,660,240,'#000',pose='reach')
I[1638]=svg(b,d)

# 1772 Last Chance: a final train leaving a night station, a figure running along the platform toward it
d,b=bg([(0,'#0a1028'),(1,'#1a2440')])
b+='<rect y="500" width="800" height="300" fill="#3a3a44"/><rect y="490" width="800" height="12" fill="#ffd02a"/>'
b+='<rect x="440" y="320" width="400" height="180" fill="#c8ccd8"/>'+''.join(f'<rect x="{470+k*90}" y="350" width="60" height="60" fill="#ffe8a0"/>' for k in range(4))+'<rect x="440" y="440" width="400" height="12" fill="#2a8a4a"/>'
b+='<g transform="rotate(12 260 520)">'+figure(260,500,240,'#000',pose='reach')+'</g>'
I[1772]=svg(b,d)

# 139 あばよ: a woman's back walking away down a rainy alley, a red umbrella, a man's hat left on a bench
d,b=bg([(0,'#3a3a4a'),(1,'#6a6a7a')])
b+=rain(70,139,'#d8d8e8',.35)+'<path d="M300 300 L500 300 L800 800 L0 800Z" fill="#2a2a34"/><path d="M0 0 L300 300 L300 800 L0 800Z M800 0 L500 300 L500 800 L800 800Z" fill="#1a1a24"/>'
b+=figure(420,520,200,'#05050a')+'<path d="M350 330 Q420 270 490 330Z" fill="#d8102a"/><path d="M420 330 L420 400" stroke="#1a1a1a" stroke-width="3"/>'
b+='<rect x="80" y="640" width="160" height="14" fill="#5a4a3a"/><path d="M120 640 Q120 610 160 610 Q200 610 200 640Z M100 640 L220 640" fill="#1a1a1a" stroke="#1a1a1a" stroke-width="6"/>'
I[139]=svg(b,d)

# 410 夏色片想い: a girl holding a letter behind her back watching someone at the far end of a sunny beach
d,b=bg([(0,'#5ac8ff'),(1,'#e0f8ff')])
b+=cloud(560,150,1.6)+'<rect y="400" width="800" height="160" fill="#2aa8e8"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#f8e0a8"/>'
b+=figure(260,700,320,'#2a2a4a')+'<rect x="290" y="500" width="50" height="34" fill="#fff" stroke="#ff8ab8" stroke-width="4"/>'+figure(620,560,110,'#5a6a8a')+heart(330,470,14,'#ff6a9a')
I[410]=svg(b,d)

# 492 SQUALL: a lone figure in a long coat on a cliff facing a violent squall of rain and lightning over the sea
d,b=bg([(0,'#1a1a24'),(1,'#3a3a4a')])
b+=rain(120,492,'#c8d0e0',.4,ang=20)+bolt([(560,40),(520,160),(560,180),(500,320)],'#fff',8)+'<rect y="520" width="800" height="280" fill="#1a2a3a"/>'
b+='<path d="M-10 800 L-10 560 L300 520 L340 800Z" fill="#0a0a10"/>'+figure(200,540,240,'#000')+'<path d="M180 400 L130 520 L230 520Z" fill="#000"/>'
I[492]=svg(b,d)

# 670 声明: a raised microphone stand like a flag on a rock stage, a crowd sea of lights
d,b=bg([(0,'#0a0a14'),(1,'#2a1a2a')])
b+=rays(400,200,24,'#fff',.15,6)+'<path d="M400 640 L400 200" stroke="#c8c8d0" stroke-width="12"/><path d="M400 200 L440 160" stroke="#c8c8d0" stroke-width="10"/><ellipse cx="452" cy="148" rx="22" ry="30" fill="#2a2a2a" transform="rotate(40 452 148)"/>'
b+='<path d="M300 640 L500 640 L520 680 L280 680Z" fill="#2a2a2a"/>'+''.join(f'<circle cx="{(k*53)%800}" cy="{700+(k*29)%100}" r="{4+k%3}" fill="{["#ffd02a","#fff","#ff4a6a"][k%3]}"/>' for k in range(60))
I[670]=svg(b,d)

# 1086 熱帯夜: a sweltering night with a fan, a melting popsicle and a ceiling of heat haze in purple-orange
d,b=bg([(0,'#3a1a4a'),(1,'#e86a3a')])
b+=moon(620,140,50,'#ffd28a',.3)+''.join(f'<path d="M0 {200+k*60} Q200 {180+k*60} 400 {200+k*60} T800 {200+k*60}" stroke="#ff9a6a" stroke-width="3" fill="none" opacity=".4"/>' for k in range(5))
b+='<circle cx="280" cy="520" r="120" fill="#2a2a3a"/>'+''.join(f'<ellipse cx="{280+60*math.cos(math.radians(a)):.0f}" cy="{520+60*math.sin(math.radians(a)):.0f}" rx="50" ry="20" fill="#9ad8ff" transform="rotate({a} {280+60*math.cos(math.radians(a)):.0f} {520+60*math.sin(math.radians(a)):.0f})"/>' for a in (0,120,240))+'<rect x="270" y="640" width="20" height="100" fill="#2a2a3a"/>'
b+='<rect x="520" y="420" width="80" height="160" rx="30" fill="#ff8ab8"/><path d="M540 580 Q550 620 540 640" stroke="#ff8ab8" stroke-width="10" fill="none"/><rect x="552" y="580" width="16" height="80" fill="#d8b878"/>'
I[1086]=svg(b,d)

# 1311 さよならクロール: a swimmer's arm mid-crawl stroke in a sparkling summer pool, lane ropes
d,b=bg([(0,'#2ac8f0'),(1,'#1a8ad8')])
b+=''.join(f'<path d="M0 {y} Q200 {y-20} 400 {y} T800 {y}" stroke="#fff" stroke-width="4" fill="none" opacity=".4"/>' for y in range(80,800,80))+''.join(f'<path d="M0 {y} L800 {y}" stroke="{c}" stroke-width="14" stroke-dasharray="20 10"/>' for y,c in [(200,'#ff4a4a'),(620,'#ffd02a')])
b+='<path d="M300 440 Q380 220 520 260" stroke="#e0b098" stroke-width="40" fill="none" stroke-linecap="round"/><ellipse cx="300" cy="460" rx="60" ry="30" fill="#1a1a1a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#fff"/>' for x,y,r2 in [(540,240,10),(560,280,7),(500,220,6),(380,480,12),(420,500,8)])
I[1311]=svg(b,d)

# 1357 しあわせの保護色: a figure blending into a pastel wall of flowers, only the outline visible
d,b=bg([(0,'#f8e0f0'),(1,'#e0f0f8')])
for k in range(40):
    x=(k*137)%800;y=(k*89)%800
    b+=flower(x,y,40,5,["#ffb8d8","#b8d8ff","#fff0a8","#c8f0c8"][k%4],'#fff')
b+='<g>'+figure(400,720,460,'#f8e0f0').replace('<g fill="#f8e0f0">','<g fill="#ffd8e8" opacity=".85" stroke="#ff8ab8" stroke-width="6">')+'</g>'
I[1357]=svg(b,d)

# 1480 PPAP: a pen, a pineapple and an apple floating together on a bright yellow-leopard-like pattern
d,b=bg([(0,'#ffe02a'),(1,'#ffb02a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="12" fill="#c8801a" opacity=".5"/>' for x in range(40,800,90) for y in range(40,800,90))
b+='<g transform="rotate(-30 200 400)"><rect x="180" y="220" width="40" height="320" rx="10" fill="#1a1a1a"/><polygon points="180,540 220,540 200,590" fill="#e8d8b8"/></g>'
b+='<ellipse cx="420" cy="460" rx="90" ry="130" fill="#e8b02a"/>'+''.join(f'<path d="M{350+k*30} 350 L{400+k*30} 580" stroke="#a8701a" stroke-width="4"/>' for k in range(4))+''.join(f'<path d="M420 330 L{420+dx} 220" stroke="#3aa83a" stroke-width="16" stroke-linecap="round"/>' for dx in (-50,0,50))
b+='<circle cx="630" cy="460" r="80" fill="#e8102a"/><path d="M630 380 L640 340" stroke="#5a3a1a" stroke-width="8"/><path d="M640 350 Q680 330 690 360 Q660 370 640 350Z" fill="#3aa83a"/>'
I[1480]=svg(b,d)

# 1606 KISSIN' MY LIPS: a lipstick kiss mark on a mirror with sparkling glints, black and hot pink
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a1a')])
b+='<rect x="140" y="140" width="520" height="520" rx="260" fill="#2a2a34" stroke="#c8a24a" stroke-width="14"/>'
b+='<path d="M260 400 Q320 320 380 360 Q400 340 420 360 Q480 320 540 400 Q480 480 400 480 Q320 480 260 400Z" fill="#ff1a7a"/><path d="M260 400 Q400 430 540 400" stroke="#2a2a34" stroke-width="6" fill="none"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(560,250,26),(240,540,18),(580,560,14)])
I[1606]=svg(b,d)

# 126 ウォンテッド: a wanted poster with a heart in place of a face, pinned on a wooden wall, late-70s disco colours
d,b=bg([(0,'#8a4a2a'),(1,'#5a2a1a')])
b+=''.join(f'<path d="M{x} 0 L{x} 800" stroke="#4a2010" stroke-width="4"/>' for x in range(0,800,80))
b+='<rect x="220" y="120" width="360" height="520" fill="#f4e0b0" transform="rotate(-3 400 380)"/>'+txt(400,220,'WANTED',70,'#5a2a1a',900)+heart(400,380,90,'#e8102a')+'<rect x="300" y="500" width="200" height="16" fill="#5a2a1a"/><rect x="330" y="540" width="140" height="12" fill="#5a2a1a"/><circle cx="400" cy="140" r="10" fill="#c8c8c8"/>'
I[126]=svg(b,d)

# 208 学生街の喫茶店: a 70s student-quarter coffee shop window, a record player and two coffee cups, autumn leaves outside
d,b=bg([(0,'#c8a070'),(1,'#8a6040')])
b+='<rect x="80" y="100" width="640" height="380" fill="#e8c890"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="8" fill="#d8602a" transform="rotate(30 {x} {y})"/>' for x,y in [(180,180),(320,240),(520,160),(620,300),(400,360)])+'<path d="M80 290 L720 290 M400 100 L400 480" stroke="#5a3a2a" stroke-width="12"/>'
b+='<rect y="480" width="800" height="320" fill="#6a4028"/><rect x="160" y="520" width="220" height="80" fill="#3a2a1a"/><circle cx="250" cy="540" r="50" fill="#1a1a1a" transform="scale(1 .4) translate(0 810)"/>'
b+=''.join(f'<path d="M{x} 560 L{x+10} 620 L{x+70} 620 L{x+80} 560Z" fill="#f4ead8"/><path d="M{x+80} 575 Q{x+105} 585 {x+80} 605" stroke="#f4ead8" stroke-width="7" fill="none"/>' for x in (460,580))
I[208]=svg(b,d)

# 336 Last Summer Whisper: a seashell held to an ear-shaped glow by the sea at sunset, city-pop pastel tones
d,b=bg([(0,'#ff9ac8'),(.6,'#ffc8a0'),(1,'#a8d8f0')])
b+=hinomaru_sun(560,380,90,'#fff0c8',.8)+'<rect y="420" width="800" height="140" fill="#6ab8e0"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#f8dcc0"/>'
b+='<path d="M280 640 Q240 520 320 470 Q420 430 460 520 Q480 600 400 660Z" fill="#fff4ea" stroke="#e8b8a8" stroke-width="6"/>'+''.join(f'<path d="M{300+k*20} 620 Q{340+k*16} 520 {420} 490" stroke="#e8b8a8" stroke-width="4" fill="none"/>' for k in range(4))
b+=''.join(f'<path d="M{480+k*30} {440-k*10} Q{500+k*30} {420-k*10} {480+k*30} {400-k*10}" stroke="#fff" stroke-width="4" fill="none" opacity="{.8-k*.2:.2f}"/>' for k in range(3))
I[336]=svg(b,d)

# 423 センチメンタル: a girl writing in a diary at a window seat, a dried flower pressed between the pages, autumn light
d,b=bg([(0,'#f8d8a8'),(1,'#e8b880')])
b+='<rect x="440" y="100" width="280" height="340" fill="#fff4d8"/><path d="M580 100 L580 440 M440 270 L720 270" stroke="#8a5a3a" stroke-width="10"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="7" fill="#e8802a" transform="rotate(30 {x} {y})"/>' for x,y in [(500,160),(640,220),(560,360)])
b+='<rect y="520" width="800" height="280" fill="#8a5a3a"/><path d="M160 560 L400 540 L640 560 L640 660 L400 640 L160 660Z" fill="#fbf6ea"/><path d="M400 540 L400 640" stroke="#c8b898" stroke-width="3"/>'+flower(500,590,22,5,'#d8a0c0','#e8c87a')
b+='<g fill="#3a2a2a"><circle cx="260" cy="400" r="30"/><path d="M220 440 L300 440 L320 540 L200 540Z"/></g>'
I[423]=svg(b,d)

# 1290 会いたくて 会いたくて: a girl clutching a phone to her chest on a bed at night, the screen glow showing an unanswered call
d,b=bg([(0,'#0a0a24'),(1,'#1a1a40')])
b+=moon(620,160,40)+'<rect y="520" width="800" height="280" fill="#2a2a50"/><path d="M80 520 L720 520 L720 600 L80 600Z" fill="#c8c8e8"/>'
b+='<g fill="#000"><circle cx="360" cy="380" r="34"/><path d="M310 420 Q360 400 410 420 L430 540 L290 540Z"/></g><path d="M330 340 Q300 400 310 460 M390 340 Q420 400 410 460" stroke="#000" stroke-width="20" fill="none"/>'
b+='<rect x="345" y="440" width="30" height="50" rx="5" fill="#9ad8ff"/>'+glow(360,465,90,'#9ad8ff',.5)
I[1290]=svg(b,d)

# 1312 永遠プレッシャー: a girl in a winter coat with a scarf blowing, a pressure gauge needle in the red behind her
d,b=bg([(0,'#c8d8f0'),(1,'#f4f8ff')])
b+=snow(40,1312,.6)+'<circle cx="400" cy="300" r="200" fill="#fff" stroke="#2a2a3a" stroke-width="16"/><path d="M260 380 A160 160 0 0 1 540 380" stroke="#e8102a" stroke-width="20" fill="none" stroke-dasharray="0 220 200"/><path d="M400 300 L520 200" stroke="#1a1a1a" stroke-width="10" stroke-linecap="round"/><circle cx="400" cy="300" r="16" fill="#1a1a1a"/>'
b+=figure(400,780,280,'#1a1a3a')+'<path d="M380 540 L300 560 L320 580Z" fill="#e8102a"/>'
I[1312]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
