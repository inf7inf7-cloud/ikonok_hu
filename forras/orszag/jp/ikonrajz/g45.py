import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 45. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 144 千曲川: a wide mountain river at dusk with a lone figure on its bank and willows, 1975 enka
d,b=bg([(0,'#5a5a8a'),(1,'#ffb08a')])
b+=hills(420,70,'#5a4a6a',144,4)+'<path d="M300 440 Q200 520 380 600 Q560 680 300 800 L700 800 Q760 680 600 580 Q480 500 500 440Z" fill="#8aa0c8"/><path d="M0 440 L800 440 L800 800 L0 800Z" fill="#4a5a3a" opacity=".0"/>'
b+=''.join(f'<path d="M{x} 600 Q{x+10} 480 {x+40} 420" stroke="#2a3a2a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x+40} 420 Q{x+40+dx} 480 {x+30+dx} 560" stroke="#3a5a3a" stroke-width="5" fill="none"/>' for dx in (-30,-10,10,30)) for x in (100,640))
b+=figure(220,640,160,'#1a1a24')
I[144]=svg(b,d)

# 1253 Ask Yourself: a figure facing a tall mirror in an empty room, the reflection lit differently, 2018
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+='<rect y="600" width="800" height="200" fill="#2a2a34"/><rect x="420" y="140" width="240" height="460" fill="#8ab0d8" stroke="#c8c8d0" stroke-width="12"/>'+glow(540,370,140,'#cfe6ff',.4)
b+=figure(300,620,320,'#000')+figure(540,560,260,'#1a3a5a')
I[1253]=svg(b,d)

# 10 リンゴ追分: apple blossoms and red apples on a branch in a Tsugaru orchard under a spring moon, 1952
d,b=bg([(0,'#3a3a6a'),(1,'#d8b8d8')])
b+=moon(620,160,60)+'<path d="M0 300 Q300 340 560 480" stroke="#3a2a1a" stroke-width="18" fill="none"/>'+''.join(flower(x,y,26,5,'#fff4f8','#ffd02a',x) for x,y in [(120,300),(220,320),(330,360),(430,410),(180,250)])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="30" fill="#e8102a"/><path d="M{x} {y-30} l4 -14" stroke="#3a2a1a" stroke-width="4"/>' for x,y in [(280,400),(480,470)])+'<rect y="600" width="800" height="200" fill="#4a5a3a"/>'
I[10]=svg(b,d)

# 161 雪椿: a red camellia blooming bright through heavy snow on a dark branch, 1987 enka
d,b=bg([(0,'#4a5468'),(1,'#c8d0dc')])
b+=snow(100,161)+'<path d="M0 520 Q300 480 520 380 Q620 330 800 320" stroke="#2a2a1a" stroke-width="16" fill="none"/><path d="M0 510 Q300 470 520 370" stroke="#f4f6ff" stroke-width="8" fill="none"/>'
b+=''.join(f'<path d="M{x} {y} q30 -20 50 -40 q-20 40 -50 40Z" fill="#2a4a2a"/>' for x,y in [(260,480),(560,360),(680,330)])+flower(420,420,70,5,'#c8102a','#ffd02a',10,.65)+'<path d="M380 370 Q420 350 460 370" stroke="#fff" stroke-width="10" fill="none"/>'
I[161]=svg(b,d)

# 198 氷の世界: a frozen window with icicles and an apple on the sill, a cold neon 1973 folk-rock
d,b=bg([(0,'#a8c8e8'),(1,'#e8f4ff')])
b+='<rect x="120" y="100" width="560" height="440" fill="#d8ecff"/>'+''.join(f'<path d="M{x} {y} L{x+40} {y+20} M{x+20} {y-20} L{x+20} {y+40}" stroke="#fff" stroke-width="4"/>' for x,y in [(200,200),(480,260),(320,420),(560,440)])
b+='<rect x="120" y="100" width="560" height="440" fill="none" stroke="#5a6a8a" stroke-width="18"/>'+''.join(f'<path d="M{x} 110 L{x+10} {180+(x%3)*30} L{x+20} 110Z" fill="#e8f8ff" stroke="#a8c8e8" stroke-width="2"/>' for x in range(140,680,40))
b+='<rect x="80" y="540" width="640" height="34" fill="#5a6a8a"/><rect y="574" width="800" height="226" fill="#3a4a6a"/><circle cx="400" cy="510" r="34" fill="#c8102a"/><path d="M400 476 l4 -14" stroke="#3a2a1a" stroke-width="4"/>'
I[198]=svg(b,d)

