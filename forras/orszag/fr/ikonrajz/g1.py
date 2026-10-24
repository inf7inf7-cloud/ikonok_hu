import sys,math;sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']
from hl import *;from fr import *
# Francia IKONOK: 1. csoport (Top 1–20), 2026-10-24
I={}
F='font-family="DejaVu Sans,Arial" font-weight="700"'

# 1 Pour que tu m'aimes encore: a woman alone in a golden spotlight offers a glowing heart with both hands, ready to give everything
d,b=bg([(0,'#1a0a1a'),(.6,'#3a1020'),(1,'#6a2018')])
b+='<polygon points="400,-20 230,800 570,800" fill="#ffd8a0" opacity=".16"/>'+glow(400,700,220,'#ffb060',.25)
b+='<ellipse cx="400" cy="720" rx="200" ry="26" fill="#ffd8a0" opacity=".25"/>'
b+=figure(400,720,330,'#0a0408',pose='hold',hair='#0a0408')
b+='<path d="M372 482 Q400 640 430 482Z" fill="#0a0408"/>'
d+=rg('h1',S((0,'#fff0d0'),(.5,'#ff6a5a'),(1,'#a8102a')),.4,.35,.7)
b+=glow(400,430,90,'#ff7a5a',.6)+heart(400,420,62,'url(#h1)')
for x,y,s in [(300,330,14),(500,300,10),(470,220,8)]: b+=sparkle(x,y,s,'#ffe0b0')
I[1]=svg(b,d)

# 2 Alors on danse: a man in shirt and bow tie dancing wildly alone under club lights, the night swallowing his worries
d,b=bg([(0,'#0a0420'),(.6,'#1a0a3a'),(1,'#300a2a')])
b+=stage_lights(4,40,['#ff2a8a','#2ad0ff','#ffd23f','#9a5aff'],.16)
b+='<rect y="690" width="800" height="110" fill="#0a0612"/>'
for i in range(8):
    for j in range(2): b+=f'<rect x="{i*100}" y="{690+j*55}" width="100" height="55" fill="{["#3a1a5a","#5a1a4a","#1a3a5a"][(i+j)%3]}" opacity=".55"/>'
b+=f'<g transform="rotate(-8 400 690)">{figure(400,690,360,"#06030c",pose="up")}</g>'
b+='<path d="M376 384 L396 396 L376 408Z M420 384 L400 396 L420 408Z" fill="#ff2a8a"/>'
b+=note(170,240,30,'#2ad0ff')+note(600,190,26,'#ff7ac0',True)
I[2]=svg(b,d)

# 3 Papaoutai: a little boy tugs at the hand of a frozen white mannequin father who never answers
d,b=bg([(0,'#d8e8f0'),(.6,'#a8c8d8'),(1,'#6a8aa0')])
b+='<rect y="640" width="800" height="160" fill="#4a6070"/>'
b+=figure(480,660,420,'#f4f4f6',pose='stand')
b+='<ellipse cx="480" cy="388" rx="26" ry="30" fill="#e8e8ec"/><circle cx="470" cy="384" r="3" fill="#bbb"/><circle cx="490" cy="384" r="3" fill="#bbb"/>'
b+=figure(300,660,200,'#1a2a3a',pose='reach')
b+='<path d="M406 504 Q432 520 440 540" stroke="#1a2a3a" stroke-width="10" fill="none" stroke-linecap="round"/>'
b+=f'<text x="250" y="330" text-anchor="middle" {F} font-size="110" fill="#1a2a3a" opacity=".8">?</text>'
I[3]=svg(b,d)

# 4 Savoir aimer: two open hands let a glowing heart rise like a lantern, love given without expecting anything back
d,b=bg([(0,'#0a1830'),(.6,'#2a3a6a'),(1,'#6a5a8a')])
b+=starsf(80,4,700,'#fff6e0')
for sx in (1,-1):
    b+=f'<path transform="translate(400 700) scale({sx} 1)" d="M10 0 Q40 -80 130 -110 Q180 -124 196 -100 Q170 -80 150 -70 Q220 -80 230 -56 Q190 -40 150 -36 Q100 -10 90 40 L10 60Z" fill="#e8c0a0"/>'
