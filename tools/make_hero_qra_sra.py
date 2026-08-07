#!/usr/bin/env python3
"""
Hero banner generator for the QRA/SRA (Tropic Ridge) post.

Reuses the house theme verbatim from tools/make_hero_2026-07-31.py
(dark navy, faint grid, purple/white two-line title, amber strap,
teal mono callout, purple ridge silhouette, SJP/CBL footer) so this
post's hero sits visually in the same series as the Renewables one.

Construction bent: three schematic tower cranes in place of the wind
turbines, tags read "risk.type: ..." instead of "asset.type: ...".

Renders 1200x630 (Open Graph / Quarto listing card ratio).
"""

import math

W, H = 1200, 630

BG      = "#10121f"
GRID    = "#191d2c"
PURPLE  = "#a78bfa"
WHITE   = "#ffffff"
MUTED   = "#8b93b8"
DIM     = "#6b7390"
AMBER   = "#fbbf24"
TEAL    = "#2dd4bf"
PINK    = "#f472b6"
INDIGO  = "#818cf8"

SANS = "Liberation Sans, DejaVu Sans, sans-serif"
MONO = "Liberation Mono, DejaVu Sans Mono, monospace"

OUT_DIR = r"C:\Users\spinb\projects\cblanalytics-blog\posts\2026-08-06-tropic-ridge-qra-sra\images"
OUT_PNG = OUT_DIR + r"\hero.png"
OUT_SVG = OUT_DIR + r"\hero.svg"

T1 = "Construction Risk"
T2 = "Priced and Replayed"
STRAP = "QRA and SRA, with Claude's help"

p = []
add = p.append


# ---------------------------------------------------------------- cranes
def crane(cx, ground, height, jib, cjib, colour, opacity=1.0):
    """A schematic tower crane standing on `ground`.

    cx      mast centreline
    height  mast height above ground (pivot height)
    jib     main jib length (load side)
    cjib    counter-jib length (counterweight side)
    """
    py = ground - height
    apex = py - height * 0.11
    base_w, top_w = height * 0.020, height * 0.008
    g = [f'<g opacity="{opacity}">']

    # tapered mast
    g.append(
        f'<path d="M {cx-base_w:.1f} {ground:.1f} L {cx-top_w:.1f} {py:.1f} '
        f'L {cx+top_w:.1f} {py:.1f} L {cx+base_w:.1f} {ground:.1f} Z" '
        f'fill="{colour}" opacity="0.85"/>'
    )
    # footing
    g.append(
        f'<rect x="{cx-base_w*3.2:.1f}" y="{ground-1.6:.1f}" '
        f'width="{base_w*6.4:.1f}" height="3" rx="1.5" '
        f'fill="{colour}" opacity="0.45"/>'
    )
    # operator cab, under the jib pivot
    cab_w, cab_h = height * 0.05, height * 0.032
    g.append(
        f'<rect x="{cx:.1f}" y="{py:.1f}" width="{cab_w:.1f}" '
        f'height="{cab_h:.1f}" fill="{colour}"/>'
    )
    # apex strut above the pivot
    g.append(
        f'<line x1="{cx:.1f}" y1="{py:.1f}" x2="{cx:.1f}" y2="{apex:.1f}" '
        f'stroke="{colour}" stroke-width="2"/>'
    )
    # jib + counter-jib beam
    g.append(
        f'<line x1="{cx-cjib:.1f}" y1="{py:.1f}" x2="{cx+jib:.1f}" y2="{py:.1f}" '
        f'stroke="{colour}" stroke-width="2.6"/>'
    )
    # tie cables, apex to each beam end
    g.append(
        f'<line x1="{cx:.1f}" y1="{apex:.1f}" x2="{cx+jib:.1f}" y2="{py:.1f}" '
        f'stroke="{colour}" stroke-width="1.2" opacity="0.8"/>'
    )
    g.append(
        f'<line x1="{cx:.1f}" y1="{apex:.1f}" x2="{cx-cjib:.1f}" y2="{py:.1f}" '
        f'stroke="{colour}" stroke-width="1.2" opacity="0.8"/>'
    )
    # counterweight block
    cw = height * 0.028
    g.append(
        f'<rect x="{cx-cjib-cw/2:.1f}" y="{py:.1f}" width="{cw:.1f}" '
        f'height="{cw*1.5:.1f}" fill="{colour}" opacity="0.9"/>'
    )
    # trolley + hoist line + hook
    trolley_x = cx + jib * 0.60
    hook_len = height * 0.28
    g.append(
        f'<line x1="{trolley_x:.1f}" y1="{py:.1f}" '
        f'x2="{trolley_x:.1f}" y2="{py+hook_len:.1f}" '
        f'stroke="{colour}" stroke-width="1.1" opacity="0.85"/>'
    )
    g.append(
        f'<circle cx="{trolley_x:.1f}" cy="{py+hook_len:.1f}" '
        f'r="{height*0.016:.1f}" fill="{colour}"/>'
    )
    g.append("</g>")
    return "".join(g)


