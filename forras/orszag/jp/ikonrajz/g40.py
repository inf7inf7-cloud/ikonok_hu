import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 40. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 760 かぞえうた: small hands counting on fingers beside a row of tiny candles, gentle 2012 ballad
d,b=bg([(0,'#2a2a3a'),(1,'#5a4a5a')])
b+='<rect y="560" width="800" height="240" fill="#3a2a2a"/>'+''.join(f'<rect x="{x}" y="470" width="20" height="90" fill="#f4ece0"/><path d="M{x+10} 448 q10 12 0 22 q-10 -10 0 -22Z" fill="#ffd02a"/>'+glow(x+10,455,40,'#ffd27a',.5) for x in range(150,700,90))
b+=''.join(f'<circle cx="{x}" cy="300" r="10" fill="#fff4c8" opacity=".6"/>' for x in range(200,620,70))
I[760]=svg(b,d)

# 1020 AS FOR ONE DAY: a girl group's silhouettes on a hill counting down to one sunset day, warm ballad
d,b=bg([(0,'#ff8a6a'),(1,'#ffd8b0')])
b+='<circle cx="400" cy="460" r="100" fill="#fff0b0"/><path d="M0 560 Q400 480 800 560 L800 800 L0 800Z" fill="#5a3a4a"/>'+''.join(figure(x,560-abs(400-x)*-.05,170,'#2a1424',hair='#2a1424') for x in (180,260,340,420,500,580))
I[1020]=svg(b,d)

# 1021 ザ☆ピ~ス!: a giant peace-sign rainbow balloon over a happy street parade with confetti
d,b=bg([(0,'#5ac8ff'),(1,'#fff0c0')])
b+=confetti(80,1021,['#ff4a8a','#ffd02a','#5ad87a','#3ab0ff'])+'<circle cx="400" cy="300" r="150" fill="none" stroke="#ff4a8a" stroke-width="30"/><path d="M400 150 L400 450 M400 300 L294 406 M400 300 L506 406" stroke="#ff4a8a" stroke-width="30" stroke-linecap="round"/>'
b+='<rect y="620" width="800" height="180" fill="#c8b8a8"/>'+''.join(figure(x,780,180,'#3a2a3a',pose='up',hair='#3a2a3a') for x in range(80,800,110))
I[1021]=svg(b,d)

