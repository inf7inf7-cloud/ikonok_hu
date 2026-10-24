import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 12. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def lips(x,y,s,c1='#e8102a',c2='#c80a20'): return f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 0 Q-60 -60 -10 -30 Q0 -40 10 -30 Q60 -60 110 0 Q60 14 0 8 Q-60 14 -110 0Z" fill="{c1}"/><path d="M-110 6 Q-60 20 0 14 Q60 20 110 6 Q60 80 0 74 Q-60 80 -110 6Z" fill="{c2}"/></g>'
def wings(x,y,s,col='#fff',st='#d8e0ec'): return ''.join(f'<path d="M{x+f*20*s:.0f} {y} Q{x+f*(120+k*24)*s:.0f} {y-(100-k*30)*s:.0f} {x+f*(220-k*10)*s:.0f} {y-(60-k*44)*s:.0f} Q{x+f*(140+k*16)*s:.0f} {y-(20-k*30)*s:.0f} {x+f*20*s:.0f} {y+30*s:.0f}Z" fill="{col}" stroke="{st}" stroke-width="3"/>' for f in (1,-1) for k in range(3))

# 605 今すぐKiss Me: a telephone booth glowing pink in the rain at night, lipstick kiss pressed on its glass
d,b=bg([(0,'#1a1a3a'),(1,'#2a1a3a')])
b+=rain(80,605,'#c8b8e8',.4,6)+'<rect y="660" width="800" height="140" fill="#14101e"/>'
b+=glow(400,420,220,'#ff5ab8',.35)+'<rect x="260" y="140" width="280" height="540" rx="10" fill="#e8302a"/><rect x="290" y="210" width="220" height="440" fill="#ffd0ec"/><rect x="290" y="160" width="220" height="40" fill="#fff"/>'
b+='<path d="M290 430 L510 430 M400 210 L400 650" stroke="#e8302a" stroke-width="10"/>'+lips(450,320,.35)+'<ellipse cx="400" cy="680" rx="200" ry="14" fill="#ff5ab8" opacity=".3"/>'
I[605]=svg(b,d)

# 1106 LAST CHRISTMAS: a lone Christmas tree twinkling in a snowy square, a single present left unopened beneath it
d,b=bg([(0,'#0a1438'),(1,'#1a2a5a')])
b+=snow(80,1106)+'<rect y="640" width="800" height="160" fill="#e8eef8"/>'
for k in range(4): w=260-k*56;y=620-k*110;b+=f'<path d="M{400-w} {y} L400 {y-170} L{400+w} {y}Z" fill="#1a6a3a"/>'
b+=star5(400,180,40,'#ffe05a')+glow(400,180,60,'#ffe05a',.6)
r=R(1106)
for _ in range(24): y=r.uniform(240,600);x=400+r.uniform(-1,1)*(y-180)*.55;b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="{r.choice(["#ffd27a","#ff5a5a","#5ab8ff","#fff"])}"/>'
b+='<rect x="380" y="620" width="40" height="40" fill="#5a3a1a"/><rect x="460" y="600" width="80" height="60" fill="#e8102a"/><path d="M500 600 L500 660 M460 630 L540 630" stroke="#ffd02a" stroke-width="8"/>'
I[1106]=svg(b,d)

# 1219 Daylight: a sunbeam piercing through a crack in a dark wall, lighting a small potted plant
d,b=bg([(0,'#1a1a1e'),(1,'#2a2a30')])
b+='<polygon points="560,0 610,0 470,800 200,800" fill="#fff6d8" opacity=".25"/>'+bolt([(570,0),(590,60),(570,110),(600,180)],'#fff6d8',8,1)
b+='<rect x="300" y="620" width="120" height="100" fill="#c8704a"/><path d="M360 620 Q340 520 300 480 M360 620 Q380 500 440 470 M360 620 Q360 520 370 440" stroke="#3a8a2a" stroke-width="8" fill="none"/>'
b+='<ellipse cx="300" cy="476" rx="30" ry="14" fill="#5ac84a"/><ellipse cx="444" cy="466" rx="30" ry="14" fill="#5ac84a"/><ellipse cx="370" cy="436" rx="20" ry="30" fill="#5ac84a"/>'+glow(360,560,180,'#fff6d8',.25)
I[1219]=svg(b,d)

# 1412 Heartache: a glowing red heart wrapped in stitched bandages, a needle and thread hanging off it
d,b=bg([(0,'#1a0a14'),(1,'#2a0a1a')])
b+=glow(400,420,240,'#ff2a4a',.35)+heart(400,420,180,'#c80a2a')
for y,a in [(360,-14),(460,10)]: b+=f'<rect x="230" y="{y}" width="340" height="44" fill="#f4ecd8" transform="rotate({a} 400 {y})"/>'
b+='<path d="M560 300 L600 260 L640 240" stroke="#c8c8d8" stroke-width="5"/><path d="M640 240 Q700 300 660 400 Q620 480 560 470" stroke="#e8102a" stroke-width="3" fill="none"/>'
b+=''.join(f'<path d="M{330+k*30} 520 L{340+k*30} 545" stroke="#1a0a0a" stroke-width="4"/>' for k in range(6))
I[1412]=svg(b,d)

