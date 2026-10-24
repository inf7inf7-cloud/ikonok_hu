# Sikerindex v3 (Miske, 2026-10-23: „hangold tökéletesre”)
# Elérés: a dal ÖSSZES hivatalos YouTube-feltöltésének nézettsége (a kiválasztott videó + az előadó saját és Topic
# csatornáin talált azonos című feltöltések, élő/remix/feldolgozás nélkül), log-skálán, országos és évtizeden belüli percentilis.
# Szerkesztői jelek: a v1 index (nagy-sláger lista, listavezető, díjak) a top 100-bónusz nélkül, percentilisként.
# Index = 15 + 75 × (0,6 × elérés + 0,4 × szerkesztői). A top 100 is ebből jön (--ir írja a top100_ids.json-t), előadónként max. 3 dal, évtizedenként a katalógus arányában.
# Futtatás: python3 /mnt/project-files/ikonok/index_v3.py [--ir]   (--ir nélkül csak az index_v3.tsv-t írja)
import json, math, re, sys, bisect, collections, unicodedata, urllib.request, urllib.parse, os
B = '/mnt/project-files/ikonok/'
SJ = B + 'songs.json'
S = json.load(open(SJ))
V1 = {x['id']: x['index'] for x in json.load(open(B + 'youtube/v2/songs_elotte_v2.json'))}
TOP = json.load(open(B + 'top100_kezi.json'))  # Miske kézi top 100-a (2026-10-22), rögzítve: szerkesztői jelként számít
EC = json.load(open(B + 'bovito/eloado_csatorna.json'))

def n(t):
    t = unicodedata.normalize('NFC', t or '').lower()
    t = re.sub(r'\(.*?\)|\[.*?\]', ' ', t)
    return re.sub(r'\s+', ' ', re.sub(r'[^\w ]', ' ', t)).strip()

ROSSZ = re.compile(r'\b(live|élő|koncert|remix|cover|karaoke|karaoké|instrumental|sped|slowed|feldolgoz|akusztik|acoustic|unplugged|teaser|előzetes|reaction)\b', re.I)

# friss nézettség minden dal kiválasztott videójára (videos.list, 50/egység)
stat = {}
ids = sorted({s['yt'] for s in S if s.get('yt')})
for i in range(0, len(ids), 50):
    q = urllib.parse.urlencode({'part': 'statistics', 'id': ','.join(ids[i:i + 50])})
    for it in json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videos?' + q)).get('items', []):
        stat[it['id']] = int(it['statistics'].get('viewCount', 0))

cache = {}
def uploads(ch):
    if ch not in cache:
        f = B + 'bovito/cache/%s.json' % ch
        cache[ch] = json.load(open(f)) if os.path.exists(f) else []
    return cache[ch]

def channels(artist):
    out = list(EC.get(artist, []))
    for part in re.split(r'\s+(?:x|feat\.?|ft\.?|&|és|,)\s+', artist):
        out += EC.get(part.strip(), [])
    return set(out)

reach, forras = {}, {}
for s in S:
    nt = n(s['title'])
    seen = {}
    if s.get('yt'): seen[s['yt']] = stat.get(s['yt'], 0)
    if len(nt) >= 3:
        for ch in channels(s['artist']):
            for u in uploads(ch):
                tt = n(u['t'])
                if ROSSZ.search(u['t']) or not re.search(r'(^| )' + re.escape(nt) + r'( |$)', tt): continue
                if len(tt) > len(nt) + 45: continue  # albumösszefoglaló, válogatás
                seen[u['yt']] = max(seen.get(u['yt'], 0), u.get('v') or 0)
    reach[s['id']] = sum(seen.values())
    forras[s['id']] = len(seen)

# keresésen alapuló elérés (eleres_kereses.py, rajongói feltöltésekkel együtt): a nagyobbik számít
try: KER = json.load(open(B + 'eleres_kereses.json'))
except Exception: KER = {}
for s in S:
    if str(s['id']) in KER: reach[s['id']] = max(reach[s['id']], KER[str(s['id'])]['v'])

