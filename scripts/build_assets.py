import base64, os, html, textwrap, zlib, struct
ROOT='/mnt/data/github_readme_build'
A=os.path.join(ROOT,'assets')

def b64(path): return base64.b64encode(open(path,'rb').read()).decode()
FONT_DISPLAY=b64(os.path.join(ROOT,'fonts','Cabin-Bold.woff2'))
FONT_MONO=b64(os.path.join(ROOT,'fonts','DejaVuSansMono.woff2'))
# 1x1 transparent PNG placeholder. User can replace via scripts/embed_images.py.
PLACEHOLDER='iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
CSS=f'''<style>
@font-face{{font-family:CabinX;src:url(data:font/woff2;base64,{FONT_DISPLAY}) format('woff2');font-weight:700}}
@font-face{{font-family:MonoX;src:url(data:font/woff2;base64,{FONT_MONO}) format('woff2');font-weight:400}}
:root{{--navy:#070b16;--blue:#247bff;--red:#ff354f;--white:#f5f7fb;--muted:#9da8bd;--line:#26324b}}
*{{font-family:CabinX,Arial,sans-serif}} .mono{{font-family:MonoX,monospace}} .small{{font-family:MonoX,monospace;font-size:14px;letter-spacing:1px}} .title{{font-size:56px;font-weight:700}} .h2{{font-size:28px;font-weight:700}} .body{{font-size:18px}} .muted{{fill:#9da8bd}} .white{{fill:#f5f7fb}} .blue{{fill:#247bff}} .red{{fill:#ff354f}}
@media (prefers-reduced-motion: reduce){{.motion,.motion *{{animation:none!important;transition:none!important}}}}
</style>'''

def bg(w,h,uid):
    return f'''<defs><pattern id="{uid}-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#ffffff" opacity=".08"/></pattern><linearGradient id="{uid}-g" x1="0" x2="1"><stop stop-color="#247bff"/><stop offset="1" stop-color="#ff354f"/></linearGradient></defs><rect width="{w}" height="{h}" rx="28" fill="#070b16"/><rect width="{w}" height="{h}" rx="28" fill="url(#{uid}-dots)"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="28" fill="none" stroke="url(#{uid}-g)" stroke-opacity=".45"/>'''

def image_data(x,y,w,h,clip=None):
    cl=f' clip-path="url(#{clip})"' if clip else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#10182a" stroke="#33405d"/><image x="{x+4}" y="{y+4}" width="{w-8}" height="{h-8}" preserveAspectRatio="xMidYMid slice" href="data:image/png;base64,{PLACEHOLDER}"{cl}/>'

