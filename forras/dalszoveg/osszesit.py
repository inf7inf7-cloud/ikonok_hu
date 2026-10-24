# b*.tsv (id, jel, szöveg) -> osszefoglalo.json. Jel: + biztos/ellenőrzött, ? bizonytalan (csak MIND=1 esetén kerül ki).
import glob,json,os
D=os.path.dirname(os.path.abspath(__file__));MIND=os.environ.get('MIND')=='1'
o={};n={'+':0,'?':0}
for f in sorted(glob.glob(D+'/b*.tsv'))+sorted(glob.glob(D+'/javit*.tsv')):
  for l in open(f,encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)<3 or not p[0].strip().isdigit():continue
    o[int(p[0])]=(p[1].strip(),p[2].strip())
for k,(j,t) in o.items():n[j]=n.get(j,0)+1
out={str(k):t for k,(j,t) in sorted(o.items()) if j=='+' or MIND}
json.dump(out,open(D+'/osszefoglalo.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print('összefoglaló:',len(out),'kint, jelek:',n)
