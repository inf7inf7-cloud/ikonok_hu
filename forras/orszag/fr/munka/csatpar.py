# a párosítatlan jelöltek címét az előadók csatornáinak feltöltéseiben keresi; a talált videók részleteit lekéri (videos.list, 1 egység/50)
# -> nyers/kereses.json {"csatorna":{vid:meta}}, amit a ytpar.py beolvas
import json,re,sys,os,urllib.request,urllib.parse
sys.path.insert(0,'/mnt/project-files/ikonok/orszag/fr/munka')
from osszefesul_n import n,lead
O='/mnt/project-files/ikonok/orszag/fr/munka/';N='/mnt/project-files/ikonok/orszag/fr/nyers/'
api=lambda ep,**p: json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/'+ep+'?'+urllib.parse.urlencode(p)))
J=json.load(open(O+'jeloltek.json'));P=json.load(open(O+'yt_par.json'));C=json.load(open(N+'csatorna_cimek.json'))
K=json.load(open(N+'kereses.json')) if os.path.exists(N+'kereses.json') else {}
have=set(json.load(open(N+'videok.json')))|{v for d in K.values() for v in d}
T=[(vid,n(t),n(ch)) for L in C.values() for vid,t,ch in L]
want=set()
for x in J:
    if x['k'] in P: continue
    t=n(x['title']);a=lead(x['artist']);toks=[w for w in a.split() if len(w)>2] or a.split()
    if not t: continue
    rx=re.compile(r'(^| )'+re.escape(t)+r'( |$)')
    for vid,vt,vc in T:
        if rx.search(vt) and (a.replace(' ','') in vc.replace(' ','') or all(re.search(r'(^| )'+re.escape(w)+r'( |$)',vt+' '+vc) for w in toks)): want.add(vid)
want-=have;want=sorted(want);print(len(want),'új videó')
D=K.setdefault('csatorna',{})
for i in range(0,len(want),50):
    for it in api('videos',part='snippet,statistics,contentDetails,status',id=','.join(want[i:i+50]),maxResults=50)['items']:
        s=it['snippet'];D[it['id']]={'t':s['title'],'ch':s['channelTitle'],'chid':s['channelId'],'pub':s['publishedAt'][:10],'desc':s.get('description','')[:200],
          'views':int(it.get('statistics',{}).get('viewCount',0)),'dur':it['contentDetails'].get('duration'),'emb':it['status'].get('embeddable'),'priv':it['status'].get('privacyStatus'),
          'rr':it['contentDetails'].get('regionRestriction',{})}
json.dump(K,open(N+'kereses.json','w'),ensure_ascii=False);print(len(D),'részletezve')
