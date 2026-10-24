# python3 jpg.py id1 id2 ... -> ../ikon/<id>.jpg 256px
import sys
from PIL import Image
for i in sys.argv[1:]:
    Image.open(f'png/{i}.png').convert('RGB').resize((256,256),Image.LANCZOS).save(f'/mnt/project-files/ikonok/orszag/fr/ikon/{i}.jpg',quality=86)
