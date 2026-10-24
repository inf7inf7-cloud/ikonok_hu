import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 9. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 229 Hot in Herre (Nelly, 2002): a sweltering St. Louis block party, a thermometer bursting past red, heat waves rising
d,b=bg([(0,'#ff6a1a'),(1,'#ffd23a')])
for k in range(10): b+=f'<path d="M{k*90} 800 Q{k*90+30} 600 {k*90} 400 Q{k*90-30} 200 {k*90} 0" stroke="#fff2c0" stroke-width="6" fill="none" opacity=".2"/>'
b+='<rect x="350" y="120" width="100" height="480" rx="50" fill="#fbf6f0" stroke="#5a2a0a" stroke-width="8"/><circle cx="400" cy="620" r="80" fill="#e0102a" stroke="#5a2a0a" stroke-width="8"/><rect x="380" y="140" width="40" height="480" rx="20" fill="#e0102a"/>'
for k in range(8): b+=f'<path d="M450 {180+k*50} l30 0" stroke="#5a2a0a" stroke-width="6"/>'
b+=sparkle(400,110,30,'#fff')
I[229]=svg(b,d)

# 230 If I Ain't Got You (Alicia Keys, 2004): hands on a grand piano's keys, a single rose in a vase on the lid, warm amber spotlight
d,b=bg([(0,'#1a0a04'),(1,'#4a2410')])
b+=spotlight(400,0,240,'#ffd8a0',.18)
b+='<rect x="0" y="480" width="800" height="320" fill="#060302"/><rect x="40" y="540" width="720" height="100" fill="#fbf8f0"/>'+''.join(f'<rect x="{70+k*50}" y="540" width="26" height="60" fill="#060302"/>' for k in range(14) if k%7 not in (2,6))
b+='<path d="M220 640 Q260 560 320 590 L340 640Z M480 640 Q520 560 580 590 L600 640Z" fill="#6a3a24"/>'
b+='<path d="M400 480 L400 330" stroke="#2a6a2a" stroke-width="5"/><circle cx="400" cy="320" r="22" fill="#d0102a"/><path d="M380 480 L420 480 L414 400 L386 400Z" fill="#cfe8f0" opacity=".6"/>'
I[230]=svg(b,d)

# 231 Let Me Love You (Mario, 2005): a young man under a streetlight outside a girl's window, holding a single flower up, city night blue
d,b=bg([(0,'#06081a'),(1,'#1a2a4a')])
b+='<rect x="420" y="80" width="340" height="560" fill="#141c30"/><rect x="520" y="200" width="120" height="140" fill="#ffd8a0"/>'+figure(580,340,110,'#3a2a1a',pose='stand',hair='#3a2a1a')
b+='<path d="M140 800 L140 220" stroke="#1a1a24" stroke-width="10"/>'+glow(140,210,60,'#ffe0a0',.8)
b+='<rect y="640" width="800" height="160" fill="#0a0e18"/>'+figure(260,760,300,'#000',pose='wave')+'<circle cx="352" cy="438" r="12" fill="#ff3a7a"/>'
I[231]=svg(b,d)

# 232 The Sweet Escape (Gwen Stefani ft. Akon, 2007): a cartoon birdcage with its door open and a canary flying out into a bright retro-pop sky
d,b=bg([(0,'#ff8ac0'),(1,'#ffe0a0')])
b+='<path d="M400 100 L400 160" stroke="#c8a040" stroke-width="8"/><path d="M260 600 L260 300 Q260 160 400 160 Q540 160 540 300 L540 600Z" fill="none" stroke="#e8c040" stroke-width="8"/>'
for k in range(1,8): b+=f'<path d="M{260+k*35} {600} L{260+k*35} {300-math.sin(k/8*math.pi)*130:.0f}" stroke="#e8c040" stroke-width="5"/>'
b+='<rect x="240" y="590" width="320" height="30" fill="#e8c040"/><path d="M470 340 L540 300 L540 480 L470 520Z" fill="#ff8ac0" stroke="#e8c040" stroke-width="5"/>'
b+='<g transform="translate(620 230)"><ellipse rx="40" ry="28" fill="#ffd21a"/><circle cx="34" cy="-16" r="18" fill="#ffd21a"/><path d="M50 -18 L66 -12 L50 -6Z" fill="#ff8a1a"/><path d="M-10 -10 Q-30 -60 -60 -50 Q-40 -20 -10 0Z" fill="#ffe14a"/></g>'
I[232]=svg(b,d)

