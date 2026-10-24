# Francia dallista + sikerindex: jeloltek.json + yt_par.json -> munka/dallista.json (rangsorolt), dallista.tsv (áttekintéshez)
import json,math,re,sys
sys.path.insert(0,'/mnt/project-files/ikonok/orszag/fr/munka')
from osszefesul_n import n,lead,key
O='/mnt/project-files/ikonok/orszag/fr/munka/'
J=json.load(open(O+'jeloltek.json'));P=json.load(open(O+'yt_par.json'))
# összevonás: régi kulcs -> megmaradó kulcs; törlés: nem francia fő előadó vagy kitalált/dupla sor
MERGE={'philippe d avilla|rois du monde':'roméo et juliette|rois du monde','dix commandements|envie d aimer':'daniel levi|envie d aimer',
 'cecilia cara|aimer':'roméo et juliette|aimer','andrea bocelli|vivo per lei':'helene segara|vivo per lei','bonnie tyler|si demain':'kareen antonn|si demain',
 'jul|bande organisee':'13 organise|bande organisee','celine dion|sous le vent':'garou|sous le vent','compagnons de la chanson|trois cloches':'edith piaf|trois cloches',
 'florent pagny|encore':'kendji girac|encore','j balvin|mi gente':'willy william|mi gente','maluma|hola senorita':'gims|hola senorita'}
DROP={'shakira|je l aime a mourir','julien dore|moi lolita','johnny hallyday|vivre','daniel lavoie|temps des cathedrales','tina arena|trois cloches','dhurata dora|zemer',
 'jean philippe audin|song of ocarina','garou|belle'}
NEV={'roméo et juliette|rois du monde':('Roméo et Juliette','Les Rois du monde'),'roméo et juliette|aimer':('Roméo et Juliette','Aimer'),'edith piaf|trois cloches':('Édith Piaf et les Compagnons de la chanson','Les Trois Cloches'),
 'helene segara|vivo per lei':('Hélène Ségara et Andrea Bocelli','Vivo per lei'),'notre dame de paris|belle':('Garou, Daniel Lavoie et Patrick Fiori','Belle'),'garou|sous le vent':('Garou et Céline Dion','Sous le vent'),
 'willy william|mi gente':('J Balvin et Willy William','Mi gente'),'gims|hola senorita':('Maluma et Gims','Hola Señorita')}
EV={'serge gainsbourg|chanson de prevert':1961,'hubert felix thiefaine|dingues et les paumes':1978}
W={'elad':2.2,'no1':1.6,'evt':1.6,'top10':1.0,'spot':0.8,'ytlist':1.0,'szav':1.8,'kanon':1.2,'szerk':1.35}
D={}
for x in J:
    k=x['k']
    if k in DROP: continue
    k2=MERGE.get(k,k)
    if k=='garou|belle': continue
    d=D.setdefault(k2,{'k':k2,'artist':x['artist'],'title':x['title'],'year':None,'sig':{},'yt':None})
    if k2==k or not d['year']: d['artist'],d['title']=x['artist'],x['title']
    for s,v in x['sig'].items(): d['sig'][s]=max(d['sig'].get(s,0),v)
    if x['year']: d['year']=min(d['year'],x['year']) if d['year'] else x['year']
    if k in P and (not d['yt'] or P[k]['views']>d['yt']['views']): d['yt']=P[k]
for k,(a,t) in NEV.items():
    if k in D: D[k]['artist'],D[k]['title']=a,t
S=list(D.values())
for d in S:
    g=d['sig'];s=sum(W[k]*v for k,v in g.items() if k in W)
    if 'spot' in g: s+=0.8*(g['spot']-1.6)
    y=d['yt']
    if y:
        s+=0.9*max(0,math.log10(max(y['views'],1))-5)   # 1M -> 0.9, 100M -> 2.7
        s+=0.12*min(y['npl'],15)
    s+={3:2.6,2:0.8}.get(g.get('szerk',0),0)
    nsrc=len([k for k in g if k!='szerk'])
    s+=0.3*nsrc
    d['nyers']=round(s,3)
    if not d['year']:
        d['year']=EV.get(d['k']) or (int(y['pub'][:4]) if y else None)
S.sort(key=lambda d:-d['nyers'])
# index 0-100: a nyers pontszám rangsor szerinti, a magyar index eloszlásához hasonló skálája (1. ~ 95, 100. ~ 70, 500. ~ 45, utolsó ~ 15)
N=len(S)
for i,d in enumerate(S):
    r=(i+1)/N
    d['index']=round(15+80*(1-r)**1.6 + 4*min(1,d['nyers']/12),1)
json.dump(S,open(O+'dallista.json','w'),ensure_ascii=False,indent=0)
with open(O+'dallista.tsv','w') as f:
    for i,d in enumerate(S): f.write(f"{i+1}\t{d['index']}\t{d['year']}\t{d['artist']}\t{d['title']}\t{d['yt']['yt'] if d['yt'] else '-'}\t{d['yt']['views']//1000 if d['yt'] else 0}\t{','.join(sorted(d['sig']))}\n")
print(N,'dal;',sum(1 for d in S if d['yt']),'videóval;',sum(1 for d in S if not d['year']),'év nélkül')
