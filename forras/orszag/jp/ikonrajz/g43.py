import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 43. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 505 ダンスホール: a lonely girl's silhouette in a smoky dance hall under coloured lights, 1985 rock
d,b=bg([(0,'#1a0a2a'),(1,'#3a1a3a')])
b+=''.join(f'<path d="M{x} 0 L{x-80} 640 L{x+80} 640Z" fill="{c}" opacity=".15"/>' for x,c in [(160,'#ff4a8a'),(400,'#4ad0ff'),(640,'#ffd02a')])+''.join(f'<ellipse cx="{x}" cy="{y}" rx="180" ry="30" fill="#fff" opacity=".06"/>' for x,y in [(200,400),(560,320),(400,520)])
b+='<rect y="640" width="800" height="160" fill="#14101a"/>'+''.join(f'<rect x="{x}" y="640" width="80" height="80" fill="{"#2a1a2a" if (x//80)%2 else "#1a101a"}"/>' for x in range(0,800,80))+figure(400,660,300,'#000',hair='#000')
I[505]=svg(b,d)

# 1173 This Love: a grand piano by a window with a single white feather resting on the keys, 2006 ballad
d,b=bg([(0,'#d8e4f0'),(1,'#f4f0e8')])
b+='<rect x="420" y="80" width="300" height="400" fill="#fff"/>'+glow(570,280,180,'#fff',.5)+'<rect x="420" y="80" width="300" height="400" fill="none" stroke="#8a8a9a" stroke-width="12"/>'
b+='<path d="M100 520 Q100 420 220 420 L500 420 Q620 440 620 520Z" fill="#111"/><rect x="100" y="520" width="520" height="40" fill="#1a1a1a"/>'+''.join(f'<rect x="{x}" y="520" width="12" height="26" fill="#fff"/>' for x in range(120,600,16))+'<path d="M140 420 L520 240" stroke="#111" stroke-width="14"/>'
b+='<g transform="rotate(-20 340 500)"><path d="M300 500 Q360 470 400 500 Q360 520 300 500Z" fill="#fff"/></g><rect y="560" width="800" height="240" fill="#8a7a6a"/>'
I[1173]=svg(b,d)

# 8 柔: a judo black belt neatly folded on a tatami mat beside a single camellia, 1964 Tokyo Olympics era
d,b=bg([(0,'#e8dcc0'),(1,'#c8b890')])
b+=''.join(f'<rect x="{x}" y="{y}" width="400" height="200" fill="#d8c890" stroke="#8a7a50" stroke-width="6"/>' for x,y in [(0,400),(400,400),(0,600),(400,600)])+'<rect x="0" y="0" width="800" height="400" fill="#f4ecd8"/>'
b+='<rect x="220" y="500" width="360" height="60" fill="#1a1a1a"/><path d="M380 560 L340 700 L380 700 L400 580 L420 700 L460 700 L420 560Z" fill="#1a1a1a"/><rect x="370" y="490" width="60" height="80" fill="#1a1a1a"/>'+flower(640,500,50,5,'#c8102a','#ffd02a')
I[8]=svg(b,d)

# 107 TOKIO: a glam-rock silhouette floating down on a parachute over a glittering neon Tokyo with Tokyo Tower
d,b=bg([(0,'#0a0a2a'),(1,'#5a1a5a')])
b+=skyline(800,'#0a0a1a',107,120,300,'#ff8ad0',100)+tokyo_tower(620,800,460)
b+='<path d="M180 220 Q320 100 460 220Z" fill="#e8302a"/><path d="M180 220 Q250 190 320 220 Q390 190 460 220" fill="#c8102a"/><path d="M180 220 L320 380 M460 220 L320 380 M320 220 L320 380" stroke="#ddd" stroke-width="3"/>'+figure(320,500,130,'#000',pose='up')
I[107]=svg(b,d)

# 164 酒よ: a lone man at a small bar counter staring into his sake cup, a single bulb overhead, 1988 enka
d,b=bg([(0,'#1a1410'),(1,'#3a2a20')])
b+='<path d="M400 0 L400 120" stroke="#555" stroke-width="3"/><circle cx="400" cy="140" r="20" fill="#ffd27a"/>'+glow(400,160,240,'#ffb070',.35)+'<rect y="520" width="800" height="280" fill="#5a3a24"/><rect y="500" width="800" height="24" fill="#7a4a2a"/>'
b+=figure(320,560,300,'#0a0a0a')+'<path d="M440 470 L500 470 L490 500 L450 500Z" fill="#f4ece0"/><path d="M540 500 L540 380 Q540 350 560 340 L560 310 L580 310 L580 340 Q600 350 600 380 L600 500Z" fill="#f4ece0"/>'
I[164]=svg(b,d)

