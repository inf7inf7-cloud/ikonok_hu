import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 44. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 84 黒ネコのタンゴ: a black cat dancing a tango with a red rose in its mouth, 1969 children's hit
d,b=bg([(0,'#ff6a5a'),(1,'#ffd8a0')])
b+='<rect y="640" width="800" height="160" fill="#5a2a2a"/>'+''.join(f'<rect x="{x}" y="640" width="80" height="80" fill="#3a1a1a"/>' for x in range(0,800,160))
b+='<ellipse cx="400" cy="480" rx="90" ry="140" fill="#111"/><circle cx="400" cy="300" r="70" fill="#111"/><path d="M340 260 L350 200 L380 240Z M460 260 L450 200 L420 240Z" fill="#111"/><circle cx="375" cy="295" r="10" fill="#ffd02a"/><circle cx="425" cy="295" r="10" fill="#ffd02a"/>'
b+='<path d="M480 560 Q600 520 580 420" stroke="#111" stroke-width="18" fill="none" stroke-linecap="round"/><path d="M330 420 L240 340 M470 420 L560 360" stroke="#111" stroke-width="22" stroke-linecap="round"/><path d="M360 600 L320 680 M440 600 L500 660" stroke="#111" stroke-width="22" stroke-linecap="round"/>'+rose(400,340,.5,90)
I[84]=svg(b,d)

# 258 案山子: a lonely scarecrow in a harvested rice field under an autumn sky with a letter tied on, 1977 folk
d,b=bg([(0,'#e8b07a'),(1,'#f8e8c8')])
b+='<rect y="500" width="800" height="300" fill="#c8a050"/>'+''.join(f'<path d="M{x} 800 L{x+8} {540+(x%4)*10}" stroke="#a8803a" stroke-width="5"/>' for x in range(10,800,24))
b+='<rect x="392" y="300" width="16" height="400" fill="#6a4a2a"/><rect x="260" y="380" width="280" height="16" fill="#6a4a2a"/><path d="M330 380 L470 380 L480 520 L320 520Z" fill="#5a7a9a"/><circle cx="400" cy="320" r="40" fill="#f4e8c8"/><ellipse cx="400" cy="290" rx="80" ry="16" fill="#d8b860"/><path d="M350 290 Q400 240 450 290Z" fill="#d8b860"/>'
b+='<rect x="490" y="410" width="60" height="44" fill="#fff" transform="rotate(10 520 432)"/>'+bird(160,200,24,'#3a2a2a')+bird(220,170,20,'#3a2a2a')
I[258]=svg(b,d)

# 352 さすらい: a drifter in a long coat walking alone along a desolate highway at dusk, 1980 city pop
d,b=bg([(0,'#3a3a6a'),(1,'#e8906a')])
b+='<rect y="500" width="800" height="300" fill="#4a3a44"/><path d="M380 500 L120 800 L680 800 L420 500Z" fill="#2a2430"/><path d="M400 520 L400 800" stroke="#c8a870" stroke-width="5" stroke-dasharray="24 20"/>'
b+=''.join(f'<rect x="{x}" y="340" width="6" height="{160}" fill="#2a2030"/>' for x in (80,700))+figure(500,720,280,'#0a0a10')
I[352]=svg(b,d)

# 353 Shadow City: long shadows of skyscrapers stretching over an empty midnight street, 1981
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=moon(140,120,40)+skyline(460,'#14142a',353,140,380,'#ffd27a',80)+'<rect y="460" width="800" height="340" fill="#2a2a3a"/>'+''.join(f'<path d="M{x} 460 L{x+60} 460 L{x+220} 800 L{x+120} 800Z" fill="#0a0a14" opacity=".7"/>' for x in (60,240,420,600))
b+=figure(380,700,180,'#000')+'<path d="M380 700 L560 780" stroke="#000" stroke-width="30" opacity=".6"/>'
I[353]=svg(b,d)

# 1681 HANDS UP: a forest of hands raised under exploding stage confetti cannons, 2019 boy group
d,b=bg([(0,'#1a0a3a'),(1,'#ff4a8a')])
b+=confetti(100,1681,['#ffd02a','#fff','#3ab0ff','#5ad87a'])+''.join(f'<path d="M{x} 800 L{x} {560-(x%7)*12}" stroke="#14081a" stroke-width="34" stroke-linecap="round"/><circle cx="{x}" cy="{550-(x%7)*12}" r="26" fill="#14081a"/>' for x in range(40,800,70))
I[1681]=svg(b,d)

