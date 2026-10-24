import sys,math,random;sys.path[:0]=['/tmp/usrajz']
from hl import *;from us import *
# USA 4. csoport: a következő 20 videós dal index szerint (2026-10-24)
I={}

# 65 Crazy (Gnarls Barkley, 2006): a swirling Rorschach inkblot that becomes two mirrored faces, black ink on cream
d,b=bg([(0,'#efe6d0'),(1,'#d8cbb0')])
r=random.Random(65);o=''
for k in range(26):
    x,y,s=r.uniform(40,330),r.uniform(130,670),r.uniform(20,80)
    o+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{s:.0f}" ry="{s*r.uniform(.5,1.2):.0f}" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+=f'<g fill="#121010">{o}</g><g fill="#121010" transform="translate(800 0) scale(-1 1)">{o}</g><rect x="330" y="120" width="140" height="560" fill="#121010"/>'
b+='<circle cx="300" cy="330" r="20" fill="#efe6d0"/><circle cx="500" cy="330" r="20" fill="#efe6d0"/>'
I[65]=svg(b,d)

# 66 Party Rock Anthem (LMFAO, 2011): neon zebra-print, a shuffling dancer in giant sunglasses and an afro, laser lights
d,b=bg([(0,'#1a0a3a'),(1,'#ff2a8a')])
for k in range(14): b+=f'<path d="M{k*60-40} 0 Q{k*60+20} 400 {k*60-60} 800" stroke="#fff" stroke-width="16" fill="none" opacity=".08"/>'
for k in range(8): b+=f'<path d="M400 0 L{k*110} 800" stroke="{["#4affd8","#ffe14a"][k%2]}" stroke-width="3" opacity=".5"/>'
b+=figure(400,780,440,'#0a0418',pose='up')+'<circle cx="400" cy="408" r="70" fill="#0a0418"/>'
b+='<rect x="350" y="412" width="44" height="26" rx="6" fill="#ffe14a"/><rect x="406" y="412" width="44" height="26" rx="6" fill="#ffe14a"/>'
b+='<path d="M290 640 L510 640 L520 700 L280 700Z" fill="#ffe14a" opacity=".2"/>'
I[66]=svg(b,d)

# 67 Luther (Kendrick Lamar & SZA, 2025): two lovers slow dancing in a pink-lit bedroom, a vintage soul record turning on a player
d,b=bg([(0,'#2a0a2a'),(1,'#d86a9a')])
b+=glow(400,360,220,'#ffc0e0',.5)
b+='<rect x="520" y="140" width="200" height="280" fill="#3a1a3a"/><rect x="540" y="160" width="160" height="240" fill="#ffb0d8" opacity=".4"/><path d="M620 160 L620 400 M540 280 L700 280" stroke="#3a1a3a" stroke-width="8"/>'
b+=figure(360,720,330,'#1a0614',pose='hold',hair='#1a0614')+figure(430,720,350,'#1a0614',pose='hold')
b+='<rect x="80" y="600" width="200" height="120" rx="10" fill="#4a2a2a"/>'+vinyl(180,600,70,'#e8c06a',False)
I[67]=svg(b,d)

# 68 Lady (Kenny Rogers, 1980): a white rose on a closed grand piano lid in warm candlelight, a gray-bearded crooner's shadow
d,b=bg([(0,'#1a0e08'),(1,'#5a3a24')])
b+=glow(560,320,140,'#ffd88a',.6)+'<rect x="550" y="300" width="20" height="80" fill="#f2e6c8"/><ellipse cx="560" cy="290" rx="8" ry="16" fill="#ffe08a"/>'
b+='<path d="M60 520 Q300 420 740 470 L740 560 L60 600Z" fill="#0a0604"/><path d="M60 520 Q300 420 740 470" stroke="#8a6a4a" stroke-width="4" fill="none"/>'
b+='<path d="M220 500 L480 470" stroke="#2a6a2a" stroke-width="6"/>'
for k in range(6): a=k*1.05;b+=f'<ellipse cx="{200+16*math.cos(a):.0f}" cy="{500+16*math.sin(a):.0f}" rx="22" ry="16" fill="#fbf7ee" transform="rotate({k*60} 200 500)"/>'
b+='<circle cx="200" cy="500" r="14" fill="#f2ead8"/>'
I[68]=svg(b,d)

