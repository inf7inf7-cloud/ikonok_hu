import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 26. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 1154 STAY: a single lit window in a winter apartment block, two cups on the sill, snow falling
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=''.join(f'<circle cx="{(k*131)%800}" cy="{(k*71)%800}" r="{2+k%3}" fill="#fff" opacity=".7"/>' for k in range(50))+'<rect x="160" y="160" width="480" height="640" fill="#2a3040"/>'
b+=''.join(f'<rect x="{200+c*140}" y="{200+r2*140}" width="100" height="100" fill="#1a2030"/>' for c in range(3) for r2 in range(4))+'<rect x="340" y="340" width="100" height="100" fill="#ffd27a"/>'+glow(390,390,120,'#ffd27a',.4)
b+='<rect x="356" y="414" width="22" height="24" fill="#fff"/><rect x="398" y="414" width="22" height="24" fill="#fff"/>'
I[1154]=svg(b,d)

# 399 赤い鳥逃げた: a red bird escaping from an open birdcage into a dark night
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+='<path d="M220 280 Q220 160 330 160 Q440 160 440 280 L440 600 L220 600Z" fill="none" stroke="#c8a85a" stroke-width="6"/>'+''.join(f'<path d="M{x} {200 if x in (280,380) else 240} L{x} 600" stroke="#c8a85a" stroke-width="4"/>' for x in range(250,440,30))+'<rect x="200" y="600" width="260" height="24" fill="#c8a85a"/>'
b+='<path d="M440 360 L540 300" stroke="#c8a85a" stroke-width="5"/><g transform="translate(600 240)" fill="#e8102a"><ellipse cx="0" cy="0" rx="50" ry="26"/><path d="M-10 -10 Q-40 -100 -100 -90 Q-50 -40 -20 0Z M10 -10 Q60 -100 120 -80 Q60 -40 20 0Z"/><circle cx="46" cy="-10" r="16"/><path d="M60 -10 L80 -4 L60 0Z" fill="#ffb02a"/></g>'
I[399]=svg(b,d)

# 752 花 -Mémento-Mori-: a single flower blooming out of a cracked asphalt road under a grey sky
d,b=bg([(0,'#8a8a94'),(1,'#c8c8cc')])
b+='<rect y="500" width="800" height="300" fill="#4a4a50"/>'+bolt([(260,800),(320,680),(380,640),(400,560)],'#2a2a30',6)
b+='<path d="M400 560 Q390 460 400 360" stroke="#4a8a3a" stroke-width="8" fill="none"/><ellipse cx="370" cy="460" rx="30" ry="12" fill="#4a8a3a" transform="rotate(-30 370 460)"/>'+flower(400,330,60,8,'#e8304a','#ffd02a')
I[752]=svg(b,d)

# 1057 Secret of my heart: a small locked heart-shaped box with a key on a velvet-blue table, soft spotlight
d,b=bg([(0,'#0a1a3a'),(1,'#2a3a6a')])
b+=glow(400,420,240,'#c8d8ff',.25)+'<rect y="560" width="800" height="240" fill="#1a2a5a"/>'+heart(400,440,120,'#c8a85a')+heart(400,440,100,'#e8c870')
b+='<rect x="380" y="420" width="40" height="36" rx="4" fill="#5a4a2a"/><path d="M388 420 Q388 396 400 396 Q412 396 412 420" stroke="#5a4a2a" stroke-width="6" fill="none"/>'
b+='<g transform="rotate(-20 580 620)"><circle cx="540" cy="620" r="18" fill="none" stroke="#c8a85a" stroke-width="7"/><path d="M558 620 L640 620 L640 636 M620 620 L620 636" stroke="#c8a85a" stroke-width="7" fill="none"/></g>'
I[1057]=svg(b,d)

