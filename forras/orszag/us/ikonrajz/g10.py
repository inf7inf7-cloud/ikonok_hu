import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 10. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 259 Come and Get Your Love (Redbone, 1974): a 70s Native American-inspired sunburst in turquoise and orange, a feathered dancer silhouette
d,b=bg([(0,'#1a8a8a'),(.6,'#f0a03a'),(1,'#f6d08a')])
b+=rays(400,520,32,'#fff2c0',.18,12)+'<circle cx="400" cy="520" r="120" fill="#ffd23a"/>'
for k in range(5): b+=f'<path d="M0 {640+k*30} L800 {640+k*30}" stroke="{["#1a6a6a","#e0602a","#f6e0a0"][k%3]}" stroke-width="16"/>'
b+=figure(400,780,360,'#2a1008',pose='up')+''.join(f'<path d="M{380+k*10} 440 L{370+k*12} 380" stroke="#2a1008" stroke-width="8" stroke-linecap="round"/>' for k in range(5))
I[259]=svg(b,d)

# 262 Evergreen (Barbra Streisand, 1977): an evergreen pine glowing in soft spotlight with a single long-stem rose leaning on it, film-star gold
d,b=bg([(0,'#0a1a14'),(1,'#2a4a3a')])
b+=spotlight(400,0,240,'#fff2c8',.2)
for k in range(5): w=60+k*50;y=160+k*80;b+=f'<path d="M400 {y-40} L{400+w} {y+60} L{400-w} {y+60}Z" fill="#1a5a3a"/>'
b+='<rect x="380" y="560" width="40" height="80" fill="#3a2a1a"/>'+star5(400,130,26,'#ffd84a')
b+='<path d="M520 700 L600 420" stroke="#2a6a2a" stroke-width="6"/><circle cx="600" cy="410" r="22" fill="#d0102a"/>'
I[262]=svg(b,d)

# 263 Rock with You (Michael Jackson, 1980): a disco dancer in a sparkling sequin suit beneath a starfield of lasers
d,b=bg([(0,'#04040e'),(1,'#1a0a3a')])
for k in range(14): b+=f'<path d="M400 120 L{k*60} 800" stroke="#9ad8ff" stroke-width="2" opacity=".35"/>'
b+=glow(400,120,40,'#fff',.9)+figure(400,780,440,'#c8c8d8',pose='wave')
r=random.Random(263)
for k in range(40): b+=f'<circle cx="{r.uniform(360,440):.0f}" cy="{r.uniform(460,780):.0f}" r="3" fill="#fff"/>'
I[263]=svg(b,d)

# 264 Footloose (Kenny Loggins, 1984): red sneakers kicking up dust on a barn dance floor, hay bales and warm Midwest light
d,b=bg([(0,'#7a3a1a'),(1,'#d89a4a')])
b+='<path d="M120 800 L120 200 L400 60 L680 200 L680 800Z" fill="#5a2010"/><path d="M200 800 L200 320 L600 320 L600 800Z" fill="#ffd27a" opacity=".5"/>'
b+='<rect y="640" width="800" height="160" fill="#8a5a2a"/>'
for x,y,a in ((330,560,-20),(470,600,15)): b+=f'<g transform="translate({x} {y}) rotate({a})"><path d="M-70 20 Q-70 -30 -20 -30 L40 -40 Q80 -40 80 0 L80 20Z" fill="#d0102a"/><rect x="-74" y="16" width="158" height="16" rx="6" fill="#fff"/></g>'
for k in range(12): b+=f'<circle cx="{300+k*20}" cy="{640+((k*13)%30)}" r="{6+k%3*4}" fill="#e8c890" opacity=".6"/>'
I[264]=svg(b,d)

# 265 I Want to Know What Love Is (Foreigner, 1985): a gospel choir's silhouettes in white robes under a cathedral rose window
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a3a')])
b+='<circle cx="400" cy="230" r="150" fill="#3a2a5a"/>'+''.join(f'<path d="M400 230 L{400+150*math.cos(k*0.524):.0f} {230+150*math.sin(k*0.524):.0f}" stroke="#0a0a1a" stroke-width="8"/>' for k in range(12))
for k,c in enumerate(('#ff4a6a','#4ad8ff','#ffd84a','#7a4aff')): b+=f'<circle cx="{400+80*math.cos(k*1.57+.78):.0f}" cy="{230+80*math.sin(k*1.57+.78):.0f}" r="40" fill="{c}" opacity=".6"/>'
b+=glow(400,230,160,'#c8a0ff',.3)
for row in range(2):
    for k in range(7): b+=figure(100+k*100+row*50,800-row*60,220,'#f2eef8' if row else '#d8d0e8',pose='stand')