# 924 BEAT YOUR HEART: a pulsing heart-shaped drum with sticks mid-hit and shock rings, 90s boy group
d,b=bg([(0,'#1a0a3a'),(1,'#e83a5a')])
b+=''.join(ring(400,440,r,'#fff',5,1-r/400) for r in (150,220,290))+heart(400,450,110,'#e8102a')+'<ellipse cx="400" cy="400" rx="90" ry="20" fill="#f4e8d0" opacity=".5"/>'
b+='<path d="M220 160 L360 380 M580 160 L440 380" stroke="#f4e8d0" stroke-width="16" stroke-linecap="round"/>'
I[924]=svg(b,d)

# 1831 秘密戦隊ゴレンジャー: five coloured stars in a V formation shooting across a dramatic sky, 70s tokusatsu
d,b=bg([(0,'#1a2a6a'),(1,'#e8803a')])
b+=rays(400,600,18,'#fff',.15,10)
for c,x,y in [('#e8302a',400,260),('#1a6aff',300,340),('#ffd02a',500,340),('#ff6aa8',200,420),('#3ad85a',600,420)]:
  b+=f'<path d="M{x} {y+20} L{x} 800" stroke="{c}" stroke-width="10" opacity=".4"/>'+star5(x,y,44,c)+glow(x,y,50,c,.5)
I[1831]=svg(b,d)

# 1870 Look Back Again: a girl on a bicycle glancing over her shoulder on a long coastal road, 2001 pop
d,b=bg([(0,'#3ab0ff'),(1,'#e0f8ff')])
b+='<rect y="440" width="800" height="160" fill="#1a8ad8"/><path d="M0 600 L800 560 L800 800 L0 800Z" fill="#c8c0b0"/><path d="M0 680 L800 640" stroke="#fff" stroke-width="6" stroke-dasharray="40 30"/>'
b+=ring(300,680,50,'#1a1a2a',8)+ring(460,670,50,'#1a1a2a',8)+'<path d="M300 680 L370 610 L460 670 M370 610 L400 590" stroke="#1a1a2a" stroke-width="8" fill="none"/>'+figure(380,620,200,'#1a1a2a',hair='#1a1a2a')
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="#fff" opacity=".7"/>' for x,y in [(140,700),(80,710)])
I[1870]=svg(b,d)

# 23 ウナ・セラ・ディ東京: a dusky Tokyo with a glowing Tokyo Tower and a couple on a bridge, 1964 kayō
d,b=bg([(0,'#3a2a6a'),(1,'#ff9a7a')])
b+=skyline(560,'#2a1a3a',23,60,220,'#ffd27a',60)+tokyo_tower(560,560,380)+'<rect y="560" width="800" height="240" fill="#2a3a5a"/>'
b+='<path d="M0 600 Q400 540 800 600" stroke="#1a1424" stroke-width="20" fill="none"/>'+figure(260,580,140,'#0a0a14')+figure(310,580,130,'#0a0a14',hair='#0a0a14')
I[23]=svg(b,d)

# 53 朝のくちづけ: morning sunlight through lace curtains onto two coffee cups and a single flower, 1968
d,b=bg([(0,'#fff4e0'),(1,'#f8e8d0')])
b+=rays(640,60,14,'#fff',.4,30)+''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="#f0d8c0" stroke-width="3"/>' for x in range(40,800,60) for y in range(40,360,60))
b+='<rect y="520" width="800" height="280" fill="#e8d0b0"/><path d="M260 440 L340 440 L330 520 L270 520Z M460 440 L540 440 L530 520 L470 520Z" fill="#fff"/><path d="M400 520 L400 400" stroke="#3a7a3a" stroke-width="5"/>'+flower(400,390,30,5,'#ff8ab0','#ffd02a')+heart(400,300,20,'#ff8ab0',' opacity=".6"')
I[53]=svg(b,d)

# 1024 歩いてる: a group of girls' silhouettes walking forward together on a long path at sunset
d,b=bg([(0,'#ff8a5a'),(1,'#ffe0b0')])
b+='<circle cx="400" cy="440" r="80" fill="#fff0b0"/><path d="M0 480 L800 480 L800 800 L0 800Z" fill="#7a5a4a"/><path d="M380 480 L160 800 L640 800 L420 480Z" fill="#a8806a"/>'
b+=''.join(figure(x,y,s,'#2a1418',hair='#2a1418') for x,y,s in [(300,700,200),(380,720,220),(460,700,200),(540,690,190),(240,690,190)])
I[1024]=svg(b,d)

