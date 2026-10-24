# Keresésen alapuló elérés a sikerindexhez: régi dalok nézettsége sokszor rajongói feltöltéseken van, nem a hivatalos csatornán.
# Dalonként 1 search (100 egység) + 1 videos.list: az azonos című, az előadót a címben vagy a csatornanévben említő,
# nem élő/remix/feldolgozás találatok nézettségének összege -> eleres_kereses.json {id: {v, n, d}}.
# Sorrend: a kézi top 100, aztán az index szerinti első N dal, ami még nincs meg (vagy 60 napnál régebbi).
# Futtatás: python3 /mnt/project-files/ikonok/eleres_kereses.py [max_kereses]   (kvótahibánál megáll, a kész sorok megmaradnak)
import json, sys, re, datetime, urllib.request, urllib.parse, urllib.error, unicodedata
B = '/mnt/project-files/ikonok/'
OUT = B + 'eleres_kereses.json'
S = [s for s in json.load(open(B + 'songs.json')) if not s.get('hide')]
try: R = json.load(open(OUT))
except Exception: R = {}
MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 80
today = datetime.date.today()
fresh = lambda i: str(i) in R and (today - datetime.date.fromisoformat(R[str(i)]['d'])).days < 60

def n(t):
    t = unicodedata.normalize('NFC', t or '').lower()
    t = re.sub(r'\(.*?\)|\[.*?\]', ' ', t)
    return re.sub(r'\s+', ' ', re.sub(r'[^\w ]', ' ', t)).strip()
ROSSZ = re.compile(r'\b(live|élő|koncert|remix|cover|karaoke|karaoké|instrumental|sped|slowed|feldolgoz|akusztik|acoustic|unplugged|teaser|előzetes|reaction|tutorial|zongora|gitár|guitar|piano)\b', re.I)
api = lambda path, q: json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/' + path + '?' + urllib.parse.urlencode(q)))

kezi = json.load(open(B + 'top100_kezi.json'))
BY = {s['id']: s for s in S}
order = [i for i in kezi if i in BY] + [s['id'] for s in sorted(S, key=lambda s: -(s.get('index') or 0)) if s['id'] not in kezi]
done = 0
for i in order:
    if done >= MAX: break
    if fresh(i): continue
    s = BY[i]
    nt, na = n(s['title']), n(re.split(r'\s+(?:x|feat\.?|ft\.?|&|és)\s+', s['artist'])[0])
    try:
        res = api('search', {'part': 'snippet', 'q': s['artist'] + ' ' + s['title'], 'type': 'video', 'maxResults': 15, 'regionCode': 'HU'})
    except urllib.error.HTTPError as e:
        print('kvóta / hiba:', e.code); break
    done += 1
    ok = []
    for it in res.get('items', []):
        t, ch = it['snippet']['title'], it['snippet']['channelTitle']
        if ROSSZ.search(t): continue
        tt = n(t)
        if not re.search(r'(^| )' + re.escape(nt) + r'( |$)', tt): continue
        rov = ''.join(w[0] for w in na.split()) if len(na.split()) > 1 else '#'  # pl. Locomotiv GT -> lgt
        if not any(a in tt.split() or a in n(ch) for a in (na, rov)) and na not in tt: continue
        ok.append(it['id']['videoId'])
    if s.get('yt') and s['yt'] not in ok: ok.append(s['yt'])
    v = 0
    if ok:
        st = api('videos', {'part': 'statistics', 'id': ','.join(ok)})
        v = sum(int(x['statistics'].get('viewCount', 0)) for x in st.get('items', []))
    R[str(i)] = {'v': v, 'n': len(ok), 'd': today.isoformat()}
    json.dump(R, open(OUT, 'w'))
print(done, 'keresés; összesen', len(R), 'dal')
