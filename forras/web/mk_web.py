# python3 web/mk_web.py -> web/: favicon, alkalmazásikonok (telepítéshez), megosztási kép (og.png)
from PIL import Image
import json,os,subprocess
L=Image.open('logo-vegleges/ikonok-jel-800.png').convert('RGBA')
BG=(24,34,72,255)
def flat(sz,scale=1.0):
    c=Image.new('RGBA',(sz,sz),BG);s=int(sz*scale);l=L.resize((s,s),Image.LANCZOS);c.alpha_composite(l,((sz-s)//2,(sz-s)//2));return c
def tr(sz):return L.resize((sz,sz),Image.LANCZOS)
tr(32).save('web/favicon-32.png');tr(16).save('web/favicon-16.png')
tr(48).save('web/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
flat(180).convert('RGB').save('web/apple-touch-icon.png')
tr(192).save('web/icon-192.png');tr(512).save('web/icon-512.png')
flat(512,.78).save('web/icon-maskable-512.png')
print('ikonok kesz')
