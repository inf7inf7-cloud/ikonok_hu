import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 12. csoport: a maradék videós dalok (2026-10-24)
I={}

# 327 1, 2 Step (Ciara ft. Missy Elliott, 2005): dance footprints numbered 1 and 2 on a glowing Atlanta club floor, a dancer's silhouette
d,b=bg([(0,'#0a0420'),(1,'#3a0a4a')])
for i in range(8):
    for j in range(4): b+=f'<path d="M{i*110-60+j*30} {560+j*60} l110 0 l30 60 l-110 0Z" fill="{["#ff3ad8","#3ad8ff"][(i+j)%2]}" opacity=".3"/>'
b+=figure(400,540,380,'#04020e',pose='wave',hair='#04020e')
for x,y,n in ((260,640,'1'),(520,700,'2')): b+=f'<ellipse cx="{x}" cy="{y}" rx="30" ry="50" fill="#fff" opacity=".85" transform="rotate(-20 {x} {y})"/><text x="{x}" y="{y+14}" font-family="Arial Black,Arial" font-size="40" text-anchor="middle" fill="#3a0a4a">{n}</text>'
I[327]=svg(b,d)

# 328 Buy U a Drank (T-Pain ft. Yung Joc, 2007): a top hat and a glowing cocktail glass with a robotic sound-wave behind, purple club haze
d,b=bg([(0,'#1a0a2a'),(1,'#5a2a7a')])
b+='<path d="M0 300 '+' '.join(f'L{k*20} {300+60*math.sin(k*.8)*((k%3)+1)/3:.0f}' for k in range(41))+'" stroke="#3affd8" stroke-width="6" fill="none" opacity=".7"/>'
b+='<path d="M300 460 L500 460 L410 600 L410 720 L460 740 L340 740 L390 720 L390 600Z" fill="#f2e6ff" opacity=".85"/><path d="M320 476 L480 476 L410 580 L390 580Z" fill="#ff6ac0"/>'
b+='<path d="M260 230 L540 230 L520 250 L280 250Z" fill="#0a0410"/><rect x="320" y="100" width="160" height="140" fill="#0a0410"/><rect x="320" y="200" width="160" height="20" fill="#c8102a"/>'
I[328]=svg(b,d)

# 329 Apologize (OneRepublic, 2008): a crumpled letter and a broken pencil on an empty piano bench, cold gray-blue light
d,b=bg([(0,'#1a2030'),(1,'#4a5a6a')])
b+='<rect x="140" y="440" width="520" height="60" fill="#0a0a10"/><rect x="170" y="500" width="20" height="200" fill="#0a0a10"/><rect x="610" y="500" width="20" height="200" fill="#0a0a10"/>'
b+='<path d="M300 400 L380 380 L420 410 L400 450 L330 455 L290 430Z" fill="#f2f0e8"/><path d="M310 410 L400 420 M320 430 L390 440" stroke="#aaa" stroke-width="3"/>'
b+='<path d="M460 430 L540 420" stroke="#e8c040" stroke-width="12"/><path d="M548 418 L600 426" stroke="#e8c040" stroke-width="12"/><path d="M600 426 L620 428" stroke="#3a2a1a" stroke-width="10"/>'
b+=spotlight(400,0,200,'#cfe0ff',.14)
I[329]=svg(b,d)

# 330 Love Story (Taylor Swift, 2009): a balcony in a castle at dusk with a lantern, a girl in a gown and a boy below with a ring, Romeo-style
d,b=bg([(0,'#2a2a5a'),(.6,'#e88a7a'),(1,'#f6c8a0')])
b+='<rect x="440" y="100" width="300" height="700" fill="#c8b0a0"/><rect x="420" y="380" width="200" height="30" fill="#a89080"/>'+''.join(f'<rect x="{430+k*30}" y="410" width="12" height="60" fill="#a89080"/>' for k in range(7))+'<rect x="420" y="470" width="200" height="16" fill="#a89080"/>'
b+='<path d="M500 380 L500 180 Q560 120 620 180 L620 380Z" fill="#ffd8a0"/>'+figure(560,380,180,'#f6f2ea',pose='stand',hair='#c8a040')
b+=figure(220,780,260,'#1a1020',pose='reach')+hills(700,10,'#3a2a3a',330,3)
I[330]=svg(b,d)

