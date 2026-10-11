import base64, os

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
A = os.path.join(ROOT, 'assets')

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

FONT_DISPLAY = b64(os.path.join(ROOT, 'fonts', 'Cabin-Bold.woff2'))
FONT_MONO    = b64(os.path.join(ROOT, 'fonts', 'DejaVuSansMono.woff2'))

PLACEHOLDER = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='

# ─── Shared CSS ───────────────────────────────────────────────────────────────
CSS = f'''<style>
@font-face{{font-family:CabinX;src:url(data:font/woff2;base64,{FONT_DISPLAY}) format('woff2');font-weight:700}}
@font-face{{font-family:MonoX;src:url(data:font/woff2;base64,{FONT_MONO}) format('woff2');font-weight:400}}
*{{font-family:CabinX,Arial,sans-serif;box-sizing:border-box}}
.mono,.sm,.tag,.label{{font-family:MonoX,monospace}}
.sm{{font-size:11px;letter-spacing:2px;text-transform:uppercase}}
.label{{font-size:10px;letter-spacing:3px;text-transform:uppercase}}
.title{{font-size:52px;font-weight:700;letter-spacing:-1px}}
.sub{{font-size:32px;font-weight:700;letter-spacing:-0.5px}}
.body{{font-size:16px;line-height:1.6}}
.caption{{font-size:13px}}
.w{{fill:#eef0f6}}.m{{fill:#6b7a99}}.b{{fill:#3b82f6}}.r{{fill:#f43f5e}}.dim{{fill:#394462}}
@media(prefers-reduced-motion:reduce){{.motion,.motion *{{animation:none!important;transition:none!important}}}}
</style>'''

# ─── Shared background ────────────────────────────────────────────────────────
def bg(w, h, uid):
    return (
        f'<defs>'
        f'<pattern id="{uid}p" width="24" height="24" patternUnits="userSpaceOnUse">'
        f'<circle cx="1" cy="1" r="1" fill="#fff" opacity=".04"/>'
        f'</pattern>'
        f'<linearGradient id="{uid}g" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="#3b82f6" stop-opacity=".6"/>'
        f'<stop offset="1" stop-color="#f43f5e" stop-opacity=".6"/>'
        f'</linearGradient>'
        f'</defs>'
        f'<rect width="{w}" height="{h}" rx="20" fill="#060c1a"/>'
        f'<rect width="{w}" height="{h}" rx="20" fill="url(#{uid}p)"/>'
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="19" fill="none" '
        f'stroke="url(#{uid}g)" stroke-width="1.5"/>'
    )

# ─── Pill / chip helper ────────────────────────────────────────────────────────
def chip(x, y, label, accent='#1e293b', border='#2d3f60', textcol='#eef0f6'):
    pad_x = 18
    char_w = 8.5
    w = int(len(label) * char_w + pad_x * 2)
    h = 30
    return (
        f'<g transform="translate({x},{y})">'
        f'<rect width="{w}" height="{h}" rx="15" fill="{accent}" stroke="{border}" stroke-width="1"/>'
        f'<text x="{w//2}" y="20" text-anchor="middle" class="sm" fill="{textcol}">{label}</text>'
        f'</g>'
    )

# ─── Divider line ──────────────────────────────────────────────────────────────
def div(x, y, w=60, col='#3b82f6'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="2" rx="1" fill="{col}"/>'

# ─── Placeholder image box ────────────────────────────────────────────────────
def imgbox(x, y, w, h):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#0d1526" stroke="#1e2d4a" stroke-width="1.5"/>'
        f'<image x="{x+3}" y="{y+3}" width="{w-6}" height="{h-6}" '
        f'preserveAspectRatio="xMidYMid slice" '
        f'href="data:image/png;base64,{PLACEHOLDER}"/>'
    )

