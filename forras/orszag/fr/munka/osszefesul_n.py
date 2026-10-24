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
