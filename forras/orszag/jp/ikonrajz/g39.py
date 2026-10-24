import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 39. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1897 水の星へ愛をこめて: a blue water planet seen from space cradled by a glowing heart of light, anime ballad
d,b=bg([(0,'#02040e'),(1,'#0a1430')])
b+=starsf(100,1897,800)+'<circle cx="400" cy="440" r="200" fill="#1a6ad8"/><path d="M300 360 Q360 330 380 390 Q330 450 290 420Z M440 480 Q520 440 540 520 Q480 570 440 540Z" fill="#3aa86a"/>'+'<path d="M200 440 A200 200 0 0 0 600 440" fill="#0a2a6a" opacity=".4"/>'
b+=heart(400,440,280,'none',' stroke="#8ad0ff" stroke-width="5" opacity=".7"')+glow(400,440,240,'#8ad0ff',.3)
I[1897]=svg(b,d)

# 38 まつり: a big festival taiko drum with crossed sticks under strings of red lanterns, enka festival
d,b=bg([(0,'#1a0a14'),(1,'#5a1a1a')])
b+='<path d="M0 140 Q400 220 800 140" stroke="#3a2a2a" stroke-width="4" fill="none"/>'+''.join(chochin(x,175+abs(400-x)*-.1+40-(x-400)**2/4000,34) for x in (80,220,360,500,640,760))
b+='<rect x="220" y="400" width="360" height="280" rx="40" fill="#8a3a1a"/><ellipse cx="400" cy="400" rx="180" ry="50" fill="#f4e8d0"/><ellipse cx="400" cy="680" rx="180" ry="40" fill="#6a2a14"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#1a1a1a"/>' for x in range(240,580,30) for y in (430,650))
b+='<path d="M300 260 L440 400 M500 260 L360 400" stroke="#f4e8d0" stroke-width="16" stroke-linecap="round"/>'
I[38]=svg(b,d)

# 64 帰って来たヨッパライ: a tipsy cartoon ghost with a sake flask floating down from heavenly clouds, 60s novelty folk
d,b=bg([(0,'#9ad0ff'),(1,'#fff0d8')])
b+=cloud(200,200,1.6)+cloud(600,160,1.3)+rays(400,0,10,'#fff',.25,20,40,140)
b+='<path d="M330 320 Q400 230 470 320 L470 480 L450 460 L430 490 L410 460 L390 490 L370 460 L350 490 L330 470Z" fill="#fff" stroke="#c8d0e0" stroke-width="3"/><circle cx="380" cy="350" r="8" fill="#3a3a4a"/><circle cx="420" cy="350" r="8" fill="#3a3a4a"/><ellipse cx="370" cy="372" rx="12" ry="7" fill="#ff8a9a"/><ellipse cx="430" cy="372" rx="12" ry="7" fill="#ff8a9a"/>'
b+='<path d="M490 400 L490 360 Q490 340 510 340 Q530 340 530 360 L530 400 Q550 420 540 470 L480 470 Q470 420 490 400Z" fill="#f4f0e4" stroke="#8a6a4a" stroke-width="3"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" opacity=".8"/>' for x,y in [(560,320),(580,290),(570,260)])
I[64]=svg(b,d)

# 963 Web of Night: a glowing spiderweb stretched across a neon city night, a lone figure suspended, 2004 rock
d,b=bg([(0,'#050a1a'),(1,'#1a0a3a')])
b+=skyline(800,'#0a0a1a',963,100,320,'#8a4aff',80)
b+=''.join(f'<path d="M400 360 L{400+420*math.cos(a)} {360+420*math.sin(a)}" stroke="#c8b8ff" stroke-width="2" opacity=".7"/>' for a in [k*math.pi/6 for k in range(12)])+''.join(f'<polygon points="'+' '.join(f'{400+r*math.cos(k*math.pi/6):.0f},{360+r*math.sin(k*math.pi/6):.0f}' for k in range(12))+'" fill="none" stroke="#c8b8ff" stroke-width="2" opacity=".6"/>' for r in (60,120,190,270))
b+=glow(400,360,100,'#8a4aff',.5)+figure(400,470,150,'#000')
I[963]=svg(b,d)

