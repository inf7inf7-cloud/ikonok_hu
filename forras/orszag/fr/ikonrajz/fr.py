# Francia és általános motívumok a dalikonokhoz (a hl.py mellé; a hl.py-t ne módosítsd).
# Használat: import sys; sys.path[:0]=['/mnt/project-files/ikonok/orszag/fr/ikonrajz']; from hl import *; from fr import *
# Minden függvény SVG-szöveget ad, 800x800-as viewBoxra.
import math,random
from hl import glow,sparkle
R=random.Random
def eiffel(x,base,h,col='#2a2238',lit=None):
    # Eiffel-torony sziluett: ívelt lábak, két kilátószint, csúcs
    w=h*.42;o=f'<g fill="{col}">'
    o+=f'<path d="M{x-w/2} {base} Q{x-w*.2} {base-h*.28} {x-w*.12} {base-h*.42} L{x+w*.12} {base-h*.42} Q{x+w*.2} {base-h*.28} {x+w/2} {base} L{x+w*.32} {base} Q{x} {base-h*.26} {x-w*.32} {base}Z"/>'
    o+=f'<rect x="{x-w*.2}" y="{base-h*.3}" width="{w*.4}" height="{h*.025}"/>'
    o+=f'<path d="M{x-w*.12} {base-h*.42} L{x-w*.04} {base-h*.78} L{x+w*.04} {base-h*.78} L{x+w*.12} {base-h*.42}Z"/>'
    o+=f'<rect x="{x-w*.13}" y="{base-h*.56}" width="{w*.26}" height="{h*.02}"/>'
    o+=f'<path d="M{x-w*.04} {base-h*.78} L{x} {base-h} L{x+w*.04} {base-h*.78}Z"/></g>'
    if lit: o+=f'<circle cx="{x}" cy="{base-h}" r="{h*.012}" fill="{lit}"/>'+f'<circle cx="{x}" cy="{base-h}" r="{h*.05}" fill="{lit}" opacity=".3" filter="url(#glow)"/>'
    return o
def roofs(y0,col,seed,chim='#000'):
    # párizsi háztetők: manzárdtetők, kémények, kis ablakok
    r=R(seed);x=-20;o=f'<g fill="{col}">'
    while x<820:
        w=r.randint(70,130);h=r.randint(40,110)
        o+=f'<path d="M{x} 800 L{x} {y0-h} L{x+12} {y0-h-38} L{x+w-12} {y0-h-38} L{x+w} {y0-h} L{x+w} 800Z"/>'
        for k in range(r.randint(1,3)): cx=x+r.randint(14,w-20);o+=f'<rect x="{cx}" y="{y0-h-60}" width="12" height="26"/>'
        x+=w
    return o+'</g>'
def vinyl(x,y,r,label='#d8342c',col='#0c0c10'):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>'
    for k in range(5): o+=f'<circle cx="{x}" cy="{y}" r="{r*(.5+k*.1):.0f}" fill="none" stroke="#2a2a34" stroke-width="{max(1,r*.012):.1f}"/>'
    o+=f'<path d="M{x-r*.7} {y-r*.45} A{r*.83} {r*.83} 0 0 1 {x+r*.1} {y-r*.82}" stroke="#fff" stroke-width="{r*.04:.0f}" fill="none" opacity=".18"/>'
    return o+f'<circle cx="{x}" cy="{y}" r="{r*.33:.0f}" fill="{label}"/><circle cx="{x}" cy="{y}" r="{r*.04:.0f}" fill="#eee"/>'