# 1063 ボーイフレンド: a girl's silhouette leaping off a beach float into the sea, a boy waving from the shore, bright summer
d,b=bg([(0,'#3ab8ff'),(1,'#c8f0ff')])
b+=hinomaru_sun(640,140,50,'#fffbe0')+'<rect y="400" width="800" height="280" fill="#2aa8d8"/><rect y="680" width="800" height="120" fill="#f8e0a8"/>'
b+='<ellipse cx="300" cy="500" rx="80" ry="16" fill="#ff6a8a"/><g transform="rotate(-25 360 380)">'+figure(360,440,150,'#0a2a4a',pose='up')+'</g>'+figure(620,760,170,'#3a2a1a',pose='wave')
I[1063]=svg(b,d)

# 1244 Love yourself: a figure facing a mirror where the reflection holds a heart out, warm vs cold halves
d,b=bg([(0,'#2a3a5a'),(1,'#4a5a7a')])
b+='<rect x="400" y="0" width="400" height="800" fill="#7a3a4a"/>'+'<rect x="420" y="140" width="300" height="520" rx="150" fill="#f4d8c8" opacity=".3" stroke="#e8c8a8" stroke-width="10"/>'
b+=figure(260,700,400,'#0a0a14')+figure(570,640,340,'#3a1a24')+heart(570,440,40,'#ff4a6a')
I[1244]=svg(b,d)

# 1376 Nobody's fault: a crowd of identical figures with one standing apart facing forward, a crumbling red bar across
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+=''.join(figure(80+k*70,420,140,'#4a4a4a') for k in range(10))+'<path d="M0 470 L800 430 L800 470 L0 510Z" fill="#c8102a"/>'+figure(400,760,320,'#000')
I[1376]=svg(b,d)

# 1383 こんなに好きになっちゃっていいの?: a girl's silhouette holding a love letter to her chest, hearts floating up, sky blue
d,b=bg([(0,'#7ac8ff'),(1,'#e8f6ff')])
b+=''.join(heart(x,y,s,'#ff8ab8') for x,y,s in [(180,200,30),(600,160,40),(520,300,24),(260,340,20),(660,380,28)])+figure(400,780,440,'#2a3a6a')+'<rect x="370" y="460" width="60" height="44" fill="#fff"/>'+heart(400,482,10,'#e8304a')
I[1383]=svg(b,d)

# 1859 プロポーズ: a ring box opened on a palm under evening city lights
d,b=bg([(0,'#1a1a3a'),(1,'#5a3a6a')])
b+=''.join(glow(x,y,30,c,.6) for x,y,c in [(120,180,'#ffd27a'),(260,120,'#ff8ad8'),(600,160,'#ffd27a'),(700,260,'#8ad8ff'),(480,90,'#ffd27a')])
b+='<rect y="560" width="800" height="240" fill="#e8e0d8"/><rect x="180" y="420" width="16" height="140" fill="#f4ead8"/><path d="M188 380 Q176 400 188 418 Q200 400 188 380Z" fill="#ffb02a"/>'+glow(188,400,60,'#ffb02a',.5)
b+='<rect x="320" y="520" width="160" height="70" fill="#5a1a2a"/><path d="M320 520 L340 420 L460 420 L480 520Z" fill="#7a2a3a"/><rect x="360" y="470" width="80" height="50" fill="#3a0a1a"/>'+ring(400,480,22,'#e8e8f0',8)+sparkle(414,452,18,'#fff')
I[1859]=svg(b,d)

# 1873 NAO: an Okinawan beach at dusk with a wooden sanshin leaning on a boat and a single figure walking away
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=hinomaru_sun(400,380,90,'#fff2c8',.8)+'<rect y="420" width="800" height="200" fill="#3aa8c0"/><rect y="620" width="800" height="180" fill="#f4e0b8"/>'
b+='<path d="M120 640 L380 640 L340 690 L160 690Z" fill="#5a3a2a"/>'+figure(600,680,160,'#2a1a1a')+'<rect x="300" y="520" width="10" height="130" fill="#3a2a1a" transform="rotate(15 305 590)"/><ellipse cx="330" cy="660" rx="22" ry="26" fill="#2a2a2a"/>'
I[1873]=svg(b,d)