# HERO
hero=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="t d">
<title id="t">Khan Ajizur Rehman — Software Developer</title><desc id="d">Animated developer profile hero for Khan Ajizur Rehman.</desc>{CSS}{bg(900,520,'hero')}
<g class="motion">
<text x="56" y="72" class="small" fill="#247bff">HELLO, I'M</text>
<text x="56" y="140" class="title white">KHAN AJIZUR</text><text x="56" y="198" class="title white">REHMAN</text>
<rect x="54" y="214" width="420" height="5" rx="3" fill="#247bff"><animate attributeName="width" from="0" to="420" dur=".8s" begin="0s" fill="freeze"/></rect>
<g transform="translate(56 258)">
<rect width="470" height="54" rx="27" fill="#10182a" stroke="#26324b"/>
<text x="24" y="35" class="body white">I build secure, useful digital experiences.</text>
</g>
<g transform="translate(56 332)">
<text class="small muted" y="0">FOCUS</text>
<g transform="translate(0 22)">
<text class="h2 white" y="0" opacity="1">FULL STACK DEVELOPER<animate attributeName="opacity" dur="10s" repeatCount="indefinite" values="1;1;0;0;0;0;0;0;0;1" keyTimes="0;.19;.20;.44;.45;.69;.70;.94;.95;1"/></text>
<text class="h2 white" y="0" opacity="0">SOC ANALYST<animate attributeName="opacity" dur="10s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0;0;0" keyTimes="0;.19;.20;.44;.45;.69;.70;.94;.95;1"/></text>
<text class="h2 white" y="0" opacity="0">DATA ANALYST<animate attributeName="opacity" dur="10s" repeatCount="indefinite" values="0;0;0;0;1;1;0;0;0;0" keyTimes="0;.19;.20;.44;.45;.69;.70;.94;.95;1"/></text>
<text class="h2 white" y="0" opacity="0">CYBER TECH<animate attributeName="opacity" dur="10s" repeatCount="indefinite" values="0;0;0;0;0;0;1;1;0;0" keyTimes="0;.19;.20;.44;.45;.69;.70;.94;.95;1"/></text>
</g></g>
{image_data(650,54,190,250)}
<text x="650" y="332" class="small blue">SOFTWARE DEVELOPER</text><text x="650" y="360" class="body white">Mumbai, India</text>
<circle cx="650" cy="389" r="5" fill="#ff354f"/><text x="666" y="395" class="small muted">BSc-IT · 8.6 CGPA</text>
<text x="56" y="474" class="small muted">PYTHON · JAVASCRIPT · REACTJS · MYSQL · LINUX</text>
</g></svg>'''
open(A+'/hero.svg','w').write(hero)

# ABOUT-LIFE
about=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="t d"><title id="t">About and interests</title><desc id="d">Capabilities and a three-slide interests carousel.</desc>{CSS}{bg(900,520,'about')}
<g class="motion"><text x="52" y="66" class="small blue">ABOUT / LIFE</text><text x="52" y="112" class="h2 white">BUILD WITH PURPOSE.</text>
<g transform="translate(52 150)"><rect width="300" height="260" rx="22" fill="#0d1424" stroke="#26324b"/><text x="22" y="42" class="small muted">CAPABILITIES</text>
<text x="22" y="82" class="body white">• Front-end interfaces</text><text x="22" y="118" class="body white">• Python development</text><text x="22" y="154" class="body white">• Security-minded UX</text><text x="22" y="190" class="body white">• Data analysis</text><text x="22" y="226" class="body white">• Linux workflows</text></g>
<g transform="translate(382 150)"><rect width="466" height="260" rx="22" fill="#0d1424" stroke="#26324b"/>
<g opacity="1"><text x="28" y="42" class="small blue">01 / CYBERSECURITY</text><text x="28" y="92" class="h2 white">SECURE BY DEFAULT.</text><text x="28" y="132" class="body muted">Exploring defensive thinking, SOC workflows</text><text x="28" y="158" class="body muted">and practical security tooling.</text><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="1;1;0;0;0;0;1" keyTimes="0;.32;.34;.65;.67;.98;1"/></g>
<g opacity="0"><text x="28" y="42" class="small blue">02 / WEB DEVELOPMENT</text><text x="28" y="92" class="h2 white">MAKE IT USEFUL.</text><text x="28" y="132" class="body muted">Designing interfaces that feel simple, fast</text><text x="28" y="158" class="body muted">and clear across real workflows.</text><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;0" keyTimes="0;.32;.34;.65;.67;.98;1"/></g>
<g opacity="0"><text x="28" y="42" class="small blue">03 / DATA</text><text x="28" y="92" class="h2 white">TURN DATA INTO SIGNAL.</text><text x="28" y="132" class="body muted">Learning to turn messy information into</text><text x="28" y="158" class="body muted">clear analysis and useful decisions.</text><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;0;0;1;1;0" keyTimes="0;.32;.34;.65;.67;.98;1"/></g>
<g transform="translate(28 214)"><rect width="126" height="4" rx="2" fill="#26324b"/><rect width="126" height="4" rx="2" fill="#247bff"><animate attributeName="width" dur="4s" repeatCount="indefinite" values="0;126;0" keyTimes="0;.98;1"/></rect><rect x="142" width="126" height="4" rx="2" fill="#26324b"/><rect x="284" width="126" height="4" rx="2" fill="#26324b"/></g></g></g></svg>'''
open(A+'/about-life.svg','w').write(about)