# 1875 かけがえのない詩: a notebook page of lyrics turning into flying birds against a blue sky
d,b=bg([(0,'#5ab0ff'),(1,'#e0f4ff')])
b+='<path d="M160 520 L400 560 L640 520 L640 760 L400 800 L160 760Z" fill="#fff" stroke="#c8d0e0" stroke-width="4"/><path d="M400 560 L400 800" stroke="#c8d0e0" stroke-width="4"/>'+''.join(f'<path d="M190 {y} L370 {y+10} M430 {y+10} L610 {y}" stroke="#8ab0d8" stroke-width="3"/>' for y in range(590,760,30))
b+=''.join(bird(x,y,s,'#fff') for x,y,s in [(420,460,30),(470,380,34),(380,320,28),(520,260,36),(440,180,30),(600,160,24)])
I[1875]=svg(b,d)

# 160 もしかしてPARTII: a heart-shaped question mark glowing over a neon bar at night, 1984 enka-pop duet
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a4a')])
b+='<path d="M320 300 Q320 200 400 200 Q480 200 480 280 Q480 340 400 360 L400 440" stroke="#ff4fa0" stroke-width="30" fill="none" stroke-linecap="round"/>'+heart(400,520,36,'#ff4fa0')+glow(400,360,200,'#ff4fa0',.4)
b+='<rect y="640" width="800" height="160" fill="#14081a"/>'+figure(200,660,200,'#000')+figure(600,660,190,'#000',hair='#000')
I[160]=svg(b,d)

# 209 君の誕生日: a single lit candle on a small cake by a dark window with a wrapped gift, 1972 folk
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a3a')])
b+=glow(400,380,200,'#ffd27a',.4)+'<rect y="560" width="800" height="240" fill="#4a3424"/><rect x="300" y="460" width="200" height="100" rx="8" fill="#f4ece0"/><rect x="300" y="480" width="200" height="14" fill="#ff8ab0"/><rect x="394" y="400" width="12" height="60" fill="#ffc0d0"/><path d="M400 370 q10 14 0 26 q-10 -12 0 -26Z" fill="#ffd02a"/>'
b+='<rect x="560" y="480" width="100" height="80" fill="#3ab0ff"/><rect x="600" y="480" width="20" height="80" fill="#ffd02a"/><path d="M610 480 Q580 450 590 440 Q610 450 610 480 Q640 450 630 440 Q610 450 610 480" stroke="#ffd02a" stroke-width="6" fill="none"/>'
I[209]=svg(b,d)

# 506 街路樹: a row of street trees under streetlights at night with a lone youth walking, 1988 rock
d,b=bg([(0,'#0a0a1a'),(1,'#1a2030')])
b+='<rect y="560" width="800" height="240" fill="#1a1a24"/>'+''.join(f'<rect x="{x}" y="380" width="14" height="200" fill="#1a1414"/><circle cx="{x+7}" cy="360" r="{60-k*8}" fill="#1a3a2a"/>' for k,x in enumerate((80,240,400,560)))+''.join(f'<rect x="{x}" y="300" width="6" height="280" fill="#3a3a44"/><circle cx="{x+3}" cy="300" r="10" fill="#fff4c8"/>'+glow(x+3,310,60,'#fff4c8',.4) for x in (170,330,490,650))
b+=figure(560,720,220,'#000')
I[506]=svg(b,d)

# 507 太陽の破片: a shattered sun with glowing shards falling over a dark city, 1988 rock
d,b=bg([(0,'#1a0a0a'),(1,'#4a1a0a')])
b+='<circle cx="400" cy="280" r="130" fill="#ff8a2a"/>'+''.join(f'<path d="M400 280 L{400+150*math.cos(a)} {280+150*math.sin(a)}" stroke="#1a0a0a" stroke-width="6"/>' for a in [k*math.pi/3.5 for k in range(7)])+glow(400,280,200,'#ff6a2a',.5)
b+=''.join(f'<polygon points="{x},{y} {x+20},{y+30} {x-10},{y+40}" fill="#ffb02a"/>' for x,y in [(300,460),(460,500),(380,560),(520,420),(260,380)])+skyline(800,'#0a0a0a',507,80,240)
I[507]=svg(b,d)

