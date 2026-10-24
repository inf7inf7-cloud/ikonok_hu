# kutatas/ye/*.txt -> munka/ye_mind.json (év, helyezés, cím, előadó, fő előadó)
import json,re,glob,os
B='/mnt/project-files/ikonok/orszag/us/'
def lead(a):
    a=re.split(r'\s+(?:featuring|feat\.|ft\.|with)\s+',a,flags=re.I)[0]
    return a.strip()
R=[]
for f in sorted(glob.glob(B+'kutatas/ye/*.txt')):
    y=int(os.path.basename(f)[:4])
    for l in open(f,encoding='utf-8'):
        p=l.rstrip('\n').split('|')
        if len(p)<3 or not p[2].strip(): continue
        R.append({'y':y,'r':int(p[0]),'t':p[1].strip(),'a':p[2].strip(),'lead':lead(p[2])})
json.dump(R,open(B+'munka/ye_mind.json','w'),ensure_ascii=False,indent=0)
L=sorted({x['lead'] for x in R})
open(B+'munka/eloadok.txt','w').write('\n'.join(L))
print(len(R),'sor',len(L),'előadó')