# STACK
stack=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="t d"><title id="t">Technology stack</title><desc id="d">Three tilted tech orbits and grouped stack chips.</desc>{CSS}{bg(900,520,'stack')}
<g class="motion"><text x="52" y="66" class="small blue">STACK / TOOLKIT</text><text x="52" y="112" class="h2 white">TOOLS I LIKE TO SHIP WITH.</text>
<g transform="translate(290 278)"><ellipse rx="230" ry="82" fill="none" stroke="#247bff" stroke-opacity=".35" stroke-width="2" transform="rotate(-18)"/><ellipse rx="230" ry="82" fill="none" stroke="#ff354f" stroke-opacity=".28" stroke-width="2" transform="rotate(34)"/><ellipse rx="230" ry="82" fill="none" stroke="#f5f7fb" stroke-opacity=".13" stroke-width="2" transform="rotate(72)"/>
<g><circle cx="-178" cy="-26" r="26" fill="#10182a" stroke="#247bff"/><text x="-178" y="-19" text-anchor="middle" class="small white">PY</text><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/></g>
<g transform="rotate(90)"><circle cx="-190" cy="0" r="26" fill="#10182a" stroke="#ff354f"/><text x="-190" y="7" text-anchor="middle" class="small white">JS</text><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/></g>
<g transform="rotate(205)"><circle cx="-190" cy="0" r="26" fill="#10182a" stroke="#247bff"/><text x="-190" y="7" text-anchor="middle" class="small white">RE</text><animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="16s" repeatCount="indefinite"/></g>
<circle r="48" fill="#0d1424" stroke="#26324b"/><text text-anchor="middle" y="8" class="h2 white">BUILD</text></g>
<g transform="translate(600 154)"><text class="small muted">LANGUAGES</text><g transform="translate(0 18)"><rect width="112" height="34" rx="17" fill="#10182a"/><text x="56" y="23" text-anchor="middle" class="small white">Python</text><rect x="122" width="126" height="34" rx="17" fill="#10182a"/><text x="185" y="23" text-anchor="middle" class="small white">JavaScript</text></g><text y="88" class="small muted">WEB</text><g transform="translate(0 106)"><rect width="84" height="34" rx="17" fill="#10182a"/><text x="42" y="23" text-anchor="middle" class="small white">HTML</text><rect x="94" width="72" height="34" rx="17" fill="#10182a"/><text x="130" y="23" text-anchor="middle" class="small white">CSS</text><rect x="176" width="100" height="34" rx="17" fill="#10182a"/><text x="226" y="23" text-anchor="middle" class="small white">ReactJS</text></g><text y="176" class="small muted">DATA / OS</text><g transform="translate(0 194)"><rect width="82" height="34" rx="17" fill="#10182a"/><text x="41" y="23" text-anchor="middle" class="small white">MySQL</text><rect x="92" width="82" height="34" rx="17" fill="#10182a"/><text x="133" y="23" text-anchor="middle" class="small white">Linux</text></g></g></g></svg>'''
open(A+'/stack.svg','w').write(stack)

# ID DASHBOARD
id_svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="t d"><title id="t">Developer ID dashboard</title><desc id="d">Hanging lanyard ID with portrait placeholder, barcode and light sweep.</desc>{CSS}{bg(900,520,'id')}
<g class="motion" transform="translate(450 30)"><animateTransform attributeName="transform" type="rotate" values="-1.7 0 0;1.7 0 0;-1.7 0 0" dur="4.8s" begin="0s" repeatCount="indefinite"/>
<path d="M-42 0 Q0 42 42 0" fill="none" stroke="#d8dde8" stroke-width="8" stroke-linecap="round"/><rect x="-18" y="8" width="36" height="18" rx="5" fill="#8c96a8"/><path d="M0 26v28" stroke="#d8dde8" stroke-width="6"/><rect x="-150" y="54" width="300" height="370" rx="24" fill="#10182a" stroke="#53627f" stroke-width="2"/><rect x="-150" y="54" width="300" height="8" rx="4" fill="#247bff"/><text x="-120" y="96" class="small blue">SOFTWARE DEVELOPER</text><text x="-120" y="132" class="h2 white">KHAN AJIZUR</text><text x="-120" y="164" class="h2 white">REHMAN</text>
<rect x="-120" y="184" width="110" height="126" rx="16" fill="#070b16" stroke="#26324b"/><image x="-116" y="188" width="102" height="118" preserveAspectRatio="xMidYMid slice" href="data:image/png;base64,{PLACEHOLDER}"/>
<text x="4" y="204" class="small muted">LOCATION</text><text x="4" y="228" class="body white">Mumbai, India</text><text x="4" y="264" class="small muted">EDUCATION</text><text x="4" y="288" class="body white">BSc-IT · 8.6 CGPA</text><text x="-120" y="338" class="small muted">GITHUB</text><text x="-120" y="362" class="body white">rehm4nkh4n</text>
<g transform="translate(-120 378)"><rect width="240" height="28" rx="5" fill="#f5f7fb" opacity=".95"/><g fill="#070b16">{''.join(f'<rect x="{i*5+4}" y="4" width="{1+(i%4==0)}" height="20"/>' for i in range(45))}</g></g>
<rect x="-150" y="54" width="300" height="370" rx="24" fill="url(#foil)" opacity=".12"><animate attributeName="x" values="-360;150;-360" dur="5s" repeatCount="indefinite"/></rect>
<defs><linearGradient id="foil" x1="0" x2="1"><stop stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs></g></svg>'''
open(A+'/id-dashboard.svg','w').write(id_svg)