dec = lambda s: max(1950, min((s['year'] or 2000) // 10 * 10, 2020))
lv = {i: math.log10(v + 1) for i, v in reach.items()}
allv = sorted(lv.values())
bydec = collections.defaultdict(list)
for s in S: bydec[dec(s)].append(lv[s['id']])
for k in bydec: bydec[k].sort()
pct = lambda arr, x: bisect.bisect_right(arr, x) / len(arr)

# szerkesztői jel: v1 a top-bónusz nélkül (top dalnál a bónusz levonva)
TI = {i: k for k, i in enumerate(TOP)}
def ed(s):  # a v1 a kézi top 100-nál 100-on telítődött, ezért ott nem vonható le a bónusz; azokat külön kezeljük
    v = V1.get(s['id'])
    if v is None or s['id'] in TI: return None
    return v
E = {s['id']: ed(s) for s in S}
ev = sorted(v for v in E.values() if v is not None)

out = []
for s in S:
    i = s['id']
    r = 0.5 * pct(allv, lv[i]) + 0.5 * pct(bydec[dec(s)], lv[i])
    if i in TI and str(i) not in KER: r = max(r, 0.8)  # amíg nincs keresési adat, a kézi top 100-at nem ejtjük ki adathiány miatt
    e = 0.95 if i in TI else pct(ev, E[i]) if E[i] is not None else 0.5  # kézi top 100: erős szerkesztői jel
    out.append((s, s.get('index'), round(15 + 75 * (0.6 * r + 0.4 * e), 1), reach[i], forras[i]))

# Top 100 (Miske, 10-23 12:50: „a top 100-at is kalkuláld újra”): a v3 index szerint, csak lejátszható videójú, ikonos dal,
# előadónként legfeljebb 3 (minél több előadó legyen benne)
ok = lambda s: s.get('yt') and not s.get('yt_nem') and not s.get('hide') and os.path.exists(B + 'ikon/%d.jpg' % s['id'])
# évtizedenkénti kvóta a katalógus arányában, hogy a régi klasszikusok ne szoruljanak ki (a nézettség az újaknak kedvez)
ndec = collections.Counter(dec(s) for s in S if ok(s))
quota = {d: round(100 * c / sum(ndec.values())) for d, c in ndec.items()}
cnt, NEWTOP, ind = collections.Counter(), [], collections.Counter()
art = lambda s: re.split(r'\s+(?:x|feat\.?|ft\.?|&|és)\s+', s['artist'])[0].strip().lower()
rank = sorted(out, key=lambda o: -o[2])
for s, o, nw, v, k in rank:
    if ok(s) and cnt[art(s)] < 3 and ind[dec(s)] < quota[dec(s)] and len(NEWTOP) < 100:
        NEWTOP.append(s['id']); cnt[art(s)] += 1; ind[dec(s)] += 1
for s, o, nw, v, k in rank:  # kerekítési maradék
    if len(NEWTOP) < 100 and ok(s) and cnt[art(s)] < 3 and s['id'] not in NEWTOP:
        NEWTOP.append(s['id']); cnt[art(s)] += 1
NV = {s['id']: nw for s, o, nw, v, k in out}
NEWTOP.sort(key=lambda i: -NV[i])

with open(B + 'index_v3.tsv', 'w') as f:
    f.write('id\tyear\tartist\ttitle\tnezes_osszes\tfeltoltes_db\tindex_regi\tindex_v3\ttop\n')
    for s, o, nw, v, k in sorted(out, key=lambda o: -o[2]):
        f.write('\t'.join(map(str, [s['id'], s['year'], s['artist'], s['title'], v, k, o, nw, NEWTOP.index(s['id']) + 1 if s['id'] in NEWTOP else ''])) + '\n')
if '--ir' in sys.argv:
    S2 = json.load(open(SJ))  # frissen olvasva
    nv = {s['id']: nw for s, o, nw, v, k in out}
    for s in S2:
        if s['id'] in nv: s['index'] = nv[s['id']]
        s['top'] = s['id'] in NEWTOP
    json.dump(S2, open(SJ, 'w'), ensure_ascii=False, indent=1)
    json.dump(NEWTOP, open(B + 'top100_ids.json', 'w'))
    print('songs.json és top100_ids.json frissítve')
print(len(out), 'dal; több feltöltésből számolt:', sum(1 for o in out if o[4] > 1), '; top 100-ból a régiben is benne volt:', len(set(NEWTOP) & set(TOP)))