d+=rg('h4',S((0,'#fff4e0'),(.5,'#ff9a7a'),(1,'#d83a5a')),.4,.35,.7)
b+=glow(400,400,120,'#ffb090',.5)+heart(400,390,80,'url(#h4)')
b+='<path d="M400 480 Q390 540 400 600" stroke="#ffd0b0" stroke-width="3" fill="none" opacity=".6" stroke-dasharray="6 8"/>'
for x,y in [(300,250),(520,210),(250,420),(560,380)]: b+=sparkle(x,y,12,'#ffe8c0',.8)
I[4]=svg(b,d)

# 5 Born to Be Alive: a disco dancer leaps with arms up into the sunrise, disco ball above, the whole world waking up
d,b=bg([(0,'#2a0a4a'),(.5,'#c83a6a'),(1,'#ffb03a')])
b+=sun(400,560,140,'#ffe07a',20)
b+='<rect y="600" width="800" height="200" fill="#2a0a2a"/>'
for k in range(9): b+=f'<path d="M{400-k*120} 800 L400 600 L{400+k*120} 800" stroke="#ff5aa8" stroke-width="3" fill="none" opacity=".5"/>'
b+=discoball(400,120,60)
b+=f'<g transform="rotate(10 400 640)">{figure(400,640,340,"#1a0420",pose="up")}</g>'
I[5]=svg(b,d)

# 6 Désenchantée: a lone girl leads a grey march of ragged children through a cold, desolate land
d,b=bg([(0,'#3a3e44'),(.6,'#6a6e70'),(1,'#9a9890')])
b+=glow(560,200,160,'#e8e0d0',.35)
b+=hills(560,40,'#4a4c50',6,5)+'<rect y="640" width="800" height="160" fill="#2a2a2e"/>'
r=R(6)
for k in range(16):
    x=r.uniform(40,760);y=r.uniform(560,620);b+=figure(x,y,r.uniform(80,120),'#3a3a3e',hair='#3a3a3e')
b+=figure(400,720,330,'#101014',pose='wave',hair='#101014')
b+=rain(60,6,'#e8e8f0',.25,20)
I[6]=svg(b,d)

# 7 Joe le taxi: a yellow taxi cruising through Paris at night, neon lights and the glowing TAXI sign on its roof
d,b=bg([(0,'#0a0a2a'),(.6,'#2a1040'),(1,'#5a1a3a')])
b+=eiffel(640,520,360,'#140a24','#ff4a8a')
b+=roofs(560,'#100820',6)
b+='<rect y="600" width="800" height="200" fill="#120a18"/><rect y="690" width="800" height="8" fill="#ffd23f" opacity=".5"/>'
b+=glow(400,610,240,'#ffd23f',.25)
b+=car(400,680,1.9,'#ffc81a','#3a6ab0')
b+='<rect x="355" y="368" width="90" height="40" rx="6" fill="#fff4c0"/>'+f'<text x="400" y="400" text-anchor="middle" {F} font-size="30" fill="#2a1a0a">TAXI</text>'
b+=glow(400,388,60,'#fff4c0',.5,'glow2')
I[7]=svg(b,d)

# 8 Bande organisée: Marseille at sunset, the gold Notre-Dame de la Garde on its hill above the Vieux-Port, a crew of silhouettes on the quay
d,b=bg([(0,'#ff8a3a'),(.5,'#e84a3a'),(1,'#4a1a3a')])
b+=sun(400,330,80,'#ffe07a')
b+='<path d="M-10 520 Q200 380 400 330 Q600 380 810 520 L810 800 L-10 800Z" fill="#5a1a30"/>'
b+='<rect x="378" y="190" width="44" height="140" fill="#3a0a1a"/><path d="M370 190 L400 120 L430 190Z" fill="#3a0a1a"/><path d="M394 120 L400 70 L406 120Z" fill="#ffd23f"/>'+glow(400,95,30,'#ffd23f',.8,'glow2')
b+=waves(600,'#2a0a2a',10,10)
for x in (160,250,330,470,560,650): b+=figure(x,640,150+((x*7)%40),'#14040e')
for x in (90,720): b+=f'<rect x="{x}" y="480" width="5" height="130" fill="#14040e"/>'
I[8]=svg(b,d)