def chip(x, y, w, h, label, sub, colour):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
        f'fill="none" stroke="{colour}" stroke-width="1.4" opacity="0.9"/>'
        f'<text x="{x+w/2}" y="{y+24}" font-family="{MONO}" font-size="14.5" '
        f'font-weight="bold" fill="{colour}" text-anchor="middle" '
        f'letter-spacing="1.4">{label}</text>'
        f'<text x="{x+w/2}" y="{y+40}" font-family="{MONO}" font-size="10.5" '
        f'fill="{MUTED}" text-anchor="middle">{sub}</text>'
    )


def tag(cx, y, text, colour):
    w = len(text) * 6.6 + 20
    return (
        f'<rect x="{cx-w/2:.1f}" y="{y}" width="{w:.1f}" height="19" rx="3.5" '
        f'fill="{BG}" stroke="{colour}" stroke-width="1.1" opacity="0.95"/>'
        f'<text x="{cx:.1f}" y="{y+13.5}" font-family="{MONO}" font-size="10.5" '
        f'fill="{colour}" text-anchor="middle">{text}</text>'
    )


# ---------------------------------------------------------------- canvas
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}">')
add('<defs>'
    f'<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
    f'<stop offset="0%" stop-color="{PURPLE}"/>'
    f'<stop offset="55%" stop-color="#c084fc"/>'
    f'<stop offset="100%" stop-color="{PINK}"/></linearGradient>'
    f'<linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0%" stop-color="#1b1533" stop-opacity="0"/>'
    f'<stop offset="100%" stop-color="#241a3d" stop-opacity="0.85"/></linearGradient>'
    '</defs>')