# 1745 Deep in your heart: a heart-shaped keyhole glowing at the bottom of a deep blue ocean, 2006 ballad
d,b=bg([(0,'#0a3a7a'),(1,'#020a24')])
b+=''.join(f'<path d="M{x} 0 L{x+40} 600" stroke="#5aa8ff" stroke-width="30" opacity=".08"/>' for x in range(0,800,100))+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#8ad0ff" stroke-width="2" opacity=".5"/>' for x,y,r in [(200,300,10),(220,250,6),(600,200,8),(580,160,5)])
b+=heart(400,560,90,'#ff4a8a')+glow(400,560,140,'#ff4a8a',.4)+'<circle cx="400" cy="540" r="16" fill="#1a0a14"/><path d="M392 550 L380 600 L420 600 L408 550Z" fill="#1a0a14"/>'
I[1745]=svg(b,d)

# 1813 酒場にて: a woman singing alone at a dim tavern with a jukebox glow, 1974 kayō
d,b=bg([(0,'#1a1014'),(1,'#3a2024')])
b+='<rect y="560" width="800" height="240" fill="#4a2a1a"/><path d="M540 560 L540 360 Q540 280 620 280 Q700 280 700 360 L700 560Z" fill="#c8702a"/><path d="M560 360 Q560 300 620 300 Q680 300 680 360 L680 440 L560 440Z" fill="#ffd27a"/>'+glow(620,400,120,'#ffd27a',.5)+''.join(f'<rect x="570" y="{y}" width="100" height="10" fill="#ff6a3a"/>' for y in (460,490,520))
b+=figure(300,600,300,'#0a0a0a',hair='#0a0a0a')+'<rect x="330" y="400" width="8" height="200" fill="#3a3a3a"/>'
I[1813]=svg(b,d)

# 1832 ジャッカー電撃隊: four glowing playing-card suit symbols charged with lightning, 70s tokusatsu
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=bolt([(400,60),(360,300),(440,320),(380,560)],'#ffd02a',10,.6)
b+=heart(220,240,60,'#e8302a')+'<path d="M580 180 L640 260 L580 340 L520 260Z" fill="#1a6aff"/>'+'<circle cx="200" cy="560" r="36" fill="#3ad85a"/><circle cx="160" cy="610" r="36" fill="#3ad85a"/><circle cx="240" cy="610" r="36" fill="#3ad85a"/><rect x="192" y="610" width="16" height="70" fill="#3ad85a"/>'
b+='<path d="M600 520 Q660 600 600 640 Q580 650 600 620 Q540 650 540 600 Q560 560 600 520Z" fill="#c8c8d8"/><path d="M600 520 Q540 600 540 610 Q560 650 600 620" fill="#c8c8d8"/><rect x="592" y="620" width="16" height="60" fill="#c8c8d8"/>'
I[1832]=svg(b,d)

# 145 ふるさと: a thatched farmhouse with smoke rising from the chimney among autumn rice fields, 1973 enka
d,b=bg([(0,'#e8a86a'),(1,'#f8e4c0')])
b+=hills(400,60,'#8a8a6a',145,4)+'<rect y="440" width="800" height="360" fill="#d8b860"/>'+''.join(f'<path d="M0 {y} L800 {y}" stroke="#c8a040" stroke-width="3"/>' for y in range(470,800,40))
b+='<rect x="280" y="400" width="240" height="140" fill="#8a6a4a"/><path d="M240 410 L400 290 L560 410Z" fill="#b8985a"/><rect x="340" y="460" width="50" height="50" fill="#ffd27a"/>'+''.join(f'<circle cx="{460+k*10}" cy="{280-k*40}" r="{16+k*6}" fill="#fff" opacity="{.5-k*.1}"/>' for k in range(4))
I[145]=svg(b,d)

# 305 夢で逢えたら: two silhouettes reaching for each other across a dreamy cloud bridge under the moon, doo-wop
d,b=bg([(0,'#1a1a4a'),(1,'#6a5aa8')])
b+=starsf(60,305,500)+moon(400,180,60)+cloud(200,480,2.0,'#c8c0f0')+cloud(600,480,2.0,'#c8c0f0')
b+=figure(250,440,200,'#1a1424')+figure(550,440,200,'#1a1424',hair='#1a1424')+'<path d="M290 330 L360 310 M510 330 L440 310" stroke="#1a1424" stroke-width="12" stroke-linecap="round"/>'+sparkle(400,310,20,'#fff4c8')
I[305]=svg(b,d)

