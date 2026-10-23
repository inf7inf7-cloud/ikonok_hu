# python3 web/mk_kartya.py -> kartya/<id>.jpg: 600x315-ös megosztókép dalonként (ikon + cím + előadó), a d/<id>.html og:image-e.
# A 256 px-es ikont a PC-s Viber (és más kliensek) túl kicsinek tartották, ezért nem mutattak képet (Miske, 10-23 15:20).
# Csak az új vagy változott (ikon, cím, előadó, év) dalokat rajzolja újra (kartya/_meta.json).
import json,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
B='/mnt/project-files/ikonok/';K=B+'kartya/'
os.makedirs(K,exist_ok=True)
F='/usr/share/fonts/opentype/inter/'
fb=lambda s:ImageFont.truetype(F+'Inter-Bold.otf',s);fm=lambda s:ImageFont.truetype(F+'Inter-Medium.otf',s)
logo=Image.open(B+'logo-vegleges/ikonok-jel-96.png').convert('RGBA').resize((44,44),Image.LANCZOS)
try: M=json.load(open(K+'_meta.json'))
except Exception: M={}
def fit(d,t,f,w):
    if d.textlength(t,font=f)<=w: return t
    while t and d.textlength(t+'…',font=f)>w: t=t[:-1]
    return t.rstrip()+'…'
def wrap(d,t,size,w,lines):  # cím: legfeljebb 2 sor, szükség esetén kisebb betűvel
    for s in (size,size-6,size-12):
        f=fb(s);ws=t.split();L=[];cur=''
        for x in ws:
            if d.textlength((cur+' '+x).strip(),font=f)<=w: cur=(cur+' '+x).strip()
            else: L.append(cur);cur=x
        L.append(cur);L=[l for l in L if l]
        if len(L)<=lines and all(d.textlength(l,font=f)<=w for l in L): return f,L
    return f,[fit(d,' '.join(L[:lines]) if False else L[0],f,w)]+([fit(d,' '.join(L[1:]),f,w)] if len(L)>1 else [])
def card(s):
    W,H=600,315;ic=Image.open(B+'ikon/%d.jpg'%s['id']).convert('RGB')
    bg=ic.resize((W,W)).crop((0,(W-H)//2,W,(W+H)//2)).filter(ImageFilter.GaussianBlur(28))
    bg=Image.blend(bg,Image.new('RGB',(W,H),(15,16,23)),0.72);im=bg.convert('RGBA');d=ImageDraw.Draw(im)
    S=235;x0,y0=28,(H-S)//2
    sh=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle((x0+4,y0+8,x0+S+4,y0+S+8),40,fill=(0,0,0,150));im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(10)))
    m=Image.new('L',(S,S),0);ImageDraw.Draw(m).rounded_rectangle((0,0,S-1,S-1),40,fill=255);im.paste(ic.resize((S,S),Image.LANCZOS),(x0,y0),m)
    d=ImageDraw.Draw(im);tx=x0+S+28;tw=W-tx-26
    f,L=wrap(d,s['title'],36,tw,2);y=92 if len(L)>1 else 112
    for l in L: d.text((tx,y),l,font=f,fill=(255,255,255));y+=f.size+8
    a=s['artist']+(' · %d'%s['year'] if s.get('year') else '');d.text((tx,y+4),fit(d,a,fm(21),tw),font=fm(21),fill=(190,193,210))
    im.alpha_composite(logo,(tx,24));xx=tx+54  # a logó színezése: IKON fehér, OK piros, .HU fehér (Miske, 10-23)
    for part,col in (('IKON',(255,255,255)),('OK',(224,24,42)),('.HU',(255,255,255))): d.text((xx,32),part,font=fb(24),fill=col);xx+=d.textlength(part,font=fb(24))
    d.text((tx,H-48),'▶  Bökj rá, és szól!',font=fm(18),fill=(255,255,255))
    im.convert('RGB').save(K+'%d.jpg'%s['id'],quality=80,optimize=True,progressive=True)
n=0
for s in json.load(open(B+'songs.json',encoding='utf-8')):
    p=B+'ikon/%d.jpg'%s['id']
    if s.get('hide') or not os.path.exists(p): continue
    k='v2|%s|%s|%s|%d'%(s['title'],s['artist'],s.get('year'),int(os.path.getmtime(p)))
    if M.get(str(s['id']))==k and os.path.exists(K+'%d.jpg'%s['id']): continue
    card(s);M[str(s['id'])]=k;n+=1
json.dump(M,open(K+'_meta.json','w'),ensure_ascii=False)
print(n,'megosztókép frissítve')
