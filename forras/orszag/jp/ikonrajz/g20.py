import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 20. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 902 All My True Love: four girls' silhouettes holding hands on a beach at sunset, a heart drawn in the sand
d,b=bg([(0,'#ff7a8a'),(.55,'#ffc8a0'),(1,'#ffe8c8')])
b+=hinomaru_sun(400,400,110,'#fff0c8',.85)+'<rect y="440" width="800" height="120" fill="#ff9a8a" opacity=".7"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#f4d8b0"/>'
b+=''.join(figure(x,620,220,'#3a1a2a') for x in (250,350,450,550))+'<path d="M290 470 L350 470 M390 470 L450 470 M490 470 L550 470" stroke="#3a1a2a" stroke-width="10"/>'+'<path d="M400 760 Q340 700 370 680 Q400 670 400 700 Q400 670 430 680 Q460 700 400 760Z" fill="none" stroke="#c8a070" stroke-width="5"/>'
I[902]=svg(b,d)

# 945 Harmony of December: two glowing windows in a snowy December street, a string of lights joining them
d,b=bg([(0,'#0a1438'),(1,'#2a3a6a')])
b+=snow(100,945)
for x in (120,480): b+=f'<rect x="{x}" y="260" width="200" height="380" fill="#3a2a2a"/><rect x="{x+40}" y="320" width="120" height="140" fill="#ffd28a"/>'+glow(x+100,390,110,'#ffd28a',.35)+f'<path d="{"M%d 300 L%d 220 L%d 300Z"%(x-10,x+100,x+210)}" fill="#fff"/>'
b+='<path d="M220 300 Q400 380 580 300" stroke="#2a2a2a" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{220+k*40}" cy="{300+80*math.sin(math.pi*k/9)*.9:.0f}" r="9" fill="{c}"/>' for k,c in enumerate(['#ff4a4a','#ffd02a','#4ad8ff','#5ad85a']*3) if k<10)+'<rect y="640" width="800" height="160" fill="#eef2fa"/>'
I[945]=svg(b,d)

# 1006 INSPIRE: a figure on a mountain ridge reaching toward a burst of light in a stormy sky
d,b=bg([(0,'#2a2a4a'),(.5,'#6a5a8a'),(1,'#d8a07a')])
b+=glow(560,220,200,'#fff6d0',.6)+rays(560,220,28,'#fff6d0',.2,6)+cloud(200,260,2,'#5a5a7a')
b+='<path d="M-10 800 L-10 620 L200 520 L360 600 L520 470 L700 560 L810 520 L810 800Z" fill="#1a1428"/>'+figure(520,480,220,'#0a0814',pose='reach')
I[1006]=svg(b,d)

# 1306 希望的リフレイン: a repeating row of sunflowers on a green hill under a clear sky, the pattern echoing like a refrain
d,b=bg([(0,'#4ab8ff'),(1,'#d8f4ff')])
b+=cloud(560,160,1.6)+'<path d="M-10 520 Q400 440 810 520 L810 810 L-10 810Z" fill="#5ac84a"/>'
for k,(x,y,s) in enumerate([(120,600,1),(260,560,1.1),(400,540,1.2),(540,560,1.1),(680,600,1)]):
    b+=f'<path d="M{x} {y} L{x} {y+220}" stroke="#2a8a2a" stroke-width="10"/>'+flower(x,y,52*s,14,'#ffd02a','#6a3a1a')
I[1306]=svg(b,d)

# 1307 #好きなんだ: a smartphone with a hashtag heart glowing, summer sea behind
d,b=bg([(0,'#4ad8ff'),(.6,'#a8f0ff'),(1,'#1a9ad8')])
b+='<rect y="460" width="800" height="340" fill="#1a9ad8"/>'+hinomaru_sun(620,160,60,'#fffbe0')
b+='<rect x="250" y="180" width="300" height="540" rx="40" fill="#1a1a1a"/><rect x="270" y="220" width="260" height="460" rx="16" fill="#fff"/>'+txt(400,400,'#',180,'#ff4a8a')+heart(400,540,60,'#ff4a8a')
I[1307]=svg(b,d)

