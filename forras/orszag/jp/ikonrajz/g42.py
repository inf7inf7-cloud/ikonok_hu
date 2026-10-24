import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 42. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1815 二人でお酒を: two small sake cups and a tokkuri on a low table with a warm lamp, 1973 kayō
d,b=bg([(0,'#2a1a14'),(1,'#5a3a2a')])
b+=glow(400,300,240,'#ffb070',.35)+'<rect y="500" width="800" height="300" fill="#4a2a1a"/><rect x="120" y="480" width="560" height="30" fill="#7a4a2a"/>'
b+='<path d="M370 480 L370 380 Q370 340 390 320 L390 290 L410 290 L410 320 Q430 340 430 380 L430 480Z" fill="#f4ece0"/><path d="M372 400 L428 400" stroke="#3a5a8a" stroke-width="8"/>'
b+='<path d="M250 440 L310 440 L300 480 L260 480Z" fill="#f4ece0"/><path d="M490 440 L550 440 L540 480 L500 480Z" fill="#f4ece0"/>'
I[1815]=svg(b,d)

# 1898 City Hunter: a neon-lit city night from a rooftop with a single red heart beacon on a tower, 80s anime ballad
d,b=bg([(0,'#0a0a24'),(1,'#3a1a4a')])
b+=starsf(30,1898,300)+skyline(800,'#0a0a1a',1898,180,500,'#ffd27a',160)+'<rect x="360" y="180" width="80" height="620" fill="#14142a"/>'+heart(400,160,30,'#ff2a4a')+glow(400,160,80,'#ff2a4a',.6)
b+='<rect x="0" y="680" width="800" height="120" fill="#05050f"/>'+figure(160,690,200,'#000')
I[1898]=svg(b,d)

# 172 夜桜お七: cherry blossoms at night beside an old fire-watch tower with a red alarm bell, 1994 enka
d,b=bg([(0,'#0a0a1a'),(1,'#2a0a2a')])
b+=moon(160,140,50)+'<rect x="520" y="200" width="16" height="600" fill="#2a1a14"/><rect x="620" y="200" width="16" height="600" fill="#2a1a14"/>'+''.join(f'<path d="M520 {y} L636 {y+60} M636 {y} L520 {y+60}" stroke="#2a1a14" stroke-width="6"/>' for y in range(260,800,80))+'<path d="M500 200 L578 140 L656 200Z" fill="#2a1a14"/><path d="M560 170 Q578 150 596 170 L600 196 L556 196Z" fill="#e8302a"/>'
b+=''.join(sakura(x,y,s,'#ffc2d6','#ff7aa8',r) for x,y,s,r in [(120,360,60,0),(260,280,70,20),(200,480,64,40),(360,400,50,10),(80,560,56,30)])+petals(40,172)+glow(578,180,100,'#ff4a2a',.4)
I[172]=svg(b,d)

# 176 ほど酔い酒: a sake bottle and a cup glowing under a warm lantern on a quiet night counter, enka-pop
d,b=bg([(0,'#1a0a14'),(1,'#4a1a24')])
b+=chochin(620,220,70)+'<rect y="520" width="800" height="280" fill="#6a3a24"/><rect y="500" width="800" height="24" fill="#8a5a3a"/>'
b+='<path d="M300 500 L300 340 Q300 300 330 290 L330 240 L370 240 L370 290 Q400 300 400 340 L400 500Z" fill="#3a6a5a"/><rect x="310" y="380" width="80" height="60" fill="#f4ece0"/>'+'<path d="M460 450 L530 450 L520 500 L470 500Z" fill="#f4ece0"/>'+glow(500,470,60,'#ffd27a',.4)
I[176]=svg(b,d)

# 1277 応答セヨ: a vintage radio transceiver with a blinking antenna sending signal waves into space
d,b=bg([(0,'#050a1a'),(1,'#1a2a4a')])
b+=starsf(70,1277,800)+''.join(f'<path d="M{430-r} {260-r*.3} Q430 {260-r} {430+r} {260-r*.3}" stroke="#3affe8" stroke-width="5" fill="none" opacity="{1-r/320}"/>' for r in (60,120,180,240))
b+='<rect x="230" y="420" width="340" height="220" rx="16" fill="#5a5a64"/><rect x="260" y="450" width="160" height="100" fill="#1a2a1a"/><path d="M270 500 L300 480 L330 520 L360 470 L410 500" stroke="#3aff8a" stroke-width="4" fill="none"/><circle cx="490" cy="500" r="40" fill="#3a3a44"/><circle cx="490" cy="500" r="10" fill="#8a8a94"/>'
b+='<path d="M430 420 L430 260" stroke="#c8c8d0" stroke-width="6"/><circle cx="430" cy="256" r="10" fill="#ff3a3a"/>'
I[1277]=svg(b,d)