# 923 ジャスミン: a sprig of white jasmine flowers glowing softly in moonlight, 2007 ballad
d,b=bg([(0,'#0a1a2a'),(1,'#2a3a5a')])
b+=moon(620,160,50)+'<path d="M160 700 Q300 500 420 420 Q520 360 620 340" stroke="#2a5a3a" stroke-width="8" fill="none"/>'+''.join(f'<path d="M{x} {y} q30 -10 40 -40 q-30 10 -40 40Z" fill="#3a7a4a"/>' for x,y in [(260,560),(380,450),(520,380)])
b+=''.join(flower(x,y,26,5,'#f4f4ff','#ffe8a0',x) for x,y in [(300,500),(420,420),(480,400),(560,350),(620,340),(350,470)])+glow(450,420,160,'#fff',.2)
I[923]=svg(b,d)

# 1682 PICK IT UP: a hand picking up a glowing microphone left on a dark stage floor, 2017 boy group
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+='<path d="M340 0 L460 0 L620 640 L180 640Z" fill="#fff" opacity=".12"/><rect y="640" width="800" height="160" fill="#14141e"/>'
b+='<g transform="rotate(-30 400 580)"><rect x="380" y="540" width="40" height="160" rx="16" fill="#2a2a34"/><circle cx="400" cy="520" r="40" fill="#8a8a9a"/></g>'+glow(400,560,120,'#8ad0ff',.4)+'<path d="M800 200 Q600 300 500 450 L470 430 Q560 280 760 160Z" fill="#000"/>'
I[1682]=svg(b,d)

# 904 熱帯夜: a sweltering tropical night: a swaying palm silhouette, a big red moon and fireflies, teen pop
d,b=bg([(0,'#1a0a2a'),(1,'#a82a4a')])
b+='<circle cx="560" cy="260" r="110" fill="#ff6a3a"/>'+glow(560,260,160,'#ff6a3a',.4)+'<rect y="600" width="800" height="200" fill="#1a0a14"/><path d="M200 600 Q190 420 230 260" stroke="#1a0a14" stroke-width="20" fill="none"/>'
b+=''.join(f'<path d="M230 260 Q{230+dx} {260+dy-50} {230+dx*1.5} {260+dy}" stroke="#1a0a14" stroke-width="18" fill="none"/>' for dx,dy in [(-110,50),(110,40),(-60,90),(80,100)])+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#ffe84a"/>'+glow(x,y,14,'#ffe84a',.6) for x,y in [(380,460),(460,520),(600,480),(320,560),(680,560)])
I[904]=svg(b,d)

# 1541 Love Forever: an old couple's silhouettes walking hand in hand along a sunset beach with footprints, 2020 pop
d,b=bg([(0,'#ff8a6a'),(1,'#ffe0b0')])
b+='<circle cx="400" cy="440" r="90" fill="#fff0b0"/><rect y="480" width="800" height="120" fill="#e8806a"/><rect y="600" width="800" height="200" fill="#f0c890"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="#d8a870"/>' for x,y in [(120,760),(170,740),(220,720),(270,700),(140,780),(190,760)])
b+=figure(360,700,220,'#2a1a1a')+figure(440,700,210,'#2a1a1a',hair='#2a1a1a')
I[1541]=svg(b,d)

# 1698 キスは待つしかないのでしょうか?: a girl waiting under a ticking clock with closed eyes and a heart, idol pop
d,b=bg([(0,'#ffd8ea'),(1,'#e0e8ff')])
b+='<circle cx="400" cy="220" r="110" fill="#fff" stroke="#ff8ab0" stroke-width="10"/><path d="M400 220 L400 140 M400 220 L460 250" stroke="#3a3a4a" stroke-width="8" stroke-linecap="round"/>'+''.join(f'<circle cx="{400+90*math.cos(a)}" cy="{220+90*math.sin(a)}" r="5" fill="#ff8ab0"/>' for a in [k*math.pi/6 for k in range(12)])
b+='<rect y="640" width="800" height="160" fill="#d8b8c8"/>'+profile(400,800,1.0,'#5a2a4a')+heart(520,420,26,'#ff4a8a')
I[1698]=svg(b,d)

