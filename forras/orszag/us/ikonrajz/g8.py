import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 8. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 191 Hollaback Girl (Gwen Stefani, 2005): a marching-band drumline and cheerleader pom-poms on a football field, bananas spelled out on the turf
d,b=bg([(0,'#2a6a3a'),(1,'#1a4a2a')])
for k in range(8): b+=f'<rect x="0" y="{k*100}" width="800" height="6" fill="#fff" opacity=".5"/>'
b+='<path d="M200 600 Q260 500 300 560 Q260 620 200 600Z M500 600 Q560 500 600 560 Q560 620 500 600Z" fill="#ffe12a"/>'
b+='<g transform="translate(400 380)"><ellipse rx="110" ry="40" fill="#f2f2f2"/><rect x="-110" y="0" width="220" height="110" fill="#e0102a"/><ellipse cy="110" rx="110" ry="40" fill="#b00a1e"/><ellipse rx="110" ry="40" fill="#f6f6f6" stroke="#ccc" stroke-width="4"/>'
b+='<path d="M-110 20 L-40 100 L40 20 L110 100" stroke="#ffd23a" stroke-width="6" fill="none"/><path d="M-60 -90 L-20 -10 M60 -90 L20 -10" stroke="#e8d0a0" stroke-width="10" stroke-linecap="round"/></g>'
for x in (130,670):
    for k in range(18): a=k*.35;b+=f'<path d="M{x} 200 l{50*math.cos(a):.0f} {50*math.sin(a):.0f}" stroke="#ffe12a" stroke-width="7" stroke-linecap="round"/>'
I[191]=svg(b,d)

# 192 Poker Face (Lady Gaga, 2009): a poker hand of cards with an ace of hearts, a lightning-bolt makeup mask over a casino-blue table
d,b=bg([(0,'#04142a'),(1,'#0a3a5a')])
b+=glow(400,420,260,'#3ad8ff',.3)
for k,a in enumerate((-30,-15,0,15,30)):
    b+=f'<g transform="rotate({a} 400 700)"><rect x="330" y="300" width="140" height="200" rx="12" fill="#fbfbfb" stroke="#c8c8d0" stroke-width="3"/></g>'
b+='<g transform="rotate(30 400 700)"><text x="360" y="350" font-family="Georgia,serif" font-size="40" fill="#d0102a">A</text></g>'+heart(470,360,26,'#d0102a','transform="rotate(30 400 700)"')
b+='<path d="M420 120 L370 220 L410 220 L370 320" stroke="#ffe14a" stroke-width="12" fill="none" stroke-linejoin="round"/>'
I[192]=svg(b,d)

# 194 Blurred Lines (Robin Thicke ft. T.I. & Pharrell, 2013): a retro chrome microphone sharp in front of out-of-focus black-and-white stripes
d,b=bg([(0,'#f6f6f6'),(1,'#d8d8d8')])
b+='<g filter="url(#glow)">'+''.join(f'<rect x="{k*100-20}" y="0" width="50" height="800" fill="#111" transform="rotate(12 400 400)"/>' for k in range(10))+'</g>'
b+=mic(400,330,170,'#e8e8ee')
I[194]=svg(b,d)

# 195 Dark Horse (Katy Perry ft. Juicy J, 2014): an Egyptian queen's eye of Horus and a black horse in gold, desert dusk
d,b=bg([(0,'#1a0a2a'),(.6,'#7a3a1a'),(1,'#d89a3a')])
b+='<path d="M120 600 L320 320 L520 600Z" fill="#3a2010"/><rect y="600" width="800" height="200" fill="#5a3a1a"/>'
b+='<g transform="translate(560 560)" fill="#0a0402"><path d="M-120 -60 Q-80 -110 20 -100 Q60 -150 100 -130 L90 -90 Q60 -90 60 -60 L50 40 L36 40 L30 -30 L-70 -30 L-90 40 L-104 40 L-100 -40 Q-140 -20 -160 -50Z"/><path d="M60 -130 Q40 -180 80 -170 Q50 -150 70 -120Z"/></g>'
b+='<g transform="translate(320 200)" stroke="#e8c040" stroke-width="10" fill="none"><path d="M-110 0 Q0 -70 110 0 Q0 60 -110 0Z"/><circle r="26" fill="#e8c040"/><path d="M-20 40 L-30 110 Q-50 130 -70 110 M20 40 L60 90"/></g>'
I[195]=svg(b,d)

# 196 Sunflower (Post Malone & Swae Lee, 2019): a giant sunflower rising against a comic-book halftone sky, a little web-swinger silhouette far away
d,b=bg([(0,'#3a8ae8'),(1,'#9ad0ff')])
for i in range(20):
    for j in range(20): b+=f'<circle cx="{i*40+20}" cy="{j*40+20}" r="5" fill="#fff" opacity=".18"/>'