# 99 越冬つばめ: a lone swallow perched on a snowy branch refusing to fly south, 1983 enka
d,b=bg([(0,'#5a6a8a'),(1,'#d8e0ec')])
b+=snow(80,99)+'<path d="M0 420 Q300 400 520 440 Q640 460 800 430" stroke="#3a2a2a" stroke-width="16" fill="none"/><path d="M0 410 Q300 390 520 430" stroke="#f4f6ff" stroke-width="8" fill="none"/>'
b+='<path d="M380 430 Q400 360 470 360 Q500 360 510 380 L540 370 L510 395 Q500 430 450 440 L420 440 L330 500 L350 450 L300 480Z" fill="#1a2a4a"/><path d="M450 400 Q480 420 500 395" fill="#e8402a"/><path d="M460 410 Q490 430 505 400 Q480 400 460 410Z" fill="#f4f4f4"/>'
I[99]=svg(b,d)

# 197 心もよう: a letter being written by lamplight with blue ink blots like a mosaic of the heart, 1973
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+=glow(560,260,200,'#ffd27a',.35)+'<rect y="540" width="800" height="260" fill="#4a3a2a"/><rect x="180" y="440" width="380" height="240" fill="#f4ece0" transform="rotate(-6 370 560)"/>'
b+=''.join(f'<path d="M210 {y} L520 {y-30}" stroke="#3a5a9a" stroke-width="3" opacity=".7"/>' for y in range(500,660,30))+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#3a5a9a" opacity=".6"/>' for x,y,r in [(300,560,14),(420,600,10),(480,520,8)])
b+='<path d="M600 300 L600 540" stroke="#3a3a3a" stroke-width="8"/><path d="M540 300 L660 300 L630 240 L570 240Z" fill="#c8a24a"/>'
I[197]=svg(b,d)

# 469 不思議な手品のように: a magician's top hat with a dove and sparkles flying out, 80s idol
d,b=bg([(0,'#2a1a5a'),(1,'#a86ac8')])
b+='<ellipse cx="400" cy="600" rx="170" ry="34" fill="#111"/><rect x="290" y="420" width="220" height="180" fill="#111"/><ellipse cx="400" cy="420" rx="110" ry="24" fill="#2a2a2a"/><rect x="290" y="540" width="220" height="24" fill="#c8102a"/>'
b+='<path d="M400 360 Q330 300 260 320 Q330 340 380 380 Q370 320 420 300 L470 290 L500 270 L470 260 Q430 260 400 300Z" fill="#fff"/>'+''.join(sparkle(x,y,s,'#fff4c8') for x,y,s in [(300,240,26),(520,200,20),(560,340,16),(240,400,14),(420,180,18)])
I[469]=svg(b,d)

# 1834 鳥人戦隊ジェットマン: five coloured jet streaks forming a bird wing formation over the sky, tokusatsu theme
d,b=bg([(0,'#1a5ad8'),(1,'#a8e0ff')])
b+=cloud(160,620,1.4)+cloud(640,660,1.2)
for k,(c,dx,dy) in enumerate([('#e8302a',0,0),('#1a4ab8',-110,80),('#ffd02a',110,80),('#fff',-220,160),('#ff6aa8',220,160)]):
  x,y=400+dx,240+dy
  b+=f'<path d="M{x} {y+40} L{x} 800" stroke="{c}" stroke-width="8" opacity=".5"/><path d="M{x} {y-30} L{x+50} {y+30} L{x+10} {y+20} L{x} {y+40} L{x-10} {y+20} L{x-50} {y+30}Z" fill="{c}" stroke="#1a1a2a" stroke-width="3"/>'
I[1834]=svg(b,d)