# 94 言えないよ: a man holding a ring box behind his back at a window, unable to say it, 1994 ballad
d,b=bg([(0,'#3a4a7a'),(1,'#a8b0d0')])
b+='<rect x="380" y="100" width="340" height="440" fill="#c8d8f0"/>'+rain(30,94,'#fff',.4,8,540)+'<rect x="380" y="100" width="340" height="440" fill="none" stroke="#3a3a4a" stroke-width="14"/><rect y="540" width="800" height="260" fill="#2a2a3a"/>'
b+=figure(260,700,340,'#0a0a14')+'<rect x="290" y="520" width="50" height="40" rx="6" fill="#8a1a2a"/>'+ring(315,516,10,'#e8c86a',4)
I[94]=svg(b,d)

# 169 おんな港町: a lone woman waiting on a misty pier with a red lantern and a docked fishing boat, enka
d,b=bg([(0,'#3a3a5a'),(1,'#7a7a9a')])
b+='<rect y="480" width="800" height="320" fill="#2a3a5a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="220" ry="30" fill="#fff" opacity=".12"/>' for x,y in [(200,460),(600,420),(400,520)])
b+='<path d="M460 500 L720 500 L680 560 L500 560Z" fill="#2a1a14"/><rect x="580" y="360" width="8" height="140" fill="#2a1a14"/><rect x="0" y="560" width="400" height="24" fill="#4a3a30"/>'+figure(260,560,220,'#0a0a10',hair='#0a0a10')+chochin(120,420,40)
I[169]=svg(b,d)

# 477 LONELY BUTTERFLY: a single glowing blue butterfly fluttering through a dark neon city, 80s rock
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=skyline(800,'#0a0a14',477,120,380,'#ff4fa0',80)+'<g transform="translate(400 320) rotate(-10)"><ellipse cx="-50" cy="-30" rx="60" ry="48" fill="#3ab0ff"/><ellipse cx="50" cy="-30" rx="60" ry="48" fill="#3ab0ff"/><ellipse cx="-36" cy="40" rx="40" ry="34" fill="#1a7ad8"/><ellipse cx="36" cy="40" rx="40" ry="34" fill="#1a7ad8"/><rect x="-6" y="-50" width="12" height="110" rx="6" fill="#111"/></g>'+glow(400,320,160,'#3ab0ff',.4)
I[477]=svg(b,d)

# 1699 意志: a sapling pushing up through a crack in concrete toward the light, idol rock
d,b=bg([(0,'#2a2a3a'),(1,'#7a7a8a')])
b+=rays(400,0,10,'#fff4c8',.2,30,60,120)+'<rect y="560" width="800" height="240" fill="#8a8a94"/><path d="M380 560 L400 620 L370 680 L410 740 L390 800" stroke="#3a3a44" stroke-width="8" fill="none"/>'
b+='<path d="M400 600 Q390 480 410 380" stroke="#3a8a3a" stroke-width="10" fill="none"/><path d="M400 500 q-70 -30 -80 10 q50 10 80 -10Z M405 440 q70 -30 80 10 q-50 10 -80 -10Z M410 390 q-40 -50 -10 -80 q30 40 10 80Z" fill="#5ac84a"/>'
I[1699]=svg(b,d)

# 69 あなたならどうする: a woman standing at a fork between two lamplit streets on a rainy night, 1970
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+=rain(70,69,'#cfe6ff',.35)+'<path d="M400 800 L380 560 L120 400 L200 380 L400 520 L600 380 L680 400 L420 560 L400 800Z" fill="#2a2a34"/>'+''.join(f'<rect x="{x}" y="300" width="6" height="100" fill="#3a3a44"/><circle cx="{x+3}" cy="300" r="10" fill="#fff4c8"/>'+glow(x+3,300,50,'#fff4c8',.5) for x in (160,640))
b+=figure(400,700,240,'#000',hair='#000')
I[69]=svg(b,d)