# 1283 リルラ リルハ: a girl skipping with a skateboard under a polka-dot sky and stars, quirky pop rock
d,b=bg([(0,'#ffe04a'),(1,'#ff9ab8')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#fff" opacity=".4"/>' for x in range(60,800,120) for y in range(60,500,120))+'<rect y="620" width="800" height="180" fill="#3a3a4a"/>'
b+='<g transform="rotate(-10 400 450)">'+figure(400,600,280,'#1a1a2a',pose='up',hair='#1a1a2a')+'</g><rect x="300" y="650" width="220" height="18" rx="9" fill="#e8302a"/><circle cx="340" cy="676" r="12" fill="#fff"/><circle cx="480" cy="676" r="12" fill="#fff"/>'
I[1283]=svg(b,d)

# 1806 僕たちはひとつの光: nine coloured beams of light converging into one bright point above a stage
d,b=bg([(0,'#0a0a2a'),(1,'#2a1a4a')])
b+=''.join(f'<path d="M{80+k*80} 800 L400 260" stroke="{c}" stroke-width="16" opacity=".7"/>' for k,c in enumerate(['#ff4a4a','#ff9a2a','#ffe02a','#5ad85a','#3ad8c8','#3a9aff','#6a5aff','#c85aff','#ff5ac8']))
b+='<circle cx="400" cy="260" r="40" fill="#fff"/>'+glow(400,260,160,'#fff',.6)+starsf(40,1806,220)
I[1806]=svg(b,d)

# 4 人生一路: a single straight road climbing over many hills toward a rising sun, 1970 enka
d,b=bg([(0,'#ff8a3a'),(1,'#ffe0a0')])
b+='<circle cx="400" cy="300" r="90" fill="#fff4c0"/>'+rays(400,300,20,'#fff',.2,10)+hills(380,30,'#a86a4a',4,4)+hills(480,40,'#7a4a3a',41,4)+hills(600,40,'#4a2a2a',42,4)
b+='<path d="M390 380 L360 800 L440 800 L410 380Z" fill="#e8d0a0"/>'+figure(400,700,160,'#1a0a0a')
I[4]=svg(b,d)

# 531 雨の終わる場所: rain stopping at a line where clear sky and a rainbow begin, a figure stepping out
d,b=bg([(0,'#5a6a8a'),(1,'#9ac8f0')])
b+='<rect x="400" y="0" width="400" height="800" fill="#8ad0ff"/>'+rain(60,531,'#e8f0ff',.5,0,800).replace('<path','<path clip-path="url(#lh)"')+'<path d="M420 560 A240 240 0 0 1 900 560" stroke="#ffe02a" stroke-width="20" fill="none" opacity=".7"/><path d="M450 560 A210 210 0 0 1 870 560" stroke="#5ad85a" stroke-width="20" fill="none" opacity=".7"/>'
b+='<rect y="620" width="800" height="180" fill="#6a8a6a"/>'+figure(420,640,240,'#1a1a2a',hair='#1a1a2a')
d+='<clipPath id="lh"><rect width="400" height="800"/></clipPath>'
I[531]=svg(b,d)

# 532 ROMANCE: two champagne glasses clinking in front of a glittering harbour night, 90s pop
d,b=bg([(0,'#1a0a3a'),(1,'#5a2a6a')])
b+=skyline(560,'#140a24',532,60,200,'#ffd27a',60)+'<rect y="560" width="800" height="240" fill="#1a1440"/>'+''.join(f'<rect x="{x}" y="580" width="6" height="120" fill="#ffd27a" opacity=".3"/>' for x in range(40,800,60))
b+='<g transform="rotate(14 340 420)"><path d="M300 260 L380 260 L360 400 L320 400Z" fill="#f4e8c0" opacity=".85"/><rect x="336" y="400" width="8" height="120" fill="#f4f4f4"/><ellipse cx="340" cy="520" rx="40" ry="8" fill="#f4f4f4"/></g>'
b+='<g transform="rotate(-14 460 420)"><path d="M420 260 L500 260 L480 400 L440 400Z" fill="#f4e8c0" opacity=".85"/><rect x="456" y="400" width="8" height="120" fill="#f4f4f4"/><ellipse cx="460" cy="520" rx="40" ry="8" fill="#f4f4f4"/></g>'+sparkle(400,240,26,'#fff')
I[532]=svg(b,d)

# 1092 夏の終わり: a wind chime and a fading sparkler on a veranda at a summer's-end dusk
d,b=bg([(0,'#3a3a6a'),(1,'#ff9a6a')])
b+='<rect y="560" width="800" height="240" fill="#5a3a2a"/>'+''.join(f'<rect x="0" y="{y}" width="800" height="6" fill="#4a2a1a"/>' for y in range(580,800,40))+'<rect x="0" y="0" width="800" height="60" fill="#2a1a14"/>'
b+='<path d="M400 60 L400 120" stroke="#888" stroke-width="3"/><path d="M360 160 Q360 110 400 110 Q440 110 440 160Z" fill="#cfe6ff" opacity=".8"/><path d="M400 160 L400 260" stroke="#888" stroke-width="2"/><rect x="384" y="260" width="32" height="70" fill="#ff8ab0"/>'
b+='<path d="M560 600 L620 460" stroke="#3a3a3a" stroke-width="3"/><circle cx="620" cy="460" r="8" fill="#ff8a2a"/>'+''.join(f'<path d="M620 460 l{dx} {dy}" stroke="#ffd02a" stroke-width="2"/>' for dx,dy in [(-14,-10),(12,-12),(16,6),(-10,14),(4,-18)])
I[1092]=svg(b,d)

# 39 加賀の女: a woman in a kimono silhouette walking along a snowy riverside lane in Kanazawa, 1969 enka
d,b=bg([(0,'#2a3450'),(1,'#6a7a9a')])
b+=snow(70,39)+'<rect y="560" width="800" height="240" fill="#e8eef8"/><path d="M0 640 Q400 600 800 650 L800 700 Q400 650 0 690Z" fill="#3a4a6a"/>'+''.join(f'<rect x="{x}" y="380" width="120" height="180" fill="#4a3428"/><path d="M{x-10} 390 L{x+60} 340 L{x+130} 390Z" fill="#f4f6ff"/>' for x in (520,660))
b+=figure(300,580,240,'#1a1424',hair='#1a1424')+'<path d="M260 440 L340 440 L360 580 L240 580Z" fill="#5a1a2a"/>'+wagasa(300,330,90,'#2a2a3a',-6)
I[39]=svg(b,d)

# 205 神田川: a small wooden bathhouse basin with a towel on a riverside alley at dusk, 70s folk
d,b=bg([(0,'#5a4a7a'),(1,'#ffa88a')])
b+='<rect x="0" y="200" width="300" height="380" fill="#3a2a2a"/><rect x="40" y="260" width="80" height="80" fill="#ffd27a" opacity=".7"/>'+'<rect y="580" width="800" height="220" fill="#4a5a7a"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".4"/>' for x,y in [(380,640),(560,700),(200,740)])
b+='<rect x="0" y="560" width="800" height="20" fill="#8a7a6a"/><path d="M380 500 L500 500 L490 560 L390 560Z" fill="#e8c88a"/><path d="M390 500 Q440 470 490 500" stroke="#fff" stroke-width="14" fill="none"/><rect x="440" y="470" width="14" height="60" fill="#fff"/>'
I[205]=svg(b,d)

# 298 きみの朝: morning sunlight pouring through curtains onto a bed with a guitar resting on it, 1979
d,b=bg([(0,'#fff0d0'),(1,'#f8e4c0')])
b+='<rect x="460" y="80" width="280" height="380" fill="#fff8e0"/>'+'<path d="M460 80 Q500 260 470 460 L440 460 L440 80Z M740 80 Q700 260 730 460 L760 460 L760 80Z" fill="#f4c8a0"/>'+'<path d="M460 460 L100 800 L700 800 L740 460Z" fill="#fff8e0" opacity=".4"/>'
b+='<rect x="60" y="520" width="560" height="160" fill="#e8e0f0"/><rect x="60" y="640" width="560" height="160" fill="#a89ab8"/>'+guitar(300,560,.8,-70,'#c8702a')
I[298]=svg(b,d)

# 1386 イチャイチャ虫: two cute ladybugs touching antennae on a leaf with tiny hearts, playful idol pop
d,b=bg([(0,'#c8f0a0'),(1,'#fff0c0')])
b+='<path d="M80 560 Q400 280 720 560 Q400 680 80 560Z" fill="#5ab84a"/><path d="M120 560 Q400 480 680 560" stroke="#3a8a2a" stroke-width="6" fill="none"/>'
for x,f in [(310,1),(490,-1)]:
  b+=f'<ellipse cx="{x}" cy="500" rx="70" ry="60" fill="#e8202a"/><path d="M{x} 440 L{x} 560" stroke="#1a1a1a" stroke-width="4"/><circle cx="{x+f*60}" cy="470" r="30" fill="#1a1a1a"/>'+''.join(f'<circle cx="{x+dx}" cy="{500+dy}" r="11" fill="#1a1a1a"/>' for dx,dy in [(-35,-10),(35,-10),(-30,25),(30,25)])+f'<path d="M{x+f*70} 450 Q{x+f*90} 400 {x+f*95} 390" stroke="#1a1a1a" stroke-width="4" fill="none"/>'
b+=heart(400,330,26,'#ff4a8a')+heart(360,270,16,'#ff7aa8')+heart(450,250,14,'#ff7aa8')
I[1386]=svg(b,d)

# 1636 INZM: a jagged lightning bolt striking down between two crouched dancers' silhouettes, 2024 hip-hop
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=bolt([(420,0),(360,260),(440,280),(370,560)],'#fff',16)+glow(400,300,200,'#8ab0ff',.5)+bolt([(420,0),(360,260),(440,280),(370,560)],'#8ab0ff',30,.4)
b+='<rect y="640" width="800" height="160" fill="#0a0a14"/>'+figure(200,660,260,'#000')+figure(600,660,260,'#000')
I[1636]=svg(b,d)

# 314 心の友: two hands clasped around a small warm candle in the dark, heartfelt 1982 ballad
d,b=bg([(0,'#1a1414'),(1,'#3a2a24')])
b+=glow(400,400,240,'#ffb070',.45)+'<rect x="370" y="400" width="60" height="120" fill="#f4ece0"/><path d="M400 350 q24 30 0 50 q-24 -20 0 -50Z" fill="#ffd02a"/>'
b+='<path d="M180 640 Q220 520 360 500 L360 560 Q260 580 240 680Z" fill="#c8906a"/><path d="M620 640 Q580 520 440 500 L440 560 Q540 580 560 680Z" fill="#b8805a"/>'
I[314]=svg(b,d)

# 458 お先に失礼: a schoolgirl waving goodbye from a school gate as she skips off at sunset, idol pop
d,b=bg([(0,'#ff8a8a'),(1,'#ffe0b0')])
b+='<rect y="600" width="800" height="200" fill="#b8a090"/><rect x="40" y="300" width="60" height="300" fill="#8a7a7a"/><rect x="200" y="300" width="60" height="300" fill="#8a7a7a"/>'+''.join(f'<rect x="{x}" y="400" width="8" height="200" fill="#5a5a5a"/>' for x in range(100,200,20))
b+=figure(520,620,260,'#2a1a2a',pose='up',hair='#2a1a2a')+'<rect x="560" y="480" width="50" height="40" rx="6" fill="#5a2a1a"/>'
I[458]=svg(b,d)

# 466 技ありっ!: a judo belt tied around a pink heart with a referee's raised hand, comic 80s idol unit
d,b=bg([(0,'#fff0a0'),(1,'#ffd0d8')])
b+=heart(400,420,140,'#ff7aa8')+'<rect x="240" y="400" width="320" height="36" fill="#1a1a1a"/><path d="M380 436 L340 560 L370 560 L400 440 L430 560 L460 560 L420 436Z" fill="#1a1a1a"/><rect x="380" y="396" width="40" height="44" fill="#1a1a1a"/>'
b+=sparkle(200,200,24,'#fff')+sparkle(620,220,30,'#fff')+sparkle(600,620,20,'#fff')
I[466]=svg(b,d)

# 533 WHEREVER YOU ARE: a globe with a single glowing heart pin and a dotted flight line, 90s pop
d,b=bg([(0,'#3a5ad8'),(1,'#a8d8ff')])
b+='<circle cx="400" cy="440" r="220" fill="#1a7ad8"/><path d="M270 330 Q340 290 370 360 Q320 420 270 400Z M430 460 Q520 420 550 510 Q480 570 430 530Z M300 520 Q340 540 330 590Z" fill="#5ac86a"/>'
b+='<path d="M290 380 Q400 200 500 490" stroke="#fff" stroke-width="4" stroke-dasharray="10 10" fill="none"/>'+heart(500,470,30,'#ff4a6a')+'<circle cx="290" cy="380" r="10" fill="#fff"/>'
I[533]=svg(b,d)

# 597 すばらしい日々: an old cassette tape with tangled tape forming a skyline of memories, 90s rock
d,b=bg([(0,'#f4c88a'),(1,'#e8e0d0')])
b+='<rect x="160" y="300" width="480" height="300" rx="20" fill="#2a2a34"/><rect x="220" y="340" width="360" height="120" rx="8" fill="#f4ece0"/><circle cx="300" cy="400" r="34" fill="#2a2a34"/><circle cx="500" cy="400" r="34" fill="#2a2a34"/>'+''.join(f'<rect x="{x}" y="500" width="40" height="60" fill="#5a5a64"/>' for x in (260,340,420,500))
b+='<path d="M300 300 Q260 200 340 160 Q420 120 400 220 Q380 280 460 220 Q560 140 520 260" stroke="#5a3a2a" stroke-width="4" fill="none"/>'
I[597]=svg(b,d)

# 598 大迷惑: a man with a suitcase being dragged away from a newly built home by a giant arrow, comic 80s rock
d,b=bg([(0,'#5ac8ff'),(1,'#e8f8ff')])
b+='<rect x="80" y="380" width="240" height="240" fill="#fff4e0"/><path d="M60 390 L200 280 L340 390Z" fill="#e8302a"/><rect x="170" y="500" width="60" height="120" fill="#8a5a3a"/>'+heart(200,340,20,'#ff7aa8')
b+='<rect y="620" width="800" height="180" fill="#8ac86a"/><path d="M380 300 L640 300 L640 250 L760 340 L640 430 L640 380 L380 380Z" fill="#ffd02a" stroke="#c8982a" stroke-width="4"/>'
b+='<g transform="rotate(-15 560 560)">'+figure(560,640,220,'#1a1a2a')+'</g><rect x="440" y="560" width="70" height="56" rx="8" fill="#6a3a2a"/>'
I[598]=svg(b,d)

# 677 愛という名のもとに: a wedding ring and a guitar pick on a rain-soaked windshield at night, 80s rock
d,b=bg([(0,'#0a1424'),(1,'#2a3a54')])
b+=''.join(f'<circle cx="{random.Random(677*k).randint(0,800)}" cy="{random.Random(677*k+1).randint(0,500)}" r="{random.Random(677*k+2).randint(10,30)}" fill="{["#ffd27a","#ff6a6a"][k%2]}" opacity=".3"/>' for k in range(24))+rain(40,677,'#cfe6ff',.4)
b+='<path d="M0 560 Q400 480 800 560 L800 800 L0 800Z" fill="#1a1a24"/>'+ring(360,560,50,'#e8c86a',14)+sparkle(360,500,20,'#fff')+'<path d="M480 540 Q520 520 560 540 Q560 590 520 620 Q480 590 480 540Z" fill="#e8302a"/>'
I[677]=svg(b,d)

# 917 Be Yourself!: a single colourful figure standing out among a row of grey silhouettes, 90s boy group
d,b=bg([(0,'#e8f0ff'),(1,'#d8e0f0')])
b+='<rect y="640" width="800" height="160" fill="#b8c0cc"/>'+''.join(figure(x,660,240,'#8a909a') for x in (100,220,580,700))+figure(400,660,280,'#ff4a6a',pose='up')+rays(400,400,16,'#ffd02a',.25,10)
I[917]=svg(b,d)

# 1266 BLUE: a figure floating on their back in deep blue ocean water seen from above, 2018 boy group
d,b=bg([(0,'#0a4a8a'),(1,'#1a8ad8')])
b+=''.join(f'<path d="M{x} {y} q40 -14 80 0" stroke="#8ad0ff" stroke-width="4" fill="none" opacity=".5"/>' for x,y in [(80,140),(520,120),(220,620),(560,680),(100,420),(640,420)])+''.join(ring(400,400,r,'#cfe6ff',3,.4) for r in (160,220))
b+='<g transform="rotate(-30 400 400)">'+figure(400,560,320,'#0a2a4a',pose='up')+'</g>'
I[1266]=svg(b,d)

# 1273 関風ファイティング: a whirlwind of Kansai energy: a folding fan and tornado swirl with a fist pump
d,b=bg([(0,'#ffd04a'),(1,'#e8402a')])
b+=''.join(f'<path d="M{400-r} {600-r*.4} Q400 {600-r*1.2} {400+r} {600-r*.4}" stroke="#fff" stroke-width="8" fill="none" opacity=".6"/>' for r in range(60,340,50))
b+='<path d="M400 680 L200 460 A280 280 0 0 1 600 460Z" fill="#c8102a"/>'+''.join(f'<path d="M400 680 L{400+280*math.cos(a)} {680-280*math.sin(a)}" stroke="#ffd04a" stroke-width="4"/>' for a in [math.radians(t) for t in range(55,130,12)])
I[1273]=svg(b,d)

# 1690 Wonderland: a giant keyhole glowing in a hedge maze at night, inviting entry, 2004 rock
d,b=bg([(0,'#0a1a14'),(1,'#1a3a2a')])
b+=starsf(40,1690,300)+'<rect x="0" y="300" width="800" height="500" fill="#1a4a2a"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="30" fill="#0a2a1a"/>' for x,y,w in [(0,420,300),(500,420,300),(100,540,220),(480,540,220),(0,660,280),(520,660,280)])
b+='<circle cx="400" cy="400" r="70" fill="#ffe08a"/><path d="M360 440 L440 440 L470 640 L330 640Z" fill="#ffe08a"/>'+glow(400,480,200,'#ffe08a',.4)
I[1690]=svg(b,d)