def micro(x,y,s,col='#c8ccd8',grille='#5a5e6a'):
    # régi stúdiómikrofon állvánnyal (x,y = fej közepe)
    return (f'<rect x="{x-6*s}" y="{y+40*s}" width="{12*s}" height="{170*s}" fill="#2a2a30"/><ellipse cx="{x}" cy="{y+212*s}" rx="{60*s}" ry="{12*s}" fill="#2a2a30"/>'
     f'<rect x="{x-34*s}" y="{y-60*s}" width="{68*s}" height="{110*s}" rx="{34*s}" fill="{col}"/>'
     +''.join(f'<rect x="{x-26*s}" y="{y-44*s+k*13*s}" width="{52*s}" height="{5*s}" rx="{2*s}" fill="{grille}"/>' for k in range(6))
     +f'<path d="M{x-46*s} {y+10*s} Q{x-46*s} {y+60*s} {x} {y+62*s} Q{x+46*s} {y+60*s} {x+46*s} {y+10*s}" stroke="#3a3a42" stroke-width="{7*s}" fill="none"/>')
def guitar(x,y,s,rot=0,body='#c8682a',dark='#3a1a0a'):
    # akusztikus gitár (x,y = hangnyílás)
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
     f'<path d="M0 -70 C60 -70 70 -20 50 10 C90 40 90 120 0 130 C-90 120 -90 40 -50 10 C-70 -20 -60 -70 0 -70Z" fill="{body}"/>'
     f'<circle r="22" fill="{dark}"/><rect x="-10" y="-280" width="20" height="215" fill="{dark}"/><rect x="-16" y="-320" width="32" height="44" rx="6" fill="{dark}"/>'
     f'<rect x="-24" y="70" width="48" height="10" fill="{dark}"/>'+''.join(f'<path d="M{-6+k*4} -300 L{-6+k*4} 75" stroke="#f0e6d0" stroke-width="1.4"/>' for k in range(4))+'</g>')
def accordion(x,y,s,col='#c8202a',kb='#f6efe2'):
    o=f'<g transform="translate({x} {y}) scale({s})"><rect x="-150" y="-90" width="70" height="180" rx="10" fill="{kb}"/>'
    o+=''.join(f'<rect x="-140" y="{-80+k*20}" width="50" height="10" rx="3" fill="#222"/>' for k in range(8))
    o+=''.join(f'<path d="M{-80+k*16} -90 L{-72+k*16} -80 L{-72+k*16} 80 L{-80+k*16} 90Z" fill="{col if k%2 else "#111"}"/>' for k in range(10))
    o+=f'<rect x="80" y="-90" width="70" height="180" rx="10" fill="{col}"/>'+''.join(f'<circle cx="{98+(k%3)*17}" cy="{-66+(k//3)*24}" r="6" fill="{kb}"/>' for k in range(21))
    return o+'</g>'
def wineglass(x,y,s,wine='#8a1030',glass='#e8f0ff'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-50 -120 Q-56 -20 0 10 Q56 -20 50 -120Z" fill="{glass}" opacity=".35"/>'
     f'<path d="M-52 -70 Q-50 -10 0 8 Q50 -10 52 -70Z" fill="{wine}"/><rect x="-4" y="8" width="8" height="100" fill="{glass}" opacity=".7"/><ellipse cy="110" rx="44" ry="8" fill="{glass}" opacity=".7"/></g>')
def rose(x,y,s,col='#d81a3a',leaf='#2a7a3a',stem=True):
    o=f'<g transform="translate({x} {y}) scale({s})">'
    if stem: o+=f'<path d="M0 30 Q10 120 -6 220" stroke="{leaf}" stroke-width="9" fill="none"/><path d="M4 110 Q50 80 70 100 Q40 130 4 110Z" fill="{leaf}"/>'
    o+=f'<path d="M-46 -4 Q-50 -50 0 -56 Q50 -50 46 -4 Q40 40 0 42 Q-40 40 -46 -4Z" fill="{col}"/>'
    o+=f'<path d="M-30 -10 Q-20 -40 10 -36 Q34 -26 24 4 Q4 20 -14 6" stroke="#7a0a1a" stroke-width="6" fill="none"/><path d="M-10 -14 Q0 -26 10 -16" stroke="#7a0a1a" stroke-width="5" fill="none"/>'
    return o+'</g>'