# CONNECT
connect=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="t d"><title id="t">Connect with Khan Ajizur Rehman</title><desc id="d">Pointing character placeholder and social cards.</desc>{CSS}{bg(900,520,'connect')}
<g class="motion">{image_data(48,110,300,300)}<text x="198" y="438" text-anchor="middle" class="small muted">RIGHT_POINTING.PNG — ADD YOUR IMAGE</text>
<text x="410" y="76" class="small blue">CONNECT</text><text x="410" y="118" class="h2 white">LET'S BUILD SOMETHING.</text>
<g transform="translate(410 158)"><rect width="390" height="74" rx="20" fill="#10182a" stroke="#26324b"/><circle cx="38" cy="37" r="20" fill="#247bff"/><text x="38" y="43" text-anchor="middle" class="small white">GH</text><text x="76" y="31" class="small muted">GITHUB</text><text x="76" y="54" class="body white">rehm4nkh4n</text><text x="350" y="45" class="h2 blue">→</text><animateTransform attributeName="transform" type="translate" values="410 158;414 158;410 158" dur="1.4s" repeatCount="indefinite"/></g>
<g transform="translate(410 248)"><rect width="390" height="74" rx="20" fill="#10182a" stroke="#26324b"/><circle cx="38" cy="37" r="20" fill="#0a66c2"/><text x="38" y="43" text-anchor="middle" class="small white">in</text><text x="76" y="31" class="small muted">LINKEDIN</text><text x="76" y="54" class="body white">ajizur-rehman-khan</text><text x="350" y="45" class="h2 blue">→</text></g>
<g transform="translate(410 338)"><rect width="390" height="74" rx="20" fill="#10182a" stroke="#26324b"/><circle cx="38" cy="37" r="20" fill="#ff354f"/><text x="38" y="43" text-anchor="middle" class="small white">↗</text><text x="76" y="31" class="small muted">PORTFOLIO</text><text x="76" y="54" class="body white">myportfolio-one-virid-51.vercel.app</text><text x="350" y="45" class="h2 blue">→</text></g>
<text x="410" y="466" class="small muted">SOCIAL LINKS ARE CLICKABLE IN README BELOW THIS IMAGE.</text></g></svg>'''
open(A+'/connect.svg','w').write(connect)

# README
readme='''# Khan Ajizur Rehman — Software Developer\n\n<p align="center">\n  <img src="./assets/hero.svg?v=1" alt="Khan Ajizur Rehman hero" width="900" />\n</p>\n\n<p align="center">\n  <img src="./assets/about-life.svg?v=1" alt="About and interests" width="900" />\n</p>\n\n<p align="center">\n  <img src="./assets/stack.svg?v=1" alt="Technology stack" width="900" />\n</p>\n\n<p align="center">\n  <img src="./assets/id-dashboard.svg?v=1" alt="Developer ID dashboard" width="900" />\n</p>\n\n## Projects\n\n| Project | Description |\n|---|---|\n| **ParentZone** | Comprehensive parental-control application using React.js to monitor and manage digital activity, with an intuitive interface and security-focused UI elements. |\n| **ChopperCare** | Dental clinic management website for clinic activities, appointment booking, and services. |\n\n<p align="center">\n  <img src="./assets/connect.svg?v=1" alt="Connect" width="900" />\n</p>\n\n### Connect\n\n- [GitHub](https://www.github.com/rehm4nkh4n)\n- [LinkedIn](https://www.linkedin.com/in/ajizur-rehman-khan-83815238a?utm_source=share_via&utm_content=profile&utm_medium=member_android)\n- [Portfolio](https://myportfolio-one-virid-51.vercel.app/)\n- [ParentZone repository](https://github.com/Rehm4nkh4n/ParentZone)\n- [ChopperCare repository](https://github.com/Rehm4nkh4n/Choppercare)\n\n> **Image setup:** `id.png` and `right_pointing.png` are intentionally left for you to add later. Run `python scripts/embed_images.py` after placing them in the repository root; the script embeds them into the SVGs so the final SVGs remain self-contained.\n\n### Typography & icon notes\n\n- Display: **Cabin Bold**, embedded as WOFF2; SIL Open Font License 1.1.\n- Mono: **DejaVu Sans Mono**, embedded as WOFF2; license text included in `licenses/`.\n- Platform cards use compact monograms rather than externally loaded brand assets, keeping all SVGs self-contained and network-free.\n- No contribution-city section is included.\n'''
open(ROOT+'/README.md','w').write(readme)