I[265]=svg(b,d)

# 266 On My Own (Patti LaBelle & Michael McDonald, 1986): a split-screen of two people on telephones in separate apartments, a line dividing them
d,b=bg([(0,'#3a1a3a'),(1,'#8a5a7a')])
b+='<rect x="0" y="0" width="396" height="800" fill="#2a1a4a"/><rect x="404" y="0" width="396" height="800" fill="#4a2a2a"/>'
b+='<rect x="80" y="120" width="220" height="260" fill="#6a5aa8" opacity=".5"/><rect x="500" y="120" width="220" height="260" fill="#c88a5a" opacity=".5"/>'
b+=figure(200,760,360,'#0a0618',pose='stand',hair='#0a0618')+figure(600,760,380,'#180a06',pose='stand')
b+='<rect x="396" y="0" width="8" height="800" fill="#f2e6d8"/>'
I[266]=svg(b,d)

# 267 I Wanna Dance with Somebody (Whitney Houston, 1987): a joyful woman with big curls dancing in a bright pastel 80s set with confetti
d,b=bg([(0,'#ff8ac0'),(1,'#9ae0ff')])
b+=confetti(90,267,['#ffd23a','#fff','#7a4aff','#ff3a6a'],0,800,.9)
b+='<circle cx="400" cy="300" r="80" fill="#3a1a0a"/>'+''.join(f'<circle cx="{400+70*math.cos(k*.45):.0f}" cy="{300+70*math.sin(k*.45):.0f}" r="30" fill="#3a1a0a"/>' for k in range(14))
b+=figure(400,780,480,'#2a0a2a',pose='up')
I[267]=svg(b,d)

# 268 Straight Up (Paula Abdul, 1989): a black-and-white tap-dance spotlight, a dancer in a bowler hat mid-spin, sharp shadows
d,b=bg([(0,'#0a0a0a'),(1,'#2a2a2a')])
b+=spotlight(400,0,200,'#ffffff',.25)+'<ellipse cx="400" cy="720" rx="180" ry="30" fill="#fff" opacity=".25"/>'
b+=figure(400,720,420,'#000',pose='reachL',hair='#000')+'<path d="M370 340 Q400 300 430 340Z" fill="#000"/><rect x="360" y="336" width="80" height="8" rx="4" fill="#000"/>'
I[268]=svg(b,d)

# 269 Poison (Bell Biv DeVoe, 1990): a glowing green poison bottle with a skull label and a woman's silhouette reflected in it, neon black
d,b=bg([(0,'#04060a'),(1,'#0a1a14')])
b+=glow(400,460,180,'#3aff7a',.4)
b+='<path d="M360 200 L440 200 L440 280 Q560 320 560 460 Q560 640 400 660 Q240 640 240 460 Q240 320 360 280Z" fill="#1a8a3a" opacity=".85" stroke="#9affb0" stroke-width="5"/><rect x="350" y="160" width="100" height="44" rx="8" fill="#3a2a1a"/>'
b+='<rect x="300" y="420" width="200" height="140" rx="12" fill="#f2f0e6"/><circle cx="400" cy="475" r="34" fill="#111"/><circle cx="388" cy="470" r="8" fill="#f2f0e6"/><circle cx="412" cy="470" r="8" fill="#f2f0e6"/><path d="M360 530 L440 510 M360 510 L440 530" stroke="#111" stroke-width="8"/>'
I[269]=svg(b,d)

# 270 Rush Rush (Paula Abdul, 1991): a vintage James-Dean-style convertible at a drive-in, a young couple in it under a starry sky
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
b+=starsf(80,270,500)+'<rect x="180" y="100" width="440" height="260" fill="#f2f0e6" opacity=".85"/><rect x="380" y="360" width="40" height="200" fill="#1a1a2a"/>'
b+='<rect y="600" width="800" height="200" fill="#0a0e18"/>'+car(400,740,150,'#c8102a','#e8e8ee',glass='#3a4a6a')
b+='<g fill="#0a0e18"><circle cx="370" cy="580" r="18"/><circle cx="430" cy="576" r="18"/></g>'
I[270]=svg(b,d)

