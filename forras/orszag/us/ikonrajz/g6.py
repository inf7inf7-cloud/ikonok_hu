import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 6. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 120 Baby Love (The Supremes, 1964): three women in matching sequined gowns at one mic, a pink Motown spotlight
d,b=bg([(0,'#2a0a2a'),(1,'#d86aa0')])
b+=spotlight(400,0,280,'#ffe0f0',.22)+'<ellipse cx="400" cy="720" rx="260" ry="34" fill="#fff" opacity=".18"/>'
for x in (290,400,510): b+=figure(x,720,330,'#1a061a',pose='stand',hair='#1a061a')+''.join(f'<circle cx="{x-16+(k%3)*16}" cy="{520+(k//3)*24}" r="3" fill="#ffd8f0"/>' for k in range(12))
b+=mic(400,500,50,'#d8d8e0')
I[120]=svg(b,d)

# 121 We Are Never Ever Getting Back Together (Taylor Swift, 2012): a phone screen showing an ignored call from an ex, a cardigan and a cracked heart sticker, bright retro pastel
d,b=bg([(0,'#ffd0e0'),(1,'#c0e8ff')])
b+='<g transform="translate(400 420) rotate(-10)"><rect x="-140" y="-250" width="280" height="500" rx="36" fill="#1a1a2a"/><rect x="-120" y="-210" width="240" height="410" rx="10" fill="#f6f2f8"/>'
b+='<circle cx="0" cy="-100" r="50" fill="#c8c0d0"/><rect x="-80" y="-30" width="160" height="20" rx="8" fill="#8a8a9a"/><circle cx="-60" cy="120" r="34" fill="#e0102a"/><circle cx="60" cy="120" r="34" fill="#c8c0d0"/>'
b+='<path d="M-76 104 L-44 136 M-44 104 L-76 136" stroke="#fff" stroke-width="8"/></g>'+heart(620,180,40,'#ff4a7a')+'<path d="M620 150 L610 180 L630 200 L620 220" stroke="#ffd0e0" stroke-width="6" fill="none"/>'
I[121]=svg(b,d)

# 122 Bye Bye Bye (NSYNC, 2000): five boy-band figures dangling from marionette strings, a giant hand above, hot red backdrop
d,b=bg([(0,'#4a0004'),(1,'#d8202a')])
b+='<path d="M140 120 L660 120 L660 150 L140 150Z" fill="#1a0004"/>'
for k,x in enumerate((200,300,400,500,600)):
    b+=f'<path d="M{x-30} 150 L{x-38} {440} M{x+30} 150 L{x+38} 440 M{x} 150 L{x} 430" stroke="#f2e6d8" stroke-width="2" opacity=".8"/>'+figure(x,720,280,'#0a0002',pose='up')
I[122]=svg(b,d)

# 123 Without Me (Eminem, 2002): a comic-book superhero cape and mask in bold pop-art dots, a big 'POW' burst
d,b=bg([(0,'#ffe12a'),(1,'#ff8a2a')])
for i in range(20):
    for j in range(20): b+=f'<circle cx="{i*40+20}" cy="{j*40+20}" r="6" fill="#e0102a" opacity=".25"/>'
b+='<path d="M400 120 L450 260 L600 210 L510 330 L660 400 L500 430 L560 580 L420 480 L330 620 L320 460 L150 480 L270 360 L140 250 L310 280Z" fill="#fff" stroke="#0a0a0a" stroke-width="10"/>'
b+='<path d="M280 360 Q400 300 520 360 Q520 430 470 430 Q430 420 400 400 Q370 420 330 430 Q280 430 280 360Z" fill="#1a3aa8" stroke="#0a0a0a" stroke-width="8"/><ellipse cx="350" cy="380" rx="26" ry="16" fill="#fff"/><ellipse cx="450" cy="380" rx="26" ry="16" fill="#fff"/>'
I[123]=svg(b,d)

# 124 Don't Stop Believin' (Journey, 1981): a midnight train leaving a small-town station, a streetlight and a lone figure on the platform
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
b+=starsf(70,124,420)+moon(640,130,34)
b+='<rect y="560" width="800" height="240" fill="#0a0e18"/><path d="M0 640 L800 600 M0 680 L800 640" stroke="#6a6a7a" stroke-width="5"/>'
b+='<g fill="#3a4a6a"><rect x="40" y="440" width="520" height="160" rx="16"/></g>'+''.join(f'<rect x="{70+k*90}" y="470" width="60" height="50" fill="#ffd27a" opacity=".8"/>' for k in range(5))
b+='<rect x="560" y="470" width="80" height="130" rx="10" fill="#3a4a6a"/>'+glow(640,520,30,'#fff2c0',.9,'glow2')
b+='<path d="M720 800 L720 360" stroke="#1a1a24" stroke-width="10"/>'+glow(720,350,50,'#ffe0a0',.8)+figure(690,700,170,'#04060c',pose='stand')
I[124]=svg(b,d)

