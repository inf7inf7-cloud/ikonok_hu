import sys,math,random;sys.path[:0]=['/mnt/project-files/natsumero/motor/ikonrajz','/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# Natsumero: 28. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 79 禁じられた恋: two hands almost touching through iron gate bars at dusk, late-60s muted palette
d,b=bg([(0,'#5a4a6a'),(1,'#c8a8a8')])
b+=''.join(f'<rect x="{x}" y="0" width="16" height="800" fill="#1a1a24"/><circle cx="{x+8}" cy="40" r="14" fill="#1a1a24"/>' for x in range(60,800,90))+'<rect y="120" width="800" height="16" fill="#1a1a24"/>'
b+='<g fill="#f0c8b0"><path d="M-10 420 L330 400 Q350 400 350 420 Q350 440 330 440 L-10 460Z"/><path d="M810 440 L470 420 Q450 420 450 440 Q450 460 470 460 L810 480Z"/></g>'
I[79]=svg(b,d)

# 210 青春の影: a young man's long shadow cast across an empty station platform at sunset
d,b=bg([(0,'#ff9a6a'),(1,'#ffe0b0')])
b+=hinomaru_sun(640,300,70,'#fff2c8',.8)+'<rect y="440" width="800" height="360" fill="#9a8a7a"/><rect y="440" width="800" height="20" fill="#e8d8a8"/>'
b+=figure(560,600,240,'#1a1010')+'<path d="M540 600 L80 720 L100 760 L580 610Z" fill="#1a1010" opacity=".35"/><rect x="200" y="300" width="12" height="160" fill="#3a2a2a"/><rect x="150" y="290" width="110" height="34" fill="#f4f0e8"/>'
I[210]=svg(b,d)

# 263 大空と大地の中で: a tiny figure in a vast Hokkaido plain under an enormous sky with one tree
d,b=bg([(0,'#2a8ae8'),(1,'#c8e8ff')])
b+=cloud(200,200,2)+cloud(620,260,1.6)+'<rect y="560" width="800" height="240" fill="#8ab84a"/><path d="M-10 560 Q400 540 810 560" stroke="#6a9a3a" stroke-width="6" fill="none"/>'
b+='<rect x="590" y="480" width="10" height="80" fill="#3a2a1a"/><circle cx="595" cy="470" r="34" fill="#3a7a2a"/>'+figure(300,600,70,'#1a1a1a')
I[263]=svg(b,d)

# 755 旅立ちの唄: a young figure with a bag stepping onto a train platform as cherry petals blow, morning
d,b=bg([(0,'#bfe0ff'),(1,'#fff4f0')])
b+='<rect x="460" y="300" width="340" height="300" fill="#e8eef8"/><rect x="460" y="340" width="340" height="16" fill="#3a8a5a"/>'+''.join(f'<rect x="{x}" y="380" width="70" height="80" fill="#9ab8d8"/>' for x in (490,590,690))
b+='<rect y="600" width="800" height="200" fill="#b8b8b8"/>'+petals(20,755,'#ffb8cc',80,600)+figure(320,680,280,'#2a2a3a')+'<rect x="340" y="560" width="50" height="40" fill="#5a3a2a"/>'
I[755]=svg(b,d)

# 1078 ラック: a pair of dice and a four-leaf clover on a casino-green table, warm lamp
d,b=bg([(0,'#1a3a2a'),(1,'#0a2a1a')])
b+=glow(400,300,300,'#ffd27a',.25)
for x,y,a,n in [(300,420,-15,5),(470,400,12,6)]:
    b+=f'<g transform="rotate({a} {x} {y})"><rect x="{x-60}" y="{y-60}" width="120" height="120" rx="18" fill="#fff"/>'+''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="11" fill="#c8102a"/>' for dx,dy in ([(-30,-30),(30,-30),(0,0),(-30,30),(30,30)] if n==5 else [(-30,-30),(30,-30),(-30,0),(30,0),(-30,30),(30,30)]))+'</g>'
b+=''.join(f'<g transform="rotate({a} 400 620)"><path d="M400 620 Q360 580 380 556 Q400 546 400 576 Q400 546 420 556 Q440 580 400 620Z" fill="#4ad84a"/></g>' for a in (0,90,180,270))
I[1078]=svg(b,d)

# 1148 アカツキの詩: a dawn horizon cracking open with gold light over a dark sea, a lone sailboat
d,b=bg([(0,'#0a1a3a'),(.55,'#ff8a5a'),(1,'#ffd890')])
b+=hinomaru_sun(400,480,90,'#fff4c8')+rays(400,480,26,'#fff',.15,10)+'<rect y="480" width="800" height="320" fill="#1a2a4a"/><rect x="340" y="480" width="120" height="320" fill="#ffd890" opacity=".25"/>'
b+='<path d="M560 600 L640 600 L620 620 L580 620Z" fill="#000"/><path d="M600 600 L600 500 L640 590Z" fill="#000"/>'
I[1148]=svg(b,d)

# 1168 LOVE & TRUTH: a girl with an acoustic guitar standing in rain under a single streetlight, sincere
d,b=bg([(0,'#1a2a3a'),(1,'#3a4a5a')])
b+=rain(70,1168,'#c8d8ff',.4)+'<rect x="590" y="140" width="12" height="520" fill="#1a1a1a"/><rect x="540" y="130" width="70" height="16" fill="#1a1a1a"/>'+glow(560,160,160,'#ffd27a',.4)+'<polygon points="560,160 420,660 700,660" fill="#ffd27a" opacity=".12"/>'
b+='<rect y="660" width="800" height="140" fill="#1a1a24"/>'+figure(420,680,320,'#000',pose='hold')+guitar(420,540,.8,-25,'#8a5a2a')
I[1168]=svg(b,d)

# 1377 Make or Break: a figure balancing on a cracked tightrope above a dark abyss, a red and white split background
d,b=bg([(0,'#1a1a1a'),(1,'#3a3a3a')])
b+='<polygon points="0,0 800,0 0,800" fill="#c8102a"/><path d="M-10 420 L810 380" stroke="#e8e8e8" stroke-width="6"/>'+bolt([(520,380),(540,420),(520,450),(550,500)],'#e8e8e8',3)
b+=figure(380,412,240,'#000',pose='up')
I[1377]=svg(b,d)

# 1617 Memorial: a scrapbook of photo frames hung on a string with clothes pins, warm fairy lights
d,b=bg([(0,'#3a2a3a'),(1,'#6a4a5a')])
b+='<path d="M-10 200 Q400 320 810 200" stroke="#c8a87a" stroke-width="3" fill="none"/>'+''.join(f'<circle cx="{x}" cy="{200+120*(1-((x-400)/410)**2):.0f}" r="7" fill="#ffd27a"/>'+glow(x,200+120*(1-((x-400)/410)**2),18,'#ffd27a',.5) for x in range(40,800,60))
for k,x in enumerate((140,320,500,660)):
    y=200+120*(1-((x-400)/410)**2)
    b+=f'<g transform="rotate({(k-1.5)*6} {x} {y})"><rect x="{x-60}" y="{y+10}" width="120" height="140" fill="#fff"/><rect x="{x-48}" y="{y+22}" width="96" height="90" fill="{["#ffb8a8","#a8d8ff","#ffe8a0","#c8f0b8"][k]}"/><rect x="{x-6}" y="{y-6}" width="12" height="26" fill="#8a6a4a"/></g>'
b+=''.join(figure(x,600,70,'#4a3a4a') for x in ())+'<path d="M-10 620 L810 620" stroke="#000" stroke-width="0"/>'
I[1617]=svg(b,d)

# 1632 REBON: a phoenix-like flame rising out of grey ashes into a bright sky
d,b=bg([(0,'#2a1a3a'),(1,'#ff7a3a')])
b+='<rect y="620" width="800" height="180" fill="#5a5a5a"/>'+''.join(f'<circle cx="{(k*67)%800}" cy="{620+(k*13)%40}" r="{8+k%4*4}" fill="#7a7a7a"/>' for k in range(30))
b+='<path d="M400 620 Q300 500 360 400 Q380 460 400 420 Q380 320 440 240 Q440 340 480 360 Q520 300 500 220 Q600 360 520 500 Q480 580 400 620Z" fill="#ffb02a"/><path d="M400 600 Q350 520 390 460 Q400 500 420 480 Q440 540 400 600Z" fill="#fff4a0"/>'
b+='<path d="M380 380 Q200 300 120 180 Q260 250 380 330Z M460 360 Q620 260 700 140 Q580 240 470 320Z" fill="#ff6a2a" opacity=".85"/>'
I[1632]=svg(b,d)

# 1795 CORE PRIDE: a glowing core inside a cracked rock held up by a fist, sparks flying
d,b=bg([(0,'#0a0a14'),(1,'#2a1a1a')])
b+='<path d="M260 300 L340 220 L480 230 L560 320 L540 460 L440 520 L300 500 L240 400Z" fill="#3a3a44"/>'+bolt([(400,230),(380,330),(420,360),(400,500)],'#ff8a2a',8)+glow(400,370,160,'#ff6a1a',.6)+'<circle cx="400" cy="370" r="40" fill="#ffd02a"/>'
b+='<g fill="#000"><rect x="330" y="540" width="140" height="100" rx="30"/><rect x="360" y="620" width="80" height="200"/></g>'+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#ffb02a"/>' for x,y in [(200,240),(620,200),(580,500),(220,520),(660,360)])
I[1795]=svg(b,d)

# 109 危険なふたり: a man and a woman's silhouettes in a fast red car at night, an older woman and young man, glam 70s
d,b=bg([(0,'#1a0a1a'),(1,'#4a1a3a')])
b+=''.join(f'<path d="M0 {y} L800 {y}" stroke="#ff4a8a" stroke-width="3" opacity=".4"/>' for y in (520,560,600))+'<rect y="640" width="800" height="160" fill="#14141a"/>'
b+='<path d="M140 660 L200 560 L480 550 L560 600 L660 610 L660 680 L140 680Z" fill="#c8102a"/>'+ring(250,690,36,'#000',18)+ring(560,690,36,'#000',18)+'<g fill="#000"><circle cx="300" cy="510" r="24"/><circle cx="390" cy="506" r="24"/><path d="M370 490 Q390 470 420 500 L430 560 L410 560Z"/></g>'
I[109]=svg(b,d)

# 456 じゃあね: a group of schoolgirls' silhouettes waving goodbye at a school gate with cherry blossoms, graduation
d,b=bg([(0,'#ffd8e4'),(1,'#fff6f0')])
b+='<rect x="40" y="280" width="40" height="380" fill="#b8b0a8"/><rect x="720" y="280" width="40" height="380" fill="#b8b0a8"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="60" fill="#ffc2d6"/>' for x,y in [(60,240),(140,200),(660,200),(740,240)])
b+='<rect y="660" width="800" height="140" fill="#d8c8b8"/>'+petals(20,456,'#ffb8cc',80,660)+''.join(figure(x,720,200,'#2a2a4a',pose='wave' if k%2==0 else 'stand') for k,x in enumerate((220,320,420,520,600)))
I[456]=svg(b,d)

