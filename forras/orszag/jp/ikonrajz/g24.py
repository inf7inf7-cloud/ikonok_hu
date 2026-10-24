import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 24. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'

# 1313 チャンスの順番: a row of numbered tickets with one golden ticket glowing in the queue
d,b=bg([(0,'#3a1a5a'),(1,'#8a3a8a')])
for k in range(6):
    x=90+k*110;c='#ffd02a' if k==3 else '#f4e8f8'
    b+=f'<g transform="rotate({(k-3)*6} {x+40} 460)"><rect x="{x}" y="380" width="80" height="160" rx="10" fill="{c}"/>'+txt(x+40,480,str(k+1),56,'#5a2a6a',900)+'</g>'
b+=glow(460,460,100,'#ffd02a',.5)+sparkle(500,340,22,'#fff')
I[1313]=svg(b,d)

# 1358 夏のFree & Easy: girls' silhouettes jumping off a pier into a turquoise sea, water splash and sun
d,b=bg([(0,'#2ac8ff'),(1,'#a8f0ff')])
b+=hinomaru_sun(640,140,60,'#fffbe0')+'<rect y="440" width="800" height="360" fill="#1ab0d8"/><rect x="-10" y="420" width="300" height="24" fill="#8a6a4a"/>'+''.join(f'<rect x="{20+k*80}" y="444" width="14" height="140" fill="#6a4a2a"/>' for k in range(4))
b+=''.join(f'<g transform="rotate({a} {x} {y})">'+figure(x,y,150,'#0a3a5a',pose='up')+'</g>' for x,y,a in [(340,380,-20),(460,320,10),(560,400,30)])+'<path d="M600 470 Q620 420 640 470 Q660 430 680 470" stroke="#fff" stroke-width="10" fill="none"/>'
I[1358]=svg(b,d)

# 1687 羽: a single white feather drifting down through a beam of light in a dark space
d,b=bg([(0,'#0a0a14'),(1,'#1a1a28')])
b+='<polygon points="360,0 440,0 520,800 280,800" fill="#fff6d8" opacity=".15"/>'
b+='<g transform="rotate(-30 400 400)"><path d="M400 200 Q470 300 440 460 Q420 560 400 620 Q380 560 360 460 Q330 300 400 200Z" fill="#f4f6ff"/><path d="M400 200 L400 640" stroke="#c8ccd8" stroke-width="4"/>'+''.join(f'<path d="M400 {260+k*40} L{440-k*2} {280+k*40} M400 {260+k*40} L{360+k*2} {280+k*40}" stroke="#d8dce8" stroke-width="2"/>' for k in range(8))+'</g>'
I[1687]=svg(b,d)

# 127 カメレオン・アーミー: a chameleon changing through disco colours on a mirror-ball branch, late 70s
d,b=bg([(0,'#2a0a3a'),(1,'#6a1a6a')])
b+=''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="{c}" opacity=".25"/>' for x,y,c in [(80,80,'#ff4fa0'),(680,120,'#4ad8ff'),(120,640,'#ffd02a'),(660,620,'#4ad84a')])
b+='<path d="M80 560 L720 520" stroke="#6a4a2a" stroke-width="20"/>'
b+='<path d="M220 520 Q260 400 400 400 Q540 400 560 500 L500 520 Q440 470 380 470 Q300 480 280 540Z" fill="url(#cam)"/><circle cx="520" cy="440" r="20" fill="#fff"/><circle cx="524" cy="440" r="9" fill="#000"/><path d="M220 520 Q160 560 180 620 Q220 640 230 600" stroke="#4ad84a" stroke-width="14" fill="none"/>'
d+=lg('cam',[(0,'#4ad84a',1),(.33,'#ffd02a',1),(.66,'#ff4fa0',1),(1,'#4ad8ff',1)],0,0,1,0)
I[127]=svg(b,d)