# 191 少年時代: a boy's silhouette with a straw hat and insect net on a summer country path, cicada sky
d,b=bg([(0,'#5ab8ff'),(1,'#f0f8e0')])
b+=cloud(200,160,1.6)+cloud(620,220,1.2)+'<rect y="520" width="800" height="280" fill="#7ab84a"/><path d="M360 520 L440 520 L560 800 L240 800Z" fill="#d8c8a0"/>'
b+=figure(420,700,240,'#2a2a1a')+'<ellipse cx="420" cy="482" rx="44" ry="10" fill="#e8c870"/><path d="M450 560 L560 400" stroke="#8a6a4a" stroke-width="6"/><ellipse cx="575" cy="380" rx="30" ry="36" fill="#fff" opacity=".7" stroke="#ddd" stroke-width="3"/>'
I[191]=svg(b,d)

# 290 ネオ・ブラボー!!: a blazing beach party, a fist-pumping crowd and fireworks of confetti
d,b=bg([(0,'#ff4a2a'),(1,'#ffc83a')])
b+=firework(400,200,140,'#fff',seed=290)+'<rect y="560" width="800" height="240" fill="#2a1a0a"/>'
b+=''.join(f'<path d="M{x} 800 L{x} 600" stroke="#000" stroke-width="20"/><circle cx="{x}" cy="580" r="18" fill="#000"/>' for x in range(40,800,60))
I[290]=svg(b,d)

# 454 3年目の浮気: a husband's silhouette sneaking off with lipstick on his collar, a wife's silhouette with arms crossed, comic duet
d,b=bg([(0,'#ffd0d8'),(1,'#fff4e8')])
b+=figure(260,720,360,'#2a2a3a')+figure(540,720,340,'#5a2a4a')+'<path d="M480 440 L600 470" stroke="#5a2a4a" stroke-width="22"/>'
b+='<path d="M272 380 Q285 370 296 380 Q285 392 272 380Z" fill="#e8102a"/>'+txt(380,200,'?!',120,'#e8302a',900)
I[454]=svg(b,d)

# 786 聖域: a ring of tall stone pillars in a misty forest, light falling into the center
d,b=bg([(0,'#3a4a3a'),(1,'#8a9a7a')])
b+='<polygon points="340,0 460,0 560,800 240,800" fill="#fff8d0" opacity=".2"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{800-y}" fill="#2a3a2a"/>' for x,y,w in [(60,200,60),(200,300,50),(560,300,50),(680,200,60)])
b+='<rect y="620" width="800" height="180" fill="#3a4a2a"/>'+figure(400,640,150,'#0a140a')
I[786]=svg(b,d)

# 823 波乗りジョニー: a surfer silhouette riding a big curling blue wave under a blazing sun
d,b=bg([(0,'#ffb02a'),(1,'#fff0a0')])
b+=hinomaru_sun(160,160,70,'#fff6d0')+'<path d="M-10 800 L-10 520 Q200 300 460 320 Q640 340 640 460 Q560 380 480 440 Q420 520 520 600 L810 600 L810 800Z" fill="#1a8ad8"/><path d="M460 320 Q640 340 640 460 Q600 400 520 410" stroke="#fff" stroke-width="10" fill="none"/>'
b+='<ellipse cx="380" cy="560" rx="90" ry="14" fill="#ff4a4a" transform="rotate(-15 380 560)"/><g transform="rotate(-10 380 480)">'+figure(380,550,150,'#0a1a2a',pose='reach')+'</g>'
I[823]=svg(b,d)