# 461 おっと CHIKAN!: a crowded train's hand straps with a girl's hand blowing an alarm whistle, comic idol warning
d,b=bg([(0,'#d8e4f0'),(1,'#b8c4d8')])
b+='<rect x="0" y="60" width="800" height="24" fill="#8a8a9a"/>'+''.join(f'<path d="M{x} 84 L{x} 180" stroke="#8a8a9a" stroke-width="5"/><path d="M{x-24} 180 Q{x} 230 {x+24} 180 Q{x+24} 250 {x} 250 Q{x-24} 250 {x-24} 180Z" fill="none" stroke="#e8e8f0" stroke-width="10"/>' for x in range(100,800,150))
b+=''.join(figure(x,880,300,'#5a6070') for x in (100,250,550,700))+'<path d="M300 800 L360 520 Q380 480 420 480 L460 470" stroke="#f4c8a8" stroke-width="40" fill="none" stroke-linecap="round"/><rect x="450" y="440" width="90" height="50" rx="20" fill="#e8302a"/>'
b+=''.join(f'<path d="M{560+k*30} {430-k*20} l30 -20" stroke="#e8302a" stroke-width="8" stroke-linecap="round"/>' for k in range(3))
I[461]=svg(b,d)

# 567 パンドラの恋人: an ornate box cracking open with butterflies and a heart of light escaping, 80s idol
d,b=bg([(0,'#1a0a3a'),(1,'#6a3a8a')])
b+='<rect x="240" y="460" width="320" height="200" fill="#6a3a1a" stroke="#c8a24a" stroke-width="8"/><path d="M230 460 L400 400 L570 460" fill="#7a4a2a" stroke="#c8a24a" stroke-width="8"/>'+glow(400,400,200,'#fff4c8',.6)+heart(400,330,50,'#ff6aa8')
b+=''.join(f'<g transform="translate({x} {y}) rotate({r})"><ellipse cx="-12" cy="0" rx="14" ry="20" fill="{c}"/><ellipse cx="12" cy="0" rx="14" ry="20" fill="{c}"/></g>' for x,y,r,c in [(260,260,-20,'#8ad0ff'),(540,220,20,'#ffd02a'),(600,340,10,'#ff8ad0'),(200,380,-30,'#fff')])
I[567]=svg(b,d)

# 586 白いクリスマス: a punk-rock kid with a guitar case walking through a snowy street on Christmas night
d,b=bg([(0,'#1a2440'),(1,'#3a4a6a')])
b+=snow(100,586)+skyline(600,'#141a30',586,60,200,'#ffd27a',50)+'<rect y="600" width="800" height="200" fill="#e8eef8"/>'+''.join(f'<circle cx="{x}" cy="{220+30*math.sin(x/100)}" r="6" fill="{["#ff4a4a","#5ad85a","#ffd02a"][(x//60)%3]}"/>' for x in range(20,800,60))
b+=figure(400,640,260,'#0a0a14')+'<rect x="430" y="520" width="40" height="130" rx="16" fill="#0a0a14" transform="rotate(10 450 585)"/>'
I[586]=svg(b,d)

# 1676 雨の御堂筋: a rainy tree-lined Osaka boulevard at night with ginkgo trees and blurred car lights
d,b=bg([(0,'#1a1a2a'),(1,'#3a3040')])
b+=rain(90,1676,'#cfe6ff',.4)+'<path d="M380 360 L100 800 L700 800 L420 360Z" fill="#2a2a34"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#c8a83a" opacity=".8"/><rect x="{x-4}" y="{y}" width="8" height="{r*2}" fill="#2a2018"/>' for x,y,r in [(120,500,60),(220,430,44),(290,390,30),(680,500,60),(580,430,44),(510,390,30)])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="{c}"/>' for x,y,c in [(360,700,'#ff4a4a'),(400,700,'#ff4a4a'),(430,560,'#fff4c8'),(450,560,'#fff4c8')])+figure(260,780,200,'#000',hair='#000')+wagasa(260,580,80,'#c8102a',-8)
I[1676]=svg(b,d)