# 316 雨宿り: two strangers sheltering from the rain under a small shop awning, 1983 ballad
d,b=bg([(0,'#4a5a6a'),(1,'#8a9aaa')])
b+=rain(90,316,'#e8f0ff',.4)+'<rect x="140" y="200" width="520" height="440" fill="#5a4a40"/><path d="M100 240 L700 240 L660 320 L140 320Z" fill="#c8402a"/>'+''.join(f'<path d="M{x} 240 L{x+40} 320" stroke="#f4f0e8" stroke-width="20"/>' for x in range(140,680,80))
b+='<rect x="300" y="380" width="200" height="140" fill="#ffd27a" opacity=".6"/><rect y="640" width="800" height="160" fill="#3a3a44"/>'+figure(260,660,250,'#0a0a14')+figure(540,660,240,'#0a0a14',hair='#0a0a14')
I[316]=svg(b,d)

# 418 スマイル・フォー・ミー: a big yellow smiley balloon tied to a girl's wrist on a sunny day, idol pop
d,b=bg([(0,'#7ac8ff'),(1,'#fff0d8')])
b+='<circle cx="460" cy="260" r="110" fill="#ffd82a"/><circle cx="420" cy="230" r="12" fill="#3a2a1a"/><circle cx="500" cy="230" r="12" fill="#3a2a1a"/><path d="M410 290 Q460 340 510 290" stroke="#3a2a1a" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+='<path d="M460 370 Q420 460 360 520" stroke="#5a5a5a" stroke-width="3" fill="none"/><rect y="640" width="800" height="160" fill="#8ac86a"/>'+figure(330,660,230,'#3a2a3a',pose='up',hair='#3a2a3a')
I[418]=svg(b,d)

# 1726 THANK YOU 4 EVERY DAY EVERY BODY: a sea of thank-you hearts drifting up from a crowd with light sticks
d,b=bg([(0,'#3a1a6a'),(1,'#ff8ad0')])
b+=''.join(heart(x,y,s,c,' opacity=".8"') for x,y,s,c in [(160,200,30,'#fff'),(300,140,40,'#ffd0e8'),(480,180,34,'#fff'),(620,120,26,'#ffd0e8'),(400,300,24,'#fff'),(240,340,20,'#fff'),(560,320,28,'#ffd0e8')])
b+='<rect y="600" width="800" height="200" fill="#1a0a2a"/>'+''.join(f'<path d="M{x} 640 L{x+10} {520+(x%5)*8}" stroke="{["#3affe8","#ffd02a","#ff4fd0"][(x//70)%3]}" stroke-width="10" stroke-linecap="round"/>'+f'<circle cx="{x}" cy="660" r="22" fill="#000"/>' for x in range(40,800,70))
I[1726]=svg(b,d)

# 11 ひばりの佐渡情話: a round wooden tub boat on the sea off Sado island with a woman's silhouette, 1962
d,b=bg([(0,'#5a7ab8'),(1,'#e8d8c0')])
b+='<path d="M440 420 Q560 340 720 400 L800 420 L800 440 L440 440Z" fill="#4a5a6a"/><rect y="440" width="800" height="360" fill="#3a6aa8"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(80,520),(560,500),(240,700),(620,680)])
b+='<ellipse cx="320" cy="580" rx="120" ry="34" fill="#8a5a2a"/><path d="M200 580 L210 620 Q320 660 430 620 L440 580Z" fill="#6a3a1a"/>'+figure(320,590,180,'#1a1a24',hair='#1a1a24')+'<path d="M360 500 L460 640" stroke="#5a3a2a" stroke-width="6"/>'
I[11]=svg(b,d)

# 46 北国の街: a snowy northern town street with warm lamps and two students walking side by side, 1965
d,b=bg([(0,'#2a3a5a'),(1,'#7a8aaa')])
b+=snow(90,46)+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{600-y}" fill="#4a3a34"/><path d="M{x-10} {y} L{x+w/2} {y-50} L{x+w+10} {y}Z" fill="#f4f6ff"/><rect x="{x+20}" y="{y+40}" width="30" height="30" fill="#ffd27a"/>' for x,y,w in [(40,380,160),(600,360,180)])
b+='<rect y="600" width="800" height="200" fill="#e8eef8"/>'+figure(360,640,200,'#1a1a2a')+figure(440,640,190,'#1a1a2a',hair='#1a1a2a')
I[46]=svg(b,d)