# 1142 ワールドアパート: two figures on separate floating islands with the whole globe between them
d,b=bg([(0,'#0a1a3a'),(1,'#3a4a7a')])
b+=starsf(60,1142,800)+'<circle cx="400" cy="420" r="140" fill="#2a6ab8"/><path d="M320 340 Q360 320 380 360 Q360 400 330 390Z M420 440 Q470 420 480 480 Q440 500 420 470Z" fill="#4ab84a"/>'
b+='<path d="M40 560 L200 560 L160 620 L80 620Z M600 260 L760 260 L720 320 L640 320Z" fill="#5a4a3a"/>'+figure(120,560,120,'#000')+figure(680,260,120,'#000')
I[1142]=svg(b,d)

# 1158 ホタルノヒカリ: fireflies drifting over a dark summer river with a small wooden bridge
d,b=bg([(0,'#050a14'),(1,'#142030')])
b+='<rect y="520" width="800" height="280" fill="#0a1a2a"/><path d="M200 520 Q400 420 600 520" stroke="#3a2a1a" stroke-width="16" fill="none"/>'+''.join(f'<path d="M{x} {520-(100-abs(x-400)/2)*.0} L{x} 520" stroke="#3a2a1a" stroke-width="4"/>' for x in ())
b+=''.join(f'<circle cx="{(k*137)%760+20}" cy="{(k*89)%460+120}" r="4" fill="#e8ff7a"/>'+glow((k*137)%760+20,(k*89)%460+120,18,'#d8ff6a',.6) for k in range(26))+hills(520,30,'#0a140a',1158)
I[1158]=svg(b,d)

# 1282 Butterfly: a white butterfly over a wedding veil and a small bouquet in soft morning light
d,b=bg([(0,'#fff0f4'),(1,'#f8f8ff')])
b+='<path d="M200 800 Q260 400 400 320 Q540 400 600 800Z" fill="#fff" stroke="#e8e0e8" stroke-width="4" opacity=".9"/>'+''.join(flower(x,y,30,6,c,'#ffd02a') for x,y,c in [(360,640,'#ffb8c8'),(420,620,'#fff'),(400,670,'#ffd0dc')])
b+='<g transform="translate(560 220)" fill="#c8b8ff"><ellipse cx="-30" cy="-20" rx="36" ry="28"/><ellipse cx="30" cy="-20" rx="36" ry="28"/><ellipse cx="-22" cy="20" rx="22" ry="18"/><ellipse cx="22" cy="20" rx="22" ry="18"/><rect x="-4" y="-34" width="8" height="70" fill="#5a4a6a"/></g>'
I[1282]=svg(b,d)

# 319 LOVELAND,ISLAND: a tropical island with palm trees and a pastel sunset, early 80s city-pop colours
d,b=bg([(0,'#ff6aa8'),(.5,'#ffb88a'),(1,'#6ad8e8')])
b+=hinomaru_sun(400,360,100,'#fff0a0')+''.join(f'<rect x="250" y="{300+k*16}" width="300" height="6" fill="#ff8ab8"/>' for k in range(4))+'<rect y="420" width="800" height="380" fill="#3ab8d8"/>'
b+='<ellipse cx="400" cy="560" rx="220" ry="40" fill="#f8e0a0"/>'+''.join(f'<path d="M{x} 560 Q{x+10} 460 {x+30} 380" stroke="#3a2a1a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x+30} 380 Q{x+30+60*math.cos(a):.0f} {380+40*math.sin(a)-20:.0f} {x+30+100*math.cos(a):.0f} {380+60*math.sin(a):.0f}" stroke="#1a5a2a" stroke-width="12" fill="none"/>' for a in [3.6,4.2,5.2,5.9,.2]) for x in (300,440))
I[319]=svg(b,d)