# 1735 意外にマンゴー: a ripe mango sliced into a hedgehog cube beside a sunny tropical drink, idol summer pop
d,b=bg([(0,'#ffd04a'),(1,'#ff9a5a')])
b+=rays(400,300,20,'#fff',.2,10)+'<ellipse cx="380" cy="460" rx="190" ry="140" fill="#ffb02a"/>'+''.join(f'<rect x="{x}" y="{y}" width="50" height="50" rx="10" fill="#ffc84a" stroke="#e8902a" stroke-width="3"/>' for x in range(240,520,56) for y in range(370,560,56))
b+='<path d="M560 320 L680 320 L660 560 L580 560Z" fill="#fff" opacity=".5"/><path d="M566 380 L674 380 L660 560 L580 560Z" fill="#ff8a2a"/><path d="M640 320 L700 180" stroke="#3ab0ff" stroke-width="10"/>'
I[1735]=svg(b,d)

# 82 宗右衛門町ブルース: a neon-lit Osaka entertainment street reflected in a canal with a lone woman, 1972 enka
d,b=bg([(0,'#1a0a24'),(1,'#3a1a3a')])
b+=''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" opacity=".85"/>' for x,y,w,h,c in [(60,120,60,200,'#ff4fa0'),(160,180,50,160,'#4fd0ff'),(560,100,70,220,'#ffd02a'),(670,160,60,180,'#ff4fa0')])+'<rect y="420" width="800" height="380" fill="#0a0a1a"/>'
b+=''.join(f'<rect x="{x}" y="{440+k*30}" width="{w}" height="10" fill="{c}" opacity="{.4-k*.06}"/>' for x,w,c in [(60,60,'#ff4fa0'),(160,50,'#4fd0ff'),(560,70,'#ffd02a'),(670,60,'#ff4fa0')] for k in range(6))
b+='<rect x="0" y="400" width="800" height="24" fill="#2a1a2a"/>'+figure(400,410,200,'#000',hair='#000')
I[82]=svg(b,d)

# 151 夫婦坂: an elderly couple slowly climbing a stone-stepped slope hand in hand under maple trees, enka
d,b=bg([(0,'#e8a87a'),(1,'#f8e0c8')])
b+=''.join(f'<rect x="{180+k*30}" y="{720-k*60}" width="{440-k*60}" height="20" fill="#a8988a"/>' for k in range(9))+tree(120,700,400,'#c8402a',151)+tree(680,700,380,'#e8602a',1511)
b+=figure(360,540,160,'#2a1a1a')+figure(430,540,150,'#2a1a1a',hair='#2a1a1a')
I[151]=svg(b,d)

# 511 19 GROWING UP: two girls' silhouettes on a rooftop sharing earphones at sunset, 80s girl band
d,b=bg([(0,'#ff6a8a'),(1,'#ffd08a')])
b+='<circle cx="400" cy="460" r="90" fill="#fff0b0"/>'+skyline(600,'#5a2a4a',511,40,160)+'<rect y="600" width="800" height="200" fill="#3a1a2a"/><rect x="0" y="580" width="800" height="20" fill="#5a3a4a"/>'
b+=figure(340,600,220,'#1a0a14',hair='#1a0a14')+figure(460,600,220,'#1a0a14',hair='#1a0a14')+'<path d="M350 400 Q400 460 450 400" stroke="#fff" stroke-width="3" fill="none"/>'
I[511]=svg(b,d)

# 1179 1LDK: a tiny one-room apartment seen from outside at night, one lit window with two mugs, R&B
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+=starsf(40,1179,300)+'<rect x="160" y="160" width="480" height="640" fill="#2a2a34"/>'+''.join(f'<rect x="{x}" y="{y}" width="100" height="80" fill="#14141e"/>' for x in (200,350,500) for y in (200,330,460,590))
b+='<rect x="350" y="330" width="100" height="80" fill="#ffd27a"/>'+glow(400,370,100,'#ffd27a',.5)+'<rect x="368" y="380" width="16" height="20" fill="#f4f0e8"/><rect x="414" y="380" width="16" height="20" fill="#f4f0e8"/>'
I[1179]=svg(b,d)