# 233 No One (Alicia Keys, 2008): a woman's silhouette at a piano on a rooftop, a sea of city lights glowing violet below
d,b=bg([(0,'#0a0620'),(1,'#3a1a5a')])
b+=skyline(600,'#1a0e30',233,60,200,'#ff9ae8',140)+'<rect y="640" width="800" height="160" fill="#06040e"/>'
b+=glow(400,560,200,'#c8a0ff',.5)+'<path d="M240 680 L520 680 Q580 680 580 640 L560 600 Q480 570 380 580 L250 590Z" fill="#06040e"/>'+figure(320,680,220,'#06040e',pose='hold',hair='#06040e')
I[233]=svg(b,d)

# 234 Just Dance (Lady Gaga ft. Colby O'Donis, 2009): a lightning-bolt disco ball spinning over a house party floor, sparkle sunglasses
d,b=bg([(0,'#1a0a3a'),(1,'#ff3ab0')])
b+=disco(400,260,140)+rays(400,260,26,'#fff',.1,8)
b+='<path d="M420 160 L380 260 L420 260 L380 360" stroke="#ffe14a" stroke-width="14" fill="none" stroke-linejoin="round"/>'
b+='<rect x="220" y="560" width="160" height="80" rx="30" fill="#0a0a14"/><rect x="420" y="560" width="160" height="80" rx="30" fill="#0a0a14"/><path d="M380 590 L420 590" stroke="#0a0a14" stroke-width="12"/>'
for k in range(10): b+=sparkle(240+k*36,600+((k*17)%30)-15,8,'#fff')
I[234]=svg(b,d)

# 235 Hey, Soul Sister (Train, 2010): a ukulele with a heart cutout on a beach towel, sunshine and a mister-mister sunflower
d,b=bg([(0,'#5ac8f0'),(1,'#fff0c0')])
b+='<rect y="460" width="800" height="340" fill="#f6dca0"/><path d="M80 520 L720 480 L740 760 L60 780Z" fill="#ff6a5a"/>'+''.join(f'<path d="M{80+k*0} {540+k*50} L{720} {500+k*50}" stroke="#fff" stroke-width="12" opacity=".7"/>' for k in range(5))
b+='<g transform="translate(400 560) rotate(-30)"><rect x="-12" y="-300" width="24" height="200" fill="#5a3a1a"/><path d="M-60 -60 Q-80 -110 -40 -120 Q0 -100 40 -120 Q80 -110 60 -60 Q90 20 50 70 Q0 100 -50 70 Q-90 20 -60 -60Z" fill="#e8a050"/>'
b+=heart(0,-10,22,'#2a1a0a')+'</g>'+glow(680,130,80,'#fff8d0',.9)
I[235]=svg(b,d)

# 237 Radioactive (Imagine Dragons, 2013): a glowing radioactive green trefoil over a ruined skyline, ash falling
d,b=bg([(0,'#0a140a'),(1,'#2a3a1a')])
b+=glow(400,300,180,'#9aff3a',.4)
for k in range(3): a=math.radians(-90+k*120);b+=f'<path d="M400 300 L{400+150*math.cos(a-0.5):.0f} {300+150*math.sin(a-0.5):.0f} A150 150 0 0 1 {400+150*math.cos(a+0.5):.0f} {300+150*math.sin(a+0.5):.0f}Z" fill="#b6ff3a"/>'
b+='<circle cx="400" cy="300" r="40" fill="#0a140a"/><circle cx="400" cy="300" r="22" fill="#b6ff3a"/>'
b+=skyline(600,'#060a06',237,80,260,None)+'<rect y="660" width="800" height="140" fill="#060a06"/>'+rain(80,237,'#cfd8c0',.3,0)
I[237]=svg(b,d)

