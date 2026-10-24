# Japán dalok videóinak állapota (a youtube/elerheto.py japán párja): python3 yt_allapot.py [songs.json]
# - yt_nem: nem nyilvános / nem beágyazható / törölt, vagy Japánból tiltott videó (ilyen dal nem kerül a Top 100-ba)
# - date: a videó közzétételi napja a dal évére szorítva -> ebből számol a „Mostanában slágerek” doboz (utolsó 365 nap)
# - hu: Magyarországról lejátszható-e (a regionRestriction alapján)
import json, os, sys, urllib.request, urllib.parse
SJ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'songs.json')
S = json.load(open(SJ, encoding='utf-8'))
ids = sorted({s['yt'] for s in S if s.get('yt')})
st, pub, rr = {}, {}, {}
for i in range(0, len(ids), 50):
    q = urllib.parse.urlencode({'part': 'status,snippet,contentDetails', 'id': ','.join(ids[i:i+50])})
    for it in json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videos?' + q)).get('items', []):
        pub[it['id']] = it['snippet']['publishedAt'][:10]
        s = it['status']; r = it.get('contentDetails', {}).get('regionRestriction', {})
        rr[it['id']] = r
        bad = None if s.get('privacyStatus') == 'public' and s.get('embeddable') else s.get('privacyStatus') + ('' if s.get('embeddable') else ', nem beágyazható')
        if not bad and ('JP' in r.get('blocked', []) or ('allowed' in r and 'JP' not in r['allowed'])): bad = 'Japánból tiltott'
        st[it['id']] = bad
n = 0
for s in S:
    y = s.get('yt')
    if y in st and st[y] is None: s.pop('yt_nem', None)
    else: s['yt_nem'] = 'nincs videó' if not y else st.get(y, 'törölt'); n += 1
    if y in pub and s.get('year'): s['date'] = min(max(pub[y], '%d-01-01' % s['year']), '%d-12-31' % s['year'])
    if y in rr: r = rr[y]; s['hu'] = not ('HU' in r.get('blocked', []) or ('allowed' in r and 'HU' not in r['allowed']))
json.dump(S, open(SJ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(n, 'dal videója nem elérhető;', sum(1 for s in S if s.get('date', '') >= '2025-10-24'), 'dal az utóbbi évből')