# 5 お祭りマンボ: a festival happi coat and paper fan whirling to a mambo beat with lanterns, 1952
d,b=bg([(0,'#1a0a2a'),(1,'#a82a2a')])
b+='<path d="M0 120 Q400 200 800 120" stroke="#3a2a2a" stroke-width="4" fill="none"/>'+''.join(chochin(x,170-(x-400)**2/6000+40,32) for x in (100,250,400,550,700))
b+='<path d="M280 360 L520 360 L600 460 L560 480 L540 440 L540 680 L260 680 L260 440 L240 480 L200 460Z" fill="#2a4ab8"/><path d="M380 360 L400 680 L420 360" stroke="#f4f4f4" stroke-width="10" fill="none"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="12" fill="#f4f4f4" opacity=".6"/>' for x,y in [(320,500),(480,560),(320,620),(480,440)])
b+=note(160,560,40,'#ffd02a')+note(640,580,40,'#ffd02a',True)
I[5]=svg(b,d)

# 918 出せない手紙: an unsent letter tucked under a desk lamp with a stamp beside it, late night
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<rect y="520" width="800" height="280" fill="#3a2a24"/><path d="M500 200 L600 360 L400 360Z" fill="#2a2a34"/><rect x="540" y="360" width="10" height="160" fill="#2a2a34"/><path d="M400 360 L200 720 L760 720 L600 360Z" fill="#fff4c8" opacity=".2"/>'
b+='<rect x="280" y="540" width="260" height="170" fill="#f4ece0" transform="rotate(-6 410 625)"/><path d="M280 540 L410 630 L540 540" stroke="#c8b8a8" stroke-width="4" fill="none" transform="rotate(-6 410 625)"/><rect x="560" y="600" width="44" height="54" fill="#e8302a" stroke="#fff" stroke-width="4" stroke-dasharray="4 4"/>'
I[918]=svg(b,d)