# 1352 いつかできるから今日できる: a girl stretching at a sunrise starting line on a school track
d,b=bg([(0,'#ffb07a'),(1,'#ffe8c8')])
b+=hinomaru_sun(560,380,100,'#fff2c8')+'<path d="M-10 480 L810 480 L810 810 L-10 810Z" fill="#d8603a"/>'+''.join(f'<path d="M-10 {520+k*70} L810 {500+k*80}" stroke="#fff" stroke-width="5"/>' for k in range(4))
b+='<rect x="300" y="560" width="10" height="240" fill="#fff"/>'+figure(260,640,260,'#2a1a2a',pose='up')
I[1352]=svg(b,d)

# 1370 風に吹かれても: a young man in a dark coat standing firm on a hill as strong wind bends the grass and leaves fly past
d,b=bg([(0,'#5a6a7a'),(1,'#a8b8c0')])
b+=''.join(f'<path d="M{-50+k*90} {200+k*30} Q{150+k*90} {170+k*30} {350+k*90} {200+k*30}" stroke="#e0e8f0" stroke-width="5" fill="none" opacity=".6"/>' for k in range(6))
b+='<path d="M-10 640 Q400 580 810 640 L810 810 L-10 810Z" fill="#3a4a3a"/>'+''.join(f'<path d="M{x} 640 Q{x+30} 600 {x+60} 590" stroke="#5a7a4a" stroke-width="5" fill="none"/>' for x in range(0,800,30))
b+=figure(400,640,360,'#0a0a10')+'<path d="M372 360 L300 380 L330 420Z" fill="#0a0a10"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="6" fill="#8a6a3a" transform="rotate(30 {x} {y})"/>' for x,y in [(560,300),(640,420),(180,260),(700,250)])
I[1370]=svg(b,d)

# 1372 BAN: a red prohibition sign cracking apart, a crowd of raised fists in silhouette below
d,b=bg([(0,'#1a0a0a'),(1,'#3a1010')])
b+=ring(400,300,180,'#e8102a',40)+'<path d="M275 175 L525 425" stroke="#e8102a" stroke-width="40"/>'+bolt([(400,120),(380,200),(420,260),(390,320)],'#1a0a0a',10)
b+=''.join(f'<path d="M{x} 800 L{x} {640-h} " stroke="#000" stroke-width="30"/><circle cx="{x}" cy="{630-h}" r="22" fill="#000"/>' for x,h in [(120,20),(220,60),(330,30),(470,70),(580,10),(690,50)])+'<rect y="720" width="800" height="80" fill="#000"/>'
I[1372]=svg(b,d)

# 1568 damn: a cracked coffee cup on a tilted piano lid, a cloud of grey sigh drifting up
d,b=bg([(0,'#e8e0d0'),(1,'#c8b8a0')])
b+='<path d="M60 560 L740 520 L740 600 L60 640Z" fill="#1a1a1a"/>'+''.join(f'<rect x="{80+k*42}" y="{596-k*2}" width="36" height="40" fill="#fff"/>' for k in range(15))
b+='<path d="M330 520 L340 400 L460 400 L470 520Z" fill="#fff" stroke="#8a7a6a" stroke-width="5"/><path d="M470 430 Q520 440 470 480" stroke="#8a7a6a" stroke-width="10" fill="none"/>'+bolt([(400,400),(390,440),(410,470),(395,520)],'#8a7a6a',4)
b+=cloud(420,260,1.3,'#8a8a90',.7)
I[1568]=svg(b,d)

# 1848 魔法にかけられて: a girl in a pumpkin-coloured dress twirling in a cloud of golden magic sparkles at midnight
d,b=bg([(0,'#1a1440'),(1,'#4a2a6a')])
b+=starsf(50,1848,600)+moon(620,160,50)+glow(400,480,220,'#ffd860',.35)
b+=''.join(sparkle(400+180*math.cos(a/3),480+120*math.sin(a/2),10+(a*7)%14,'#ffe680') for a in range(0,24))
b+=figure(400,700,320,'#1a0a24',pose='up')+'<path d="M330 560 Q400 520 470 560 L520 680 L280 680Z" fill="#e8802a"/>'
I[1848]=svg(b,d)