# 1725 OUR DAYS: a scrapbook of polaroid photos of friends pinned with tape, 1999 pop
d,b=bg([(0,'#ffe8d8'),(1,'#f0e0f0')])
for x,y,r,c in [(220,240,-10,'#8ad0ff'),(520,220,8,'#ffd02a'),(300,500,6,'#ff8ab0'),(560,520,-6,'#5ad87a')]:
  b+=f'<g transform="rotate({r} {x} {y})"><rect x="{x-110}" y="{y-120}" width="220" height="240" fill="#fff" stroke="#ddd" stroke-width="2"/><rect x="{x-94}" y="{y-104}" width="188" height="170" fill="{c}"/>'+figure(x-30,y+66,110,'#2a2a3a')+figure(x+30,y+66,100,'#2a2a3a',hair='#2a2a3a')+f'<rect x="{x-30}" y="{y-134}" width="60" height="24" fill="#f4e8a0" opacity=".8"/></g>'
I[1725]=svg(b,d)

# 1835 光戦隊マスクマン: five beams of coloured light bursting from a glowing prism into the sky, tokusatsu theme
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=starsf(50,1835,500)+''.join(f'<path d="M400 520 L{x} 0" stroke="{c}" stroke-width="22" opacity=".7"/>' for x,c in [(100,'#e8302a'),(250,'#1a6aff'),(400,'#ffd02a'),(550,'#ff6aa8'),(700,'#3ad85a')])
b+='<circle cx="400" cy="530" r="60" fill="#fff"/>'+glow(400,530,160,'#fff',.7)+figure(400,600,200,'#0a0a14',pose='up')+'<rect y="600" width="800" height="200" fill="#0a0a14"/>'
I[1835]=svg(b,d)

# 189 永遠の嘘をついてくれ: a man in a coat at an airport window watching a plane take off at night, 1995 folk-rock
d,b=bg([(0,'#0a1028'),(1,'#2a3458')])
b+=starsf(40,189,400)+'<path d="M200 300 L300 280 L340 240 L360 250 L340 290 L440 300 L440 310 L340 310 L320 340 L300 340 L310 310 L200 310Z" fill="#c8c8d0" transform="rotate(-14 320 300)"/><circle cx="440" cy="296" r="5" fill="#ff4a4a"/>'
b+='<rect x="0" y="420" width="800" height="380" fill="#14182a"/>'+''.join(f'<circle cx="{x}" cy="440" r="5" fill="#4a8aff"/>' for x in range(20,800,50))+'<rect x="0" y="0" width="800" height="800" fill="none" stroke="#0a0a14" stroke-width="40"/>'+figure(600,800,360,'#000')
I[189]=svg(b,d)

# 475 RASPBERRY DREAM: a giant glossy raspberry floating in a dreamy pink night sky with stars, 80s rock
d,b=bg([(0,'#2a0a3a'),(1,'#ff4a8a')])
b+=starsf(60,475,500)+''.join(f'<circle cx="{400+dx}" cy="{420+dy}" r="34" fill="#c8103a"/><circle cx="{390+dx}" cy="{410+dy}" r="10" fill="#fff" opacity=".4"/>' for dx,dy in [(0,0),(-60,-20),(60,-20),(-30,-80),(30,-80),(-50,50),(50,50),(0,100),(0,-140),(-90,40),(90,40),(-20,-30),(30,20)])
b+='<path d="M360 270 L400 240 L440 270 L420 280 L400 260 L380 280Z" fill="#3a8a3a"/>'+glow(400,420,200,'#ff4a8a',.3)
I[475]=svg(b,d)

# 1093 愛し君へ: a hand-written note tucked into a single sunflower on a windowsill, gentle 2004 ballad
d,b=bg([(0,'#cfe8ff'),(1,'#fff8e0')])
b+='<rect x="120" y="80" width="560" height="420" fill="#e8f4ff"/><rect x="120" y="80" width="560" height="420" fill="none" stroke="#a8988a" stroke-width="16"/><rect x="80" y="500" width="640" height="34" fill="#a8988a"/><rect y="534" width="800" height="266" fill="#7a6a5a"/>'
b+='<rect x="370" y="420" width="60" height="80" fill="#cfe6ff" opacity=".6" stroke="#fff" stroke-width="3"/><path d="M400 420 L400 260" stroke="#3a7a2a" stroke-width="8"/>'+flower(400,240,70,14,'#ffd02a','#6a4a1a',0,.5)+'<rect x="420" y="320" width="80" height="54" fill="#fff" transform="rotate(12 460 347)"/>'
I[1093]=svg(b,d)