# 45 高校三年生: a school cap and diploma under a cherry-less spring sky with a row of students' silhouettes, 1963
d,b=bg([(0,'#9ad0ff'),(1,'#fff4e0')])
b+='<rect x="100" y="260" width="600" height="300" fill="#e8dcc8"/><rect x="340" y="200" width="120" height="70" fill="#e8dcc8"/><circle cx="400" cy="230" r="24" fill="#f4f0e8" stroke="#8a7a6a" stroke-width="4"/>'+''.join(f'<rect x="{x}" y="{y}" width="50" height="60" fill="#8ab0d8"/>' for x in (140,240,510,610) for y in (300,420))
b+='<rect y="560" width="800" height="240" fill="#c8b8a0"/>'+''.join(figure(x,720,180,'#1a1a2a',hair='#1a1a2a' if k%2 else None) for k,x in enumerate((200,300,400,500,600)))
I[45]=svg(b,d)

# 304 ランナウェイ: a pair of white-gloved hands and a black fedora flying away from a doo-wop mic, 1980
d,b=bg([(0,'#0a0a0a'),(1,'#2a2a2a')])
b+='<path d="M360 0 L440 0 L560 620 L240 620Z" fill="#fff" opacity=".12"/><rect y="620" width="800" height="180" fill="#14141a"/><rect x="396" y="380" width="8" height="240" fill="#c8c8d0"/><rect x="380" y="330" width="40" height="60" rx="20" fill="#3a3a44"/>'
b+='<g transform="rotate(-20 560 220)"><ellipse cx="560" cy="240" rx="110" ry="24" fill="#111"/><path d="M490 240 Q500 150 560 150 Q620 150 630 240Z" fill="#111"/><rect x="494" y="214" width="132" height="16" fill="#f4f4f4"/></g>'
b+='<path d="M180 260 L240 200 L260 220 L210 280Z M220 210 L230 170 M235 205 L250 170 M248 215 L268 185" stroke="#f4f4f4" stroke-width="16" fill="#f4f4f4" stroke-linecap="round"/>'
I[304]=svg(b,d)

# 606 GAMBAらなくちゃね: a sweaty office worker's silhouette sprinting to catch a train with a coffee, 90s pop-rock
d,b=bg([(0,'#ffd04a'),(1,'#ffefc0')])
b+='<rect y="560" width="800" height="240" fill="#9a9aa0"/><rect x="460" y="380" width="340" height="180" fill="#5ab84a"/>'+''.join(f'<rect x="{x}" y="410" width="50" height="50" fill="#e8f8ff"/>' for x in (490,570,650,730))
b+='<g transform="rotate(15 280 500)">'+figure(280,700,320,'#1a1a2a',pose='up')+'</g><rect x="140" y="380" width="30" height="40" fill="#fff" stroke="#8a5a3a" stroke-width="4"/>'+''.join(f'<path d="M{x} {y} L{x-120} {y}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>' for x,y in [(160,520),(140,580),(170,640)])
I[606]=svg(b,d)

# 1680 Tonight: a city rooftop party at night with string lights and a dancing silhouette, 2017 boy group
d,b=bg([(0,'#0a0a24'),(1,'#3a1a4a')])
b+=skyline(620,'#140a24',1680,60,240,'#ffd27a',60)+'<path d="M0 200 Q200 260 400 200 T800 200" stroke="#3a3a4a" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{x}" cy="{200+30*math.sin(x/127)}" r="8" fill="#ffd27a"/>' for x in range(30,800,60))
b+='<rect y="620" width="800" height="180" fill="#0a0a14"/>'+figure(400,640,320,'#000',pose='up')
I[1680]=svg(b,d)

# 1775 愛情: a heart made of candlelight held between two cupped hands in darkness, powerful soul ballad
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a14')])
b+=glow(400,380,240,'#ff6a5a',.5)+heart(400,380,90,'#ff4a4a')+'<path d="M180 620 Q200 480 320 470 L320 540 Q240 560 240 640Z" fill="#c8906a"/><path d="M620 620 Q600 480 480 470 L480 540 Q560 560 560 640Z" fill="#b8805a"/>'
I[1775]=svg(b,d)

# 7 花笠道中: a woman's silhouette travelling a country road wearing a big flower-decorated straw hat, 1962
d,b=bg([(0,'#9ad0ff'),(1,'#fff0d8')])
b+=hills(440,50,'#8ab06a',7,4)+'<rect y="480" width="800" height="320" fill="#a8c878"/><path d="M380 480 L200 800 L600 800 L420 480Z" fill="#e8d8a8"/>'
b+=figure(400,700,280,'#3a2a3a',hair='#3a2a3a')+'<ellipse cx="400" cy="420" rx="110" ry="24" fill="#e8c870"/><path d="M330 420 Q400 360 470 420Z" fill="#e8c870"/>'+''.join(flower(x,y,16,5,c,'#ffd02a') for x,y,c in [(340,400,'#ff6a8a'),(380,384,'#ff9ac0'),(420,384,'#e8302a'),(460,400,'#ff6a8a')])
I[7]=svg(b,d)