# 1022 抱いてHOLD ON ME!: two silhouettes in an embrace inside a spinning neon heart, 1998 idol pop
d,b=bg([(0,'#2a0a3a'),(1,'#ff4a8a')])
b+=heart(400,420,190,'none',' stroke="#fff" stroke-width="10"')+glow(400,420,220,'#ff8ad0',.4)+figure(370,620,280,'#1a0a1a',hair='#1a0a1a')+figure(430,620,300,'#1a0a1a')+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(160,180,24),(640,160,30),(660,560,20)])
I[1022]=svg(b,d)

# 1664 YUME日和: a girl lying in a field of flowers looking up at drifting dream-like bubbles and clouds
d,b=bg([(0,'#9ad8ff'),(1,'#fff0f8')])
b+=cloud(200,200,1.2)+cloud(600,160,1.0)+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".4" stroke="#fff" stroke-width="3"/>' for x,y,r in [(300,340,30),(420,280,40),(540,360,24),(380,420,18)])
b+='<path d="M0 560 Q400 520 800 560 L800 800 L0 800Z" fill="#8ad06a"/>'+''.join(flower(x,y,16,5,c,'#ffd02a') for x,y,c in [(100,640,'#ff8ab0'),(220,700,'#fff'),(560,660,'#ffd02a'),(700,720,'#ff8ab0'),(640,600,'#fff')])
b+='<g transform="rotate(-90 400 620)">'+figure(400,700,240,'#3a2a3a',hair='#3a2a3a')+'</g>'
I[1664]=svg(b,d)