# 274 ラスト・シーン: a theatre curtain closing on a single spotlight with a man's silhouette walking off, 1991 rock
d,b=bg([(0,'#0a0a0a'),(1,'#2a0a0a')])
b+='<path d="M0 0 L320 0 Q280 400 340 800 L0 800Z M800 0 L480 0 Q520 400 460 800 L800 800Z" fill="#8a0a1a"/>'+''.join(f'<path d="M{x} 0 Q{x-20} 400 {x+10} 800" stroke="#5a0010" stroke-width="6" fill="none"/>' for x in (80,180,280,520,620,720))
b+='<ellipse cx="400" cy="700" rx="70" ry="16" fill="#fff4c8" opacity=".5"/>'+figure(420,700,200,'#000')
I[274]=svg(b,d)

# 170 愛の終着駅: the end of a snowy railway line with a buffer stop and a woman's silhouette, 1977 enka
d,b=bg([(0,'#2a3450'),(1,'#7a8aa8')])
b+=snow(80,170)+'<rect y="520" width="800" height="280" fill="#e0e8f4"/><path d="M300 520 L100 800 M500 520 L700 800" stroke="#5a5a64" stroke-width="10"/>'+''.join(f'<rect x="{400-(y-520)*.75-20}" y="{y}" width="{(y-520)*1.5+40}" height="10" fill="#7a6a5a"/>' for y in (560,620,700,790))
b+='<rect x="330" y="470" width="140" height="60" fill="#c8302a"/><rect x="340" y="530" width="20" height="40" fill="#3a3a3a"/><rect x="440" y="530" width="20" height="40" fill="#3a3a3a"/>'+figure(560,560,200,'#0a0a14',hair='#0a0a14')
I[170]=svg(b,d)

# 222 You're Rollin' Thunder: thunder clouds rolling over a prairie with a lightning bolt striking a lone tree, 1977 rock
d,b=bg([(0,'#1a1a2a'),(1,'#4a4a6a')])
b+=cloud(240,180,2.0,'#3a3a4a')+cloud(560,160,1.8,'#4a4a5a')+bolt([(420,220),(380,360),(430,370),(380,540)],'#fff',10)+glow(400,380,140,'#cfe6ff',.4)
b+='<rect y="560" width="800" height="240" fill="#2a3a2a"/>'+tree(380,580,160,'#0a140a',222)
I[222]=svg(b,d)

# 1023 Mr.Moonlight: a dapper big-band singer's silhouette in a tuxedo under a giant crescent moon, 2001 idol swing
d,b=bg([(0,'#1a0a3a'),(1,'#4a2a6a')])
b+=starsf(50,1023,600)+'<path d="M480 120 A170 170 0 1 0 620 420 A136 136 0 1 1 480 120Z" fill="#fff4c8"/>'+'<rect y="660" width="800" height="140" fill="#14081a"/>'
b+=figure(320,680,360,'#000')+'<ellipse cx="320" cy="346" rx="54" ry="10" fill="#000"/><path d="M290 344 Q320 300 350 344Z" fill="#000"/><path d="M300 400 L320 420 L340 400" stroke="#fff" stroke-width="5" fill="none"/>'+''.join(f'<path d="M{x} 680 L{x+20} 520 L{x+50} 500 L{x+40} 540 L{x+30} 680Z" fill="#c8a24a"/>' for x in (520,620))
I[1023]=svg(b,d)

# 1830 宇宙戦艦ヤマト: an old battleship silhouette rising from the sea into a starry space toward a distant red planet
d,b=bg([(0,'#02040e'),(1,'#0a1a3a')])
b+=starsf(100,1830,800)+'<circle cx="150" cy="170" r="60" fill="#c8402a"/>'+glow(150,170,80,'#ff6a3a',.4)
b+='<g transform="rotate(18 400 480)"><path d="M140 480 L660 480 L620 540 L200 540Z" fill="#4a5060"/><rect x="340" y="400" width="80" height="80" fill="#5a6070"/><rect x="370" y="340" width="30" height="60" fill="#5a6070"/><rect x="260" y="450" width="60" height="30" fill="#5a6070"/><rect x="460" y="450" width="60" height="30" fill="#5a6070"/><path d="M140 480 L120 470 L140 500Z" fill="#c8302a"/></g>'
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.4}" fill="#fff" opacity=".3"/>' for x,y,r in [(200,640,60),(300,680,40),(160,700,50)])
I[1830]=svg(b,d)

