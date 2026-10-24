# Amerikai motívumok a dalikonokhoz (a hl.py mellé; a hl.py-t ne módosítsd).
# Használat a g<N>.py-ban: import sys; sys.path[:0]=['/tmp/usrajz']; from hl import *; from us import *
# Minden függvény SVG-szöveget ad (800x800 viewBox).
import math,random
from hl import glow,R

def guitar(x,y,s,body='#c8442a',neck='#4a2a14',rot=0,edge='#f3d7a0'):
    # akusztikus gitár: két kör test, hanglyuk, nyak, fej
    g=f'<g transform="translate({x} {y}) rotate({rot}) scale({s/100})">'
    g+=f'<rect x="-9" y="-250" width="18" height="190" rx="4" fill="{neck}"/>'
    g+=f'<path d="M-16 -290 L16 -290 L12 -248 L-12 -248Z" fill="{neck}"/>'
    for k in range(3): g+=f'<circle cx="-20" cy="{-282+k*12}" r="4" fill="#ddd"/><circle cx="20" cy="{-282+k*12}" r="4" fill="#ddd"/>'
    g+=f'<circle cx="0" cy="-40" r="58" fill="{body}" stroke="{edge}" stroke-width="4"/><circle cx="0" cy="40" r="78" fill="{body}" stroke="{edge}" stroke-width="4"/>'
    g+=f'<rect x="-50" y="-40" width="100" height="70" fill="{body}"/>'
    g+=f'<circle cx="0" cy="-10" r="24" fill="#1a0e08"/><rect x="-30" y="66" width="60" height="10" rx="3" fill="{neck}"/>'
    for k in range(-2,4): g+=f'<line x1="{k*3-1.5}" y1="-250" x2="{k*3-1.5}" y2="70" stroke="#eee" stroke-width="1" opacity=".7"/>'
    return g+'</g>'

def eguitar(x,y,s,body='#d62a2a',neck='#3a2412',rot=0):
    # elektromos gitár (Strat-szerű)
    g=f'<g transform="translate({x} {y}) rotate({rot}) scale({s/100})">'
    g+=f'<rect x="-8" y="-260" width="16" height="200" rx="3" fill="{neck}"/><path d="M-10 -300 Q10 -310 18 -290 L10 -258 L-8 -258Z" fill="{neck}"/>'
    g+=f'<path d="M-40 -70 Q-30 -95 -10 -75 L10 -75 Q40 -110 55 -70 Q80 -20 60 30 Q75 80 30 95 Q0 105 -30 95 Q-75 80 -60 30 Q-80 -20 -40 -70Z" fill="{body}"/>'
    g+=f'<path d="M-20 -50 L30 -50 L40 40 L-30 40Z" fill="#f2f2f2" opacity=".9"/><rect x="-18" y="-20" width="36" height="6" fill="#333"/><rect x="-18" y="10" width="36" height="6" fill="#333"/><rect x="-14" y="55" width="28" height="8" fill="#333"/>'
    return g+'</g>'

def mic(x,y,s,col='#c9c9d2',stand=True,rot=0):
    # retro stúdiómikrofon (55-ös stílus) állvánnyal
    g=f'<g transform="translate({x} {y}) rotate({rot}) scale({s/100})">'
    if stand: g+='<rect x="-5" y="40" width="10" height="260" fill="#222"/><ellipse cx="0" cy="300" rx="60" ry="12" fill="#222"/>'
    g+=f'<rect x="-36" y="-80" width="72" height="120" rx="36" fill="{col}"/>'
    for k in range(7): g+=f'<line x1="-30" y1="{-60+k*14}" x2="30" y2="{-60+k*14}" stroke="#555" stroke-width="3"/>'
    g+='<rect x="-12" y="38" width="24" height="16" fill="#333"/>'
    return g+'</g>'