# 271 Save the Best for Last (Vanessa Williams, 1992): a heart-shaped box of chocolates with one golden truffle left in the middle
d,b=bg([(0,'#5a0a1a'),(1,'#c83a4a')])
b+=heart(400,420,190,'#d0102a','stroke="#f2c0c8" stroke-width="10"')+heart(400,420,150,'#3a0a10')
r=[(330,330),(470,330),(290,420),(510,420),(350,500),(450,500),(400,580)]
for x,y in r: b+=f'<circle cx="{x}" cy="{y}" r="30" fill="#f2e6d8" opacity=".15"/>'
b+='<circle cx="400" cy="420" r="36" fill="#e8b830"/>'+sparkle(420,396,14,'#fff')
I[271]=svg(b,d)

# 272 That's the Way Love Goes (Janet Jackson, 1993): a relaxed loft party at golden hour, a woman in a crop top and baggy jeans leaning back, warm haze
d,b=bg([(0,'#7a4a2a'),(1,'#f0b06a')])
b+='<rect x="80" y="80" width="300" height="400" fill="#ffe0a0" opacity=".6"/><rect x="420" y="80" width="300" height="400" fill="#ffe0a0" opacity=".6"/>'+glow(400,280,240,'#fff2c0',.4)
b+='<rect y="560" width="800" height="240" fill="#5a3218"/><path d="M200 560 Q200 480 300 480 L520 480 Q600 480 600 560Z" fill="#8a4a2a"/>'
b+=figure(400,560,260,'#2a1408',pose='stand',hair='#2a1408')
I[272]=svg(b,d)

# 274 Un-Break My Heart (Toni Braxton, 1997): a cracked heart being stitched together with gold thread on dark velvet
d,b=bg([(0,'#0a0410'),(1,'#2a0a2a')])
b+=heart(400,420,190,'#a0102a')+'<path d="M400 260 L370 360 L420 430 L380 520 L400 600" stroke="#0a0410" stroke-width="10" fill="none"/>'
for k in range(6): y=300+k*50;b+=f'<path d="M{375} {y} L{425} {y+14}" stroke="#ffd84a" stroke-width="5"/>'
b+=glow(400,420,200,'#ff4a6a',.2)
I[274]=svg(b,d)

# 275 Heartbreak Hotel (Whitney Houston ft. Faith Evans & Kelly Price, 1999): a sleek 90s hotel corridor, a room-key card and a 'do not disturb' sign, purple
d,b=bg([(0,'#1a0a2a'),(1,'#4a1a5a')])
b+='<path d="M0 0 L300 280 L300 520 L0 800Z M800 0 L500 280 L500 520 L800 800Z" fill="#2a1438"/><rect x="300" y="280" width="200" height="240" fill="#0a0414"/>'
for k in range(4): b+=f'<rect x="{30+k*60}" y="{200+k*40}" width="40" height="{400-k*80}" fill="#3a2048" transform="skewY({ 40-k*0})"/>'
b+='<rect x="460" y="430" width="200" height="120" rx="12" fill="#e8e0f0" transform="rotate(-12 560 490)"/><rect x="480" y="480" width="160" height="16" fill="#d0102a" transform="rotate(-12 560 490)"/>'+heart(400,380,30,'#ff3a7a','opacity=".8"')
I[275]=svg(b,d)

# 276 I Wanna Know (Joe, 2000): a man in a white linen suit by a candlelit pool at night, smooth R&B blue
d,b=bg([(0,'#04081a'),(1,'#0a2a4a')])
b+='<rect y="520" width="800" height="280" fill="#1a6ab0"/>'+''.join(f'<path d="M{k*80} {560+k%3*40} q20 -8 40 0" stroke="#9ad8ff" stroke-width="4" fill="none" opacity=".6"/>' for k in range(10))
for x in (120,240,560,680): b+=f'<rect x="{x-8}" y="490" width="16" height="36" fill="#f2e6c8"/>'+glow(x,482,18,'#ffcf6a',.9,'glow2')
b+=figure(400,520,300,'#f6f2ee',pose='stand')+'<ellipse cx="400" cy="262" rx="18" ry="22" fill="#2a1408"/>'
I[276]=svg(b,d)