# 63 悲しくてやりきれない: a lone figure sitting on a riverbank at dusk tossing stones into the water, 1968 folk
d,b=bg([(0,'#5a5a7a'),(1,'#c8a8a8')])
b+='<rect y="460" width="800" height="200" fill="#5a6a8a"/>'+''.join(ring(500,540,r,'#fff',3,.5) for r in (20,44,70))+'<path d="M0 620 Q300 560 800 640 L800 800 L0 800Z" fill="#4a5a3a"/>'
b+=figure(260,620,160,'#1a1a24')+'<path d="M300 520 Q400 440 500 530" stroke="#fff" stroke-width="2" stroke-dasharray="6 8" fill="none"/>'
I[63]=svg(b,d)

# 173 祝い酒: a festive sake cask with a red-and-white ribbon and a cup of sake under celebratory lanterns, enka
d,b=bg([(0,'#ff6a3a'),(1,'#ffd08a')])
b+=''.join(chochin(x,140,40) for x in (140,400,660))+'<ellipse cx="400" cy="400" rx="170" ry="40" fill="#e8dcc0"/><rect x="230" y="400" width="340" height="260" fill="#e8dcc0"/><ellipse cx="400" cy="660" rx="170" ry="40" fill="#c8b890"/>'
b+='<rect x="230" y="460" width="340" height="20" fill="#3a3a3a"/><rect x="230" y="600" width="340" height="20" fill="#3a3a3a"/><rect x="330" y="500" width="140" height="90" fill="#c8102a"/><path d="M600 640 L680 640 L670 690 L610 690Z" fill="#e8302a"/>'
I[173]=svg(b,d)

# 266 安奈: a candle in a rain-streaked window for someone far away, a guitar case by the door, rock ballad
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+='<rect x="200" y="120" width="400" height="420" fill="#2a3a5a"/>'+rain(40,266,'#cfe6ff',.5,8,540)+'<rect x="200" y="120" width="400" height="420" fill="none" stroke="#3a2a24" stroke-width="18"/><rect x="390" y="120" width="20" height="420" fill="#3a2a24"/><rect y="540" width="800" height="260" fill="#2a2020"/>'
b+='<rect x="370" y="470" width="30" height="70" fill="#f4ece0"/><path d="M385 440 q12 16 0 30 q-12 -14 0 -30Z" fill="#ffd02a"/>'+glow(385,480,100,'#ffd27a',.5)+'<rect x="660" y="520" width="50" height="160" rx="20" fill="#1a1a1a" transform="rotate(-8 685 600)"/>'
I[266]=svg(b,d)

# 322 アトムの子: a boy's silhouette holding up a toy rocket toward a sky with a glowing atom orbit symbol, 1991
d,b=bg([(0,'#3a8ae8'),(1,'#e0f4ff')])
b+=''.join(f'<ellipse cx="560" cy="220" rx="120" ry="40" fill="none" stroke="#fff" stroke-width="6" transform="rotate({a} 560 220)"/>' for a in (0,60,120))+'<circle cx="560" cy="220" r="20" fill="#ffd02a"/>'
b+='<rect y="640" width="800" height="160" fill="#8ac86a"/>'+figure(300,660,260,'#1a2a4a',pose='up')+'<path d="M330 300 Q345 270 360 300 L360 360 L330 360Z" fill="#e8302a"/><path d="M330 360 L320 380 L330 370Z M360 360 L370 380 L360 370Z" fill="#e8302a"/>'
I[322]=svg(b,d)

# 508 路上のルール: a youth's silhouette at a graffiti-covered underpass with a stop sign light, 1985 rock
d,b=bg([(0,'#1a1a1a'),(1,'#2a2a2a')])
b+='<path d="M0 200 Q400 60 800 200 L800 800 L0 800Z" fill="#3a3a3a"/><path d="M120 800 Q120 300 400 300 Q680 300 680 800Z" fill="#141414"/>'
b+=''.join(f'<path d="M{x} {y} q30 -40 60 0 t60 0" stroke="{c}" stroke-width="10" fill="none" stroke-linecap="round"/>' for x,y,c in [(40,500,'#ff4a8a'),(640,460,'#3ab0ff'),(30,650,'#ffd02a'),(660,620,'#5ad87a')])
b+=figure(400,780,280,'#000')+'<circle cx="400" cy="380" r="34" fill="#e8302a"/>'+glow(400,380,100,'#e8302a',.4)
I[508]=svg(b,d)

