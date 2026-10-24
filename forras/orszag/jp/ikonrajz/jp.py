# Japán motívumok a dalikonokhoz (a motor/ikonrajz/hl.py mellé; a hl.py-t ne módosítsd).
# Használat a g<N>.py-ban:  import sys; sys.path[:0]=['../../../motor/ikonrajz','.']; from hl import *; from jp import *
# Minden függvény SVG-szöveget ad vissza, 800x800-as viewBoxra méretezve; ami színátmenetet kér, (defs, body) párt ad.
import math,random
R=random.Random

def sakura(x,y,s,col='#ffc2d6',mid='#ff7aa8',rot=0,op=1):
    # cseresznyevirág: öt bevágott szirom, sötétebb közép
    o=f'<g transform="translate({x} {y}) rotate({rot}) scale({s/100})" opacity="{op}">'
    for k in range(5):
        o+=f'<path transform="rotate({k*72})" d="M0 0 C-34 -30 -30 -82 -10 -96 L0 -84 L10 -96 C30 -82 34 -30 0 0Z" fill="{col}"/>'
    o+=f'<circle r="16" fill="{mid}"/>'
    for k in range(5):
        a=math.radians(k*72+36);o+=f'<circle cx="{26*math.sin(a):.1f}" cy="{-26*math.cos(a):.1f}" r="4" fill="{mid}"/>'
    return o+'</g>'

def petals(n,seed,col='#ffd0e0',y0=0,y1=800,smin=8,smax=18,op=.85):
    # hulló szirmok (egy-egy ovális, kis bevágással)
    r=R(seed);o=''
    for _ in range(n):
        x,y,s,a=r.uniform(0,800),r.uniform(y0,y1),r.uniform(smin,smax),r.uniform(0,360)
        o+=f'<path transform="translate({x:.0f} {y:.0f}) rotate({a:.0f})" d="M0 {-s} C{s*.8} {-s*.6} {s*.6} {s*.6} 0 {s} C{-s*.6} {s*.6} {-s*.8} {-s*.6} 0 {-s}Z M-2 {-s} L0 {-s*.7} L2 {-s}Z" fill="{col}" opacity="{op*r.uniform(.6,1):.2f}"/>'
    return o

def fuji(cx,base,w,h,col='#3a4a7a',snow='#f4f6ff',id='fj'):
    # Fuji-hegy: lapos csúcs, csipkés hósapka; (defs, body)
    d=f'<linearGradient id="{id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="{col}" stop-opacity=".75"/></linearGradient>'
    t=w*.09;b=f'<path d="M{cx-w/2} {base} L{cx-t} {base-h} L{cx+t} {base-h} L{cx+w/2} {base}Z" fill="url(#{id})"/>'
    sy=base-h*.6;k=(base-sy)/h;sx=t+(w/2-t)*(1-k)  # hóhatár: a csúcstól a magasság 40%-áig, csipkés alsó széllel
    n=8;pts=' '.join(f'L{cx+sx-(2*sx)*i/n:.0f} {sy+(18 if i%2 else 0):.0f}' for i in range(n+1))
    b+=f'<path d="M{cx-t} {base-h} L{cx+t} {base-h} L{cx+sx:.0f} {sy:.0f} {pts} Z" fill="{snow}"/>'
    return d,b

