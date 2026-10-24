import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 7. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 155 Irreplaceable (Beyoncé, 2007): a box of a man's belongings by the front door, pointing hand: to the left, the left
d,b=bg([(0,'#3a2a1a'),(1,'#c8a06a')])
b+='<rect x="440" y="140" width="240" height="460" fill="#2a1a0a"/><rect x="460" y="160" width="200" height="440" fill="#f6dfa0" opacity=".7"/>'
b+='<path d="M120 520 L380 520 L360 680 L140 680Z" fill="#b08040"/><path d="M120 520 L170 480 L410 480 L380 520Z" fill="#c8985a"/>'
b+='<rect x="170" y="440" width="120" height="70" fill="#3a4a7a"/><circle cx="320" cy="460" r="26" fill="#e8e8f0"/>'
b+='<path d="M220 280 L120 280 L150 250 M120 280 L150 310" stroke="#fff" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
b+='<rect y="680" width="800" height="120" fill="#4a3018"/>'
I[155]=svg(b,d)

# 156 Low (Flo Rida ft. T-Pain, 2008): apple-bottom jeans and boots with fur in a packed club, a bass speaker pulsing low
d,b=bg([(0,'#0a0420'),(1,'#3a0a4a')])
b+='<rect x="250" y="260" width="300" height="420" rx="20" fill="#14101a"/>'
for y,r in ((380,110),(580,80)): b+=f'<circle cx="400" cy="{y}" r="{r}" fill="#2a2234"/><circle cx="400" cy="{y}" r="{r*.6:.0f}" fill="#0a0810"/><circle cx="400" cy="{y}" r="{r*.2:.0f}" fill="#4a4258"/>'
for k in range(4): b+=f'<circle cx="400" cy="380" r="{140+k*40}" fill="none" stroke="#ff3ad8" stroke-width="4" opacity="{.6-k*.12:.2f}"/>'
b+='<rect y="700" width="800" height="100" fill="#0a0414"/>'
I[156]=svg(b,d)

# 157 Boom Boom Pow (The Black Eyed Peas, 2009): a futuristic digital grid exploding with neon pixels, a robotic figure in LED armor
d,b=bg([(0,'#000'),(1,'#0a0a2a')])
for k in range(16): b+=f'<path d="M{k*50} 0 L{k*50} 800 M0 {k*50} L800 {k*50}" stroke="#3ad8ff" stroke-width="1" opacity=".2"/>'
r=random.Random(157)
for k in range(80): x,y=r.randrange(0,16)*50,r.randrange(0,16)*50;b+=f'<rect x="{x}" y="{y}" width="50" height="50" fill="{r.choice(["#3ad8ff","#ff3ad8","#ffe14a"])}" opacity="{r.uniform(.1,.5):.2f}"/>'
b+=glow(400,520,180,'#3ad8ff',.35)+figure(400,780,460,'#0a0a1a',pose='up')+''.join(f'<rect x="{372+(k%4)*14}" y="{460+(k//4)*20}" width="10" height="10" fill="#3ad8ff"/>' for k in range(16))
I[157]=svg(b,d)

# 158 Tik Tok (Kesha, 2010): a glittery party girl waking in a bathtub, alarm clock and spilled glitter, morning after
d,b=bg([(0,'#f2e8f0'),(1,'#d8c8e0')])
b+='<path d="M120 460 L680 460 L640 680 Q620 720 580 720 L220 720 Q180 720 160 680Z" fill="#fbfbfb" stroke="#c8c0d0" stroke-width="6"/>'
b+='<path d="M240 460 Q260 400 320 400 Q380 410 390 460Z" fill="#e8c06a"/>'+confetti(120,158,['#ffd23a','#ff3a9a','#3ad8ff','#fff'],380,720,.9)
b+='<g transform="translate(600 300)"><circle r="80" fill="#ff3a7a"/><circle r="64" fill="#fff"/><path d="M0 0 L0 -44 M0 0 L30 16" stroke="#111" stroke-width="7" stroke-linecap="round"/><circle cx="-60" cy="-70" r="22" fill="#ff3a7a"/><circle cx="60" cy="-70" r="22" fill="#ff3a7a"/></g>'
I[158]=svg(b,d)