# 331 OMG (Usher ft. will.i.am, 2010): a heart-shaped pair of LED sunglasses pulsing on a club dance floor, robot lasers
d,b=bg([(0,'#04020e'),(1,'#1a0a3a')])
for k in range(12): b+=f'<path d="M400 400 L{400+600*math.cos(k*.524):.0f} {400+600*math.sin(k*.524):.0f}" stroke="{["#3affd8","#ff3ab0"][k%2]}" stroke-width="3" opacity=".5"/>'
b+=heart(280,400,90,'#ff3ab0')+heart(520,400,90,'#ff3ab0')+'<path d="M360 380 L440 380" stroke="#0a0a14" stroke-width="16"/>'
for k in range(16): b+=f'<circle cx="{220+(k%4)*40 + (k//8)*240}" cy="{370+((k//4)%2)*40}" r="6" fill="#fff"/>'
I[331]=svg(b,d)

# 332 Give Me Everything (Pitbull ft. Ne-Yo, 2011): a Miami penthouse party at night, a champagne bottle popping with a spray over the bay
d,b=bg([(0,'#04082a'),(1,'#3a1a6a')])
b+=skyline(580,'#1a1438',332,60,240,'#ff9ae8',90)+'<rect y="620" width="800" height="180" fill="#2a4a8a"/>'+palm(100,640,260,'#04040e',8)
b+='<g transform="translate(560 540) rotate(-30)"><path d="M-30 0 L30 0 L30 -140 Q30 -170 12 -180 L12 -230 L-12 -230 L-12 -180 Q-30 -170 -30 -140Z" fill="#1a4a2a"/><rect x="-14" y="-240" width="28" height="20" fill="#e8c040"/></g>'
for k in range(20): a=math.radians(-150+k*6);b+=f'<circle cx="{470+120*math.cos(a)+k*3:.0f}" cy="{330+120*math.sin(a):.0f}" r="6" fill="#fff2c0" opacity=".8"/>'
I[332]=svg(b,d)

# 334 Counting Stars (OneRepublic, 2014): a man lying in a field counting stars, constellations connected in lines across the night
d,b=bg([(0,'#04061a'),(1,'#1a2a4a')])
b+=starsf(140,334,560)
pts=[(120,120),(220,180),(300,110),(380,200),(470,140),(560,220),(660,120)]
b+='<path d="M'+' L'.join(f'{x} {y}' for x,y in pts)+'" stroke="#bfd8ff" stroke-width="2" fill="none"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff"/>' for x,y in pts)
b+=hills(620,20,'#0a1a14',334,4)
b+='<g transform="translate(400 650) rotate(-90)" fill="#04080a"><circle cx="0" cy="-200" r="18"/><rect x="-20" y="-180" width="40" height="120"/><rect x="-20" y="-60" width="40" height="80"/></g>'
I[334]=svg(b,d)

# 335 Sugar (Maroon 5, 2015): a wedding reception in full swing, a tiered cake with pink icing and sugar cubes heart, fairy lights
d,b=bg([(0,'#fbd8e0'),(1,'#f6efe8')])
b+='<path d="M0 120 Q200 180 400 120 Q600 180 800 120" stroke="#c8a0a8" stroke-width="2" fill="none"/>'+''.join(f'<circle cx="{k*40}" cy="{140+30*math.sin(k*40/800*4*math.pi):.0f}" r="6" fill="#ffe08a"/>' for k in range(21))
for k,(w,y) in enumerate(((320,560),(240,460),(160,370))): b+=f'<rect x="{400-w/2}" y="{y}" width="{w}" height="100" rx="10" fill="#fbf6f2"/><path d="M{400-w/2} {y+20} Q{400} {y+40} {400+w/2} {y+20}" stroke="#ff8ab0" stroke-width="10" fill="none"/>'
b+=heart(400,320,30,'#ff5a8a')+'<rect x="200" y="660" width="400" height="20" fill="#e8d8d0"/>'
I[335]=svg(b,d)

