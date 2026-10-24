# Francia jelöltlista: a kutatas/*.txt források összefésülése -> munka/jeloltek.json
# kulcs: (fő előadó, cím) normalizálva; jelek forrásonként; év: szerkesztői > lista/eladás (legkorábbi) > top10 év
import re,json,unicodedata,math,collections,os
K='/mnt/project-files/ikonok/orszag/fr/kutatas/';O='/mnt/project-files/ikonok/orszag/fr/munka/'
def n(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('œ','oe').replace('&',' et ')
    s=re.sub(r'\(.*?\)','',s);s=re.sub(r"[^a-z0-9]+",' ',s).strip()
    return re.sub(r'^(le|la|les|l) ','',s)
ALIAS={'maitre gims':'gims','gims':'gims','jean jacques goldman':'jean jacques goldman','notre dame de paris':'garou','patrick fiori':'garou','daniel lavoie':'garou',
 'damien sargue':'roméo et juliette','philippe d avilla':'roméo et juliette','star academy 1':'star academy','star academy 2':'star academy','star academy 4':'star academy','star academy 5':'star academy','star academy 3':'star academy',
 'jul':'jul','13 organise':'13 organise','jean philippe audin':'jean philippe audin','doc gyneco':'doc gyneco','arsenik':'arsenik','supreme ntm':'supreme ntm','m':'m'}
def lead(a):
    a=re.split(r'\s+(?:et|feat\.?|ft\.?|featuring|vs\.?|x)\s+|,|&| / ',a)[0].strip()
    a=n(a).replace('arsenik','arsenik');return ALIAS.get(a,a)
def key(a,t): return lead(a)+'|'+n(t)
D={}
def add(src,a,t,y=None,val=None):
    k=key(a,t);d=D.setdefault(k,{'artist':a,'title':t,'years':{},'sig':collections.defaultdict(float)})
    if y: d['years'].setdefault(src,[]).append(int(y))
    if src=='szerk': d['artist'],d['title']=a,t
    elif 'szerk' not in d['years'] and len(a)<len(d['artist']) : pass
    d['sig'][src]=max(d['sig'][src],val) if val is not None else d['sig'][src]+1
def rd(f):
    for l in open(K+f,encoding='utf-8'):
        l=l.strip()
        if not l or l.startswith('#'): continue
        yield [x.strip() for x in l.split('|')]
for y,a,t,s in rd('legtobb_eladott.txt'): add('elad',a,t,y,math.log10(int(s)/100000))
for r,a,t,y in rd('top100_1990s.txt'): add('evt',a,t,y,(101-int(r))/100)
for r,a,t,y in rd('top100_2000s.txt'): add('evt',a,t,y,(101-int(r))/100)
for r,a,t,y in rd('top100_2010.txt'): add('evt',a,t,y,(101-int(r.split('-')[-1]))/100 if '-' not in r else .6)
for y,a,t,w in rd('no1.txt'): add('no1',a,t,y,min(1.5,.4+int(w)/10))
for y,a,t,p in rd('top10.txt'): add('top10',a,t,y,(11-int(p))/10 if int(p) else .3)
for a,t,s in rd('spotify_fr.txt'): add('spot',a,t,None,math.log10(int(s)))
for r,a,t,v,y in rd('yt_legnezettebb.txt'): add('ytlist',a,t,y,1)
for r,a,t in rd('szavazas_riffx2018.txt'): add('szav',a,t,None,(21-int(r))/20+.5)
for r,a,t in rd('kanon_demotivateur.txt'): add('kanon',a,t,None,(51-int(r))/50+.3)
for a,t,y,w in rd('szerkesztoi.txt'): add('szerk',a,t,y,int(w))
out=[]
for k,d in D.items():
    ys=d['years']
    y=min(ys['szerk']) if 'szerk' in ys else min([v for s in ('elad','no1','evt') for v in ys.get(s,[])] or [v for s in ys for v in ys[s]] or [0]) or None
    out.append({'k':k,'artist':d['artist'],'title':d['title'],'year':y,'sig':dict(d['sig'])})
json.dump(out,open(O+'jeloltek.json','w'),ensure_ascii=False,indent=0)
print(len(out),'jelölt;',sum(1 for x in out if not x['year']),'év nélkül;', sum(1 for x in out if list(x['sig'])==['szerk']),'csak szerkesztői')
for x in out:
    if not x['year']: print(' év?',x['artist'],'-',x['title'],x['sig'])
