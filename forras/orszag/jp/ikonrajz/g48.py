import sys,math,random;sys.path[:0]=['/tmp/jprajz']
from hl import *;from jp import *
from g2h import *
# IKONOK /jp/: 48. csoport, 2026-10-24
I={}
def ring(cx,cy,r,col,w=10,op=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>'
def txt(x,y,t,size,col,w=700,anchor='middle',op=1): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Noto Sans JP" font-weight="{w}" font-size="{size}" fill="{col}" opacity="{op}">{t}</text>'


# 36 赤いランプの終列車: the last train's red tail lamp disappearing into a snowy night, a figure on the platform, 1952
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+=snow(60,36)+'<path d="M380 440 L100 800 M420 440 L700 800" stroke="#5a5a64" stroke-width="10"/><rect x="0" y="560" width="200" height="240" fill="#4a4a54"/>'
b+='<rect x="360" y="400" width="80" height="50" fill="#1a1a24"/><circle cx="380" cy="430" r="8" fill="#ff2a2a"/><circle cx="420" cy="430" r="8" fill="#ff2a2a"/>'+glow(400,430,60,'#ff2a2a',.6)+figure(100,580,200,'#0a0a14',hair='#0a0a14')
I[36]=svg(b,d)

# 1801 夜は眠れるかい?: a sleepless figure on a rooftop under a vast night sky, a phone screen glowing, 2016 rock
d,b=bg([(0,'#050a24'),(1,'#1a1a4a')])
b+=starsf(100,1801,560)+skyline(640,'#0a0a1a',1801,40,160,'#ffd27a',30)+'<rect y="640" width="800" height="160" fill="#05050f"/>'
b+=figure(400,660,200,'#000')+'<rect x="420" y="540" width="20" height="30" fill="#8ad0ff"/>'+glow(430,555,40,'#8ad0ff',.6)
I[1801]=svg(b,d)

# 1820 恋の終わりの名古屋にひとり: a woman alone before a castle with golden roof ornaments at dusk, enka
d,b=bg([(0,'#5a4a7a'),(1,'#ffa88a')])
b+='<rect x="400" y="300" width="240" height="300" fill="#e8e0d0"/>'+''.join(f'<path d="M{380-k*10} {300+k*90} L{660+k*10} {300+k*90} L{620+k*10} {270+k*90} L{420-k*10} {270+k*90}Z" fill="#3a6a6a"/>' for k in range(3))+'<path d="M440 270 L520 200 L600 270Z" fill="#3a6a6a"/>'
b+='<path d="M440 200 q-10 -30 10 -40 l10 30Z M600 200 q10 -30 -10 -40 l-10 30Z" fill="#ffd02a"/><rect y="600" width="800" height="200" fill="#5a4a4a"/>'+figure(220,640,240,'#1a1014',hair='#1a1014')
I[1820]=svg(b,d)

# 49 十七才のこの胸に: a teenage boy's silhouette holding a letter to his chest under a big spring sky, 1964
d,b=bg([(0,'#7ac8ff'),(1,'#fff0e0')])
b+=cloud(200,180,1.3)+cloud(620,220,1.0)+'<path d="M0 600 Q400 540 800 600 L800 800 L0 800Z" fill="#7ab85a"/>'+figure(400,620,300,'#1a2a3a')+'<rect x="372" y="420" width="60" height="44" fill="#fff" transform="rotate(-10 402 442)"/>'+heart(402,442,12,'#ff6a8a')
I[49]=svg(b,d)

# 1336 鈴懸の木の道で…: a tree-lined avenue of plane trees with dappled sunlight and two schoolgirls, idol pop
d,b=bg([(0,'#c8e8a8'),(1,'#f4f8e0')])
b+='<path d="M380 400 L120 800 L680 800 L420 400Z" fill="#d8c8a0"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{800-y}" fill="#8a7a6a"/><circle cx="{x+w/2}" cy="{y}" r="{w*3}" fill="#5aa84a" opacity=".9"/>' for x,y,w in [(60,360,30),(180,380,22),(290,400,14),(700,360,30),(600,380,22),(500,400,14)])
b+=''.join(f'<ellipse cx="{x}" cy="{y}" rx="30" ry="10" fill="#fff8c8" opacity=".6"/>' for x,y in [(300,620),(460,700),(380,560)])+figure(360,700,180,'#2a2a3a',hair='#2a2a3a')+figure(430,700,170,'#2a2a3a',hair='#2a2a3a')
I[1336]=svg(b,d)