def torii(x,base,h,col='#d8342c',dark='#1a1214'):
    # torii-kapu: két oszlop, ívelt felső gerenda (kasagi), alatta egyenes (nuki)
    w=h*.95;p=h*.075;o=''
    for sx in (x-w*.36,x+w*.36):
        o+=f'<path d="M{sx-p*.55} {base} L{sx-p*.42} {base-h*.86} L{sx+p*.42} {base-h*.86} L{sx+p*.55} {base}Z" fill="{col}"/>'
        o+=f'<rect x="{sx-p*.7}" y="{base-p*.6}" width="{p*1.4}" height="{p*.6}" fill="{dark}"/>'
    o+=f'<rect x="{x-w*.45}" y="{base-h*.7}" width="{w*.9}" height="{p*.7}" fill="{col}"/>'
    o+=f'<path d="M{x-w*.6} {base-h*.94} Q{x} {base-h*.82} {x+w*.6} {base-h*.94} L{x+w*.55} {base-h*.84} Q{x} {base-h*.75} {x-w*.55} {base-h*.84}Z" fill="{col}"/>'
    o+=f'<path d="M{x-w*.62} {base-h*.98} Q{x} {base-h*.86} {x+w*.62} {base-h*.98} L{x+w*.6} {base-h*.94} Q{x} {base-h*.82} {x-w*.6} {base-h*.94}Z" fill="{dark}"/>'
    o+=f'<rect x="{x-p*.4}" y="{base-h*.84}" width="{p*.8}" height="{h*.14}" fill="{col}"/>'
    return o

def chochin(x,y,s,col='#e8402a',glowc='#ffb070',mark=None):
    # papírlampion (chōchin): bordázott ovális, fekete tető és talp, opcionális felirat (1-2 írásjel)
    o=f'<circle cx="{x}" cy="{y}" r="{s*1.3}" fill="{glowc}" opacity=".35" filter="url(#glow)"/>'
    o+=f'<ellipse cx="{x}" cy="{y}" rx="{s*.72}" ry="{s}" fill="{col}"/>'
    for k in range(1,7):
        yy=y-s+k*2*s/7;ww=s*.72*math.sqrt(max(0,1-((yy-y)/s)**2))
        o+=f'<path d="M{x-ww:.1f} {yy:.1f} Q{x} {yy+s*.06:.1f} {x+ww:.1f} {yy:.1f}" stroke="#000" stroke-opacity=".18" stroke-width="{s*.02:.1f}" fill="none"/>'
    o+=f'<rect x="{x-s*.4}" y="{y-s*1.08}" width="{s*.8}" height="{s*.16}" rx="{s*.04}" fill="#15100c"/><rect x="{x-s*.4}" y="{y+s*.92}" width="{s*.8}" height="{s*.16}" rx="{s*.04}" fill="#15100c"/>'
    if mark: o+=f'<text x="{x}" y="{y+s*.18}" text-anchor="middle" font-family="Noto Sans JP,Noto Sans CJK JP,sans-serif" font-weight="700" font-size="{s*.62 if len(mark)<2 else s*.42}" fill="#15100c">{mark}</text>'
    return o

def wagasa(x,y,s,col='#c8283a',rot=-12,ribs='#f6e6c8'):
    # japán papír esernyő felülnézetből-oldalról: kupola bordákkal, nyél
    o=f'<g transform="translate({x} {y}) rotate({rot})">'
    o+=f'<path d="M{-s} 0 Q0 {-s*.95} {s} 0 Q0 {-s*.18} {-s} 0Z" fill="{col}"/>'
    for k in range(-4,5):
        o+=f'<path d="M0 {-s*.47} L{k*s/4.4:.1f} {-abs(k)*s*.004-s*.04:.1f}" stroke="{ribs}" stroke-opacity=".55" stroke-width="{s*.012:.1f}"/>'
    o+=f'<rect x="{-s*.015}" y="{-s*.48}" width="{s*.03}" height="{s*1.1}" fill="#3a2414"/><circle cy="{-s*.5}" r="{s*.04}" fill="#3a2414"/>'
    return o+'</g>'

def seigaiha(y0,col='#ffffff',op=.12,r=48,y1=800):
    # hullámminta (seigaiha): egymásra boruló félkörívek soronként eltolva
    o=f'<g fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="3">'
    row=0;y=y0
    while y<y1+r:
        off=(row%2)*r
        for x in range(-r*2,800+r*2,r*2):
            for k in (1,.72,.44):
                o+=f'<path d="M{x+off-r*k:.0f} {y} A{r*k:.0f} {r*k:.0f} 0 0 1 {x+off+r*k:.0f} {y}"/>'
        y+=r*.5;row+=1
    return o+'</g>'