# 9 La Tribu de Dana: a Celtic warrior on a misty green moor holds up sword and shield, stone circle behind
d,b=bg([(0,'#1a3a2a'),(.6,'#4a7a5a'),(1,'#a8c0a0')])
for x,h in [(140,170),(250,210),(560,220),(670,170)]: b+=f'<path d="M{x-26} 600 L{x-20} {600-h} Q{x} {590-h} {x+20} {600-h} L{x+26} 600Z" fill="#3a4a40"/>'
b+=hills(600,20,'#2a4a30',9,4)+'<rect y="640" width="800" height="160" fill="#1a3020"/>'
b+=figure(400,700,330,'#0a1a10',pose='up',hair='#0a1a10')
b+='<path d="M330 380 L310 180 L320 176 L344 378Z" fill="#c8d0d8"/><rect x="316" y="372" width="40" height="10" fill="#6a4a2a"/>'
b+='<circle cx="476" cy="420" r="56" fill="#6a4a2a"/><circle cx="476" cy="420" r="40" fill="none" stroke="#d8b040" stroke-width="8"/><path d="M450 420 Q476 380 502 420 Q476 460 450 420Z" fill="none" stroke="#d8b040" stroke-width="6"/>'
b+='<rect y="560" width="800" height="90" fill="#e8f0e8" opacity=".25" filter="url(#glow)"/>'
I[9]=svg(b,d)

# 10 Djadja: a confident woman raises her hand to stop the lies, while gossip bubbles fly around her phone
d,b=bg([(0,'#ff6ab0'),(.6,'#c83a9a'),(1,'#5a1a6a')])
b+=glow(400,380,240,'#ffc0e0',.35)
b+=figure(380,760,420,'#2a0a2a',pose='wave',hair='#2a0a2a')
b+='<path d="M470 290 Q474 250 488 248 Q492 210 506 214 Q514 200 524 214 Q534 206 538 224 L540 300 Q520 330 486 320Z" fill="#2a0a2a"/>'
for x,y,w in [(140,200,150),(170,330,110),(600,450,140)]:
    b+=f'<rect x="{x-w/2}" y="{y-34}" width="{w}" height="68" rx="30" fill="#fff"/><path d="M{x-10} {y+30} L{x-26} {y+56} L{x+8} {y+32}Z" fill="#fff"/>'
    b+=''.join(f'<circle cx="{x-24+k*24}" cy="{y}" r="8" fill="#c83a9a"/>' for k in range(3))
I[10]=svg(b,d)

# 11 Nuit de folie: an 80s night of madness: neon palm, crescent moon and a crowd dancing under a giant disco ball
d,b=bg([(0,'#0a0a30'),(.6,'#3a0a5a'),(1,'#ff3a8a')])
b+=moon(620,170,60,'#fff0c0')+'<circle cx="645" cy="155" r="56" fill="#160a3a"/>'
b+=discoball(300,180,70)
b+=rays(300,180,14,'#ffffff',.06,4)
b+='<rect y="620" width="800" height="180" fill="#1a0420"/>'
for k in range(10): b+=f'<rect x="{k*80}" y="620" width="80" height="180" fill="{["#ff2a8a","#2ad0ff","#ffd23f"][k%3]}" opacity=".25"/>'
r=R(11)
for k in range(7):
    x=90+k*105;b+=figure(x,700,r.uniform(200,260),'#0a0210',pose=r.choice(['up','wave','stand']),hair='#0a0210' if k%2 else None)
I[11]=svg(b,d)

# 12 Formidable: a drunk heartbroken man staggers in the rain on an empty street crossing, bottle in hand, lamps blurred
d,b=bg([(0,'#1a2030'),(.6,'#3a4050'),(1,'#5a5a60')])
b+=skyline(520,'#141a26',12,140,320,'#ffd36a',60)
b+='<rect y="560" width="800" height="240" fill="#2a2e38"/>'
for k in range(6): b+=f'<rect x="{80+k*120}" y="680" width="70" height="26" fill="#e8e8ea" opacity=".8"/>'
b+=f'<g transform="rotate(14 400 700)">{figure(400,700,340,"#0a0c12",pose="reach")}</g>'
b+='<path d="M560 455 L590 430 L604 444 L574 470Z" fill="#2a6a3a"/>'
b+=rain(90,12,'#d0dcf0',.3,10)
b+='<ellipse cx="420" cy="712" rx="110" ry="12" fill="#000" opacity=".35"/>'
I[12]=svg(b,d)