# 1823 踊り子: a dancer's silhouette under a small stage spotlight, a worn ticket stub on the floor, 1983 folk
d,b=bg([(0,'#1a0a14'),(1,'#3a1a24')])
b+='<path d="M370 0 L430 0 L560 600 L240 600Z" fill="#ffd8a8" opacity=".2"/><ellipse cx="400" cy="600" rx="170" ry="34" fill="#ffd8a8" opacity=".35"/><rect y="600" width="800" height="200" fill="#2a1414"/>'
b+='<g transform="rotate(8 400 450)">'+figure(400,600,320,'#000',pose='up',hair='#000')+'</g><path d="M340 600 Q400 500 470 600Z" fill="#000"/><rect x="560" y="680" width="100" height="44" fill="#d8c8a8" transform="rotate(-12 610 700)"/>'
I[1823]=svg(b,d)

# 1887 昴: the Pleiades star cluster shining over a vast dark wilderness and a lone traveller, 1980 ballad
d,b=bg([(0,'#020818'),(1,'#141e3a')])
b+=starsf(90,1887,560)+''.join(star5(x,y,s,'#cfe6ff')+glow(x,y,s*2,'#8ab0ff',.5) for x,y,s in [(360,160,18),(410,140,14),(440,180,16),(390,210,20),(470,150,12),(430,230,12),(500,200,10)])
b+='<path d="M0 600 Q200 560 400 600 T800 580 L800 800 L0 800Z" fill="#0a0a14"/>'+figure(400,620,180,'#000')
I[1887]=svg(b,d)

