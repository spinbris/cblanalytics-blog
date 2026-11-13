#!/usr/bin/env python3
"""
Hero banner generator for "Retire the tool, keep the method" (12/11/2026).

House theme from tools/make_hero_2026-07-31.py and make_hero_qra_sra.py
(dark navy, faint grid, purple/white two-line title, amber strap, teal mono
callout, purple ridge, SJP/CBL footer). Variation for this post: three
schematic filings in place of turbines/cranes, the retired app faded and
dashed, highlighted blocks standing for the script-filled figures.

Renders 1200x630. Writes the SVG; PNG via cairosvg if installed, otherwise
render the SVG separately (headless browser).
"""

import os
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

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "posts", "2026-11-12-retire-the-tool-keep-the-method", "images")
OUT_SVG = os.path.join(OUT_DIR, "hero.svg")
OUT_PNG = os.path.join(OUT_DIR, "hero.png")

T1 = "Retire the Tool,"
T2 = "Keep the Method"
STRAP = "SEC research, rebuilt on current tools"

p = []
add = p.append


# ---------------------------------------------------------------- filings
def filing(cx, ground, h, colour, opacity=1.0, dashed=False):
    """A schematic filing (page with folded corner and text lines) standing on `ground`."""
    w = h * 0.74
    x0, y0 = cx - w / 2, ground - h
    fold = w * 0.24
    dash = ' stroke-dasharray="6 5"' if dashed else ''
    g = [f'<g opacity="{opacity}">']
    g.append(
        f'<path d="M {x0:.1f} {y0:.1f} L {x0+w-fold:.1f} {y0:.1f} L {x0+w:.1f} {y0+fold:.1f} '
        f'L {x0+w:.1f} {ground:.1f} L {x0:.1f} {ground:.1f} Z" fill="{BG}" '
        f'stroke="{colour}" stroke-width="2.2"{dash}/>'
    )
    g.append(
        f'<path d="M {x0+w-fold:.1f} {y0:.1f} L {x0+w-fold:.1f} {y0+fold:.1f} L {x0+w:.1f} {y0+fold:.1f}" '
        f'fill="none" stroke="{colour}" stroke-width="1.6"{dash}/>'
    )
    # text lines; the last few carry {{token}} blocks to echo the prose slots
    n = 6
    for i in range(n):
        ly = y0 + fold + 12 + i * (h - fold - 24) / (n - 1)
        lw = (w - 26) * (0.55 if i == n - 1 else 0.9)
        g.append(
            f'<line x1="{x0+13:.1f}" y1="{ly:.1f}" x2="{x0+13+lw:.1f}" y2="{ly:.1f}" '
            f'stroke="{colour}" stroke-width="2" opacity="0.55" stroke-linecap="round"/>'
        )
        if not dashed and i in (1, 3):
            g.append(
                f'<rect x="{x0+13+lw*0.55:.1f}" y="{ly-4:.1f}" width="{lw*0.28:.1f}" height="8" '
                f'rx="2" fill="{colour}" opacity="0.95"/>'
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
    f'A 95,000-line app retired; a small Python core and a</text>')
add(f'<text x="{X}" y="457" font-family="{SANS}" font-size="17" fill="#c4cad8">'
    f'Claude skill rebuilt the method, checked, in a day.</text>')
add(f'<text x="{X}" y="507" font-family="{MONO}" font-size="15" fill="{TEAL}">'
    f'moral: retire(tool); keep(method)  # same or better</text>')

# footer
add(f'<text x="{X}" y="599" font-family="{SANS}" font-size="14" font-weight="bold" '
    f'fill="{AMBER}">SJP Consulting</text>')
add(f'<text x="{X+123}" y="599" font-family="{SANS}" font-size="14" fill="{DIM}">'
    f'&#183;  CBL Analytics</text>')

# right side: tool-chain chips
cw, ch, gap, cx0, cy0 = 88, 50, 12, 700, 240
for i, (lab, sub, col) in enumerate([
        ("SEC", "edgartools", TEAL),
        ("PYTHON", "core + tests", INDIGO),
        ("CLAUDE", "prose slots", PINK),
        ("GATE", "my sign-off", AMBER)]):
    add(chip(cx0 + i * (cw + gap), cy0, cw, ch, lab, sub, col))

add(f'<line x1="{cx0}" y1="{cy0+ch+14}" x2="{cx0+4*cw+3*gap}" y2="{cy0+ch+14}" '
    f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')
for i in range(4):
    x = cx0 + i * (cw + gap) + cw / 2
    add(f'<line x1="{x}" y1="{cy0+ch}" x2="{x}" y2="{cy0+ch+14}" '
        f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')

# filings on the ridge: the retired app faded and dashed, the method and the rebuild bright
add(filing(1100, 545, 92, INDIGO, opacity=0.45, dashed=True))
add(filing(958, 550, 118, PINK, opacity=0.9))
add(filing(800, 544, 150, TEAL, opacity=1.0))

add(tag(800, 566, "method: kept", TEAL))
add(tag(958, 566, "engine: rebuilt", PINK))
add(tag(1100, 566, "app.v1: retired", INDIGO))

add("</svg>")

svg = "".join(p)
os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_SVG, "w", encoding="utf-8") as f:
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