# 69 I'll Make Love to You (Boyz II Men, 1994): candles and rose petals around a soft bed, satin sheets in deep wine
d,b=bg([(0,'#1a040a'),(1,'#4a0a1a')])
b+='<path d="M80 520 L720 520 L760 700 L40 700Z" fill="#8a1a2a"/><path d="M80 520 Q400 480 720 520" stroke="#c84a5a" stroke-width="8" fill="none"/><rect x="100" y="380" width="600" height="150" rx="20" fill="#3a0812"/>'
for x in (140,240,560,660): b+=f'<rect x="{x-12}" y="640" width="24" height="70" fill="#f2e6c8"/>'+glow(x,620,30,'#ffcf6a',.9,'glow2')+f'<ellipse cx="{x}" cy="630" rx="7" ry="14" fill="#ffe08a"/>'
r=random.Random(69)
for k in range(24): x,y=r.uniform(120,680),r.uniform(530,680);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="12" ry="7" fill="#e0102a" transform="rotate({r.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>'
b+=heart(400,300,50,'#ff4a6a','opacity=".7"')
I[69]=svg(b,d)

# 71 Humble (Kendrick Lamar, 2017): a lone figure in a bright spotlight beneath a floating golden halo, deep black and stark white
d,b=bg([(0,'#000'),(1,'#141414')])
b+=spotlight(400,0,200,'#ffffff',.22)+'<ellipse cx="400" cy="730" rx="180" ry="30" fill="#fff" opacity=".2"/>'
b+=figure(400,730,420,'#050505',pose='stand')
b+=glow(400,282,40,'#ffd84a',.6,'glow2')+'<ellipse cx="400" cy="282" rx="56" ry="14" fill="none" stroke="#ffd84a" stroke-width="9"/>'
I[71]=svg(b,d)

# 72 My Girl (The Temptations, 1964): sunshine on a cloudy day, a golden sun breaking out behind matching-suit singers in a row
d,b=bg([(0,'#5a8ac8'),(1,'#f6dfa0')])
b+=glow(400,260,200,'#fff2a0',.9)+'<circle cx="400" cy="260" r="110" fill="#ffd84a"/>'+rays(400,260,24,'#fff6c0',.2,10)
for x,y in ((160,200),(640,180),(300,120)): b+=f'<ellipse cx="{x}" cy="{y}" rx="110" ry="40" fill="#fff" opacity=".9"/>'
b+='<rect y="660" width="800" height="140" fill="#3a2a3a"/>'
for k,x in enumerate((200,300,400,500,600)): b+=figure(x,720,260,'#1a1a3a',pose='wave' if k%2 else 'stand')
I[72]=svg(b,d)

# 73 skip
# 74 Vogue (Madonna, 1990): a black-and-white Hollywood glamour portrait pose, hands framing the face, art-deco fan behind
d,b=bg([(0,'#1a1a1a'),(1,'#4a4a4a')])
for k in range(13): a=math.radians(180+k*15);b+=f'<path d="M400 520 L{400+400*math.cos(a):.0f} {520+400*math.sin(a):.0f}" stroke="#d8d8d8" stroke-width="10" opacity=".25"/>'
b+='<circle cx="400" cy="520" r="120" fill="none" stroke="#d8d8d8" stroke-width="6" opacity=".4"/>'
b+='<ellipse cx="400" cy="340" rx="66" ry="84" fill="#f2f2f2"/><path d="M330 330 Q320 230 400 230 Q490 230 470 330 Q460 280 400 274 Q350 280 330 330Z" fill="#f6f2d8"/>'
b+='<path d="M310 420 L330 270 L350 270 L344 400Z M490 420 L470 270 L450 270 L456 400Z" fill="#f2f2f2"/><path d="M290 800 L330 420 L470 420 L510 800Z" fill="#0a0a0a"/>'
b+='<path d="M380 380 Q400 392 420 380" stroke="#a0101a" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="378" cy="330" r="6" fill="#111"/><circle cx="422" cy="330" r="6" fill="#111"/>'
I[74]=svg(b,d)