# 22 恋のフーガ: two hearts chasing each other around a spiral of music staff, 60s twin vocal pop
d,b=bg([(0,'#ffe8f0'),(1,'#e8e0ff')])
b+=''.join(f'<path d="M{400+r*math.cos(a)} {400+r*math.sin(a)} A{r} {r} 0 0 1 {400+r*math.cos(a+2)} {400+r*math.sin(a+2)}" stroke="#a87ac8" stroke-width="3" fill="none"/>' for r in range(80,320,40) for a in (0,3.2))
b+=heart(260,300,50,'#ff4a8a')+heart(540,520,50,'#e8102a')+note(560,240,40,'#a87ac8')+note(240,540,40,'#a87ac8',True)
I[22]=svg(b,d)

# 150 浮草ぐらし: floating duckweed drifting on a dark pond with a single lantern reflection, 1981 enka
d,b=bg([(0,'#0a1424'),(1,'#1a2a3a')])
b+=moon(600,140,40)+''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.5}" fill="#3a8a4a"/>' for x,y,r in [(200,420,30),(260,460,20),(420,520,36),(560,480,24),(340,640,30),(620,620,20),(180,700,26)])
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="80" ry="12" fill="none" stroke="#5a7aa8" stroke-width="3" opacity=".4"/>' for x,y in [(300,560),(520,700)])+'<rect x="590" y="280" width="20" height="40" fill="#ffd27a" opacity=".8"/>'+glow(600,300,40,'#ffd27a',.5)
I[150]=svg(b,d)

# 153 天城越え: a misty mountain pass with a waterfall and a woman in kimono crossing a hanging bridge, enka
d,b=bg([(0,'#3a4a5a'),(1,'#9aa8b8')])
b+='<path d="M0 800 L0 200 L260 360 L260 800Z" fill="#2a3a3a"/><path d="M800 800 L800 160 L540 320 L540 800Z" fill="#2a3a3a"/><rect x="380" y="200" width="40" height="600" fill="#e8f0ff" opacity=".7"/>'
b+='<path d="M260 420 Q400 480 540 400" stroke="#5a3a2a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x} {420+60*math.sin((x-260)/280*math.pi)-(x-260)*0.07} L{x} {380+60*math.sin((x-260)/280*math.pi)-(x-260)*0.07}" stroke="#5a3a2a" stroke-width="3"/>' for x in range(280,540,30))
b+=figure(330,430,140,'#4a0a1a',hair='#0a0a0a')+''.join(f'<ellipse cx="{x}" cy="{y}" rx="200" ry="30" fill="#fff" opacity=".2"/>' for x,y in [(200,600),(600,500),(400,700)])
I[153]=svg(b,d)

# 156 浪花節だよ人生は: a folding fan, a sake cup and a shamisen on a wooden stage with a red curtain, enka
d,b=bg([(0,'#5a0a14'),(1,'#a82a2a')])
b+='<path d="M0 0 L200 0 Q160 400 220 800 L0 800Z M800 0 L600 0 Q640 400 580 800 L800 800Z" fill="#7a0a1a"/><rect y="600" width="800" height="200" fill="#8a5a3a"/>'
b+='<path d="M400 600 L240 420 A220 220 0 0 1 560 420Z" fill="#ffd02a"/>'+''.join(f'<path d="M400 600 L{400+220*math.cos(a)} {600-220*math.sin(a)}" stroke="#c8982a" stroke-width="4"/>' for a in [math.radians(t) for t in range(48,135,12)])+'<path d="M560 620 L620 620 L610 660 L570 660Z" fill="#f4ece0"/>'
I[156]=svg(b,d)

# 187 今日までそして明日から: a boy with a guitar case standing at a crossroads signpost under a big sky, 1971 folk
d,b=bg([(0,'#7ab0e8'),(1,'#f4f0d8')])
b+='<rect y="520" width="800" height="280" fill="#a8b878"/><path d="M380 520 L100 800 M420 520 L700 800 M400 600 L0 680 M400 600 L800 660" stroke="#e8d8a8" stroke-width="40"/>'
b+='<rect x="460" y="360" width="10" height="260" fill="#5a3a2a"/><path d="M470 380 L580 380 L600 400 L580 420 L470 420Z M460 440 L350 440 L330 460 L350 480 L460 480Z" fill="#c8a870"/>'+figure(300,640,220,'#1a1a2a')+'<rect x="330" y="540" width="36" height="110" rx="14" fill="#1a1a2a" transform="rotate(10 348 595)"/>'
I[187]=svg(b,d)