b+='<path d="M400 800 L400 460" stroke="#2a7a2a" stroke-width="22"/><path d="M400 640 Q480 600 540 640 Q480 680 400 640Z M400 700 Q320 660 260 700 Q320 740 400 700Z" fill="#3a9a3a"/>'
for k in range(20): a=k*0.314;b+=f'<ellipse cx="{400+130*math.cos(a):.0f}" cy="{360+130*math.sin(a):.0f}" rx="60" ry="24" fill="#ffd21a" transform="rotate({k*18} {400+130*math.cos(a):.0f} {360+130*math.sin(a):.0f})"/>'
b+='<circle cx="400" cy="360" r="90" fill="#5a2a0a"/>'+''.join(f'<circle cx="{400+r_*math.cos(a):.0f}" cy="{360+r_*math.sin(a):.0f}" r="5" fill="#3a1a04"/>' for r_ in (30,60) for a in [k*0.5 for k in range(13)])
b+='<path d="M720 40 L640 150" stroke="#fff" stroke-width="2"/>'+figure(640,180,40,'#c8102a',pose='up')
I[196]=svg(b,d)

# 197 Circles (Post Malone, 2020): a lone figure walking in endless concentric circles on a misty hill at dawn
d,b=bg([(0,'#3a3a5a'),(1,'#d8b8a0')])
for k in range(9): b+=f'<ellipse cx="400" cy="600" rx="{60+k*48}" ry="{18+k*14}" fill="none" stroke="#f2e6e0" stroke-width="5" opacity="{.8-k*.07:.2f}"/>'
b+=glow(400,300,120,'#fff2e0',.7)+figure(400,610,200,'#1a1a24',pose='stand')
I[197]=svg(b,d)

# 198 A Bar Song (Tipsy) (Shaboozey, 2024): a honky-tonk bar with a neon beer sign, whiskey shots lined up and a cowboy hat on the counter
d,b=bg([(0,'#1a0a04'),(1,'#4a2010')])
b+=neon('BAR',400,200,120,'#ff6a2a','Arial Black,Arial',False)
b+='<rect y="520" width="800" height="280" fill="#3a1a08"/><rect y="500" width="800" height="30" fill="#6a3a14"/>'
for x in (160,240,320,400,480): b+=f'<path d="M{x-24} 440 L{x+24} 440 L{x+20} 500 L{x-20} 500Z" fill="#f6efe0" opacity=".5"/><path d="M{x-22} 460 L{x+22} 460 L{x+20} 500 L{x-20} 500Z" fill="#d8902a"/>'
b+=hat(630,490,80,'#c8905a','#3a2010')
I[198]=svg(b,d)

# 199 Don't Be Cruel (Elvis Presley, 1956): a 1950s telephone with a curly cord and a heart-shaped note pinned to a bulletin board, rockabilly red
d,b=bg([(0,'#d8202a'),(1,'#7a0a10')])
for k in range(8): b+=f'<rect x="{k*100}" y="0" width="50" height="800" fill="#fff" opacity=".06"/>'
b+='<path d="M260 520 L540 520 L520 640 L280 640Z" fill="#0a0a0a"/><path d="M240 500 Q400 400 560 500 L540 530 Q400 450 260 530Z" fill="#1a1a1a"/><circle cx="400" cy="580" r="40" fill="#f2f2f2"/>'
b+='<path d="M540 600 q30 20 0 40 q-30 20 0 40 q30 20 0 40" stroke="#0a0a0a" stroke-width="8" fill="none"/>'
b+=heart(400,260,80,'#fbf6ea')+'<circle cx="400" cy="200" r="10" fill="#d0102a"/>'
I[199]=svg(b,d)

# 200 Don't (Elvis Presley, 1958): a tender slow-dance at a 50s prom, gym streamers and a mirror ball, pastel blue
d,b=bg([(0,'#1a2a4a'),(1,'#7a9ac8')])
b+=disco(400,120,60)+''.join(f'<path d="M{k*100} 0 Q{k*100+50} 120 {k*100+100} 0" stroke="{["#ffb0d0","#bff0ff"][k%2]}" stroke-width="10" fill="none"/>' for k in range(8))
b+='<ellipse cx="400" cy="720" rx="220" ry="30" fill="#fff" opacity=".18"/>'
b+=figure(370,720,340,'#0a1020',pose='hold')+'<g>'+figure(430,720,320,'#0a1020',pose='hold',hair='#0a1020')+'</g><path d="M360 720 Q430 560 500 720Z" fill="#ffb0d0"/>'
I[200]=svg(b,d)

