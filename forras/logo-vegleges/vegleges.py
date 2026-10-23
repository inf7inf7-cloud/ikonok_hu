# Végleges IKONOK logó: maltipoo a bakelit címkéjén, lemezjátszó karral
import math
exec(open('../logo4/logo4.py').read().split('L=[]\nT=')[0])
d='''<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff1b8"/><stop offset=".25" stop-color="#f2c94c"/><stop offset=".5" stop-color="#b8860b"/><stop offset=".72" stop-color="#f7d774"/><stop offset="1" stop-color="#8a6212"/></linearGradient>
<radialGradient id="tilebg" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="#22305a"/><stop offset="1" stop-color="#0d1530"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000" flood-opacity=".45"/></filter>'''
gr=''.join(f'<circle cx="200" cy="210" r="{r}" fill="none" stroke="#7a5410" stroke-width="1.6" opacity=".45"/>' for r in range(76,140,8))
shine='<path d="M200 210 L112 98 A142 142 0 0 1 166 72 Z" fill="#fff" opacity=".28"/><path d="M200 210 L288 322 A142 142 0 0 1 234 348 Z" fill="#fff" opacity=".18"/>'
spark='<path d="M296 104 q4 14 18 18 q-14 4 -18 18 q-4 -14 -18 -18 q14 -4 18 -18z" fill="#fff6d0"/><path d="M110 318 q3 9 12 12 q-9 3 -12 12 q-3 -9 -12 -12 q9 -3 12 -12z" fill="#fff6d0" opacity=".8"/>'
mark=(sq(50,60,300,'url(#tilebg)')+'<g filter="url(#sh)"><circle cx="200" cy="210" r="142" fill="url(#gold)"/></g>'+gr+shine
      +'<circle cx="200" cy="210" r="66" fill="#14213d"/><circle cx="200" cy="210" r="66" fill="none" stroke="#f2c94c" stroke-width="4"/>'
      +dog(200,214,98,tongue='#ff6f86')+spark)
clip='<clipPath id="tile"><rect x="50" y="60" width="300" height="300" rx="69"/></clipPath>'
open('ikonok-jel.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="50 60 300 300" width="800" height="800"><defs>{d}{clip}</defs><g clip-path="url(#tile)">{mark}</g></svg>')
open('ikonok-logo-felirattal.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="30 40 760 340" width="1520" height="680"><defs>{d}{clip}</defs><g clip-path="url(#tile)">{mark}</g>{ik_ok(390,250,"#14213d","#c9971c")}</svg>')