# 160 Happy (Pharrell Williams, 2014): a giant yellow smiley wearing a tall felt ranger hat, people dancing around it
d,b=bg([(0,'#ffe12a'),(1,'#ffb02a')])
b+='<circle cx="400" cy="420" r="190" fill="#fff23a" stroke="#e8a000" stroke-width="10"/><circle cx="340" cy="380" r="22" fill="#2a1a0a"/><circle cx="460" cy="380" r="22" fill="#2a1a0a"/><path d="M300 470 Q400 560 500 470" stroke="#2a1a0a" stroke-width="16" fill="none" stroke-linecap="round"/>'
b+='<path d="M220 250 Q400 210 580 250 L560 270 Q400 240 240 270Z" fill="#6a4a2a"/><path d="M300 250 Q290 120 340 100 Q400 80 460 100 Q510 120 500 250Z" fill="#7a5a34"/><path d="M300 230 Q400 214 500 230 L500 250 Q400 236 300 250Z" fill="#3a2a1a"/>'
for k,x in enumerate((90,710)): b+=figure(x,780,240,'#3a2a0a',pose='up' if k else 'wave')
I[160]=svg(b,d)

# 161 Lose Control (Teddy Swims, 2024): a soul singer with a beanie, eyes closed, gripping a mic, warm smoky stage light breaking apart
d,b=bg([(0,'#1a0a04'),(1,'#5a2a14')])
b+=spotlight(400,0,220,'#ffcf8a',.22)+glow(400,300,160,'#ffa04a',.4)
b+=figure(400,800,520,'#0a0402',pose='hold')+'<path d="M360 316 Q360 270 400 268 Q440 270 440 316Z" fill="#c8402a"/>'
b+=mic(400,470,60,'#c8c8d0',stand=False)
for k in range(6): b+=f'<path d="M{200+k*80} 700 l{20-k*8} -60" stroke="#ffcf8a" stroke-width="4" opacity=".4"/>'
I[161]=svg(b,d)

# 165 I Fall to Pieces (Patsy Cline, 1961): a porcelain heart breaking into floating pieces over a vintage country radio
d,b=bg([(0,'#2a3a5a'),(1,'#8aa0b8')])
b+='<rect x="250" y="540" width="300" height="180" rx="26" fill="#8a5a2a"/><rect x="280" y="570" width="160" height="110" rx="10" fill="#e8d8b0"/><circle cx="490" cy="600" r="22" fill="#3a2a1a"/><circle cx="490" cy="660" r="16" fill="#3a2a1a"/>'
for k,(x,y,a) in enumerate(((360,300,-12),(440,280,10),(330,400,20),(460,390,-18),(400,460,4))): b+=f'<path d="M{x} {y} l40 -10 l20 40 l-30 30 l-40 -16Z" fill="#e0102a" transform="rotate({a} {x} {y})"/>'
I[165]=svg(b,d)

# 170 The Letter (The Box Tops, 1967): a jet plane climbing over an airmail envelope, red-blue striped border
d,b=bg([(0,'#7ab0e0'),(1,'#d8ecf8')])
b+='<g transform="translate(400 520) rotate(-6)"><rect x="-240" y="-150" width="480" height="300" fill="#fbf8f0"/>'
for k in range(24): b+=f'<rect x="{-240+k*20}" y="-150" width="10" height="12" fill="{["#e0102a","#1a3aa8"][k%2]}"/><rect x="{-240+k*20}" y="138" width="10" height="12" fill="{["#1a3aa8","#e0102a"][k%2]}"/>'
b+='<rect x="140" y="-120" width="70" height="80" fill="#e8c06a"/><path d="M-200 -40 L60 -40 M-200 0 L20 0 M-200 40 L80 40" stroke="#8a8a9a" stroke-width="6"/></g>'
b+='<g transform="translate(470 200) rotate(-20)" fill="#f2f2f6"><path d="M-160 10 L140 -6 Q170 -6 160 12 L-150 26Z"/><path d="M-20 4 L-90 80 L-60 80 L30 4Z"/><path d="M-20 0 L-80 -50 L-56 -50 L20 0Z"/><path d="M-150 12 L-176 -30 L-152 -30 L-120 10Z"/></g>'
I[170]=svg(b,d)