# 76 Say My Name (Destiny's Child, 2000): a ringing landline phone on a nightstand glowing in a color-blocked room, three silhouettes in the doorway
d,b=bg([(0,'#3a0a4a'),(1,'#ff6a3a')])
b+='<rect x="0" y="0" width="270" height="800" fill="#ffb03a" opacity=".3"/><rect x="530" y="0" width="270" height="800" fill="#3ad8ff" opacity=".2"/>'
for k,x in enumerate((300,400,500)): b+=figure(x,560,260,'#1a0420',pose='stand',hair='#1a0420')
b+='<rect x="160" y="620" width="480" height="180" fill="#2a0a2a"/><path d="M300 600 L500 600 L520 650 L280 650Z" fill="#e8102a"/><path d="M290 590 Q400 540 510 590 L500 610 Q400 570 300 610Z" fill="#b00a1e"/>'
for k in range(3): b+=f'<path d="M{520+k*20} {560-k*10} q16 16 0 32" stroke="#fff" stroke-width="6" fill="none"/>'
I[76]=svg(b,d)

# 77 Gold Digger (Kanye West ft. Jamie Foxx, 2005): a gold-plated pin-up silhouette over a pile of gold chains and coins, retro poster red
d,b=bg([(0,'#7a0a0a'),(1,'#d8302a')])
b+=rays(400,420,28,'#ffd84a',.12,14)
d+=lg('gold',S((0,'#fff2a0'),(.5,'#e8b030'),(1,'#a0701a')),0,0,1,1)
b+=figure(400,640,440,'url(#gold)',pose='up',hair='url(#gold)')
r=random.Random(77)
for k in range(40): x,y=r.uniform(120,680),r.uniform(640,780);b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="24" ry="9" fill="url(#gold)" stroke="#8a5a10" stroke-width="2"/>'
I[77]=svg(b,d)

# 80 Blank Space (Taylor Swift, 2014): a mansion's long table with a dropped red apple and a cracked phone, a crimson-lipped portrait frame empty and blank
d,b=bg([(0,'#0a1a14'),(1,'#2a3a2a')])
b+='<rect x="250" y="120" width="300" height="360" fill="#c8a04a"/><rect x="276" y="146" width="248" height="308" fill="#f6f2e8"/>'
b+='<rect y="560" width="800" height="240" fill="#2a1408"/><path d="M0 560 L800 560" stroke="#6a3a1a" stroke-width="6"/>'
b+='<circle cx="320" cy="640" r="44" fill="#d8101a"/><path d="M320 600 l6 -20" stroke="#3a2a0a" stroke-width="6"/><path d="M326 594 q20 -16 30 -4 q-14 10 -30 4Z" fill="#2a8a2a"/>'
b+='<rect x="470" y="610" width="70" height="120" rx="10" fill="#111" transform="rotate(20 505 670)"/><path d="M480 640 L520 680 L500 700 L530 720" stroke="#ccc" stroke-width="3" fill="none" transform="rotate(20 505 670)"/>'
I[80]=svg(b,d)

# 81 Wipe Out (The Surfaris, 1963): a surfer tumbling off a giant curling wave, longboard flying, drumsticks of foam
d,b=bg([(0,'#f6c06a'),(1,'#3ab0d8')])
b+='<path d="M0 800 L0 420 Q200 160 480 200 Q700 230 720 420 Q640 300 520 320 Q400 360 440 520 Q520 620 800 600 L800 800Z" fill="#0a6aa0"/>'
b+='<path d="M720 420 Q640 300 520 320 Q600 280 700 350Z" fill="#e8f8ff"/>'
for k in range(12): b+=f'<circle cx="{560+k*16}" cy="{330+((k*37)%40)}" r="{6+k%3*3}" fill="#fff" opacity=".85"/>'
b+='<g transform="translate(470 270) rotate(40)"><ellipse rx="110" ry="16" fill="#ffd84a"/><path d="M-100 0 L100 0" stroke="#e8102a" stroke-width="4"/></g>'
b+='<g transform="translate(330 380) rotate(-60)">'+figure(0,0,150,'#2a1a0a',pose='up')+'</g>'
I[81]=svg(b,d)