def vinyl(x,y,r,label='#d33',shine=True):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#0c0c0e"/>'
    for k in range(1,9): o+=f'<circle cx="{x}" cy="{y}" r="{r*(.38+k*.07):.0f}" fill="none" stroke="#2a2a2e" stroke-width="2"/>'
    o+=f'<circle cx="{x}" cy="{y}" r="{r*.32:.0f}" fill="{label}"/><circle cx="{x}" cy="{y}" r="{r*.04:.0f}" fill="#111"/>'
    if shine: o+=f'<path d="M{x-r*.7:.0f} {y-r*.5:.0f} A{r*.86:.0f} {r*.86:.0f} 0 0 1 {x+r*.2:.0f} {y-r*.85:.0f}" stroke="#fff" stroke-width="6" fill="none" opacity=".18"/>'
    return o

def car(x,y,s,col='#e23b3b',chrome='#e8e8ee',flip=False,glass='#9cd2ff'):
    # 50-es évekbeli amerikai autó oldalnézetből (farokúszó)
    t=f'translate({x} {y}) scale({-s/100 if flip else s/100} {s/100})'
    g=f'<g transform="{t}">'
    g+=f'<path d="M-200 -20 L-190 -60 L-120 -66 L-80 -110 L40 -110 L90 -66 L180 -60 L210 -80 L205 -20Z" fill="{col}"/>'
    g+=f'<path d="M-70 -100 L35 -100 L72 -66 L-105 -66Z" fill="{glass}" opacity=".85"/><line x1="-18" y1="-100" x2="-22" y2="-66" stroke="{col}" stroke-width="8"/>'
    g+=f'<rect x="-205" y="-30" width="415" height="12" rx="6" fill="{chrome}"/>'
    for cx in (-120,120): g+=f'<circle cx="{cx}" cy="-10" r="36" fill="#141414"/><circle cx="{cx}" cy="-10" r="18" fill="{chrome}"/>'
    g+=f'<circle cx="198" cy="-48" r="7" fill="#ffdf6a"/><circle cx="-192" cy="-46" r="7" fill="#ff4040"/>'
    return g+'</g>'

def hat(x,y,s,col='#8a5a2b',band='#3a2210'):
    # cowboykalap
    g=f'<g transform="translate({x} {y}) scale({s/100})">'
    g+=f'<path d="M-140 10 Q-150 -30 -110 -20 Q-60 0 0 0 Q60 0 110 -20 Q150 -30 140 10 Q80 40 0 40 Q-80 40 -140 10Z" fill="{col}"/>'
    g+=f'<path d="M-62 0 Q-70 -80 -40 -100 Q-20 -84 0 -92 Q20 -84 40 -100 Q70 -80 62 0Z" fill="{col}"/><path d="M-63 -14 Q0 -2 63 -14 L62 4 Q0 14 -62 4Z" fill="{band}"/>'
    return g+'</g>'

def palm(x,y,h,col='#0d1a14',lean=8):
    # pálmafa sziluett
    tx=x+lean*h/100;ty=y-h
    o=f'<path d="M{x-8} {y} Q{x+lean*h/200} {y-h/2} {tx-4} {ty} L{tx+4} {ty} Q{x+lean*h/200+10} {y-h/2} {x+8} {y}Z" fill="{col}"/>'
    for a in (-160,-125,-95,-60,-25,5,30):
        r=math.radians(a);L=h*.42
        ex,ey=tx+L*math.cos(r),ty+L*math.sin(r)+h*.12
        o+=f'<path d="M{tx} {ty} Q{tx+L*.55*math.cos(r):.0f} {ty+L*.55*math.sin(r)-h*.08:.0f} {ex:.0f} {ey:.0f} Q{tx+L*.5*math.cos(r):.0f} {ty+L*.5*math.sin(r)+4:.0f} {tx} {ty+6}Z" fill="{col}"/>'
    return o

def spotlight(x,y,w,col='#fff4c8',op=.28,y1=800):
    return f'<polygon points="{x-14},{y} {x+14},{y} {x+w},{y1} {x-w},{y1}" fill="{col}" opacity="{op}"/>'

def neon(txt,x,y,size,col='#ff3ea5',font='Georgia,serif',it=True,anchor='middle'):
    st=' font-style="italic"' if it else ''
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="700"{st} text-anchor="{anchor}" fill="{col}" opacity=".55" filter="url(#glow2)">{txt}</text>'
            f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="700"{st} text-anchor="{anchor}" fill="#fff" stroke="{col}" stroke-width="3">{txt}</text>')