# 1145 夢の蕾: a bud on a young sapling about to bloom on a graduation morning, warm rock ballad
d,b=bg([(0,'#9ad0ff'),(1,'#fff4e0')])
b+='<circle cx="600" cy="200" r="70" fill="#fff8d0"/>'+rays(600,200,16,'#fff',.25,10)+'<path d="M0 600 Q400 560 800 600 L800 800 L0 800Z" fill="#8ac86a"/>'
b+='<path d="M400 640 Q390 480 410 340" stroke="#5a3a2a" stroke-width="12" fill="none"/><path d="M400 500 q-70 -30 -90 10 q50 16 90 -10Z M405 440 q70 -30 90 10 q-50 16 -90 -10Z" fill="#5ab84a"/><path d="M410 340 Q380 300 410 250 Q440 300 410 340Z" fill="#ff8ab0"/><path d="M410 340 Q395 310 410 280" stroke="#e85a8a" stroke-width="3" fill="none"/>'
I[1145]=svg(b,d)

# 9 越後獅子の唄: a child performer's lion-dance headpiece and drum on a dusty country road, 1950
d,b=bg([(0,'#c8a87a'),(1,'#e8d8b8')])
b+=hills(440,40,'#a8906a',9,4)+'<rect y="480" width="800" height="320" fill="#c8b088"/>'
b+='<path d="M300 420 Q300 320 400 310 Q500 320 500 420 L480 470 L320 470Z" fill="#c8302a"/><circle cx="360" cy="380" r="16" fill="#ffd02a"/><circle cx="440" cy="380" r="16" fill="#ffd02a"/><path d="M330 440 L470 440" stroke="#f4f0e8" stroke-width="10"/><path d="M300 420 Q260 440 250 500 M500 420 Q540 440 550 500" stroke="#f4f0e8" stroke-width="14" fill="none"/>'
b+='<ellipse cx="560" cy="600" rx="60" ry="20" fill="#f4ece0"/><rect x="500" y="600" width="120" height="60" fill="#8a3a1a"/><ellipse cx="560" cy="660" rx="60" ry="20" fill="#6a2a14"/>'+figure(240,680,180,'#3a2a1a')
I[9]=svg(b,d)

# 61 ブルー・シャトウ: a fairy-tale blue castle by a misty forest lake at dusk, 1967 group sounds
d,b=bg([(0,'#3a4a8a'),(1,'#a8b8e8')])
b+=hills(480,40,'#1a3a3a',61,6)+'<rect y="500" width="800" height="300" fill="#2a4a7a"/>'
b+=''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{500-y}" fill="#5a7ad8"/><path d="M{x-10} {y} L{x+w/2} {y-60} L{x+w+10} {y}Z" fill="#2a3a8a"/>' for x,y,w in [(300,300,60),(440,300,60),(360,240,80)])+'<rect x="300" y="380" width="200" height="120" fill="#5a7ad8"/>'
b+='<g transform="translate(0 1000) scale(1 -1)" opacity=".3">'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{500-y}" fill="#8ab0ff"/>' for x,y,w in [(300,300,60),(440,300,60),(360,240,80)])+'</g>'+moon(620,140,40)
I[61]=svg(b,d)

# 108 カサブランカ・ダンディ: a fedora tipped over a whisky glass and a trench coat on a bar stool, 1979 glam
d,b=bg([(0,'#1a1410'),(1,'#3a2a1a')])
b+=glow(400,260,240,'#ffb070',.3)+'<rect y="520" width="800" height="280" fill="#3a2414"/><rect x="0" y="500" width="800" height="24" fill="#6a4a2a"/>'
b+='<ellipse cx="300" cy="490" rx="120" ry="20" fill="#2a2a2a"/><path d="M230 490 Q240 400 300 400 Q360 400 370 490Z" fill="#2a2a2a"/><rect x="234" y="470" width="132" height="16" fill="#6a1a1a"/>'
b+='<path d="M480 400 L560 400 L550 500 L490 500Z" fill="#f4ece0" opacity=".5"/><path d="M484 440 L556 440 L550 500 L490 500Z" fill="#c8802a"/><rect x="496" y="452" width="22" height="22" fill="#e8f4ff" opacity=".7"/>'
I[108]=svg(b,d)

# 168 もう一度逢いたい: a faded photo in a cracked frame on a rainy windowsill, 1976 enka
d,b=bg([(0,'#4a4a5a'),(1,'#8a8a9a')])
b+=rain(60,168,'#e8f0ff',.35,8,500)+'<rect y="500" width="800" height="300" fill="#4a3a30"/><rect x="280" y="300" width="240" height="220" fill="#c8a870"/><rect x="300" y="320" width="200" height="180" fill="#e0d4b8"/>'+profile(410,500,.8,'#8a7a5a')+'<path d="M300 340 L380 420 L360 470" stroke="#fff" stroke-width="3" fill="none"/>'
I[168]=svg(b,d)