# 173 Bad, Bad Leroy Brown (Jim Croce, 1973): a sharp-dressed man in a fedora leaning on a custom Eldorado on a Chicago South Side street
d,b=bg([(0,'#0a0a1a'),(1,'#3a2a4a')])
b+=skyline(520,'#1a142a',173,100,280,'#ffd27a',70)+'<rect y="600" width="800" height="200" fill="#141018"/>'
b+=car(470,720,150,'#e8d040','#f2f2f2',glass='#9ac0e0')
b+=figure(180,740,320,'#0a0610',pose='stand')+hat(180,438,44,'#0a0610','#c8102a')
b+='<circle cx="140" cy="560" r="8" fill="#ffd84a"/>'
I[173]=svg(b,d)

# 174 Rhinestone Cowboy (Glen Campbell, 1975): a sparkling rhinestone cowboy hat and boots under Broadway marquee lights
d,b=bg([(0,'#1a0a2a'),(1,'#5a2a6a')])
b+='<rect x="60" y="80" width="680" height="120" fill="#2a1a3a"/>'+''.join(f'<circle cx="{80+k*36}" cy="{90 if k%2 else 190}" r="9" fill="#ffd84a"/>' for k in range(19))
b+=hat(400,420,170,'#f2f2fa','#5a8ad8')
r=random.Random(174)
for k in range(30): x,y=r.uniform(170,630),r.uniform(270,470);b+=sparkle(round(x),round(y),r.choice([6,9,12]),'#fff') if abs(x-400)<250 else ''
b+=star5(400,620,70,'#ffd84a')
I[174]=svg(b,d)

# 177 Eye of the Tiger (Survivor, 1982): a fierce tiger's eye in close-up, orange-black stripes, a boxing glove hanging below
d,b=bg([(0,'#e8801a'),(1,'#a84a0a')])
for k in range(9): b+=f'<path d="M{k*100-60} 0 Q{k*100+20} 200 {k*100-20} 400 Q{k*100+40} 600 {k*100-30} 800" stroke="#1a0a02" stroke-width="30" fill="none"/>'
b+='<path d="M140 360 Q400 160 660 360 Q400 560 140 360Z" fill="#f6e0a0" stroke="#1a0a02" stroke-width="16"/><circle cx="400" cy="360" r="110" fill="#e8b020"/><ellipse cx="400" cy="360" rx="26" ry="96" fill="#0a0402"/><circle cx="360" cy="320" r="18" fill="#fff" opacity=".8"/>'
b+='<path d="M560 800 L560 640" stroke="#f2f2f2" stroke-width="6"/><path d="M500 640 Q500 560 560 550 Q630 550 630 620 Q630 680 580 690 L520 690 Q500 680 500 640Z" fill="#d0102a"/>'
I[177]=svg(b,d)

# 178 What's Love Got to Do with It (Tina Turner, 1984): a wild-maned woman in a leather jacket and miniskirt striding down a sunlit NYC street
d,b=bg([(0,'#f0b06a'),(1,'#8a4a2a')])
b+=skyline(520,'#5a2a1a',178,120,320,None)+'<rect y="660" width="800" height="140" fill="#3a2010"/>'
b+='<path d="M400 160 Q300 200 310 300 Q290 340 330 360 Q350 300 400 296 Q450 300 470 360 Q510 340 490 300 Q500 200 400 160Z" fill="#1a0a04"/>'
b+=figure(400,760,480,'#0a0402',pose='stand')
I[178]=svg(b,d)

