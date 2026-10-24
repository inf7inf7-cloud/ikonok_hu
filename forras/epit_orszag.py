# python3 epit_orszag.py jp  ->  /tmp/jp-dist (a kész ország-oldal, ikonok.hu/jp/) + orszag/jp/jp-weboldal.zip
# Az ország oldala a MAGYAR oldal mai motorjából épül (mk_nyito.py, build_nyito.py, nyito_*, i18n/), így minden új funkció magától átkerül.
# Országos rész: orszag/<kód>/ = songs.json, top100_ids.json, ikon/, csere.json (pontos szövegcserék a nyito.tpl.html-en; ami nem található, az hiba),
# orszag.json (márka, útvonal, megosztószöveg), rol/<nyelv>.json forrása (natsumero_dalok.json leirasai).
# A magyar dist.py a végén ezt a zipet bontja ki a /jp/ mappába, így a magyar építés nem törli a japán oldalt.
import json,os,re,shutil,subprocess,sys,time,zipfile,hashlib,base64,html as H,datetime as _dt,zoneinfo as _zi
M=os.path.dirname(os.path.abspath(__file__));cc=sys.argv[1];C=f'{M}/orszag/{cc}';W=f'/tmp/epit-{cc}';D=f'/tmp/{cc}-dist'
O=json.load(open(C+'/orszag.json',encoding='utf-8'))
shutil.rmtree(W,ignore_errors=True);os.makedirs(W)
for f in ('mk_nyito.py','build_nyito.py','nyito_logic.js','nyito_extra.css','nyito_set.html','nyito_btn.html','nyito_head.html','plausible.html'): shutil.copy(f'{M}/{f}',W)
for d in ('mirahits-skill','i18n','logo-vegleges','web'): shutil.copytree(f'{M}/{d}',f'{W}/{d}',ignore=shutil.ignore_patterns('*.zip','__pycache__'))
shutil.copytree(C+'/ikon',W+'/ikon')
if os.path.isdir(f'/tmp/{cc}-ikon_webp'): shutil.copytree(f'/tmp/{cc}-ikon_webp',W+'/ikon_webp')  # helyi WebP-gyorsítótár
run=lambda c:subprocess.run(c,shell=True,cwd=W,check=True)
# dalok: csak a kész ikonnal rendelkező dal jelenik meg (Miske szabálya: betűs helykitöltő nem lehet); a többi rejtve, amíg az ikonja el nem készül
S=json.load(open(C+'/songs.json',encoding='utf-8'))
for x in S:
    if not os.path.exists(f"{C}/ikon/{x['id']}.jpg"): x['hide']=True
json.dump(S,open(W+'/songs.json','w',encoding='utf-8'),ensure_ascii=False)
shutil.copy(C+'/top100_ids.json',W)
run('python3 mk_nyito.py')
t=open(W+'/nyito.tpl.html',encoding='utf-8').read()
for a,b in json.load(open(C+'/csere.json',encoding='utf-8')):
    assert a in t,'csere.json: nem található: '+a[:80];t=t.replace(a,b)
# ábécérend az ország nyelvén, olvasat (kana) szerint: x.localeCompare(y,'hu') -> KC(x,y)
t,n=re.subn(r"([\w\[\]]+)\.localeCompare\(([\w\[\]]+),'hu'\)",r"KC(\1,\2)",t);assert n>=4,n
open(W+'/nyito.tpl.html','w',encoding='utf-8').write(t)
run('python3 build_nyito.py')
t=open(W+'/index.html',encoding='utf-8').read()
V=[x for x in S if not x.get('hide')]
KANA={};KR={}
for x in V:
    if x.get('artist_kana'): KANA[x['artist']]=x['artist_kana']
    if x.get('title_kana'): KANA[x['title']]=x['title_kana']
    if x.get('artist_rom'): KR[x['artist']]=x['artist_rom']
LG=O['lang']
desc="(function(){var C={},cur={},L0='';function ld(){var l=document.documentElement.lang;l=l==='hu'||l==='"+LG+"'?l:'en';if(l===L0)return;L0=l;(C[l]||(C[l]=fetch('rol/'+l+'.json').then(function(r){return r.json()}).catch(function(){return {}}))).then(function(m){if(L0===l)cur=m})}"\
 "ld();new MutationObserver(ld).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});return typeof Proxy==='function'?new Proxy({},{get:function(_,k){return cur[k]}}):{}})()"
extra='KANA='+json.dumps(KANA,ensure_ascii=False,separators=(',',':'))+',KR='+json.dumps(KR,ensure_ascii=False,separators=(',',':'))+",KC=function(a,b){return String(KANA[a]||a).localeCompare(String(KANA[b]||b),'"+LG+"')},"
assert t.count(',DESC={},')==1
k=t.index(',DESC={},');t=t[:k]+t[k:].replace(',DESC={},',',DESC='+desc+',',1).replace('DATA={top:[]};',extra+'DATA={top:[]};',1)
open(W+'/index.html','w',encoding='utf-8').write(t)
shutil.rmtree(f'/tmp/{cc}-ikon_webp',ignore_errors=True);shutil.copytree(W+'/ikon_webp',f'/tmp/{cc}-ikon_webp')
# --- weboldal (a dist.py mintájára) ---
shutil.rmtree(D,ignore_errors=True);os.makedirs(D+'/ikon')
ids=[x['id'] for x in V]
for i in ids: shutil.copy(f'{W}/ikon/{i}.jpg',D+'/ikon/');shutil.copy(f'{W}/ikon_webp/{i}.webp',D+'/ikon/')
PL=open(W+'/plausible.html',encoding='utf-8').read()
t=re.sub(r'(<head[^>]*>)',lambda m:m.group(1)+'\n'+PL,t,count=1)
try: VER=int(open(C+'/ver.txt').read().strip())+1
except Exception: VER=1
open(C+'/ver.txt','w').write(str(VER))
BLD=_dt.datetime.now(_zi.ZoneInfo(O['tz'])).strftime('%Y.%m.%d. %H:%M')
t=t.replace('</body>','<p id="bld"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" rel="noopener">Build: '+BLD+' · '+cc.upper()+' v'+str(VER)+'</a></p>\n</body>',1)
os.makedirs(D+'/a')
def asset(name,ext,data):
    b=data.encode() if isinstance(data,str) else data;h=hashlib.sha1(b).hexdigest()[:10];fn=f'a/{name}.{h}.{ext}'
    open(f'{D}/{fn}','wb').write(b);return fn
