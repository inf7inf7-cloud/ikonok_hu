# USA songs.json + top100_ids.json a jelöltekből (munka/jeloltek.json), a videópárosításból (munka/yt_par.json) és a videóadatokból (nyers/videoadat.json, ha van)
# sikerindex (0-100): lista- és kánonpont (Billboard év vége, listavezető, RS500, RIAA, Grammy) 70%, YouTube-nézettség (log) 30%
import json,math,os,re
B='/mnt/project-files/ikonok/orszag/us/'
J=json.load(open(B+'munka/jeloltek.json'));P=json.load(open(B+'munka/yt_par.json'));ID=json.load(open(B+'munka/dalid.json'))
V=json.load(open(B+'nyers/videoadat.json')) if os.path.exists(B+'nyers/videoadat.json') else {}
KI=json.load(open(B+'munka/kizart.json')) if os.path.exists(B+'munka/kizart.json') else {}
mp=max(d['pont'] for d in J);mv=max([v.get('views',0) for v in V.values()]+[1])
S=[]
for d in J:
    k=d['k'];yt=P.get(k)
    if not yt or k in KI: continue
    v=V.get(yt,{})
    if v and (v.get('ok') is False): continue
    pi=math.sqrt(d['pont']/mp);vi=math.log10(1+v.get('views',0))/math.log10(1+mv) if v else pi
    idx=round(100*(.7*pi+.3*vi),1)
    S.append({'id':ID[k],'year':d['year'],'artist':d['artist'],'title':d['title'],'src':'orig','flags':[],'yt':yt,'top':False,'index':idx,
              'views':v.get('views',0),'no1':[],'jel':d['jel'],'date':f"{d['year']}-12-31"})
S.sort(key=lambda x:-x['index'])
json.dump(S,open(B+'songs.json','w'),ensure_ascii=False,indent=0)
ik={int(f[:-4]) for f in os.listdir(B+'ikon') if f.endswith('.jpg')}
top=[x['id'] for x in S if x['id'] in ik][:100]
json.dump(top,open(B+'top100_ids.json','w'))
print(len(S),'dal videóval;',sum(1 for x in S if x['id'] in ik),'ikonnal')
