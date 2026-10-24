import sys,math;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
# Natsumero: 1. csoport, 20 mintaikon Miske jóváhagyására (2026-10-24)
I={}
JF='font-family="Noto Sans JP,Noto Sans CJK JP,sans-serif" font-weight="700"'

# 12 上を向いて歩こう (1961): alone at night, the walker tilts his head up to a sky full of stars so the tears won't fall
d,b=bg([(0,'#081030'),(.65,'#1a2a5a'),(1,'#2a3a6a')])
b+=starsf(90,12,560,'#fff6d0')
for x,y,s in [(520,160,22),(610,250,14),(440,260,10),(660,130,9),(560,330,12)]: b+=sparkle(x,y,s,'#fff2b0')
b+=hills(640,25,'#101a3a',4)+'<rect y="700" width="800" height="100" fill="#0a1028"/>'
b+='<rect x="190" y="330" width="10" height="380" fill="#060a1a"/><path d="M170 334 L220 334 L212 310 L178 310Z" fill="#060a1a"/>'+glow(195,345,70,'#ffd98a',.45)+'<path d="M176 334 L214 334 L208 350 L182 350Z" fill="#fff0b8"/>'
b+=f'<g transform="rotate(-6 420 760)">{figure(420,760,400,"#04060f",pose="stand")}</g>'
b+='<path d="M412 432 q6 14 0 22 q-8 -8 0 -22Z" fill="#bfe0ff"/>'
I[12]=svg(b,d)

# 68 ブルー・ライト・ヨコハマ (1969): Yokohama harbour at night, blue city lights trembling in the water, a couple walking on the pier
d,b=bg([(0,'#04103a'),(.55,'#0a2a6a'),(1,'#05123a')])
b+=glow(520,420,260,'#3a8aff',.35)
b+=skyline(470,'#06123a',68,40,170,'#7ac0ff',120)
b+='<path d="M600 470 L612 250 L628 250 L640 470Z" fill="#0a1a4a"/><rect x="596" y="230" width="48" height="24" rx="6" fill="#7ac0ff"/>'+glow(620,242,30,'#a8d8ff',.7,'glow2')
b+='<rect y="470" width="800" height="330" fill="#03102e"/>'
r=R(68)
for k in range(70):
    x=r.uniform(0,800);y=r.uniform(480,700);w=r.uniform(14,60)
    b+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="3" rx="1.5" fill="{r.choice(["#5aa8ff","#9ad0ff","#3a6aff"])}" opacity="{r.uniform(.3,.8):.2f}"/>'
b+='<path d="M-10 640 L560 600 L580 640 L-10 690Z" fill="#081a40"/><rect x="-10" y="680" width="820" height="130" fill="#020818"/>'
b+=figure(300,760,290,'#010410',hair='#010410')+figure(380,760,320,'#010410')
I[68]=svg(b,d)

# 122 UFO (1978): a glowing flying saucer beams pink light down onto two dancing silhouettes in disco pose
d,b=bg([(0,'#12052a'),(.6,'#2a0a4a'),(1,'#4a0a4a')])
b+=starsf(60,122,500,'#ffd0f0')
b+='<polygon points="400,250 190,760 610,760" fill="#ff7ad8" opacity=".22"/><polygon points="400,250 270,760 530,760" fill="#ffb0ec" opacity=".2"/>'
b+=glow(400,220,170,'#ff7ad8',.45)
b+='<ellipse cx="400" cy="230" rx="230" ry="52" fill="#c8c8e0"/><ellipse cx="400" cy="218" rx="230" ry="40" fill="#e8e8f8"/><path d="M290 205 Q400 80 510 205Z" fill="#9ae8ff" opacity=".9"/><path d="M320 190 Q360 130 400 125" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>'
for k in range(7): b+=f'<circle cx="{220+k*60}" cy="{240+ (12 if k in (0,6) else 20 if k in (1,5) else 24)}" r="10" fill="{["#ff5ac8","#ffe05a","#5ae8ff"][k%3]}"/>'
b+=figure(340,760,250,'#1a0520',pose='up',hair='#1a0520')+figure(460,760,250,'#1a0520',pose='wave',hair='#1a0520')
b+='<rect y="760" width="800" height="40" fill="#1a0520"/>'
I[122]=svg(b,d)