# 13 Je te donne: two guitarists, back to back, French and Welsh-English pride, a heart passing between their guitar necks
d,b=bg([(0,'#1a1a3a'),(.6,'#3a2a5a'),(1,'#6a3a4a')])
b+=glow(400,400,260,'#ffb070',.25)
b+=guitar(300,520,1.2,-25,'#c8682a')+guitar(500,520,1.2,25,'#a83a2a')
d+=rg('h13',S((0,'#fff0d0'),(.5,'#ff6a5a'),(1,'#a8102a')),.4,.35,.7)
b+=heart(400,180,58,'url(#h13)')+glow(400,180,70,'#ff8a6a',.5)
b+='<rect y="700" width="800" height="100" fill="#120a1a"/>'
I[13]=svg(b,d)

# 14 Moi... Lolita: a young girl silhouette with a giant pink heart lollipop, flowers and sweets on a pastel background
d,b=bg([(0,'#ffd0e8'),(.6,'#ff9ac8'),(1,'#d85aa0')])
b+=glow(520,300,200,'#fff',.35)
b+='<rect x="512" y="300" width="12" height="400" fill="#f6efe2"/>'
d+=rg('l14',S((0,'#fff'),(.4,'#ff6ab0'),(1,'#c8186a')),.4,.35,.7)
b+=heart(518,270,110,'url(#l14)')
b+='<path d="M450 240 Q518 200 590 250 M440 300 Q518 260 600 310" stroke="#fff" stroke-width="8" fill="none" opacity=".6"/>'
b+=figure(330,760,380,'#4a0a3a',pose='reach',hair='#4a0a3a')
b+='<path d="M306 380 Q280 400 286 430 M354 380 Q380 400 374 430" stroke="#4a0a3a" stroke-width="16" stroke-linecap="round" fill="none"/>'
I[14]=svg(b,d)

# 15 Non, je ne regrette rien: the small singer in a black dress, arms wide, alone before red velvet curtains in a single spotlight
d,b=bg([(0,'#3a0608'),(1,'#1a0204')])
for k in range(10): b+=f'<path d="M{k*80} 0 Q{k*80+40} 400 {k*80} 800 L{k*80+80} 800 Q{k*80+40} 400 {k*80+80} 0Z" fill="{"#8a0e14" if k%2 else "#6a0a10"}"/>'
b+='<path d="M-10 -10 Q400 140 810 -10 L810 90 Q400 230 -10 90Z" fill="#a8141c"/>'
b+='<polygon points="400,-20 250,800 550,800" fill="#fff6dc" opacity=".2"/>'+'<ellipse cx="400" cy="730" rx="160" ry="24" fill="#fff6dc" opacity=".35"/>'
b+=figure(400,730,280,'#050204',pose='up',hair='#050204')
b+='<path d="M372 510 Q400 740 428 510Z" fill="#050204"/>'
I[15]=svg(b,d)

# 16 Dernière danse: a woman in a red dress whirls alone on a wet Paris street at night, the Eiffel Tower glowing in the mist
d,b=bg([(0,'#0a0a1a'),(.6,'#1a1a3a'),(1,'#3a2a4a')])
b+=glow(600,380,170,'#ffd27a',.25)+eiffel(600,600,470,'#4a3a5a','#ffd27a')
b+=roofs(600,'#0e0e1c',16)
b+='<rect y="640" width="800" height="160" fill="#14141e"/>'
b+='<ellipse cx="330" cy="760" rx="160" ry="20" fill="#d81a2a" opacity=".25"/>'
b+=figure(330,740,360,'#0a0408',pose='up',hair='#0a0408')
b+='<path d="M306 468 Q230 640 200 744 Q330 720 460 744 Q430 640 354 468Z" fill="#d81a2a"/>'
b+=rain(70,16,'#c0c8e8',.25,8)
I[16]=svg(b,d)

# 17 Ma philosophie: a young woman stands tall on a mountain top facing the sun, head high, refusing to be put down
d,b=bg([(0,'#ffb03a'),(.5,'#ff6a5a'),(1,'#7a2a6a')])
b+=sun(400,290,110,'#fff0a0',18)
b+='<path d="M-10 800 L200 560 L300 620 L400 470 L520 600 L620 540 L810 800Z" fill="#3a1a3a"/><path d="M360 520 L400 470 L440 520Z" fill="#fff" opacity=".8"/>'
b+=figure(400,480,180,'#1a0814',pose='up',hair='#1a0814')
for x,y in [(160,180),(650,160),(700,320)]: b+=bird(x,y,18,'#3a1a3a')
I[17]=svg(b,d)