# 626 晴天を誉めるなら夕暮れを待て: a figure sitting on a hill waiting as a clear day turns to a crimson sunset
d,b=bg([(0,'#3a8ae8'),(.5,'#ffb06a'),(1,'#e8402a')])
b+=hinomaru_sun(560,520,80,'#fff0c0',.8)+'<path d="M-10 640 Q300 560 810 620 L810 810 L-10 810Z" fill="#2a1a1a"/><g fill="#000"><circle cx="240" cy="560" r="22"/><path d="M220 582 L260 582 L280 630 L210 630Z"/></g>'
I[626]=svg(b,d)

# 1155 虹: a rainbow arching between two hands reaching from opposite sides, rain clearing
d,b=bg([(0,'#8ab8e8'),(1,'#e8f4ff')])
b+=''.join(f'<path d="M140 620 A260 260 0 0 1 660 620" stroke="{c}" stroke-width="22" fill="none" transform="translate(0 {k*22})"/>' for k,c in enumerate(['#ff5a5a','#ffa82a','#ffe85a','#5ad85a','#5aa8ff','#8a5aff']))
b+=cloud(160,620,1.4)+cloud(640,640,1.4)+''.join(f'<path d="M{x} {y} L{x-4} {y+14}" stroke="#7a9ac8" stroke-width="3"/>' for x,y in [(120,140),(200,200),(600,160),(700,120),(660,220)])
I[1155]=svg(b,d)

