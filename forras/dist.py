# python3 dist.py -> /tmp/ikonok-dist/ (feltölthető statikus weboldal) + ikonok-weboldal.zip
# Gyorsítás (Miske, 10-23 16:20): a sok ezer kis fájlt helyi lemezen rakja össze és tömöríti, a hálózati meghajtóra csak a kész zip kerül
# (korábban a /mnt alatti dist/ törlése és írása 10+ percig tartott). A dist/ mappa a projektmappában már nem frissül.
import json,shutil,os,zipfile
os.system('python3 /mnt/project-files/ikonok/youtube/elerheto.py')  # elérhetetlen videó -> yt_nem, ilyen dal nem kerül a top 100-ba (hálózat nélkül a régi jelölés marad)
os.system('cd /tmp && python3 /mnt/project-files/ikonok/index_v3.py --ir')  # sikerindex v3: friss nézettség minden építéskor
os.system('python3 dalszoveg/osszesit.py');os.system('python3 build_nyito.py')
D='/tmp/ikonok-dist';shutil.rmtree(D,ignore_errors=True);os.makedirs(D+'/ikon',exist_ok=True)  # a halozati meghajton a torles nem mindig teljes
ids=[int(f[:-4]) for f in os.listdir('ikon') if f.endswith('.jpg')]
for i in ids: shutil.copy(f'ikon/{i}.jpg',f'{D}/ikon/')
for s in (512,192): shutil.copy(f'logo-vegleges/ikonok-jel-{s}.png',f'{D}/logo-{s}.png')  # regi nevek, maradnak
t=open('index.html',encoding='utf-8').read()
# Plausible mérőkód (Miske kérése) a head elejére, csak a feltölthető változatba
import re
PL=open('plausible.html',encoding='utf-8').read()
def pl(h): return re.sub(r'(<head[^>]*>)',lambda m:m.group(1)+'\n'+PL,h,count=1)
t=pl(t)
# build dátum és verzió a nyitólap aljára (Miske, 10-23 18:00; rákattintva rickroll, 18:04); a verziószám minden dist.py futáskor eggyel nő (ver.txt)
import time as _t
try: VER=int(open('ver.txt').read().strip())+1
except Exception: VER=104
open('ver.txt','w').write(str(VER))
import datetime as _dt,zoneinfo as _zi
BLD=_dt.datetime.now(_zi.ZoneInfo('Europe/Budapest')).strftime('%Y.%m.%d. %H:%M')
t=t.replace('</body>','<p id="bld"><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" rel="noopener">Build: '+BLD+' · v'+str(VER)+'</a></p>\n</body>',1)
# Szétbontás (Miske, 10-24 11:06: kis, gyors oldalak): a stílus, a program és a dal-adat külön, tartalom szerinti nevű fájlba kerül (a/),
# így a böngésző egy évig tárolhatja őket, és visszatérő látogatónál csak a pár KB-os HTML töltődik le. Az artifact.html továbbra is egyben van.
import hashlib,base64
os.makedirs(f'{D}/a',exist_ok=True)
def asset(name,ext,data):
    b=data.encode() if isinstance(data,str) else data;h=hashlib.sha1(b).hexdigest()[:10];fn=f'a/{name}.{h}.{ext}'
    open(f'{D}/{fn}','wb').write(b);return fn
m=re.search(r'<style>(.*?)</style>',t,re.S);t=t[:m.start()]+'<link rel="stylesheet" href="'+asset('app','css',m.group(1))+'">'+t[m.end():]
m=re.search(r'<script>(\s*var ALL=.*?)</script>',t,re.S);js=m.group(1)
d=re.search(r'var ALL=.*?DATA=\{top:\[\]\};',js,re.S)
fd=asset('hu','js',d.group(0));fa=asset('app','js',js[:d.start()]+js[d.end():])
t=t[:m.start()]+'<script src="'+fd+'"></script><script src="'+fa+'"></script>'+t[m.end():]
m=re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)',t);t=t[:m.start()]+asset('logo','png',base64.b64decode(m.group(1)))+t[m.end():]
open(f'{D}/_headers','w').write('/a/*\n  Cache-Control: public, max-age=31536000, immutable\n/ikon/*\n  Cache-Control: public, max-age=2592000\n')
open(f'{D}/index.html','w',encoding='utf-8').write(t)
# telepithetoseg (PWA), favicon, megosztasi kep: web/ (python3 web/mk_web.py keszitette)
import time
for f in ('favicon.ico','favicon-16.png','favicon-32.png','apple-touch-icon.png','icon-192.png','icon-512.png','icon-maskable-512.png','og.jpg'): shutil.copy('web/'+f,f'{D}/{f}')
open(f'{D}/sw.js','w').write(open('web/sw.js').read().replace('/*VER*/',time.strftime('%Y%m%d%H%M')))
json.dump({'id':'./','name':'IKONOK.HU – magyar slágerek ikonokban','short_name':'IKONOK','description':'A magyar könnyűzene legsikeresebb számai ikonokban. Kattints egy ikonra, és szól a dal.','lang':'hu','dir':'ltr','start_url':'./','scope':'./','display':'standalone','orientation':'any','background_color':'#0f1017','theme_color':'#0f1017','categories':['music','entertainment'],
 'icons':[{'src':'icon-192.png','sizes':'192x192','type':'image/png','purpose':'any'},{'src':'icon-512.png','sizes':'512x512','type':'image/png','purpose':'any'},{'src':'icon-maskable-512.png','sizes':'512x512','type':'image/png','purpose':'maskable'}],
 'screenshots':[{'src':'og.jpg','sizes':'1200x630','type':'image/jpeg','form_factor':'wide','label':'IKONOK.HU'}]},open(f'{D}/manifest.webmanifest','w'),ensure_ascii=False)