def sun(x,y,r,col='#ffd23f',n=16):
    return glow(x,y,r*1.9,col,.45)+''.join(f'<path d="M{x+math.cos(a)*r*1.15:.0f} {y+math.sin(a)*r*1.15:.0f} L{x+math.cos(a)*r*1.6:.0f} {y+math.sin(a)*r*1.6:.0f}" stroke="{col}" stroke-width="{r*.12:.0f}" stroke-linecap="round"/>' for a in [i*2*math.pi/n for i in range(n)])+f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>'
def waves(y,col,amp=14,n=8,op=1,dy=0):
    d=f'M-10 800 L-10 {y}'
    for i in range(n): x0=-10+i*820/n;d+=f' Q{x0+820/n/4:.0f} {y-amp+dy} {x0+820/n/2:.0f} {y} T{x0+820/n:.0f} {y}'
    return f'<path d="{d} L810 800Z" fill="{col}" opacity="{op}"/>'
def palm(x,y,h,col='#0a1a10',lean=10):
    tx=x+lean;ty=y-h;o=f'<path d="M{x-8} {y} Q{x+lean*.3} {y-h*.5} {tx-4} {ty} L{tx+4} {ty} Q{x+lean*.3+10} {y-h*.5} {x+8} {y}Z" fill="{col}"/>'
    for a in (-160,-120,-70,-20,20,-200):
        r=math.radians(a);ex,ey=tx+math.cos(r)*h*.45,ty+math.sin(r)*h*.25+h*.08
        o+=f'<path d="M{tx} {ty} Q{(tx+ex)/2:.0f} {min(ty,ey)-h*.12:.0f} {ex:.0f} {ey:.0f} Q{(tx+ex)/2:.0f} {min(ty,ey)-h*.02:.0f} {tx} {ty+6}Z" fill="{col}"/>'
    return o
def discoball(x,y,r):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9aa0b8"/>'
    rr=R(int(x+y))
    for i in range(-5,6):
        for j in range(-5,6):
            cx,cy=x+i*r/5.5,y+j*r/5.5
            if (cx-x)**2+(cy-y)**2<(r*.95)**2: o+=f'<rect x="{cx-r/12:.0f}" y="{cy-r/12:.0f}" width="{r/6.5:.0f}" height="{r/6.5:.0f}" fill="{rr.choice(["#e8ecff","#b8c0e0","#7a80a0","#fff"])}"/>'
    return o+f'<rect x="{x-2}" y="0" width="4" height="{y-r}" fill="#888"/>'+sparkle(x-r*.4,y-r*.4,r*.35,'#fff')
def car(x,y,s,col='#d8342c',win='#9ad0ff'):
    # kis retró autó oldalnézetből (x,y = talppont közepe)
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-150 -30 L-150 -70 Q-140 -86 -100 -90 L-60 -140 Q-50 -150 0 -150 L50 -150 Q70 -148 90 -100 L140 -90 Q160 -86 160 -60 L160 -30Z" fill="{col}"/>'
     f'<path d="M-52 -96 L-20 -136 L10 -136 L10 -96Z M24 -96 L24 -136 L50 -136 Q64 -132 76 -96Z" fill="{win}"/><circle cx="-90" cy="-30" r="30" fill="#1a1a1e"/><circle cx="-90" cy="-30" r="12" fill="#aaa"/><circle cx="100" cy="-30" r="30" fill="#1a1a1e"/><circle cx="100" cy="-30" r="12" fill="#aaa"/></g>')
def phone(x,y,s,col='#d8342c'):
    # régi tárcsás telefon
    o=f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 60 L-80 -30 L80 -30 L110 60Z" fill="{col}"/><circle cy="10" r="50" fill="#f6efe2"/><circle cy="10" r="16" fill="{col}"/>'
    o+=''.join(f'<circle cx="{math.cos(math.radians(-60+k*30))*34:.0f}" cy="{10+math.sin(math.radians(-60+k*30))*34:.0f}" r="7" fill="#333"/>' for k in range(10))
    return o+f'<path d="M-130 -40 Q-130 -80 -90 -80 L90 -80 Q130 -80 130 -40 L100 -40 Q100 -54 80 -56 L-80 -56 Q-100 -54 -100 -40Z" fill="{col}"/></g>'