# ══════════════════════════════════════════════════════════════════════════════
# 1. HERO
# ══════════════════════════════════════════════════════════════════════════════
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="ht hd">
<title id="ht">Khan Ajizur Rehman — Software Developer</title>
<desc id="hd">Developer profile card for Khan Ajizur Rehman.</desc>
{CSS}{bg(900,480,'h')}
<g class="motion">

  <!-- left column -->
  <text x="56" y="72" class="label m">Mumbai, India</text>
  <text x="56" y="136" class="title w">Khan Ajizur</text>
  <text x="56" y="190" class="title w">Rehman.</text>
  {div(56, 206, 48)}

  <!-- animated role -->
  <g transform="translate(56 240)">
    <text y="0" class="sub b" opacity="1">Full-Stack Developer<animate attributeName="opacity" dur="9s" repeatCount="indefinite" values="1;1;0;0;0;0;0;0;1" keyTimes="0;.22;.25;.50;.52;.77;.80;.98;1"/></text>
    <text y="0" class="sub b" opacity="0">SOC Analyst<animate attributeName="opacity" dur="9s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0;0" keyTimes="0;.22;.25;.50;.52;.77;.80;.98;1"/></text>
    <text y="0" class="sub b" opacity="0">Data Analyst<animate attributeName="opacity" dur="9s" repeatCount="indefinite" values="0;0;0;0;1;1;0;0;0" keyTimes="0;.22;.25;.50;.52;.77;.80;.98;1"/></text>
  </g>

  <text x="56" y="316" class="body m">Building secure, fast web experiences</text>
  <text x="56" y="338" class="body m">with Python, React, and a security-first mindset.</text>

  <!-- stat pills -->
  {chip(56, 368, 'BSc-IT', '#0f1e38', '#2d3f60')}
  {chip(148, 368, '8.6 CGPA', '#0f1e38', '#2d3f60')}
  {chip(260, 368, 'Open to Work', '#0f2310', '#1a5c2a', '#4ade80')}

  <!-- bottom tech bar -->
  <rect x="56" y="438" width="420" height="1" fill="#1e2d4a"/>
  <text x="56" y="460" class="label m">Python · JavaScript · React · MySQL · Linux</text>

  <!-- right column: photo placeholder -->
  {imgbox(660, 50, 200, 280)}
  <text x="760" y="354" text-anchor="middle" class="label b">Software Developer</text>
  <text x="760" y="374" text-anchor="middle" class="caption m">@rehm4nkh4n</text>

  <!-- animated entry bar -->
  <rect x="56" y="204" width="0" height="2" rx="1" fill="#3b82f6">
    <animate attributeName="width" from="0" to="48" dur="0.6s" begin="0.2s" fill="freeze"/>
  </rect>

</g>
</svg>'''

# ══════════════════════════════════════════════════════════════════════════════
# 2. ABOUT / LIFE
# ══════════════════════════════════════════════════════════════════════════════
about = f'''<svg xmlns="http://www.w3.org/2000/svg"
  width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="at ad">
<title id="at">About and interests — Khan Ajizur Rehman</title>
<desc id="ad">Capabilities panel and interests carousel.</desc>
{CSS}{bg(900,480,'a')}
<g class="motion">

  <text x="56" y="64" class="label b">About</text>
  <text x="56" y="108" class="sub w">Always learning,</text>
  <text x="56" y="144" class="sub w">always building.</text>
  {div(56, 158, 32)}

  <!-- left card: skills -->
  <g transform="translate(56 180)">
    <rect width="268" height="242" rx="16" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
    <text x="22" y="36" class="label m">Capabilities</text>
    <text x="22" y="74" class="caption w">  Front-end development</text>
    <text x="22" y="100" class="caption w">  Python scripting</text>
    <text x="22" y="126" class="caption w">  Security-conscious design</text>
    <text x="22" y="152" class="caption w">  Data analysis</text>
    <text x="22" y="178" class="caption w">  Linux system workflows</text>
    <text x="22" y="214" class="caption m">BSc-IT · 8.6 CGPA · Mumbai</text>
  </g>

  <!-- right carousel -->
  <g transform="translate(356 180)">
    <rect width="490" height="242" rx="16" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>

    <!-- slide 1: cybersecurity -->
    <g opacity="1">
      <text x="28" y="36" class="label b">01 — Cybersecurity</text>
      <text x="28" y="80" class="sub w">Secure by default.</text>
      <text x="28" y="122" class="caption m">Exploring SOC workflows, defensive</text>
      <text x="28" y="146" class="caption m">thinking, and practical security tooling.</text>
      <animate attributeName="opacity" dur="12s" repeatCount="indefinite"
        values="1;1;0;0;0;0;1" keyTimes="0;.30;.34;.63;.67;.96;1"/>
    </g>

    <!-- slide 2: web dev -->
    <g opacity="0">
      <text x="28" y="36" class="label b">02 — Web Development</text>
      <text x="28" y="80" class="sub w">Make it useful.</text>
      <text x="28" y="122" class="caption m">Designing interfaces that feel fast,</text>
      <text x="28" y="146" class="caption m">intentional, and accessible.</text>
      <animate attributeName="opacity" dur="12s" repeatCount="indefinite"
        values="0;0;1;1;0;0;0" keyTimes="0;.30;.34;.63;.67;.96;1"/>
    </g>

    <!-- slide 3: data -->
    <g opacity="0">
      <text x="28" y="36" class="label b">03 — Data</text>
      <text x="28" y="80" class="sub w">Signal over noise.</text>
      <text x="28" y="122" class="caption m">Turning raw data into clear insights</text>
      <text x="28" y="146" class="caption m">through analysis and visualization.</text>
      <animate attributeName="opacity" dur="12s" repeatCount="indefinite"
        values="0;0;0;0;1;1;0" keyTimes="0;0;.34;.63;.67;.96;1"/>
    </g>

    <!-- progress dots -->
    <g transform="translate(28 210)">
      <circle cx="6"  cy="6" r="5" fill="#1e2d4a"/>
      <circle cx="22" cy="6" r="5" fill="#1e2d4a"/>
      <circle cx="38" cy="6" r="5" fill="#1e2d4a"/>
      <!-- active dot -->
      <circle cx="6" cy="6" r="5" fill="#3b82f6">
        <animate attributeName="cx" dur="12s" repeatCount="indefinite"
          values="6;6;22;22;38;38;6" keyTimes="0;.30;.34;.63;.67;.96;1"/>
      </circle>
    </g>
  </g>

