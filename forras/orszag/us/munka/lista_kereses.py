# YouTube lejátszási listák keresése (search.list type=playlist, 100 egység/keresés) -> nyers/playlists.json
import json,sys,urllib.request,urllib.parse,os
N='/mnt/project-files/ikonok/orszag/us/nyers/'
api=lambda ep,**p: json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/'+ep+'?'+urllib.parse.urlencode(p)))
F=N+'playlists.json';P=json.load(open(F)) if os.path.exists(F) else {}
for q in sys.argv[1:]:
    if q in P: continue
    d=api('search',part='snippet',type='playlist',maxResults=50,q=q,regionCode='US')
    P[q]=[[it['id']['playlistId'],it['snippet']['title'],it['snippet']['channelTitle']] for it in d['items']]
    print(q,len(P[q]),flush=True)
json.dump(P,open(F,'w'),ensure_ascii=False,indent=0)
