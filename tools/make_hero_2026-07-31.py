#!/usr/bin/env python3
"""
Hero banner generator for cblanalytics.com posts.

House theme (extracted from the Feb/Jun 2026 heroes):
  bg            #10121f  dark navy
  grid          #171a27
  purple title  #a78bfa
  white title   #ffffff
  muted         #8b93b8
  amber         #fbbf24
  teal          #2dd4bf
  pink          #f472b6
  indigo        #818cf8
  ridge         layered dark purple silhouette across the bottom

Renders 1200x630 (Open Graph / Quarto listing card ratio).
"""

import math
import cairosvg

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

import os
VARIANT = os.environ.get("VARIANT", "a")
T1 = "Financial Modelling"
T2 = {"a": "builds automated", "b": "Automated Builds"}[VARIANT]
STRAP = "with Python, Excel and a little AI"
OUT = f"hero_{VARIANT}.png"

p = []          # svg fragments
add = p.append


# ---------------------------------------------------------------- turbines
def turbine(cx, ground, height, rotor, colour, phase=0.0, opacity=1.0):
    """A schematic three-blade turbine standing on `ground`.

    cx      tower centreline
    height  hub height above ground
    rotor   blade length from hub
    phase   rotor rotation in degrees
    """
    hub_y = ground - height
    base_w, top_w = height * 0.021, height * 0.011
    g = [f'<g opacity="{opacity}">']

    # tapered tower
    g.append(
        f'<path d="M {cx-base_w:.1f} {ground:.1f} '
        f'L {cx-top_w:.1f} {hub_y:.1f} L {cx+top_w:.1f} {hub_y:.1f} '
        f'L {cx+base_w:.1f} {ground:.1f} Z" fill="{colour}" opacity="0.85"/>'
    )
    # footing
    g.append(
        f'<rect x="{cx-base_w*3.4:.1f}" y="{ground-1.6:.1f}" '
        f'width="{base_w*6.8:.1f}" height="3" rx="1.5" '
        f'fill="{colour}" opacity="0.45"/>'
    )

    # three tapered blades at 120 degrees
    for i in range(3):
        a = math.radians(phase + i * 120)
        ca, sa = math.cos(a), math.sin(a)

        def pt(u, v):
            # u along the blade axis, v perpendicular
            return (cx + u * ca - v * sa, hub_y + u * sa + v * ca)

        root_w, mid_w, tip = rotor * 0.036, rotor * 0.055, rotor * 0.010
        a1 = pt(rotor * 0.06, -root_w)
        a2 = pt(rotor * 0.34, -mid_w)
        a3 = pt(rotor * 0.99, -tip)
        b3 = pt(rotor * 0.99, tip)
        b2 = pt(rotor * 0.40, root_w * 0.55)
        b1 = pt(rotor * 0.06, root_w * 0.55)
        c1 = pt(rotor * 0.68, -mid_w * 0.85)   # control points
        c2 = pt(rotor * 0.70, tip * 2.2)
        g.append(
            f'<path d="M {a1[0]:.1f} {a1[1]:.1f} '
            f'Q {a2[0]:.1f} {a2[1]:.1f} {c1[0]:.1f} {c1[1]:.1f} '
            f'L {a3[0]:.1f} {a3[1]:.1f} L {b3[0]:.1f} {b3[1]:.1f} '
            f'Q {c2[0]:.1f} {c2[1]:.1f} {b2[0]:.1f} {b2[1]:.1f} '
            f'L {b1[0]:.1f} {b1[1]:.1f} Z" fill="{colour}"/>'
        )

    # nacelle + hub
    nl = rotor * 0.115
    g.append(
        f'<rect x="{cx-nl*0.35:.1f}" y="{hub_y-nl*0.30:.1f}" '
        f'width="{nl:.1f}" height="{nl*0.60:.1f}" rx="{nl*0.30:.1f}" '
        f'fill="{colour}"/>'
    )
    g.append(f'<circle cx="{cx:.1f}" cy="{hub_y:.1f}" r="{rotor*0.052:.1f}" fill="{BG}"/>')
    g.append(f'<circle cx="{cx:.1f}" cy="{hub_y:.1f}" r="{rotor*0.028:.1f}" fill="{colour}"/>')
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