</g>
</svg>'''

# ══════════════════════════════════════════════════════════════════════════════
# 3. STACK
# ══════════════════════════════════════════════════════════════════════════════
# Build chips for each category
lang_chips = ''
lang_row = ['Python', 'JavaScript']
xc = 0
for t in lang_row:
    cw = int(len(t) * 8.5 + 36)
    lang_chips += chip(xc, 0, t)
    xc += cw + 10

web_chips = ''
web_row = ['HTML', 'CSS', 'React']
xc = 0
for t in web_row:
    cw = int(len(t) * 8.5 + 36)
    web_chips += chip(xc, 0, t)
    xc += cw + 10

data_chips = ''
data_row = ['MySQL', 'Linux', 'Git']
xc = 0
for t in data_row:
    cw = int(len(t) * 8.5 + 36)
    data_chips += chip(xc, 0, t)
    xc += cw + 10

security_chips = ''
sec_row = ['Wireshark', 'Nmap', 'Kali Linux']
xc = 0
for t in sec_row:
    cw = int(len(t) * 8.5 + 36)
    security_chips += chip(xc, 0, t)
    xc += cw + 10

stack = f'''<svg xmlns="http://www.w3.org/2000/svg"
  width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="st sd">
<title id="st">Technology stack — Khan Ajizur Rehman</title>
<desc id="sd">Programming languages and tools used by Khan Ajizur Rehman.</desc>
{CSS}{bg(900,480,'s')}
<g class="motion">

  <text x="56" y="64" class="label b">Stack</text>
  <text x="56" y="108" class="sub w">Tools I ship with.</text>
  {div(56, 122, 32)}

  <!-- orbit visual, center at 260,290 -->
  <g transform="translate(260 295)">
    <ellipse rx="180" ry="68" fill="none" stroke="#3b82f6" stroke-opacity=".2" stroke-width="1.5" transform="rotate(-15)"/>
    <ellipse rx="180" ry="68" fill="none" stroke="#f43f5e" stroke-opacity=".15" stroke-width="1.5" transform="rotate(35)"/>
    <ellipse rx="180" ry="68" fill="none" stroke="#eef0f6" stroke-opacity=".07" stroke-width="1.5" transform="rotate(78)"/>

    <!-- orbiting nodes -->
    <g><circle cx="-140" cy="-18" r="22" fill="#0a1628" stroke="#3b82f6" stroke-width="1.5"/>
       <text x="-140" y="-11" text-anchor="middle" class="sm w">PY</text>
       <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="13s" repeatCount="indefinite"/>
    </g>
    <g transform="rotate(90)">
       <circle cx="-150" cy="0" r="22" fill="#0a1628" stroke="#f43f5e" stroke-width="1.5"/>
       <text x="-150" y="7" text-anchor="middle" class="sm w">JS</text>
       <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="17s" repeatCount="indefinite"/>
    </g>
    <g transform="rotate(210)">
       <circle cx="-150" cy="0" r="22" fill="#0a1628" stroke="#3b82f6" stroke-width="1.5"/>
       <text x="-150" y="7" text-anchor="middle" class="sm w">RE</text>
       <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="15s" repeatCount="indefinite"/>
    </g>

    <!-- center -->
    <circle r="40" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
    <text y="6" text-anchor="middle" class="sm b">BUILD</text>
  </g>

  <!-- right: chip groups -->
  <g transform="translate(520 160)">
    <text y="0" class="label m">Languages</text>
    <g transform="translate(0 14)">{lang_chips}</g>

    <text y="70" class="label m">Web</text>
    <g transform="translate(0 84)">{web_chips}</g>

    <text y="140" class="label m">Data / OS</text>
    <g transform="translate(0 154)">{data_chips}</g>

    <text y="210" class="label m">Security</text>
    <g transform="translate(0 224)">{security_chips}</g>
  </g>