def crown(x,y,s,col='#ffd23f'):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-100 40 L-110 -60 L-50 -10 L0 -80 L50 -10 L110 -60 L100 40Z" fill="{col}"/><rect x="-100" y="40" width="200" height="26" fill="{col}"/>'+''.join(f'<circle cx="{c}" cy="53" r="8" fill="#d8342c"/>' for c in (-60,0,60))+'</g>'
def headphones(x,y,s,col='#d8342c'):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-110 30 Q-110 -110 0 -110 Q110 -110 110 30" stroke="#1a1a20" stroke-width="22" fill="none"/><rect x="-140" y="10" width="60" height="100" rx="24" fill="{col}"/><rect x="80" y="10" width="60" height="100" rx="24" fill="{col}"/></g>'
def tricolore(x,y,w,h,wave=0):
    # francia zászló, enyhén lobogó
    c=['#1a3aa8','#f6f6f6','#e0242a'];o=''
    for k in range(3):
        x0=x+k*w/3;o+=f'<path d="M{x0} {y+wave*k*.3} Q{x0+w/6} {y-wave+wave*k*.3} {x0+w/3} {y+wave*(k+1)*.3} L{x0+w/3} {y+h+wave*(k+1)*.3} Q{x0+w/6} {y+h-wave+wave*k*.3} {x0} {y+h+wave*k*.3}Z" fill="{c[k]}"/>'
    return o
def snow(n,seed,col='#fff',op=.85):
    r=R(seed);return ''.join(f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(0,800):.0f}" r="{r.choice([2,3,4,5])}" fill="{col}" opacity="{r.uniform(.4,op):.2f}"/>' for _ in range(n))
def boat(x,y,s,col='#f6efe2',sail='#fff',hull='#1a2a4a'):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-120 0 L120 0 L90 40 L-90 40Z" fill="{hull}"/><rect x="-4" y="-200" width="8" height="200" fill="#3a2a1a"/><path d="M8 -190 L110 -10 L8 -10Z" fill="{sail}"/><path d="M-8 -160 L-90 -10 L-8 -10Z" fill="{col}"/></g>'
def train(x,y,s,col='#2a2a30',light='#ffd27a'):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-160" y="-110" width="220" height="90" rx="10" fill="{col}"/><rect x="60" y="-160" width="90" height="140" rx="8" fill="{col}"/><rect x="-140" y="-180" width="36" height="72" fill="{col}"/>'
     f'<rect x="80" y="-140" width="50" height="40" fill="{light}"/>'+''.join(f'<circle cx="{c}" cy="-12" r="26" fill="#111"/><circle cx="{c}" cy="-12" r="8" fill="#888"/>' for c in (-120,-50,20,100))+f'<circle cx="-170" cy="-80" r="12" fill="{light}"/></g>')
def stage_lights(n,y,cols,op=.18):
    o=''
    for k in range(n):
        x=80+k*640/(max(1,n-1));c=cols[k%len(cols)]
        o+=f'<polygon points="{x},{y} {x-140+k*20},800 {x+140-k*20},800" fill="{c}" opacity="{op}"/>'+f'<circle cx="{x}" cy="{y}" r="16" fill="{c}"/>'
    return o
def keys(x,y,w,n=14,h=None):
    # zongorabillentyűk felülnézetből
    h=h or w/n*5;kw=w/n;o=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f6efe2"/>'
    o+=''.join(f'<rect x="{x+i*kw:.0f}" y="{y}" width="2" height="{h}" fill="#555"/>' for i in range(n))
    o+=''.join(f'<rect x="{x+i*kw+kw*.65:.0f}" y="{y}" width="{kw*.7:.0f}" height="{h*.6:.0f}" fill="#111"/>' for i in range(n-1) if i%7 not in (2,6))
    return o