# 1503 Same Blue: two kids on a summer school rooftop looking up at the same endless blue sky, one pointing
d,b=bg([(0,'#0a7ae8'),(1,'#8ad0ff')])
b+=cloud(200,200,1.4)+cloud(620,140,1.0)+'<rect y="560" width="800" height="240" fill="#c8c8d0"/><path d="M-10 560 L810 560" stroke="#8a8a94" stroke-width="8"/>'+''.join(f'<path d="M{x} 560 L{x} 480" stroke="#8a8a94" stroke-width="6"/>' for x in range(20,800,60))+'<path d="M-10 490 L810 490" stroke="#8a8a94" stroke-width="6"/>'
b+=figure(340,700,200,'#1a2a4a',pose='up')+figure(460,700,190,'#1a2a4a',hair='#1a2a4a')
I[1503]=svg(b,d)

# 1537 ピーターパン: a boy's silhouette flying past a clock tower against a giant moon, a trail of fairy dust behind
d,b=bg([(0,'#0a1438'),(1,'#2a2a5a')])
b+=moon(460,300,190,'#fff6d8')+glow(460,300,240,'#fff6d8',.25)+starsf(40,1537,800,'#fff')
b+='<rect x="80" y="300" width="120" height="500" fill="#0a0e20"/><path d="M70 300 L140 200 L210 300Z" fill="#0a0e20"/><circle cx="140" cy="380" r="40" fill="#fff6d8"/><path d="M140 380 L140 350 M140 380 L160 390" stroke="#0a0e20" stroke-width="5"/>'
b+='<path d="M200 520 Q330 440 420 330" stroke="#ffe8a0" stroke-width="4" fill="none" stroke-dasharray="3 10"/><g transform="rotate(60 460 320)">'+figure(460,400,160,'#0a0e20',pose='up')+'</g>'
I[1537]=svg(b,d)

# 211 心の旅: a steam train pulling away across a long bridge at dawn, a hand waving from its window
d,b=bg([(0,'#5a6aa8'),(.6,'#ffb88a'),(1,'#ffe0b0')])
b+=hinomaru_sun(560,440,90,'#fff4d0',.8)+'<rect y="500" width="800" height="300" fill="#4a6a8a"/>'
b+='<rect x="-10" y="400" width="820" height="20" fill="#2a2a34"/>'+''.join(f'<path d="M{k*120} 420 Q{k*120+60} 480 {k*120+120} 420 L{k*120+120} 520 L{k*120} 520Z" fill="none" stroke="#2a2a34" stroke-width="10"/>' for k in range(7))
b+='<rect x="120" y="320" width="420" height="80" rx="8" fill="#1a1a24"/><rect x="460" y="270" width="40" height="50" fill="#1a1a24"/>'+''.join(f'<rect x="{150+k*80}" y="336" width="50" height="30" fill="#ffd27a"/>' for k in range(4))
b+=''.join(f'<circle cx="{480-k*50}" cy="{240-k*30}" r="{30+k*10}" fill="#fff" opacity="{.7-k*.1:.1f}"/>' for k in range(5))+'<path d="M180 336 L170 300" stroke="#1a1a24" stroke-width="8" stroke-linecap="round"/>'
I[211]=svg(b,d)

# 357 夏の扉: a door opening onto a dazzling summer beach, a swim ring hanging on its handle
d,b=bg([(0,'#ffd8e0'),(1,'#ffc0d0')])
b+='<rect x="230" y="140" width="340" height="560" fill="#3ab8f8"/><rect x="230" y="420" width="340" height="140" fill="#1a90d8"/><rect x="230" y="560" width="340" height="140" fill="#f8e0a0"/><circle cx="480" cy="250" r="50" fill="#fff8d0"/>'
b+='<path d="M230 140 L130 190 L130 720 L230 700Z" fill="#fff"/><rect x="230" y="140" width="340" height="560" fill="none" stroke="#fff" stroke-width="20"/>'
b+=ring(170,450,60,'#ff5a7a',30)+''.join(f'<path d="M{170+60*math.cos(math.radians(a)):.0f} {450+60*math.sin(math.radians(a)):.0f} l{12*math.cos(math.radians(a)):.0f} {12*math.sin(math.radians(a)):.0f}" stroke="#fff" stroke-width="20"/>' for a in (0,90,180,270))
I[357]=svg(b,d)

# 648 Liar! Liar!: a wooden puppet's nose growing long into a forked road sign, under a dramatic red spotlight
d,b=bg([(0,'#3a0a0a'),(1,'#1a0404')])
b+='<polygon points="300,-20 140,800 500,800" fill="#ff3a3a" opacity=".12"/>'
b+='<circle cx="300" cy="400" r="120" fill="#d8a060"/><circle cx="260" cy="370" r="14" fill="#1a1a1a"/><path d="M240 450 Q280 480 320 450" stroke="#1a1a1a" stroke-width="8" fill="none"/>'
b+='<path d="M380 400 L720 340 L724 360 L384 420Z" fill="#d8a060"/><path d="M600 360 L680 290 M640 350 L740 400" stroke="#d8a060" stroke-width="12" stroke-linecap="round"/><path d="M640 280 L700 300 L690 320 L630 300Z" fill="#f4e8d0"/>'
b+='<path d="M220 300 Q300 240 380 300" stroke="#5a3a1a" stroke-width="20" fill="none"/>'
I[648]=svg(b,d)