# 336 Stressed Out (Twenty One Pilots, 2016): two young men on tiny tricycles in a suburban street, red beanie, a cassette tape and childhood nostalgia
d,b=bg([(0,'#9ac8e8'),(1,'#f2ead8')])
b+='<rect y="560" width="800" height="240" fill="#8a8a8a"/><path d="M0 620 L800 620" stroke="#fff" stroke-width="6" stroke-dasharray="40 30"/>'
for x in (280,520):
    b+=figure(x,600,240,'#1a1a2a',pose='hold')+f'<path d="M{x-17} 386 Q{x} 362 {x+17} 386Z" fill="#d0102a"/>'
    b+=f'<circle cx="{x-50}" cy="650" r="26" fill="none" stroke="#d0102a" stroke-width="8"/><circle cx="{x+50}" cy="650" r="26" fill="none" stroke="#d0102a" stroke-width="8"/><circle cx="{x}" cy="620" r="36" fill="none" stroke="#d0102a" stroke-width="8"/>'
I[336]=svg(b,d)

# 337 Something Just Like This (The Chainsmokers & Coldplay, 2017): a comic-book superhero cape draped over an ordinary person staring at the cosmos
d,b=bg([(0,'#0a0420'),(1,'#3a1a6a')])
b+=starsf(120,337,600)+'<circle cx="600" cy="200" r="60" fill="#ffb0e0" opacity=".7"/><circle cx="200" cy="260" r="30" fill="#9ad8ff" opacity=".7"/>'
b+=hills(640,20,'#0a0614',337,4)
b+='<path d="M380 400 Q300 560 320 680 L480 680 Q500 560 420 400Z" fill="#d0102a"/>'+figure(400,700,330,'#0a0614',pose='stand')
I[337]=svg(b,d)

# 338 Rockstar (Post Malone ft. 21 Savage, 2018): a smashed electric guitar in front of an amp stack under red-hot stage lights, a sword-like shadow
d,b=bg([(0,'#1a0002'),(1,'#7a0a0a')])
for x in (200,600): b+=spotlight(x,0,120,'#ff4a4a',.18)
b+='<rect x="500" y="300" width="220" height="400" fill="#0a0a0a"/>'+''.join(f'<rect x="520" y="{320+k*130}" width="180" height="110" fill="#1a1a1a"/><circle cx="610" cy="{375+k*130}" r="40" fill="#2a2a2a"/>' for k in range(3))
b+=eguitar(300,580,150,'#f2f2f2','#2a1a0a',rot=40)+'<path d="M220 640 L260 610 L240 660 L290 640" stroke="#fff2c0" stroke-width="4" fill="none"/>'
I[338]=svg(b,d)

# 339 Wow (Post Malone, 2019): a jaw-dropping diamond-encrusted chain glinting, gold and ice on black velvet
d,b=bg([(0,'#04040a'),(1,'#1a1a24')])
b+='<path d="M200 140 Q400 600 600 140" stroke="#e8c040" stroke-width="16" fill="none" stroke-dasharray="20 6"/>'
b+='<path d="M400 420 L470 500 L400 620 L330 500Z" fill="#cfefff" stroke="#fff" stroke-width="5"/><path d="M330 500 L470 500 M400 420 L400 620" stroke="#9ad0ff" stroke-width="3"/>'
for x,y in ((360,460),(450,560),(520,280),(280,300)): b+=sparkle(x,y,24,'#fff')
I[339]=svg(b,d)