# 411 もう逢えないかもしれない: a girl at a seaside station watching a ferry leave, holding a ribbon in the wind
d,b=bg([(0,'#a8b8d8'),(1,'#e8d8e0')])
b+='<rect y="420" width="800" height="380" fill="#6a8ab8"/><path d="M500 420 L700 420 L680 450 L520 450Z" fill="#f4f0e8"/><rect x="580" y="380" width="40" height="40" fill="#f4f0e8"/>'
b+='<rect y="620" width="800" height="180" fill="#8a8a94"/>'+figure(260,640,300,'#2a2a3a')+'<path d="M300 440 Q380 400 420 430 Q460 460 520 420" stroke="#ff8ab8" stroke-width="8" fill="none" stroke-linecap="round"/>'
I[411]=svg(b,d)

# 749 Not Found: a search magnifying glass over an empty map with a dashed question-mark path
d,b=bg([(0,'#e8e4d8'),(1,'#c8c0b0')])
b+='<rect x="80" y="80" width="640" height="640" fill="#f4eed8" stroke="#a89878" stroke-width="6"/>'+''.join(f'<path d="M80 {k*80+80} L720 {k*80+80} M{k*80+80} 80 L{k*80+80} 720" stroke="#d8ccb0" stroke-width="2"/>' for k in range(8))
b+='<path d="M180 620 Q260 520 340 560 Q420 600 440 480 Q460 380 360 340" stroke="#c8302a" stroke-width="6" stroke-dasharray="14 10" fill="none"/>'
b+=ring(470,300,110,'#3a3a3a',22)+'<circle cx="470" cy="300" r="99" fill="#e8f4ff" opacity=".4"/><path d="M548 378 L660 490" stroke="#3a3a3a" stroke-width="34" stroke-linecap="round"/>'+txt(470,340,'?',130,'#c8302a',900)
I[749]=svg(b,d)

# 819 ダーリン: a heart-shaped neon sign "Darling" glowing in a smoky bar, a bottle and glass below
d,b=bg([(0,'#1a0a14'),(1,'#2a1420')])
b+=heart(400,300,170,'none','stroke="#ff4fa0" stroke-width="12"')+glow(400,300,200,'#ff4fa0',.25)+txt(400,320,'Darling',70,'#ff9ad8',700)
b+='<rect y="580" width="800" height="220" fill="#3a2010"/><path d="M220 580 L220 470 Q220 440 240 430 L240 400 L264 400 L264 430 Q284 440 284 470 L284 580Z" fill="#3a6a3a"/><path d="M520 580 L510 500 L570 500 L560 580Z" fill="#e8d8b0" opacity=".7"/>'
I[819]=svg(b,d)

# 951 Hey! みんな元気かい?: a crowd of waving hands silhouetted against a sunny open-air festival stage
d,b=bg([(0,'#5ac8ff'),(1,'#e0f6ff')])
b+=hinomaru_sun(400,200,80,'#fffbe0')+rays(400,200,24,'#fff',.25,8)+'<rect x="180" y="320" width="440" height="180" fill="#2a2a3a"/><rect x="160" y="300" width="480" height="30" fill="#ff4a4a"/>'
b+=''.join(f'<path d="M{x} 800 L{x+((x*7)%40-20)} {600-((x*13)%60)}" stroke="#1a1a2a" stroke-width="22" stroke-linecap="round"/><circle cx="{x}" cy="{720-((x*11)%20)}" r="24" fill="#1a1a2a"/>' for x in range(30,800,56))
I[951]=svg(b,d)

# 964 未来へ: a child and a mother's silhouette walking hand in hand on a road toward a sunrise
d,b=bg([(0,'#ffb88a'),(1,'#fff0d0')])
b+=hinomaru_sun(400,420,110,'#fff4d0')+rays(400,420,20,'#fff',.2,8)+'<rect y="480" width="800" height="320" fill="#b8c88a"/><path d="M380 480 L420 480 L620 800 L180 800Z" fill="#d8c8a0"/>'
b+=figure(360,720,240,'#3a2a2a')+figure(440,720,150,'#3a2a2a')+'<path d="M392 560 L418 600" stroke="#3a2a2a" stroke-width="10"/>'
I[964]=svg(b,d)

# 1012 talkin' 2 myself: a girl's silhouette facing her reflection in a dark window, speech bubbles crossing between them
d,b=bg([(0,'#1a1a2a'),(1,'#3a2a4a')])
b+='<rect x="420" y="120" width="300" height="520" fill="#2a3a5a" opacity=".8"/>'+figure(570,640,380,'#4a5a7a')+figure(260,680,420,'#05050a')
b+='<rect x="300" y="140" width="160" height="70" rx="35" fill="#fff"/><rect x="380" y="240" width="140" height="60" rx="30" fill="#c8d8f0"/>'
I[1012]=svg(b,d)

