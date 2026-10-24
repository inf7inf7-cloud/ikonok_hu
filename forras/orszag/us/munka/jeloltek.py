# USA jelöltlista: Billboard év végi listák (kutatas/ye) + kánon (kutatas/kanon.txt) -> munka/jeloltek.json
# Csak amerikai fő előadó (munka/nem_usa.txt kizárva). Kulcs: normalizált fő előadó|cím.
import re,json,unicodedata,collections
B='/mnt/project-files/ikonok/orszag/us/'
def n(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('&',' and ');s=re.sub(r'\(.*?\)','',s);s=re.sub(r"['’]",'',s);s=re.sub(r'[^a-z0-9]+',' ',s).strip()
    return re.sub(r'^the ','',s)
def lead(a): return re.split(r'\s+(?:featuring|feat\.|ft\.|with)\s+',a,flags=re.I)[0].strip()
ALIAS={'little stevie wonder':'stevie wonder','john cougar':'john mellencamp','prince and revolution':'prince','prince and new power generation':'prince',
 'bob seger and silver bullet band':'bob seger','bob seger system':'bob seger','b j thomas and triumphs':'b j thomas','raiders':'paul revere and raiders',
 'junior walker and all stars':'jr walker and all stars','sly and family stone':'sly and family stone','black eyed peas':'black eyed peas','outkast':'outkast',
 'smokey robinson and miracles':'miracles','hall and oates':'daryl hall and john oates','dave baby cortez':'dave cortez','rick nelson':'ricky nelson',
 'p diddy':'puff daddy','janet':'janet jackson','pussycat dolls':'pussycat dolls','lil jon and east side boyz':'lil jon','snoop doggy dogg':'snoop dogg',
 'gloria estefan and miami sound machine':'gloria estefan','miami sound machine':'gloria estefan','kenny rogers and first edition':'kenny rogers','jon bon jovi':'bon jovi'}
def la(a):
    x=n(lead(a));return ALIAS.get(x,x)
NEM={n(l.strip()) for l in open(B+'munka/nem_usa.txt',encoding='utf-8') if l.strip() and not l.startswith('#')}
D={}
def add(y,t,a,src,pt):
    if n(lead(a)) in NEM: return
    k=la(a)+'|'+n(t)
    d=D.setdefault(k,{'k':k,'title':t,'artist':a,'year':y,'jel':[],'pont':0})
    d['year']=min(d['year'],y);d['jel'].append(src);d['pont']+=pt
for x in json.load(open(B+'munka/ye_mind.json')):
    pt=(101-x['r']) if x['y']>=1958 else (51-x['r'])*2
    add(x['y'],x['t'],x['a'],'ye%d#%d'%(x['y'],x['r']),pt)
TP={'no1':40,'rs':45,'riaa':30,'gr':35,'radio':30,'xmas':40,'ye57':45,'kanon':25}
for l in open(B+'kutatas/kanon.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    y,t,a,j=l.rstrip('\n').split('|')
    for s in j.split(','): add(int(y),t,a,s,TP[s])
J=sorted(D.values(),key=lambda d:-d['pont'])
json.dump(J,open(B+'munka/jeloltek.json','w'),ensure_ascii=False,indent=0)
c=collections.Counter(d['year']//10*10 for d in J)
print(len(J),'jelölt;',dict(sorted(c.items())))
