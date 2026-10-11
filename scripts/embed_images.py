from pathlib import Path
import base64
ROOT=Path(__file__).resolve().parents[1]
assets=ROOT/'assets'

def data_uri(path):
    return 'data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode()

def replace_all(old,new):
    for p in assets.glob('*.svg'):
        s=p.read_text()
        s=s.replace(old,new)
        p.write_text(s)

# Exact supplied assets are embedded only after you place them here.
# id.png updates portrait slots; right_pointing.png updates the Connect portrait slot.
idp=ROOT/'id.png'
rp=ROOT/'right_pointing.png'
if not idp.exists() or not rp.exists():
    missing=[]
    if not idp.exists(): missing.append('id.png')
    if not rp.exists(): missing.append('right_pointing.png')
    raise SystemExit('Missing: '+', '.join(missing))
uid=data_uri(idp); urp=data_uri(rp)
for name in ['hero.svg','id-dashboard.svg']:
    p=assets/name; s=p.read_text(); s=s.replace('data:image/png;base64,PLACEHOLDER_ID',uid)
# replace existing placeholder data in hero/id with id image, and connect with right image
placeholder='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
for name in ['hero.svg','id-dashboard.svg']:
    p=assets/name; p.write_text(p.read_text().replace(placeholder,uid))
p=assets/'connect.svg'; p.write_text(p.read_text().replace(placeholder,urp))
print('Embedded id.png into hero.svg + id-dashboard.svg; right_pointing.png into connect.svg')