# 179 Say You, Say Me (Lionel Richie, 1986): a man at a grand piano under one spotlight, a white rose floating, gentle indigo
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=spotlight(400,0,220,'#f2f0ff',.2)
b+='<path d="M180 640 L540 640 Q620 640 620 590 L600 550 Q500 500 380 520 L190 540Z" fill="#05050e"/><rect x="200" y="640" width="12" height="100" fill="#05050e"/><rect x="520" y="640" width="12" height="100" fill="#05050e"/>'
b+='<rect x="190" y="580" width="230" height="18" fill="#f2f0ff"/>'+figure(300,640,190,'#05050e',pose='hold')
b+='<circle cx="560" cy="300" r="22" fill="#fbf8f0"/><path d="M560 322 L560 380" stroke="#4a8a4a" stroke-width="5"/>'
I[179]=svg(b,d)

# 180 Alone (Heart, 1987): a figure at a dark window by a phone, rain streaks, one candle burning, night blue
d,b=bg([(0,'#04061a'),(1,'#141a3a')])
b+='<rect x="200" y="100" width="400" height="460" fill="#1a2a4a"/>'+rain(90,180,'#cfe0ff',.4,4,560)+'<path d="M400 100 L400 560 M200 330 L600 330" stroke="#04061a" stroke-width="14"/><rect x="200" y="100" width="400" height="460" fill="none" stroke="#04061a" stroke-width="20"/>'
b+='<rect y="600" width="800" height="200" fill="#0a0c1a"/>'+figure(400,780,380,'#000',pose='stand',hair='#000')
b+='<rect x="640" y="560" width="22" height="60" fill="#f2e6c8"/>'+glow(651,548,26,'#ffcf6a',.9,'glow2')+'<ellipse cx="651" cy="550" rx="6" ry="12" fill="#ffe08a"/>'
I[180]=svg(b,d)

# 181 My Prerogative (Bobby Brown, 1989): a new-jack-swing dancer in a high-top fade and baggy pants doing a sharp kick, graffiti wall
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<rect y="0" width="800" height="560" fill="#5a5a5a"/>'
for k,c in enumerate(('#ff3a3a','#3ad8ff','#ffe14a','#3aff7a')): b+=f'<path d="M{k*200} {200+k%2*80} q60 -80 120 0 t120 0" stroke="{c}" stroke-width="30" fill="none" opacity=".6"/>'
b+='<rect y="560" width="800" height="240" fill="#2a2a2a"/>'
b+=figure(400,740,420,'#0a0a0a',pose='reach')+'<rect x="366" y="300" width="68" height="40" fill="#0a0a0a"/>'
I[181]=svg(b,d)

# 183 Baby Got Back (Sir Mix-a-Lot, 1992): a giant 90s boombox on a pastel pedestal, two big speaker domes and a peach sitting on top
d,b=bg([(0,'#ffd23a'),(1,'#ff8a5a')])
b+='<rect x="140" y="320" width="520" height="280" rx="30" fill="#2a2a34"/><path d="M220 320 L260 240 L540 240 L580 320" stroke="#5a5a6a" stroke-width="16" fill="none"/>'
for x in (260,540): b+=f'<circle cx="{x}" cy="470" r="96" fill="#4a4a58"/><circle cx="{x}" cy="470" r="60" fill="#14141a"/><circle cx="{x}" cy="470" r="18" fill="#6a6a7a"/>'
b+='<rect x="340" y="350" width="120" height="50" rx="6" fill="#3ad8ff" opacity=".8"/>'
b+='<circle cx="380" cy="200" r="50" fill="#ffa070"/><circle cx="430" cy="200" r="50" fill="#ff8a5a"/><path d="M405 152 Q420 120 450 120" stroke="#2a6a2a" stroke-width="8" fill="none"/>'
I[183]=svg(b,d)