# 126 Jump Around (House of Pain, 1992): a crowd jumping as one, sneakers in the air, green shamrock lights
d,b=bg([(0,'#04140a'),(1,'#1a6a3a')])
for x in (200,600): b+=spotlight(x,0,150,'#aaffc0',.12)
r=random.Random(126)
for k in range(14):
    x=40+k*56;y=r.uniform(560,660);b+=f'<g transform="translate({x} {y})">'+figure(0,0,170,'#020a04',pose='up')+'</g>'
b+='<rect y="720" width="800" height="80" fill="#020a04"/>'
for x,y in ((160,180),(640,200)): b+=''.join(f'<circle cx="{x+22*math.cos(a):.0f}" cy="{y+22*math.sin(a):.0f}" r="20" fill="#4aff7a" opacity=".55"/>' for a in (-1.57,0.52,2.62))
I[126]=svg(b,d)

# 127 All I Wanna Do (Sheryl Crow, 1994): a sunny Santa Monica Boulevard bar at noon, a beer glass and a ceiling fan, palms outside
d,b=bg([(0,'#7ad0f0'),(1,'#fff0c0')])
b+=palm(130,560,320,'#2a6a3a',8)+palm(680,560,300,'#2a6a3a',-8)+glow(400,140,90,'#fffbe0',.9)
b+='<rect y="520" width="800" height="280" fill="#6a3a1a"/><rect y="520" width="800" height="20" fill="#8a5a2a"/>'
b+='<path d="M330 380 L470 380 L460 540 Q400 560 340 540Z" fill="#f6c040" opacity=".9"/><path d="M330 380 L470 380 L466 420 L334 420Z" fill="#fff8e8"/>'
b+='<path d="M400 0 L400 80" stroke="#3a2a1a" stroke-width="6"/><ellipse cx="400" cy="90" rx="160" ry="14" fill="#5a3a1a"/>'
I[127]=svg(b,d)

# 130 Heartbreak Hotel (Elvis Presley, 1956): a lonely hotel at the end of Lonely Street, a flickering neon heart sign cracked in two
d,b=bg([(0,'#06061a'),(1,'#1a1a3a')])
b+=starsf(50,130,300)+'<rect x="200" y="200" width="400" height="460" fill="#141428"/>'
for i in range(4):
    for j in range(5): b+=f'<rect x="{230+i*95}" y="{360+j*55}" width="50" height="34" fill="{"#ffd27a" if (i*5+j)%4==0 else "#24243a"}"/>'
b+=heart(400,270,60,'none','stroke="#ff3a7a" stroke-width="10"')+glow(400,270,70,'#ff3a7a',.4)+'<path d="M400 240 L390 270 L410 290 L400 320" stroke="#141428" stroke-width="8" fill="none"/>'
b+='<rect y="660" width="800" height="140" fill="#0a0a14"/><path d="M360 660 L360 600 L440 600 L440 660Z" fill="#ffd27a" opacity=".6"/>'
I[130]=svg(b,d)

# 134 Surfin' U.S.A. (The Beach Boys, 1963): a woodie station wagon with surfboards on the roof at a sunny California beach
d,b=bg([(0,'#4ab8e8'),(1,'#bff0ff')])
b+=glow(620,150,90,'#fffbe0',.9)+'<rect y="420" width="800" height="140" fill="#1a8ac8"/>'+''.join(f'<path d="M{k*90} 450 q22 -14 45 0 q22 14 45 0" stroke="#fff" stroke-width="4" fill="none" opacity=".7"/>' for k in range(10))
b+='<rect y="560" width="800" height="240" fill="#f6dca0"/>'
b+=car(400,720,150,'#8a5a2a','#f2f2f2',glass='#bff0ff')
for k,c in enumerate(('#ffd23a','#e8102a','#3ad8e8')): b+=f'<ellipse cx="{400+(k-1)*10}" cy="{545-k*14}" rx="190" ry="14" fill="{c}"/>'
I[134]=svg(b,d)