# 664 BURN ‐フメツノフェイス‐: a mask-like face silhouette made of flames that will not die, embers rising
d,b=bg([(0,'#1a0505'),(1,'#3a0a0a')])
r=random.Random(664)
b+=''.join(f'<circle cx="{r.randint(60,740)}" cy="{r.randint(60,700)}" r="{r.randint(2,6)}" fill="#ffb02a" opacity="{r.uniform(.4,.9):.2f}"/>' for _ in range(40))
b+='<path d="M400 120 Q520 260 500 420 Q490 560 400 640 Q310 560 300 420 Q280 260 400 120Z" fill="#e8402a"/><path d="M400 220 Q470 330 460 440 Q450 540 400 590 Q350 540 340 440 Q330 330 400 220Z" fill="#ffa02a"/><path d="M400 330 Q440 400 430 470 Q420 530 400 550 Q380 530 370 470 Q360 400 400 330Z" fill="#ffe86a"/>'
b+='<ellipse cx="360" cy="420" rx="22" ry="12" fill="#1a0505"/><ellipse cx="440" cy="420" rx="22" ry="12" fill="#1a0505"/>'
I[664]=svg(b,d)

# 707 離したくはない: two hands tightly clasped against a dark blue night, a thin silver ring of light around them
d,b=bg([(0,'#0a1028'),(1,'#1a2a5a')])
b+=glow(400,420,200,'#8ab8ff',.35)+ring(400,420,170,'#c8d8ff',4,.7)
b+='<g fill="#e0b098" stroke="#b88a72" stroke-width="5"><path d="M120 560 Q260 520 330 440 Q380 390 420 420 Q440 450 400 480 Q340 540 160 620Z"/><path d="M680 300 Q540 340 470 420 Q420 470 380 440 Q360 410 400 380 Q460 320 640 240Z"/></g>'
I[707]=svg(b,d)

# 1137 宇宙飛行士への手紙: a paper letter floating up toward an astronaut silhouette among the stars, Earth below
d,b=bg([(0,'#020214'),(1,'#0a1440')])
b+=starsf(80,1137,800)+'<circle cx="400" cy="1000" r="420" fill="#2a6ad8"/><path d="M60 760 Q200 700 300 740 Q260 790 120 800Z M480 700 Q600 660 720 720 L700 800 L520 800Z" fill="#3ac86a" opacity=".8"/>'
b+='<g transform="rotate(-12 340 480)"><rect x="280" y="440" width="120" height="80" fill="#f4f0e8"/><path d="M280 440 L340 490 L400 440" stroke="#c8b8a0" stroke-width="4" fill="none"/></g>'
b+='<g fill="#e8eef8"><circle cx="560" cy="220" r="40"/><rect x="525" y="250" width="70" height="90" rx="20"/></g><circle cx="560" cy="220" r="26" fill="#1a2a4a"/><path d="M525 280 L480 320 M595 280 L640 250" stroke="#e8eef8" stroke-width="18" stroke-linecap="round"/>'
I[1137]=svg(b,d)

# 1631 GRIT: a hand gripping a rope in a tug of war, dust flying, warm stadium light
d,b=bg([(0,'#3a2a1a'),(1,'#8a5a2a')])
b+=glow(400,300,300,'#ffc87a',.35)+'<path d="M-10 420 Q400 380 810 440" stroke="#d8b878" stroke-width="40" fill="none"/>'+''.join(f'<path d="M{x} 400 L{x+20} 440" stroke="#a8884a" stroke-width="4"/>' for x in range(0,800,40))
b+='<g fill="#c8906a" stroke="#8a5a3a" stroke-width="6"><path d="M300 330 Q360 300 440 320 Q480 340 470 380 L460 470 Q430 500 380 490 L310 470 Q280 420 300 330Z"/></g><path d="M330 380 L440 380 M330 420 L440 420" stroke="#8a5a3a" stroke-width="5"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#c8a878" opacity=".5"/>' for x,y,r2 in [(120,620,40),(200,660,30),(620,640,50),(700,600,30),(520,700,36)])
I[1631]=svg(b,d)

# 345 Merry Christmas Mr. Lawrence: a single red flower on snow beside a barbed-wire fence, a tropical sky fading to winter
d,b=bg([(0,'#3a5a3a'),(.5,'#8a9a8a'),(1,'#e8eef0')])
b+=snow(50,345,.6)+'<rect y="560" width="800" height="240" fill="#f4f6f8"/>'
b+=''.join(f'<rect x="{80+k*160}" y="380" width="12" height="220" fill="#4a3a2a"/>' for k in range(5))+''.join(f'<path d="M80 {420+k*50} L720 {420+k*50}" stroke="#5a5a5a" stroke-width="3" stroke-dasharray="14 6"/>' for k in range(3))
b+='<path d="M420 640 L420 560" stroke="#2a5a2a" stroke-width="5"/>'+flower(420,550,34,6,'#e8102a','#ffd02a')
I[345]=svg(b,d)