# faint grid
for x in range(0, W + 1, 60):
    add(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{GRID}" stroke-width="1"/>')
for y in range(0, H + 1, 60):
    add(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{GRID}" stroke-width="1"/>')

# ---------------------------------------------------------------- ridge
add(f'<rect x="0" y="380" width="{W}" height="250" fill="url(#glow)"/>')
# far ridge - the turbines stand on this one
add('<path d="M 0 588 L 210 578 L 400 586 L 560 566 L 700 556 L 800 543 '
    f'L 900 553 L 985 541 L 1080 546 L 1200 533 L 1200 630 L 0 630 Z" '
    f'fill="#2e2149" opacity="0.85"/>')
# near ridge - overlaps the tower feet for depth
add('<path d="M 0 610 L 260 600 L 520 608 L 700 592 L 880 601 L 1040 588 '
    f'L 1200 596 L 1200 630 L 0 630 Z" fill="#1b1530" opacity="0.95"/>')

# ---------------------------------------------------------------- frame
add(f'<path d="M 34 52 L 34 22 L 64 22" fill="none" stroke="{PURPLE}" '
    f'stroke-width="1.6" opacity="0.75"/>')
add(f'<line x1="80" y1="101" x2="1120" y2="101" stroke="url(#rule)" stroke-width="1.8"/>')
add(f'<circle cx="243" cy="74" r="3.4" fill="{TEAL}"/>')
add(f'<circle cx="544" cy="91" r="3.4" fill="{PINK}"/>')
add(f'<circle cx="1082" cy="76" r="3.0" fill="{MUTED}" opacity="0.8"/>')
add(f'<circle cx="578" cy="482" r="3.2" fill="{AMBER}"/>')

# ---------------------------------------------------------------- copy
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
    f'One spec generates the workbook, the engine and the</text>')
add(f'<text x="{X}" y="457" font-family="{SANS}" font-size="17" fill="#c4cad8">'
    f'report &#8212; and they reconcile.</text>')
add(f'<text x="{X}" y="507" font-family="{MONO}" font-size="15" fill="{TEAL}">'
    f'moral: regenerate(spec) == model  # every time</text>')

# footer
add(f'<text x="{X}" y="599" font-family="{SANS}" font-size="14" font-weight="bold" '
    f'fill="{AMBER}">SJP Consulting</text>')
add(f'<text x="{X+123}" y="599" font-family="{SANS}" font-size="14" fill="{DIM}">'
    f'&#183;  CBL Analytics</text>')

# ---------------------------------------------------------------- right side
cw, ch, gap, cx0, cy0 = 88, 50, 12, 700, 240
for i, (lab, sub, col) in enumerate([
        ("SPEC", "one yaml", TEAL),
        ("EXCEL", "workbook", INDIGO),
        ("PYTHON", "engine", PINK),
        ("REPORT", "quarto", AMBER)]):
    add(chip(cx0 + i * (cw + gap), cy0, cw, ch, lab, sub, col))

# connector rail under the chips
add(f'<line x1="{cx0}" y1="{cy0+ch+14}" x2="{cx0+4*cw+3*gap}" y2="{cy0+ch+14}" '
    f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')
for i in range(4):
    x = cx0 + i * (cw + gap) + cw / 2
    add(f'<line x1="{x}" y1="{cy0+ch}" x2="{x}" y2="{cy0+ch+14}" '
        f'stroke="{MUTED}" stroke-width="1" opacity="0.35"/>')

# turbines on the ridge
add(turbine(1088, 545, 74,  32, INDIGO, phase=-112, opacity=0.48))
add(turbine(958,  550, 100, 44, PINK,   phase=-68,  opacity=0.85))
add(turbine(800,  544, 132, 58, TEAL,   phase=-90,  opacity=1.0))

add(tag(800, 566, "asset.type: wind", TEAL))
add(tag(963, 566, "asset.type: solar", PINK))
add(tag(1113, 566, "asset.type: ...", INDIGO))

add("</svg>")

svg = "".join(p)
with open(OUT.replace(".png",".svg"), "w") as f:
    f.write(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT,
                 output_width=W, output_height=H)
print("wrote", OUT)