# 142 The Way We Were (Barbra Streisand, 1974): faded watercolor photographs scattered on a table, a couple's memory in sepia, soft gold light
d,b=bg([(0,'#3a2a1a'),(1,'#8a6a4a')])
b+=glow(400,300,240,'#ffe8c0',.4)
for x,y,a in ((260,360,-12),(500,330,10),(380,520,-4)):
    b+=f'<g transform="translate({x} {y}) rotate({a})"><rect x="-130" y="-100" width="260" height="210" fill="#f6efe0"/><rect x="-112" y="-84" width="224" height="160" fill="#c8a07a"/>'
    b+=figure(-20,76,130,'#6a4a2a',pose='stand',hair='#6a4a2a')+figure(30,76,140,'#6a4a2a',pose='stand')+'</g>'
I[142]=svg(b,d)

# 144 My Sharona (The Knack, 1979): a bold new-wave poster with a power-pop guitar and big jagged red-black stripes
d,b=bg([(0,'#f2ead8'),(1,'#e8dcc0')])
for k in range(6): b+=f'<path d="M{-100+k*170} 0 L{0+k*170} 0 L{-200+k*170} 800 L{-300+k*170} 800Z" fill="{["#e0102a","#0a0a0a"][k%2]}"/>'
b+=eguitar(400,560,170,'#f2ead8','#0a0a0a',rot=-30)
I[144]=svg(b,d)

# 145 Call Me (Blondie, 1980): a pink payphone receiver dangling off its hook in a neon-lit 1980 street, cord swinging
d,b=bg([(0,'#0a0620'),(1,'#3a1a5a')])
b+=neon('CALL',400,180,110,'#ff3ea5','Arial Black,Arial',False)
b+='<rect x="320" y="260" width="160" height="260" rx="14" fill="#2a2a3a"/><rect x="350" y="300" width="100" height="140" rx="8" fill="#4a4a5a"/>'+''.join(f'<circle cx="{368+(k%3)*32}" cy="{320+(k//3)*32}" r="9" fill="#d8d8e0"/>' for k in range(12))
b+='<path d="M470 400 Q560 520 470 600 Q400 660 460 700" stroke="#ff7ac0" stroke-width="6" fill="none"/><g transform="translate(470 710) rotate(70)"><rect x="-70" y="-14" width="140" height="28" rx="12" fill="#ff7ac0"/><rect x="-80" y="-24" width="36" height="48" rx="12" fill="#ff7ac0"/><rect x="44" y="-24" width="36" height="48" rx="12" fill="#ff7ac0"/></g>'
I[145]=svg(b,d)

# 146 That's What Friends Are For (Dionne Warwick & Friends, 1986): four friends seen from behind, arms around each other's shoulders in a warm glow, a red ribbon above
d,b=bg([(0,'#2a1a3a'),(1,'#c86a6a')])
b+=glow(400,380,240,'#ffe0c0',.6)
for x in (250,350,450,550): b+=figure(x,780,380,'#1a0a14',pose='stand',hair='#1a0a14' if x in (350,550) else None)
b+='<path d="M220 520 Q400 480 580 520" stroke="#1a0a14" stroke-width="22" fill="none" stroke-linecap="round"/>'
b+='<path d="M400 230 Q370 290 350 330 M400 230 Q430 290 450 330" stroke="#e0102a" stroke-width="14" fill="none"/><path d="M400 230 Q360 180 380 160 Q400 170 400 196 Q400 170 420 160 Q440 180 400 230Z" fill="#e0102a"/>'
I[146]=svg(b,d)

# 147 Walk Like an Egyptian (The Bangles, 1987): profile figures striking the classic Egyptian pose before pyramids and a golden sun
d,b=bg([(0,'#3a6ab8'),(.6,'#f2a04a'),(1,'#f6d890')])
b+=glow(400,280,140,'#fff2c0',.8)+'<path d="M80 600 L280 300 L480 600Z" fill="#c8902a"/><path d="M380 600 L560 340 L740 600Z" fill="#a8701a"/>'
b+='<rect y="600" width="800" height="200" fill="#d8b070"/>'
for x in (200,400,600):
    b+=f'<g transform="translate({x} 760)" fill="#1a0e04"><circle cx="0" cy="-270" r="24"/><path d="M-22 -244 L22 -244 L18 -130 L-18 -130Z"/><path d="M-18 -130 L18 -130 L40 0 L22 0 L0 -100 L-30 0 L-46 0Z"/>'
    b+='<path d="M20 -236 L80 -236 L80 -290" stroke="#1a0e04" stroke-width="14" fill="none" stroke-linejoin="round"/><path d="M-20 -230 L-70 -190 L-110 -190" stroke="#1a0e04" stroke-width="14" fill="none" stroke-linejoin="round"/></g>'
