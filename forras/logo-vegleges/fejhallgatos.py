# Végleges IKONOK logó (2026-10-22 12:56): maltipoo fej fejhallgatóval, sötétkék csempén, piros fejhallgató
exec(open('../logo3/logo3.py').read().split('L=[]')[0])
d='''<radialGradient id="tilebg" cx=".5" cy=".3" r=".85"><stop offset="0" stop-color="#26346a"/><stop offset="1" stop-color="#0d1530"/></radialGradient>
<linearGradient id="cupg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff4b5c"/><stop offset="1" stop-color="#c8102e"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#000" flood-opacity=".4"/></filter>'''
def ph(cx,cy,s):
    k=s/200
    return (f'<path d="M{cx-96*k} {cy+4*k} V{cy-24*k} A{96*k} {96*k} 0 0 1 {cx+96*k} {cy-24*k} V{cy+4*k}" fill="none" stroke="#e0182a" stroke-width="{18*k}" stroke-linecap="round"/>'
            +f'<path d="M{cx-86*k} {cy-30*k} A{86*k} {86*k} 0 0 1 {cx+86*k} {cy-30*k}" fill="none" stroke="#ff8a95" stroke-width="{4*k}" stroke-linecap="round" opacity=".7"/>'
            +sq(cx-124*k,cy-22*k,52*k,'url(#cupg)',.45)+sq(cx+72*k,cy-22*k,52*k,'url(#cupg)',.45)
            +f'<circle cx="{cx-98*k}" cy="{cy+4*k}" r="{9*k}" fill="#ffd166"/><circle cx="{cx+98*k}" cy="{cy+4*k}" r="{9*k}" fill="#ffd166"/>')
notes=('<g fill="#ffd166"><g transform="translate(300 112) rotate(14)"><ellipse cx="0" cy="22" rx="12" ry="9"/><rect x="8" y="-16" width="5" height="40"/><path d="M13 -16 q20 6 16 26 q-4 -14 -16 -16z"/></g>'
       '<g transform="translate(92 120) rotate(-12) scale(.75)"><ellipse cx="0" cy="22" rx="12" ry="9"/><rect x="8" y="-16" width="5" height="40"/><path d="M13 -16 q20 6 16 26 q-4 -14 -16 -16z"/></g></g>')
mark=sq(50,60,300,'url(#tilebg)')+notes+'<g filter="url(#sh)">'+dog(200,226,196,tongue='#ff6f86')+ph(200,226,196)+'</g>'
clip='<clipPath id="tile"><rect x="50" y="60" width="300" height="300" rx="69"/></clipPath>'
open('ikonok-jel.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="50 60 300 300" width="800" height="800"><defs>{d}{clip}</defs><g clip-path="url(#tile)">{mark}</g></svg>')
open('ikonok-logo-felirattal.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="30 40 760 340" width="1520" height="680"><defs>{d}{clip}</defs><g clip-path="url(#tile)">{mark}</g>{ik_ok(390,250,"#14213d","#e0182a")}</svg>')