# 1062 相思相愛: two red strings forming a perfect heart between two small figures on hills
d,b=bg([(0,'#ffe0e8'),(1,'#fff8f0')])
b+='<path d="M-10 640 Q200 560 400 640 Q600 560 810 640 L810 810 L-10 810Z" fill="#c8e0a8"/>'+figure(160,620,180,'#3a2a3a')+figure(640,620,180,'#3a2a3a')
b+='<path d="M180 470 Q240 200 400 330 Q560 200 620 470" stroke="#e8102a" stroke-width="8" fill="none"/><path d="M400 330 L400 460" stroke="#e8102a" stroke-width="8"/>'
I[1062]=svg(b,d)

# 1239 時代: a big wall clock whose hands are made of light beams sweeping over five silhouettes on stage
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+='<circle cx="400" cy="300" r="220" fill="none" stroke="#c8d0e8" stroke-width="10"/>'+''.join(f'<path d="M{400+200*math.cos(math.radians(a)):.0f} {300+200*math.sin(math.radians(a)):.0f} L{400+180*math.cos(math.radians(a)):.0f} {300+180*math.sin(math.radians(a)):.0f}" stroke="#c8d0e8" stroke-width="6"/>' for a in range(0,360,30))
b+='<path d="M400 300 L400 120" stroke="#ffd02a" stroke-width="12"/><path d="M400 300 L540 380" stroke="#ffd02a" stroke-width="8"/><rect y="640" width="800" height="160" fill="#0a1020"/>'+''.join(figure(x,660,200,'#000') for x in (200,300,400,500,600))
I[1239]=svg(b,d)

# 87 瀬戸の花嫁: a small boat carrying a bride in a white wataboshi across the calm Seto Inland Sea, islands in the haze
d,b=bg([(0,'#f8d8b8'),(1,'#fff0e0')])
b+=hinomaru_sun(560,300,70,'#fff6d8',.8)+'<rect y="400" width="800" height="400" fill="#7ab0d0"/>'+''.join(f'<path d="M{x} 410 Q{x+80} 340 {x+160} 410Z" fill="#7a9a8a" opacity="{o}"/>' for x,o in [(60,.6),(260,.4),(520,.5)])
b+='<path d="M260 560 L540 560 L500 610 L300 610Z" fill="#8a5a3a"/><g fill="#fff"><circle cx="400" cy="490" r="24"/><path d="M370 510 L430 510 L440 560 L360 560Z"/></g><path d="M372 480 Q400 450 428 480 L432 500 L368 500Z" fill="#fff" stroke="#e8e8e8" stroke-width="3"/>'
I[87]=svg(b,d)

# 102 はじめての出来事: a schoolgirl's silhouette finding a pink love letter in her shoe locker, a 70s pastel palette
d,b=bg([(0,'#f8e0d8'),(1,'#fff4ec')])
b+=''.join(f'<rect x="{80+c*130}" y="{100+r2*120}" width="120" height="110" fill="#d8c8b8" stroke="#a89888" stroke-width="4"/>' for c in range(5) for r2 in range(4))
b+='<rect x="340" y="340" width="120" height="110" fill="#f4ead8"/><rect x="360" y="370" width="80" height="50" fill="#ffb8c8"/>'+heart(400,395,14,'#e8304a')
b+=figure(220,780,340,'#3a2a3a',pose='reach')
I[102]=svg(b,d)

# 529 Eyes to me: a pair of eyes glowing inside a heart-shaped window under soft moonlight
d,b=bg([(0,'#1a1a3a'),(1,'#3a3a6a')])
b+=moon(640,140,40)+heart(400,420,170,'#2a2a4a','stroke="#ffd8e8" stroke-width="8"')
for x in (330,470): b+=f'<path d="M{x-50} 400 Q{x} 360 {x+50} 400 Q{x} 440 {x-50} 400Z" fill="#fff"/><circle cx="{x}" cy="400" r="20" fill="#5a3a8a"/><circle cx="{x+6}" cy="394" r="6" fill="#fff"/>'
I[529]=svg(b,d)