# 188 どうしてこんなに悲しいんだろう: a man sitting alone on a hillside under a grey sky watching geese fly
d,b=bg([(0,'#7a8494'),(1,'#c8ccd4')])
b+='<path d="M0 560 Q400 480 800 560 L800 800 L0 800Z" fill="#6a7a6a"/>'+figure(400,540,150,'#1a1a24')+''.join(bird(x,y,s,'#2a2a34') for x,y,s in [(240,200,30),(290,230,26),(340,260,22),(190,230,26),(140,260,22)])
I[188]=svg(b,d)

# 424 センチメンタル・ジャーニー: a vintage suitcase covered in travel stickers on a railway platform, 80s idol
d,b=bg([(0,'#ffc8a8'),(1,'#f4e0d0')])
b+='<rect y="560" width="800" height="240" fill="#8a7a7a"/><rect y="560" width="800" height="14" fill="#e8e0d0"/>'+''.join(f'<rect x="{x}" y="160" width="12" height="400" fill="#5a4a4a"/>' for x in (100,700))+'<rect x="80" y="150" width="640" height="16" fill="#5a4a4a"/>'
b+='<rect x="260" y="400" width="280" height="200" rx="14" fill="#a85a3a"/><rect x="360" y="370" width="80" height="34" rx="10" fill="none" stroke="#5a3a2a" stroke-width="10"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="24" fill="{c}"/>' for x,y,c in [(320,460,'#ff8ab0'),(470,500,'#3ab0ff'),(360,540,'#ffd02a')])+'<rect x="420" y="430" width="60" height="40" fill="#5ad87a" transform="rotate(10 450 450)"/>'
I[424]=svg(b,d)

# 920 UTAO-UTAO: a crowd of silhouettes singing with arms around each other under a sky of music notes
d,b=bg([(0,'#3ab0ff'),(1,'#fff0c0')])
b+=''.join(note(x,y,s,c) for x,y,s,c in [(140,140,44,'#ff6aa0'),(300,100,36,'#ffd02a'),(480,160,40,'#5ad87a'),(640,120,46,'#ff6aa0'),(220,280,30,'#5ad87a'),(560,300,34,'#ffd02a')])
b+='<rect y="620" width="800" height="180" fill="#5a8a4a"/>'+''.join(figure(x,780,260,'#1a2a3a') for x in range(100,800,120))+'<path d="M100 560 L700 560" stroke="#1a2a3a" stroke-width="18"/>'
I[920]=svg(b,d)

# 1479 Step Up Love: a staircase of glowing neon steps climbing to a heart in a night city
d,b=bg([(0,'#0a0a24'),(1,'#2a0a3a')])
b+=skyline(800,'#0a0a1a',1479,80,260,'#8ad0ff',60)+''.join(f'<rect x="{120+k*90}" y="{660-k*80}" width="100" height="16" fill="#ff4fd0"/>' for k in range(6))+glow(600,200,100,'#ff4fd0',.5)+heart(640,220,40,'#ff4fd0')+figure(250,580,120,'#000',hair='#000')
I[1479]=svg(b,d)

# 1730 ミニモニ。テレフォン!リンリンリン: a candy-coloured toy telephone ringing with bouncing sound marks, kids' pop
d,b=bg([(0,'#ffe0f0'),(1,'#fff8c0')])
b+=confetti(30,1730,['#ff6aa0','#3ab0ff','#ffd02a'])+'<path d="M250 560 Q230 420 300 400 L500 400 Q570 420 550 560Z" fill="#ff6aa8"/><circle cx="400" cy="480" r="50" fill="#fff"/>'+''.join(f'<circle cx="{400+34*math.cos(a)}" cy="{480+34*math.sin(a)}" r="8" fill="#3ab0ff"/>' for a in [k*math.pi/5 for k in range(10)])
b+='<path d="M240 380 Q250 310 330 320 L470 320 Q550 310 560 380" stroke="#3ab0ff" stroke-width="38" fill="none" stroke-linecap="round"/>'+''.join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#ff4a8a" stroke-width="8" stroke-linecap="round"/>' for x,y,dx,dy in [(200,300,-40,-40),(180,380,-50,0),(600,300,40,-40),(620,380,50,0)])
I[1730]=svg(b,d)