# 1895 雨の物語: raindrops trickling down a window drawing lines into a little story, 1977 folk
d,b=bg([(0,'#7a8aa8'),(1,'#b8c4d8')])
b+='<rect x="100" y="80" width="600" height="560" fill="#9aaac4"/>'+''.join(f'<path d="M{x} {y} Q{x+10} {y+100} {x-6} {y+200}" stroke="#e8f0ff" stroke-width="5" fill="none"/><circle cx="{x-6}" cy="{y+200}" r="8" fill="#e8f0ff"/>' for x,y in [(200,120),(320,200),(440,140),(560,260),(620,120)])
b+='<rect x="100" y="80" width="600" height="560" fill="none" stroke="#5a4a3a" stroke-width="18"/><rect x="60" y="640" width="680" height="30" fill="#5a4a3a"/><rect y="670" width="800" height="130" fill="#3a2a24"/>'+profile(360,640,.8,'#2a2a34')
I[1895]=svg(b,d)

# 73 冬のリヴィエラ: a winter Mediterranean-style seaside promenade with a lone man in a coat, 1982 pop-enka
d,b=bg([(0,'#5a7aa8'),(1,'#d8e0ec')])
b+='<rect y="440" width="800" height="200" fill="#3a6aa8"/>'+''.join(f'<path d="M{x} {y} q30 -6 60 0" stroke="#fff" stroke-width="3" fill="none" opacity=".5"/>' for x,y in [(100,480),(400,520),(600,470)])+'<rect y="640" width="800" height="160" fill="#c8c0b0"/>'
b+=''.join(f'<rect x="{x}" y="560" width="10" height="80" fill="#e8e0d0"/>' for x in range(0,800,40))+'<rect y="550" width="800" height="12" fill="#e8e0d0"/>'+figure(520,700,280,'#1a1a24')+bird(200,200,30,'#fff')+bird(260,160,24,'#fff')
I[73]=svg(b,d)