# 1264 紅く燃ゆる太陽: a blazing crimson sun scorching over a rocky ridge with silhouettes raising their fists
d,b=bg([(0,'#3a0a0a'),(1,'#e8402a')])
b+='<circle cx="400" cy="320" r="170" fill="#ff2a1a"/>'+glow(400,320,240,'#ff6a2a',.5)+rays(400,320,20,'#ffd02a',.15,10)+'<path d="M0 620 L160 520 L300 580 L420 500 L560 560 L700 500 L800 540 L800 800 L0 800Z" fill="#1a0a0a"/>'
b+=''.join(figure(x,560-(x%3)*10,150,'#1a0a0a',pose='up') for x in (200,320,440,560))
I[1264]=svg(b,d)

# 1716 COUNTDOWN: a large digital countdown display flickering in a dark room, a red ignition glow
d,b=bg([(0,'#0a0a0a'),(1,'#1a0a0a')])
b+='<rect x="120" y="260" width="560" height="240" rx="20" fill="#1a1a1a" stroke="#3a3a3a" stroke-width="8"/>'
seg={'0':'abcdef','3':'abcdg','2':'abdeg','1':'bc'}
def dig(x,y,c):
  o='';P={'a':(x,y,80,14),'b':(x+70,y,14,80),'c':(x+70,y+80,14,80),'d':(x,y+150,80,14),'e':(x,y+80,14,80),'f':(x,y,14,80),'g':(x,y+75,80,14)}
  for s_ in seg[c]: X,Y,W,H=P[s_];o+=f'<rect x="{X}" y="{Y}" width="{W}" height="{H}" rx="4" fill="#ff2a2a"/>'
  return o
b+=dig(180,300,'0')+dig(290,300,'0')+'<circle cx="400" cy="350" r="9" fill="#ff2a2a"/><circle cx="400" cy="420" r="9" fill="#ff2a2a"/>'+dig(430,300,'0')+dig(540,300,'3')+glow(400,380,240,'#ff2a2a',.3)
I[1716]=svg(b,d)

# 408 天国にいちばん近い島: a tiny palm-tree island in a turquoise lagoon under a heavenly starry dusk
d,b=bg([(0,'#3a3a8a'),(1,'#ff9ac0')])
b+=starsf(50,408,360)+'<rect y="460" width="800" height="340" fill="#2ac8c8"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(120,560),(560,600),(260,700),(600,720)])
b+='<ellipse cx="400" cy="480" rx="160" ry="30" fill="#f4e0a8"/><path d="M400 480 Q390 380 420 300" stroke="#5a3a2a" stroke-width="12" fill="none"/>'+''.join(f'<path d="M420 300 Q{420+dx} {300+dy-40} {420+dx*1.4} {300+dy}" stroke="#2a6a3a" stroke-width="14" fill="none"/>' for dx,dy in [(-90,40),(90,30),(-50,70),(70,80)])
b+=star5(560,160,26,'#fff4c8')+glow(560,160,40,'#fff4c8',.5)
I[408]=svg(b,d)

# 万里の河: a vast winding river through a continental landscape at dusk, a lone traveller on the bank
d,b=bg([(0,'#c84a2a'),(1,'#ffc08a')])
b+='<circle cx="400" cy="300" r="70" fill="#fff0c0"/>'+hills(360,60,'#7a4a4a',615,4)+'<rect y="380" width="800" height="420" fill="#8a6a4a"/>'
b+='<path d="M380 380 Q300 450 420 520 Q560 600 300 680 Q140 740 160 800 L460 800 Q420 740 560 680 Q760 600 520 520 Q400 460 420 380Z" fill="#e8b070"/>'+figure(620,700,140,'#2a1a14')
I[615]=svg(b,d)

# 791 Hey!: a man's silhouette turning with a hand raised in greeting on a sunny seaside street
d,b=bg([(0,'#3ab0ff'),(1,'#e0f8ff')])
b+='<circle cx="640" cy="140" r="60" fill="#fff4a0"/><rect y="480" width="800" height="100" fill="#1a8ad8"/><rect y="580" width="800" height="220" fill="#d8d0c0"/>'
b+=figure(360,760,360,'#1a1a2a')+'<path d="M400 470 L470 370" stroke="#1a1a2a" stroke-width="22" stroke-linecap="round"/><circle cx="476" cy="356" r="18" fill="#1a1a2a"/>'
I[791]=svg(b,d)

# 1265 トップガン: a fighter jet silhouette streaking up into the sun with vapour trails, 2019 boy group
d,b=bg([(0,'#1a3a8a'),(1,'#ffb07a')])
b+='<circle cx="560" cy="220" r="90" fill="#fff4c8"/>'+''.join(f'<path d="M{x} 800 Q{x+100} 500 {x+200} 400" stroke="#fff" stroke-width="10" fill="none" opacity=".7"/>' for x in (180,230))
b+='<g transform="rotate(-50 440 380)"><path d="M440 280 L460 340 L540 380 L540 400 L460 390 L455 450 L480 470 L480 480 L440 475 L400 480 L400 470 L425 450 L420 390 L340 400 L340 380 L420 340Z" fill="#1a1a2a"/></g>'
I[1265]=svg(b,d)