# 938 スワンソング: a white swan gliding alone across a silver lake at dusk, one feather drifting behind
d,b=bg([(0,'#8a8ab8'),(.6,'#e8c0c8'),(1,'#f4e0e0')])
b+='<rect y="460" width="800" height="340" fill="#a8b0d0"/>'+''.join(f'<rect x="{200+k*40}" y="{500+k*30}" width="{200-k*20}" height="4" fill="#fff" opacity=".5"/>' for k in range(6))
b+='<path d="M260 560 Q300 500 400 500 Q520 500 560 460 Q540 560 440 580 Q320 590 260 560Z" fill="#fff"/><path d="M300 520 Q260 400 300 300 Q330 260 360 300" stroke="#fff" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M360 296 L400 310 L360 314Z" fill="#ff8a2a"/><circle cx="346" cy="294" r="5" fill="#1a1a1a"/>'
b+='<path d="M260 580 Q400 620 560 580" fill="#fff" opacity=".3"/><path d="M640 360 Q660 380 650 420 Q630 400 640 360Z" fill="#fff"/>'
I[938]=svg(b,d)

# 1400 Snow Magic Fantasy: a snow globe holding a tiny glowing castle, snowflakes swirling in a magic spiral
d,b=bg([(0,'#1a2a6a'),(1,'#3a4a9a')])
b+=snow(50,1400)
b+='<circle cx="400" cy="360" r="230" fill="#bfe8ff" opacity=".25" stroke="#fff" stroke-width="6"/><path d="M220 560 Q400 620 580 560 L620 680 L180 680Z" fill="#5a3a7a"/>'
b+='<path d="M300 520 L300 380 L330 340 L360 380 L360 420 L440 420 L440 380 L470 340 L500 380 L500 520Z" fill="#f4f0ff"/><path d="M380 420 L400 300 L420 420Z" fill="#f4f0ff"/>'+glow(400,450,80,'#ffd27a',.5)+'<rect x="385" y="460" width="30" height="60" rx="15" fill="#ffd27a"/>'
for k in range(14): a=k*.6;r_=40+k*12;b+=f'<circle cx="{400+r_*math.cos(a):.0f}" cy="{360+r_*.6*math.sin(a):.0f}" r="6" fill="#fff"/>'
I[1400]=svg(b,d)

# 1548 踊: a crowd of paper lanterns spinning wildly around a central drum, red and black streamers whipping in the night
d,b=bg([(0,'#0a0404'),(1,'#2a0a0a')])
b+=glow(400,420,260,'#e8102a',.35)
for k in range(8):
    a=math.radians(k*45);x=400+260*math.cos(a);y=420+200*math.sin(a)
    b+=f'<path d="M400 420 Q{400+150*math.cos(a+.6):.0f} {420+150*math.sin(a+.6):.0f} {x:.0f} {y:.0f}" stroke="{["#e8102a","#1a1a1a"][k%2]}" stroke-width="18" fill="none"/>'+chochin(x,y,44)
b+='<ellipse cx="400" cy="420" rx="90" ry="90" fill="#8a2a1a"/><circle cx="400" cy="420" r="70" fill="#f4e8d8"/>'+tomoe(400,420,40) if 'tomoe' in dir() else '<ellipse cx="400" cy="420" rx="90" ry="90" fill="#8a2a1a"/><circle cx="400" cy="420" r="70" fill="#f4e8d8"/><path d="M380 400 Q400 380 420 400 Q420 440 380 440Z" fill="#e8102a"/>'
I[1548]=svg(b,d)

# 1847 いつか: a dog-eared bus ticket and a pair of keys left on a café table at closing time, rain outside
d,b=bg([(0,'#2a2a3a'),(1,'#4a3a3a')])
b+='<rect x="80" y="80" width="640" height="320" fill="#3a4a6a"/>'+rain(40,1847,'#a8b8d8',.4,5)+'<rect x="80" y="80" width="640" height="320" fill="none" stroke="#1a1a24" stroke-width="18"/>'
b+='<rect y="440" width="800" height="360" fill="#6a4a3a"/>'+glow(400,560,200,'#ffc870',.3)
b+='<rect x="240" y="540" width="200" height="90" fill="#f4ecd8" transform="rotate(-8 340 585)"/><path d="M260 560 L420 540" stroke="#a8a8b0" stroke-width="5" stroke-dasharray="6 6" transform="rotate(-8 340 585)"/>'
b+='<circle cx="530" cy="600" r="24" fill="none" stroke="#c8c8d0" stroke-width="8"/><path d="M550 610 L640 640 L636 654 L620 648 L616 660 L606 656" stroke="#d8b040" stroke-width="10" fill="none"/>'
I[1847]=svg(b,d)

# 1849 Mela!: a radiant sun-yellow heart bursting with fireworks of joy over a cheering summer crowd
d,b=bg([(0,'#ff7a3a'),(1,'#ffd04a')])
b+=rays(400,320,24,'#fff',.3,9)+glow(400,320,180,'#fff8c8',.6)+heart(400,320,140,'#ffe05a')+firework(160,180,70,'#fff',16,1)+firework(640,180,70,'#fff',16,2)
for k in range(9): x=50+k*88;b+=figure(x,820,200,'#5a1a0a',pose='up' if k%2 else 'wave')
I[1849]=svg(b,d)