# 1178 そばにいるね: two phones side by side with speech bubbles of hearts, a cosy pink room
d,b=bg([(0,'#ffd8e4'),(1,'#fff0f4')])
b+='<rect y="560" width="800" height="240" fill="#e8c8c8"/>'+''.join(f'<rect x="{x}" y="300" width="160" height="290" rx="24" fill="#2a2a3a"/><rect x="{x+14}" y="330" width="132" height="230" fill="{c}"/>' for x,c in [(180,'#c8e8ff'),(460,'#ffe0ec')])
b+='<rect x="210" y="360" width="100" height="40" rx="18" fill="#fff"/><rect x="490" y="420" width="100" height="40" rx="18" fill="#ff8ab8"/>'+heart(260,380,12,'#ff4a7a')+heart(540,440,12,'#fff')+heart(400,220,40,'#ff6a9a')
I[1178]=svg(b,d)

# 1618 Waltz for Lily: white lilies and a pair of dancing shoes on a ballroom floor with chandelier light
d,b=bg([(0,'#2a1a3a'),(1,'#5a3a6a')])
b+=glow(400,140,180,'#ffe8b0',.4)+''.join(f'<circle cx="{400+k*30-90}" cy="{150+abs(k-3)*-10+30}" r="8" fill="#ffe8b0"/>' for k in range(7))+'<rect y="560" width="800" height="240" fill="#6a4a3a"/>'
for x,y in [(260,420),(340,380),(300,460)]: b+=''.join(f'<path d="M{x} {y} Q{x+30*math.cos(a):.0f} {y+30*math.sin(a):.0f} {x+56*math.cos(a):.0f} {y+56*math.sin(a):.0f} Q{x+30*math.cos(a+.5):.0f} {y+30*math.sin(a+.5):.0f} {x} {y}Z" fill="#fff"/>' for a in [k*1.05-1.6 for k in range(6)])
b+='<path d="M300 480 L300 600" stroke="#4a8a3a" stroke-width="6"/><path d="M480 640 Q520 600 580 620 L590 650 L480 650Z M560 670 Q600 630 660 650 L670 680 L560 680Z" fill="#e8d8c8"/>'
I[1618]=svg(b,d)