# 1635 GOAT: a mountain goat silhouette wearing a gold crown on a peak at sunrise, 2023 hip-hop boy group
d,b=bg([(0,'#1a1a3a'),(1,'#e8902a')])
b+='<circle cx="400" cy="520" r="160" fill="#ffd02a" opacity=".8"/><path d="M100 800 L400 480 L700 800Z" fill="#1a1414"/>'
b+='<path d="M330 480 L340 420 Q360 380 420 380 L460 380 L480 340 Q490 320 510 330 L520 360 L520 380 Q530 400 510 410 L480 410 L470 440 L470 480 L455 480 L450 440 L370 440 L360 480Z" fill="#1a1414"/><path d="M490 330 Q470 280 440 290 M500 330 Q500 280 470 270" stroke="#1a1414" stroke-width="8" fill="none"/>'
b+='<path d="M460 290 L470 250 L490 275 L505 245 L515 280 L535 255 L530 300Z" fill="#ffd02a" transform="rotate(10 495 280)"/>'
I[1635]=svg(b,d)

# 1645 You Know What To Do: a hand on a glowing door handle, light pouring through the gap, 2026 boy group
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+='<rect x="200" y="100" width="400" height="640" fill="#2a2a34"/><path d="M560 100 L600 100 L600 740 L560 740Z" fill="#fff4c8"/>'+'<path d="M600 100 L800 0 L800 800 L600 740Z" fill="#fff4c8" opacity=".25"/>'+glow(580,420,200,'#fff4c8',.4)
b+='<rect x="500" y="400" width="50" height="16" rx="8" fill="#c8a24a"/><path d="M800 520 Q640 470 540 420 L520 440 Q620 500 800 600Z" fill="#14141a"/>'
I[1645]=svg(b,d)

# 1879 今夜はブギーバック: a boombox on a night-time rooftop with a mirror ball moon, 90s-style hip-hop
d,b=bg([(0,'#1a0a3a'),(1,'#5a2a6a')])
b+=starsf(40,1879,400)+'<circle cx="600" cy="180" r="70" fill="#d8d8e8"/>'+''.join(f'<rect x="{x}" y="{y}" width="16" height="16" fill="#fff" opacity=".7"/>' for x,y in [(570,150),(600,170),(620,140),(580,200),(610,210)])+skyline(560,'#0a0a1a',1879,40,160,'#ffd27a',40)
b+='<rect y="560" width="800" height="240" fill="#1a1424"/><rect x="200" y="420" width="400" height="200" rx="20" fill="#2a2a34"/><circle cx="290" cy="530" r="60" fill="#111" stroke="#c8c8d8" stroke-width="6"/><circle cx="510" cy="530" r="60" fill="#111" stroke="#c8c8d8" stroke-width="6"/><rect x="360" y="450" width="80" height="30" fill="#3affe8" opacity=".7"/><path d="M260 420 Q400 360 540 420" stroke="#8a8a9a" stroke-width="10" fill="none"/>'
I[1879]=svg(b,d)

# 71 襟裳岬: a lighthouse on a windswept northern cape in winter with waves crashing, 1974 folk-enka
d,b=bg([(0,'#3a4a6a'),(1,'#9aaac0')])
b+=snow(30,71,.6)+'<rect y="520" width="800" height="280" fill="#2a3a5a"/><path d="M300 520 L800 360 L800 800 L240 800Z" fill="#4a4a3a"/>'+''.join(f'<path d="M{x} {y} q30 -30 60 0" stroke="#fff" stroke-width="6" fill="none" opacity=".7"/>' for x,y in [(160,560),(80,640),(220,700)])
b+='<path d="M580 420 L600 180 L640 180 L660 420Z" fill="#f4f4f4"/><rect x="590" y="260" width="60" height="30" fill="#c8302a"/><rect x="585" y="150" width="70" height="30" fill="#3a3a3a"/><path d="M620 165 L300 80 L300 240Z" fill="#fff4c8" opacity=".3"/>'
I[71]=svg(b,d)