# 1053 You Go Your Way: two arrows heading in different directions from the same point on a sunset road
d,b=bg([(0,'#ff8a5a'),(1,'#ffd8a8')])
b+=hinomaru_sun(400,360,90,'#fff2c8',.8)+'<rect y="420" width="800" height="380" fill="#6a5a5a"/>'
b+='<path d="M400 800 L400 560 L160 420 M400 560 L640 420" stroke="#f4f0e8" stroke-width="30" fill="none" stroke-linejoin="round"/><path d="M140 400 L200 400 L150 450Z M660 400 L600 400 L650 450Z" fill="#f4f0e8"/>'
b+=figure(250,520,150,'#1a1a2a')+figure(560,520,150,'#1a1a2a')
I[1053]=svg(b,d)

# 1111 Each Other's Way ~旅の途中~: a group of travellers' silhouettes walking along a long desert-coloured road with backpacks, a road sign ahead
d,b=bg([(0,'#5aa8e8'),(1,'#f0d8a8')])
b+='<rect y="520" width="800" height="280" fill="#d8b878"/><path d="M380 520 L420 520 L700 800 L100 800Z" fill="#8a8a8a"/>'+cloud(600,200,1.4)
b+='<rect x="560" y="420" width="10" height="160" fill="#4a4a4a"/><rect x="520" y="400" width="100" height="40" fill="#2a8a4a"/>'
b+=''.join(figure(x,y,h,'#2a1a1a') for x,y,h in [(300,760,220),(380,740,200),(460,750,210),(540,770,230)])+''.join(f'<rect x="{x-24}" y="{y-h*.75}" width="30" height="40" rx="6" fill="#5a3a2a"/>' for x,y,h in [(300,760,220),(380,740,200),(460,750,210),(540,770,230)])
I[1111]=svg(b,d)

# 1157 気まぐれロマンティック: a girl's silhouette holding a balloon that changes colour, polka dots and a cat's tail
d,b=bg([(0,'#ffd0e0'),(1,'#d0f0ff')])
b+=''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="{c}" opacity=".5"/>' for x,y,c in [(120,140,'#ff8ab8'),(260,220,'#8ab8ff'),(660,160,'#ffd06a'),(560,280,'#8ad8a8'),(120,520,'#8ab8ff'),(680,560,'#ff8ab8')])
b+='<path d="M460 220 Q470 340 420 470" stroke="#5a5a5a" stroke-width="3" fill="none"/><ellipse cx="460" cy="180" rx="70" ry="84" fill="url(#bal)"/>'+figure(400,740,320,'#2a2a4a',pose='wave')
d+=lg('bal',[(0,'#ff6a9a',1),(.5,'#ffb02a',1),(1,'#6aa8ff',1)],0,0,1,1)
I[1157]=svg(b,d)

# 1240 PIKA☆NCHI: five boys' silhouettes on a rooftop of a run-down apartment block at sunset, a big star above
d,b=bg([(0,'#ff8a3a'),(1,'#ffd08a')])
b+=star5(400,170,70,'#ffe86a')+glow(400,170,100,'#fff6a0',.5)+'<rect x="100" y="440" width="600" height="360" fill="#6a5a5a"/>'+''.join(f'<rect x="{140+(k%6)*90}" y="{480+(k//6)*90}" width="50" height="50" fill="#3a2a2a"/>' for k in range(18))
b+=''.join(figure(x,440,h,'#1a0a0a',pose=p) for x,h,p in [(200,190,'up'),(310,200,'stand'),(400,210,'wave'),(490,195,'stand'),(600,200,'up')])
I[1240]=svg(b,d)

# 1374 UDAGAWA GENERATION: a crowded Shibuya-style street with a steep slope and neon signs, silhouettes walking in formation
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+='<path d="M-10 800 L-10 560 L810 380 L810 800Z" fill="#1a1a24"/>'+''.join(neon(x,y,t,c,40) for x,y,t,c in [(140,180,'UDA','#ff4fa0'),(620,140,'GEN','#4ad8ff'),(400,260,'渋','#ffd02a')])
b+=skyline(420,'#141420',1374,80,240,'#ff8ad8',60)+''.join(figure(120+k*110,620-k*24,180,'#000') for k in range(6))
I[1374]=svg(b,d)