# 371 瞳はダイアモンド: a single large diamond with a tear-like glint, soft night-blue
d,b=bg([(0,'#1a2a4a'),(1,'#4a5a8a')])
b+=glow(400,400,240,'#c8e0ff',.3)+'<path d="M260 320 L320 240 L480 240 L540 320 L400 560Z" fill="#d8ecff"/><path d="M260 320 L540 320 M320 240 L360 320 L400 240 L440 320 L480 240 M360 320 L400 560 L440 320" stroke="#8ab0d8" stroke-width="4" fill="none"/>'
b+=sparkle(520,240,26,'#fff')+'<path d="M400 600 Q385 630 400 650 Q415 630 400 600Z" fill="#c8e8ff"/>'
I[371]=svg(b,d)

# 841 ホワイトロード: a long white snowy road through a winter field toward faint mountains
d,b=bg([(0,'#a8b8d0'),(1,'#e8eef8')])
b+=hills(440,30,'#c8d0e0',841)+'<rect y="460" width="800" height="340" fill="#f4f6fa"/><path d="M390 460 L410 460 L560 800 L240 800Z" fill="#fff" stroke="#d8dce8" stroke-width="3"/>'
b+=''.join(f'<circle cx="{(k*113)%800}" cy="{(k*67)%460}" r="3" fill="#fff"/>' for k in range(50))+figure(420,560,90,'#3a3a4a')
I[841]=svg(b,d)

# 953 永遠に: two hands sealing a promise with intertwined pinkies before an infinity sign of light
d,b=bg([(0,'#2a1a3a'),(1,'#6a4a7a')])
b+='<path d="M400 300 C320 200 200 200 200 300 C200 400 320 400 400 300 C480 200 600 200 600 300 C600 400 480 400 400 300Z" fill="none" stroke="#ffd8a0" stroke-width="10"/>'+glow(400,300,220,'#ffd8a0',.2)
b+='<g fill="#f0c8b0"><path d="M120 700 Q200 560 360 540 L380 570 Q260 600 180 720Z"/><path d="M680 700 Q600 560 440 540 L420 570 Q540 600 620 720Z"/></g>'+ring(400,555,22,'#f0c8b0',12)
I[953]=svg(b,d)

# 1316 ハロウィン・ナイト: jack-o'-lanterns and a dancing crowd under a big orange moon with bats
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a3a')])
b+='<circle cx="400" cy="260" r="160" fill="#ff8a2a"/>'+''.join(f'<path d="M{x} {y} q15 -18 30 0 q15 -18 30 0 q-15 8 -30 20 q-15 -12 -30 -20Z" fill="#000"/>' for x,y in [(160,140),(580,120),(640,300)])
b+=''.join(figure(x,780,200,'#000',pose=p) for x,p in [(120,'up'),(260,'wave'),(540,'up'),(680,'wave')])
b+='<ellipse cx="400" cy="700" rx="70" ry="56" fill="#ff7a1a"/><path d="M370 690 L385 670 L400 690Z M400 690 L415 670 L430 690Z M370 720 Q400 740 430 720" fill="#ffe86a" stroke="#ffe86a" stroke-width="3"/><rect x="394" y="636" width="12" height="18" fill="#3a5a2a"/>'
I[1316]=svg(b,d)

# 1401 SOS: an S.O.S. signal flashing from a lighthouse on a dark rocky coast
d,b=bg([(0,'#0a1424'),(1,'#1a2a44')])
b+='<polygon points="440,240 800,160 800,320" fill="#fff8c8" opacity=".25"/><rect y="560" width="800" height="240" fill="#14243a"/><path d="M280 560 L340 560 L330 600 L290 600Z M240 800 L300 560 L400 560 L460 800Z" fill="#0a0a14"/>'
b+='<path d="M380 560 L400 260 L470 260 L490 560Z" fill="#e8e8f0"/><rect x="390" y="230" width="90" height="40" fill="#ffe87a"/>'+glow(435,250,80,'#ffe87a',.5)
b+=''.join(f'<circle cx="{560+k*30}" cy="240" r="9" fill="#fff"/>' for k in range(3))+''.join(f'<rect x="{560+k*40-18}" y="282" width="34" height="12" fill="#fff"/>' for k in range(3))+''.join(f'<circle cx="{560+k*30}" cy="330" r="9" fill="#fff"/>' for k in range(3))
I[1401]=svg(b,d)