# 358 あなたに逢いたくて～Missing You～: a phone screen glowing in a dark bedroom with an unsent message, a teardrop on the pillow
d,b=bg([(0,'#0a1028'),(1,'#1a1a3a')])
b+='<rect x="460" y="60" width="260" height="300" fill="#1a2a5a"/>'+moon(590,180,40)+'<rect x="460" y="60" width="260" height="300" fill="none" stroke="#06081a" stroke-width="16"/>'
b+='<rect y="500" width="800" height="300" fill="#2a2a4a"/><ellipse cx="260" cy="520" rx="200" ry="60" fill="#3a3a5a"/>'
b+=glow(400,560,160,'#8ab8ff',.4)+'<rect x="340" y="500" width="120" height="200" rx="16" fill="#1a1a24" transform="rotate(-10 400 600)"/><rect x="352" y="516" width="96" height="164" rx="6" fill="#bfe0ff" transform="rotate(-10 400 600)"/>'+heart(398,600,24,'#ff5a8a')
b+='<path d="M220 480 Q230 500 230 510 A10 10 0 0 1 210 510 Q210 500 220 480Z" fill="#bfe0ff"/>'
I[358]=svg(b,d)

# 359 天使のウィンク: a heart with tiny angel wings and a halo, one side of the halo tipped like a wink
d,b=bg([(0,'#ffd0e8'),(1,'#d0e8ff')])
b+=rays(400,400,20,'#fff',.3,8)+wings(400,420,1.4)+heart(400,420,130,'#ff4a8a')
b+='<ellipse cx="400" cy="250" rx="90" ry="22" fill="none" stroke="#ffd02a" stroke-width="14" transform="rotate(-15 400 250)"/>'+sparkle(560,230,30,'#fff')+sparkle(240,600,20,'#fff')
I[359]=svg(b,d)

# 727 True Love: two hands holding a single candle flame between them in a quiet chapel, light reflecting in stained glass
d,b=bg([(0,'#1a1a2a'),(1,'#2a1a2a')])
b+='<path d="M260 380 L260 160 Q400 40 540 160 L540 380Z" fill="#2a2a3a"/>'
for i,c in enumerate(['#e8302a','#ffd02a','#3a8ae8','#3ac85a','#a87aff','#ff8a3a']): b+=f'<path d="M400 360 L{280+i*44} 160 Q{300+i*44} 140 {324+i*44} 160Z" fill="{c}" opacity=".6"/>'
b+=glow(400,500,200,'#ffc870',.5)+'<rect x="380" y="480" width="40" height="100" rx="6" fill="#fff6e8"/><path d="M400 420 Q424 456 400 480 Q376 456 400 420Z" fill="#ffd060"/>'
b+='<path d="M240 700 Q240 560 340 540 L360 620 Q340 640 350 720Z M560 700 Q560 560 460 540 L440 620 Q460 640 450 720Z" fill="#e8b890"/>'
I[727]=svg(b,d)

# 1065 milk: a glass of milk on a breakfast table with a single drop splashing into a crown shape
d,b=bg([(0,'#fff6e8'),(1,'#ffe8d0')])
b+='<rect y="560" width="800" height="240" fill="#e8d0b0"/>'+''.join(f'<rect x="{k*100}" y="560" width="50" height="240" fill="#f4e0c8"/>' for k in range(8))
b+='<path d="M300 300 L500 300 L480 640 L320 640Z" fill="#e8f4ff" opacity=".6"/><path d="M308 380 L492 380 L480 640 L320 640Z" fill="#fff"/>'
b+='<path d="M330 380 Q340 320 360 340 Q370 300 390 330 Q400 290 410 330 Q430 300 440 340 Q460 320 470 380Z" fill="#fff"/><circle cx="400" cy="230" r="16" fill="#fff"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="8" fill="#fff"/>' for x,y in [(340,300),(460,296),(380,270)])
I[1065]=svg(b,d)

# 388 LIAR: a cracked mirror reflecting a woman's red smile, shards scattered on a dark vanity
d,b=bg([(0,'#1a0a14'),(1,'#2a0a1a')])
b+='<ellipse cx="400" cy="360" rx="220" ry="280" fill="#c8a040"/><ellipse cx="400" cy="360" rx="196" ry="256" fill="#3a3a54"/>'+lips(400,380,1.2)
b+=bolt([(300,140),(360,280),(320,360),(420,600)],'#e8e8f8',5,1)+bolt([(360,280),(500,240)],'#e8e8f8',4,1)
b+='<rect y="660" width="800" height="140" fill="#2a1a10"/>'+''.join(f'<polygon points="{x},{y} {x+30},{y+10} {x+10},{y+30}" fill="#c8c8e8"/>' for x,y in [(160,700),(240,720),(560,690),(620,730)])
I[388]=svg(b,d)

# 488 ANGEL: a black-winged figure standing on the edge of a ruined cathedral roof under lightning
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+=bolt([(160,0),(220,120),(180,140),(260,300)],'#e8f0ff',8,1)+rain(40,488,'#8a8aa8',.3,5)
b+='<path d="M-10 800 L-10 560 L200 560 L200 420 L260 340 L320 420 L320 560 L810 560 L810 800Z" fill="#0a0a14"/>'
b+=wings(560,440,1.5,'#0a0a10','#3a3a4a')+figure(560,560,220,'#000')
I[488]=svg(b,d)