# 1818 瞳の中のファーラウェイ: a faraway horizon reflected inside a large dreamy eye-shaped lens, 1989 Eurobeat idol
d,b=bg([(0,'#2a1a5a'),(1,'#ff8ab0')])
b+='<path d="M120 400 Q400 160 680 400 Q400 640 120 400Z" fill="#fff"/><circle cx="400" cy="400" r="150" fill="#3a8ae8"/>'
b+='<clipPath id="ey"><circle cx="400" cy="400" r="150"/></clipPath><g clip-path="url(#ey)"><rect x="250" y="250" width="300" height="150" fill="#ffb88a"/><circle cx="400" cy="400" r="40" fill="#fff4c8"/><rect x="250" y="400" width="300" height="150" fill="#1a5ab8"/></g>'
b+='<path d="M120 400 Q400 160 680 400 Q400 640 120 400Z" fill="none" stroke="#1a0a2a" stroke-width="12"/>'+sparkle(470,330,26,'#fff')
I[1818]=svg(b,d)

# 57 銀河のロマンス: a white horse-drawn carriage gliding along the Milky Way among stars, 1968 group sounds
d,b=bg([(0,'#05081a'),(1,'#1a1a4a')])
b+=starsf(120,57,800)+'<path d="M-40 640 Q400 360 840 160" stroke="#c8d0ff" stroke-width="140" fill="none" opacity=".12"/>'
b+='<path d="M300 440 Q300 400 340 400 L440 400 Q470 400 470 440 L470 480 L300 480Z" fill="#f4f4ff"/>'+ring(330,490,22,'#f4f4ff',6)+ring(440,490,22,'#f4f4ff',6)
b+='<path d="M490 450 L540 430 Q560 400 590 400 L610 380 L620 400 L600 430 L600 470 L580 470 L570 450 L540 460 L530 490 L510 490 L515 460Z" fill="#f4f4ff"/><path d="M470 440 L520 440" stroke="#f4f4ff" stroke-width="4"/>'
I[57]=svg(b,d)

# 1746 妖 ~あやかし~: a fox-fire flame flickering beside a moonlit shrine lantern in a dark bamboo grove, 2009
d,b=bg([(0,'#0a0a1a'),(1,'#1a1a3a')])
b+=''.join(f'<rect x="{x}" y="0" width="22" height="800" fill="#1a3a2a"/>'+''.join(f'<rect x="{x-2}" y="{y}" width="26" height="6" fill="#0a2a1a"/>' for y in range(60,800,120)) for x in (40,140,620,720))+moon(400,140,50)
b+='<rect x="380" y="500" width="40" height="160" fill="#5a5a64"/><rect x="350" y="440" width="100" height="70" fill="#7a7a84"/><path d="M340 440 L400 400 L460 440Z" fill="#5a5a64"/><rect x="370" y="460" width="60" height="30" fill="#ffd27a"/>'
b+=''.join(f'<path d="M{x} {y} q18 -30 0 -60 q-18 30 0 60Z" fill="#8ad0ff" opacity=".85"/>'+glow(x,y-30,40,'#8ad0ff',.5) for x,y in [(250,480),(560,420),(500,580)])
I[1746]=svg(b,d)

# 19 旅人よ: a wanderer with a backpack on a mountain ridge overlooking a sea of clouds at dawn, 1966
d,b=bg([(0,'#ff9a6a'),(1,'#ffe8c0')])
b+='<circle cx="560" cy="380" r="70" fill="#fff4d0"/>'+cloud(200,500,2.4,'#fff')+cloud(600,520,2.2,'#fff')+'<path d="M0 800 L0 560 L300 460 L420 560 L420 800Z" fill="#3a2a2a"/>'+figure(300,470,180,'#0a0a10')+'<rect x="310" y="340" width="34" height="60" rx="10" fill="#0a0a10"/>'
I[19]=svg(b,d)