# 1802 恋する季節: a cherry-pink and summer-blue sky divided diagonally, a couple sharing earphones on a bench
d,b=bg([(0,'#ffc8d8'),(1,'#a8e0ff')])
b+='<polygon points="800,0 800,800 0,800" fill="#a8e0ff"/>'+petals(14,1802,'#ffc2d6',0,400)
b+='<rect x="220" y="560" width="360" height="20" fill="#8a6a4a"/><rect x="240" y="580" width="14" height="80" fill="#8a6a4a"/><rect x="546" y="580" width="14" height="80" fill="#8a6a4a"/>'
b+='<g fill="#2a2a3a"><circle cx="340" cy="450" r="26"/><path d="M314 480 L366 480 L374 560 L306 560Z"/><circle cx="460" cy="450" r="26"/><path d="M434 480 L486 480 L494 560 L426 560Z"/></g><path d="M352 470 Q400 520 448 470" stroke="#fff" stroke-width="4" fill="none"/>'
I[1802]=svg(b,d)

# 1868 星を仰ぐ: a young man lying on a hill looking up at a vast field of stars and a bright one
d,b=bg([(0,'#020214'),(1,'#1a1a48')])
b+=starsf(140,1868,600)+sparkle(500,180,30,'#fff')+glow(500,180,60,'#c8d8ff',.6)+'<path d="M-10 620 Q400 540 810 620 L810 810 L-10 810Z" fill="#0a0a1a"/>'
b+='<g fill="#000"><circle cx="300" cy="580" r="22"/><path d="M320 575 L560 590 L560 608 L320 598Z"/></g>'
I[1868]=svg(b,d)

# 574 C-Girl: a girl's silhouette in a beret riding a scooter along a summer coastal road, 80s idol pastels
d,b=bg([(0,'#ffb0c8'),(1,'#a8e8ff')])
b+=hinomaru_sun(600,200,60,'#fffbe0')+'<rect y="420" width="800" height="120" fill="#5ac8e8"/><rect y="540" width="800" height="260" fill="#a8a8b0"/>'
b+=''.join(ring(x,640,40,'#1a1a1a',10) for x in (300,480))+'<path d="M300 640 L340 560 L460 560 L480 640 M440 560 L460 480" stroke="#ff4a8a" stroke-width="16" fill="none"/><g fill="#2a2a4a"><circle cx="380" cy="420" r="22"/><path d="M360 444 L400 444 L420 540 L350 540Z"/></g><ellipse cx="380" cy="404" rx="30" ry="10" fill="#e8302a"/>'
I[574]=svg(b,d)

# 595 Forever Love: a grand piano under a single spotlight with rose petals falling on the keys, deep blue
d,b=bg([(0,'#050a24'),(1,'#141a40')])
b+='<polygon points="400,0 220,700 580,700" fill="#c8d8ff" opacity=".15"/>'+petals(20,595,'#e8304a',100,700,8,14)
b+='<path d="M200 520 Q200 380 360 380 L600 380 Q640 380 640 440 L640 520Z" fill="#0a0a0a"/><path d="M220 520 L640 520 L640 560 L220 560Z" fill="#1a1a1a"/>'+''.join(f'<rect x="{230+k*20}" y="524" width="16" height="30" fill="#fff"/>' for k in range(20))+'<path d="M240 560 L240 700 M620 560 L620 700" stroke="#0a0a0a" stroke-width="12"/>'
I[595]=svg(b,d)

# 671 野性のENERGY: a wild wolf's silhouette howling on a rock in front of an electric orange lightning sky
d,b=bg([(0,'#3a1a0a'),(1,'#e8601a')])
b+=bolt([(120,40),(180,180),(140,200),(220,360)],'#ffe86a',8)+bolt([(700,60),(640,200),(690,220),(620,360)],'#ffe86a',8)
b+='<path d="M200 800 L260 560 L560 540 L640 800Z" fill="#1a0a04"/><g fill="#000"><path d="M300 560 Q290 470 340 430 L380 330 L392 300 L430 250 L452 262 L420 312 L436 320 L414 340 Q440 420 470 470 Q540 480 560 560Z"/><path d="M392 300 L384 268 L404 290Z"/><path d="M540 540 Q620 520 620 470 Q600 510 540 510Z"/></g>'
I[671]=svg(b,d)