# 166 雨の慕情: a woman with an umbrella waiting by a lit window in heavy rain, 1980 enka
d,b=bg([(0,'#1a2030'),(1,'#3a4058')])
b+=rain(100,166,'#cfe6ff',.4)+'<rect x="480" y="120" width="320" height="560" fill="#2a2430"/><rect x="540" y="200" width="160" height="200" fill="#ffd27a"/>'+glow(620,300,140,'#ffd27a',.4)
b+='<rect y="680" width="800" height="120" fill="#14182a"/>'+figure(300,700,260,'#000',hair='#000')+wagasa(300,440,110,'#3a4a8a',-6)
I[166]=svg(b,d)

# 1710 BABY! 恋にKNOCK OUT!: a pink boxing glove punching a heart with comic impact stars, idol trio pop
d,b=bg([(0,'#ffe04a'),(1,'#ff9ac0')])
b+=rays(500,400,18,'#fff',.3,14)+'<path d="M500 400 L540 320 L570 390 L650 360 L600 430 L680 480 L590 480 L600 560 L540 500 L480 560 L490 480Z" fill="#fff"/>'+heart(560,440,60,'#e8102a')
b+='<rect x="60" y="400" width="130" height="120" rx="14" fill="#fff"/><rect x="170" y="330" width="260" height="250" rx="110" fill="#ff5a9a"/><ellipse cx="300" cy="590" rx="70" ry="40" fill="#ff5a9a"/><path d="M220 360 Q300 330 380 370" stroke="#fff" stroke-width="6" fill="none" opacity=".6"/><ellipse cx="340" cy="540" rx="60" ry="34" fill="#e8408a"/>'
I[1710]=svg(b,d)