# 609 Be My Baby: a baby's pacifier and a guitar pick side by side under a hot stage spotlight, rock and tenderness
d,b=bg([(0,'#1a1a2a'),(1,'#0a0a14')])
b+='<polygon points="400,-20 160,700 640,700" fill="#fff6d8" opacity=".12"/><ellipse cx="400" cy="640" rx="260" ry="50" fill="#fff6d8" opacity=".15"/>'
b+=guitar(400,420,1.1,25,'#c8702a')
b+='<path d="M560 140 Q620 160 640 220 Q620 300 560 330 Q500 300 480 220 Q500 160 560 140Z" fill="#e8302a"/>'+heart(560,230,30,'#fff')
I[609]=svg(b,d)

# 700 きっと忘れない: a lighthouse of memory: a small seaside house's window with a hand-drawn heart on its fogged glass
d,b=bg([(0,'#5a7aa8'),(1,'#a8c0d8')])
b+='<rect x="140" y="120" width="520" height="520" fill="#c8d8e8" opacity=".85"/>'+''.join(f'<circle cx="{160+(k*97)%480}" cy="{140+(k*61)%480}" r="{2+k%3}" fill="#fff" opacity=".6"/>' for k in range(50))
b+='<path d="M400 520 C280 440 280 320 350 310 C380 306 400 330 400 350 C400 330 420 306 450 310 C520 320 520 440 400 520Z" fill="none" stroke="#5a7aa8" stroke-width="12" stroke-linecap="round"/>'
b+='<path d="M140 120 L660 120 L660 640 L140 640Z M400 120 L400 640 M140 380 L660 380" stroke="#f4f4f4" stroke-width="20" fill="none" opacity=".9"/>'
b+='<rect y="640" width="800" height="160" fill="#8a6a4a"/>'
I[700]=svg(b,d)

# 1025 丸の内サディスティック: a red stiletto stepping on a crumpled salaryman's tie on a Tokyo station platform
d,b=bg([(0,'#3a2a2a'),(1,'#1a1414')])
b+='<rect x="-10" y="100" width="820" height="220" fill="#7a4a3a"/>'+''.join(f'<rect x="{40+k*150}" y="{140}" width="90" height="140" fill="#f4e0b8" opacity=".6"/>' for k in range(6))
b+='<rect y="420" width="800" height="380" fill="#5a5a64"/><rect y="420" width="800" height="20" fill="#ffd02a"/>'
b+='<path d="M180 640 Q280 620 380 660 Q440 680 520 640 L560 660 L520 700 L540 760 L500 740 L380 700 Q280 680 180 680Z" fill="#2a3a8a"/><path d="M220 650 L520 670" stroke="#d8b040" stroke-width="5" stroke-dasharray="20 20"/>'
b+='<path d="M380 600 Q420 540 500 540 L560 560 Q600 570 600 600 L600 620 L420 620 Q400 640 380 640Z" fill="#e8102a"/><path d="M590 610 L600 700 L612 700 L606 610" fill="#a80a1a"/>'
I[1025]=svg(b,d)

# 1530 ハルカ: a coffee mug with a hand-drawn star on it sitting on a desk by a window, watching years of mornings pass
d,b=bg([(0,'#ffe8c8'),(1,'#ffd0a0')])
b+='<rect x="480" y="80" width="260" height="320" fill="#c8e8ff"/><path d="M480 80 L740 80 L740 400 L480 400Z M610 80 L610 400" stroke="#fff" stroke-width="12" fill="none"/>'+hinomaru_sun(560,180,40,'#fff6d0',1)
b+='<polygon points="480,400 740,400 600,800 200,800" fill="#fff8e0" opacity=".4"/><rect y="540" width="800" height="260" fill="#a87a5a"/>'
b+='<path d="M260 380 L440 380 L430 580 L270 580Z" fill="#f4f0e8"/><path d="M440 420 Q500 420 494 480 Q488 530 434 520" stroke="#f4f0e8" stroke-width="20" fill="none"/>'+star5(350,470,50,'#ffd02a')
b+='<path d="M310 360 Q320 320 310 290 M360 360 Q370 320 360 280" stroke="#fff" stroke-width="6" fill="none" opacity=".6"/>'
I[1530]=svg(b,d)

# 1538 シャッター: a camera shutter mid-click capturing a couple's last photo together against a sunset
d,b=bg([(0,'#ff8a6a'),(1,'#ffc8a0')])
b+=hinomaru_sun(400,400,130,'#fff4d0',.8)+figure(340,620,220,'#3a1a2a',hair='#3a1a2a')+figure(460,620,240,'#3a1a2a')
for k in range(8): a=k*45;b+=f'<path d="M400 400 L{400+500*math.cos(math.radians(a)):.0f} {400+500*math.sin(math.radians(a)):.0f} L{400+500*math.cos(math.radians(a+45)):.0f} {400+500*math.sin(math.radians(a+45)):.0f}Z" fill="#1a1a24" transform="rotate(15 400 400)" opacity=".92" clip-path="url(#ap)"/>'
d+='<clipPath id="ap"><path d="M0 0 H800 V800 H0Z M400 120 A280 280 0 1 0 400.1 120Z" clip-rule="evenodd"/></clipPath>'
b+=ring(400,400,280,'#3a3a44',12)
I[1538]=svg(b,d)