# 105 勝手にしやがれ (1977): the famous moment on stage, a fedora flung high into the spotlight above the singer
d,b=bg([(0,'#0a0a0e'),(1,'#2a1a10')])
b+='<polygon points="520,-20 320,800 760,800" fill="#ffe2a8" opacity=".14"/>'+glow(540,720,220,'#ffcf7a',.25)
b+='<rect y="700" width="800" height="100" fill="#140c08"/><ellipse cx="540" cy="712" rx="230" ry="26" fill="#ffd98a" opacity=".25"/>'
b+=figure(540,712,330,'#050302',pose='up')
b+='<g transform="rotate(-24 300 230)"><ellipse cx="300" cy="262" rx="150" ry="34" fill="#2a2018"/><path d="M200 258 Q205 150 300 140 Q395 150 400 258 Q300 280 200 258Z" fill="#3a2c20"/><path d="M262 150 Q300 172 338 150" stroke="#1a120c" stroke-width="12" fill="none"/><path d="M204 236 Q300 256 396 236 L398 254 Q300 276 202 254Z" fill="#a8341c"/></g>'
for x,y,a in [(430,330,30),(170,360,-40),(250,120,0)]: b+=f'<path d="M{x} {y} q{-20+a/3} 30 {-40+a} 40" stroke="#ffe2a8" stroke-width="4" fill="none" opacity=".5" stroke-linecap="round"/>'
I[105]=svg(b,d)

# 1678 およげ!たいやきくん (1976): a taiyaki cake that escaped the shop, swimming happily through the blue sea among bubbles
d,b=bg([(0,'#6ad0f0'),(.5,'#1a8ac8'),(1,'#0a3a7a')])
b+=rays(400,-60,9,'#ffffff',.08,6,60,120)
b+='<g transform="translate(400 420) rotate(-10)">'
b+='<path d="M-210 0 Q-200 -110 -60 -120 Q90 -126 150 -40 L250 -110 Q236 0 250 110 L150 40 Q90 126 -60 120 Q-200 110 -210 0Z" fill="#c8782a"/>'
b+='<path d="M-190 -10 Q-170 -96 -60 -100 Q70 -104 130 -40 Q60 -70 -60 -72 Q-160 -66 -190 -10Z" fill="#e8a24a"/>'
for k in range(5): b+=f'<path d="M{-40+k*36} -80 q16 80 0 160" stroke="#9a5418" stroke-width="7" fill="none" opacity=".55"/>'
b+='<path d="M170 -40 L230 -80 M170 40 L230 80 M180 0 L240 0" stroke="#9a5418" stroke-width="6" opacity=".5"/>'
b+='<circle cx="-140" cy="-34" r="22" fill="#fff"/><circle cx="-146" cy="-34" r="11" fill="#2a1408"/><path d="M-200 30 Q-180 46 -158 34" stroke="#2a1408" stroke-width="7" fill="none" stroke-linecap="round"/></g>'
r=R(7)
for _ in range(16):
    x,y,s=r.uniform(60,760),r.uniform(80,760),r.uniform(8,26)
    if 170<x<660 and 270<y<580: continue
    b+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="none" stroke="#e0f8ff" stroke-width="3" opacity=".7"/><circle cx="{x-s*.35:.0f}" cy="{y-s*.35:.0f}" r="{s*.2:.1f}" fill="#fff" opacity=".8"/>'
b+='<path d="M-10 760 Q100 700 200 760 T420 760 T640 760 T820 760 L820 810 L-10 810Z" fill="#0a2a5a"/>'
I[1678]=svg(b,d)