# 809 たのしく たのしく やさしくね: a smiling cartoon cloud raining candy and flowers over a playground, 90s pop
d,b=bg([(0,'#9ad8ff'),(1,'#fff4f8')])
b+=cloud(400,220,2.4,'#fff')+'<circle cx="360" cy="220" r="8" fill="#3a3a4a"/><circle cx="440" cy="220" r="8" fill="#3a3a4a"/><path d="M370 250 Q400 280 430 250" stroke="#3a3a4a" stroke-width="6" fill="none"/>'
b+=''.join(flower(x,y,16,5,c,'#ffd02a') for x,y,c in [(260,400,'#ff8ab0'),(400,460,'#ffd02a'),(540,380,'#8ad0ff'),(320,540,'#5ad87a'),(480,560,'#ff8ab0')])+'<rect y="660" width="800" height="140" fill="#8ad06a"/>'
I[809]=svg(b,d)

# 852 鼓動: a glowing heart beating inside a dark ribcage-like rock arena with sound rings, 2007 rock
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a0a')])
b+=''.join(ring(400,400,r,'#ff3a3a',6,1-r/400) for r in (130,200,270,340))+heart(400,410,90,'#e8102a')+glow(400,400,160,'#ff3a3a',.5)
I[852]=svg(b,d)

# 1267 LPS: vinyl records spinning in a row on a turntable shelf glowing in retro colours, 2018 boy group
d,b=bg([(0,'#1a1a3a'),(1,'#3a2a5a')])
b+=''.join(f'<circle cx="{x}" cy="400" r="110" fill="#111"/>'+''.join(ring(x,400,r,'#2a2a2a',2) for r in range(50,110,14))+f'<circle cx="{x}" cy="400" r="40" fill="{c}"/><circle cx="{x}" cy="400" r="6" fill="#111"/>' for x,c in [(160,'#ff6aa0'),(400,'#ffd02a'),(640,'#3ab0ff')])
b+='<rect y="540" width="800" height="260" fill="#14142a"/>'
I[1267]=svg(b,d)

# 1278 ここに: a group of friends' hands stacked together in a circle seen from above, 2018 boy band
d,b=bg([(0,'#ffd88a'),(1,'#ffeccc')])
b+=rays(400,400,20,'#fff',.25,12)+''.join(f'<path d="M{400+380*math.cos(a)} {400+380*math.sin(a)} L{400+60*math.cos(a)} {400+60*math.sin(a)}" stroke="{c}" stroke-width="64" stroke-linecap="round"/>' for a,c in [(k*2*math.pi/7,['#e8a888','#c88868','#f4c8a8','#a86848','#d8987a','#b87858','#e8b898'][k]) for k in range(7)])
I[1278]=svg(b,d)

# 1739 欲望者: a glowing red apple on a pedestal with clawing shadowy hands reaching for it, idol rock
d,b=bg([(0,'#0a0a0a'),(1,'#3a0a14')])
b+='<rect x="340" y="500" width="120" height="300" fill="#2a2a2a"/><rect x="310" y="480" width="180" height="30" fill="#3a3a3a"/>'+'<circle cx="400" cy="420" r="60" fill="#e8102a"/><path d="M400 360 L404 330" stroke="#3a2a1a" stroke-width="6"/><path d="M404 340 q20 -20 40 -6 q-20 16 -40 6Z" fill="#3a8a3a"/>'+glow(400,420,120,'#ff3a3a',.5)
b+=''.join(f'<path d="M{x} 800 L{x+dx} 520 L{x+dx-20} 480 M{x+dx} 520 L{x+dx} 470 M{x+dx} 520 L{x+dx+20} 480" stroke="#000" stroke-width="22" stroke-linecap="round" fill="none"/>' for x,dx in [(120,80),(680,-80),(220,40),(580,-40)])
I[1739]=svg(b,d)

# 1789 ホメチギリスト: a shower of gold stars and clapping hands raining praise on a smiling figure, boy group pop
d,b=bg([(0,'#ffe04a'),(1,'#ffb84a')])
b+=rays(400,300,20,'#fff',.3,12)+''.join(star5(x,y,s,'#fff') for x,y,s in [(160,180,30),(640,160,36),(260,320,20),(560,340,24),(400,120,28)])
b+=figure(400,760,320,'#5a2a0a',pose='up')+''.join(f'<path d="M{x} {y} q-20 -30 0 -50 q20 20 0 50Z M{x+16} {y} q20 -30 0 -50" fill="#f4c8a8" stroke="#c8906a" stroke-width="3"/>' for x,y in [(120,560),(640,540)])
I[1789]=svg(b,d)