# 1593 サクラキミワタシ: two silhouettes under a cherry tree, a pink petal storm between them
d,b=bg([(0,'#ffd0e0'),(1,'#fff6f8')])
b+='<rect x="580" y="300" width="36" height="400" fill="#5a3a2a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffb8d0"/>' for x,y,r in [(600,220,140),(460,260,100),(720,280,90)])
b+='<rect y="680" width="800" height="120" fill="#c8e0a8"/>'+petals(30,1593,'#ff9ab8',100,700)+figure(220,720,240,'#3a2a3a')+figure(380,720,250,'#3a2a3a')
I[1593]=svg(b,d)

# 1639 Tiger: a tiger-stripe pattern of orange and black slashes behind a dancer silhouette in a power pose
d,b=bg([(0,'#ff8a1a'),(1,'#ffb84a')])
b+=''.join(f'<path d="M{x} -10 Q{x+40} 200 {x-20} 400 Q{x+30} 600 {x} 810" stroke="#000" stroke-width="{24+k%3*10}" fill="none"/>' for k,x in enumerate(range(60,800,140)))
b+='<circle cx="400" cy="420" r="230" fill="#ffb84a"/>'+figure(400,640,380,'#000',pose='reachL')
I[1639]=svg(b,d)

# 1852 ブルーベリー・ナイツ: blueberries spilled on a table in a dim bar, a glass and blue neon
d,b=bg([(0,'#0a0a2a'),(1,'#1a1a4a')])
b+=neon(400,200,'Blueberry','#6a8aff',60)+'<rect y="520" width="800" height="280" fill="#2a1a1a"/><path d="M500 520 L490 400 L570 400 L560 520Z" fill="#c8d8ff" opacity=".4"/>'
b+=''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#3a3a8a"/><circle cx="{x-6}" cy="{y-6}" r="6" fill="#6a6ab8"/>' for x,y in [(220,560),(260,590),(300,570),(240,630),(340,610),(190,600)])
I[1852]=svg(b,d)

# 1853 恋人ごっこ: two paper cut-out figures holding hands on a cardboard stage set, toy-like
d,b=bg([(0,'#f8e8d0'),(1,'#e8d0b0')])
b+='<rect x="80" y="140" width="640" height="460" fill="#c8a07a"/><rect x="80" y="140" width="640" height="40" fill="#e8304a"/><path d="M80 180 Q140 260 200 180 M600 180 Q660 260 720 180" stroke="#e8304a" stroke-width="20" fill="none"/>'
b+='<rect y="600" width="800" height="200" fill="#8a6a4a"/>'+figure(340,600,240,'#fff')+figure(460,600,240,'#fff')+'<path d="M370 470 L430 470" stroke="#fff" stroke-width="10"/>'+heart(400,260,26,'#ff6a8a')
I[1853]=svg(b,d)

# 158 矢切の渡し: a small ferry boat with a boatman's pole crossing a quiet river at dusk, reeds on the bank
d,b=bg([(0,'#c89a8a'),(1,'#f0d8c0')])
b+=hinomaru_sun(560,340,50,'#fff0d0',.7)+'<rect y="380" width="800" height="420" fill="#7a8aa0"/>'+''.join(f'<path d="M{x} 800 L{x+10} {560+(x*7)%60}" stroke="#4a4a2a" stroke-width="4"/>' for x in range(0,200,14))
b+='<path d="M260 560 L560 560 L520 600 L300 600Z" fill="#3a2a1a"/>'+figure(480,560,180,'#1a1010')+'<path d="M500 440 L560 680" stroke="#3a2a1a" stroke-width="6"/>'+'<g fill="#1a1010"><circle cx="340" cy="510" r="18"/><path d="M320 528 L360 528 L366 560 L314 560Z"/><circle cx="390" cy="510" r="18"/><path d="M370 528 L410 528 L416 560 L364 560Z"/></g>'
I[158]=svg(b,d)