# 167 なみだ恋: a woman's teardrop falling into a glass of whisky at a dim bar counter, 1973 enka
d,b=bg([(0,'#1a1014'),(1,'#3a2024')])
b+=glow(400,300,200,'#ffb070',.3)+'<rect y="560" width="800" height="240" fill="#5a3a24"/><rect y="540" width="800" height="24" fill="#7a4a2a"/>'
b+='<path d="M330 400 L470 400 L460 540 L340 540Z" fill="#f4ece0" opacity=".5"/><path d="M336 460 L464 460 L460 540 L340 540Z" fill="#c8802a" opacity=".8"/>'+'<path d="M400 260 Q420 300 400 320 Q380 300 400 260Z" fill="#8ad0ff"/>'+profile(620,560,.8,'#0a0a0a',True)
I[167]=svg(b,d)

# 207 あの唄はもう唄わないのですか: an old acoustic guitar leaning against a wall under a faded poster, 1976 folk
d,b=bg([(0,'#d8c8a8'),(1,'#b8a888')])
b+='<rect x="440" y="120" width="240" height="320" fill="#e8dcc0" transform="rotate(4 560 280)"/>'+''.join(note(x,y,s,'#a8987a') for x,y,s in [(520,220,40),(600,300,30)])+'<rect y="640" width="800" height="160" fill="#7a5a3a"/>'
b+=guitar(300,520,1.2,-10,'#a86a2a')
I[207]=svg(b,d)

# 342 Technopolis: a retro-futuristic city grid of neon towers with a pulse travelling along the lines, 1979 techno
d,b=bg([(0,'#000010'),(1,'#100a30')])
b+=''.join(f'<rect x="{x}" y="{800-h}" width="60" height="{h}" fill="#0a0a20" stroke="#3affe8" stroke-width="3"/>' for x,h in [(40,300),(120,420),(200,260),(280,520),(360,380),(440,600),(520,340),(600,460),(680,280)])
b+=''.join(f'<rect x="{x+16}" y="{y}" width="28" height="10" fill="#ff4fd0"/>' for x,h in [(120,420),(280,520),(440,600),(600,460)] for y in range(820-h,800,40))+'<path d="M0 520 L800 520" stroke="#e8302a" stroke-width="6"/>'+glow(400,520,60,'#e8302a',.7)
I[342]=svg(b,d)

# 553 Please: a woman's hands clasped in a plea before a rain-streaked window with city lights, 1991 pop
d,b=bg([(0,'#1a1a3a'),(1,'#4a3a6a')])
b+=''.join(f'<circle cx="{random.Random(553*k).randint(0,800)}" cy="{random.Random(553*k+1).randint(0,500)}" r="{random.Random(553*k+2).randint(10,30)}" fill="{["#ffd27a","#ff8ad0"][k%2]}" opacity=".3"/>' for k in range(24))+rain(40,553,'#cfe6ff',.35)
b+='<path d="M330 800 L350 520 Q360 440 400 420 Q440 440 450 520 L470 800Z" fill="#2a1a2a"/><path d="M370 520 Q400 440 430 520 L420 560 L380 560Z" fill="#c8906a"/>'
I[553]=svg(b,d)

# 679 ラストショー: an empty drive-in movie screen glowing at night with one car left, 1981 rock
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=starsf(60,679,400)+'<rect x="160" y="140" width="480" height="260" fill="#e8e0d0"/>'+glow(400,270,280,'#e8e0d0',.25)+'<rect x="380" y="400" width="40" height="200" fill="#2a2a34"/><rect y="600" width="800" height="200" fill="#14141e"/>'
b+='<path d="M300 660 L340 610 L480 610 L520 660 L540 670 L540 700 L280 700 L280 670Z" fill="#2a2a3a"/><circle cx="330" cy="702" r="20" fill="#111"/><circle cx="490" cy="702" r="20" fill="#111"/>'+profile(380,650,.25,'#000')+profile(440,650,.25,'#000',True)
I[679]=svg(b,d)