I[147]=svg(b,d)

# 149 Hold On (Wilson Phillips, 1990): three women on a cliff top above the sea, hair in the wind, a bright breaking sky
d,b=bg([(0,'#4a7ab8'),(1,'#e8e0d0')])
b+=glow(560,200,140,'#fff8e0',.8)+'<rect y="560" width="800" height="240" fill="#2a5a8a"/>'
b+='<path d="M0 520 L520 480 Q560 600 520 800 L0 800Z" fill="#3a4a2a"/>'
for x in (220,320,420): b+=figure(x,520,230,'#1a1a14',pose='stand',hair='#c8a060')
I[149]=svg(b,d)

# 150 End of the Road (Boyz II Men, 1992): a long empty highway running into a fading sunset, a single rose lying on the asphalt
d,b=bg([(0,'#2a1a3a'),(.6,'#c86a5a'),(1,'#f2b07a')])
b+=glow(400,480,140,'#ffe8c0',.7)+hills(500,10,'#3a1a2a',150,4)+road(400,500,'#1a1418','#f2e0a0',640)
b+='<g transform="translate(400 680) rotate(-20)"><path d="M-70 0 L70 0" stroke="#2a6a2a" stroke-width="6"/><circle cx="-70" cy="0" r="22" fill="#d0102a"/></g>'
I[150]=svg(b,d)

# 151 Too Close (Next, 1998): two silhouettes slow dancing very close on a dim club floor, a single blue light
d,b=bg([(0,'#02040e'),(1,'#0a1a3a')])
b+=spotlight(400,0,170,'#6aa8ff',.18)+'<ellipse cx="400" cy="720" rx="180" ry="28" fill="#6aa8ff" opacity=".2"/>'
b+=figure(375,720,380,'#000',pose='hold',hair='#000')+figure(425,720,400,'#000',pose='hold')
I[151]=svg(b,d)

# 152 Believe (Cher, 1999): a futuristic chrome figure in a laser-lit dance hall, robotic vocal waves rippling out in neon
d,b=bg([(0,'#0a0a2a'),(1,'#3a0a5a')])
for k in range(8): b+=f'<circle cx="400" cy="380" r="{80+k*50}" fill="none" stroke="{["#ff3ad8","#3ad8ff"][k%2]}" stroke-width="5" opacity="{.7-k*.07:.2f}"/>'
d+=lg('chr',S((0,'#ffffff'),(.5,'#9aa0b8'),(1,'#e8e8f0')),0,0,1,0)
b+=figure(400,780,460,'url(#chr)',pose='up',hair='#1a1a2a')
I[152]=svg(b,d)

# 153 Breathe (Faith Hill, 2000): white sheets billowing in a breeze over a quiet country field at golden hour
d,b=bg([(0,'#f2c08a'),(1,'#f6e8c8')])
b+=glow(600,300,140,'#fff8e0',.9)+hills(560,24,'#c8a050',153,4)+hills(620,18,'#a88040',154,5)
b+='<path d="M100 200 L700 220" stroke="#5a4a3a" stroke-width="4"/>'
b+='<path d="M160 204 Q220 300 180 420 Q260 380 320 430 Q300 320 340 210Z" fill="#fbf8f0" opacity=".95"/><path d="M420 212 Q500 330 460 460 Q560 410 640 470 Q600 330 640 218Z" fill="#fbf8f0" opacity=".9"/>'
I[153]=svg(b,d)

# 154 Hanging by a Moment (Lifehouse, 2001): a figure dangling from a single rope over a vast misty canyon at dawn
d,b=bg([(0,'#2a3a5a'),(1,'#d8c0a0')])
b+='<path d="M0 0 L200 0 L240 300 L160 800 L0 800Z M800 0 L600 0 L560 340 L640 800 L800 800Z" fill="#2a2024"/>'
b+='<ellipse cx="400" cy="700" rx="400" ry="120" fill="#f2e8e0" opacity=".5" filter="url(#glow)"/>'
b+='<path d="M220 60 Q400 120 580 60" stroke="#8a6a4a" stroke-width="5" fill="none"/><path d="M400 104 L400 300" stroke="#c8a06a" stroke-width="4"/>'
b+=figure(400,560,240,'#1a1418',pose='up')
I[154]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