# 270 身も心も: a man and woman dancing cheek to cheek in a smoky bar under a single amber lamp, 1977 rock ballad
d,b=bg([(0,'#1a1010'),(1,'#3a2018')])
b+='<path d="M400 0 L400 140" stroke="#555" stroke-width="3"/><path d="M360 140 L440 140 L420 180 L380 180Z" fill="#c8802a"/>'+glow(400,180,240,'#ffb070',.35)+'<rect y="640" width="800" height="160" fill="#14100a"/>'
b+=figure(360,660,320,'#000')+figure(430,660,300,'#000',hair='#000')
I[270]=svg(b,d)

# 604 サイレント・イヴ: a snow-dusted window with a single candle and a lonely Christmas Eve cityscape beyond, 1990
d,b=bg([(0,'#0a1028'),(1,'#2a3458')])
b+='<rect x="160" y="100" width="480" height="440" fill="#1a2a5a"/>'+skyline(540,'#0a1430',604,40,200,'#ffd27a',40)+snow(40,604,.8,540)+'<rect x="160" y="100" width="480" height="440" fill="none" stroke="#3a2a24" stroke-width="20"/><rect x="390" y="100" width="20" height="440" fill="#3a2a24"/>'
b+='<rect x="120" y="540" width="560" height="30" fill="#5a4030"/><rect y="570" width="800" height="230" fill="#2a1a14"/><rect x="290" y="470" width="24" height="70" fill="#f4ece0"/><path d="M302 446 q10 14 0 24 q-10 -10 0 -24Z" fill="#ffd02a"/>'+glow(302,480,80,'#ffd27a',.5)
I[604]=svg(b,d)

# 31 赤いハンカチ: a red handkerchief caught on a branch fluttering over a lonely northern road, 1962 film song
d,b=bg([(0,'#5a6a8a'),(1,'#c8ccd4')])
b+='<rect y="500" width="800" height="300" fill="#8a8a7a"/><path d="M380 500 L200 800 L600 800 L420 500Z" fill="#a8a898"/>'+'<path d="M600 800 L610 380 M610 460 L700 380 M610 520 L520 440" stroke="#2a2a24" stroke-width="12" fill="none"/>'
b+='<path d="M520 440 L470 420 Q440 440 450 480 Q480 470 500 490Z" fill="#e8102a"/>'+figure(320,700,200,'#1a1a24')
I[31]=svg(b,d)

# 26 情熱の花: a passionate red hibiscus-like flower blooming in a dark night with Latin rhythm swirls, 1959
d,b=bg([(0,'#2a0a1a'),(1,'#6a0a2a')])
b+=''.join(f'<path d="M{x} {y} q40 -40 80 0 t80 0" stroke="#ff8a5a" stroke-width="4" fill="none" opacity=".4"/>' for x,y in [(60,160),(520,200),(80,640),(540,620)])+flower(400,400,180,5,'#e8102a','#ffd02a',10,.7)+glow(400,400,240,'#ff3a3a',.35)
I[26]=svg(b,d)

# 1672 少しだけまわり道: a winding detour path through a meadow with a signpost and two strolling figures, 1978
d,b=bg([(0,'#9ad0ff'),(1,'#f8f0d8')])
b+=hills(420,40,'#8ab06a',1672,4)+'<rect y="460" width="800" height="340" fill="#a8c878"/><path d="M400 800 Q100 700 300 600 Q520 520 300 470" stroke="#f0e0b0" stroke-width="40" fill="none"/>'
b+='<rect x="560" y="520" width="10" height="160" fill="#6a4a2a"/><path d="M570 540 L660 540 L680 560 L660 580 L570 580Z" fill="#c8a870"/>'+figure(300,620,140,'#2a2a3a')+figure(340,620,130,'#2a2a3a',hair='#2a2a3a')
I[1672]=svg(b,d)