# 42 薩摩の女: a woman's silhouette with Sakurajima volcano smoking across the bay at dusk, 1968 enka
d,b=bg([(0,'#8a4a5a'),(1,'#ffb08a')])
b+='<path d="M380 460 L520 280 L560 280 L720 460Z" fill="#5a3a4a"/><path d="M540 280 Q520 200 560 140 Q600 80 580 40" stroke="#c8b8b8" stroke-width="40" fill="none" opacity=".6" stroke-linecap="round"/>'
b+='<rect y="460" width="800" height="340" fill="#4a5a8a"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(100,520),(400,560),(600,620)])+'<path d="M0 600 L320 600 L320 800 L0 800Z" fill="#2a1a24"/>'+figure(180,600,240,'#0a0a10',hair='#0a0a10')
I[42]=svg(b,d)

# 85 北国の春: white magnolia blossoms and birch trees beside a melting stream in a northern spring, 1977
d,b=bg([(0,'#a8d0f0'),(1,'#f4f8f0')])
b+=''.join(f'<rect x="{x}" y="160" width="20" height="640" fill="#f4f4f0"/>'+''.join(f'<rect x="{x}" y="{y}" width="20" height="6" fill="#3a3a3a"/>' for y in range(200,800,70)) for x in (100,180,660))
b+='<path d="M300 800 Q360 600 420 520 Q480 440 560 420" stroke="#7ab0e8" stroke-width="50" fill="none"/>'+'<rect y="700" width="800" height="100" fill="#e8eef8" opacity=".7"/>'
b+='<path d="M800 200 Q620 240 500 320" stroke="#5a3a2a" stroke-width="12" fill="none"/>'+''.join(flower(x,y,30,6,'#fff','#ffe0e8',r) for x,y,r in [(700,220,0),(600,260,20),(520,310,40),(640,320,10)])
I[85]=svg(b,d)

# 476 Friends: two bicycles leaning together against a school fence at sunset, 80s rock
d,b=bg([(0,'#ff7a5a'),(1,'#ffd8a0')])
b+='<circle cx="400" cy="420" r="90" fill="#fff0b0"/><rect y="520" width="800" height="280" fill="#6a4a4a"/>'+''.join(f'<rect x="{x}" y="380" width="8" height="160" fill="#3a2a2a"/>' for x in range(0,800,40))+'<rect y="400" width="800" height="8" fill="#3a2a2a"/>'
for x,r in [(280,-6),(480,6)]:
  b+=f'<g transform="rotate({r} {x} 600)">'+ring(x-70,640,50,'#1a1a1a',8)+ring(x+70,640,50,'#1a1a1a',8)+f'<path d="M{x-70} 640 L{x} 570 L{x+70} 640 M{x} 570 L{x+30} 550" stroke="#1a1a1a" stroke-width="8" fill="none"/></g>'
I[476]=svg(b,d)

# 681 星の指輪: a ring made of starlight circling a full moon over a calm sea, 1993 rock ballad
d,b=bg([(0,'#050a24'),(1,'#1a2a5a')])
b+=starsf(80,681,480)+moon(400,300,100)+'<ellipse cx="400" cy="300" rx="190" ry="60" fill="none" stroke="#fff4c8" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round"/>'+star5(580,280,24,'#fff')+glow(580,280,40,'#fff',.6)
b+='<rect y="480" width="800" height="320" fill="#0a1430"/>'+''.join(f'<rect x="{380-k*8}" y="{500+k*40}" width="{40+k*16}" height="6" fill="#fff4c8" opacity=".5"/>' for k in range(7))
I[681]=svg(b,d)

# 27 有楽町で逢いましょう: a couple meeting under umbrellas outside a glowing department store on a rainy night, 1957
d,b=bg([(0,'#1a1a2a'),(1,'#3a3044')])
b+=rain(80,27,'#cfe6ff',.35)+'<rect x="80" y="120" width="640" height="460" fill="#2a2430"/>'+''.join(f'<rect x="{x}" y="{y}" width="80" height="60" fill="#ffd27a" opacity=".8"/>' for x in range(120,700,120) for y in (160,260,360))+'<rect y="580" width="800" height="220" fill="#14141e"/>'
b+=figure(320,720,220,'#000')+figure(460,720,210,'#000',hair='#000')+wagasa(320,520,90,'#2a2a3a',-10)+wagasa(460,520,90,'#c8302a',10)
I[27]=svg(b,d)