# 6 港町十三番地: a cobbled harbour street with a numbered lamp post and ships' masts at dusk, 1957
d,b=bg([(0,'#4a5a8a'),(1,'#ffb08a')])
b+='<rect y="500" width="800" height="120" fill="#3a5a8a"/>'+''.join(f'<path d="M{x} 500 L{x} 260 M{x-50} 320 L{x+50} 320" stroke="#2a2030" stroke-width="6"/><path d="M{x-80} 500 L{x+80} 500 L{x+60} 540 L{x-60} 540Z" fill="#2a2030"/>' for x in (480,660))
b+='<rect y="620" width="800" height="180" fill="#6a5a5a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="26" ry="10" fill="#5a4a4a"/>' for x in range(20,800,60) for y in (650,700,750))
b+='<rect x="190" y="300" width="10" height="340" fill="#1a1a1a"/><rect x="170" y="280" width="50" height="40" fill="#1a1a1a"/><rect x="178" y="288" width="34" height="24" fill="#ffd27a"/>'+glow(195,300,80,'#ffd27a',.5)+'<rect x="200" y="400" width="60" height="40" fill="#f4f0e8"/>'
I[6]=svg(b,d)

# 40 風雪ながれ旅: a wandering shamisen player trudging through a blizzard on a northern road, 1980 enka
d,b=bg([(0,'#4a5a74'),(1,'#a8b4c8')])
b+=snow(110,40)+''.join(f'<path d="M{x} {y} l-80 30" stroke="#fff" stroke-width="3" opacity=".6"/>' for x,y in [(600,200),(700,320),(500,420),(300,160)])+'<rect y="600" width="800" height="200" fill="#e8eef8"/>'
b+=figure(400,640,280,'#1a1a24')+'<path d="M340 360 Q400 330 460 360 L470 380 L330 380Z" fill="#c8a870"/><rect x="430" y="380" width="10" height="200" fill="#5a3a2a" transform="rotate(-25 435 480)"/><rect x="380" y="500" width="60" height="70" rx="6" fill="#d8c8a8" transform="rotate(-25 410 535)"/>'
I[40]=svg(b,d)

# 98 ターンAターン: a full moon with a giant sand hourglass turning over in front of it, 1999 anime theme
d,b=bg([(0,'#0a1028'),(1,'#2a3460')])
b+=starsf(70,98,800)+moon(400,380,220)
b+='<g transform="rotate(20 400 400)"><path d="M320 220 L480 220 L410 400 L480 580 L320 580 L390 400Z" fill="#cfe6ff" opacity=".6" stroke="#c8a24a" stroke-width="8"/><rect x="300" y="200" width="200" height="24" fill="#c8a24a"/><rect x="300" y="576" width="200" height="24" fill="#c8a24a"/><path d="M340 560 L460 560 L410 480 L390 480Z" fill="#e8c86a"/><path d="M370 250 L430 250 L405 300 L395 300Z" fill="#e8c86a"/></g>'
I[98]=svg(b,d)

# 185 結婚しようよ: a young couple's silhouettes under a church bell with flowers in long hair, 1972 folk
d,b=bg([(0,'#a8d8ff'),(1,'#fff4e0')])
b+='<rect x="520" y="200" width="160" height="400" fill="#f4f0e8"/><path d="M500 210 L600 100 L700 210Z" fill="#c84a3a"/><path d="M580 240 Q600 210 620 240 L624 290 L576 290Z" fill="#c8a24a"/>'+'<rect y="600" width="800" height="200" fill="#8ac86a"/>'
b+=figure(260,640,260,'#2a2a3a',hair='#2a2a3a')+figure(380,640,280,'#2a2a3a',hair='#2a2a3a')+''.join(flower(x,y,10,5,c,'#ffd02a') for x,y,c in [(250,385,'#ff8ab0'),(270,390,'#fff')])+heart(320,320,26,'#ff7aa8')
I[185]=svg(b,d)

# 196 リバーサイド ホテル: a riverside hotel's lit windows reflecting into a dark river at night, 1982
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=starsf(40,196,300)+'<rect x="200" y="160" width="400" height="320" fill="#1a1a2a"/>'+''.join(f'<rect x="{x}" y="{y}" width="40" height="30" fill="{"#ffd27a" if (x+y)%3 else "#2a2a3a"}"/>' for x in range(230,580,60) for y in range(190,460,50))
b+='<rect y="480" width="800" height="320" fill="#0a1020"/>'+''.join(f'<rect x="{x}" y="{500+k*14}" width="40" height="6" fill="#ffd27a" opacity="{.4-k*.05}"/>' for x in range(230,580,60) for k in range(6))
I[196]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