# 18 J'ai demandé à la lune: a boy sits on a rooftop under a huge, kind full moon, asking it a question
d,b=bg([(0,'#04081a'),(.6,'#10204a'),(1,'#2a3a6a')])
b+=starsf(90,18,600)
b+=moon(470,300,170,'#f4f0dc',.3)
b+='<circle cx="420" cy="260" r="26" fill="#e0dcc4"/><circle cx="530" cy="350" r="34" fill="#e0dcc4"/><circle cx="500" cy="220" r="14" fill="#e0dcc4"/>'
b+=roofs(660,'#060a18',18)
b+='<path d="M60 660 L60 560 L360 560 L360 660Z" fill="#060a18"/>'
b+=figure(200,562,260,'#060a18','reach')
I[18]=svg(b,d)

# 19 Le Sud: a sun-drenched southern landscape, a tiled-roof farmhouse among cypresses and sunflower fields that stretch forever
d,b=bg([(0,'#5ab0e8'),(.6,'#a8d8f0'),(1,'#fff0c0')])
b+=sun(620,150,60,'#fff4a0')
b+=hills(470,30,'#8ab07a',19,4)
b+='<rect x="280" y="380" width="180" height="110" fill="#f0d8a8"/><path d="M266 384 L370 330 L474 384Z" fill="#c8582a"/><rect x="340" y="420" width="40" height="70" fill="#7a4a2a"/><rect x="300" y="410" width="26" height="26" fill="#5a8ab0"/><rect x="410" y="410" width="26" height="26" fill="#5a8ab0"/>'
for x,h in [(230,200),(500,230),(540,180)]: b+=f'<path d="M{x} 490 Q{x-24} {490-h*.6} {x} {490-h} Q{x+24} {490-h*.6} {x} 490Z" fill="#2a4a2a"/>'
b+='<rect y="490" width="800" height="310" fill="#e8b020"/>'
r=R(19)
for k in range(46):
    x=r.uniform(-20,820);y=r.uniform(510,800);s=6+(y-500)/14
    b+=''.join(f'<ellipse cx="{x+math.cos(a)*s:.0f}" cy="{y+math.sin(a)*s:.0f}" rx="{s*.5:.0f}" ry="{s*.25:.0f}" transform="rotate({math.degrees(a):.0f} {x+math.cos(a)*s:.0f} {y+math.sin(a)*s:.0f})" fill="#ffd23f"/>' for a in [i*math.pi/4 for i in range(8)])+f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s*.55:.0f}" fill="#6a3a0a"/>'
I[19]=svg(b,d)

# 20 Mistral gagnant: a father and his little girl on a park bench by the sea, sharing old-fashioned sweets
d,b=bg([(0,'#ffcf8a'),(.5,'#f8a07a'),(1,'#8a5a7a')])
b+=sun(560,380,70,'#fff0c0')
b+=waves(440,'#5a7aa0',8,9)+waves(470,'#4a6a90',6,7)
b+='<rect y="560" width="800" height="240" fill="#d8b890"/>'
b+='<rect x="170" y="560" width="460" height="18" rx="4" fill="#5a3a20"/><rect x="170" y="500" width="460" height="16" rx="4" fill="#5a3a20"/><rect x="190" y="578" width="14" height="100" fill="#3a2414"/><rect x="596" y="578" width="14" height="100" fill="#3a2414"/>'
b+=f'<g>{figure(330,640,260,"#2a1a2a")}</g>'+figure(470,620,150,'#2a1a2a',pose='hold',hair='#2a1a2a')
b+='<rect x="450" y="470" width="40" height="54" rx="4" fill="#f6f0e0"/><path d="M450 488 L490 488" stroke="#2a5ad0" stroke-width="6"/><path d="M450 500 L490 500" stroke="#d8342c" stroke-width="6"/>'
I[20]=svg(b,d)

for k,v in I.items(): open(f'/mnt/project-files/ikonok/orszag/fr/ikonrajz/svg/{k}.svg','w').write(v)
print(len(I))