# 1673 スカイレストラン: a rooftop restaurant table with two wine glasses high above a twinkling city at night, 1975
d,b=bg([(0,'#0a1028'),(1,'#3a2a5a')])
b+=starsf(50,1673,300)+skyline(800,'#0a0a1a',1673,40,200,'#ffd27a',140)+'<rect x="0" y="480" width="800" height="24" fill="#c8c8d0" opacity=".5"/>'
b+='<ellipse cx="400" cy="460" rx="160" ry="30" fill="#f4ece0"/><rect x="394" y="460" width="12" height="100" fill="#c8c8d0"/>'+''.join(f'<path d="M{x-20} 380 L{x+20} 380 L{x+10} 420 L{x-10} 420Z" fill="#a81a2a" opacity=".8"/><rect x="{x-2}" y="420" width="4" height="30" fill="#ddd"/>' for x in (350,450))+'<rect x="396" y="400" width="8" height="50" fill="#f4ece0"/><path d="M400 392 q6 8 0 12 q-6 -4 0 -12Z" fill="#ffd02a"/>'
I[1673]=svg(b,d)

# 268 裏切りの街角: a dark street corner in the rain with two figures parting under a flickering neon sign, rock
d,b=bg([(0,'#0a0a14'),(1,'#2a2030')])
b+=rain(90,268,'#cfe6ff',.35)+'<rect x="0" y="100" width="380" height="600" fill="#1a1a24"/><rect x="60" y="180" width="200" height="60" rx="8" fill="none" stroke="#ff4a6a" stroke-width="6"/>'+glow(160,210,120,'#ff4a6a',.3)
b+='<rect y="640" width="800" height="160" fill="#14141e"/>'+figure(460,660,260,'#000',hair='#000')+figure(660,660,280,'#000')+'<path d="M560 660 L600 800" stroke="#ff4a6a" stroke-width="3" opacity=".4"/>'
I[268]=svg(b,d)

# 1705 メロディ: a music box ballerina turning beside floating notes in soft lamplight, 80s idol
d,b=bg([(0,'#ffe8d8'),(1,'#f0d8e8')])
b+='<rect x="240" y="480" width="320" height="160" fill="#c8784a"/><rect x="240" y="470" width="320" height="20" fill="#e8a870"/><path d="M240 470 L280 280 L600 280 L560 470Z" fill="#e8a870" opacity=".6"/>'
b+=figure(400,470,180,'#ff8ab0',pose='up',hair='#ff8ab0')+'<path d="M360 400 Q400 380 440 400 L440 410 L360 410Z" fill="#ffc0d8"/>'+''.join(note(x,y,s,'#c8607a') for x,y,s in [(180,240,40),(620,200,36),(650,380,28)])
I[1705]=svg(b,d)

# 1780 Ready Go!: two young guitarists' silhouettes leaping off a stage edge at the start of a show, 2006
d,b=bg([(0,'#1a1a4a'),(1,'#ff8a3a')])
b+=rays(400,600,20,'#fff',.2,12)+'<rect y="640" width="800" height="160" fill="#14101a"/>'
b+='<g transform="rotate(-12 300 500)">'+figure(300,640,260,'#000',pose='up')+'</g><g transform="rotate(12 500 500)">'+figure(500,640,260,'#000',pose='up')+'</g>'+guitar(300,560,.5,40,'#000')+guitar(500,560,.5,-40,'#000')
I[1780]=svg(b,d)

# 795 Overnight Sensation: a dance floor exploding with laser light and a lone dancer frozen mid-move, 1995 dance
d,b=bg([(0,'#0a0014'),(1,'#2a0a3a')])
b+=''.join(f'<path d="M400 0 L{x} 800" stroke="{c}" stroke-width="4" opacity=".7"/>' for x,c in [(0,'#3affe8'),(160,'#ff4fd0'),(320,'#3affe8'),(480,'#ffd02a'),(640,'#ff4fd0'),(800,'#3affe8')])
b+='<rect y="640" width="800" height="160" fill="#0a0a14"/>'+''.join(f'<rect x="{x}" y="640" width="100" height="40" fill="{c}" opacity=".5"/>' for x,c in zip(range(0,800,100),['#ff4fd0','#3affe8','#ffd02a','#ff4fd0','#3affe8','#ffd02a','#ff4fd0','#3affe8']))+figure(400,660,320,'#000',pose='up')
I[795]=svg(b,d)