# 51 男はつらいよ: a battered trunk and a worn hat left on a grassy riverbank at sunset, the eternal wanderer
d,b=bg([(0,'#e89a6a'),(1,'#f8e0b8')])
b+='<rect y="480" width="800" height="120" fill="#7a9ac8"/><path d="M0 560 Q400 520 800 580 L800 800 L0 800Z" fill="#8aa86a"/>'
b+='<rect x="280" y="560" width="200" height="120" rx="8" fill="#8a5a2a"/><rect x="280" y="600" width="200" height="12" fill="#5a3a1a"/><rect x="350" y="540" width="60" height="24" rx="8" fill="none" stroke="#5a3a1a" stroke-width="8"/>'
b+='<ellipse cx="560" cy="660" rx="70" ry="16" fill="#5a4a3a"/><path d="M510 660 Q520 610 560 610 Q600 610 610 660Z" fill="#5a4a3a"/><rect x="512" y="644" width="96" height="10" fill="#2a1a14"/>'+bird(240,200,26,'#3a2a2a')
I[51]=svg(b,d)

# 343 君に、胸キュン。: a heart squeezed by a pastel synth keyboard ribbon on a summer beach, 1983 techno-pop
d,b=bg([(0,'#7ad8ff'),(1,'#fff0d8')])
b+='<rect y="500" width="800" height="100" fill="#3ab0e8"/><path d="M0 600 Q400 560 800 600 L800 800 L0 800Z" fill="#f4dca0"/>'
b+=heart(400,360,110,'#ff6aa8')+'<rect x="180" y="380" width="440" height="60" rx="10" fill="#f4f4f4" transform="rotate(-8 400 410)"/>'+''.join(f'<rect x="{x}" y="386" width="12" height="40" fill="#1a1a1a" transform="rotate(-8 400 410)"/>' for x in range(200,600,34))
I[343]=svg(b,d)

# 568 あなたを愛したい: a girl holding a single red rose to her heart by a window full of autumn light, 80s idol
d,b=bg([(0,'#f8c89a'),(1,'#f4e8d8')])
b+='<rect x="440" y="100" width="300" height="400" fill="#ffe8c0"/><rect x="440" y="100" width="300" height="400" fill="none" stroke="#a8806a" stroke-width="12"/>'+''.join(f'<path d="M{x} {y} q14 -20 28 0 q-14 20 -28 0Z" fill="#e8802a" transform="rotate({x} {x} {y})"/>' for x,y in [(500,200),(620,300),(560,400)])
b+='<rect y="600" width="800" height="200" fill="#a8806a"/>'+figure(260,620,320,'#3a2a2a',hair='#3a2a2a')+rose(270,400,.6,0)
I[568]=svg(b,d)

# 925 GENERATION GAP: an old radio and a modern smartphone facing each other across a crack, boy group
d,b=bg([(0,'#e8e0d0'),(1,'#c8c0b0')])
b+='<path d="M400 0 L380 200 L420 400 L380 600 L400 800" stroke="#5a5a5a" stroke-width="10" fill="none"/>'
b+='<rect x="80" y="320" width="240" height="180" rx="20" fill="#8a5a2a"/><circle cx="160" cy="410" r="50" fill="#c8a870"/>'+''.join(f'<circle cx="160" cy="410" r="{r}" fill="none" stroke="#8a5a2a" stroke-width="3"/>' for r in (20,36))+'<rect x="230" y="370" width="70" height="20" fill="#f4e8c0"/><circle cx="265" cy="440" r="16" fill="#5a3a1a"/>'
b+='<rect x="520" y="260" width="160" height="300" rx="24" fill="#1a1a1a"/><rect x="534" y="290" width="132" height="240" fill="#3ab0ff"/>'+''.join(f'<rect x="{x}" y="{y}" width="30" height="30" rx="6" fill="#fff" opacity=".7"/>' for x in (548,590,632) for y in (310,360,410))
I[925]=svg(b,d)

