import math,random
from hl import *
from jp import *
# közös segédfüggvények a g2-től (felhő, virág, hó, villám)
def cloud(x,y,s,col='#fff',op=.92):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{col}" opacity="{op}"><ellipse cx="0" cy="0" rx="90" ry="34"/><circle cx="-30" cy="-22" r="34"/><circle cx="24" cy="-30" r="42"/><circle cx="62" cy="-8" r="28"/></g>'
def flower(x,y,r,n,col,mid,rot=0,petal=.55):
    o=f'<g transform="translate({x} {y}) rotate({rot})">'
    for k in range(n): o+=f'<ellipse cx="0" cy="{-r*.55:.1f}" rx="{r*petal*.5:.1f}" ry="{r*.5:.1f}" fill="{col}" transform="rotate({k*360/n:.1f})"/>'
    return o+f'<circle r="{r*.25:.1f}" fill="{mid}"/></g>'
def snow(n,seed,op=.85,y1=800):
    r=R(seed);return ''.join(f'<circle cx="{r.uniform(0,800):.0f}" cy="{r.uniform(0,y1):.0f}" r="{r.choice([2,3,4,5])}" fill="#fff" opacity="{r.uniform(.4,op):.2f}"/>' for _ in range(n))
def bolt(pts,col,w=8,op=1):
    return f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" opacity="{op}"/>'


def rose(x,y,s,rot=0):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'+''.join(f'<path d="M0 0 C-50 -10 -46 -70 0 -76 C46 -70 50 -10 0 0Z" fill="{c}" transform="rotate({a}) scale({k})"/>' for a,c,k in [(0,'#a8081e',1),(60,'#c81028',.9),(-60,'#c81028',.9),(150,'#e01a34',.7),(-150,'#e01a34',.7)])+'</g>'
def star5(x,y,s,col,rot=0):
    return f'<path transform="rotate({rot} {x} {y})" d="'+' '.join(f'{"M" if k==0 else "L"}{x+s*(1 if k%2==0 else .42)*math.sin(k*math.pi/5):.1f} {y-s*(1 if k%2==0 else .42)*math.cos(k*math.pi/5):.1f}' for k in range(10))+f'Z" fill="{col}"/>'


def guitar(x,y,s,a,col='#c8702a'):
    return f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><ellipse cx="0" cy="60" rx="70" ry="64" fill="{col}"/><ellipse cx="0" cy="-10" rx="52" ry="50" fill="{col}"/><circle cx="0" cy="30" r="20" fill="#1a1a1a"/><rect x="-8" y="-220" width="16" height="200" fill="#3a2414"/><rect x="-14" y="-260" width="28" height="44" rx="4" fill="#3a2414"/></g>'
def phone(x,y,s,col='#1a1a1a'):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-120 -20 Q-130 -60 -90 -60 L90 -60 Q130 -60 120 -20 L80 -20 L70 -40 L-70 -40 L-80 -20Z" fill="{col}"/><path d="M-100 0 L100 0 L120 100 L-120 100Z" fill="{col}"/><circle cx="0" cy="50" r="34" fill="#f4f0e8"/>'+''.join(f'<circle cx="{24*math.cos(math.radians(a)):.0f}" cy="{50+24*math.sin(math.radians(a)):.0f}" r="5" fill="{col}"/>' for a in range(0,360,36))+'</g>'