# 1167 It's all too much: a girl's silhouette with an electric guitar surrounded by a whirlwind of paper and notes
d,b=bg([(0,'#3a3a5a'),(1,'#8a8aa8')])
r=random.Random(1167)
b+=''.join(f'<rect x="{400+260*math.cos(a)-20:.0f}" y="{420+200*math.sin(a)-14:.0f}" width="40" height="28" fill="#f4f0e8" transform="rotate({r.randint(0,180)} {400+260*math.cos(a):.0f} {420+200*math.sin(a):.0f})"/>' for a in [k*.4 for k in range(16)])
b+=''.join(note(400+300*math.cos(a),420+230*math.sin(a),28,'#fff') for a in [k*.9+.3 for k in range(6)])+figure(400,720,380,'#0a0a14',pose='hold')+guitar(400,560,.9,-25,'#e8302a')
I[1167]=svg(b,d)

# 1432 starting over: a figure stepping off a broken bridge onto a newly lit path of stones across water
d,b=bg([(0,'#1a2a4a'),(.6,'#5a6a8a'),(1,'#e8b88a')])
b+=hinomaru_sun(640,520,60,'#fff2c8',.8)+'<rect y="540" width="800" height="260" fill="#2a3a5a"/>'
b+='<path d="M-10 520 L240 520 L260 560 L-10 560Z" fill="#3a2a2a"/>'+''.join(f'<ellipse cx="{300+k*90}" cy="{580+k*14}" rx="40" ry="14" fill="#ffe8a0" opacity="{.5+k*.08:.2f}"/>' for k in range(5))+figure(250,520,200,'#000',pose='reach')
I[1432]=svg(b,d)

# 1674 女のみち: a woman in kimono walking alone along a dim alley of bars and red lanterns, early-70s enka mood
d,b=bg([(0,'#1a0a14'),(1,'#3a1a24')])
b+=chochin(160,220,.9,'#d8342c','#ffb070')+chochin(640,260,.8,'#d8342c','#ffb070')+'<path d="M300 300 L500 300 L800 800 L0 800Z" fill="#2a1a20"/>'
b+='<g fill="#0a0408"><circle cx="400" cy="440" r="22"/><path d="M370 470 Q400 460 430 470 L440 640 L360 640Z"/><ellipse cx="400" cy="412" rx="28" ry="16"/></g><rect x="370" y="520" width="60" height="16" fill="#8a1a3a"/>'
I[1674]=svg(b,d)

# 1731 ガチ夢中!: a boy with lightsticks cheering wildly, hearts and stars bursting from a stage screen
d,b=bg([(0,'#1a0a3a'),(1,'#4a1a6a')])
b+='<rect x="140" y="80" width="520" height="280" rx="20" fill="#2a2a4a" stroke="#ff4fa0" stroke-width="8"/>'+''.join(heart(x,y,s,'#ff4fa0') for x,y,s in [(260,200,40),(400,160,50),(540,220,36)])+''.join(star5(x,y,20,'#ffe86a') for x,y in [(320,300),(480,300)])
b+=figure(400,780,360,'#000',pose='up')+'<path d="M330 420 L300 330 M470 420 L500 330" stroke="#4ad8ff" stroke-width="14" stroke-linecap="round"/>'+glow(300,330,40,'#4ad8ff',.7)+glow(500,330,40,'#4ad8ff',.7)
I[1731]=svg(b,d)

# 1790 青嵐: a fresh green wind sweeping up young leaves and blue streaks over a hilltop, early summer
d,b=bg([(0,'#3a9af0'),(1,'#c8f0e8')])
b+=''.join(f'<path d="M{-100+k*80} {600-k*60} Q{200+k*80} {500-k*80} {500+k*60} {300-k*40}" stroke="#e8fbff" stroke-width="10" fill="none" opacity=".6" stroke-linecap="round"/>' for k in range(5))
b+='<path d="M-10 620 Q400 540 810 620 L810 810 L-10 810Z" fill="#4aa84a"/>'+''.join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="8" fill="#5ad85a" transform="rotate({x%90} {x} {y})"/>' for x,y in [(220,420),(340,300),(480,220),(600,340),(380,460),(660,180)])
I[1790]=svg(b,d)