# 15 見上げてごらん夜の星を: a boy and a girl lying on a grassy hill gazing up at a huge starry sky, 1963
d,b=bg([(0,'#02061a'),(1,'#1a2a5a')])
b+=starsf(140,15,600)+'<path d="M80 200 Q400 120 720 220" stroke="#c8d8ff" stroke-width="60" fill="none" opacity=".08"/><path d="M0 620 Q400 540 800 620 L800 800 L0 800Z" fill="#0a1424"/>'
b+='<g transform="rotate(-80 340 600)">'+figure(340,700,160,'#5a6a9a')+'</g><g transform="rotate(-80 460 610)">'+figure(460,710,150,'#5a6a9a',hair='#5a6a9a')+'</g>'
I[15]=svg(b,d)

# 118 やさしい悪魔: a cute devil's tail and tiny horns peeking from behind a pink heart, 1977 idol trio
d,b=bg([(0,'#3a0a3a'),(1,'#ff4a8a')])
b+=heart(400,440,140,'#ff9ac0')+'<path d="M300 300 L280 220 L330 280Z M500 300 L520 220 L470 280Z" fill="#c8102a"/><path d="M520 540 Q620 560 640 480 Q650 440 620 440 L660 420 L640 460" stroke="#c8102a" stroke-width="10" fill="none"/><path d="M630 430 L670 410 L650 450Z" fill="#c8102a"/>'
b+=''.join(sparkle(x,y,s,'#fff') for x,y,s in [(160,180,22),(640,200,26),(140,580,18)])
I[118]=svg(b,d)

# 259 線香花火: a single senko-hanabi sparkler dangling its glowing bead in a dark summer night, 1976 folk
d,b=bg([(0,'#050510'),(1,'#141424')])
b+='<path d="M400 0 L404 380" stroke="#c8784a" stroke-width="4"/><circle cx="404" cy="400" r="18" fill="#ff8a2a"/>'+glow(404,400,80,'#ff8a2a',.7)
b+=''.join(f'<path d="M{404+dx} {400+dy} l{dx*.6} {dy*.6} m0 0 l{dy*.3} {-dx*.3}" stroke="#ffd02a" stroke-width="2"/>' for dx,dy in [(-60,-20),(50,-40),(70,20),(-40,50),(20,70),(-70,30),(40,-70),(-20,-70)])
b+='<path d="M200 800 L260 620 Q300 560 380 600 L360 640" fill="#0a0a14" stroke="#2a1a14" stroke-width="2"/>'
I[259]=svg(b,d)

# 260 秋桜: a field of pink and white cosmos flowers swaying under a soft autumn sky, 1977 ballad
d,b=bg([(0,'#c8e0f8'),(1,'#f8f0f0')])
b+='<rect y="520" width="800" height="280" fill="#8ab06a"/>'+''.join(f'<path d="M{x} 800 Q{x+10} {y+100} {x} {y}" stroke="#4a8a3a" stroke-width="4" fill="none"/>'+flower(x,y,s,8,c,'#ffd02a',x) for x,y,s,c in [(80,520,40,'#ff9ac0'),(200,460,50,'#fff'),(320,540,44,'#ff7aa8'),(440,440,54,'#ffc0d8'),(560,520,46,'#fff'),(680,470,50,'#ff9ac0'),(140,640,36,'#ffc0d8'),(500,640,38,'#ff7aa8'),(740,620,34,'#fff')])
I[260]=svg(b,d)

# 275 東京: a lone rock star's silhouette on a rooftop above Tokyo at night with Tokyo Tower glowing, 1993
d,b=bg([(0,'#0a0a24'),(1,'#3a1a3a')])
b+=skyline(800,'#0a0a14',275,100,340,'#ffd27a',120)+tokyo_tower(600,800,520)+'<rect x="0" y="600" width="360" height="200" fill="#05050a"/>'+figure(200,610,240,'#000')
I[275]=svg(b,d)

# 601 夏祭り: a summer festival night with goldfish scooping, lanterns and a girl in yukata holding a fan
d,b=bg([(0,'#1a0a3a'),(1,'#5a2a5a')])
b+='<path d="M0 120 Q400 200 800 120" stroke="#3a2a2a" stroke-width="4" fill="none"/>'+''.join(chochin(x,170-(x-400)**2/6000+40,30) for x in (100,250,400,550,700))
b+='<rect x="380" y="560" width="400" height="120" fill="#3a8ad8"/>'+''.join(f'<path d="M{x} {y} q14 -10 24 0 l10 -8 l0 16 l-10 -8 q-10 10 -24 0Z" fill="#ff4a2a"/>' for x,y in [(440,600),(540,630),(640,590),(700,640)])
b+=figure(220,680,300,'#1a0a14',hair='#1a0a14')+'<path d="M180 420 L260 420 L280 680 L160 680Z" fill="#3a5ab8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="#fff" opacity=".7"/>' for x,y in [(200,480),(240,560),(200,620)])
I[601]=svg(b,d)