# szamonkenti megoszto oldalak: d/<id>.html (elonezet a dal ikonjaval), a megnyito a fooldalra kerul (#d<id>.<nezet>)
import html as H
SITE='https://ikonok.hu';shutil.rmtree(f'{D}/i18n',ignore_errors=True);shutil.copytree('i18n_json',f'{D}/i18n');os.makedirs(f'{D}/d',exist_ok=True);
# megosztókép (600x315, ikon + cím): a 256 px-es ikont a PC-s Viber nem mutatta (web/mk_kartya.py, csak a változottakat rajzolja)
# 10-24 (Miske): nincs külön megosztókép, az előnézet maga a dal ikonja (ikon/<id>.jpg); a web/mk_kartya.py nem fut
for x in json.load(open('songs.json',encoding='utf-8')):
    if x.get('hide'): continue
    i=x['id'];t=H.escape(x['title']+' – '+x['artist'],quote=True);dd=H.escape('Bökj rá, és szól! '+x['artist']+': '+x['title']+(' ('+str(x['year'])+')' if x.get('year') else '')+' az IKONOK.HU-n.',quote=True)
    ik=os.path.exists('ikon/%d.jpg'%i)
    img=SITE+('/ikon/%d.jpg'%i if ik else '/og.jpg')
    # meta refresh nincs: a link-elonezet keszitok (Viber) kovettek, es a fooldal kepet mutattak
    open(f'{D}/d/{i}.html','w',encoding='utf-8').write(f"""<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} – IKONOK.HU</title><meta name="description" content="{dd}"><meta name="robots" content="noindex,follow"><link rel="canonical" href="{SITE}/d/{i}.html"><link rel="icon" href="../favicon.ico">
<meta property="og:type" content="music.song"><meta property="og:site_name" content="IKONOK.HU"><meta property="og:locale" content="hu_HU"><meta property="og:title" content="{t}"><meta property="og:description" content="{dd}"><meta property="og:url" content="{SITE}/d/{i}.html">
<meta property="og:image" content="{img}">{'<meta property="og:image:width" content="256"><meta property="og:image:height" content="256">' if '/ikon/' in img else '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'}<meta property="og:image:type" content="image/jpeg"><meta name="twitter:card" content="summary"><meta name="twitter:image" content="{img}">
<script>location.replace('../#d{i}'+(location.hash.length>1?'.'+location.hash.slice(1):''))</script></head>
<body style="font-family:system-ui,sans-serif;text-align:center;padding:40px"><p><a href="../#d{i}">{t} – IKONOK.HU</a></p></body></html>""")
os.makedirs(f'{D}/admin',exist_ok=True);open(f'{D}/admin/index.html','w',encoding='utf-8').write(pl(open('admin.html',encoding='utf-8').read()));shutil.copy('songs.json',f'{D}/admin/songs.json')
open(f'{D}/OLVASSEL.txt','w',encoding='utf-8').write('''IKONOK weboldal
Feltöltés: a mappa teljes tartalmát másold a tárhely gyökerébe (pl. public_html). Más nem kell, statikus oldal.
- index.html: a weboldal (adatok és logó beépítve), ikon/: a dalikonok.
- d/: számonkénti megosztó oldalak (a továbbküldött link ide mutat, az előnézet a dal ikonja; az oldal a https://ikonok.hu címet feltételezi).
- admin/: a karbantartó felület. Nyisd meg a saját gépeden, töltsd be a songs.json-t, szerkeszd, mentsd, és küldd vissza Claude-nak az oldal újraépítéséhez. Ha nem akarod nyilvánossá tenni, ne töltsd fel az admin mappát.
- YouTube: a beágyazott lejátszás saját tárhelyen működik, amint a számokhoz videóazonosító kerül a songs.json "yt" mezőjébe. Addig a lejátszó a YouTube-keresésre mutató linket ad.
''')
ZL='/tmp/ikonok-weboldal.zip';z=zipfile.ZipFile(ZL,'w',zipfile.ZIP_DEFLATED)
for r,_,fs in os.walk(D):
    for f in fs: z.write(os.path.join(r,f),os.path.join(r,f)[len(D)+1:])
z.close();shutil.copy(ZL,'ikonok-weboldal.zip');print(len(ids),'ikon',os.path.getsize('ikonok-weboldal.zip')//1024,'KB')