# 238 All of Me (John Legend, 2014): a couple's hands with wedding rings resting together on piano keys, black-and-white elegance
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<rect x="0" y="420" width="800" height="380" fill="#fbfbf8"/>'+''.join(f'<rect x="{30+k*60}" y="420" width="32" height="200" fill="#0a0a0a"/>' for k in range(13) if k%7 not in (2,6))
b+='<path d="M120 560 Q260 500 380 530 L420 580 Q300 620 120 640Z" fill="#6a4a3a"/><path d="M680 540 Q540 480 420 520 L400 570 Q520 600 680 620Z" fill="#c89a7a"/>'
b+='<rect x="350" y="530" width="20" height="10" rx="4" fill="#e8c040"/><rect x="430" y="520" width="20" height="10" rx="4" fill="#e8c040"/>'+sparkle(440,505,12,'#fff')
I[238]=svg(b,d)

# 239 See You Again (Wiz Khalifa ft. Charlie Puth, 2015): two sports cars splitting at a fork in a sunset road, white dove above
d,b=bg([(0,'#3a2a5a'),(.6,'#e8805a'),(1,'#f6d0a0')])
b+=glow(400,460,170,'#fff2d0',.8)+hills(500,14,'#4a2a3a',239,4)
b+='<path d="M400 500 L60 800 L240 800 L400 520Z M400 500 L740 800 L560 800 L400 520Z" fill="#2a1e24"/>'
b+='<g transform="translate(240 700) scale(.6)">'+car(0,0,100,'#f2f2f2','#c8c8d0',glass='#3a4a6a')+'</g><g transform="translate(560 700) scale(.6)">'+car(0,0,100,'#3a3a44','#c8c8d0',flip=True,glass='#3a4a6a')+'</g>'
b+=bird(400,220,70,'#fff')
I[239]=svg(b,d)

# 240 That's What I Like (Bruno Mars, 2017): a gold-chain Cadillac and champagne flutes on a penthouse balcony, a bright neon '24K' glow
d,b=bg([(0,'#1a0a3a'),(1,'#d83a8a')])
b+=skyline(560,'#1a0a2a',240,80,220,'#ffd27a',80)+'<rect y="600" width="800" height="200" fill="#0e0618"/>'
b+=neon('24K',400,200,130,'#ffd84a','Arial Black,Arial',False)
for x in (300,500): b+=f'<path d="M{x-20} 420 L{x+20} 420 L{x+6} 500 L{x+6} 560 L{x+20} 570 L{x-20} 570 L{x-6} 560 L{x-6} 500Z" fill="#fff2c0" opacity=".85"/>'
b+='<path d="M290 430 L310 430 L306 480 L294 480Z M490 430 L510 430 L506 480 L494 480Z" fill="#ffd84a"/>'
I[240]=svg(b,d)

# 241 Meant to Be (Bebe Rexha ft. Florida Georgia Line, 2018): a pickup truck on a lakeside dirt road at dusk, string lights and two people on the tailgate
d,b=bg([(0,'#2a3a6a'),(.6,'#e8906a'),(1,'#f2c88a')])
b+='<rect y="480" width="800" height="120" fill="#3a5a8a"/>'+hills(480,14,'#2a2a3a',241,4)+'<rect y="580" width="800" height="220" fill="#3a2a1a"/>'
b+='<path d="M0 200 Q200 260 400 200 Q600 260 800 200" stroke="#2a1a1a" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{k*50}" cy="{230+20*math.sin(k*50/800*2*math.pi*2):.0f}" r="7" fill="#ffe08a"/>' for k in range(17))
b+='<g fill="#1a1414"><path d="M140 680 L140 600 L300 600 L340 540 L460 540 L480 600 L520 600 L520 680Z"/></g>'+''.join(f'<circle cx="{x}" cy="690" r="34" fill="#0a0a0a"/>' for x in (210,450))
b+=figure(180,600,120,'#1a1414',pose='stand',hair='#1a1414')+figure(230,600,130,'#1a1414',pose='stand')
I[241]=svg(b,d)