# 946 Topaz Love: a large golden topaz gem glowing with a heart-shaped facet, warm light rays
d,b=bg([(0,'#3a1a0a'),(1,'#1a0a04')])
b+=rays(400,420,24,'#ffc84a',.15,8)+glow(400,420,240,'#ffb02a',.5)
b+='<polygon points="400,180 560,300 520,600 280,600 240,300" fill="#ffb02a"/><polygon points="400,180 480,300 400,600 320,300" fill="#ffd060"/><polygon points="240,300 560,300 400,340" fill="#ffe08a"/>'+heart(400,450,50,'#fff2a0','opacity=".8"')
I[946]=svg(b,d)

# 1007 July 1st: a seaside calendar page torn to July 1st fluttering above blue water
d,b=bg([(0,'#3ab8f8'),(1,'#c8f0ff')])
b+='<rect y="480" width="800" height="320" fill="#1a8ad8"/>'+''.join(sparkle(x,y,16,'#fff') for x,y in [(150,560),(300,620),(620,540),(520,680)])+cloud(180,160,1.4)
b+='<g transform="rotate(-8 420 320)"><rect x="300" y="180" width="240" height="280" fill="#fff"/><rect x="300" y="180" width="240" height="70" fill="#e8302a"/>'+txt(420,232,'JULY',44,'#fff')+txt(420,410,'1',150,'#1a1a1a')+'</g>'
I[1007]=svg(b,d)

# 1115 さくらんぼ: a pair of shiny red cherries on a pink polka-dot background
d,b=bg([(0,'#ffd0e0'),(1,'#fff0f6')])
b+=''.join(f'<circle cx="{60+(k%8)*100+(k//8%2)*50}" cy="{60+(k//8)*100}" r="14" fill="#ffffff" opacity=".7"/>' for k in range(64))
b+='<path d="M330 520 Q360 300 470 200 M500 520 Q480 330 470 200" stroke="#3a8a2a" stroke-width="10" fill="none"/><path d="M470 200 Q540 160 600 200 Q540 230 470 200Z" fill="#4ac84a"/>'
b+='<circle cx="320" cy="560" r="90" fill="#e8102a"/><circle cx="500" cy="560" r="90" fill="#d8082a"/><ellipse cx="290" cy="530" rx="22" ry="14" fill="#fff" opacity=".7"/><ellipse cx="470" cy="530" rx="22" ry="14" fill="#fff" opacity=".7"/>'
I[1115]=svg(b,d)

# 1448 Brave Shine: a sword of light planted in the ground with a burst of white-blue shine against a dark red sky
d,b=bg([(0,'#3a0a14'),(1,'#0a0a1a')])
b+=glow(400,360,260,'#9ad8ff',.5)+rays(400,360,30,'#e8f8ff',.18,6)+'<rect y="640" width="800" height="160" fill="#140a14"/>'
b+='<path d="M388 200 L412 200 L412 640 L400 680 L388 640Z" fill="#f4faff"/><rect x="340" y="560" width="120" height="16" fill="#c8a24a"/><rect x="390" y="576" width="20" height="60" fill="#5a3a2a"/>'
I[1448]=svg(b,d)

