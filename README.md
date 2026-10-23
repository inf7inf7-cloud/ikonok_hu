# IKONOK.HU

- `oldal/` – a kész weboldal, ugyanaz, ami az `ikonok-weboldal.zip`-ben van; ennek a tartalma kerül az ikonok.hu tárhelyére.
- `forras/` – amiből az oldal készül: kinézet és működés (`nyito_*`), dallista (`songs.json`), top 100 (`top100_*.json`), dalikonok (`ikon/`), logó, valamint az összerakó szkriptek.

Összerakás a `forras/` mappában: `python3 mk_nyito.py && python3 build_nyito.py && python3 dist.py`.