# 753 【es】～Theme of es～: a lone figure's silhouette on a stage under one spotlight, dark ocean-blue haze
d,b=bg([(0,'#050a1a'),(1,'#1a2a4a')])
b+='<polygon points="400,0 280,720 520,720" fill="#c8d8ff" opacity=".18"/><ellipse cx="400" cy="720" rx="140" ry="20" fill="#c8d8ff" opacity=".3"/>'+figure(400,720,300,'#000')+txt(120,140,'es',60,'#8aa8d8',300,op=.6)
I[753]=svg(b,d)

# 954 約束: two fingers hooked in a pinky promise against a sunset sky
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=hinomaru_sun(400,560,140,'#fff2c8',.7)
b+='<rect y="600" width="800" height="200" fill="#8a6a5a"/>'+figure(330,620,280,'#2a1a1a')+figure(470,620,270,'#2a1a1a')+'<path d="M362 470 Q400 500 438 470" stroke="#2a1a1a" stroke-width="12" fill="none"/>'+heart(400,380,24,'#ff6a6a')
I[954]=svg(b,d)

# 1292 if: a girl at a crossroads looking at two doors, one pink and one blue, under a pale sky
d,b=bg([(0,'#d8e0f0'),(1,'#f8f4f0')])
b+='<rect y="600" width="800" height="200" fill="#c8c0b8"/><rect x="160" y="260" width="160" height="340" fill="#ff9ab8"/><rect x="480" y="260" width="160" height="340" fill="#7ab0ff"/>'+'<circle cx="300" cy="440" r="8" fill="#fff"/><circle cx="500" cy="440" r="8" fill="#fff"/>'+figure(400,760,260,'#2a2a3a')
I[1292]=svg(b,d)

# 1317 LOVE TRIP: a vintage open-top car driving a coastal road with a heart balloon trailing
d,b=bg([(0,'#5ac8ff'),(1,'#e0f8ff')])
b+=cloud(160,160,1.3)+'<rect y="440" width="800" height="140" fill="#2aa8d8"/><rect y="580" width="800" height="220" fill="#a8a8a8"/>'
b+='<path d="M220 640 L260 580 L420 570 L480 600 L560 610 L560 660 L220 660Z" fill="#ff4a6a"/>'+ring(290,670,30,'#1a1a1a',14)+ring(500,670,30,'#1a1a1a',14)+'<g fill="#1a1a1a"><circle cx="340" cy="540" r="16"/><circle cx="400" cy="540" r="16"/></g>'
b+='<path d="M400 540 Q500 420 620 300" stroke="#555" stroke-width="2" fill="none"/>'+heart(640,280,44,'#ff4a8a')
I[1317]=svg(b,d)

# 1694 「いちご白書」をもう一度: a 70s movie theatre facade with a red strawberry on the marquee, a couple's silhouettes
d,b=bg([(0,'#2a1a1a'),(1,'#5a3a2a')])
b+='<rect x="120" y="120" width="560" height="200" fill="#e8d8b8"/><path d="M400 150 Q350 170 360 230 Q380 290 400 300 Q420 290 440 230 Q450 170 400 150Z" fill="#e8102a"/><path d="M380 150 L400 130 L420 150Z" fill="#3a8a3a"/>'
b+=''.join(f'<circle cx="{x}" cy="120" r="7" fill="#ffd27a"/><circle cx="{x}" cy="320" r="7" fill="#ffd27a"/>' for x in range(140,680,40))+'<rect y="560" width="800" height="240" fill="#3a2a2a"/>'+figure(340,640,260,'#000')+figure(450,640,250,'#000')
I[1694]=svg(b,d)