# Embed script
script='''from pathlib import Path\nimport base64\nROOT=Path(__file__).resolve().parents[1]\nassets=ROOT/'assets'\n\ndef data_uri(path):\n    return 'data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode()\n\ndef replace_all(old,new):\n    for p in assets.glob('*.svg'):\n        s=p.read_text()\n        s=s.replace(old,new)\n        p.write_text(s)\n\n# Exact supplied assets are embedded only after you place them here.\n# id.png updates portrait slots; right_pointing.png updates the Connect portrait slot.\nidp=ROOT/'id.png'\nrp=ROOT/'right_pointing.png'\nif not idp.exists() or not rp.exists():\n    missing=[]\n    if not idp.exists(): missing.append('id.png')\n    if not rp.exists(): missing.append('right_pointing.png')\n    raise SystemExit('Missing: '+', '.join(missing))\nuid=data_uri(idp); urp=data_uri(rp)\nfor name in ['hero.svg','id-dashboard.svg']:\n    p=assets/name; s=p.read_text(); s=s.replace('data:image/png;base64,PLACEHOLDER_ID',uid)\n# replace existing placeholder data in hero/id with id image, and connect with right image\nplaceholder='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='\nfor name in ['hero.svg','id-dashboard.svg']:\n    p=assets/name; p.write_text(p.read_text().replace(placeholder,uid))\np=assets/'connect.svg'; p.write_text(p.read_text().replace(placeholder,urp))\nprint('Embedded id.png into hero.svg + id-dashboard.svg; right_pointing.png into connect.svg')\n'''
open(ROOT+'/scripts/embed_images.py','w').write(script)

# Preview
preview='''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Khan Ajizur Rehman README Preview</title><style>body{margin:0;background:#050811;color:#f5f7fb;font-family:Arial,sans-serif}main{max-width:940px;margin:auto;padding:20px}img{display:block;width:100%;margin:20px 0;border-radius:28px;background:#070b16}a{color:#70a8ff}</style></head><body><main><h1>Khan Ajizur Rehman — README Preview</h1><img src="assets/hero.svg?v=1"><img src="assets/about-life.svg?v=1"><img src="assets/stack.svg?v=1"><img src="assets/id-dashboard.svg?v=1"><img src="assets/connect.svg?v=1"><p><a href="https://www.github.com/rehm4nkh4n">GitHub</a> · <a href="https://www.linkedin.com/in/ajizur-rehman-khan-83815238a?utm_source=share_via&utm_content=profile&utm_medium=member_android">LinkedIn</a> · <a href="https://myportfolio-one-virid-51.vercel.app/">Portfolio</a></p></main></body></html>'''
open(ROOT+'/preview.html','w').write(preview)

# Build instructions and verification manifest
open(ROOT+'/BUILD_NOTES.md','w').write('''# Upload notes\n\n1. Add your exact `id.png` and `right_pointing.png` at repository root.\n2. Run `python scripts/embed_images.py`.\n3. Commit the generated SVGs and README.\n\nCurrent SVGs contain a 1×1 transparent placeholder because the requested image files were not supplied in this conversation. No portrait was redrawn or invented.\n''')
print('built')