# 186 You Were Meant for Me (Jewel, 1997): a diner booth at morning with pancakes and a coffee cup, a lone girl's guitar leaning on the seat
d,b=bg([(0,'#c8e0e8'),(1,'#f6efe0')])
b+='<rect x="0" y="100" width="800" height="300" fill="#fbf6e8"/><rect x="100" y="140" width="600" height="200" fill="#bfe0f0"/>'
b+='<rect x="0" y="440" width="800" height="40" fill="#c8102a"/><rect x="60" y="480" width="680" height="320" fill="#e8e0d0"/>'
b+='<ellipse cx="340" cy="520" rx="120" ry="30" fill="#fff"/><ellipse cx="340" cy="505" rx="90" ry="20" fill="#d8a050"/><ellipse cx="340" cy="492" rx="90" ry="20" fill="#e8b860"/><rect x="320" y="470" width="30" height="12" fill="#fff2a0"/>'
b+='<path d="M500 450 L580 450 L570 540 L510 540Z" fill="#fff"/><ellipse cx="540" cy="452" rx="40" ry="8" fill="#5a2a10"/>'+guitar(680,560,110,'#c8843a','#4a2a14',-14)
I[186]=svg(b,d)

# 187 The Boy Is Mine (Brandy & Monica, 1998): two women in profile facing off with a man's silhouette in a framed photo between them
d,b=bg([(0,'#1a1a3a'),(1,'#6a3a7a')])
b+='<rect x="320" y="240" width="160" height="200" fill="#e8c06a"/><rect x="334" y="254" width="132" height="172" fill="#3a3a5a"/>'+figure(400,420,150,'#0a0a1a',pose='stand')
b+=profile(140,440,1.4,'#0a0618')+f'<g transform="translate(800 0) scale(-1 1)">{profile(140,440,1.4,"#0a0618")}</g>'
b+='<path d="M410 520 L380 580 L410 580 L385 640" stroke="#ff3a7a" stroke-width="10" fill="none" stroke-linejoin="round"/>'
I[187]=svg(b,d)

# 188 Foolish (Ashanti, 2002): a woman alone at a vanity mirror with a single tear, a wilted bouquet, warm sepia lamplight
d,b=bg([(0,'#2a1a10'),(1,'#7a5a3a')])
b+='<ellipse cx="400" cy="330" rx="170" ry="210" fill="#c8a06a"/><ellipse cx="400" cy="330" rx="150" ry="190" fill="#e8d8c0"/>'+glow(400,330,120,'#fff2d8',.4)
b+=profile(330,350,1.1,'#5a3a2a')+'<path d="M378 360 l-4 30" stroke="#9ad0ff" stroke-width="5" stroke-linecap="round"/>'
b+='<rect y="560" width="800" height="240" fill="#3a2414"/>'
b+='<path d="M600 560 Q620 500 640 480 M600 560 Q600 500 580 470" stroke="#5a6a2a" stroke-width="5" fill="none"/><circle cx="640" cy="490" r="16" fill="#8a3a4a"/><circle cx="578" cy="480" r="14" fill="#8a3a4a"/>'
I[188]=svg(b,d)

# 190 Burn (Usher, 2004): a love letter and photo curling in flames, embers rising into a dark room
d,b=bg([(0,'#0a0402'),(1,'#2a0a04')])
b+=glow(400,520,200,'#ff6a1a',.5)
b+='<g transform="translate(400 520) rotate(8)"><rect x="-150" y="-110" width="300" height="220" fill="#f6efe0"/><path d="M-150 60 Q-80 20 0 70 Q80 30 150 70 L150 110 L-150 110Z" fill="#1a0a04"/></g>'
for k in range(9): x=280+k*30;b+=f'<path d="M{x} 620 Q{x-20} 540 {x} 470 Q{x+20} 520 {x+12} 620Z" fill="{["#ff6a1a","#ffd23a"][k%2]}" opacity=".9"/>'
r=random.Random(190)
for k in range(30): b+=f'<circle cx="{r.uniform(240,560):.0f}" cy="{r.uniform(100,440):.0f}" r="{r.uniform(2,5):.1f}" fill="#ffb04a" opacity="{r.uniform(.4,1):.2f}"/>'
I[190]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