# 340 Rockstar (DaBaby ft. Roddy Ricch, 2020): police lights flashing red and blue across a rain-wet street, a silhouette with a crown of light
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a2a')])
b+='<rect width="400" height="800" fill="#d0102a" opacity=".22"/><rect x="400" width="400" height="800" fill="#1a4ad0" opacity=".22"/>'
b+=glow(220,160,120,'#ff2a2a',.6)+glow(580,160,120,'#2a6aff',.6)
b+='<rect y="640" width="800" height="160" fill="#0a0a14"/>'+figure(400,740,420,'#000',pose='stand')+'<path d="M370 300 L370 270 L385 285 L400 260 L415 285 L430 270 L430 300Z" fill="#e8c040"/>'
I[340]=svg(b,d)

# 341 Good 4 U (Olivia Rodrigo, 2021): a cheerleader-uniformed girl with a match in hand in front of a purple house, pop-punk pink and fire
d,b=bg([(0,'#2a0a3a'),(1,'#ff3a8a')])
b+='<path d="M440 640 L440 360 L600 240 L760 360 L760 640Z" fill="#6a3a8a"/>'+glow(600,500,100,'#ff8a2a',.6)+''.join(f'<path d="M{520+k*30} 640 Q{510+k*30} 560 {530+k*30} 500 Q{550+k*30} 560 {540+k*30} 640Z" fill="#ffb03a"/>' for k in range(6))
b+='<rect y="640" width="800" height="160" fill="#1a0614"/>'+figure(240,740,360,'#1a0614',pose='reach',hair='#1a0614')+'<path d="M368 488 L376 470" stroke="#ffd84a" stroke-width="6"/>'+glow(378,466,12,'#ffb03a',.9,'glow2')
I[341]=svg(b,d)

# 342 Creepin' (Metro Boomin, The Weeknd & 21 Savage, 2023): a shadowy figure lurking behind a glowing red-lit window blind, noir slats
d,b=bg([(0,'#0a0004'),(1,'#2a0008')])
b+='<rect x="160" y="120" width="480" height="560" fill="#d0102a" opacity=".55"/>'
b+='<ellipse cx="400" cy="380" rx="110" ry="140" fill="#0a0004"/><path d="M290 680 Q300 520 400 500 Q500 520 510 680Z" fill="#0a0004"/>'
for k in range(14): b+=f'<rect x="160" y="{120+k*40}" width="480" height="18" fill="#1a0006" opacity=".9"/>'
b+='<circle cx="360" cy="360" r="6" fill="#ff4a4a"/><circle cx="440" cy="360" r="6" fill="#ff4a4a"/>'
I[342]=svg(b,d)

# 343 Lovin on Me (Jack Harlow, 2024): a sleek bedroom door with a heart doorknob sign, warm low lights, minimal beige and red
d,b=bg([(0,'#e8d8c0'),(1,'#c8a888')])
b+='<rect x="280" y="140" width="240" height="560" fill="#8a5a3a"/><rect x="300" y="160" width="200" height="240" fill="#7a4a2a"/><rect x="300" y="420" width="200" height="260" fill="#7a4a2a"/>'
b+='<circle cx="490" cy="440" r="12" fill="#e8c040"/><path d="M490 452 L470 500" stroke="#3a2a1a" stroke-width="2"/>'+heart(460,530,30,'#d0102a')
b+='<rect y="700" width="800" height="100" fill="#a07a5a"/>'+glow(400,720,160,'#ffd8a0',.4)
I[343]=svg(b,d)

# 363 How Will I Know (Whitney Houston, 1986): a girl in a colorful 80s dress dancing among giant scribbled pastel shapes, bow in her hair
d,b=bg([(0,'#ffd0f0'),(1,'#c0f0ff')])
for k,(x,y,c) in enumerate(((140,160,'#ff4ab0'),(660,200,'#4ad8ff'),(160,620,'#ffd23a'),(640,620,'#7a4aff'))): b+=f'<path d="M{x-80} {y} L{x} {y-80} L{x+80} {y} L{x} {y+80}Z" fill="none" stroke="{c}" stroke-width="16"/>'
b+=figure(400,760,460,'#ff3a8a',pose='up',hair='#3a1a0a')+'<path d="M380 230 L360 210 L360 250Z M420 230 L440 210 L440 250Z" fill="#fff"/>'
I[363]=svg(b,d)

