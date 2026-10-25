"""Generate the light and dark SVGs used in README.md.

Run from the repo root:  python scripts/build_svgs.py
Each visual is written twice (assets/<name>-light.svg, assets/<name>-dark.svg)
so README <picture> tags can follow the viewer's GitHub theme.
"""

from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

# GitHub Primer colors, so the SVGs sit naturally on github.com in either theme.
THEMES = {
    "light": {
        "text": "#1f2328",
        "muted": "#59636e",
        "border": "#d0d7de",
        "surface": "#f6f8fa",
        "accent": "#bc4c00",
        "win": "#1a7f37",
        "win_soft": "#dafbe1",
    },
    "dark": {
        "text": "#e6edf3",
        "muted": "#9198a1",
        "border": "#3d444d",
        "surface": "#151b23",
        "accent": "#f0883e",
        "win": "#3fb950",
        "win_soft": "#12261e",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def page_card(x, y, label, c, winner=False):
    """A small landing-page skeleton, one of the variants traffic is routed to."""
    stroke = c["win"] if winner else c["border"]
    fill = c["win_soft"] if winner else c["surface"]
    width = 2.5 if winner else 1.5
    check = ""
    if winner:
        check = (
            f'<circle cx="{x + 100}" cy="{y}" r="12" fill="{c["win"]}"/>'
            f'<path d="M{x + 94} {y} l4 4 l8 -8" fill="none" stroke="#ffffff" '
            f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        )
    return f"""
    <g class="{'winner' if winner else ''}">
      <rect x="{x}" y="{y}" width="100" height="62" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>
      <rect x="{x + 12}" y="{y + 12}" width="44" height="7" rx="3.5" fill="{c['muted']}" opacity="0.7"/>
      <rect x="{x + 12}" y="{y + 27}" width="76" height="5" rx="2.5" fill="{c['border']}"/>
      <rect x="{x + 12}" y="{y + 38}" width="60" height="5" rx="2.5" fill="{c['border']}"/>
      <text x="{x + 88}" y="{y + 54}" text-anchor="end" font-family="{MONO}" font-size="13" font-weight="700" fill="{stroke if winner else c['muted']}">{label}</text>
      {check}
    </g>"""


def banner(c):
    # Router graphic: visitors flow in, the router splits them across page
    # variants, and most traffic ends up on the winning page (B).
    src_y = 175
    router = (700, 150, 80, 50)
    cards = {"A": 72, "B": 144, "C": 216}
    rx, ry, rw, rh = router

    wires = "".join(
        f'<path d="M{rx + rw} {src_y} C{rx + rw + 45} {src_y} {rx + rw + 35} {cy + 31} 850 {cy + 31}" '
        f'fill="none" stroke="{c["win"] if label == "B" else c["border"]}" stroke-width="{2 if label == "B" else 1.5}"/>'
        for label, cy in cards.items()
    )

    # (path, begin offset in seconds): B gets most of the traffic.
    dot_plan = [("B", 0), ("A", 0.6), ("B", 1.2), ("C", 1.8), ("B", 2.4), ("B", 3.0)]
    dots = ""
    for label, begin in dot_plan:
        d = (
            f"M600 {src_y} L{rx + rw} {src_y} "
            f"C{rx + rw + 45} {src_y} {rx + rw + 35} {cards[label] + 31} 850 {cards[label] + 31}"
        )
        color = c["win"] if label == "B" else c["accent"]
        dots += f"""
      <circle class="dot" r="4.5" fill="{color}" opacity="0">
        <animateMotion dur="3.6s" begin="{begin}s" repeatCount="indefinite" path="{d}"/>
        <animate attributeName="opacity" dur="3.6s" begin="{begin}s" repeatCount="indefinite"
                 values="0;1;1;0" keyTimes="0;0.08;0.9;1"/>
      </circle>"""

    cards_svg = "".join(page_card(850, cy, label, c, winner=(label == "B")) for label, cy in cards.items())

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-labelledby="title desc">
  <title id="title">Aditya Joshi</title>
  <desc id="desc">Product Manager by day. AI builder by habit. Product Manager at Revcloud, building Alyson AI. Illustration: website visitors flow through a traffic router to three landing page variants, and most traffic lands on the winning page.</desc>
  <style>
    .winner {{ animation: glow 3.6s ease-in-out infinite; }}
    @keyframes glow {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.82; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .dot {{ display: none; }}
      .winner {{ animation: none; }}
    }}
  </style>

  <text x="40" y="92" font-family="{MONO}" font-size="17" font-weight="600" letter-spacing="2" fill="{c['accent']}">PRODUCT MANAGER · REVCLOUD</text>
  <text x="38" y="166" font-family="{SANS}" font-size="70" font-weight="700" fill="{c['text']}">Aditya Joshi</text>
  <text x="40" y="218" font-family="{SANS}" font-size="31" fill="{c['text']}">Product Manager by day.</text>
  <text x="40" y="258" font-family="{SANS}" font-size="31" fill="{c['muted']}">AI builder by habit.</text>

  <g>
    <text x="600" y="{src_y - 16}" font-family="{MONO}" font-size="13" fill="{c['muted']}">visitors</text>
    <path d="M600 {src_y} L{rx} {src_y}" fill="none" stroke="{c['border']}" stroke-width="1.5" stroke-dasharray="4 5"/>
    {wires}
    {dots}
    <rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="10" fill="{c['surface']}" stroke="{c['accent']}" stroke-width="2"/>
    <text x="{rx + rw / 2}" y="{ry + 30}" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="600" fill="{c['accent']}">router</text>
    {cards_svg}
  </g>
</svg>
"""


def stats(c):
    tiles = [
        ("400K+", "visits routed", "by Alyson's router"),
        ("$175K+", "in revenue", "from internal lead gen"),
        ("Jun '26", "promoted to PM", "from Data Scientist"),
    ]
    w, h, gap = 280, 180, 30
    x0 = (900 - (3 * w + 2 * gap)) / 2
    body = ""
    for i, (big, label, sub) in enumerate(tiles):
        x = x0 + i * (w + gap)
        body += f"""
  <g>
    <rect x="{x}" y="10" width="{w}" height="{h}" rx="14" fill="{c['surface']}" stroke="{c['border']}" stroke-width="1.5"/>
    <rect x="{x + 24}" y="34" width="28" height="5" rx="2.5" fill="{c['accent']}"/>
    <text x="{x + 24}" y="98" font-family="{SANS}" font-size="50" font-weight="700" fill="{c['text']}">{big}</text>
    <text x="{x + 24}" y="136" font-family="{SANS}" font-size="24" font-weight="600" fill="{c['text']}">{label}</text>
    <text x="{x + 24}" y="166" font-family="{SANS}" font-size="18" fill="{c['muted']}">{sub}</text>
  </g>"""
    desc = "; ".join(f"{b} {l} {s}" for b, l, s in tiles)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200" role="img" aria-labelledby="title desc">
  <title id="title">Alyson AI at a glance</title>
  <desc id="desc">{desc}</desc>{body}
</svg>
"""


def main():
    for theme, colors in THEMES.items():
        for name, build in (("banner", banner), ("alyson-stats", stats)):
            out = ASSETS / f"{name}-{theme}.svg"
            out.write_text(build(colors), encoding="utf-8")
            print(f"wrote {out.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