# 1677 感恩的心: two hands pressed together in gratitude with soft golden light rising, 1994 ballad
d,b=bg([(0,'#fff0d0'),(1,'#f0d8b0')])
b+=rays(400,300,20,'#fff',.4,10)+glow(400,300,200,'#fff4c8',.6)
b+='<path d="M360 700 L370 420 Q380 300 400 260 Q420 300 430 420 L440 700Z" fill="#e8b494"/><path d="M400 270 L400 600" stroke="#c8906a" stroke-width="3"/><path d="M300 800 L360 700 L440 700 L500 800Z" fill="#8a6a5a"/>'
I[1677]=svg(b,d)

# 1814 テネシー・ワルツ: a couple waltzing in a 1950s ballroom under a chandelier with a jealous onlooker
d,b=bg([(0,'#3a2a1a'),(1,'#7a5a3a')])
b+='<path d="M400 0 L400 100" stroke="#c8a24a" stroke-width="4"/>'+''.join(f'<circle cx="{400+r*math.cos(a)}" cy="{140+r*.3*math.sin(a)}" r="8" fill="#fff4c8"/>' for r in (40,80) for a in [k*math.pi/4 for k in range(8)])+glow(400,140,160,'#fff4c8',.4)
b+='<rect y="600" width="800" height="200" fill="#5a3a24"/>'+''.join(f'<rect x="{x}" y="600" width="80" height="200" fill="#6a4a2a" opacity=".6"/>' for x in range(0,800,160))
b+=figure(380,640,280,'#1a0a0a')+figure(440,640,260,'#1a0a0a',hair='#1a0a0a')+'<path d="M390 440 Q460 520 500 640 L400 640Z" fill="#1a0a0a"/>'+figure(680,640,200,'#2a1a14',hair='#2a1a14')
I[1814]=svg(b,d)

# 224 時には昔の話を: two old friends' silhouettes at a café table under a warm lamp, old photos between them, 1987
d,b=bg([(0,'#3a2a20'),(1,'#6a4a30')])
b+=glow(400,260,260,'#ffb070',.35)+'<rect y="520" width="800" height="280" fill="#4a2a1a"/><ellipse cx="400" cy="520" rx="220" ry="30" fill="#8a5a3a"/>'
b+=profile(200,520,.9,'#0a0a0a')+profile(600,520,.9,'#0a0a0a',True)+''.join(f'<rect x="{x}" y="490" width="60" height="44" fill="#e8d8b8" transform="rotate({r} {x+30} 512)"/>' for x,r in [(340,-10),(400,8)])
I[224]=svg(b,d)

# 1821 河内おとこ節: a festival drum and a happi coat on a pole with a bold wind-blown banner, Osaka enka
d,b=bg([(0,'#ff6a3a'),(1,'#ffd08a')])
b+=rays(400,300,20,'#fff',.2,12)+'<path d="M200 800 L200 120" stroke="#5a3a2a" stroke-width="12"/><path d="M206 140 Q400 120 580 180 Q500 240 580 320 Q400 280 206 300Z" fill="#1a3a8a"/><path d="M260 180 Q380 170 480 210" stroke="#fff" stroke-width="10" fill="none"/>'
b+='<ellipse cx="520" cy="560" rx="140" ry="40" fill="#f4e8d0"/><rect x="380" y="560" width="280" height="160" fill="#8a3a1a"/><ellipse cx="520" cy="720" rx="140" ry="40" fill="#6a2a14"/><path d="M420 440 L500 540 M620 440 L540 540" stroke="#f4e8d0" stroke-width="12" stroke-linecap="round"/>'
I[1821]=svg(b,d)