# 211 I Heard It Through the Grapevine (Marvin Gaye, 1968): a cluster of purple grapes on a vine whispering in a speech bubble, a 60s soul radio
d,b=bg([(0,'#2a1a3a'),(1,'#7a5a8a')])
b+='<path d="M80 120 Q300 60 520 140" stroke="#5a3a1a" stroke-width="12" fill="none"/>'+''.join(f'<path d="M{150+k*110} {100+k*8} q30 -40 60 0 q-30 30 -60 0Z" fill="#4a8a3a"/>' for k in range(4))
r=random.Random(211)
for row in range(6):
    for col in range(6-row): b+=f'<circle cx="{300+col*48-(5-row)*24+120}" cy="{180+row*44}" r="26" fill="#6a2a8a" stroke="#4a1a6a" stroke-width="3"/>'
b+='<path d="M480 380 Q480 300 600 300 Q720 300 720 380 Q720 460 600 460 L560 460 L520 500 L530 460 Q480 450 480 380Z" fill="#fff" opacity=".9"/>'+''.join(f'<circle cx="{560+k*40}" cy="380" r="8" fill="#5a3a6a"/>' for k in range(3))
I[211]=svg(b,d)

# 212 It's Too Late (Carole King, 1971): a woman with long curly hair at a window seat with a cat, a Laurel Canyon morning, piano in shadow
d,b=bg([(0,'#c8a080'),(1,'#f2e0c8')])
b+='<rect x="160" y="80" width="480" height="420" fill="#a8c8d8"/>'+hills(360,30,'#6a8a5a',212,4)+'<path d="M160 290 L640 290 M400 80 L400 500" stroke="#5a3a24" stroke-width="16"/><rect x="160" y="80" width="480" height="420" fill="none" stroke="#5a3a24" stroke-width="20"/>'
b+='<rect y="500" width="800" height="300" fill="#8a5a3a"/>'
b+='<g fill="#2a1408"><circle cx="330" cy="420" r="40"/><path d="M290 420 Q260 480 280 540 L380 540 Q400 480 370 420Z"/><path d="M270 540 L460 540 L460 600 L270 600Z"/></g>'
b+='<g fill="#2a1408"><ellipse cx="500" cy="560" rx="40" ry="26"/><circle cx="530" cy="530" r="18"/><path d="M520 516 L524 500 L532 514Z M536 514 L544 500 L546 516Z"/></g>'
I[212]=svg(b,d)

# 220 I Miss You (Klymaxx, 1986): an empty chair beside a lit lamp and a framed photo, rain on the window, mauve 80s glow
d,b=bg([(0,'#2a1a3a'),(1,'#8a5a7a')])
b+='<rect x="460" y="100" width="260" height="360" fill="#3a3a5a"/>'+rain(50,220,'#e0e0ff',.4,4,460)
b+='<rect y="560" width="800" height="240" fill="#2a1424"/>'
b+='<path d="M200 380 L340 380 L340 560 L320 560 L320 480 L220 480 L220 560 L200 560Z" fill="#5a2a3a"/><rect x="200" y="460" width="140" height="30" fill="#7a3a4a"/>'
b+='<path d="M400 560 L400 300" stroke="#c8b0a0" stroke-width="6"/><path d="M360 300 L440 300 L420 240 L380 240Z" fill="#f2d8a0"/>'+glow(400,300,70,'#ffe0b0',.6)
b+='<rect x="470" y="490" width="70" height="80" fill="#c8a06a"/><rect x="478" y="498" width="54" height="64" fill="#5a4a6a"/>'
I[220]=svg(b,d)

# 221 Shake You Down (Gregory Abbott, 1987): a smooth crooner in a white suit under a palm-shadowed magenta sunset, a sax glinting
d,b=bg([(0,'#2a0a3a'),(.6,'#c83a7a'),(1,'#ffb07a')])
b+=glow(400,520,180,'#ffe0c0',.7)+palm(130,620,340,'#1a0614',10)+palm(680,620,300,'#1a0614',-10)
b+='<rect y="620" width="800" height="180" fill="#1a0614"/>'+figure(400,760,380,'#f6f2ee',pose='stand')+'<ellipse cx="400" cy="474" rx="22" ry="27" fill="#2a1408"/>'
I[221]=svg(b,d)

# 222 Every Rose Has Its Thorn (Poison, 1989): a single long-stemmed red rose with sharp thorns lying across an acoustic guitar
d,b=bg([(0,'#0a0404'),(1,'#2a0a0a')])
b+=guitar(420,520,160,'#8a5a2a','#3a2010',30)
b+='<path d="M120 640 Q360 520 620 260" stroke="#1a5a1a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{200+k*90} {600-k*72} l-16 -18 l22 4Z" fill="#1a5a1a"/>' for k in range(4))
b+='<g transform="translate(630 250)"><circle r="40" fill="#c8001a"/><path d="M-26 -10 Q0 -40 26 -10 Q0 10 -26 -10Z" fill="#8a0010"/><path d="M-20 10 Q0 -14 20 10" stroke="#ff4a5a" stroke-width="4" fill="none"/></g>'
I[222]=svg(b,d)

