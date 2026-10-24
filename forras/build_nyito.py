# python3 build_nyito.py -> index.html (saját tárhelyre) és artifact.html (Claude-nézőhöz), a MIRAHITS ikonoldal-sablonból
import json,os,re,base64
S=json.load(open('songs.json',encoding='utf-8'))
TOP=json.load(open('top100_ids.json'))
# Top 100: elérhetetlen videójú dal (youtube/elerheto.py 'yt_nem') nem lehet benne; a helyét a sikerindex szerinti következő, lejátszható dal tölti ki
_ok=lambda x:x.get('yt') and not x.get('yt_nem') and not x.get('hide') and os.path.exists('ikon/%d.jpg'%x['id'])
_SI={x['id']:x for x in S}
TOP=[i for i in TOP if i in _SI and _ok(_SI[i])]
TOP+=[x['id'] for x in sorted(S,key=lambda x:-(x.get('index') or 0)) if _ok(x) and x['id'] not in TOP][:100-len(TOP)]
# Toplista 1000-ig, 100-as dobozokban a Válogatóban (Miske, 10-23 14:58): a top 100 után százanként ugyanazokkal a szabályokkal,
# mint az index_v3.py top 100-a (sikerindex szerint, dobozonként előadónként max. 3, évtizedenként a katalógus arányában)
import collections
_art=lambda x:re.split(r'\s+(?:x|feat\.?|ft\.?|&|és)\s+',x['artist'])[0].strip().lower()
_dec=lambda x:(x.get('year') or 0)//10*10
_nd=collections.Counter(_dec(x) for x in S if _ok(x));_q={d:round(100*c/sum(_nd.values())) for d,c in _nd.items()}
RL=list(TOP);_rk=sorted([x for x in S if _ok(x)],key=lambda x:-(x.get('index') or 0))
while True:  # a Sikerindex nézethez minden dal helyezést kap (a 100-as blokkszabályokkal)
    _in=set(RL);_p=[x for x in _rk if x['id'] not in _in]
    if not _p: break
    B=[];_c=collections.Counter();_d=collections.Counter()
    for x in _p:
        if len(B)<100 and _c[_art(x)]<3 and _d[_dec(x)]<_q[_dec(x)]: B.append(x['id']);_c[_art(x)]+=1;_d[_dec(x)]+=1
    for x in _p:
        if len(B)<100 and _c[_art(x)]<3 and x['id'] not in B: B.append(x['id']);_c[_art(x)]+=1
    for x in _p:
        if len(B)<100 and x['id'] not in B: B.append(x['id'])
    RL+=B
RL+=[x['id'] for x in sorted(S,key=lambda x:-(x.get('index') or 0)) if not x.get('hide') and x['id'] not in set(RL)]
ALL=[[x['id'],x['year'] or 0,x['artist'],x['title'],x.get('yt') or '',x.get('index') or 0] for x in S if not x.get('hide')]
# Mostanában slágerek doboz (Miske, 10-23; korábban Aktuális): az utóbbi 1 év dalai, sikerindex szerint. 'date' a youtube/elerheto.py-ból;
# [id,dátum] párok 400 napra visszamenőleg, a böngésző a mai naptól számolt 365 napra szűr (évváltáskor sem kell kézzel állítani)
import datetime
_c=str(datetime.date.today()-datetime.timedelta(400))
FRESH=[[x['id'],x['date']] for x in sorted([x for x in S if not x.get('hide') and x.get('date','')>=_c],key=lambda x:-(x.get('index') or 0))]
ICON={x['id']:1 for x in S if os.path.exists('ikon/%d.jpg'%x['id'])}
# a weboldal WebP ikonokat tölt (kb. negyed akkora, mint a JPG); a JPG marad a megosztási előnézethez és az artifacthoz. Gyorsítótár: ikon_webp/
from PIL import Image
os.makedirs('ikon_webp',exist_ok=True)
for _i in ICON:
    _j,_w='ikon/%d.jpg'%_i,'ikon_webp/%d.webp'%_i
    if not os.path.exists(_w) or os.path.getmtime(_w)<os.path.getmtime(_j): Image.open(_j).convert('RGB').save(_w,'WEBP',quality=80,method=6)
