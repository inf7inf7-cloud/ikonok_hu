# IKONOK – napi automata frissítés (Miske, 2026-10-23: „automatizáld magad teljesen”)

Miske kérése: javíts mindent, amit jónak látsz, kérdezés nélkül. Kivétel: amit Miske korábban kifejezetten eldöntött (lásd memória: ikonok-alapok, ikonok-finomitas); azt ne írd felül.
Minden futás előtt: `songs.json` mentése `bovito/songs_auto_<dátum>.json` néven. Az ikonok.hu a GitHub main ágából magától települ, ezért a push élesít (2026-10-23 óta).

## Naponta (sorrendben)
0. **Sikerindex-adat:** `python3 eleres_kereses.py 60` (/tmp-ből): keresésen alapuló elérés (rajongói feltöltésekkel), először a kézi top 100 (top100_kezi.json), aztán index szerint. Az index_v3.py (a dist.py futtatja) ebből és a hivatalos feltöltésekből számolja az indexet ÉS a top 100-at (top100_ids.json; előadónként max. 3, évtizedenként a katalógus arányában).
1. **Videók + dátumok:** `python3 youtube/elerheto.py` (a dist.py is futtatja). Elérhetetlen videó: csere a bovito/cache vagy videos/playlistItems alapján (ytpotlas.py), ha nincs nyilvános videó, a dal kivétele (torolt.json). Keresés (search) 100 egység, napi max. ~40.
2. **Évszámok:** a `flags`-ben „ellenőrizendő” évű dalok közül max. 40: `bovito/evcsekk.py` (Topic ℗ / Released on), javítás a songs.json-ban.
3. **Ikonfinomítás dalszöveg alapján:** először az ikonrajz/munka/kor2_ids.txt még nem feldolgozott id-jei (az első 60 a fin_k2a/k2b-ben kész vagy folyamatban), és a fin_k2*.tsv „3. kör” sorai, aztán a többi dal sikerindex szerint. Napi adag ~60 dal, 2 rajzoló ügynök, óránként max. ~80 WebFetch (zeneszoveg.hu). Kimenet: munka/fin_auto_<dátum>.tsv, összevető lap, régi ikonok munka/regi/. Csak ott rajzolj újat, ahol a dalszöveg alapján a régi félrevezető vagy semmitmondó.
4. **Adathibák:** a rajzolók által jelzett előadó/cím hibák javítása a hivatalos YouTube-videó címe alapján (videos.list, 1 egység).
5. **Építés és közzététel:** `python3 dist.py` (a dist/ mappa 10-23 óta /tmp/ikonok-dist, a zip továbbra is ide kerül; az artifact.html és ikonpack/ itt marad) (ha nyito_* változott, előbb `mk_nyito.py`), majd artifact.html + ikonpack/*.json másolása a scratchpad/pub alá (ha nincs, hozd létre), publish https://claude.ai/artifact/RHTgxQbAa52VCeEbtoymK3 (root=pub, files ikonpack/p1..pN.json).
5b. **Élesítés (ikonok.hu):** a GitHub-repóba (inf7inf7-cloud/ikonok_hu, main) push. Ha nincs /home/user/ikonok_hu: add_repo, majd `git clone --depth 1`. Utána `rm -rf oldal && cp -r /tmp/ikonok-dist oldal`, a módosított forrásfájlok a forras/ alá, commit, `git push -u origin main`. A Cloudflare 1-2 perc alatt kiteszi. A zip csak tartalék.
5c. **„Mostanában slágerek” doboz:** minden futáskor ellenőrizd, hogy pontosan az utóbbi 12 hónap (gördülő, date mező) dalait mutatja; ha nem, javítsd még a push előtt.
6. **Jelentés Miskének** a Finomító szálban, röviden: mi változott, csatolva a zip és az összevető PDF. Ha semmi érdemi nem változott, ne írj.

## Hetente (hétfőn) még
7. **Slágerbővítő kör:** bovito/CIKLUS.md lépései (csatornak → gyujt → jelolt → kor.py N). Automatikus felvétel szigorúbb küszöbbel: meglévő előadótól a nálunk lévő dalai mediánjánál többet nézett dal (min. 500 ezer), új magyar előadótól 5 millió fölött; előadónként max. 3, körönként max. 40. `felvesz.py`-hoz a pipák helyett a kor listájából generált export. Ikont minden új dal kap. A jelentésben a felvett dalok listája; amit Miske kivetet, az kizart.json-ba.
8. **Friss slágerek:** YouTube HU zenei toplista (videos chart=mostPopular, regionCode=HU, videoCategoryId=10): a magyar előadók nálunk hiányzó dalai ugyanígy felvételre kerülnek, hogy a „Mostanában slágerek” doboz friss maradjon.

## Állandó szabályok
- „Mostanában slágerek” doboz: az utóbbi 365 nap dalai (date mező), cím nem változik.
- Top 100-ban csak lejátszható videójú, ikonnal rendelkező dal.
- Lejátszó: csak előadó és cím; mobilon egy sorban a vezérlők.
- Csak magyar előadók.

## Nyitott adatellenőrzések
(2026-10-24: a 10-23-i lista javítva: 4515, 4458, 4456, 4461, 4500 előadó a hivatalos videó szerint; a többi rendben.)