# 1619 halfmoon: a half moon over a quiet city rooftop where a figure sits with headphones
d,b=bg([(0,'#0a0a2a'),(1,'#2a2a5a')])
b+=starsf(60,1619,500)+'<circle cx="560" cy="200" r="90" fill="#fff4c8"/><rect x="560" y="100" width="100" height="200" fill="#121238"/>'+skyline(620,'#0a0a1a',1619,60,200,'#ffd27a',40)
b+='<rect x="120" y="560" width="360" height="60" fill="#1a1a2a"/><g fill="#000"><circle cx="300" cy="500" r="22"/><path d="M280 522 L320 522 L330 560 L270 560Z"/></g><path d="M278 494 Q300 466 322 494" stroke="#4ad8ff" stroke-width="5" fill="none"/>'
I[1619]=svg(b,d)

# 1724 BE TOGETHER: hands of a crowd joined in a circle seen from above, bright neon dance colours
d,b=bg([(0,'#ff4fa0'),(1,'#7a4aff')])
b+=''.join(f'<path d="M400 400 L{400+300*math.cos(a):.0f} {400+300*math.sin(a):.0f}" stroke="#fff" stroke-width="2" opacity=".3"/>' for a in [k*.39 for k in range(16)])
b+=ring(400,400,200,'#fff',6)+''.join(f'<circle cx="{400+200*math.cos(a):.0f}" cy="{400+200*math.sin(a):.0f}" r="34" fill="#1a0a2a"/>' for a in [k*math.pi/4 for k in range(8)])+star5(400,400,60,'#ffe86a')
I[1724]=svg(b,d)