# 365 So Emotional (Whitney Houston, 1988): a singer belting into a mic under purple and pink concert lights with smoke
d,b=bg([(0,'#1a0a2a'),(1,'#6a1a6a')])
for x,c in ((150,'#ff4ab0'),(400,'#c8a0ff'),(650,'#ff4ab0')): b+=spotlight(x,0,140,c,.16)
b+='<ellipse cx="400" cy="720" rx="400" ry="60" fill="#e8d8ff" opacity=".2" filter="url(#glow)"/>'
b+=figure(400,760,460,'#0a0414',pose='wave',hair='#0a0414')+mic(370,480,50,'#d8d8e0',stand=False,rot=-20)
I[365]=svg(b,d)

# 366 Cold Hearted (Paula Abdul, 1989): a heart made of ice with frost cracks on a dark warehouse stage, dancers in silhouette behind
d,b=bg([(0,'#04081a'),(1,'#1a2a4a')])
for x in (160,290,510,640): b+=figure(x,700,240,'#0a1020',pose='reach' if x<400 else 'reachL')
d+=lg('ice',S((0,'#ffffff'),(.5,'#9ad8ff'),(1,'#4a8ad8')),0,0,1,1)
b+=heart(400,380,150,'url(#ice)','stroke="#e8f8ff" stroke-width="6"')+'<path d="M340 300 L380 360 L360 420 M440 300 L420 380 L460 440" stroke="#fff" stroke-width="4" fill="none"/>'
I[366]=svg(b,d)

# 372 Together Again (Janet Jackson, 1998): a dancer on a savanna plain at sunrise with giraffes, joyous African-inspired colors
d,b=bg([(0,'#ff8a3a'),(1,'#ffe08a')])
b+=glow(400,420,200,'#fff2c0',.8)+'<rect y="560" width="800" height="240" fill="#c8902a"/>'
for x in (620,700):
    b+=f'<g fill="#5a2a0a"><path d="M{x} 560 L{x} 460 L{x+10} 460 L{x+10} 560Z M{x+40} 560 L{x+40} 460 L{x+50} 460 L{x+50} 560Z"/><ellipse cx="{x+25}" cy="450" rx="40" ry="24"/><path d="M{x+50} 440 L{x+70} 300 L{x+82} 300 L{x+66} 444Z"/><ellipse cx="{x+86}" cy="296" rx="18" ry="10"/></g>'
b+=figure(300,700,360,'#2a0a04',pose='up',hair='#2a0a04')
I[372]=svg(b,d)

# 380 Right Round (Flo Rida, 2009): a spinning vinyl record seen from above, motion blur rings, gold and red club light
d,b=bg([(0,'#1a0a04'),(1,'#7a2a0a')])
b+=vinyl(400,400,280,'#e8c040')
for k in range(4): b+=f'<path d="M{400+300*math.cos(k*1.57):.0f} {400+300*math.sin(k*1.57):.0f} A300 300 0 0 1 {400+300*math.cos(k*1.57+.8):.0f} {400+300*math.sin(k*1.57+.8):.0f}" stroke="#ffd84a" stroke-width="10" fill="none" opacity=".5"/>'
I[380]=svg(b,d)

# 382 Grenade (Bruno Mars, 2011): a man dragging a piano down a long street, a heart-shaped grenade with the pin pulled lying in the road
d,b=bg([(0,'#2a2a3a'),(1,'#7a6a6a')])
b+=road(400,460,'#3a3a44','#c8c0a0',560)+skyline(460,'#3a3a4a',382,40,140,None)
b+='<g transform="translate(400 560)"><rect x="-90" y="-80" width="180" height="90" fill="#0a0a0a"/><rect x="-90" y="-20" width="180" height="20" fill="#f2f2f2"/></g>'+figure(530,640,170,'#0a0a0a',pose='reachL')
b+=heart(260,720,40,'#3a4a2a')+'<rect x="250" y="670" width="20" height="18" fill="#5a5a5a"/><circle cx="296" cy="672" r="12" fill="none" stroke="#aaa" stroke-width="4"/>'
I[382]=svg(b,d)

