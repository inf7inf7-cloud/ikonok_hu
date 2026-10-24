# jelöltek <-> YouTube-videók párosítása (a begyűjtött lejátszási listákból + kereső-gyorsítótár) -> munka/yt_par.json
import json,re,sys,os,unicodedata
sys.path.insert(0,'/mnt/project-files/ikonok/orszag/fr/munka');
N='/mnt/project-files/ikonok/orszag/fr/nyers/';O='/mnt/project-files/ikonok/orszag/fr/munka/'
from osszefesul_n import n,lead
J=json.load(open(O+'jeloltek.json'));M=json.load(open(N+'videok.json'));V=json.load(open(N+'pl_items.json'))
if os.path.exists(N+'kereses.json'):
    for q,items in json.load(open(N+'kereses.json')).items():
        for vid,m in items.items(): M.setdefault(vid,m)
def dur(s):
    m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',s or '');return sum(int(x or 0)*k for x,k in zip(m.groups(),(3600,60,1))) if m else 0
BAD=re.compile(r'\b(live|en concert|karaoke|karaoké|cover|reprise|remix|instrumental|piano|tuto|parodie|medley|extrait|teaser|lyrics? (en|english)|1 hour|1 heure|slowed|sped up|nightcore|mix 20|playlist|best of|full album|album complet)\b',re.I)
VT={vid:(n(m['t']),n(m['ch'])) for vid,m in M.items()}
res={}
for x in J:
    t=n(x['title']);a=lead(x['artist']);toks=[w for w in a.split() if len(w)>2] or a.split()
    if not t: continue
    best=None
    for vid,(vt,vc) in VT.items():
        if not re.search(r'(^| )'+re.escape(t)+r'( |$)',vt): continue
        ac=a.replace(' ','')
        if not (all(re.search(r'(^| )'+re.escape(w)+r'( |$)',vt+' '+vc) for w in toks) or ac in vc.replace(' ','')): continue
        m=M[vid]
        if m.get('priv')!='public' or m.get('emb') is False: continue
        rr=m.get('rr') or {}
        if 'FR' in rr.get('blocked',[]) or ('allowed' in rr and 'FR' not in rr['allowed']): continue  # Franciaországból tiltott
        d=dur(m.get('dur'));
        if d and (d<90 or d>720): continue
        if BAD.search(m['t']) and not BAD.search(x['title']): continue
        off=bool(re.search(r'vevo|official|officiel|- topic',m['ch'],re.I)) or a.replace(' ','') in vc.replace(' ','')
        sc=(off, m['views'])
        if not best or sc>best[0]: best=(sc,vid)
    if best:
        vid=best[1];m=M[vid];res[x['k']]={'yt':vid,'views':m['views'],'pub':m['pub'],'ch':m['ch'],'t':m['t'],'npl':len(set(V.get(vid,{}).get('pl',[]))),'rr':m.get('rr',{})}
json.dump(res,open(O+'yt_par.json','w'),ensure_ascii=False,indent=0)
print(len(res),'/',len(J),'párosítva')