# 1781 Journey through the Decade: a tunnel of clock-like rings and film frames receding into light, a figure walking in
d,b=bg([(0,'#0a0a14'),(1,'#1a1a2a')])
b+=''.join(ring(400,400,r2,'#c8a85a' if k%2 else '#8a8aa8',8,.8-k*.08) for k,r2 in enumerate(range(380,40,-40)))+glow(400,400,60,'#fff',.8)+figure(400,620,180,'#000')
I[1781]=svg(b,d)

# 1860 セレナーデ: a guitarist serenading below a lit balcony window at night, moon and roses
d,b=bg([(0,'#0a1a3a'),(1,'#2a2a5a')])
b+=moon(160,140,40)+'<rect x="420" y="100" width="300" height="560" fill="#2a2a44"/><rect x="480" y="180" width="180" height="200" fill="#ffd27a"/><rect x="460" y="380" width="220" height="16" fill="#e8e0d0"/>'+''.join(f'<rect x="{x}" y="396" width="8" height="60" fill="#e8e0d0"/>' for x in range(470,680,24))
b+='<rect y="660" width="800" height="140" fill="#14142a"/>'+figure(240,680,300,'#000',pose='hold')+guitar(240,560,.7,-25,'#8a5a2a')+''.join(flower(x,456,14,5,'#e8304a','#8a0a1a') for x in (480,540,600,660))
I[1860]=svg(b,d)

# 1890 田園: a wide rice paddy field with a narrow ridge path and a figure walking under a summer sky
d,b=bg([(0,'#5ab8ff'),(1,'#e8f6ff')])
b+=cloud(560,160,1.8)+hills(420,30,'#5a8a6a',1890)+'<rect y="440" width="800" height="360" fill="#7ac84a"/>'+''.join(f'<path d="M{x} 800 L400 440" stroke="#5aa83a" stroke-width="3"/>' for x in range(-400,1200,80))
b+='<path d="M380 440 L420 440 L460 800 L340 800Z" fill="#c8b07a"/>'+figure(410,620,160,'#2a2a1a')
I[1890]=svg(b,d)

# 320 蒼氓: a crowd of ordinary people walking on a wide city crossing seen from above, blue-grey dusk
d,b=bg([(0,'#3a4a6a'),(1,'#6a7a9a')])
b+=''.join(f'<rect x="{80+k*70}" y="300" width="40" height="200" fill="#e8e8f0" opacity=".6"/>' for k in range(10))
r=random.Random(320)
b+=''.join(f'<circle cx="{r.randint(40,760)}" cy="{r.randint(200,620)}" r="{r.randint(10,14)}" fill="#14182a"/>' for k in range(70))
I[320]=svg(b,d)

# 437 HEART OF RAINBOW: a heart-shaped rainbow bridge with a couple crossing it, mid-80s pastel
d,b=bg([(0,'#c8e0ff'),(1,'#fff0f8')])
for k,c in enumerate(['#ff5a5a','#ffa82a','#ffe85a','#5ad85a','#5aa8ff','#8a5aff']):
    s2=1-k*.08;b+=f'<g transform="translate(400 420) scale({s2}) translate(-400 -420)">'+heart(400,420,240,'none',f'stroke="{c}" stroke-width="20"')+'</g>'
b+=figure(320,260,90,'#2a2a3a')+figure(360,260,90,'#2a2a3a')
I[437]=svg(b,d)

