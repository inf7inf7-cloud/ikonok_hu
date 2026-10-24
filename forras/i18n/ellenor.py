# Fordításfájlok ellenőrzése: sorszám és {n} helyőrzők egyezése a kulcsok.txt-vel.
import re, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
K = [l.rstrip('\n') for l in open('kulcsok.txt', encoding='utf-8') if not l.startswith('#')]
ok = True
for f in sorted(glob.glob('*.txt')):
    if f == 'kulcsok.txt':
        continue
    T = open(f, encoding='utf-8').read().rstrip('\n').split('\n')
    if len(T) != len(K):
        print(f, 'SOROK:', len(T), '!=', len(K)); ok = False
    for i, (k, t) in enumerate(zip(K, T)):
        if sorted(re.findall(r'\{\d\}', k)) != sorted(re.findall(r'\{\d\}', t)) or not t.strip():
            print(f, i, k, '|', t); ok = False
print('OK' if ok else 'HIBA', len(glob.glob('*.txt')) - 1, 'nyelv')