# 82 Drivers License (Olivia Rodrigo, 2021): a teenager crying in a car parked on a suburban street at night, streetlight through the windshield
d,b=bg([(0,'#06081a'),(1,'#1a1a3a')])
b+=glow(640,180,80,'#ffd8a0',.8)+'<path d="M640 180 L640 560" stroke="#2a2a3a" stroke-width="10"/>'
b+='<path d="M60 720 L60 260 Q400 160 740 260 L740 720Z" fill="#0a0a14"/><path d="M110 600 L130 320 Q400 250 670 320 L690 600Z" fill="#2a3a6a" opacity=".7"/>'
b+=figure(400,700,320,'#060610',pose='stand',hair='#060610')+'<path d="M380 470 l-4 30" stroke="#9ad0ff" stroke-width="4" stroke-linecap="round"/>'
b+='<circle cx="400" cy="640" r="100" fill="none" stroke="#1a1a24" stroke-width="22"/><rect x="290" y="300" width="90" height="56" rx="6" fill="#f2e6c8" transform="rotate(-6 335 328)"/>'
I[82]=svg(b,d)

# 83 Sicko Mode (Travis Scott, 2018): a psychedelic Astroworld rollercoaster loop over a burning orange sky, a lone figure in the car
d,b=bg([(0,'#1a0a2a'),(.6,'#c83a1a'),(1,'#ffb03a')])
b+='<path d="M0 640 Q200 640 300 500 Q360 260 500 300 Q620 360 520 480 Q440 560 560 620 Q680 660 800 600" stroke="#f2e6d8" stroke-width="14" fill="none"/><path d="M0 660 Q200 660 300 520 Q370 290 500 320" stroke="#f2e6d8" stroke-width="6" fill="none"/>'
for k in range(12): b+=f'<rect x="{40+k*65}" y="{560+(k%3)*20}" width="8" height="240" fill="#3a1a1a"/>'
b+='<rect y="720" width="800" height="80" fill="#1a0a0a"/>'+glow(430,330,40,'#ffe080',.8,'glow2')+'<rect x="410" y="300" width="50" height="30" rx="6" fill="#0a0a0a" transform="rotate(-50 435 315)"/>'
I[83]=svg(b,d)

# 84 Girls Just Want to Have Fun (Cyndi Lauper, 1984): a 1980s girl with wild two-tone hair dancing in the street with friends, confetti and neon
d,b=bg([(0,'#ff3a8a'),(1,'#ffd23a')])
b+=confetti(80,84,['#3ad8ff','#fff','#7a3aff','#2ae07a'],0,800,.9)
for k,x in enumerate((180,620)): b+=figure(x,780,320,'#3a0a3a',pose='up',hair='#3a0a3a')
b+=figure(400,780,440,'#1a0a2a',pose='up')
b+='<path d="M350 330 Q340 250 400 240 Q470 250 460 320 Q500 300 480 380 Q420 300 360 340 Q330 360 320 400 Q300 320 350 330Z" fill="#ff6a1a"/><path d="M400 240 Q470 250 460 320 Q500 300 480 380 Q440 320 400 300Z" fill="#e8102a"/>'
I[84]=svg(b,d)

# 85 I Want It That Way (Backstreet Boys, 1999): five boys in white standing on an airport runway with a jet behind, sunset glow
d,b=bg([(0,'#4a6ab0'),(.6,'#f0a07a'),(1,'#f6d8b0')])
b+='<rect y="600" width="800" height="200" fill="#4a4a5a"/><path d="M400 600 L340 800 M400 600 L460 800" stroke="#f2f2f2" stroke-width="6"/>'
b+='<g transform="translate(400 330)" fill="#e8e8f0"><path d="M-260 20 L240 -10 Q280 -10 260 20 L-240 40Z"/><path d="M-40 10 L-140 120 L-100 120 L40 10Z"/><path d="M-40 0 L-120 -80 L-90 -80 L20 0Z"/><path d="M-250 20 L-280 -40 L-250 -40 L-210 18Z"/></g>'
for x in (220,310,400,490,580): b+=figure(x,760,250,'#f6f6f6',pose='stand')
I[85]=svg(b,d)