# 1252 White X'mas: a snow-covered Christmas tree in a quiet plaza with a couple's silhouettes, 2008
d,b=bg([(0,'#1a2a4a'),(1,'#4a5a8a')])
b+=snow(100,1252)+'<rect y="620" width="800" height="180" fill="#e8eef8"/><path d="M400 140 L540 620 L260 620Z" fill="#1a5a3a"/>'+''.join(f'<path d="M{400-w} {y} Q400 {y-20} {400+w} {y}" stroke="#f4f6ff" stroke-width="10" fill="none"/>' for w,y in [(50,280),(80,400),(110,520)])
b+=star5(400,130,30,'#ffd02a')+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"/>' for x,y,c in [(370,320,'#ff4a4a'),(430,360,'#ffd02a'),(340,460,'#8ad0ff'),(460,480,'#ff4a4a'),(400,560,'#ffd02a')])+figure(160,700,180,'#0a0a14')+figure(220,700,170,'#0a0a14',hair='#0a0a14')
I[1252]=svg(b,d)

# 1734 無意識の色: a girl's silhouette filled with swirling unconscious colours against white, idol pop
d,b=bg([(0,'#f4f4f8'),(1,'#e8e8f0')])
d+='<linearGradient id="sw" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff4a8a"/><stop offset=".35" stop-color="#ffd02a"/><stop offset=".7" stop-color="#3ad8c8"/><stop offset="1" stop-color="#6a4aff"/></linearGradient>'
b+=figure(400,760,560,'url(#sw)',hair='url(#sw)')+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity=".5"/>' for x,y,r,c in [(160,200,30,'#ff4a8a'),(640,260,24,'#3ad8c8'),(600,600,40,'#ffd02a'),(180,560,20,'#6a4aff')])
I[1734]=svg(b,d)

# 1747 青春時計: a school clock tower with hands spinning fast and petals of youth flying, Niigata idol group
d,b=bg([(0,'#8ad0ff'),(1,'#fff0e0')])
b+='<rect x="300" y="240" width="200" height="560" fill="#e8dcc8"/><path d="M280 250 L400 140 L520 250Z" fill="#3a6a8a"/><circle cx="400" cy="340" r="70" fill="#fff" stroke="#3a3a4a" stroke-width="8"/>'
b+='<path d="M400 340 L400 290 M400 340 L440 360" stroke="#3a3a4a" stroke-width="8" stroke-linecap="round"/>'+''.join(f'<path d="M{400+90*math.cos(a)} {340+90*math.sin(a)} A90 90 0 0 1 {400+90*math.cos(a+.6)} {340+90*math.sin(a+.6)}" stroke="#ff8ab0" stroke-width="5" fill="none"/>' for a in (0,2.1,4.2))
b+=''.join(f'<rect x="{x}" y="{y}" width="40" height="50" fill="#8ab0d8"/>' for x in (330,430) for y in (460,560,660))+''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="6" fill="#ffd0e0" transform="rotate({x} {x} {y})"/>' for x,y in [(140,200),(220,320),(620,180),(680,420),(160,520),(600,600)])
I[1747]=svg(b,d)

# 572 スターダスト・ドリーム: a girl on a crescent moon swing sprinkling stardust over a sleeping city, 80s idol
d,b=bg([(0,'#0a0a3a'),(1,'#4a2a7a')])
b+=starsf(80,572,800)+skyline(800,'#0a0a1a',572,60,200,'#ffd27a',40)+'<path d="M420 160 A120 120 0 1 0 520 360 A96 96 0 1 1 420 160Z" fill="#fff4c8"/>'
b+=figure(400,330,130,'#ffd0e8',hair='#ffd0e8')+''.join(sparkle(x,y,s,'#fff4c8') for x,y,s in [(400,420,16),(440,480,12),(380,520,14),(420,560,10),(360,600,12)])
I[572]=svg(b,d)

# 680 MONEY: a single crumpled banknote blowing down a dark alley past a neon sign, 1984/99 rock
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+='<rect x="0" y="100" width="260" height="700" fill="#1a1a24"/><rect x="540" y="100" width="260" height="700" fill="#1a1a24"/><path d="M260 800 L360 300 L440 300 L540 800Z" fill="#2a2a34"/>'+'<rect x="40" y="220" width="180" height="60" rx="8" fill="none" stroke="#3aff8a" stroke-width="6"/>'+glow(130,250,120,'#3aff8a',.3)
b+='<g transform="rotate(-20 420 520)"><rect x="340" y="480" width="170" height="80" fill="#a8c890"/><circle cx="425" cy="520" r="24" fill="none" stroke="#5a7a4a" stroke-width="4"/><rect x="350" y="490" width="150" height="60" fill="none" stroke="#5a7a4a" stroke-width="3"/></g>'+''.join(f'<path d="M{x} {y} q30 -10 60 0" stroke="#5a5a6a" stroke-width="3" fill="none"/>' for x,y in [(240,560),(500,600)])
I[680]=svg(b,d)