# 223 Gonna Make You Sweat (Everybody Dance Now) (C+C Music Factory, 1991): an early-90s gym-turned-rave with a dancer in a cut-off top and lasers
d,b=bg([(0,'#1a0a3a'),(1,'#ff2a6a')])
for k in range(12): b+=f'<path d="M0 {k*60} L800 {800-k*60}" stroke="{["#3affe0","#ffe14a"][k%2]}" stroke-width="3" opacity=".4"/>'
b+=figure(400,780,460,'#0a0418',pose='up')
for k in range(10): b+=f'<circle cx="{330+(k%5)*35}" cy="{300+(k//5)*20}" r="5" fill="#9ad8ff"/>'
I[223]=svg(b,d)

# 224 Jump (Kris Kross, 1992): two kids jumping high wearing backwards jeans, baseball caps flying, a 90s neon backdrop
d,b=bg([(0,'#3ad8ff'),(1,'#ffe14a')])
b+='<rect y="680" width="800" height="120" fill="#2a2a3a"/>'
for x,y in ((300,560),(500,520)): b+=figure(x,y,300,'#1a1a2a',pose='up')+f'<path d="M{x-30} {y-310} L{x+30} {y-310} L{x+44} {y-296} L{x-30} {y-296}Z" fill="#e0102a"/>'
b+='<ellipse cx="300" cy="720" rx="60" ry="10" fill="#000" opacity=".3"/><ellipse cx="500" cy="720" rx="60" ry="10" fill="#000" opacity=".3"/>'
I[224]=svg(b,d)

# 225 Creep (TLC, 1995): three women in satin silk pajamas posing in a slick blue-lit warehouse
d,b=bg([(0,'#0a1a3a'),(1,'#3a6ab0')])
for x in (200,400,600): b+=spotlight(x,0,120,'#bfe0ff',.12)
d+=lg('silk',S((0,'#e8f0ff'),(.5,'#9ab8e8'),(1,'#f2f6ff')),0,0,1,0)
for x in (260,400,540): b+=figure(x,740,380,'url(#silk)',pose='stand',hair='#0a0a14')
I[225]=svg(b,d)

# 226 Angel of Mine (Monica, 1999): a soft-feather angel wing behind a woman in white, clouds and pearly glow
d,b=bg([(0,'#5a7ab0'),(1,'#d8c8e0')])
b+=glow(400,360,200,'#fff',.6)
for s in (-1,1):
    for k in range(6): b+=f'<path d="M400 340 Q{400+s*(140+k*30)} {200+k*20} {400+s*(260+k*20)} {300+k*40} Q{400+s*(180+k*20)} {320+k*20} 400 {380+k*10}Z" fill="#fff" stroke="#d8e0f0" stroke-width="3"/>'
b+=figure(400,760,420,'#f6f2ee',pose='hold',hair='#3a2a1a')+'<ellipse cx="400" cy="402" rx="25" ry="30" fill="#5a3a2a"/><ellipse cx="400" cy="350" rx="40" ry="10" fill="none" stroke="#ffd84a" stroke-width="6"/>'
I[226]=svg(b,d)

# 227 Maria Maria (Santana ft. The Product G&B, 2000): a woman in a flowing red dress in a Spanish Harlem street, a flamenco guitar and hot sun
d,b=bg([(0,'#ffb03a'),(1,'#d8402a')])
b+=glow(600,180,110,'#fff2c0',.8)+skyline(560,'#7a2a1a',227,140,320,'#ffd27a',30)+'<rect y="640" width="800" height="160" fill="#5a1a0a"/>'
b+='<g transform="translate(330 760)"><circle cx="0" cy="-320" r="26" fill="#1a0604"/><path d="M-20 -296 L20 -296 L36 -180 Q140 -40 170 0 L-170 0 Q-90 -60 -36 -180Z" fill="#e0102a"/><path d="M-170 0 Q-60 -30 170 0 Q40 -50 -170 0Z" fill="#a00a1a"/></g>'
b+=guitar(600,620,110,'#c8843a','#3a2010',18)
I[227]=svg(b,d)

# 228 All for You (Janet Jackson, 2001): a sunny animated city street with a woman dancing on a rooftop, bright sky blue and lime
d,b=bg([(0,'#3ab8ff'),(1,'#bff0ff')])
b+=skyline(520,'#2a5a8a',228,120,300,'#bff0ff',60)+'<rect y="560" width="800" height="240" fill="#9ae04a"/>'
b+='<rect x="300" y="440" width="200" height="120" fill="#ff6a3a"/>'+figure(400,440,240,'#1a1a2a',pose='wave',hair='#1a1a2a')
b+=glow(640,120,80,'#fff8c0',.9)
I[228]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