# 356 赤いスイートピー (1982): a spray of red sweet peas against a soft spring sky, a seaside railway line far below
d,b=bg([(0,'#ffe8ec'),(.6,'#ffd0d8'),(1,'#a8d8e8')])
b+=glow(560,240,220,'#ffffff',.6)
b+='<rect y="640" width="800" height="160" fill="#8ac8e0"/><path d="M-10 690 L810 650 L810 668 L-10 708Z" fill="#6a4a3a"/>'
for k in range(14): b+=f'<rect x="{k*60}" y="{688-k*2.8:.0f}" width="22" height="6" fill="#4a3428"/>'
def pea(x,y,s,rot,col='#c8102e',col2='#ff3a52'):
    # szagosbükköny: nagy, fodros zászlószirom, alatta két szárnyszirom és a csónak
    wav=' '.join(f'Q{-60+k*20+10} {-112-(8 if k%2 else 0)} {-60+(k+1)*20} {-104+(2 if k%2 else 0)}' for k in range(6))
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M-8 -10 Q-80 -30 -64 -96 {wav} Q84 -30 8 -10Z" fill="{col2}"/>'
            f'<path d="M0 -14 Q-30 -40 -20 -80 M0 -14 Q30 -40 20 -80" stroke="{col}" stroke-width="5" fill="none" opacity=".6"/>'
            f'<ellipse cx="-24" cy="-6" rx="30" ry="20" fill="{col}" transform="rotate(-20 -24 -6)"/><ellipse cx="24" cy="-6" rx="30" ry="20" fill="{col}" transform="rotate(20 24 -6)"/>'
            f'<path d="M-10 4 Q0 22 10 4Z" fill="#ffd0d8"/><path d="M-4 10 Q0 34 4 50 L-2 50 Q-8 30 -10 10Z" fill="#4a8a3a"/></g>')
b+='<path d="M300 800 Q330 600 420 470 Q480 380 560 330" stroke="#4a8a3a" stroke-width="9" fill="none"/><path d="M330 660 Q260 600 230 540" stroke="#4a8a3a" stroke-width="7" fill="none"/>'
b+='<path d="M560 330 q40 -40 80 -20 q-30 0 -50 30" stroke="#6aaa4a" stroke-width="5" fill="none"/>'
for x,y,s,rot in [(560,330,1.25,20),(450,440,1.1,-10),(380,560,1.0,25),(230,540,1.05,-25),(520,520,.8,40)]: b+=pea(x,y,s,rot)
b+=petals(10,356,'#ff8aa0',300,640,6,12,.6)
I[356]=svg(b,d)

# 379 DESIRE -情熱- (1986): the bob-cut silhouette of a dancer in profile, wrapped in a blaze of crimson flame
d,b=bg([(0,'#0a0004'),(.6,'#3a0410'),(1,'#7a0a14')])
b+=glow(430,470,260,'#ff2a3a',.4)
r=R(379)
for k in range(9):
    x=150+k*68;h=r.uniform(260,460);w=r.uniform(60,110)
    b+=f'<path d="M{x-w} 800 Q{x-w*.6} {800-h*.5} {x+r.uniform(-30,30):.0f} {800-h:.0f} Q{x+w*.7} {800-h*.5} {x+w} 800Z" fill="{r.choice(["#ff3a2a","#ff6a1a","#d8102a"])}" opacity=".75"/>'
b+=profile(400,720,2.1,'#05000a')
b+='<path d="M300 220 Q330 140 420 150 Q520 160 540 250 L548 360 Q520 330 500 300 L480 230 Q420 210 360 260 L330 380 L300 400 Q280 300 300 220Z" fill="#05000a"/>'
I[379]=svg(b,d)