# 1683 赤い果実: a single shiny red fruit hanging from a dark branch under a spotlight, sultry 2017 pop
d,b=bg([(0,'#1a0a0a'),(1,'#3a0a14')])
b+='<path d="M0 160 Q300 180 420 260" stroke="#2a1a14" stroke-width="16" fill="none"/><path d="M420 260 L420 320" stroke="#2a1a14" stroke-width="6"/><path d="M420 280 q40 -30 80 -10 q-40 30 -80 10Z" fill="#2a5a2a"/>'
b+='<circle cx="420" cy="400" r="90" fill="#e8102a"/><ellipse cx="390" cy="370" rx="20" ry="30" fill="#fff" opacity=".35"/>'+glow(420,400,180,'#ff3a3a',.4)
I[1683]=svg(b,d)

# 1684 君、僕。: two silhouettes sitting back to back on a grassy hill under a starry sky, 2018
d,b=bg([(0,'#0a1a3a'),(1,'#3a3a6a')])
b+=starsf(90,1684,560)+'<path d="M0 600 Q400 480 800 600 L800 800 L0 800Z" fill="#14202a"/>'+figure(370,540,170,'#000')+figure(430,540,160,'#000',hair='#000')+'<path d="M400 360 L400 420" stroke="#fff4c8" stroke-width="2" opacity=".6"/>'
I[1684]=svg(b,d)

# 1827 セタップ! 仮面ライダーX: a motorcycle rider's silhouette with a long scarf jumping against a sea cliff sunrise, 70s tokusatsu
d,b=bg([(0,'#e8402a'),(1,'#ffd08a')])
b+='<circle cx="560" cy="440" r="100" fill="#fff0b0"/><rect y="500" width="800" height="300" fill="#2a4a8a"/><path d="M0 560 L320 460 L320 800 L0 800Z" fill="#2a1a14"/>'
b+='<g transform="rotate(-20 420 400)">'+ring(340,440,40,'#1a1a1a',10)+ring(500,440,40,'#1a1a1a',10)+'<path d="M340 440 L410 380 L500 440 M410 380 L470 370 L480 350" stroke="#1a1a1a" stroke-width="12" fill="none"/>'+figure(420,400,140,'#1a1a1a')+'<path d="M410 290 Q320 270 260 300 Q320 300 360 320" fill="#e8102a"/></g>'
I[1827]=svg(b,d)