# 86 Jailhouse Rock (Elvis Presley, 1957): a jail cell block of stacked bars turned into a dance set, a pompadour silhouette mid-swivel in stripes
d,b=bg([(0,'#0a0a10'),(1,'#2a2a3a')])
b+=spotlight(400,0,240,'#f2f0e0',.2)
for k in range(3): b+=f'<rect x="60" y="{80+k*180}" width="680" height="10" fill="#8a8a9a"/>'+''.join(f'<rect x="{80+j*60}" y="{90+k*180}" width="8" height="170" fill="#6a6a7a"/>' for j in range(12))
b+='<g transform="translate(400 760)"><circle cx="0" cy="-330" r="28" fill="#0a0a0a"/><path d="M-30 -350 Q-20 -390 30 -370 Q20 -350 -30 -350Z" fill="#0a0a0a"/>'
b+='<path d="M-40 -300 L40 -300 L46 -170 L-46 -170Z" fill="#f2f2f2"/>'+''.join(f'<rect x="-44" y="{-290+k*26}" width="88" height="12" fill="#111"/>' for k in range(5))
b+='<path d="M-46 -170 L46 -170 L90 0 L60 0 L0 -110 L-30 0 L-60 0Z" fill="#0a0a0a"/><path d="M38 -290 Q110 -260 130 -200 M-38 -290 Q-120 -280 -150 -340" stroke="#f2f2f2" stroke-width="22" fill="none" stroke-linecap="round"/></g>'
I[86]=svg(b,d)

# 88 You Send Me (Sam Cooke, 1957): a vintage love letter with a red wax heart seal floating on a warm cream glow, soft musical notes
d,b=bg([(0,'#3a2a3a'),(1,'#c88a6a')])
b+=glow(400,400,240,'#ffe8c8',.6)
b+='<g transform="translate(400 420) rotate(-8)"><rect x="-220" y="-140" width="440" height="280" fill="#f6efe0"/><path d="M-220 -140 L0 40 L220 -140" stroke="#d8c8a8" stroke-width="6" fill="none"/></g>'
b+=heart(400,440,34,'#b0101a')+note(170,210,40,'#fff2d8')+note(640,190,34,'#fff2d8',True)+note(600,640,30,'#fff2d8')
I[88]=svg(b,d)

# 89 Shake It Off (Taylor Swift, 2014): a dancer in a gold-sequined cheer outfit shaking pom-poms in front of a bright stripe backdrop
d,b=bg([(0,'#3ad8e8'),(1,'#ff8ac0')])
for k in range(10): b+=f'<rect x="{k*80}" y="0" width="40" height="800" fill="#fff" opacity=".18"/>'
b+=figure(400,780,460,'#1a1a3a',pose='up',hair='#e8c06a')
for x,y in ((330,330),(470,330)):
    for k in range(20): a=k*0.314;b+=f'<path d="M{x} {y} l{50*math.cos(a):.0f} {50*math.sin(a):.0f}" stroke="#ffd23a" stroke-width="8" stroke-linecap="round"/>'
b+='<path d="M366 440 L434 440 L440 560 L360 560Z" fill="#ffd23a"/>'
I[89]=svg(b,d)

# 90 Truth Hurts (Lizzo, 2019): a bride in a white veil marrying herself, holding her own hand, under a sweet pink arch of flowers
d,b=bg([(0,'#ffb0d0'),(1,'#ffe8f0')])
b+='<path d="M180 800 L180 300 Q400 60 620 300 L620 800" stroke="#f6c0d8" stroke-width="30" fill="none"/>'
r=random.Random(90)
for k in range(40): a=math.pi*(1-k/39);x=400+220*math.cos(a)*1.0;y=330-240*math.sin(a)*.9;b+=f'<circle cx="{x+r.uniform(-14,14):.0f}" cy="{y+r.uniform(-14,14):.0f}" r="{r.uniform(12,22):.0f}" fill="{r.choice(["#ff4a8a","#fff","#ffd23a","#ff8ab0"])}"/>'
b+='<g transform="translate(400 780)"><circle cx="0" cy="-400" r="30" fill="#5a2a1a"/><path d="M-30 -420 Q-80 -300 -120 -100 L120 -100 Q80 -300 30 -420Z" fill="#fff" opacity=".6"/>'
b+='<path d="M-40 -366 L40 -366 L60 -240 Q140 -60 170 0 L-170 0 Q-140 -60 -60 -240Z" fill="#fbf8f6"/></g>'+heart(400,470,22,'#ff3a7a')
I[90]=svg(b,d)

for k,v in I.items(): open(f'/tmp/usrajz/svg/{k}.svg','w').write(v)
print(len(I),'ikon')