m=re.search(r'<style>(.*?)</style>',t,re.S);t=t[:m.start()]+'<link rel="stylesheet" href="'+asset('app','css',m.group(1))+'">'+t[m.end():]
m=re.search(r'<script>(\s*var ALL=.*?)</script>',t,re.S);js=m.group(1)
d=re.search(r'var ALL=.*?DATA=\{top:\[\]\};',js,re.S)
fd=asset(cc,'js',d.group(0));fa=asset('app','js',js[:d.start()]+js[d.end():])
t=t[:m.start()]+'<script src="'+fd+'"></script><script src="'+fa+'"></script>'+t[m.end():]
m=re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)',t);t=t[:m.start()]+asset('logo','png',base64.b64decode(m.group(1)))+t[m.end():]
open(D+'/index.html','w',encoding='utf-8').write(t)
for f in ('favicon.ico','favicon-16.png','favicon-32.png','apple-touch-icon.png','icon-192.png','icon-512.png','icon-maskable-512.png'): shutil.copy(f'{M}/web/{f}',D)
shutil.copy(C+'/og.jpg' if os.path.exists(C+'/og.jpg') else f'{M}/web/og.jpg',D+'/og.jpg')
open(D+'/sw.js','w').write(open(W+'/web/sw.js').read().replace('/*VER*/',cc+time.strftime('%Y%m%d%H%M')))
json.dump({'id':'./','name':O['manifest_name'],'short_name':O['short'],'description':O['description'],'lang':LG,'dir':'ltr','start_url':'./','scope':'./','display':'standalone','orientation':'any','background_color':'#0f1017','theme_color':'#0f1017','categories':['music','entertainment'],
 'icons':[{'src':'icon-192.png','sizes':'192x192','type':'image/png','purpose':'any'},{'src':'icon-512.png','sizes':'512x512','type':'image/png','purpose':'any'},{'src':'icon-maskable-512.png','sizes':'512x512','type':'image/png','purpose':'maskable'}]},open(D+'/manifest.webmanifest','w'),ensure_ascii=False)
shutil.copytree(W+'/i18n_json',D+'/i18n')
# dalok egymondatos leírása a felület nyelvén (hu, en, az ország nyelve; a többi nyelven angolul): rol/<nyelv>.json
os.makedirs(D+'/rol');R=json.load(open(C+'/natsumero_dalok.json',encoding='utf-8'));vis=set(ids)
for l in ('hu','en',LG): json.dump({str(r['id']):r['leiras_'+l] for r in R if r['id'] in vis and r.get('leiras_'+l)},open(f'{D}/rol/{l}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
# dalonkénti megosztó lapok: d/<id>.html, az előnézet a dal ikonja
SITE=O['site'];os.makedirs(D+'/d')
for x in V:
    i=x['id'];tt=H.escape(x['title']+' – '+x['artist'],quote=True);dd=H.escape(O['megoszto_leiras'].format(artist=x['artist'],title=x['title'],ev=('(%d)'%x['year']) if x.get('year') else ''),quote=True);img=f'{SITE}/ikon/{i}.jpg'
    open(f'{D}/d/{i}.html','w',encoding='utf-8').write(f"""<!doctype html><html lang="{LG}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{tt} – IKONOK.HU</title><meta name="description" content="{dd}"><meta name="robots" content="noindex,follow"><link rel="canonical" href="{SITE}/d/{i}.html"><link rel="icon" href="../favicon.ico">
<meta property="og:type" content="music.song"><meta property="og:site_name" content="IKONOK.HU"><meta property="og:locale" content="{O['og_locale']}"><meta property="og:title" content="{tt}"><meta property="og:description" content="{dd}"><meta property="og:url" content="{SITE}/d/{i}.html">
<meta property="og:image" content="{img}"><meta property="og:image:width" content="256"><meta property="og:image:height" content="256"><meta property="og:image:type" content="image/jpeg"><meta name="twitter:card" content="summary"><meta name="twitter:image" content="{img}">
<script>location.replace('../#d{i}'+(location.hash.length>1?'.'+location.hash.slice(1):''))</script></head>
<body style="font-family:system-ui,sans-serif;text-align:center;padding:40px"><p><a href="../#d{i}">{tt} – IKONOK.HU</a></p></body></html>""")
ZL=f'/tmp/{cc}-weboldal.zip';z=zipfile.ZipFile(ZL,'w',zipfile.ZIP_DEFLATED)
for r,_,fs in os.walk(D):
    for f in fs: z.write(os.path.join(r,f),os.path.join(r,f)[len(D)+1:])
z.close();shutil.copy(ZL,f'{C}/{cc}-weboldal.zip')
print(cc,'v%d'%VER,len(ids),'dal (ikonnal),',len(S)-len(ids),'rejtve;',os.path.getsize(ZL)//1024,'KB zip; kész:',D)