def flagstripes(y0,h,op=.25):
    o=''
    for k in range(7): o+=f'<rect y="{y0+k*h*2}" width="800" height="{h}" fill="#b22234" opacity="{op}"/>'
    return o

def star5(x,y,r,col,rot=-90,op=1):
    p=[]
    for k in range(10):
        a=math.radians(rot+k*36);rr=r if k%2==0 else r*.42
        p.append(f'{x+rr*math.cos(a):.1f},{y+rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(p)}" fill="{col}" opacity="{op}"/>'

def disco(x,y,r,base='#c9ccd6'):
    # diszkógömb tükörlapokkal és csillanással
    o=f'<line x1="{x}" y1="0" x2="{x}" y2="{y-r}" stroke="#aaa" stroke-width="3"/><circle cx="{x}" cy="{y}" r="{r}" fill="{base}"/>'
    rr=random.Random(int(x+y))
    for i in range(-6,7):
        for j in range(-6,7):
            px,py=x+i*r/6.2,y+j*r/6.2
            if (px-x)**2+(py-y)**2<(r*.95)**2:
                c=rr.choice(['#ffffff','#9aa3b8','#e6e9f2','#6c7488','#cfd5e6'])
                o+=f'<rect x="{px-r/14:.0f}" y="{py-r/14:.0f}" width="{r/7.5:.0f}" height="{r/7.5:.0f}" fill="{c}"/>'
    o+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#555" stroke-width="2"/>'
    return o

def road(vx,vy,col='#2a2a2e',line='#ffd84a',w=520,y1=800):
    # perspektivikus országút a látóhatárig
    o=f'<polygon points="{vx-6},{vy} {vx+6},{vy} {vx+w},{y1} {vx-w},{y1}" fill="{col}"/>'
    for k in range(8):
        t0=(k/8)**1.7;t1=((k+.5)/8)**1.7
        ya,yb=vy+(y1-vy)*t0,vy+(y1-vy)*t1;wa,wb=2+10*t0,2+10*t1
        o+=f'<polygon points="{vx-wa/2:.0f},{ya:.0f} {vx+wa/2:.0f},{ya:.0f} {vx+wb/2:.0f},{yb:.0f} {vx-wb/2:.0f},{yb:.0f}" fill="{line}"/>'
    return o

def cactus(x,y,h,col='#123824'):
    w=h*.16
    return (f'<g fill="{col}"><rect x="{x-w/2}" y="{y-h}" width="{w}" height="{h}" rx="{w/2}"/>'
            f'<path d="M{x-w/2} {y-h*.45} L{x-w*1.6} {y-h*.45} Q{x-w*2.1} {y-h*.45} {x-w*2.1} {y-h*.6} L{x-w*2.1} {y-h*.75}" stroke="{col}" stroke-width="{w*.8}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{x+w/2} {y-h*.6} L{x+w*1.5} {y-h*.6} Q{x+w*2} {y-h*.6} {x+w*2} {y-h*.75} L{x+w*2} {y-h*.88}" stroke="{col}" stroke-width="{w*.8}" fill="none" stroke-linecap="round"/></g>')

def jukebox(x,y,s):
    g=f'<g transform="translate({x} {y}) scale({s/100})">'
    g+='<path d="M-120 0 L-120 -220 Q-120 -330 0 -330 Q120 -330 120 -220 L120 0Z" fill="#7a1f1f"/>'
    g+='<path d="M-95 -20 L-95 -215 Q-95 -305 0 -305 Q95 -305 95 -215 L95 -20Z" fill="#ffb347"/>'
    g+='<path d="M-70 -120 L-70 -210 Q-70 -275 0 -275 Q70 -275 70 -210 L70 -120Z" fill="#2a1a3a"/>'
    for k in range(5): g+=f'<rect x="-60" y="{-110+k*16}" width="120" height="8" rx="4" fill="{["#ff4f6d","#4fd2ff","#7dff6a","#ffe14f","#c56bff"][k]}"/>'
    g+='<rect x="-130" y="0" width="260" height="20" rx="6" fill="#3a0f0f"/>'
    return g+'</g>'