# 242 Without Me (Halsey, 2019): a girl standing alone in heavy rain under a broken umbrella, deep teal and blue
d,b=bg([(0,'#04141e'),(1,'#1a4a5a')])
b+=rain(220,242,'#bfe8ff',.4,10)+'<rect y="680" width="800" height="120" fill="#06141a"/>'
b+=figure(400,740,340,'#020a0e',pose='hold',hair='#4ad8e8')
b+='<path d="M400 420 L400 300" stroke="#020a0e" stroke-width="8"/><path d="M260 300 Q400 160 540 300 L500 280 L470 310 L430 270 L400 300 L360 266 L320 300Z" fill="#020a0e"/><path d="M460 260 L500 200" stroke="#020a0e" stroke-width="8"/>'
I[242]=svg(b,d)

# 243 The Box (Roddy Ricch, 2020): a cardboard box sitting alone under one spotlight on a dark stage, a car-door 'eee-err' squeak lines
d,b=bg([(0,'#04040a'),(1,'#1a1a24')])
b+=spotlight(400,0,200,'#f2f0e0',.22)
b+='<path d="M260 480 L540 480 L540 680 L260 680Z" fill="#a8783a"/><path d="M260 480 L340 420 L620 420 L540 480Z" fill="#c8985a"/><path d="M540 480 L620 420 L620 620 L540 680Z" fill="#8a5a24"/><path d="M380 480 L460 420" stroke="#d8c8a0" stroke-width="16"/>'
for k in range(3): b+=f'<path d="M{620+k*24} {380-k*14} q20 20 0 40" stroke="#fff" stroke-width="6" fill="none" opacity="{.8-k*.2:.1f}"/>'
I[243]=svg(b,d)

# 244 Kill Bill (SZA, 2023): a vintage pink-and-black film poster style, a katana blade gleaming across a broken heart
d,b=bg([(0,'#ffd23a'),(1,'#ff9a2a')])
b+=heart(400,420,180,'#1a0a0a')+'<path d="M400 290 L370 380 L420 440 L380 520 L400 600" stroke="#ffd23a" stroke-width="10" fill="none"/>'
b+='<g transform="rotate(-30 400 420)"><rect x="100" y="410" width="520" height="16" fill="#e8e8f0"/><rect x="620" y="402" width="20" height="32" fill="#2a1a0a"/><rect x="640" y="410" width="110" height="16" fill="#c8102a"/></g>'
I[244]=svg(b,d)

# 245 Beautiful Things (Benson Boone, 2024): a young man doing a backflip off a stage under glittering golden light, arms wide
d,b=bg([(0,'#1a0a04'),(1,'#5a3a14')])
b+=rays(400,0,22,'#ffd88a',.12,10)+confetti(60,245,['#ffd84a','#fff'],0,600,.7)
b+='<rect y="640" width="800" height="160" fill="#0a0402"/>'
b+='<g transform="translate(400 380) rotate(160)">'+figure(0,150,300,'#0a0402',pose='up')+'</g>'
b+='<path d="M250 600 Q400 420 550 600" stroke="#ffd88a" stroke-width="4" stroke-dasharray="8 12" fill="none" opacity=".6"/>'
I[245]=svg(b,d)