</g>
</svg>'''

# ══════════════════════════════════════════════════════════════════════════════
# 4. ID DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
# barcode bars
bars = ''.join(
    f'<rect x="{i*4+4}" y="3" width="{2 if i%5==0 else 1}" height="18" fill="#060c1a"/>'
    for i in range(56)
)

id_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="it id_">
<title id="it">Developer ID — Khan Ajizur Rehman</title>
<desc id="id_">Hanging developer ID card for Khan Ajizur Rehman.</desc>
{CSS}{bg(900,480,'i')}
<defs>
  <linearGradient id="foil" x1="0" x2="1">
    <stop offset="0"   stop-color="#fff" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#fff" stop-opacity="1"/>
    <stop offset="1"   stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="cardclip"><rect x="-148" y="52" width="296" height="372" rx="20"/></clipPath>
</defs>
<g class="motion" transform="translate(280 24)">
  <animateTransform attributeName="transform" type="rotate"
    values="-1.2 0 0;1.2 0 0;-1.2 0 0" dur="5s" repeatCount="indefinite"/>

  <!-- lanyard -->
  <path d="M-36 0 Q0 36 36 0" fill="none" stroke="#c8d0e0" stroke-width="6" stroke-linecap="round"/>
  <rect x="-14" y="8" width="28" height="16" rx="4" fill="#7a8599"/>
  <path d="M0 24 L0 52" stroke="#c8d0e0" stroke-width="5" stroke-linecap="round"/>

  <!-- card body -->
  <rect x="-148" y="52" width="296" height="372" rx="20" fill="#0a1628" stroke="#2d3f60" stroke-width="1.5"/>

  <!-- top accent bar -->
  <rect x="-148" y="52" width="296" height="6" rx="3" fill="#3b82f6"/>

  <!-- header area -->
  <text x="-118" y="90"  class="label b">Software Developer</text>
  <text x="-118" y="126" class="sub w">Khan Ajizur</text>
  <text x="-118" y="158" class="sub w">Rehman</text>
  {div(-118, 168, 40)}

  <!-- photo -->
  <rect x="-118" y="180" width="106" height="120" rx="12" fill="#060c1a" stroke="#1e2d4a" stroke-width="1.5"/>
  <image x="-114" y="184" width="98" height="112"
    preserveAspectRatio="xMidYMid slice"
    href="data:image/png;base64,{PLACEHOLDER}" clip-path="url(#cardclip)"/>

  <!-- right-side metadata -->
  <text x="4" y="196" class="label m">Location</text>
  <text x="4" y="216" class="caption w">Mumbai, India</text>

  <text x="4" y="244" class="label m">Education</text>
  <text x="4" y="264" class="caption w">BSc-IT · 8.6 CGPA</text>

  <text x="4" y="292" class="label m">GitHub</text>
  <text x="4" y="312" class="caption b">rehm4nkh4n</text>

  <!-- bottom section -->
  <rect x="-118" y="316" width="266" height="1" fill="#1e2d4a"/>
  <text x="-118" y="340" class="label m">Member Since</text>
  <text x="-118" y="360" class="caption w">2023</text>

  <!-- barcode -->
  <rect x="-118" y="378" width="236" height="28" rx="5" fill="#eef0f6" opacity=".95"/>
  <g transform="translate(-118 378)">{bars}</g>

  <!-- foil sweep -->
  <rect x="-148" y="52" width="296" height="372" rx="20"
    fill="url(#foil)" opacity=".08" clip-path="url(#cardclip)">
    <animate attributeName="x" values="-360;160;-360" dur="6s" repeatCount="indefinite"/>
  </rect>
</g>

<!-- right: quick stats -->
<g transform="translate(580 80)">
  <text y="0" class="label m">Quick Stats</text>

  <rect y="18"  width="264" height="72" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
  <text x="20"  y="50" class="label m">Degree</text>
  <text x="20"  y="72" class="caption w">BSc-IT — 8.6 CGPA</text>

  <rect y="106" width="264" height="72" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
  <text x="20"  y="138" class="label m">Location</text>
  <text x="20"  y="160" class="caption w">Mumbai, Maharashtra</text>

  <rect y="194" width="264" height="72" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
  <text x="20"  y="226" class="label m">Focus</text>
  <text x="20"  y="248" class="caption w">Full-Stack · Security · Data</text>

  <rect y="282" width="264" height="72" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
  <text x="20"  y="314" class="label m">Available For</text>
  <text x="20"  y="336" class="caption b">Internships · Collaborations</text>
</g>

</svg>'''