# 582 渡良瀬橋: a long bridge over a river at sunset with a girl's silhouette on the bank, a small town
d,b=bg([(0,'#ff9a7a'),(1,'#ffe0c0')])
b+=hinomaru_sun(560,380,70,'#fff2c8',.8)+'<rect y="440" width="800" height="200" fill="#8aa8c8"/><rect y="640" width="800" height="160" fill="#6a8a4a"/>'
b+='<rect x="-10" y="400" width="820" height="18" fill="#3a3a4a"/>'+''.join(f'<rect x="{x}" y="418" width="12" height="60" fill="#3a3a4a"/>' for x in range(40,800,120))+''.join(f'<path d="M{x} 400 Q{x+60} 340 {x+120} 400" stroke="#3a3a4a" stroke-width="6" fill="none"/>' for x in range(-20,800,120))
b+=figure(260,720,200,'#1a1a1a')
I[582]=svg(b,d)

# 623 if: a figure standing at a crossroads of light paths under a dark sky, one path glowing
d,b=bg([(0,'#1a1a3a'),(1,'#3a3a5a')])
b+='<path d="M400 800 L400 520 L120 300 M400 520 L680 300 M400 520 L400 200" stroke="#5a5a7a" stroke-width="40" fill="none" stroke-linejoin="round"/><path d="M400 520 L680 300" stroke="#ffd27a" stroke-width="40"/>'+glow(680,300,80,'#ffd27a',.6)+figure(400,600,200,'#000')
I[623]=svg(b,d)

# 767 優しいあの子: a girl's silhouette in a wide northern meadow with a red-crowned crane flying overhead
d,b=bg([(0,'#9ad0ff'),(1,'#f0faff')])
b+='<path d="M-10 600 Q400 540 810 600 L810 810 L-10 810Z" fill="#9ac86a"/>'+figure(260,660,200,'#3a3a4a')
b+='<g transform="translate(520 240)"><ellipse cx="0" cy="0" rx="60" ry="16" fill="#fff"/><path d="M-20 -6 Q-80 -110 -160 -90 Q-90 -40 -30 0Z M20 -6 Q80 -110 160 -100 Q90 -40 30 0Z" fill="#fff"/><path d="M-160 -90 L-130 -70 M160 -100 L130 -80" stroke="#000" stroke-width="10"/><path d="M60 0 L120 -20" stroke="#000" stroke-width="5"/><circle cx="118" cy="-22" r="8" fill="#e8102a"/></g>'
I[767]=svg(b,d)

# 882 Over Drive: a girl's silhouette on a scooter racing down a highway with motion streaks, bright pop colours
d,b=bg([(0,'#ffd02a'),(1,'#ff6a9a')])
b+=''.join(f'<path d="M0 {y} L{300+k*40} {y}" stroke="#fff" stroke-width="6" opacity=".6"/>' for k,y in enumerate((300,360,440,520)))+'<rect y="640" width="800" height="160" fill="#3a3a4a"/>'
b+=ring(380,620,36,'#000',12)+ring(560,620,36,'#000',12)+'<path d="M380 620 L420 540 L540 540 L560 620 M520 540 L540 470" stroke="#3a8aff" stroke-width="16" fill="none"/><g fill="#000"><circle cx="460" cy="400" r="24"/><path d="M440 424 L480 424 L500 540 L430 540Z"/></g><path d="M440 390 Q380 380 340 400" stroke="#000" stroke-width="12" fill="none"/>'
I[882]=svg(b,d)

# 1751 陰ニモ日向ニモ: a figure standing exactly on the line between shadow and sunlight on a street
d,b=bg([(0,'#ffd88a'),(1,'#fff4d8')])
b+='<polygon points="0,0 360,0 520,800 0,800" fill="#3a4a6a"/>'+figure(440,700,320,'#1a1a1a')+glow(640,160,140,'#fff',.6)
I[1751]=svg(b,d)