# 195 いっそ セレナーデ: a man's silhouette under a balcony window glowing at night, a serenade, 1984
d,b=bg([(0,'#0a0a24'),(1,'#2a2a4a')])
b+=moon(160,140,50)+'<rect x="440" y="0" width="360" height="800" fill="#2a2430"/><rect x="520" y="160" width="160" height="200" fill="#ffd27a"/>'+glow(600,260,140,'#ffd27a',.4)+'<rect x="490" y="360" width="220" height="16" fill="#1a1420"/>'+''.join(f'<rect x="{x}" y="376" width="6" height="60" fill="#1a1420"/>' for x in range(500,710,20))
b+='<rect y="680" width="800" height="120" fill="#14141e"/>'+figure(280,700,260,'#000')+''.join(note(x,y,s,'#ffd27a') for x,y,s in [(340,380,30),(400,300,26)])
I[195]=svg(b,d)

# 333 もう一度: two coffee cups on a café table, one with a lipstick mark, rain on the window
d,b=bg([(0,'#5a6a8a'),(1,'#a8b0c0')])
b+=rain(50,333,'#e8f0ff',.4,8,440)+'<rect x="0" y="440" width="800" height="360" fill="#6a4a3a"/>'
b+='<ellipse cx="300" cy="560" rx="80" ry="20" fill="#f4f0e8"/><path d="M250 470 L350 470 L340 550 L260 550Z" fill="#f4f0e8"/><ellipse cx="300" cy="470" rx="50" ry="12" fill="#5a3a2a"/>'
b+='<ellipse cx="520" cy="580" rx="80" ry="20" fill="#f4f0e8"/><path d="M470 490 L570 490 L560 570 L480 570Z" fill="#f4f0e8"/><ellipse cx="520" cy="490" rx="50" ry="12" fill="#5a3a2a"/><path d="M490 486 q10 8 20 0" stroke="#c8102a" stroke-width="6" fill="none"/>'
I[333]=svg(b,d)

# 405 探偵物語: a detective's magnifying glass over a footprint trail on a rainy night street, 1983 film song
d,b=bg([(0,'#1a1a24'),(1,'#3a3a4a')])
b+=rain(60,405,'#cfe6ff',.3)+'<rect y="460" width="800" height="340" fill="#2a2a34"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="16" fill="#4a4a5a"/>' for x,y in [(160,760),(220,700),(260,640),(320,590),(360,540),(420,500)])
b+='<circle cx="480" cy="300" r="110" fill="#8ab0d8" opacity=".3" stroke="#c8a24a" stroke-width="18"/><rect x="560" y="380" width="30" height="180" rx="12" fill="#5a3a2a" transform="rotate(-40 575 390)"/>'+figure(620,760,260,'#000')+'<ellipse cx="620" cy="512" rx="50" ry="10" fill="#000"/><path d="M590 510 Q620 480 650 510Z" fill="#000"/>'
I[405]=svg(b,d)

# 444 真夜中すぎの恋: a neon-lit clock tower past midnight and two silhouettes in a doorway, 80s rock ballad
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+=starsf(40,444,400)+'<rect x="80" y="160" width="160" height="640" fill="#1a1a2a"/><circle cx="160" cy="260" r="56" fill="#f4f0e8"/><path d="M160 260 L160 214 M160 260 L172 220" stroke="#1a1a1a" stroke-width="6"/>'
b+='<rect x="400" y="300" width="260" height="500" fill="#2a1a2a"/><rect x="460" y="460" width="140" height="240" fill="#ff7aa8" opacity=".6"/>'+glow(530,580,140,'#ff7aa8',.4)+profile(500,700,.6,'#000')+profile(560,700,.6,'#000',True)+'<rect y="700" width="800" height="100" fill="#0a0a14"/>'
I[444]=svg(b,d)

# 540 言葉にできない (2001): a vast sky full of light with a single white dove gliding, wordless gratitude
d,b=bg([(0,'#5a9ae8'),(1,'#fff4e0')])
b+=rays(400,600,24,'#fff',.25,10)+'<circle cx="400" cy="600" r="140" fill="#fff8e0"/>'+cloud(150,300,1.2)+cloud(650,260,1.0)
b+='<path d="M400 360 Q330 300 260 320 Q330 340 380 380 Q340 400 320 440 Q380 420 410 390 L470 380 L500 360 L470 350Z" fill="#fff" stroke="#c8d0e0" stroke-width="2"/>'
I[540]=svg(b,d)