# ══════════════════════════════════════════════════════════════════════════════
# 5. CONNECT
# ══════════════════════════════════════════════════════════════════════════════
connect = f'''<svg xmlns="http://www.w3.org/2000/svg"
  width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="ct cd">
<title id="ct">Connect with Khan Ajizur Rehman</title>
<desc id="cd">Contact and social links for Khan Ajizur Rehman.</desc>
{CSS}{bg(900,480,'c')}
<g class="motion">

  <!-- left column: avatar + tagline -->
  {imgbox(52, 60, 260, 300)}
  <text x="182" y="378" text-anchor="middle" class="label m">Add your photo here</text>
  <text x="182" y="398" text-anchor="middle" class="caption m">run scripts/embed_images.py</text>

  <!-- right column -->
  <text x="360" y="80" class="label b">Connect</text>
  <text x="360" y="128" class="sub w">Let's build something</text>
  <text x="360" y="164" class="sub w">worth sharing.</text>
  {div(360, 178, 32)}

  <!-- GitHub card -->
  <a href="https://github.com/rehm4nkh4n" target="_blank">
    <g transform="translate(360 206)">
      <rect width="488" height="68" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
      <circle cx="34" cy="34" r="18" fill="#161b22" stroke="#2d3f60" stroke-width="1.5"/>
      <text x="34" y="39" text-anchor="middle" class="sm w">GH</text>
      <text x="68" y="24" class="label m">GitHub</text>
      <text x="68" y="46" class="caption w">github.com/rehm4nkh4n</text>
      <text x="460" y="40" text-anchor="end" class="caption b">→</text>
      <animateTransform attributeName="transform" type="translate"
        values="360 206;364 206;360 206" dur="2s" repeatCount="indefinite"/>
    </g>
  </a>

  <!-- LinkedIn card -->
  <a href="https://linkedin.com/in/ajizur-rehman-khan-83815238a" target="_blank">
    <g transform="translate(360 290)">
      <rect width="488" height="68" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
      <circle cx="34" cy="34" r="18" fill="#0a66c2" stroke="#0d5fa3" stroke-width="1.5"/>
      <text x="34" y="39" text-anchor="middle" class="sm w">in</text>
      <text x="68" y="24" class="label m">LinkedIn</text>
      <text x="68" y="46" class="caption w">ajizur-rehman-khan</text>
      <text x="460" y="40" text-anchor="end" class="caption b">→</text>
    </g>
  </a>

  <!-- Portfolio card -->
  <a href="https://myportfolio-one-virid-51.vercel.app/" target="_blank">
    <g transform="translate(360 374)">
      <rect width="488" height="68" rx="14" fill="#0a1628" stroke="#1e2d4a" stroke-width="1.5"/>
      <circle cx="34" cy="34" r="18" fill="#f43f5e" stroke="#c0304a" stroke-width="1.5"/>
      <text x="34" y="39" text-anchor="middle" class="sm w">↗</text>
      <text x="68" y="24" class="label m">Portfolio</text>
      <text x="68" y="46" class="caption w">myportfolio-one-virid-51.vercel.app</text>
      <text x="460" y="40" text-anchor="end" class="caption b">→</text>
    </g>
  </a>

</g>
</svg>'''

# ─── Write all files ──────────────────────────────────────────────────────────
files = {
    'hero.svg':         hero,
    'about-life.svg':   about,
    'stack.svg':        stack,
    'id-dashboard.svg': id_svg,
    'connect.svg':      connect,
}
for name, content in files.items():
    path = os.path.join(A, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ {name}')

print('\nDone. Run scripts/embed_images.py after adding id.png and right_pointing.png.')