# 429 稲妻パラダイス: a pink lightning bolt striking a tropical island paradise at sunset, 1984 idol
d,b=bg([(0,'#5a1a6a'),(1,'#ff8a5a')])
b+='<rect y="500" width="800" height="300" fill="#3a6ac8"/><ellipse cx="400" cy="520" rx="200" ry="34" fill="#f0c890"/>'+''.join(f'<path d="M{x} 520 Q{x+10} 420 {x+30} 360" stroke="#2a1a1a" stroke-width="10" fill="none"/>'+''.join(f'<path d="M{x+30} 360 Q{x+30+dx} 330 {x+30+dx*1.4} 380" stroke="#2a1a1a" stroke-width="8" fill="none"/>' for dx in (-50,50,-30,30)) for x in (300,460))
b+=bolt([(520,0),(440,180),(520,200),(420,380)],'#ff6ad0',14)+glow(460,200,160,'#ff6ad0',.5)
I[429]=svg(b,d)

# 1819 捨てられて: a woman's discarded umbrella lying in the rain beside a puddle at night, 1995 enka
d,b=bg([(0,'#1a1a2a'),(1,'#3a3a4a')])
b+=rain(100,1819,'#cfe6ff',.4)+'<rect y="560" width="800" height="240" fill="#2a2a34"/><ellipse cx="400" cy="680" rx="200" ry="30" fill="#5a6a8a" opacity=".4"/>'
b+='<g transform="rotate(70 400 620)">'+wagasa(400,620,110,'#a81a3a',0)+'</g>'+figure(640,580,220,'#0a0a14',hair='#0a0a14')
I[1819]=svg(b,d)

# 62 北国の二人: a young couple's silhouettes in a sleigh-like snowy field under northern lights, 1967
d,b=bg([(0,'#0a1a2a'),(1,'#2a3a5a')])
b+=''.join(f'<path d="M-20 {y} Q200 {y-80} 400 {y} T820 {y}" stroke="{c}" stroke-width="40" fill="none" opacity=".25"/>' for y,c in [(200,'#3aff8a'),(260,'#3affe8'),(320,'#8a5aff')])+starsf(50,62,400)
b+='<rect y="580" width="800" height="220" fill="#e8eef8"/>'+snow(40,62,.7)+figure(360,620,220,'#0a0a14')+figure(430,620,210,'#0a0a14',hair='#0a0a14')
I[62]=svg(b,d)

# 1817 柳ヶ瀬ブルース: willow branches hanging over a neon-lit entertainment street at night in the rain, 1966
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+=rain(60,1817,'#cfe6ff',.3)+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" opacity=".8"/>' for x,y,w,h,c in [(500,200,60,180,'#ff4fa0'),(600,240,50,160,'#4fd0ff'),(680,180,70,200,'#ffd02a')])+'<rect y="560" width="800" height="240" fill="#14101a"/>'
b+='<path d="M200 800 L200 160" stroke="#2a2a1a" stroke-width="16"/>'+''.join(f'<path d="M200 {y} Q{200+dx} {y+80} {200+dx*1.2} {y+260}" stroke="#4a7a3a" stroke-width="4" fill="none"/>' for y in (160,200,240) for dx in (-120,-60,60,120,180))+figure(420,600,220,'#000',hair='#000')
I[1817]=svg(b,d)

# 1833 キャンディ キャンディ: a big tree on a gentle green hill with a ribbon tied to a branch and a letter, 1976 anime theme
d,b=bg([(0,'#9ad8ff'),(1,'#fff4e8')])
b+=cloud(160,180,1.2)+'<path d="M0 620 Q400 420 800 620 L800 800 L0 800Z" fill="#7ac85a"/><rect x="390" y="300" width="30" height="240" fill="#6a4a2a"/><circle cx="405" cy="260" r="130" fill="#4aa84a"/><circle cx="330" cy="300" r="70" fill="#3a983a"/><circle cx="480" cy="300" r="70" fill="#3a983a"/>'
b+='<path d="M470 360 Q440 340 450 330 Q470 340 470 360 Q500 340 490 330 Q470 340 470 360 L460 400 M470 360 L484 400" stroke="#ff4a8a" stroke-width="6" fill="#ff8ab0"/>'+''.join(flower(x,y,12,5,'#fff','#ffd02a') for x,y in [(200,640),(600,620),(300,700),(520,700)])
I[1833]=svg(b,d)