# 1803 HOT LIMIT: a blazing summer beach sign reading LIMIT, a sun at max heat and a heat-shimmer horizon
d,b=bg([(0,'#ff3a1a'),(1,'#ffc83a')])
b+=hinomaru_sun(400,240,130,'#fff4a0')+rays(400,240,30,'#fff',.3,8)+'<rect y="440" width="800" height="100" fill="#1ab0d8"/><rect y="540" width="800" height="260" fill="#ffe0a0"/>'
b+='<rect x="120" y="460" width="12" height="220" fill="#5a3a2a"/><rect x="40" y="460" width="180" height="60" fill="#fff" stroke="#e8102a" stroke-width="8"/>'+txt(130,505,'LIMIT',40,'#e8102a',900)+figure(520,720,260,'#2a1010',pose='up')
I[1803]=svg(b,d)

# 1891 ファンファーレ: golden trumpets raised into a bright morning sky with streamers
d,b=bg([(0,'#4aa8ff'),(1,'#fff8d8')])
for x,a in [(260,-30),(540,30)]:
    b+=f'<g transform="rotate({a} {x} 500)"><rect x="{x-10}" y="300" width="20" height="240" fill="#e8b830"/><path d="M{x-10} 300 L{x-50} 220 L{x+50} 220 L{x+10} 300Z" fill="#ffd040"/></g>'
b+=''.join(f'<path d="M{x} {y} q30 30 0 60 q-30 30 0 60" stroke="{c}" stroke-width="8" fill="none"/>' for x,y,c in [(120,120,'#ff4a6a'),(680,100,'#4ad84a'),(400,80,'#ff8a2a')])+sparkle(400,300,30,'#fff')
I[1891]=svg(b,d)

# 128 モンスター: a cartoon monster's shadow looming on a wall behind two dancing girls in sparkly outfits, late 70s
d,b=bg([(0,'#1a0a3a'),(1,'#5a2a7a')])
b+='<path d="M180 600 L200 200 Q260 100 400 120 Q540 100 600 200 L620 600Z" fill="#2a0a4a"/><circle cx="330" cy="260" r="30" fill="#ffe86a"/><circle cx="470" cy="260" r="30" fill="#ffe86a"/><path d="M300 400 L340 360 L380 400 L420 360 L460 400 L500 360" stroke="#ffe86a" stroke-width="8" fill="none"/>'
b+='<rect y="640" width="800" height="160" fill="#14081f"/>'+figure(320,700,240,'#ff8ad8',pose='up')+figure(480,700,240,'#ff8ad8',pose='up')
I[128]=svg(b,d)

# 803 sweet heart: a glowing heart-shaped candy wrapped in cellophane, against a cool trance-blue background
d,b=bg([(0,'#0a1a4a'),(1,'#3a5aa8')])
b+=''.join(ring(400,400,r2,'#8ad8ff',2,.3) for r2 in (200,260,320))+heart(400,420,130,'#ff6a9a')+heart(380,390,40,'#fff',)+'<path d="M260 420 L180 370 L180 470Z M540 420 L620 370 L620 470Z" fill="#c8e8ff" opacity=".7"/>'
I[803]=svg(b,d)

# 1074 すべてへ: two young men's silhouettes with guitars on a hilltop waving to a wide world below
d,b=bg([(0,'#4ab8ff'),(1,'#f0f8ff')])
b+=cloud(600,160,1.4)+'<rect y="600" width="800" height="200" fill="#8ab86a"/>'+'<path d="M-10 800 L-10 560 Q200 460 440 520 L440 800Z" fill="#4a8a3a"/>'
b+=figure(180,520,200,'#1a1a1a',pose='wave')+figure(300,520,200,'#1a1a1a',pose='wave')
I[1074]=svg(b,d)

