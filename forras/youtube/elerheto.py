# Minden dal yt-videójának elérhetősége (videos.list, 1 egység / 50 videó) -> songs.json 'yt_nem' mező
# (nem nyilvános / nem beágyazható / törölt videó). A build_nyito.py ezeket nem engedi a top 100-ba.
# Közben 'date' mező: a videó közzétételi napja a dal évére szorítva -> ebből számol az 'Aktuális slágerek' doboz (utolsó 365 nap).
# Futtatás: python3 /mnt/project-files/ikonok/youtube/elerheto.py
import json, urllib.request, urllib.parse
SJ = '/mnt/project-files/ikonok/songs.json'
S = json.load(open(SJ))
ids = sorted({s['yt'] for s in S if s.get('yt')})
st = {}
pub = {}
for i in range(0, len(ids), 50):
    q = urllib.parse.urlencode({'part': 'status,snippet', 'id': ','.join(ids[i:i+50])})
    for it in json.load(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videos?' + q)).get('items', []):
        pub[it['id']] = it['snippet']['publishedAt'][:10]
        s = it['status']
        st[it['id']] = None if s.get('privacyStatus') == 'public' and s.get('embeddable') else s.get('privacyStatus') + ('' if s.get('embeddable') else ', nem beágyazható')
S = json.load(open(SJ))  # frissen olvasva
n = 0
for s in S:
    y = s.get('yt')
    ok = y and y in st and st[y] is None
    if ok: s.pop('yt_nem', None)
    if y in pub and s.get('year'): s['date'] = min(max(pub[y], '%d-01-01' % s['year']), '%d-12-31' % s['year'])
    else: s['yt_nem'] = 'nincs videó' if not y else st.get(y, 'törölt'); n += 1
json.dump(S, open(SJ, 'w'), ensure_ascii=False, indent=1)
print(n, 'dal videója nem elérhető')
for s in S:
    if s.get('yt_nem') and s.get('top'): print('TOP:', s['id'], s['artist'], s['title'], s['yt_nem'])