# 729 Go The Distance: a long road stretching across a vast plain toward distant mountains under a big sky, 2000
d,b=bg([(0,'#3a8ae8'),(1,'#e0f0ff')])
b+=cloud(200,160,1.2)+cloud(600,120,1.0)+hills(440,50,'#8a9ab8',729,4)+'<rect y="460" width="800" height="340" fill="#c8b878"/><path d="M396 460 L200 800 L600 800 L404 460Z" fill="#5a5a64"/><path d="M400 470 L400 800" stroke="#ffd02a" stroke-width="5" stroke-dasharray="30 30"/>'+figure(430,720,180,'#1a1a2a')
I[729]=svg(b,d)

# 425 ビリーヴ: a girl's silhouette holding up a glowing paper lantern to a starry sky, 2009 idol
d,b=bg([(0,'#0a1a4a'),(1,'#4a3a8a')])
b+=starsf(90,425,560)+'<path d="M0 640 Q400 560 800 640 L800 800 L0 800Z" fill="#0a0a1a"/>'+figure(360,620,220,'#000',pose='up',hair='#000')+'<path d="M380 280 L440 280 L450 360 L370 360Z" fill="#ffd27a"/>'+glow(410,320,120,'#ffd27a',.6)
b+=''.join(f'<path d="M{x-14} {y-14} L{x+14} {y-14} L{x+18} {y+14} L{x-18} {y+14}Z" fill="#ffd27a" opacity=".7"/>' for x,y in [(560,200),(640,140),(220,160)])
I[425]=svg(b,d)

# 427 PASSION: a flamenco-style dancer's silhouette with a swirling red skirt against a blazing sunset, 1985 idol
d,b=bg([(0,'#3a0a14'),(1,'#ff6a2a')])
b+='<circle cx="400" cy="460" r="200" fill="#ffb02a" opacity=".8"/><rect y="640" width="800" height="160" fill="#1a0a0a"/>'
b+=figure(400,640,340,'#1a0a0a',pose='up',hair='#1a0a0a')+'<path d="M380 460 Q260 560 220 640 Q400 600 600 660 Q520 560 420 460Z" fill="#c8102a"/>'
I[427]=svg(b,d)

# 133 ひなげしの花: a field of red poppies on a sunny hill with a girl in a sunhat, 1973 idol
d,b=bg([(0,'#9ad8ff'),(1,'#fff4e0')])
b+='<path d="M0 520 Q400 440 800 520 L800 800 L0 800Z" fill="#8ac86a"/>'+''.join(f'<path d="M{x} 800 L{x} {y}" stroke="#4a8a3a" stroke-width="3"/>'+flower(x,y,s,4,'#e8202a','#1a1a1a',x) for x,y,s in [(60,600,24),(150,560,20),(240,620,26),(560,580,22),(660,620,28),(740,560,20),(120,700,30),(620,720,32),(380,720,28)])
b+=figure(400,620,220,'#3a2a3a',hair='#3a2a3a')+'<ellipse cx="400" cy="420" rx="60" ry="14" fill="#f4e0b0"/><path d="M370 420 Q400 380 430 420Z" fill="#f4e0b0"/>'
I[133]=svg(b,d)

# 75 東京砂漠: a lone figure walking among towering grey skyscrapers like canyon walls, a hot sun above, 1976
d,b=bg([(0,'#e8b880'),(1,'#f4e0c0')])
b+='<circle cx="400" cy="140" r="60" fill="#fff4c8"/>'+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{800-y}" fill="{c}"/>' for x,y,w,c in [(0,100,180,'#7a7a84'),(160,260,120,'#8a8a94'),(620,80,180,'#7a7a84'),(520,240,120,'#8a8a94')])
b+=''.join(f'<rect x="{x}" y="{y}" width="20" height="14" fill="#5a5a64"/>' for x in (30,80,130,650,700,750) for y in range(140,780,50))+'<rect x="280" y="620" width="240" height="180" fill="#c8a880"/>'+figure(400,720,180,'#3a2a1a')
I[75]=svg(b,d)

