# a párosítatlan dalok előadóinak saját/Topic csatornáit bejárja (uploads, part=snippet: csak címek, olcsó, max 6 oldal)
# -> nyers/csatorna_cimek.json {chid:[[vid,cím,csatornanév],...]}; a párosítás után csak a talált videókat kérjük le (ytpar.py)
import json,sys,urllib.request,urllib.parse,collections,os
sys.path.insert(0,'/mnt/project-files/ikonok/orszag/fr/munka')
from osszefesul_n import lead,n
O='/mnt/project-files/ikonok/orszag/fr/munka/';N='/mnt/project-files/ikonok/orszag/fr/nyers/'
api=lambda ep,**p: json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/'+ep+'?'+urllib.parse.urlencode(p)))
J=json.load(open(O+'jeloltek.json'));P=json.load(open(O+'yt_par.json'));M=json.load(open(N+'videok.json'))
F=N+'csatorna_cimek.json';C=json.load(open(F)) if os.path.exists(F) else {}
ch=collections.defaultdict(set)
for k,p in P.items():
    if p['yt'] in M: ch[k.split('|')[0]].add((M[p['yt']]['chid'],M[p['yt']]['ch']))
need={lead(x['artist']) for x in J if x['k'] not in P}
q=sorted({cid for a in need for cid,cn in ch.get(a,()) if 'topic' in cn.lower() or a.replace(' ','') in n(cn).replace(' ','')}-set(C))
print(len(q),'csatorna',flush=True)
for i,c in enumerate(q):
    tok='';L=[]
    for _ in range(6):
        try: d=api('playlistItems',part='snippet',maxResults=50,playlistId='UU'+c[2:],pageToken=tok)
        except Exception as e: break
        L+=[[it['snippet']['resourceId']['videoId'],it['snippet']['title'],it['snippet']['channelTitle']] for it in d['items']]
        tok=d.get('nextPageToken')
        if not tok: break
    C[c]=L
    if i%20==19: json.dump(C,open(F,'w'),ensure_ascii=False);print(i+1,flush=True)
json.dump(C,open(F,'w'),ensure_ascii=False);print(sum(len(v) for v in C.values()),'cím')