# 1279 crystal: a large faceted crystal refracting a beam of light into soft colours, 2019 ballad
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+='<polygon points="400,180 520,320 470,600 330,600 280,320" fill="#cfe6ff" opacity=".85"/><polygon points="400,180 520,320 400,360" fill="#fff" opacity=".7"/><polygon points="280,320 400,360 330,600" fill="#8ab0e8" opacity=".7"/><polygon points="400,360 520,320 470,600" fill="#a8c8f0" opacity=".7"/>'
b+=glow(400,400,220,'#cfe6ff',.35)+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(220,220,20),(600,240,26),(620,560,16),(200,520,18)])
I[1279]=svg(b,d)

# 1757 Make My Day: a girl twirling with an umbrella turned upside down to catch sunshine, bright pop
d,b=bg([(0,'#ffd04a'),(1,'#fff4d0')])
b+=rays(400,120,20,'#fff',.35,10)+'<circle cx="400" cy="120" r="60" fill="#fff4a0"/><rect y="640" width="800" height="160" fill="#8ac86a"/>'
b+=figure(400,660,280,'#3a2a3a',hair='#3a2a3a',pose='up')+'<path d="M300 300 Q400 420 500 300Z" fill="#ff6aa8"/><path d="M400 330 L400 380" stroke="#3a2a3a" stroke-width="5"/>'+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(320,260,14),(480,250,16),(400,230,12)])
I[1757]=svg(b,d)

# 1889 三都物語: three small vignettes in a row: a pagoda, a castle tower and a harbour crane at dusk, 1992
d,b=bg([(0,'#5a4a8a'),(1,'#ffb88a')])
b+='<rect y="560" width="800" height="240" fill="#3a2a3a"/>'
b+=''.join(f'<rect x="{150-w/2}" y="{560-(k+1)*70}" width="{w}" height="70" fill="#2a1a24"/><path d="M{150-w/2-20} {560-(k+1)*70} L{150+w/2+20} {560-(k+1)*70} L{150+w/2} {560-(k+1)*70-16} L{150-w/2} {560-(k+1)*70-16}Z" fill="#2a1a24"/>' for k,w in enumerate((70,60,50,40)))
b+='<rect x="350" y="420" width="100" height="140" fill="#2a1a24"/><path d="M330 420 L400 360 L470 420Z M350 360 L400 320 L450 360Z" fill="#2a1a24"/><rect x="370" y="330" width="60" height="30" fill="#2a1a24"/>'
b+='<path d="M620 560 Q660 440 630 300 L690 300 Q660 440 700 560Z" fill="#2a1a24"/><rect x="624" y="290" width="72" height="14" fill="#2a1a24"/>'+moon(400,160,40)
I[1889]=svg(b,d)

# 32 哀愁列車: a steam train pulling out of a snowy rural station with a hand waving from the window, 1956
d,b=bg([(0,'#5a6a8a'),(1,'#c8d0dc')])
b+=snow(60,32)+'<rect y="560" width="800" height="240" fill="#e0e6f0"/><rect x="0" y="540" width="800" height="16" fill="#5a5a64"/>'
b+='<rect x="140" y="400" width="420" height="140" rx="10" fill="#2a2a34"/><rect x="560" y="440" width="120" height="100" fill="#1a1a24"/><rect x="600" y="380" width="30" height="60" fill="#1a1a24"/>'+''.join(f'<rect x="{x}" y="430" width="60" height="50" fill="#ffd27a"/>' for x in (170,260,350,440))+''.join(f'<circle cx="{620-k*40}" cy="{360-k*30}" r="{20+k*8}" fill="#fff" opacity="{.6-k*.1}"/>' for k in range(5))
b+='<path d="M290 440 L300 410 L310 440" stroke="#f4c8a8" stroke-width="10" fill="none" stroke-linecap="round"/>'+''.join(f'<circle cx="{x}" cy="550" r="16" fill="#111"/>' for x in (190,300,410,520,620))
I[32]=svg(b,d)