# 1877 赤黄色の金木犀: clusters of tiny orange osmanthus flowers on a branch in an autumn evening, 2004 rock
d,b=bg([(0,'#5a4a8a'),(1,'#ffb07a')])
b+='<path d="M0 200 Q300 260 500 400 Q600 470 800 480" stroke="#3a2a1a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M{x} {y} q30 -20 50 -40 q-20 40 -50 40Z" fill="#2a5a2a"/>' for x,y in [(160,240),(340,320),(520,420),(680,470)])
b+=''.join(''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="6" fill="{c}"/>' for dx,dy in [(-10,0),(10,0),(0,-10),(0,10),(0,0),(-14,-14),(14,14)]) for x,y,c in [(200,260,'#ff9a2a'),(260,290,'#ffb02a'),(380,350,'#ff8a1a'),(450,380,'#ffb02a'),(560,430,'#ff9a2a'),(620,460,'#ff8a1a')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#ffb02a" opacity=".7"/>' for x,y in [(240,500),(400,560),(520,620),(320,680)])
I[1877]=svg(b,d)

# 1888 群青: a deep ultramarine sea with a lone boat beneath a vast star-filled sky, 1981 ballad
d,b=bg([(0,'#050a30'),(1,'#1a2a8a')])
b+=starsf(100,1888,460)+'<rect y="460" width="800" height="340" fill="#0a1a6a"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#5a7ae8" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(100,520),(500,560),(260,660),(600,700)])
b+='<path d="M340 500 L460 500 L440 530 L360 530Z" fill="#0a0a14"/><rect x="398" y="420" width="4" height="80" fill="#0a0a14"/><path d="M402 420 L450 490 L402 490Z" fill="#c8d0e8"/>'
I[1888]=svg(b,d)

# 44 沓掛時次郎: a wandering swordsman's silhouette in a wide straw sandogasa hat and cape on a mountain road, 1961
d,b=bg([(0,'#e8a06a'),(1,'#f4e0c0')])
b+=hills(460,50,'#a8806a',44,4)+'<rect y="500" width="800" height="300" fill="#c8a880"/><path d="M380 500 L200 800 L600 800 L420 500Z" fill="#e0c8a0"/>'
b+=figure(400,720,300,'#2a1a14')+'<ellipse cx="400" cy="430" rx="100" ry="22" fill="#d8b870"/><path d="M330 430 L400 380 L470 430Z" fill="#d8b870"/><path d="M340 470 L460 470 L500 640 L300 640Z" fill="#3a2a1a"/><rect x="460" y="520" width="8" height="160" fill="#1a1a1a" transform="rotate(30 464 600)"/>'
I[44]=svg(b,d)

# 117 銀河系まで飛んで行け!: three girls' silhouettes riding a shooting star into the galaxy, 1977 idol trio
d,b=bg([(0,'#0a0a3a'),(1,'#4a2a7a')])
b+=starsf(100,117,800)+''.join(f'<ellipse cx="560" cy="200" rx="{r}" ry="{r*.35}" fill="none" stroke="#c8a8ff" stroke-width="3" opacity=".5" transform="rotate(-20 560 200)"/>' for r in (60,110,160))
b+='<path d="M80 700 Q300 560 480 420" stroke="#fff4c8" stroke-width="20" fill="none" opacity=".6" stroke-linecap="round"/>'+star5(500,400,46,'#fff4c8')+glow(500,400,80,'#fff4c8',.6)+''.join(figure(x,y,90,'#ffd0e8',hair='#ffd0e8') for x,y in [(380,500),(320,550),(260,600)])
I[117]=svg(b,d)

# 478 76th Star: Halley's-comet-like star streaking across the sky above a girl on a hill, 80s rock
d,b=bg([(0,'#050a24'),(1,'#2a2a5a')])
b+=starsf(90,478,600)+'<path d="M140 140 L520 320" stroke="#cfe6ff" stroke-width="30" opacity=".3" stroke-linecap="round"/><path d="M200 170 L520 320" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'+glow(520,320,60,'#fff',.8)
b+='<path d="M0 640 Q400 540 800 640 L800 800 L0 800Z" fill="#0a0a14"/>'+figure(560,600,180,'#000',pose='up',hair='#000')
I[478]=svg(b,d)

# 28 夜霧の第二国道: a car's headlights cutting through thick night fog on an empty highway, 1957
d,b=bg([(0,'#3a3a4a'),(1,'#8a8a9a')])
b+='<path d="M380 360 L120 800 L680 800 L420 360Z" fill="#4a4a54"/><path d="M400 380 L400 800" stroke="#e8e8e8" stroke-width="5" stroke-dasharray="30 30"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="320" ry="40" fill="#e8e8f0" opacity=".2"/>' for x,y in [(300,400),(500,480),(400,560),(300,640)])
b+='<circle cx="350" cy="560" r="16" fill="#fff4c8"/><circle cx="450" cy="560" r="16" fill="#fff4c8"/>'+glow(400,560,160,'#fff4c8',.5)+''.join(f'<rect x="{x}" y="380" width="6" height="140" fill="#3a3a44"/>' for x in (200,600))
I[28]=svg(b,d)

# 103 しあわせ芝居: a small stage with curtains where a puppet couple performs a happy scene, a lone audience member
d,b=bg([(0,'#2a1a1a'),(1,'#4a2a2a')])
b+='<rect x="160" y="160" width="480" height="340" fill="#f4e0c0"/>'+glow(400,330,200,'#fff4c8',.3)+'<path d="M140 140 L340 140 Q300 300 260 500 L140 500Z M660 140 L460 140 Q500 300 540 500 L660 500Z" fill="#a81a2a"/>'
b+=figure(360,480,140,'#5a3a4a',hair='#5a3a4a')+figure(440,480,150,'#3a3a5a')+heart(400,250,24,'#ff4a8a')+'<rect y="500" width="800" height="300" fill="#1a1010"/>'+profile(400,800,.9,'#000')
I[103]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
