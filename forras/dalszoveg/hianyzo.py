# Azok a dalok, amelyeknek még nincs ellenőrzött („+”) összefoglalója, sikerindex szerint. Használat: python3 dalszoveg/hianyzo.py [N]
import json,os,sys
D=os.path.dirname(os.path.abspath(__file__));N=int(sys.argv[1]) if len(sys.argv)>1 else 60
S=[x for x in json.load(open(D+'/../songs.json',encoding='utf-8')) if not x.get('hide')]
O=json.load(open(D+'/osszefoglalo.json',encoding='utf-8'))
h=[x for x in sorted(S,key=lambda x:-(x.get('index') or 0)) if str(x['id']) not in O]
print('hiányzik:',len(h),'/',len(S),file=sys.stderr)
for x in h[:N]:print(x['id'],x['year'],x['artist'],'–',x['title'],sep='\t')
