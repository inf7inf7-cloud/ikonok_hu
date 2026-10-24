# a lezárt francia lista -> forras/orszag/fr/ (songs.json, top100_ids.json, ikon/); videóállapot a már letöltött videóadatokból (API-hívás nélkül)
import json,os,shutil,re
O='/mnt/project-files/ikonok/orszag/fr/';R='/home/user/ikonok_hu/forras/orszag/fr/'
L=json.load(open(O+'munka/dallista.json'));I=json.load(open(O+'munka/idk.json'))
M=json.load(open(O+'nyers/videok.json'))
K=json.load(open(O+'nyers/kereses.json'))
for d in K.values(): M.update(d)
nx=max(I.values())+1
for x in L:
    if x['k'] not in I: I[x['k']]=nx;nx+=1
json.dump(I,open(O+'munka/idk.json','w'),ensure_ascii=False,indent=0)
S=[]
for x in L:
    y=(x.get('yt') or {}).get('yt');m=M.get(y,{}) if y else {};r=m.get('rr') or {}
    s={'id':I[x['k']],'year':x['year'],'artist':x['artist'],'title':x['title'],'src':'orig','flags':[],'yt':y or '','top':False,'index':round(x['index'],1)}
    bad=None
    if not y: bad='nincs videó'
    elif m.get('priv')!='public' or m.get('emb') is False: bad='nem nyilvános / nem beágyazható'
    elif 'FR' in r.get('blocked',[]) or ('allowed' in r and 'FR' not in r['allowed']): bad='Franciaországból tiltott'
    if bad: s['yt_nem']=bad
    if y and m.get('pub') and x['year']: s['date']=min(max(m['pub'],'%d-01-01'%x['year']),'%d-12-31'%x['year'])
    if y and m: s['hu']=not ('HU' in r.get('blocked',[]) or ('allowed' in r and 'HU' not in r['allowed']))
    S.append(s)
S.sort(key=lambda s:s['id'])
json.dump(S,open(R+'songs.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(list(range(1,101)),open(R+'top100_ids.json','w'))
os.makedirs(R+'ikon',exist_ok=True)
for f in os.listdir(O+'ikon'): shutil.copy(O+'ikon/'+f,R+'ikon/'+f)
print(len(S),'dal;',sum(1 for s in S if s.get('yt_nem')),'videó nélkül;',len(os.listdir(R+'ikon')),'ikon;','top100 hibás:',[s['id'] for s in S if s['id']<=100 and s.get('yt_nem')])