# 921 スピリット: a bright spirit flame rising from an open palm into the dark sky, 2009 boy group
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=starsf(50,921,700)+'<path d="M400 520 Q340 420 380 340 Q390 380 400 360 Q400 300 440 260 Q430 340 460 380 Q480 440 400 520Z" fill="#8ad0ff"/>'+glow(410,420,160,'#8ad0ff',.6)
b+='<path d="M240 800 L280 620 Q300 560 360 560 L460 560 Q540 560 560 620 L580 800Z" fill="#14142a"/>'
I[921]=svg(b,d)

# 922 COSMIC RESCUE: a rescue rocket's tractor beam lifting a little astronaut back from deep space
d,b=bg([(0,'#02040e'),(1,'#141a3a')])
b+=starsf(90,922,800)+'<circle cx="640" cy="640" r="120" fill="#6a4aa8"/><ellipse cx="640" cy="640" rx="190" ry="30" fill="none" stroke="#a88ae8" stroke-width="6"/>'
b+='<path d="M360 260 L250 620 L470 620Z" fill="#fff4a0" opacity=".25"/><path d="M360 120 Q400 160 400 260 L320 260 Q320 160 360 120Z" fill="#e8e8f4"/><circle cx="360" cy="200" r="16" fill="#3ab0ff"/><path d="M320 240 L290 280 L320 270Z M400 240 L430 280 L400 270Z" fill="#e8302a"/>'
b+='<circle cx="360" cy="520" r="30" fill="#f4f4f4"/><circle cx="360" cy="520" r="18" fill="#3a5a8a"/><rect x="335" y="548" width="50" height="60" rx="16" fill="#f4f4f4"/>'
I[922]=svg(b,d)

# 41 函館の女: a famous-style night view: a narrow strip of city lights between two dark bays, a woman's silhouette, enka
d,b=bg([(0,'#050a1a'),(1,'#1a2440')])
b+=starsf(40,41,300)+'<path d="M0 440 Q200 420 300 470 Q400 520 500 470 Q600 420 800 440 L800 800 L0 800Z" fill="#0a1020"/>'
b+='<path d="M220 460 Q400 600 580 460 L620 800 L180 800Z" fill="#141420"/>'+''.join(f'<circle cx="{random.Random(41*k).randint(200,600)}" cy="{random.Random(41*k+1).randint(470,800)}" r="3" fill="{["#ffd27a","#fff","#ff9a6a"][k%3]}"/>' for k in range(200) if True)
b+='<path d="M0 360 L180 300 L180 800 L0 800Z" fill="#0a0a14"/>'+figure(110,320,140,'#000',hair='#000')
I[41]=svg(b,d)

# 43 いつでも夢を: two young silhouettes on a hill pointing at a rising star at dawn, 1962
d,b=bg([(0,'#2a3a8a'),(1,'#ffc8a0')])
b+=starsf(30,43,300)+star5(560,200,30,'#fff4c8')+glow(560,200,60,'#fff4c8',.6)+'<path d="M0 640 Q400 500 800 640 L800 800 L0 800Z" fill="#2a2440"/>'
b+=figure(340,580,200,'#0a0a14')+figure(430,580,190,'#0a0a14',hair='#0a0a14')+'<path d="M450 470 L520 400" stroke="#0a0a14" stroke-width="10" stroke-linecap="round"/>'
I[43]=svg(b,d)

# 445 KISSに撃たれて眠りたい: a lipstick kiss mark shaped like a bullet hole on a cracked mirror, 1993 rock
d,b=bg([(0,'#1a0a14'),(1,'#4a0a1a')])
b+='<rect x="160" y="140" width="480" height="520" rx="20" fill="#3a3a4a" stroke="#c8a24a" stroke-width="16"/>'+''.join(f'<path d="M400 400 L{400+300*math.cos(a)} {400+300*math.sin(a)}" stroke="#d8d8e8" stroke-width="3"/>' for a in [k*math.pi/4+.2 for k in range(8)])
b+='<g transform="translate(400 400) scale(2.6) translate(-400 -400)"><path d="M340 400 Q370 360 400 385 Q430 360 460 400 Q430 410 400 405 Q370 410 340 400Z M340 400 Q400 450 460 400 Q430 430 400 432 Q370 430 340 400Z" fill="#e8102a"/></g>'
I[445]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