# 1549 ギラギラ: a single eye glaring from behind a curtain of neon green glitter in the dark
d,b=bg([(0,'#04100a'),(1,'#0a1a10')])
r=R(1549)
for _ in range(200): x,y=r.uniform(0,800),r.uniform(0,800);b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{r.uniform(4,10):.0f}" height="{r.uniform(4,10):.0f}" fill="{r.choice(["#5aff8a","#b8ff5a","#e8ffe8","#2ac85a"])}" opacity="{r.uniform(.3,.9):.2f}" transform="rotate(45 {x:.0f} {y:.0f})"/>'
b+='<path d="M180 400 Q400 230 620 400 Q400 570 180 400Z" fill="#f4fff4"/><circle cx="400" cy="400" r="100" fill="#2ac85a"/><circle cx="400" cy="400" r="46" fill="#000"/><circle cx="370" cy="370" r="16" fill="#fff"/>'+glow(400,400,240,'#5aff8a',.25)
I[1549]=svg(b,d)

# 1577 Blue Ambience: a glass of blue soda on a windowsill casting a long blue shadow in afternoon light
d,b=bg([(0,'#d8eaf8'),(1,'#a8c8e8')])
b+='<polygon points="0,800 300,300 500,300 800,800" fill="#fff" opacity=".35"/><rect y="560" width="800" height="240" fill="#e8f0f8"/>'
b+='<path d="M320 300 L480 300 L470 560 L330 560Z" fill="#5ab0ff" opacity=".6" stroke="#fff" stroke-width="5"/><path d="M326 360 L474 360 L470 556 L330 556Z" fill="#2a8ae8" opacity=".8"/>'
b+='<path d="M330 560 L470 560 L660 760 L520 780Z" fill="#2a8ae8" opacity=".25"/>'+''.join(ring(360+(k*31)%90,380+k*30,6,'#fff',3,.8) for k in range(6))
b+='<rect x="420" y="200" width="12" height="200" fill="#ff7aa8" transform="rotate(10 426 300)"/>'
I[1577]=svg(b,d)

# 1598 Dangerholic: a red warning siren light spinning in the dark, hazard stripes and a heart behind it
d,b=bg([(0,'#1a0a0a'),(1,'#0a0404')])
for k in range(10): b+=f'<path d="M{k*100-200} 800 L{k*100} 600 L{k*100+50} 600 L{k*100-150} 800Z" fill="#ffd02a"/>'
b+='<polygon points="400,320 -20,120 -20,380" fill="#ff2a2a" opacity=".3"/><polygon points="400,320 820,200 820,460" fill="#ff2a2a" opacity=".2"/>'
b+=glow(400,320,200,'#ff2a2a',.6)+'<path d="M300 440 L300 300 Q300 200 400 200 Q500 200 500 300 L500 440Z" fill="#e8102a"/><rect x="270" y="440" width="260" height="50" rx="8" fill="#2a2a34"/>'+heart(400,330,50,'#fff')
I[1598]=svg(b,d)

# 389 1/2の神話: a single tarot-like card split down the middle, one half day and one half night
d,b=bg([(0,'#1a1a2a'),(1,'#2a2a3a')])
b+='<rect x="220" y="140" width="180" height="520" fill="#ffd87a"/><rect x="400" y="140" width="180" height="520" fill="#1a2a6a"/>'
b+='<path d="M400 290 A110 110 0 0 0 400 510Z" fill="#fff4c8"/><path d="M400 290 A110 110 0 0 1 400 510 A80 80 0 0 0 400 290Z" fill="#f4f0ff"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff"/>' for x,y in [(460,200),(540,260),(500,600),(440,560)])
b+=''.join(f'<path d="M310 {200+k*20} L310 {180+k*20}" stroke="#fff" stroke-width="3"/>' for k in range(1))+'<rect x="220" y="140" width="360" height="520" fill="none" stroke="#c8a040" stroke-width="10"/><path d="M400 130 L400 670" stroke="#c8a040" stroke-width="4" stroke-dasharray="14 10"/>'
I[389]=svg(b,d)

# 390 SAND BEIGE -砂漠へ-: a woman in a flowing veil walking alone across golden dunes toward a distant oasis
d,b=bg([(0,'#ffb060'),(1,'#ffe0a0')])
b+=hinomaru_sun(560,240,90,'#fff4c8',.8)
b+='<path d="M-10 520 Q200 440 400 500 T810 460 L810 810 L-10 810Z" fill="#e8b060"/><path d="M-10 620 Q300 540 560 620 T810 600 L810 810 L-10 810Z" fill="#d89a40"/>'
b+='<path d="M640 470 L650 420 M660 470 L680 430" stroke="#3a6a2a" stroke-width="4"/><path d="M620 420 Q650 400 680 420 M650 410 Q670 390 700 400" stroke="#3a8a2a" stroke-width="8" fill="none"/>'
b+=figure(300,600,220,'#3a1a0a',hair='#3a1a0a')+'<path d="M290 430 Q200 460 140 420 Q200 520 290 520Z" fill="#fff4e0" opacity=".85"/>'
for k in range(5): b+=f'<ellipse cx="{340+k*60}" cy="{620+k*20}" rx="10" ry="4" fill="#a8702a"/>'
I[390]=svg(b,d)