# 1509 BOY: a young boy silhouette on a bicycle with a paper crown, a yellow-red pop-art sky
d,b=bg([(0,'#ffd02a'),(1,'#ff6a3a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="#fff" opacity=".35"/>' for x in range(30,800,60) for y in range(30,400,60))+'<rect y="600" width="800" height="200" fill="#2a2a3a"/>'
b+=''.join(ring(x,560,60,'#000',10) for x in (300,520))+'<path d="M300 560 L380 460 L520 560 M380 460 L480 460 L520 560 M380 460 L360 420" stroke="#000" stroke-width="10" fill="none"/>'+'<g fill="#000"><circle cx="420" cy="320" r="26"/><path d="M400 350 L440 350 L470 460 L390 460Z"/></g><path d="M396 296 L404 270 L420 290 L436 270 L444 296Z" fill="#ffd02a"/>'
I[1509]=svg(b,d)

# 1609 BOYZ: six bold silhouettes in a row under stage lights, a graffiti wall behind
d,b=bg([(0,'#0a0a10'),(1,'#2a2a3a')])
b+=''.join(f'<polygon points="{x},0 {x-90},700 {x+90},700" fill="{c}" opacity=".18"/>' for x,c in [(130,'#ff3a6a'),(400,'#3ad8ff'),(670,'#ffd02a')])+'<rect y="660" width="800" height="140" fill="#14141c"/>'
b+=''.join(figure(x,680,h,'#000') for x,h in [(120,300),(230,320),(340,290),(460,330),(570,300),(680,310)])+txt(400,170,'BOYZ',110,'#ff3a6a',900,op=.8)
I[1609]=svg(b,d)

# 1773 太陽がくれた季節: young people's silhouettes running along a summer beach under a huge orange sun, early-70s faded palette
d,b=bg([(0,'#f0a060'),(1,'#f8e0b0')])
b+=hinomaru_sun(400,320,170,'#ffe0a0',.9)+'<rect y="460" width="800" height="100" fill="#d8a080"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#e8c898"/>'
b+=''.join(figure(x,660,h,'#5a3020',pose=p) for x,h,p in [(220,220,'up'),(360,230,'wave'),(500,215,'up'),(620,225,'stand')])
I[1773]=svg(b,d)

# 828 End Of Sorrow: rain stopping over a dark lake as one break of light opens in the clouds
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a5a')])
b+=cloud(220,200,2.4,'#2a2a3a')+cloud(600,180,2.6,'#2a2a3a')+'<polygon points="380,240 440,240 560,800 260,800" fill="#e8f0ff" opacity=".2"/>'+rain(50,828,'#c8d8f0',.25)
b+='<rect y="560" width="800" height="240" fill="#14141e"/><ellipse cx="410" cy="600" rx="120" ry="10" fill="#e8f0ff" opacity=".4"/>'
I[828]=svg(b,d)

# 839 Missing You: a phone booth glowing alone on a winter night street, snow falling
d,b=bg([(0,'#0a1028'),(1,'#1a2448')])
b+=snow(80,839)+'<rect y="620" width="800" height="180" fill="#e8eef8"/>'
b+='<rect x="320" y="240" width="160" height="400" fill="#2a8a4a"/><rect x="340" y="280" width="120" height="320" fill="#ffe8a8"/>'+glow(400,440,180,'#ffe8a8',.35)+'<rect x="380" y="380" width="40" height="60" fill="#3a3a3a"/>'+'<path d="M320 240 L480 240 L470 220 L330 220Z" fill="#fff"/>'
I[839]=svg(b,d)

# 1256 恋のABO: four colourful blood-type letter bubbles with hearts, a playful pop background
d,b=bg([(0,'#ff8ad8'),(1,'#ffd8f0')])
for (x,y,t,c) in [(240,280,'A','#ff4a4a'),(560,280,'B','#3a8af8'),(240,560,'O','#ffb02a'),(560,560,'AB','#8a4af8')]:
    b+=f'<circle cx="{x}" cy="{y}" r="110" fill="{c}"/>'+txt(x,y+40,t,110 if len(t)==1 else 90,'#fff',900)
b+=heart(400,420,50,'#fff')
I[1256]=svg(b,d)

# 1308 桜の木になろう: a young cherry tree growing on a school field, a ribbon tied to a branch, petals in the air
d,b=bg([(0,'#a8d8ff'),(1,'#f4faff')])
b+='<path d="M-10 600 Q400 560 810 600 L810 810 L-10 810Z" fill="#9ad06a"/><path d="M400 640 Q392 500 404 380" stroke="#6a4a3a" stroke-width="22" fill="none"/><path d="M400 460 L320 400 M402 420 L480 360" stroke="#6a4a3a" stroke-width="10"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#ffb8d0"/>' for x,y,r2 in [(400,300,90),(310,370,70),(490,340,80),(350,250,60),(460,250,60)])+''.join(sakura(x,y,s) for x,y,s in [(400,300,1.2),(310,370,1),(490,340,1),(350,250,.8),(460,250,.8)])+'<path d="M320 404 L300 450 M320 404 L340 452" stroke="#e8302a" stroke-width="6"/>'+petals(20,1308)
I[1308]=svg(b,d)

# 1763 CHA CHA CHA: a dancing couple silhouette on a disco floor with a mirror ball and pink 80s neon
d,b=bg([(0,'#2a0a3a'),(1,'#6a1a6a')])
b+=''.join(f'<polygon points="400,120 {x},800 {x+60},800" fill="{c}" opacity=".15"/>' for x,c in [(60,'#ff4fa0'),(300,'#4ad8ff'),(560,'#ffd02a')])
b+='<circle cx="400" cy="120" r="60" fill="#c8c8d8"/>'+''.join(f'<rect x="{352+(k%6)*16}" y="{72+(k//6)*16}" width="14" height="14" fill="#e8e8f8"/>' for k in range(36))
b+=figure(330,700,310,'#0a0410',pose='up')+figure(480,700,300,'#0a0410',pose='reachL')+'<path d="M455 520 Q490 600 540 640 L420 640Z" fill="#0a0410"/>'
I[1763]=svg(b,d)

# 1857 Evening Primrose: pale yellow evening primrose flowers opening at dusk beside a riverbank
d,b=bg([(0,'#3a3a6a'),(.6,'#c8a0b8'),(1,'#f8d8b8')])
b+='<rect y="520" width="800" height="100" fill="#7a7aa8" opacity=".7"/><path d="M-10 600 Q400 560 810 600 L810 810 L-10 810Z" fill="#2a3a2a"/>'
for x,y,s in [(220,560,1),(360,500,1.2),(520,540,1.1),(640,590,.9)]: b+=f'<path d="M{x} {y} L{x+4} {y+260}" stroke="#3a6a3a" stroke-width="6"/>'+flower(x,y,50*s,4,'#fff6a0','#e8c84a',petal=.8)
I[1857]=svg(b,d)

# 143 よこはま・たそがれ: a harbour at dusk with a cargo ship, gulls and a lamp post, retro faded tones
d,b=bg([(0,'#5a4a7a'),(.6,'#e89a6a'),(1,'#f8c88a')])
b+='<rect y="460" width="800" height="340" fill="#4a4a6a"/><path d="M380 440 L680 440 L660 480 L400 480Z" fill="#2a2a3a"/><rect x="460" y="380" width="80" height="60" fill="#2a2a3a"/><rect x="560" y="340" width="20" height="100" fill="#2a2a3a"/>'
b+='<rect x="140" y="300" width="10" height="380" fill="#1a1a24"/><circle cx="145" cy="290" r="22" fill="#ffd28a"/>'+glow(145,290,60,'#ffd28a',.6)+bird(300,220,1.4,'#fff',3)+bird(360,260,1,'#fff',3)+'<rect y="680" width="800" height="120" fill="#2a2a34"/>'
I[143]=svg(b,d)

# 241 やさしさに包まれたなら: a sleeping child wrapped in a soft blanket of clouds, morning light streaming in
d,b=bg([(0,'#ffe8c8'),(1,'#d8ecff')])
b+=rays(400,120,20,'#fff',.25,10)+glow(400,140,140,'#fff6d8',.7)
b+=cloud(400,560,4,'#fff')+'<circle cx="330" cy="470" r="44" fill="#f0c8a8"/><path d="M286 462 Q330 400 374 462 Q330 440 286 462Z" fill="#5a3a2a"/><path d="M312 478 Q318 484 324 478 M338 478 Q344 484 350 478" stroke="#5a3a2a" stroke-width="4" fill="none"/>'+cloud(600,580,2.2,'#fff')+'<path d="M290 520 Q400 480 560 520" stroke="#ffd0e0" stroke-width="40" fill="none" stroke-linecap="round"/>'
I[241]=svg(b,d)

# 242 ルージュの伝言: a lipstick message written on a bathroom mirror, a red lipstick lying below
d,b=bg([(0,'#d8e8f0'),(1,'#a8c0d0')])
b+='<rect x="140" y="140" width="520" height="420" rx="30" fill="#e8f4fa" stroke="#c8b08a" stroke-width="16"/><path d="M220 240 Q280 200 330 260 T460 250 T600 230" stroke="#d8102a" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M240 340 Q300 310 360 360 T520 330" stroke="#d8102a" stroke-width="10" fill="none" stroke-linecap="round"/>'+heart(560,420,36,'#d8102a')
b+='<rect y="600" width="800" height="200" fill="#f4f4f6"/><g transform="rotate(-20 400 660)"><rect x="330" y="640" width="120" height="40" rx="6" fill="#c8a24a"/><path d="M450 646 L510 646 L520 674 L450 674Z" fill="#d8102a"/></g>'
I[242]=svg(b,d)

# 665 GOLD: a golden trophy-like crown of light on a black stage, gold confetti raining
d,b=bg([(0,'#0a0804'),(1,'#2a200a')])
b+=confetti(60,665,['#ffd02a','#ffe88a','#e8b02a'])+glow(400,420,220,'#ffd02a',.4)
b+='<path d="M280 360 L520 360 L500 520 Q400 580 300 520Z" fill="#e8b02a"/><path d="M280 380 Q200 380 220 460 Q240 500 300 500 M520 380 Q600 380 580 460 Q560 500 500 500" stroke="#e8b02a" stroke-width="16" fill="none"/><rect x="370" y="560" width="60" height="70" fill="#c8901a"/><rect x="320" y="630" width="160" height="40" fill="#e8b02a"/>'
I[665]=svg(b,d)

# 704 サヨナラは今もこの胸に居ます: a pressed flower inside an open letter on a windowsill, rain on the glass
d,b=bg([(0,'#7a8aa8'),(1,'#b8c8d8')])
b+=rain(40,704,'#e8f0ff',.4)+'<rect y="560" width="800" height="240" fill="#e8dcc8"/>'
b+='<path d="M200 520 L400 560 L600 520 L600 700 L400 740 L200 700Z" fill="#fbf6ea" stroke="#c8b898" stroke-width="4"/><path d="M400 560 L400 740" stroke="#c8b898" stroke-width="3"/>'+''.join(f'<path d="M230 {590+k*26} L370 {610+k*26}" stroke="#8a8aa8" stroke-width="3"/>' for k in range(4))
b+='<path d="M500 690 L520 600" stroke="#6a8a5a" stroke-width="4"/>'+flower(520,598,26,5,'#c8a0d8','#ffe08a')
I[704]=svg(b,d)

# 1049 大きな古時計: a tall old grandfather clock in a wooden room, its pendulum stopped
d,b=bg([(0,'#4a2a1a'),(1,'#2a160a')])
b+=glow(400,300,240,'#ffc87a',.25)+'<rect y="700" width="800" height="100" fill="#3a2010"/>'
b+='<rect x="300" y="120" width="200" height="580" fill="#6a3a1a"/><path d="M300 120 Q400 60 500 120Z" fill="#5a2a10"/><circle cx="400" cy="230" r="76" fill="#f4ead0" stroke="#c8a24a" stroke-width="10"/>'+''.join(f'<circle cx="{400+60*math.cos(math.radians(a)):.0f}" cy="{230+60*math.sin(math.radians(a)):.0f}" r="4" fill="#3a2a1a"/>' for a in range(0,360,30))
b+='<path d="M400 230 L400 180 M400 230 L440 250" stroke="#1a1a1a" stroke-width="6"/><rect x="340" y="340" width="120" height="300" fill="#3a1a0a"/><path d="M400 350 L400 560" stroke="#c8a24a" stroke-width="5"/><circle cx="400" cy="580" r="30" fill="#c8a24a"/>'
I[1049]=svg(b,d)

# 1052 Point of No Return: two figures on a railway track at night, a red signal light and the rails disappearing
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+=starsf(40,1052,400)+'<path d="M340 400 L460 400 L760 800 L40 800Z" fill="#1a1418"/><path d="M390 400 L180 800 M410 400 L620 800" stroke="#8a8a96" stroke-width="6"/>'+''.join(f'<path d="M{400-20-k*40} {420+k*70} L{400+20+k*40} {420+k*70}" stroke="#4a3a30" stroke-width="10"/>' for k in range(6))
b+='<rect x="600" y="200" width="16" height="300" fill="#2a2a2a"/><rect x="580" y="180" width="56" height="90" rx="10" fill="#1a1a1a"/><circle cx="608" cy="210" r="16" fill="#ff2a2a"/>'+glow(608,210,50,'#ff2a2a',.6)+figure(330,700,220,'#000')+figure(470,700,230,'#000')
I[1052]=svg(b,d)

# 1243 Keep the faith: a fist raised high holding a burning torch against a dark storm
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a3a')])
b+=cloud(200,200,2.4,'#2a2a3a')+cloud(620,240,2.2,'#2a2a3a')+bolt([(700,80),(660,180),(690,200),(640,300)],'#e8e8ff',6)
b+='<path d="M380 800 L370 520 Q370 480 400 470 Q440 470 440 520 L430 800Z" fill="#000"/><rect x="390" y="300" width="20" height="180" fill="#6a4a2a"/><path d="M400 300 Q340 240 380 180 Q400 220 410 160 Q460 220 430 260 Q450 280 400 300Z" fill="#ff8a2a"/><path d="M400 290 Q380 250 400 220 Q420 250 400 290Z" fill="#ffe06a"/>'+glow(400,240,120,'#ffa02a',.5)
I[1243]=svg(b,d)

# 1309 風は吹いている: a girl's silhouette on a bare coastal hill facing the wind, a single fallen-leaf seedling sprouting at her feet
d,b=bg([(0,'#8a9ab0'),(1,'#d8e0e8')])
b+=''.join(f'<path d="M{-50+k*120} {180+k*40} Q{200+k*120} {150+k*40} {450+k*120} {190+k*40}" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/>' for k in range(5))
b+='<path d="M-10 620 Q300 540 600 600 Q700 620 810 600 L810 810 L-10 810Z" fill="#6a7a6a"/>'+figure(380,600,300,'#1a1a24')+'<path d="M352 330 Q300 340 270 320" stroke="#1a1a24" stroke-width="12" fill="none"/><path d="M440 600 L440 570 M440 580 Q460 560 470 570 M440 576 Q420 556 412 566" stroke="#4ac84a" stroke-width="5" fill="none"/>'
I[1309]=svg(b,d)

# 396 Dear Friend: two girls' silhouettes sitting back to back under a big tree at golden hour
d,b=bg([(0,'#f8b07a'),(1,'#ffe8c8')])
b+=hinomaru_sun(600,420,90,'#fff4d0',.8)+'<rect y="560" width="800" height="240" fill="#a8b86a"/>'+tree(260,580,420,'#3a5a2a',396)
b+='<g fill="#3a2a1a"><circle cx="380" cy="470" r="24"/><path d="M356 494 Q380 486 400 494 L404 580 L350 580Z"/><circle cx="440" cy="470" r="24"/><path d="M420 494 Q440 486 464 494 L470 580 L416 580Z"/></g>'
I[396]=svg(b,d)

# 666 RED: a single red guitar string vibrating across a black field, a red spotlight
d,b=bg([(0,'#050505'),(1,'#1a0505')])
b+=glow(400,400,280,'#e8102a',.4)+'<path d="M40 400 Q200 340 400 400 T760 400" stroke="#ff1a3a" stroke-width="10" fill="none"/><path d="M40 400 Q200 460 400 400 T760 400" stroke="#ff1a3a" stroke-width="4" fill="none" opacity=".5"/>'
b+='<circle cx="40" cy="400" r="14" fill="#c8c8d0"/><circle cx="760" cy="400" r="14" fill="#c8c8d0"/>'+txt(400,620,'RED',120,'#e8102a',900,op=.9)
I[666]=svg(b,d)

# 869 forbidden lover: two silhouettes reaching toward each other through a wrought-iron gate under a pale moon
d,b=bg([(0,'#1a1028'),(1,'#3a2a4a')])
b+=moon(400,180,70)+'<rect y="640" width="800" height="160" fill="#140a1a"/>'+''.join(f'<rect x="{x}" y="260" width="12" height="400" fill="#0a0a0a"/><path d="M{x-6} 270 L{x+6} 240 L{x+18} 270Z" fill="#0a0a0a"/>' for x in range(330,480,30))+'<rect x="320" y="380" width="170" height="12" fill="#0a0a0a"/>'
b+=figure(220,660,300,'#000',pose='reach')+figure(580,660,290,'#000',pose='reachL')
I[869]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