# 1756 赤い糸: a red thread winding across a pale sky linking two small figures on distant hills
d,b=bg([(0,'#e8eef8'),(1,'#fff4f0')])
b+='<path d="M-10 680 Q120 600 240 660 Q400 740 560 660 Q680 600 810 680 L810 810 L-10 810Z" fill="#b8d8a8"/>'+figure(160,640,140,'#3a3a4a')+figure(640,640,140,'#3a3a4a')
b+='<path d="M175 560 Q260 200 400 360 Q520 500 620 200 Q660 120 625 560" stroke="#e8102a" stroke-width="6" fill="none"/>'
I[1756]=svg(b,d)

# 55 花の首飾り: a necklace of small wildflowers floating on a lake under a pale sky, late-60s soft palette
d,b=bg([(0,'#c8d8e8'),(1,'#f0f4f0')])
b+='<rect y="420" width="800" height="380" fill="#7a9ab0"/>'+hills(420,30,'#7a9a7a',55,op=.7)
b+=''.join(flower(400+200*math.cos(a),600+90*math.sin(a),20,6,c,'#ffd02a') for a,c in zip([k*.5 for k in range(13)],['#fff','#ffb8c8','#fff8a8']*5))
I[55]=svg(b,d)

# 234 ファイト!: a fist raised high against a rough grey sky with a lone small figure, wind lines
d,b=bg([(0,'#4a4a5a'),(1,'#9a9aa8')])
b+=''.join(f'<path d="M-10 {y} Q400 {y-40} 810 {y}" stroke="#c8c8d8" stroke-width="4" fill="none" opacity=".4"/>' for y in (160,260,360))
b+='<rect y="640" width="800" height="160" fill="#2a2a34"/>'+figure(400,660,320,'#000',pose='up')
I[234]=svg(b,d)

# 312 ひとつ: a single candle flame lighting up a dark field, many small lights joining it
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=''.join(f'<circle cx="{(k*97)%760+20}" cy="{560+(k*37)%200}" r="4" fill="#ffd27a"/>'+glow((k*97)%760+20,560+(k*37)%200,14,'#ffd27a',.5) for k in range(30))
b+='<rect x="370" y="360" width="60" height="200" fill="#f4ead8"/><path d="M400 260 Q380 310 400 340 Q420 310 400 260Z" fill="#ffd02a"/>'+glow(400,310,140,'#ffb02a',.5)
I[312]=svg(b,d)

# 372 時間の国のアリス: a girl's silhouette falling past floating clocks and a rabbit's pocket watch, pastel dream
d,b=bg([(0,'#c8b8ff'),(1,'#ffd8f0')])
for x,y,r2 in [(160,180,60),(620,220,80),(560,600,50),(180,560,44)]:
    b+=f'<circle cx="{x}" cy="{y}" r="{r2}" fill="#fff" stroke="#c8a85a" stroke-width="6"/><path d="M{x} {y} L{x} {y-r2*.7} M{x} {y} L{x+r2*.5} {y+r2*.2}" stroke="#3a3a3a" stroke-width="4"/>'
b+='<g transform="rotate(30 400 400)">'+figure(400,560,300,'#4a2a6a',pose='up')+'</g>'
I[372]=svg(b,d)

# 473 フレンズ: two friends' silhouettes walking away at dusk on a city overpass, one bag swinging, 80s rock
d,b=bg([(0,'#5a3a6a'),(1,'#ff9a7a')])
b+=skyline(480,'#2a1a3a',473,60,240,'#ffd27a',40)+'<rect y="560" width="800" height="30" fill="#3a2a3a"/>'+''.join(f'<rect x="{x}" y="500" width="8" height="60" fill="#3a2a3a"/>' for x in range(0,800,40))+'<rect y="496" width="800" height="8" fill="#3a2a3a"/>'
b+=figure(340,560,220,'#000')+figure(450,560,210,'#000')
I[473]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