# 93 逢いたくてしかたない: a mobile-phone-era figure watching a train window pass by in the rain at night, 1995
d,b=bg([(0,'#0a1028'),(1,'#2a3050')])
b+=rain(70,93,'#cfe6ff',.35)+'<rect x="0" y="300" width="800" height="200" fill="#c8ccd8"/>'+''.join(f'<rect x="{x}" y="330" width="120" height="90" fill="#ffe8b0"/>' for x in range(30,800,160))+'<rect y="500" width="800" height="300" fill="#14141e"/>'+figure(400,780,300,'#000')
I[93]=svg(b,d)

# 137 古い日記: an old diary lying open with dried pressed flowers and a ribbon bookmark, 1974
d,b=bg([(0,'#c8b08a'),(1,'#e8d8b8')])
b+='<path d="M120 300 L400 340 L680 300 L680 640 L400 680 L120 640Z" fill="#f4ecd8" stroke="#a8906a" stroke-width="6"/><path d="M400 340 L400 680" stroke="#a8906a" stroke-width="6"/>'+''.join(f'<path d="M160 {y} L360 {y+10} M440 {y+10} L640 {y}" stroke="#c8b898" stroke-width="3"/>' for y in range(380,620,30))
b+=flower(520,480,40,5,'#c87a8a','#e8c870')+'<path d="M400 340 L410 760" stroke="#c8302a" stroke-width="10"/>'
I[137]=svg(b,d)

# 257 Lemon: a bright lemon falling from a bridge toward a train passing far below a gorge, 1978 folk
d,b=bg([(0,'#c8d8e8'),(1,'#f0f0e8')])
b+='<path d="M0 0 L240 0 L280 800 L0 800Z" fill="#7a8a6a"/><path d="M800 0 L560 0 L520 800 L800 800Z" fill="#7a8a6a"/><rect x="0" y="120" width="800" height="40" fill="#5a5a64"/>'+''.join(f'<rect x="{x}" y="160" width="12" height="40" fill="#5a5a64"/>' for x in range(240,560,40))
b+='<rect x="260" y="640" width="280" height="70" rx="10" fill="#e8a83a"/>'+''.join(f'<rect x="{x}" y="656" width="34" height="26" fill="#3a3a4a"/>' for x in range(276,530,50))+'<rect y="720" width="800" height="80" fill="#3a5a7a"/>'
b+='<ellipse cx="420" cy="380" rx="44" ry="32" fill="#ffe02a" transform="rotate(20 420 380)"/><circle cx="458" cy="394" r="6" fill="#d8b81a"/>'+''.join(f'<path d="M{x} {y} l-6 -30" stroke="#888" stroke-width="3"/>' for x,y in [(400,330),(430,320)])
I[257]=svg(b,d)

# 14 心の瞳: two old hands holding each other with a soft light shining from the joined palms, 1985 ballad
d,b=bg([(0,'#f4e0c8'),(1,'#e8d0b8')])
b+=glow(400,420,220,'#fff4d8',.7)+'<path d="M0 520 Q160 460 320 430 L400 440 L380 500 Q200 540 0 620Z" fill="#c8987a"/><path d="M800 520 Q640 460 480 430 L400 440 L420 500 Q600 540 800 620Z" fill="#b8886a"/>'
b+=''.join(f'<path d="M{x} {y} q20 -10 40 0" stroke="#8a6a4a" stroke-width="3" fill="none"/>' for x,y in [(200,500),(240,480),(540,480),(580,500)])
I[14]=svg(b,d)

# 58 シー・シー・シー: a 60s group-sounds band's silhouettes in military-style jackets under a psychedelic sun
d,b=bg([(0,'#ff6a2a'),(1,'#ffd04a')])
b+=''.join(ring(400,280,r,c,22) for r,c in [(60,'#e8102a'),(110,'#ff8a2a'),(160,'#ffd02a'),(210,'#ff4a8a')])
b+='<rect y="640" width="800" height="160" fill="#2a0a1a"/>'+''.join(figure(x,660,260,'#1a0a14',hair='#1a0a14') for x in (160,280,400,520,640))+guitar(300,560,.5,30,'#1a0a14')+guitar(520,560,.5,-30,'#1a0a14')
I[58]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