# 1285 Story: an open book whose pages turn into a path with a small figure walking into it, warm light
d,b=bg([(0,'#3a2a1a'),(1,'#6a4a2a')])
b+=glow(400,300,240,'#ffd27a',.3)+'<path d="M120 520 Q260 480 400 520 Q540 480 680 520 L680 620 Q540 580 400 620 Q260 580 120 620Z" fill="#f4ead8"/><path d="M400 520 L400 620" stroke="#c8b898" stroke-width="3"/>'
b+='<path d="M380 520 Q360 400 400 300 Q440 200 420 120" stroke="#ffe8b0" stroke-width="30" fill="none" opacity=".7"/>'+figure(410,330,80,'#000')
I[1285]=svg(b,d)

# 1293 Dear...: a letter starting with 'Dear' lying beside a pen and a cup, soft morning window light
d,b=bg([(0,'#fff0e8'),(1,'#f0e0d0')])
b+='<rect y="440" width="800" height="360" fill="#d8b890"/><rect x="200" y="460" width="300" height="260" fill="#fff" transform="rotate(-6 350 590)"/>'+txt(300,540,'Dear',44,'#3a3a5a',400)+''.join(f'<path d="M230 {580+k*30} L460 {560+k*30}" stroke="#c8c8d8" stroke-width="3"/>' for k in range(4))
b+='<rect x="520" y="560" width="160" height="10" fill="#3a3a5a" transform="rotate(-30 600 565)"/><rect x="580" y="460" width="80" height="80" rx="8" fill="#e8f0f8"/>'
I[1293]=svg(b,d)

# 1784 虹: a crowd of people's silhouettes on a hillside looking at a rainbow after rain, puddles shining
d,b=bg([(0,'#7aa8d8'),(1,'#e8f0f8')])
b+=''.join(f'<path d="M40 640 A360 360 0 0 1 760 640" stroke="{c}" stroke-width="22" fill="none" opacity=".75" transform="translate(0 {k*22})"/>' for k,c in enumerate(['#ff5a5a','#ffa82a','#ffe85a','#5ad85a','#5aa8ff','#8a5aff']))
b+='<path d="M-10 640 Q400 600 810 640 L810 810 L-10 810Z" fill="#4a6a4a"/>'+''.join(figure(x,700,160,'#1a1a2a',pose='up' if k==2 else 'stand') for k,x in enumerate((180,290,400,510,620)))
I[1784]=svg(b,d)

# 787 HEAVEN: a white spiral staircase rising into bright clouds, a figure climbing
d,b=bg([(0,'#8ab8e8'),(1,'#fff')])
b+=cloud(200,160,1.8)+cloud(600,120,2)+''.join(f'<rect x="{400+120*math.cos(k*.6)-60:.0f}" y="{760-k*36}" width="120" height="16" fill="#fff" stroke="#c8d0e0" stroke-width="3"/>' for k in range(18))+figure(420,700,90,'#2a2a3a')
I[787]=svg(b,d)

# 1029 孤独のあかつき: a woman's silhouette alone on a dark field watching the first red dawn line break
d,b=bg([(0,'#0a0a1a'),(.7,'#2a1a2a'),(1,'#c8302a')])
b+='<rect x="0" y="600" width="800" height="6" fill="#ff6a3a"/>'+glow(400,600,300,'#ff4a2a',.25)+'<rect y="606" width="800" height="200" fill="#050505"/>'+figure(560,640,240,'#000')
I[1029]=svg(b,d)

# 1181 Beautiful: a woman's silhouette with arms wide open on a cliff before a vast golden sunrise, flowers in the wind
d,b=bg([(0,'#ff8a3a'),(1,'#ffe8a0')])
b+=hinomaru_sun(400,440,140,'#fff6d0')+rays(400,440,30,'#fff',.2,10)+'<path d="M-10 800 L-10 620 Q400 560 810 620 L810 800Z" fill="#3a2a1a"/>'+figure(400,640,320,'#000',pose='up')
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="5" fill="#ff6a8a" transform="rotate(30 {x} {y})"/>' for x,y in [(200,380),(260,320),(560,300),(620,360),(300,260)])
I[1181]=svg(b,d)

for k,v in I.items(): open(f'/tmp/jprajz/svg/{k}.svg','w').write(v)
print(len(I))