# 277 Drops of Jupiter (Train, 2001): a woman drifting back from space trailing stars past Jupiter's stripes and the Milky Way
d,b=bg([(0,'#04040e'),(1,'#1a0a2a')])
b+=starsf(160,277,800)
b+='<circle cx="560" cy="300" r="160" fill="#d8a06a"/>'+''.join(f'<path d="M400 {200+k*30} Q560 {180+k*30} 720 {200+k*30}" stroke="{["#a8603a","#f2d0a0"][k%2]}" stroke-width="14" fill="none" opacity=".7"/>' for k in range(7))
b+='<ellipse cx="620" cy="360" rx="30" ry="18" fill="#a0402a"/>'
b+='<g transform="translate(240 520) rotate(-30)">'+figure(0,100,220,'#f2eef8',pose='up',hair='#f2eef8')+'</g>'
for k in range(12): b+=sparkle(120+k*10,700-k*8,6,'#fff')
I[277]=svg(b,d)

# 278 Dilemma (Nelly ft. Kelly Rowland, 2002): two figures on facing porches across a sunny suburban street, a heart dangling between
d,b=bg([(0,'#7ac8f0'),(1,'#f6e0c0')])
b+='<rect y="560" width="800" height="240" fill="#6a6a6a"/><rect y="600" width="800" height="10" fill="#f2f2f2"/>'
for x,f in ((140,1),(660,-1)): b+=f'<path d="M{x-120} 560 L{x-120} 340 L{x} 260 L{x+120} 340 L{x+120} 560Z" fill="{["#f2e0c8","#c8d8e8"][f>0]}"/><rect x="{x-30}" y="440" width="60" height="120" fill="#5a3a24"/>'
b+=figure(250,560,200,'#2a1408',pose='stand')+figure(550,560,190,'#2a1408',pose='stand',hair='#2a1408')
b+='<path d="M250 300 Q400 360 550 300" stroke="#c8102a" stroke-width="3" fill="none"/>'+heart(400,350,30,'#e0102a')
I[278]=svg(b,d)

# 279 This Love (Maroon 5, 2004): a pair of hands holding a falling broken photo strip in a dark room lit by a red neon heart
d,b=bg([(0,'#0a0404'),(1,'#2a0a0a')])
b+=heart(400,300,120,'none','stroke="#ff2a3a" stroke-width="14"')+glow(400,300,140,'#ff2a3a',.3)
for k in range(4): b+=f'<g transform="rotate({-10+k*8} 400 600)"><rect x="330" y="{450+k*75}" width="140" height="70" fill="#f2f0e8"/><rect x="340" y="{458+k*75}" width="120" height="54" fill="#3a2a2a"/></g>'
I[279]=svg(b,d)

# 280 Big Girls Don't Cry (Fergie, 2007): a girl with a suitcase walking away down a sunny dirt road, a mascara tear on a fallen photo
d,b=bg([(0,'#7ab0e0'),(1,'#f6e8d0')])
b+=hills(520,30,'#9ac06a',280,5)+road(400,520,'#c8a070','#c8a070',400)
b+=figure(400,640,170,'#2a1a14',pose='stand',hair='#c8a040')+'<rect x="420" y="590" width="50" height="40" rx="6" fill="#a83a2a"/>'
b+='<g transform="translate(200 700) rotate(-14)"><rect x="-70" y="-50" width="140" height="100" fill="#fff"/><rect x="-60" y="-40" width="120" height="70" fill="#8ab0d8"/></g>'
I[280]=svg(b,d)

# 281 Lollipop (Lil Wayne, 2008): a giant swirl lollipop on a stick in purple and pink, a sparkle and a grill-glint
d,b=bg([(0,'#3a0a5a'),(1,'#ff6ac0')])
b+='<rect x="390" y="440" width="20" height="360" fill="#fbf6f0"/>'
p='M400 300 '+' '.join(f'L{400+t*0.9*math.cos(t/14):.0f} {300+t*0.9*math.sin(t/14):.0f}' for t in range(1,190))
b+='<circle cx="400" cy="300" r="180" fill="#ff3aa8"/>'+f'<path d="{p}" stroke="#fff" stroke-width="22" fill="none"/>'+sparkle(520,180,26,'#fff')
I[281]=svg(b,d)

# 282 I Gotta Feeling (The Black Eyed Peas, 2009): a night-out countdown: a giant clock at 'tonight', champagne fountain and confetti over a crowd
d,b=bg([(0,'#0a0a2a'),(1,'#3a1a6a')])
b+=firework(200,180,110,'#ffd84a',seed=4)+firework(620,160,120,'#ff4ab0',seed=5)
b+=confetti(60,282,['#ffd84a','#4ad8ff','#fff'],0,600,.8)
for k in range(16): b+=f'<g transform="translate({k*52+20} {760-(k%2)*20})">'+figure(0,0,150,'#04040e',pose='up' if k%3 else 'wave')+'</g>'
I[282]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