def tokyo_tower(x,base,h,col='#ff5a2a',white='#f4f0e8'):
    # Tokió-torony: karcsú rácsos torony, piros-fehér sávok, két kilátószint
    o='';w=h*.34
    pts=lambda t:(w*(1-t)**1.6/2)
    for i in range(12):
        t0,t1=i/12,(i+1)/12;c=col if i%2==0 else white
        o+=f'<path d="M{x-pts(t0):.1f} {base-h*t0:.1f} L{x-pts(t1):.1f} {base-h*t1:.1f} L{x+pts(t1):.1f} {base-h*t1:.1f} L{x+pts(t0):.1f} {base-h*t0:.1f}Z" fill="{c}"/>'
    for t in (.36,.62):
        ww=pts(t)+h*.03;o+=f'<rect x="{x-ww:.1f}" y="{base-h*t-h*.025:.1f}" width="{2*ww:.1f}" height="{h*.05:.1f}" rx="{h*.01:.1f}" fill="{white}"/>'
    o+=f'<rect x="{x-h*.006:.1f}" y="{base-h*1.12:.1f}" width="{h*.012:.1f}" height="{h*.13:.1f}" fill="{white}"/>'
    o+=f'<path d="M{x-w*.36} {base} Q{x} {base-h*.18} {x+w*.36} {base}" fill="#000" opacity=".35"/>'
    return o

def shinkansen(x,y,s,col='#f4f6fa',stripe='#1c4ab8'):
    # 0-s sorozatú shinkansen oldalnézetből, kerek orral (a 60-as évek jelképe)
    o=f'<g transform="translate({x} {y}) scale({s/100})">'
    o+=f'<path d="M-300 -30 L60 -30 Q120 -30 150 0 Q160 14 140 22 L-300 22Z" fill="{col}"/>'
    o+=f'<path d="M-300 6 L150 6 Q156 12 146 16 L-300 16Z" fill="{stripe}"/>'
    o+=f'<path d="M66 -24 Q104 -24 126 -6 L74 -6Z" fill="#1a2a44"/>'
    for k in range(7): o+=f'<rect x="{-280+k*44}" y="-20" width="26" height="14" rx="3" fill="#1a2a44"/>'
    return o+'</g>'

def neon(x,y,text,col='#ff4fa0',size=70,font='Noto Sans JP,Noto Sans CJK JP,sans-serif',rot=0):
    # neonfelirat (rövid japán vagy latin szó): elmosott fény + vékony világos kontúr
    t=f'font-family="{font}" font-weight="700" font-size="{size}" text-anchor="middle"'
    return (f'<g transform="rotate({rot} {x} {y})"><text x="{x}" y="{y}" {t} fill="{col}" opacity=".9" filter="url(#glow2)">{text}</text>'
            f'<text x="{x}" y="{y}" {t} fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="{size*.04:.1f}">{text}</text>'
            f'<text x="{x}" y="{y}" {t} fill="{col}" opacity=".55">{text}</text></g>')

def enka_mic(x,y,s,col='#c8a24a'):
    # régi állványos énekesmikrofon (enka-színpad), aranyszínű rács
    o=f'<g transform="translate({x} {y}) scale({s/100})">'
    o+=f'<rect x="-5" y="40" width="10" height="260" fill="#2a2a30"/><ellipse cx="0" cy="300" rx="60" ry="12" fill="#1a1a20"/>'
    o+=f'<rect x="-36" y="-70" width="72" height="110" rx="36" fill="{col}"/>'
    for k in range(6): o+=f'<rect x="-30" y="{-56+k*16}" width="60" height="5" rx="2" fill="#000" opacity=".22"/>'
    o+=f'<rect x="-44" y="22" width="88" height="14" rx="7" fill="#3a3a44"/>'
    return o+'</g>'

def hinomaru_sun(x,y,r,col='#e8302a',op=1):
    # nagy vörös lemenő nap (nem zászló: háttérelemként, a horizonton)
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity="{op}"/>'