# 1 川の流れのように (1989): a calm river winding from the hills toward a golden sunset, life flowing gently on
d,b=bg([(0,'#ffcf8a'),(.45,'#ff9a6a'),(1,'#5a3a6a')])
b+=glow(400,330,160,'#fff0c0',.7)+hinomaru_sun(400,330,80,'#fff2c8')
b+=hills(400,40,'#a8607a',3,5,.8)+hills(470,50,'#7a4a6a',8)
b+='<path d="M380 410 Q420 450 360 500 Q260 580 360 650 Q480 730 300 810 L620 810 Q620 720 470 650 Q380 600 440 530 Q500 470 420 410Z" fill="#ffd8a0"/>'
b+='<path d="M380 410 Q420 450 360 500 Q260 580 360 650 Q480 730 300 810 L360 810 Q520 730 400 650 Q300 580 400 500 Q450 450 400 410Z" fill="#fff0d0" opacity=".6"/>'
b+='<path d="M-10 520 Q200 500 330 560 Q260 640 320 810 L-10 810Z" fill="#4a2a4a"/><path d="M810 520 Q620 500 520 560 Q600 650 560 810 L810 810Z" fill="#4a2a4a"/>'
for x in (90,170,690,740): b+=tree(x,580,140,'#3a1f3a',x)
I[1]=svg(b,d)

# 535 ラブ・ストーリーは突然に (1991): a crowded station crossing at dusk, two figures turn toward each other and a heart flashes between them
d,b=bg([(0,'#2a3a7a'),(.55,'#c86a8a'),(1,'#ffb07a')])
b+=skyline(560,'#2a2050',535,80,260,'#ffd27a',60)
b+='<rect y="560" width="800" height="240" fill="#3a2a4a"/>'
for k in range(8): b+=f'<rect x="{40+k*96}" y="610" width="60" height="150" fill="#f4e8e0" opacity=".25" transform="skewX(-8)"/>'
b+=figure(270,760,260,'#120a1a',pose='reach')+figure(540,760,250,'#120a1a',pose='reachL',hair='#120a1a')
b+=glow(405,400,110,'#ff5a8a',.6)+heart(405,400,70,'#ff3a6a')+rays(405,400,14,'#fff0f4',.18,4)
I[535]=svg(b,d)

# 226 空と君のあいだに (1994): a child and a faithful dog sit on a hill under a vast blue sky with drifting clouds
d,b=bg([(0,'#3a8ae0'),(.7,'#8ac8f8'),(1,'#d8f0ff')])
for x,y,s in [(170,170,1.1),(560,250,1.4),(320,330,.8)]:
    b+=f'<g transform="translate({x} {y}) scale({s})" fill="#fff" opacity=".92"><ellipse cx="0" cy="0" rx="90" ry="34"/><circle cx="-30" cy="-22" r="34"/><circle cx="24" cy="-30" r="42"/><circle cx="62" cy="-8" r="28"/></g>'
b+='<path d="M-10 620 Q400 480 810 600 L810 810 L-10 810Z" fill="#4a9a4a"/><path d="M-10 680 Q400 590 810 690 L810 810 L-10 810Z" fill="#2a7a3a"/>'
b+='<g fill="#123018"><ellipse cx="330" cy="540" rx="34" ry="40"/><circle cx="330" cy="482" r="24"/><path d="M300 560 L370 560 L380 580 L292 580Z"/></g>'
b+=('<g fill="#123018"><path d="M420 580 Q410 530 436 500 Q450 486 466 492 L470 470 Q472 452 490 450 Q508 450 512 466 L530 474 Q534 484 520 486 L506 488 Q500 520 504 548 Q508 572 500 580Z"/>'
    '<path d="M478 452 Q470 470 474 490 Q482 470 478 452Z" fill="#0a2010"/><path d="M420 576 Q392 576 388 556" stroke="#123018" stroke-width="10" fill="none" stroke-linecap="round"/></g>')
I[226]=svg(b,d)