# 419 けんかをやめて: two boys' silhouettes glaring at each other with a girl in between holding them apart, 1982 idol
d,b=bg([(0,'#ffd8e8'),(1,'#e8e0ff')])
b+='<rect y="640" width="800" height="160" fill="#c8b8c8"/>'+figure(180,660,300,'#2a2a4a')+figure(620,660,300,'#2a2a4a')+figure(400,660,260,'#e85a8a',hair='#e85a8a')
b+='<path d="M380 420 L270 400 M420 420 L530 400" stroke="#e85a8a" stroke-width="14" stroke-linecap="round"/>'+bolt([(260,240),(300,280),(280,290),(320,330)],'#e8302a',6)+bolt([(540,240),(500,280),(520,290),(480,330)],'#e8302a',6)
I[419]=svg(b,d)

# 426 夏色のナンシー: a bright summer beach with a striped swimsuit drying, a surfboard and a can of soda, 1983 idol
d,b=bg([(0,'#2ab8ff'),(1,'#d8f8ff')])
b+='<circle cx="640" cy="140" r="70" fill="#fff4a0"/><rect y="420" width="800" height="140" fill="#1a8ad8"/><path d="M0 560 Q400 520 800 560 L800 800 L0 800Z" fill="#f8e0a8"/>'
b+='<path d="M140 760 L190 380 Q210 320 230 380 L280 760Z" fill="#ffd02a"/><path d="M210 360 L210 760" stroke="#ff4a8a" stroke-width="10"/>'+'<rect x="440" y="560" width="70" height="120" rx="10" fill="#e8302a"/><rect x="440" y="600" width="70" height="20" fill="#fff"/>'+''.join(f'<rect x="{x}" y="620" width="120" height="16" fill="{c}"/>' for x,c in [(560,'#ff6aa0')])+'<path d="M560 620 L680 620 L660 700 L580 700Z" fill="#ff6aa0"/>'+''.join(f'<rect x="580" y="{y}" width="80" height="8" fill="#fff"/>' for y in (640,660,680))
I[426]=svg(b,d)

# 607 恋をしようよ Yeah! Yeah!: a girl leaping with a heart-shaped kite on a windy spring day, 90s band pop
d,b=bg([(0,'#5ac8ff'),(1,'#fff4d8')])
b+=cloud(160,200,1.2)+'<rect y="620" width="800" height="180" fill="#8ac86a"/>'+heart(560,220,60,'#ff4a8a')+'<path d="M560 290 Q500 420 420 500" stroke="#5a5a5a" stroke-width="3" fill="none"/>'+''.join(f'<path d="M{560+k*8} {290+k*40} l14 10" stroke="#ff4a8a" stroke-width="6"/>' for k in range(1,4))
b+='<g transform="rotate(-10 380 480)">'+figure(380,620,260,'#2a2a3a',pose='up',hair='#2a2a3a')+'</g>'
I[607]=svg(b,d)

# 926 Orange: a sliced orange glowing like a setting sun over a city of rooftops, 2005 ballad
d,b=bg([(0,'#ff8a3a'),(1,'#ffe0a0')])
b+='<circle cx="400" cy="400" r="160" fill="#ff9a1a"/><circle cx="400" cy="400" r="136" fill="#ffc84a"/>'+''.join(f'<path d="M400 400 L{400+124*math.cos(a)} {400+124*math.sin(a)} A124 124 0 0 1 {400+124*math.cos(a+.7)} {400+124*math.sin(a+.7)}Z" fill="#ffa82a" stroke="#fff4c8" stroke-width="6"/>' for a in [k*2*math.pi/8 for k in range(8)])
b+=skyline(800,'#5a2a2a',926,80,220,'#ffd27a',40)
I[926]=svg(b,d)

# 29 君恋し: a lone man at a lamppost on a foggy night street with a lit window far away, 1961 jazz-kayō
d,b=bg([(0,'#2a2a3a'),(1,'#5a5a6a')])
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="300" ry="40" fill="#e8e8f0" opacity=".12"/>' for x,y in [(300,300),(500,420),(400,560)])+'<rect y="620" width="800" height="180" fill="#1a1a24"/><rect x="560" y="360" width="80" height="60" fill="#ffd27a" opacity=".7"/>'
b+='<rect x="300" y="220" width="10" height="400" fill="#2a2a34"/><circle cx="305" cy="220" r="18" fill="#fff4c8"/>'+glow(305,230,100,'#fff4c8',.4)+figure(360,640,240,'#000')+'<ellipse cx="360" cy="402" rx="46" ry="10" fill="#000"/><path d="M336 400 Q360 370 384 400Z" fill="#000"/>'
I[29]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