# 538 こころ: a paper heart folded like origami, held gently in an open palm with a soft light around it
d,b=bg([(0,'#f4ece4'),(1,'#e0d4c8')])
b+=glow(400,380,200,'#fff',.6)
b+='<path d="M180 560 Q200 460 300 460 L520 460 Q620 460 640 520 Q620 600 520 620 L300 640 Q200 640 180 560Z" fill="#e8c0a0"/><path d="M520 460 Q600 420 640 460" stroke="#e8c0a0" stroke-width="40" fill="none" stroke-linecap="round"/>'
b+='<path d="M400 460 L300 360 Q280 300 330 290 Q380 290 400 340 Q420 290 470 290 Q520 300 500 360Z" fill="#e8302a"/><path d="M400 340 L400 460 M300 360 L400 400 L500 360" stroke="#c81a1a" stroke-width="4" fill="none"/>'
I[538]=svg(b,d)

# 1220 つなぐ: five hands linked in a ring seen from above, a small glowing light in the middle
d,b=bg([(0,'#1a2a4a'),(1,'#3a4a6a')])
b+=glow(400,400,120,'#ffe8a0',.8)
for k,c in enumerate(['#3a8ae8','#e8302a','#ffd02a','#3ac85a','#a87aff']):
    a=math.radians(k*72-90);x=400+200*math.cos(a);y=400+200*math.sin(a)
    b+=f'<path d="M{400+330*math.cos(a):.0f} {400+330*math.sin(a):.0f} L{x:.0f} {y:.0f}" stroke="{c}" stroke-width="60" stroke-linecap="round"/><circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#e8b890"/>'
b+=ring(400,400,200,'#e8b890',40)+sparkle(400,400,40,'#fff')
I[1220]=svg(b,d)

# 1242 Real Face: a cracked porcelain mask peeling away to reveal a burning eye beneath, sparks flying
d,b=bg([(0,'#0a0a0a'),(1,'#1a0a0a')])
b+=glow(420,400,220,'#ff5a1a',.4)
b+='<path d="M260 200 Q400 120 540 200 Q580 400 400 640 Q220 400 260 200Z" fill="#f4f0e8"/><path d="M400 140 L380 260 L420 330 L390 420 L430 520 L400 640 Q560 420 540 200 Q470 150 400 140Z" fill="#2a0a0a"/>'
b+='<ellipse cx="330" cy="330" rx="40" ry="24" fill="#1a1a1a"/><ellipse cx="480" cy="330" rx="40" ry="24" fill="#ff5a1a"/><circle cx="480" cy="330" r="12" fill="#fff4c8"/>'
r=R(1242)
for _ in range(16): x,y=r.uniform(500,740),r.uniform(160,520);b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3" fill="#ffa83a"/>'
I[1242]=svg(b,d)

# 1558 東京フラッシュ: a camera flash popping white over a neon Tokyo intersection, two figures caught in the light
d,b=bg([(0,'#1a0a3a'),(1,'#0a0420')])
b+=skyline(640,'#140a28',1558,120,460,'#ff5ab8',100)
for x,c in [(120,'#5ae8ff'),(680,'#ffe05a'),(220,'#ff5ab8')]: b+=f'<rect x="{x-30}" y="200" width="60" height="200" fill="{c}" opacity=".6"/>'
b+='<rect y="640" width="800" height="160" fill="#1a1428"/>'+''.join(f'<rect x="{k*100}" y="660" width="60" height="140" fill="#fff" opacity=".25"/>' for k in range(8))
b+=rays(400,420,24,'#fff',.35,4)+glow(400,420,200,'#fff',.7)+figure(370,720,200,'#0a0414')+figure(430,720,190,'#0a0414',hair='#0a0414')
I[1558]=svg(b,d)

# 391 TATTOO: a crimson dragon tattoo coiling over a bare shoulder silhouette lit by a red neon sign
d,b=bg([(0,'#6a2a3a'),(1,'#3a1020')])
b+=glow(600,200,160,'#ff2a3a',.4)+'<rect x="520" y="160" width="160" height="80" rx="10" fill="none" stroke="#ff3a4a" stroke-width="8"/>'
b+='<path d="M180 800 Q230 640 220 560 Q200 420 260 360 Q330 330 360 300 L360 250 Q360 210 400 210 Q440 210 440 250 L440 300 Q470 330 540 360 Q600 420 580 560 Q570 640 620 800Z" fill="#e8c0a0"/><ellipse cx="400" cy="200" rx="56" ry="64" fill="#1a0a0a"/><path d="M360 230 Q380 300 400 300 Q420 300 440 230Z" fill="#1a0a0a"/>'
b+='<path d="M330 740 Q260 640 340 580 Q420 530 380 470 Q340 420 400 380 Q470 350 480 420" stroke="#c80a1a" stroke-width="22" fill="none" stroke-linecap="round"/><path d="M480 420 L510 400 L500 440Z" fill="#c80a1a"/>'+''.join(f'<path d="M{x} {y} l-14 -14 M{x} {y} l14 -14" stroke="#c80a1a" stroke-width="6"/>' for x,y in [(300,640),(370,560),(370,450)])+''
I[391]=svg(b,d)