# 762 チェリー (1996): two bright red cherries on one stem swinging in spring light, sakura petals dancing around
d,b=bg([(0,'#c8f0a8'),(.6,'#8ad87a'),(1,'#3a9a5a')])
b+=glow(400,400,280,'#fffbe0',.5)+petals(26,762,'#ffd6e4',0,800,8,16,.8)
b+='<path d="M400 170 Q380 270 290 430" stroke="#4a6a2a" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M400 170 Q450 280 500 470" stroke="#4a6a2a" stroke-width="12" fill="none" stroke-linecap="round"/>'
b+='<path d="M400 170 Q470 100 560 130 Q500 190 400 170Z" fill="#5ab04a"/><path d="M400 170 Q480 130 556 132" stroke="#3a8a2a" stroke-width="4" fill="none"/>'
d+=rg('ch',S((0,'#ff8a8a'),(.45,'#e8102a'),(1,'#7a0010')),.38,.35,.7)
for x,y,r_ in [(290,520,110),(510,560,115)]:
    b+=f'<circle cx="{x}" cy="{y}" r="{r_}" fill="url(#ch)"/><ellipse cx="{x-36}" cy="{y-44}" rx="26" ry="16" fill="#fff" opacity=".7" transform="rotate(-30 {x-36} {y-44})"/>'
I[762]=svg(b,d)

# 278 TSUNAMI (2000): a towering curling wave at sunset on the Shonan coast, spray glittering in the last light
d,b=bg([(0,'#ff9a5a'),(.45,'#ff6a6a'),(1,'#2a2a6a')])
b+=hinomaru_sun(560,300,90,'#ffe0a0')+glow(560,300,160,'#ffd08a',.5)
b+='<rect y="430" width="800" height="370" fill="#1a3a7a"/>'
b+='<path d="M-10 800 L-10 430 Q120 120 380 160 Q560 190 560 330 Q520 240 420 250 Q340 260 360 340 Q380 400 470 380 Q400 470 300 440 Q200 420 200 520 L240 800Z" fill="#0a4a8a"/>'
b+='<path d="M380 160 Q560 190 560 330 Q540 260 470 240 Q400 220 380 160Z" fill="#e8f6ff"/>'
b+='<path d="M560 330 q-14 -20 -34 -24 m16 22 q-20 -14 -40 -10 m30 16 q-18 -6 -34 4" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/>'
b+=seigaiha(520,'#9ad0ff',.18,40)
b+=ellipse_dots(520,250,70,40,14,'#ffffff',5,.8)
b+='<path d="M-10 800 L-10 430 Q120 120 380 160 Q200 200 140 400 Q100 560 240 800Z" fill="#06306a" opacity=".7"/>'
I[278]=svg(b,d)

# 971 traveling (2001): a retro-futuristic night ride, light trails streaking through a neon tunnel toward a glowing horizon
d,b=bg([(0,'#1a0a3a'),(.5,'#5a1a6a'),(1,'#ff6a9a')])
b+=glow(400,430,170,'#fff0a0',.8)+f'<circle cx="400" cy="430" r="50" fill="#fffbe8"/>'
for k in range(14):
    a=math.radians(k*360/14)
    b+=f'<path d="M{400+60*math.cos(a):.0f} {430+60*math.sin(a):.0f} L{400+700*math.cos(a-0.05):.0f} {430+700*math.sin(a-0.05):.0f} L{400+700*math.cos(a+0.05):.0f} {430+700*math.sin(a+0.05):.0f}Z" fill="{["#ff5ab8","#5ae8ff","#ffe05a"][k%3]}" opacity=".35"/>'
for k in range(6):
    r_=110+k*k*22
    b+=f'<rect x="{400-r_}" y="{430-r_*.8:.0f}" width="{2*r_}" height="{r_*1.6:.0f}" rx="{r_*.25:.0f}" fill="none" stroke="#ff7ad8" stroke-width="{2+k}" opacity="{.7-k*.08:.2f}"/>'
b+='<path d="M250 800 L380 470 L420 470 L550 800Z" fill="#12082a"/><path d="M398 800 L398 480 L402 480 L402 800Z" fill="#ffe05a" opacity=".6"/>'
I[971]=svg(b,d)

