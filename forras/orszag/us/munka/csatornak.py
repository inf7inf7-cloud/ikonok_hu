# Előadói csatornák handle alapján (channels.list forHandle, 1 egység), uploads lapozása (playlistItems, 1 egység/50) addig,
# amíg az előadó minden jelölt dala meg nem lesz. python3 csatornak.py <jelöltek száma> <max oldal/csatorna> <egységkeret>
# -> nyers/csatornak.json {előadó:[[chid,cím],...]}, nyers/uploads.json {chid:[[vid,cím],...]}, munka/yt_par.json {kulcs:vid}
import json,sys,os,re,urllib.request,urllib.parse,unicodedata
B='/mnt/project-files/ikonok/orszag/us/';N=B+'nyers/'
used=0
def api(ep,**p):
    global used;used+=1
    try: return json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/'+ep+'?'+urllib.parse.urlencode(p)))
    except urllib.error.HTTPError as e:
        if e.code in (403,429): print('KERET',e.read()[:300]);save();sys.exit(1)
        return {}
def n(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('&',' and ');s=re.sub(r"['’]",'',s);return re.sub(r'[^a-z0-9]+',' ',s).strip()
def nt(t): return n(re.sub(r'\(.*?\)','',t)) or n(t)
BAD=re.compile(r'\b(live|karaoke|cover|remix|instrumental|reaction|lyric breakdown|behind the|making of|interview|teaser|trailer|8d|slowed|sped up|commentary|tutorial|lesson|medley|rehearsal|acoustic)\b',re.I)
GROUPS=r"^(Simon & Garfunkel|Earth, Wind & Fire|Daryl Hall & John Oates|Hall & Oates|Sam & Dave|Peter, Paul and Mary|Crosby, Stills, Nash & Young|Blood, Sweat & Tears|Sonny & Cher|Captain & Tennille|Peaches & Herb|Kool & the Gang|Booker T\. & the M\.G\.'s|Ike & Tina Turner|Martha and the Vandellas|Sly and the Family Stone|Sly & the Family Stone|Tommy James and the Shondells|Dion and the Belmonts|Gladys Knight & the Pips|Huey Lewis and the News|Lisa Lisa and Cult Jam|Marvin Gaye & Tammi Terrell|Hootie & the Blowfish|Macklemore & Ryan Lewis|Dan \+ Shay|Florida Georgia Line|Silk Sonic|KC and the Sunshine Band|Joan Jett & The Blackhearts|Tony Orlando and Dawn|Bruce Hornsby and the Range|Gary Puckett & The Union Gap|Paul Revere & the Raiders|Gary Lewis & the Playboys|Sam the Sham and the Pharaohs|Little Anthony and the Imperials|Archie Bell & the Drells|Mitch Ryder & The Detroit Wheels|Bob Seger & The Silver Bullet Band|Prince & the Revolution|Prince and The Revolution|Prince and The New Power Generation|Frankie Lymon and the Teenagers|Danny & the Juniors|Bill Haley & His Comets|Jay and the Americans|Ruby & the Romantics|Smokey Robinson and the Miracles|Mary J\. Blige|Jr\. Walker & The All Stars|Junior Walker & the All Stars)"
def lead(a):
    m=re.match(GROUPS,a)
    if m: return m.group(1)
    return re.split(r'\s+(?:featuring|feat\.|ft\.|with|and|&|x)\s+|,\s*',a)[0].strip()
J=json.load(open(B+'munka/jeloltek.json'))[:int(sys.argv[1])];MAXP=int(sys.argv[2]);KERET=int(sys.argv[3])
FC=N+'csatornak.json';C=json.load(open(FC)) if os.path.exists(FC) else {}
FU=N+'uploads.json';U=json.load(open(FU)) if os.path.exists(FU) else {}
FP=B+'munka/yt_par.json';P=json.load(open(FP)) if os.path.exists(FP) else {}
def save():
    json.dump(C,open(FC,'w'),ensure_ascii=False);json.dump(U,open(FU,'w'),ensure_ascii=False);json.dump(P,open(FP,'w'),ensure_ascii=False,indent=0)
def match(songs,items,cn):
    for x in songs:
        if x['k'] in P: continue
        t=nt(x['title']);best=None
        for vid,vt in items:
            v=n(vt)
            if not re.search(r'(^| )'+re.escape(t)+r'( |$)',v): continue
            if BAD.search(vt) and not BAD.search(x['title']): continue
            sc=(('official' in v) + ('video' in v), -len(v))
            if not best or sc>best[0]: best=(sc,vid)
        if best: P[x['k']]=best[1]
by={}
for x in J: by.setdefault(lead(x['artist']),[]).append(x)
print(len(by),'előadó',flush=True)
for i,(a,songs) in enumerate(by.items()):
    if used>KERET: print('egységkeret elérve');break
    if all(x['k'] in P for x in songs): continue
    if a not in C:
        base=re.sub(r'[^A-Za-z0-9]','',unicodedata.normalize('NFKD',a).encode('ascii','ignore').decode());b2=re.sub(r'^The','',base)
        C[a]=[]
        for h in dict.fromkeys([base,b2,base+'VEVO',b2+'VEVO']):
            d=api('channels',part='snippet',forHandle='@'+h)
            for it in d.get('items',[]):
                t=it['snippet']['title']
                if (n(a).replace(' ','') in n(t).replace(' ','') or n(t).replace(' ','') in n(a).replace(' ','') or n(re.sub(r'^The ','',a)).replace(' ','') in n(t).replace(' ','')) and [it['id'],t] not in C[a]: C[a].append([it['id'],t])
            if len(C[a])>=2: break
    for chid,cn in C[a]:
        if all(x['k'] in P for x in songs): break
        L=U.get(chid)
        if L is None:
            L=[];tok=''
            for _ in range(MAXP):
                d=api('playlistItems',part='snippet',maxResults=50,playlistId='UU'+chid[2:],pageToken=tok)
                L+=[[y['snippet']['resourceId']['videoId'],y['snippet']['title']] for y in d.get('items',[])]
                match(songs,L,cn)
                tok=d.get('nextPageToken')
                if not tok or all(x['k'] in P for x in songs): break
            U[chid]=L
        match(songs,L,cn)
    if i%25==24: save();print(i+1,'előadó',used,'egység',len(P),'párosítva',flush=True)
save();print('kész',used,'egység;',len(P),'/',len(J),'párosítva')