# 249 Crying (Roy Orbison, 1961): a single teardrop on dark sunglasses, rain on a midnight-blue window
d,b=bg([(0,'#04081a'),(1,'#141e3a')])
b+=rain(120,249,'#bfd8ff',.4,4)
for cx in (270,530): b+=f'<path d="M{cx-130} 330 Q{cx} 300 {cx+130} 330 Q{cx+120} 470 {cx} 470 Q{cx-120} 470 {cx-130} 330Z" fill="#000"/><path d="M{cx-90} 350 Q{cx-50} 340 {cx-20} 352" stroke="#fff" stroke-width="5" opacity=".3" fill="none"/>'
b+='<path d="M380 340 Q400 320 420 340" stroke="#000" stroke-width="16" fill="none"/>'
b+='<path d="M300 500 Q280 540 300 570 Q320 540 300 500Z" fill="#9ad8ff"/>'
I[249]=svg(b,d)

# 253 Last Train to Clarksville (The Monkees, 1966): a 60s steam train leaving a little station, a girl waving, sunny pop colors
d,b=bg([(0,'#7ad0f0'),(1,'#f6e8c0')])
b+=hills(520,30,'#6ab04a',253,5)+'<rect y="600" width="800" height="200" fill="#a8885a"/><path d="M0 640 L800 640 M0 680 L800 680" stroke="#5a4a3a" stroke-width="6"/>'
b+='<g><rect x="120" y="500" width="260" height="130" fill="#e0102a"/><rect x="300" y="440" width="80" height="80" fill="#1a1a2a"/><rect x="150" y="450" width="40" height="60" fill="#1a1a2a"/><rect x="380" y="540" width="200" height="90" fill="#1a3aa8"/><rect x="590" y="540" width="200" height="90" fill="#ffd23a"/></g>'
for x in (170,330,440,520,650,730): b+=f'<circle cx="{x}" cy="640" r="24" fill="#1a1a1a"/>'
for k in range(4): b+=f'<circle cx="{170-k*30}" cy="{420-k*40}" r="{24+k*10}" fill="#fff" opacity=".8"/>'
I[253]=svg(b,d)

# 255 (Sittin' On) The Dock of the Bay (Otis Redding, 1968): a man sitting on a wooden dock watching ships roll in at a San Francisco sunset
d,b=bg([(0,'#3a3a6a'),(.6,'#e8905a'),(1,'#f6c88a')])
b+=glow(400,430,160,'#fff2c8',.8)+'<rect y="460" width="800" height="340" fill="#4a5a8a"/>'+''.join(f'<path d="M{k*80} {500+k%3*30} q20 -8 40 0" stroke="#ffd8a0" stroke-width="4" fill="none" opacity=".6"/>' for k in range(10))
b+='<path d="M560 450 L700 450 L680 470 L580 470Z M620 450 L620 400 L660 450Z" fill="#1a1a2a"/>'
b+='<rect x="0" y="560" width="440" height="30" fill="#3a2414"/>'+''.join(f'<rect x="{30+k*100}" y="590" width="20" height="210" fill="#2a180a"/>' for k in range(5))
b+='<g fill="#0a0604"><circle cx="330" cy="490" r="20"/><path d="M314 512 L346 512 L350 560 L310 560Z"/><path d="M346 556 L400 560 L410 620" stroke="#0a0604" stroke-width="16" fill="none"/></g>'
I[255]=svg(b,d)

# 258 Without You (Harry Nilsson, 1972): a lone figure at a dark doorway watching a car's taillights fade into night, an empty bed visible
d,b=bg([(0,'#04040e'),(1,'#1a1a2a')])
b+='<rect x="120" y="140" width="240" height="460" fill="#ffd8a0" opacity=".6"/>'+figure(240,600,300,'#000',pose='stand')
b+='<rect y="600" width="800" height="200" fill="#0a0a12"/>'+road(600,600,'#141420','#3a3a44',300)
b+=glow(580,620,14,'#ff2a2a',.9,'glow2')+glow(620,620,14,'#ff2a2a',.9,'glow2')
I[258]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