# 649 Don't Leave Me: a hand gripping the strap of a departing train door as it closes, rain on the platform
d,b=bg([(0,'#3a4a5a'),(1,'#5a6a7a')])
b+=rain(80,649,'#c8d8e8',.4,6)
b+='<rect x="140" y="100" width="520" height="620" fill="#c8ccd4"/><rect x="180" y="140" width="200" height="280" fill="#6a7a8a"/><rect x="420" y="140" width="200" height="280" fill="#6a7a8a"/><path d="M400 100 L400 720" stroke="#1a1a24" stroke-width="16"/>'
b+='<g fill="#e8b890"><rect x="300" y="430" width="200" height="60" rx="30"/><rect x="260" y="400" width="90" height="120" rx="40"/></g><path d="M300 360 L300 440 M500 360 L500 440" stroke="#5a5a64" stroke-width="10"/>'
I[649]=svg(b,d)

# 650 衝動: a red sports car exploding out of a burst of flame and speed lines, tyres smoking
d,b=bg([(0,'#1a0404'),(1,'#3a0a0a')])
b+=glow(200,440,260,'#ff5a1a',.6)+''.join(f'<path d="M{100+k*20} {360+k*20} L-10 {360+k*20}" stroke="#ffa83a" stroke-width="5" opacity=".6"/>' for k in range(8))
b+='<path d="M200 520 Q220 450 320 440 L420 390 Q520 370 600 410 L660 450 Q720 460 720 510 L720 540 L200 540Z" fill="#e8102a"/><path d="M430 400 L520 386 L590 416 L440 430Z" fill="#1a1a24"/>'
for x in (300,620): b+=f'<circle cx="{x}" cy="540" r="44" fill="#1a1a1a"/><circle cx="{x}" cy="540" r="18" fill="#c8c8d0"/>'
b+='<rect y="584" width="800" height="216" fill="#1a1a1a"/>'+''.join(f'<circle cx="{220-k*40}" cy="{560-k*10}" r="{30+k*8}" fill="#8a8a94" opacity="{.4-k*.08:.2f}"/>' for k in range(4))
I[650]=svg(b,d)

# 738 Gift: a small wrapped present held out at arm's length toward the sunrise, a gold medal ribbon trailing from it
d,b=bg([(0,'#3a5ab8'),(.6,'#ffb88a'),(1,'#ffe0b0')])
b+=rays(400,600,20,'#fff',.3,6)+hinomaru_sun(400,600,130,'#fff4d0',.9)
b+='<g fill="#e8b890"><rect x="140" y="480" width="200" height="60" rx="30" transform="rotate(-10 240 510)"/><rect x="460" y="480" width="200" height="60" rx="30" transform="rotate(10 560 510)"/></g>'
b+='<rect x="320" y="300" width="160" height="160" fill="#3a8ae8"/><rect x="390" y="300" width="20" height="160" fill="#ffd02a"/><rect x="320" y="370" width="160" height="20" fill="#ffd02a"/><path d="M400 300 Q360 250 340 280 Q350 300 400 300 Q440 250 460 280 Q450 300 400 300Z" fill="#ffd02a"/>'
b+='<path d="M480 380 Q560 400 600 340" stroke="#e8302a" stroke-width="16" fill="none"/><circle cx="610" cy="320" r="30" fill="#ffd02a" stroke="#c8901a" stroke-width="6"/>'
I[738]=svg(b,d)

# 939 やめないで, PURE: a white dove taking off from a pair of open hands into a pure blue sky
d,b=bg([(0,'#5ab8f8'),(1,'#e0f4ff')])
b+=rays(400,200,18,'#fff',.35,7)
b+='<path d="M220 720 Q240 600 340 580 L380 640 Q350 660 360 740Z M580 720 Q560 600 460 580 L420 640 Q450 660 440 740Z" fill="#e8c0a0"/>'
b+='<g transform="translate(400 380)"><path d="M-30 20 Q0 -10 40 0 Q70 10 80 -10 Q70 30 30 40 Q-10 50 -30 20Z" fill="#fff"/><path d="M0 0 Q-60 -120 -160 -100 Q-90 -40 -20 20Z" fill="#fff"/><path d="M10 0 Q80 -140 180 -140 Q120 -60 30 10Z" fill="#f4f8ff"/><circle cx="66" cy="-4" r="4" fill="#1a1a1a"/><path d="M80 -6 L96 0 L80 4Z" fill="#ffa83a"/></g>'
I[939]=svg(b,d)

# 1165 GLORIA: a school graduation chorus seen from behind, music sheets raised high into a golden auditorium light
d,b=bg([(0,'#ffd27a'),(1,'#ffa84a')])
b+=rays(400,120,20,'#fff',.35,8)+glow(400,140,160,'#fff8d8',.8)
for row,(y,h,n) in enumerate([(580,160,8),(700,190,7),(820,220,6)]):
    for k in range(n): x=60+k*(680/(n-1));b+=figure(x,y,h,'#3a1a0a')+(f'<rect x="{x-16}" y="{y-h*.92:.0f}" width="32" height="24" fill="#fff" transform="rotate(-10 {x} {y-h*.9:.0f})"/>' if (k+row)%3==0 else '')
b+=note(200,240,30,'#fff')+note(600,220,26,'#fff',True)
I[1165]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