# 1759 あじさい橋: a small arched bridge over a stream lined with blue hydrangeas in June rain, enka
d,b=bg([(0,'#8a9ab8'),(1,'#c8d4e4')])
b+=rain(60,1759,'#fff',.35)+'<rect y="520" width="800" height="280" fill="#5a7a9a"/><path d="M180 520 Q400 380 620 520 L620 540 Q400 410 180 540Z" fill="#c8302a"/>'+''.join(f'<rect x="{x}" y="{440+abs(400-x)*.3}" width="6" height="40" fill="#c8302a"/>' for x in range(220,600,40))
b+=''.join(''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="18" fill="{c}"/>' for dx,dy in [(-20,0),(20,0),(0,-18),(0,18),(0,0)]) for x,y,c in [(100,560,'#6a7ae8'),(180,620,'#9a6ae8'),(620,600,'#5a8ae8'),(710,560,'#8a7ae8'),(100,700,'#7a8ae8'),(700,690,'#9a7ae8')])
I[1759]=svg(b,d)

# 220 遠くで汽笛を聞きながら: a lone figure on a hillside listening to a distant steam train's whistle at dusk
d,b=bg([(0,'#5a4a7a'),(1,'#ffb08a')])
b+=hills(520,40,'#6a5a7a',220,4)+'<rect x="420" y="490" width="120" height="30" fill="#1a1424"/><rect x="520" y="470" width="20" height="20" fill="#1a1424"/><circle cx="440" cy="525" r="10" fill="#1a1424"/><circle cx="510" cy="525" r="10" fill="#1a1424"/>'+''.join(f'<circle cx="{530+k*30}" cy="{450-k*26}" r="{12+k*6}" fill="#fff" opacity="{.6-k*.1}"/>' for k in range(4))
b+='<path d="M0 640 Q300 580 520 640 L520 800 L0 800Z" fill="#2a2030"/>'+figure(220,620,200,'#0a0a14')
I[220]=svg(b,d)

# 451 My Truth: a rock trio's silhouettes on stage under a single shaft of white light, 80s rock
d,b=bg([(0,'#0a0a14'),(1,'#2a1a2a')])
b+='<path d="M360 0 L440 0 L640 680 L160 680Z" fill="#fff" opacity=".15"/><rect y="680" width="800" height="120" fill="#14101a"/>'
b+=figure(260,700,280,'#000',hair='#000')+guitar(280,560,.6,30,'#000')+figure(400,700,300,'#000',hair='#000')+'<rect x="396" y="440" width="6" height="260" fill="#333"/>'+figure(540,700,280,'#000',hair='#000')+guitar(520,560,.6,-30,'#000')
I[451]=svg(b,d)

# 616 モーニングムーン: a pale white moon still hanging in a bright morning sky over city rooftops
d,b=bg([(0,'#8ac8ff'),(1,'#ffe8d0')])
b+='<circle cx="560" cy="200" r="80" fill="#fff" opacity=".85"/><circle cx="540" cy="190" r="12" fill="#e0e8f0"/><circle cx="580" cy="220" r="8" fill="#e0e8f0"/>'+rays(0,800,16,'#fff',.2,10,-90,0)+skyline(800,'#5a6a8a',616,80,300,'#ffe8a0',40)
I[616]=svg(b,d)

# 688 雨にキッスの花束を: a bouquet of flowers held out in the rain under a clear umbrella, 1990 pop
d,b=bg([(0,'#7a8ab8'),(1,'#c8d0e8')])
b+=rain(80,688,'#fff',.4)+'<path d="M200 380 Q400 160 600 380Z" fill="#fff" opacity=".35" stroke="#fff" stroke-width="4"/><path d="M400 280 L400 620" stroke="#ddd" stroke-width="6"/>'
b+='<path d="M360 560 L440 560 L410 700 L390 700Z" fill="#f4e0c8"/>'+''.join(flower(x,y,26,6,c,'#ffd02a') for x,y,c in [(370,520,'#ff6a8a'),(430,520,'#ff9ac0'),(400,490,'#fff'),(350,480,'#ffb0c8'),(450,480,'#e8508a')])
I[688]=svg(b,d)

# 1728 雨のバラード: rain streaming down a café window with blurred city lights behind, 1971 ballad
d,b=bg([(0,'#1a2030'),(1,'#3a4050')])
b+=''.join(f'<circle cx="{random.Random(1728*k).randint(0,800)}" cy="{random.Random(1728*k+1).randint(200,700)}" r="{random.Random(1728*k+2).randint(14,40)}" fill="{["#ffd27a","#ff6a6a","#8ad0ff"][k%3]}" opacity=".35"/>' for k in range(30))
b+=''.join(f'<path d="M{x} {y} Q{x+4} {y+60} {x} {y+120}" stroke="#cfe6ff" stroke-width="4" fill="none" opacity=".6"/>' for x,y in [(random.Random(17280+k).randint(0,800),random.Random(17290+k).randint(0,600)) for k in range(30)])
b+='<rect x="0" y="0" width="800" height="800" fill="none" stroke="#2a1a14" stroke-width="40"/><rect x="390" y="0" width="20" height="800" fill="#2a1a14"/>'
I[1728]=svg(b,d)

# 1750 風を待つ: a girl on a breakwater holding a pinwheel waiting for the wind, Setouchi idol ballad
d,b=bg([(0,'#7ab8e8'),(1,'#e8f4ff')])
b+='<rect y="480" width="800" height="320" fill="#3a8ad8"/>'+hills(480,30,'#5a8aa8',1750,3,.8)+'<rect x="0" y="600" width="520" height="200" fill="#a8a8b0"/>'
b+=figure(300,600,240,'#1a1a2a',hair='#1a1a2a')+'<path d="M340 470 L380 380" stroke="#1a1a2a" stroke-width="5"/>'+''.join(f'<path d="M380 380 L{380+50*math.cos(a)} {380+50*math.sin(a)} L{380+50*math.cos(a+.8)} {380+50*math.sin(a+.8)}Z" fill="{c}"/>' for a,c in [(0,'#ff5a7a'),(math.pi/2,'#ffd02a'),(math.pi,'#3ab0ff'),(3*math.pi/2,'#5ad87a')])
I[1750]=svg(b,d)

# 1822 初恋: a schoolboy's silhouette watching a girl through a classroom window in the warm afternoon, 1983 folk
d,b=bg([(0,'#f8d8a8'),(1,'#f4ecd8')])
b+='<rect x="80" y="120" width="640" height="400" fill="#ffe8b8"/>'+''.join(f'<rect x="{x}" y="120" width="12" height="400" fill="#8a6a4a"/>' for x in (80,290,500,710))+'<rect x="80" y="310" width="640" height="10" fill="#8a6a4a"/>'
b+=figure(560,520,180,'#5a4a5a',hair='#5a4a5a')+'<rect y="520" width="800" height="280" fill="#c8a07a"/>'+figure(200,780,300,'#2a1a1a')
I[1822]=svg(b,d)

# 474 MOON: a woman on a rooftop in a silver moonlight beam, reaching toward a giant moon, 80s rock
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=starsf(60,474,600)+moon(500,280,180)+'<rect y="640" width="800" height="160" fill="#0a0a14"/>'+skyline(640,'#0a0a1a',474,30,100)
b+=figure(320,660,240,'#000',pose='up',hair='#000')
I[474]=svg(b,d)

# 808 LOVE IS ALL MUSIC: a heart-shaped speaker pulsing with rainbow sound waves, 90s dance pop
d,b=bg([(0,'#2a0a4a'),(1,'#ff6aa0')])
b+=''.join(f'<path d="M{400-r} 420 Q400 {420-r} {400+r} 420" stroke="{c}" stroke-width="8" fill="none" opacity=".7"/>' for r,c in [(220,'#ff4a4a'),(260,'#ffd02a'),(300,'#5ad87a'),(340,'#3ab0ff')])
b+=heart(400,440,130,'#1a1a2a')+'<circle cx="400" cy="430" r="60" fill="#3a3a4a"/><circle cx="400" cy="430" r="24" fill="#ff4a8a"/>'
I[808]=svg(b,d)

# 1738 ワロタピーポー: a crowd of silhouettes laughing with big comic speech-bubble sparkles, Osaka idol
d,b=bg([(0,'#ffd04a'),(1,'#ff8a3a')])
b+=rays(400,300,20,'#fff',.2,12)+''.join(figure(x,820,220+(x%3)*20,'#3a1a0a',pose='up' if k%2 else 'stand') for k,x in enumerate(range(60,800,100)))
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="70" ry="44" fill="#fff"/><path d="M{x-10} {y+40} L{x-30} {y+80} L{x+10} {y+40}Z" fill="#fff"/><path d="M{x-30} {y} q30 20 60 0" stroke="#3a1a0a" stroke-width="8" fill="none"/>' for x,y in [(180,200),(420,140),(640,240)])
I[1738]=svg(b,d)

# 112 追憶: an old sepia photograph and a dried rose on a window ledge with rain outside, 1974
d,b=bg([(0,'#5a4a3a'),(1,'#8a7a6a')])
b+=rain(40,112,'#e8e0d0',.3,8,480)+'<rect y="480" width="800" height="320" fill="#4a3424"/>'
b+='<rect x="220" y="360" width="240" height="180" fill="#d8c09a" transform="rotate(-6 340 450)"/>'+profile(370,540,.6,'#8a6a4a')+rose(520,500,.6,40)+'<path d="M520 540 L600 640" stroke="#5a3a2a" stroke-width="6"/>'
I[112]=svg(b,d)

# 566 秋のIndication: a girl's silhouette on a platform as golden ginkgo leaves fall around a signal light
d,b=bg([(0,'#e8a84a'),(1,'#fff0c8')])
b+=''.join(f'<path d="M{x} {y} q-20 -30 0 -40 q20 10 0 40Z" fill="#ffc82a" transform="rotate({x%120} {x} {y})"/>' for x,y in [(120,140),(260,220),(420,110),(560,200),(680,140),(180,360),(620,380),(320,320)])
b+='<rect y="560" width="800" height="240" fill="#7a6a5a"/><rect x="600" y="300" width="14" height="260" fill="#3a3a3a"/><rect x="580" y="240" width="54" height="80" rx="10" fill="#2a2a2a"/><circle cx="607" cy="262" r="14" fill="#3aff8a"/>'+figure(340,580,240,'#3a2a2a',hair='#3a2a2a')
I[566]=svg(b,d)

# 618 太陽と埃の中で: a dusty desert road with a blazing sun and two travellers' silhouettes, 1990 rock
d,b=bg([(0,'#e86a2a'),(1,'#f8d088')])
b+='<circle cx="400" cy="300" r="110" fill="#fff4c0"/>'+rays(400,300,20,'#fff',.15,10)+'<rect y="460" width="800" height="340" fill="#c8945a"/><path d="M380 460 L220 800 L580 800 L420 460Z" fill="#a8744a"/>'
b+=''.join(f'<circle cx="{random.Random(618*k).randint(0,800)}" cy="{random.Random(618*k+1).randint(460,800)}" r="{random.Random(618*k+2).randint(4,20)}" fill="#f4dcb0" opacity=".4"/>' for k in range(30))+figure(360,680,200,'#2a1a0a')+figure(450,680,210,'#2a1a0a')
I[618]=svg(b,d)

# 1885 ALMIGHTY~仮面の約束: a half-mask and a trumpet crossed under a hard red spotlight, ska rock
d,b=bg([(0,'#0a0a0a'),(1,'#4a0a0a')])
b+='<path d="M340 0 L460 0 L640 700 L160 700Z" fill="#ff3a2a" opacity=".2"/>'
b+='<path d="M220 340 Q300 260 400 300 Q500 260 580 340 Q560 430 470 420 Q400 380 330 420 Q240 430 220 340Z" fill="#f4f4f4"/><ellipse cx="320" cy="350" rx="44" ry="24" fill="#0a0a0a"/><ellipse cx="480" cy="350" rx="44" ry="24" fill="#0a0a0a"/>'
b+='<g transform="rotate(20 400 560)"><rect x="200" y="540" width="320" height="26" fill="#e8b830"/><path d="M520 510 L640 470 L640 640 L520 596Z" fill="#e8b830"/><rect x="300" y="500" width="16" height="40" fill="#c8982a"/><rect x="340" y="500" width="16" height="40" fill="#c8982a"/><rect x="380" y="500" width="16" height="40" fill="#c8982a"/></g>'
I[1885]=svg(b,d)

# 140 そして・・・めぐり逢い: two paths in a snowy field converging at a single lit lamp post, enka reunion
d,b=bg([(0,'#3a4a6a'),(1,'#8a9ab8')])
b+=snow(50,140)+'<rect y="480" width="800" height="320" fill="#e8eef8"/><path d="M0 800 Q200 640 400 560 M800 800 Q600 640 400 560" stroke="#b8c4d8" stroke-width="40" fill="none"/>'
b+='<rect x="396" y="380" width="8" height="180" fill="#3a3a4a"/><circle cx="400" cy="380" r="14" fill="#fff4c8"/>'+glow(400,380,100,'#fff4c8',.6)+figure(250,680,170,'#1a1a2a')+figure(560,680,160,'#1a1a2a',hair='#1a1a2a')
I[140]=svg(b,d)

# 146 大阪しぐれ: a woman under a red umbrella on a rainy Osaka canal bridge with neon reflections, enka
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a3a')])
b+=rain(80,146,'#cfe6ff',.35)+skyline(500,'#14141e',146,80,260,'#ff8ad0',60)+'<rect y="500" width="800" height="300" fill="#141428"/>'+''.join(f'<rect x="{x}" y="520" width="10" height="200" fill="{c}" opacity=".3"/>' for x,c in [(100,'#ff4fa0'),(300,'#ffd02a'),(620,'#4fd0ff')])
b+='<rect x="0" y="560" width="800" height="16" fill="#3a2a2a"/>'+figure(440,560,220,'#000',hair='#000')+wagasa(440,370,110,'#c8102a',-8)
I[146]=svg(b,d)

# 147 ふたりの大阪: two silhouettes sharing a drink at a small Osaka bar counter with a red lantern, enka duet
d,b=bg([(0,'#2a1414'),(1,'#5a2a1a')])
b+=chochin(160,180,60)+'<rect x="0" y="500" width="800" height="40" fill="#8a5a3a"/><rect y="540" width="800" height="260" fill="#3a1a14"/>'+''.join(f'<rect x="{x}" y="300" width="40" height="120" rx="8" fill="{c}" opacity=".7"/>' for x,c in [(480,'#5a8a5a'),(540,'#c8a24a'),(600,'#8a3a2a'),(660,'#5a5a8a')])+'<rect x="440" y="420" width="320" height="10" fill="#5a3a2a"/>'
b+=figure(300,560,240,'#0a0a0a',hair='#0a0a0a')+figure(400,560,250,'#0a0a0a')+'<rect x="330" y="470" width="20" height="30" fill="#f4f0e4"/><rect x="380" y="470" width="20" height="30" fill="#f4f0e4"/>'
I[147]=svg(b,d)

# 407 時をかける少女: a girl leaping through a swirl of clock faces and lavender sprigs, 1983/94 classic
d,b=bg([(0,'#5a4a9a'),(1,'#d8c8f0')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f4f0e8" opacity=".7" stroke="#c8a24a" stroke-width="4"/><path d="M{x} {y} L{x} {y-r*.7} M{x} {y} L{x+r*.5} {y+r*.2}" stroke="#3a3a4a" stroke-width="4"/>' for x,y,r in [(160,200,60),(620,180,44),(680,520,56),(140,560,40)])
b+=''.join(f'<path d="M{x} {y} L{x+10} {y-80}" stroke="#4a8a3a" stroke-width="4"/>'+''.join(f'<ellipse cx="{x+2+i*1.6}" cy="{y-30-i*12}" rx="7" ry="10" fill="#9a6ad8"/>' for i in range(5)) for x,y in [(300,760),(500,780),(560,740)])
b+='<g transform="rotate(-20 400 400)">'+figure(400,560,280,'#1a1430',pose='up',hair='#1a1430')+'</g>'
I[407]=svg(b,d)

# 575 虹のDreamer: a girl sitting on top of a rainbow arc dangling her feet above the clouds, 80s idol
d,b=bg([(0,'#7ac8ff'),(1,'#fff0f8')])
b+=''.join(f'<path d="M{80+k*24} 700 A{320-k*24} {320-k*24} 0 0 1 {720-k*24} 700" stroke="{c}" stroke-width="24" fill="none"/>' for k,c in enumerate(['#ff4a4a','#ff9a2a','#ffe02a','#5ad85a','#3a9aff','#8a5aff']))
b+=cloud(120,700,1.6)+cloud(680,700,1.6)+figure(400,400,140,'#3a2a4a',hair='#3a2a4a')+sparkle(560,200,20,'#fff')+sparkle(240,180,16,'#fff')
I[575]=svg(b,d)

# 619 ひとり咲き: a single wild flower blooming alone in a cracked dry field under a wide sky, 1979 folk-rock
d,b=bg([(0,'#9ab8d8'),(1,'#f0e4c8')])
b+='<rect y="500" width="800" height="300" fill="#c8a878"/>'+''.join(f'<path d="M{x} {y} l40 20 l-10 40 l50 10" stroke="#8a6a4a" stroke-width="3" fill="none"/>' for x,y in [(80,560),(500,620),(250,700),(620,520)])
b+='<path d="M400 640 Q390 520 410 420" stroke="#3a7a2a" stroke-width="8" fill="none"/><path d="M400 560 q-50 -20 -70 10 q40 10 70 -10Z" fill="#3a7a2a"/>'+flower(410,400,60,6,'#ff6a3a','#ffd02a')
I[619]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