# 1191 Love so sweet (2007): a heart-shaped candy lollipop in a cellophane wrap with a ribbon, sparkling with sugar
d,b=bg([(0,'#ffe0f0'),(.6,'#ffb8d8'),(1,'#ff8ab8')])
b+=confetti(40,1191,['#ffffff','#ffe05a','#ff5a9a','#8ad8ff'])
d+=rg('lp',S((0,'#ffd0e4'),(.5,'#ff4a8a'),(1,'#b0104a')),.35,.3,.75)
b+='<rect x="390" y="430" width="22" height="350" rx="11" fill="#fff6f0"/>'
b+=heart(400,330,170,'url(#lp)')
b+='<path d="M310 250 Q340 210 380 230" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".7"/>'
for k in range(4): b+=f'<path d="M{330+k*30} {300+k*30} q50 -10 90 30" stroke="#ff90b8" stroke-width="10" fill="none" opacity=".6"/>'
b+='<path d="M400 470 L330 430 L340 500Z M400 470 L470 430 L460 500Z" fill="#8a2ae8"/><circle cx="400" cy="470" r="14" fill="#6a12c8"/>'
b+=sparkle(600,200,22,'#fff')+sparkle(200,560,18,'#fff')+sparkle(620,560,14,'#fff')
I[1191]=svg(b,d)

# 1454 恋 (2016): a newly-wed couple doing the famous little hand dance, small hearts popping between them
d,b=bg([(0,'#fff2c8'),(.6,'#ffd88a'),(1,'#ffb07a')])
b+=rays(400,420,18,'#ffffff',.25,8)
b+=figure(300,740,330,'#3a1a2a',pose='wave')+figure(500,740,320,'#3a1a2a',pose='up',hair='#3a1a2a')
b+='<rect y="740" width="800" height="60" fill="#c87a4a"/>'
for x,y,s,c in [(400,270,38,'#ff4a6a'),(330,180,22,'#ff7a8a'),(480,200,26,'#ff5a7a'),(400,130,16,'#ff9aa8')]: b+=heart(x,y,s,c)
I[1454]=svg(b,d)

# 1461 Lemon (2018): a single lemon resting in a pool of soft light on deep teal, a clear tear-drop falling beside it
d,b=bg([(0,'#082a2a'),(1,'#0a4a4a')])
b+=glow(400,450,240,'#f8f0a0',.3)
d+=rg('lm',S((0,'#fff8a0'),(.55,'#ffd820'),(1,'#c89a00')),.38,.32,.75)
b+='<ellipse cx="400" cy="640" rx="230" ry="30" fill="#000" opacity=".35"/>'
b+='<g transform="rotate(-18 400 460)"><path d="M180 460 Q170 430 200 420 Q260 300 400 296 Q540 300 600 420 Q630 430 620 460 Q630 490 600 500 Q540 620 400 624 Q260 620 200 500 Q170 490 180 460Z" fill="url(#lm)"/>'
b+='<ellipse cx="330" cy="380" rx="70" ry="26" fill="#fff" opacity=".35" transform="rotate(-14 330 380)"/>'
b+='<path d="M600 420 q30 -30 60 -26 q-14 26 -40 36Z" fill="#5a9a3a"/></g>'
b+='<path d="M640 150 Q680 220 640 240 Q600 220 640 150Z" fill="#bff0f0" opacity=".85"/>'
I[1461]=svg(b,d)

# 1518 夜に駆ける (2019): a girl runs along a rooftop edge toward a deep blue night sky full of stars
d,b=bg([(0,'#04061a'),(.6,'#1a1a5a'),(1,'#5a2a7a')])
b+=starsf(110,1518,620,'#e8e0ff')+moon(600,180,46,'#f4f0ff',.4)
b+=skyline(700,'#0a0a2a',1518,40,200,'#ff9ad8',90)
b+='<path d="M-10 640 L560 600 L560 810 L-10 810Z" fill="#05061a"/><path d="M-10 640 L560 600" stroke="#ff7ad8" stroke-width="3" opacity=".6"/>'
b+=f'<g transform="rotate(12 360 610)">{figure(360,612,330,"#020210",pose="reach",hair="#020210")}</g>'
for k in range(5): b+=f'<path d="M{250-k*40} {560+k*6} l-60 4" stroke="#ff9ad8" stroke-width="4" opacity="{.6-k*.1:.1f}" stroke-linecap="round"/>'
I[1518]=svg(b,d)