# 1854 Lovers: two coffee mugs leaning together on a window ledge, their steam curling into one heart
d,b=bg([(0,'#d8e8f8'),(1,'#f8f0e8')])
b+='<rect y="540" width="800" height="260" fill="#c8a080"/>'
b+='<path d="M260 540 L270 400 L380 400 L390 540Z" fill="#ff8ab8" transform="rotate(8 320 470)"/><path d="M420 540 L430 400 L540 400 L550 540Z" fill="#6ab8ff" transform="rotate(-8 480 470)"/>'
b+='<path d="M330 390 Q300 320 350 280 Q400 250 400 300 Q400 250 450 280 Q500 320 470 390" stroke="#fff" stroke-width="8" fill="none" opacity=".8"/>'
I[1854]=svg(b,d)

# 1862 Myra: a lighthouse-like star (Mira) pulsing in a night sky over a small figure on a pier, slow rings of light
d,b=bg([(0,'#050a24'),(1,'#1a2448')])
b+=starsf(60,1862,600)+''.join(ring(560,200,30+k*30,'#ffb8a0',3,.6-k*.12) for k in range(5))+glow(560,200,40,'#ffb8a0',.8)+'<circle cx="560" cy="200" r="12" fill="#fff"/>'
b+='<rect y="600" width="800" height="200" fill="#0a1430"/><rect x="-10" y="580" width="360" height="20" fill="#2a2a34"/>'+figure(260,580,180,'#000')
I[1862]=svg(b,d)

# 1864 けっかおーらい: a messy path of scribbled detours that still ends at a smiling sun, cheerful flat colours
d,b=bg([(0,'#fff4c8'),(1,'#ffe0a0')])
b+='<path d="M80 720 Q160 560 260 640 Q380 740 360 560 Q340 400 200 460 Q100 500 200 360 Q300 240 420 320 Q540 400 580 260" stroke="#3a3a5a" stroke-width="10" fill="none" stroke-dasharray="20 14" stroke-linecap="round"/>'
b+=hinomaru_sun(620,200,80,'#ffb02a')+'<circle cx="596" cy="190" r="8" fill="#5a3a1a"/><circle cx="644" cy="190" r="8" fill="#5a3a1a"/><path d="M590 220 Q620 250 650 220" stroke="#5a3a1a" stroke-width="7" fill="none"/>'+'<circle cx="80" cy="720" r="16" fill="#e8302a"/>'
I[1864]=svg(b,d)

# 77 夜明けのスキャット: a dawn sky over a quiet lake with soft wordless notes floating up like birds, late-60s soft palette
d,b=bg([(0,'#5a5a8a'),(.6,'#e8b8b8'),(1,'#f8e0c8')])
b+='<rect y="480" width="800" height="320" fill="#8a8ab0"/><ellipse cx="400" cy="490" rx="160" ry="12" fill="#ffe8c8" opacity=".6"/>'+hills(480,40,'#4a4a6a',77)
b+=''.join(note(x,y,34,'#fff',k%2==0) for k,(x,y) in enumerate([(220,380),(320,300),(430,240),(540,180),(640,120)]))
I[77]=svg(b,d)

# 479 B-Blue: a blue electric guitar against a cracked blue wall, a single beam of white light
d,b=bg([(0,'#0a1a4a'),(1,'#1a3a8a')])
b+=bolt([(100,0),(160,200),(120,340),(200,560)],'#0a1030',8)+bolt([(700,100),(640,300),(700,420),(660,800)],'#0a1030',8)+'<polygon points="400,0 340,800 460,800" fill="#fff" opacity=".12"/>'
b+=guitar(400,440,1.6,-30,'#2a8af8')
I[479]=svg(b,d)