# 1043 My Way: a swallowtail butterfly flying over a neon-lit immigrant city at night, 2015 band
d,b=bg([(0,'#0a0a1a'),(1,'#2a1a2a')])
b+=skyline(800,'#0a0a10',1043,120,360,'#ffd02a',80)+''.join(f'<rect x="{x}" y="{y}" width="40" height="20" fill="{c}" opacity=".7"/>' for x,y,c in [(80,560,'#ff4a4a'),(600,520,'#3affe8'),(300,600,'#ffd02a')])
b+='<g transform="translate(400 300) rotate(-12) scale(1.4)"><path d="M0 0 Q-120 -100 -140 -20 Q-120 40 0 10Z M0 0 Q120 -100 140 -20 Q120 40 0 10Z" fill="#ffd02a"/><path d="M0 10 Q-80 60 -60 140 Q-20 100 0 20Z M0 10 Q80 60 60 140 Q20 100 0 20Z" fill="#ff8a2a"/><path d="M-60 140 L-70 180 M60 140 L70 180" stroke="#ffd02a" stroke-width="6"/><rect x="-6" y="-30" width="12" height="80" rx="6" fill="#1a1a1a"/></g>'+glow(400,300,140,'#ffd02a',.25)
I[1043]=svg(b,d)

# 1778 Lifetime Respect: an elderly couple's hands with matching rings resting together, reggae warmth
d,b=bg([(0,'#3a8a3a'),(1,'#ffd04a')])
b+=rays(400,300,18,'#fff',.15,12)+'<path d="M0 560 Q160 480 320 460 L420 470 L400 540 Q200 580 0 660Z" fill="#c8987a"/><path d="M800 520 Q640 440 480 430 L380 450 L400 510 Q600 540 800 620Z" fill="#a8785a"/>'
b+=ring(360,470,16,'#e8c86a',6)+ring(470,445,16,'#e8c86a',6)+heart(420,300,40,'#e8302a')
I[1778]=svg(b,d)

# 560 From mermaid: a mermaid's tail silhouette diving into a moonlit sea with sparkling bubbles, 1988 idol
d,b=bg([(0,'#0a1a4a'),(1,'#1a5a9a')])
b+=moon(600,140,50)+'<rect y="360" width="800" height="440" fill="#0a3a7a"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#cfe6ff" stroke-width="3" opacity=".6"/>' for x,y,r in [(300,320,10),(320,280,7),(340,250,5),(480,560,12),(460,620,8)])
b+='<path d="M380 380 Q400 300 360 260 Q420 260 440 220 Q440 280 420 320 Q460 400 420 480Z" fill="#3ad8b8"/><path d="M360 260 L320 220 L360 240 L380 200Z" fill="#3ad8b8"/>'+''.join(ring(400,380,r,'#cfe6ff',3,.5) for r in (60,100))
I[560]=svg(b,d)

# 113 Darling: a single red rose and a love letter left on a piano lid under a spotlight, 1978 rock
d,b=bg([(0,'#1a0a0a'),(1,'#3a1a1a')])
b+='<path d="M360 0 L440 0 L600 600 L200 600Z" fill="#fff" opacity=".1"/><path d="M100 600 Q100 460 260 460 L560 460 Q700 480 700 600Z" fill="#0a0a0a"/>'
b+='<rect x="300" y="420" width="160" height="100" fill="#f4ece0" transform="rotate(-8 380 470)"/>'+heart(380,470,22,'#c8102a')+rose(520,440,.7,-30)+'<path d="M520 480 L620 540" stroke="#3a6a3a" stroke-width="6"/>'
I[113]=svg(b,d)

# 1130 GLAMOROUS SKY: a woman's silhouette on a rooftop under a glittering pink and violet sky, 2005 rock
d,b=bg([(0,'#2a0a4a'),(1,'#ff4a8a')])
b+=starsf(80,1130,560)+''.join(sparkle(x,y,s,'#fff') for x,y,s in [(140,160,24),(620,120,30),(480,260,18),(240,300,16)])+skyline(700,'#140a24',1130,60,220,'#ff8ad0',60)+'<rect y="700" width="800" height="100" fill="#0a0514"/>'
b+=figure(400,720,300,'#000',hair='#000')+'<path d="M370 470 L300 400" stroke="#000" stroke-width="14" stroke-linecap="round"/>'
I[1130]=svg(b,d)

for i,s in I.items(): open(f'/tmp/jprajz/svg/{i}.svg','w').write(s)