# 1488 Pretender (2019): a sunset street, two silhouettes standing apart, one turning back toward the other who walks away
d,b=bg([(0,'#3a2a6a'),(.5,'#c85a6a'),(1,'#ffb06a')])
b+=hinomaru_sun(400,520,140,'#ffd08a',.9)+glow(400,520,240,'#ffb07a',.5)
b+=skyline(600,'#3a1a3a',1488,60,240,'#ffd27a',50)
b+='<path d="M-10 810 L330 600 L470 600 L810 810Z" fill="#2a1428"/>'
b+='<path d="M398 610 L402 610 L420 810 L380 810Z" fill="#ffd08a" opacity=".5"/>'
b+=figure(250,770,280,'#14060f')+figure(560,700,200,'#14060f',hair='#14060f')
b+='<path d="M300 500 L400 470" stroke="#fff" stroke-dasharray="6 10" stroke-width="3" opacity=".5"/>'
I[1488]=svg(b,d)

# 1543 唱 (2023): the kanji 唱 blazing as a neon sign above a vintage stage microphone, sound waves bursting outward
d,b=bg([(0,'#0a0006'),(.6,'#2a0412'),(1,'#4a0818')])
b+=rays(400,560,20,'#ff3a5a',.12,5)
for k in range(5): b+=f'<circle cx="400" cy="430" r="{120+k*60}" fill="none" stroke="#ff4a6a" stroke-width="5" opacity="{.5-k*.08:.2f}"/>'
b+=neon(400,330,'唱','#ff2a4a',260)
b+=enka_mic(400,470,90,'#d8d8e0')
I[1543]=svg(b,d)

# 1584 Bling-Bang-Bang-Born (2024): a giant golden cream puff exploding with bling sparkles and confetti
d,b=bg([(0,'#1a1040'),(.6,'#3a1a6a'),(1,'#6a2a8a')])
b+=rays(400,440,24,'#ffe05a',.14,5)+glow(400,440,220,'#ffd84a',.45)
d+=rg('cp',S((0,'#ffe8a0'),(.6,'#e8a63a'),(1,'#9a5a14')),.4,.3,.75)
b+='<ellipse cx="400" cy="520" rx="230" ry="110" fill="url(#cp)"/>'
b+='<path d="M170 480 '+' '.join(f'Q{170+k*46+23} {(440 if k%2 else 520)} {170+(k+1)*46} 480' for k in range(10))+' Q400 540 170 480Z" fill="#fffaf0"/>'
b+='<path d="M200 450 Q190 380 250 340 Q270 290 340 292 Q380 260 440 280 Q520 270 556 330 Q620 370 600 450 Q500 420 400 430 Q300 420 200 450Z" fill="url(#cp)"/>'
b+='<path d="M300 330 l30 26 M430 300 l-20 30 M520 360 l-34 14" stroke="#9a5a14" stroke-width="6" opacity=".5" stroke-linecap="round"/>'
b+=ellipse_dots(400,300,90,16,22,'#ffffff',6,.9)
b+='<path d="M260 380 Q300 320 380 312" stroke="#fff6d8" stroke-width="12" fill="none" stroke-linecap="round" opacity=".6"/>'
for x,y,s in [(170,230,40),(640,220,48),(620,640,30),(180,650,28),(400,180,24)]: b+=sparkle(x,y,s,'#fff2a0')
b+=confetti(40,1584,['#ffe05a','#ff5ab8','#5ae8ff','#ffffff'])
I[1584]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