# 388 Psycho (Post Malone ft. Ty Dolla Sign, 2018): a fluorescent-lit convenience store parking lot at 3am, a sports car and blue neon
d,b=bg([(0,'#04040e'),(1,'#141420')])
b+='<rect x="100" y="200" width="600" height="300" fill="#e8f8ff" opacity=".2"/><rect x="100" y="180" width="600" height="40" fill="#2a8aff"/>'+''.join(f'<rect x="{140+k*140}" y="250" width="100" height="220" fill="#cfefff" opacity=".4"/>' for k in range(4))
b+='<rect y="560" width="800" height="240" fill="#0a0a14"/>'+''.join(f'<path d="M{100+k*150} 620 L{60+k*150} 800" stroke="#f2f2f2" stroke-width="4" opacity=".5"/>' for k in range(5))+car(400,720,150,'#1a1a2a','#9ad0ff',glass='#2a8aff')
I[388]=svg(b,d)

# 390 Kiss Me More (Doja Cat ft. SZA, 2021): a pink retro-futurist space station, an astronaut in a heart-shaped helmet window, lipstick kiss print
d,b=bg([(0,'#ff9ad8'),(1,'#ffd8f0')])
b+=starsf(40,390,800,'#fff')+'<circle cx="400" cy="400" r="200" fill="#fbf6fa"/>'+heart(400,400,100,'#ff3a8a')
b+='<path d="M330 400 Q400 360 470 400 Q400 440 330 400Z" fill="#c8001a"/><path d="M330 400 Q400 410 470 400" stroke="#8a0010" stroke-width="5"/>'
b+='<rect x="320" y="600" width="160" height="40" rx="12" fill="#e8d8e8"/>'
I[390]=svg(b,d)

# 391 First Class (Jack Harlow, 2022): a private-jet first-class seat with a champagne flute by an oval window looking over clouds
d,b=bg([(0,'#e8e0d0'),(1,'#c8b8a0')])
b+='<ellipse cx="560" cy="320" rx="130" ry="170" fill="#9ad0f0" stroke="#f2f2f2" stroke-width="20"/><ellipse cx="560" cy="380" rx="110" ry="40" fill="#fff"/>'
b+='<path d="M120 300 Q120 200 220 200 L300 200 Q360 200 360 300 L360 560 L120 560Z" fill="#f6f2ea"/><rect x="100" y="540" width="300" height="80" rx="20" fill="#ece4d8"/><rect x="100" y="620" width="40" height="160" fill="#a89070"/>'
b+='<path d="M420 520 L460 520 L446 600 L446 660 L462 668 L418 668 L434 660 L434 600Z" fill="#fff2c0" opacity=".9"/>'
I[391]=svg(b,d)

# 395 It's Now or Never (Elvis Presley, 1960): a gondola on a moonlit Neapolitan bay with a mandolin, a romantic serenade
d,b=bg([(0,'#06081e'),(1,'#1a2a5a')])
b+=starsf(60,395,400)+moon(560,170,60)+'<rect y="460" width="800" height="340" fill="#0e1a3a"/>'+''.join(f'<path d="M{540+k*6} {500+k*30} l40 0" stroke="#fff6dc" stroke-width="4" opacity="{.6-k*.08:.2f}"/>' for k in range(7))
b+='<path d="M140 600 Q400 660 660 600 L680 560 Q640 620 400 630 Q160 620 120 560Z" fill="#04060e"/>'+figure(560,610,180,'#04060e',pose='stand')
b+=guitar(330,560,80,'#c8843a','#3a2010',-30)
I[395]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