# Dalok egymondatos összefoglalója a lejátszó alatt (Miske, 10-24): dalszoveg/osszefoglalo.json, a dalszoveg/osszesit.py állítja elő
DESC=json.load(open('dalszoveg/osszefoglalo.json',encoding='utf-8')) if os.path.exists('dalszoveg/osszefoglalo.json') else {}
# Többnyelvű felület (Miske, 10-24): kulcsok (magyar szövegek) beégetve, a fordítások i18n_json/<kód>.json, futáskor töltődik be
import sys as _s;_s.path.insert(0,'i18n');from nyelvek import L as _NY
I18K=[l.rstrip('\n') for l in open('i18n/kulcsok.txt',encoding='utf-8') if not l.startswith('#') and l.strip()]
os.makedirs('i18n_json',exist_ok=True);I18L=[]
for _c,_n,_d in _NY:
    _f='i18n/%s.txt'%_c;_ok=_c=='hu'
    if not _ok and os.path.exists(_f):
        _t=[l.rstrip('\n') for l in open(_f,encoding='utf-8')]
        while _t and not _t[-1].strip(): _t.pop()
        if len(_t)==len(I18K): json.dump(_t,open('i18n_json/%s.json'%_c,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'));_ok=True
        else: print('FORDÍTÁS HIBA',_c,len(_t),'sor, kellene',len(I18K))
    if _ok: I18L.append([_c,_n,_d])
logo='data:image/png;base64,'+base64.b64encode(open('logo-vegleges/ikonok-jel-96.png','rb').read()).decode()
t=open('nyito.tpl.html',encoding='utf-8').read()
t=t.replace('/*DATA*/','var ALL='+json.dumps(ALL,ensure_ascii=False,separators=(',',':'))+',TOPI='+json.dumps(TOP)+',RLI='+json.dumps(RL)+',FRESH='+json.dumps(FRESH)+',ICON='+json.dumps(ICON,separators=(',',':'))+',DESC='+json.dumps(DESC,ensure_ascii=False,separators=(',',':'))+',I18K='+json.dumps(I18K,ensure_ascii=False,separators=(',',':'))+',I18L='+json.dumps(I18L,ensure_ascii=False,separators=(',',':'))+',DATA={top:[]};').replace('/*LOGO*/',logo)
open('index.html','w',encoding='utf-8').write(t)
# artifact: skeleton nélkül
head=re.search(r'<title>.*?</title>',t).group(0)+'<meta name="claude:viewport-fit-sides" content="cover">'+re.search(r'<link rel="stylesheet" href="https://fonts.googleapis[^>]*>',t).group(0)+re.search(r'<style>.*?</style>',t,re.S).group(0)
body=t.split('<body class="nojs">',1)[1].rsplit('</body>',1)[0]
# artifact: legfeljebb 511 fájl lehet benne, ezért az ikonok csomagokban (ikonpack/p<N>.json, id -> data URI) mennek
PK={};order=[i for i in TOP if i in ICON]+[x['id'] for x in sorted(S,key=lambda x:-(x.get('index') or 0)) if x['id'] in ICON and x['id'] not in TOP]
for k,i in enumerate(order): PK[i]=1 if k<len(TOP) else 2+(k-len(TOP))//60
ab=body.replace("document.body.className='js'","document.body.classList.add('js')").replace('ICON='+json.dumps(ICON,separators=(',',':')),'ICON='+json.dumps(PK,separators=(',',':')))
ab=ab.replace('\'<img src="ikon/\'+id+\'.webp"','\'<img data-ik="\'+id+\'" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="')
LD="""<script>(function(){var C={};function pk(n){return C[n]||(C[n]=fetch('ikonpack/p'+n+'.json').then(function(r){return r.json()}).catch(function(){delete C[n];return {}}))}
function fix(){document.querySelectorAll('img[data-ik]').forEach(function(im){var id=im.getAttribute('data-ik');im.removeAttribute('data-ik');var n=ICON[id];if(n==null)return;pk(n).then(function(m){if(m[id])im.src=m[id]})})}
new MutationObserver(function(){fix()}).observe(document.documentElement,{childList:true,subtree:true});document.addEventListener('DOMContentLoaded',fix);fix()})();</script>"""
open('artifact.html','w',encoding='utf-8').write(head+'<div class="nojs" id="bodyc"></div>'+ab+LD)
os.makedirs('ikonpack',exist_ok=True)
G={}
for i,n in PK.items(): G.setdefault(n,{})[str(i)]='data:image/jpeg;base64,'+base64.b64encode(open('ikon/%d.jpg'%i,'rb').read()).decode()
for n,m in G.items(): json.dump(m,open('ikonpack/p%d.json'%n,'w'),separators=(',',':'))
print(len(G),'ikoncsomag')
print(len(t)//1024,'KB')