add(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

for x in range(0, W + 1, 60):
    add(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{GRID}" stroke-width="1"/>')
for y in range(0, H + 1, 60):
    add(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{GRID}" stroke-width="1"/>')

# ridge (same silhouette as the house theme)
add(f'<rect x="0" y="380" width="{W}" height="250" fill="url(#glow)"/>')
add('<path d="M 0 588 L 210 578 L 400 586 L 560 566 L 700 556 L 800 543 '
    f'L 900 553 L 985 541 L 1080 546 L 1200 533 L 1200 630 L 0 630 Z" '
    f'fill="#2e2149" opacity="0.85"/>')
add('<path d="M 0 610 L 260 600 L 520 608 L 700 592 L 880 601 L 1040 588 '
    f'L 1200 596 L 1200 630 L 0 630 Z" fill="#1b1530" opacity="0.95"/>')

# frame
add(f'<path d="M 34 52 L 34 22 L 64 22" fill="none" stroke="{PURPLE}" '
    f'stroke-width="1.6" opacity="0.75"/>')
add(f'<line x1="80" y1="101" x2="1120" y2="101" stroke="url(#rule)" stroke-width="1.8"/>')
add(f'<circle cx="243" cy="74" r="3.4" fill="{TEAL}"/>')
add(f'<circle cx="544" cy="91" r="3.4" fill="{PINK}"/>')
add(f'<circle cx="1082" cy="76" r="3.0" fill="{MUTED}" opacity="0.8"/>')
add(f'<circle cx="578" cy="482" r="3.2" fill="{AMBER}"/>')

# copy
X = 88
add(f'<text x="{X}" y="165" font-family="{SANS}" font-size="15" font-weight="bold" '
    f'fill="{MUTED}" letter-spacing="5.2">VIBE ANALYTICS</text>')

add(f'<text x="{X}" y="255" font-family="{SANS}" font-size="60" font-weight="bold" '
    f'fill="{PURPLE}">{T1}</text>')
add(f'<text x="{X}" y="328" font-family="{SANS}" font-size="60" font-weight="bold" '
    f'fill="{WHITE}">{T2}</text>')

add(f'<text x="{X}" y="390" font-family="{SANS}" font-size="22" font-weight="bold" '
    f'fill="{AMBER}">{STRAP}</text>')
add(f'<text x="{X}" y="432" font-family="{SANS}" font-size="17" fill="#c4cad8">'
    f'A cost Monte Carlo and a full CPM schedule replay run off</text>')
add(f'<text x="{X}" y="457" font-family="{SANS}" font-size="17" fill="#c4cad8">'
    f'the same risk register &#8212; then join correctly.</text>')
add(f'<text x="{X}" y="507" font-family="{MONO}" font-size="15" fill="{TEAL}">'
    f'moral: P80(cost) + P80(schedule) != P80(joint)</text>')

# footer
add(f'<text x="{X}" y="599" font-family="{SANS}" font-size="14" font-weight="bold" '
    f'fill="{AMBER}">SJP Consulting</text>')
add(f'<text x="{X+123}" y="599" font-family="{SANS}" font-size="14" fill="{DIM}">'
    f'&#183;  CBL Analytics</text>')

# right side: tool-chain chips
cw, ch, gap, cx0, cy0 = 88, 50, 12, 700, 240
for i, (lab, sub, col) in enumerate([
        ("REGISTER", "risk + EMV", TEAL),
        ("EXCEL", "xlwings", INDIGO),
        ("PYTHON", "CPM engine", PINK),
        ("DASHBOARD", "monthly", AMBER)]):
    add(chip(cx0 + i * (cw + gap), cy0, cw, ch, lab, sub, col))

add(f'<line x1="{cx0}" y1="{cy0+ch+14}" x2="{cx0+4*cw+3*gap}" y2="{cy0+ch+14}" '
    f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')
for i in range(4):
    x = cx0 + i * (cw + gap) + cw / 2
    add(f'<line x1="{x}" y1="{cy0+ch}" x2="{x}" y2="{cy0+ch+14}" '
        f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')

# cranes on the ridge (mirrors the turbine composition: faded/mid/foreground)
add(crane(1088, 545, 74, 40, 16, INDIGO, opacity=0.48))
add(crane(958, 550, 100, 54, 20, PINK, opacity=0.85))
add(crane(800, 544, 132, 70, 26, TEAL, opacity=1.0))

add(tag(800, 566, "risk.type: cost", TEAL))
add(tag(963, 566, "risk.type: schedule", PINK))
add(tag(1113, 566, "risk.type: joint", INDIGO))

add("</svg>")

svg = "".join(p)
with open(OUT_SVG, "w") as f:
    f.write(svg)
print("wrote", OUT_SVG)

try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT_PNG,
                      output_width=W, output_height=H)
    print("wrote", OUT_PNG, "via cairosvg")
except Exception as e:
    print("cairosvg unavailable (", e, ") - render", OUT_SVG,
          "to PNG separately, e.g. via headless Edge.")