# 909 愛なんだ: a group of six silhouettes jumping on a summer beach with a giant heart-shaped sun
d,b=bg([(0,'#ff8a8a'),(1,'#ffe0a0')])
b+=heart(400,320,150,'#ffd02a')+'<rect y="460" width="800" height="100" fill="#4ac8e8"/><path d="M-10 560 L810 540 L810 810 L-10 810Z" fill="#f8e0a8"/>'
b+=''.join(figure(x,y,190,'#3a1a1a',pose='up') for x,y in [(140,700),(250,660),(360,690),(470,650),(580,690),(690,660)])
I[909]=svg(b,d)

# 910 Feel your breeze: a dandelion releasing its seeds into a light breeze over a green field and blue sky
d,b=bg([(0,'#5ab8ff'),(1,'#e0f6ff')])
b+='<path d="M-10 620 Q400 560 810 620 L810 810 L-10 810Z" fill="#6ac84a"/><path d="M260 640 Q250 520 280 400" stroke="#4a8a3a" stroke-width="6" fill="none"/>'
b+=''.join(f'<path d="M280 400 L{280+60*math.cos(a):.0f} {400+60*math.sin(a):.0f}" stroke="#fff" stroke-width="2"/><circle cx="{280+60*math.cos(a):.0f}" cy="{400+60*math.sin(a):.0f}" r="5" fill="#fff"/>' for a in [k*.4 for k in range(16)])
b+=''.join(f'<path d="M{x} {y} L{x+14} {y-14}" stroke="#fff" stroke-width="2"/><circle cx="{x+14}" cy="{y-14}" r="6" fill="#fff"/>' for x,y in [(400,320),(480,260),(560,220),(640,170),(520,330),(700,260)])
I[910]=svg(b,d)

# 1054 It Takes Two: two hands each holding one end of a shared umbrella in light rain, warm street lights
d,b=bg([(0,'#2a2a4a'),(1,'#5a5a7a')])
b+=rain(70,1054,'#c8d8ff',.35)+'<rect y="640" width="800" height="160" fill="#2a2a3a"/>'+''.join(f'<circle cx="{x}" cy="200" r="16" fill="#ffd27a"/>'+glow(x,200,40,'#ffd27a',.5) for x in (120,680))
b+='<path d="M220 400 Q400 220 580 400Z" fill="#e8d8b8"/><path d="M400 400 L400 560" stroke="#3a3a3a" stroke-width="6"/>'+figure(340,660,280,'#000')+figure(460,660,290,'#000')
I[1054]=svg(b,d)

# 1112 FIREWORKS: a big multi-colour firework display over a harbour city, reflections in the water
d,b=bg([(0,'#050514'),(1,'#141430')])
b+=firework(220,220,120,'#ff4a6a',seed=1)+firework(560,180,150,'#ffd02a',seed=2)+firework(400,340,90,'#4ad8ff',seed=3)
b+=skyline(560,'#0a0a1a',1112,40,180,'#ffd27a',60)+'<rect y="560" width="800" height="240" fill="#0a0e24"/>'+''.join(f'<rect x="{x-20}" y="{580+k*16}" width="40" height="4" fill="{c}" opacity="{.5-k*.08:.2f}"/>' for x,c in [(220,'#ff4a6a'),(560,'#ffd02a'),(400,'#4ad8ff')] for k in range(5))
I[1112]=svg(b,d)

# 1138 Good Luck: a four-leaf clover held up to a bright sky between two fingers, a small plane flying away
d,b=bg([(0,'#3aa8f8'),(1,'#d8f2ff')])
b+=cloud(560,200,1.4)+'<path d="M600 140 L660 130 L640 146Z M620 138 L630 120 L640 136Z" fill="#fff"/>'
b+='<path d="M400 480 L400 640" stroke="#3a8a3a" stroke-width="8"/>'+''.join(f'<g transform="rotate({a} 400 420)"><path d="M400 420 Q340 360 370 320 Q400 300 400 340 Q400 300 430 320 Q460 360 400 420Z" fill="#3ac84a"/></g>' for a in (0,90,180,270))
b+='<g fill="#f0c8b0" stroke="#c8a088" stroke-width="5"><path d="M330 800 L350 640 Q360 600 390 610 L400 660 L380 800Z"/><path d="M470 800 L450 640 Q440 600 410 610 L400 660 L420 800Z"/></g>'
I[1138]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
