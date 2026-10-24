# python3 fin.py g<N>.py -> a csoport ikonjai JPG-ként az orszag/us/ikon alá, a szkript az orszag/us/ikonrajz alá
import sys,re,shutil
from PIL import Image
g=sys.argv[1];src=open('/tmp/usrajz/'+g).read()
ids=sorted({int(x) for x in re.findall(r'^I\[(\d+)\]=',src,re.M)})
for i in ids: Image.open(f'/tmp/usrajz/png/{i}.png').convert('RGB').resize((256,256),Image.LANCZOS).save(f'/mnt/project-files/ikonok/orszag/us/ikon/{i}.jpg',quality=86)
for f in (g,'us.py','fin.py'): shutil.copy('/tmp/usrajz/'+f,'/mnt/project-files/ikonok/orszag/us/ikonrajz/'+f)
print(len(ids),'ikon kész:',ids[0],'-',ids[-1])
