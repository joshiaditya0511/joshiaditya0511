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
    },
    "dark": {
        "text": "#e6edf3",
        "muted": "#9198a1",
        "border": "#3d444d",
        "surface": "#151b23",
        "accent": "#f0883e",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def banner(c):
    # Right side: a small terminal card that says what I do and what I'm building.
    x, y, w, h = 575, 56, 385, 238
    lines = [
        ("cmd", "whoami"),
        ("out", "product manager @ revcloud"),
        ("cmd", "cat now.txt"),
        ("out", "building alyson.ai, which tests"),
        ("out", "landing pages on live traffic"),
        ("cmd", ""),
    ]
    body = ""
    for i, (kind, text) in enumerate(lines):
        ly = y + 66 + i * 30
        delay = 0.3 + i * 0.35
        if kind == "cmd":
            body += (
                f'<text class="line" style="animation-delay:{delay:.2f}s" x="{x + 22}" y="{ly}" font-family="{MONO}" font-size="16">'
                f'<tspan fill="{c["accent"]}" font-weight="700">$ </tspan><tspan fill="{c["text"]}">{text}</tspan></text>'
            )
        else:
            body += (
                f'<text class="line" style="animation-delay:{delay:.2f}s" x="{x + 22}" y="{ly}" font-family="{MONO}" font-size="16" fill="{c["muted"]}">{text}</text>'
            )
    cursor_y = y + 66 + (len(lines) - 1) * 30
    cursor = f'<rect class="cursor" x="{x + 42}" y="{cursor_y - 14}" width="9" height="18" fill="{c["accent"]}"/>'
    dots = "".join(
        f'<circle cx="{x + 20 + i * 18}" cy="{y + 18}" r="5.5" fill="{color}"/>'
        for i, color in enumerate(("#ff5f57", "#febc2e", "#28c840"))
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-labelledby="title desc">
  <title id="title">Aditya Joshi</title>
  <desc id="desc">Product Manager by day. AI builder by habit. A terminal card reads: whoami, product manager at Revcloud; now, building alyson.ai, which tests landing pages on live traffic.</desc>
  <style>
    .line {{ animation: type-in 0.4s ease-out both; }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes type-in {{ from {{ opacity: 0; transform: translateX(-6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .line, .cursor {{ animation: none; }}
    }}
  </style>

  <text x="40" y="92" font-family="{MONO}" font-size="17" font-weight="600" letter-spacing="2" fill="{c['accent']}">PRODUCT MANAGER · REVCLOUD</text>
  <text x="38" y="166" font-family="{SANS}" font-size="70" font-weight="700" fill="{c['text']}">Aditya Joshi</text>
  <text x="40" y="218" font-family="{SANS}" font-size="31" fill="{c['text']}">Product Manager by day.</text>
  <text x="40" y="258" font-family="{SANS}" font-size="31" fill="{c['muted']}">AI builder by habit.</text>

  <g>
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c['surface']}" stroke="{c['border']}" stroke-width="1.5"/>
    <path d="M{x} {y + 36} H{x + w}" stroke="{c['border']}" stroke-width="1.5"/>
    {dots}
    <text x="{x + w / 2 + 20}" y="{y + 23}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c['muted']}">aditya@pune: ~</text>
    {body}
    {cursor}
  </g>
</svg>
"""


def stats(c):
    tiles = [
        ("400K+", "visits routed", "by Alyson's router"),
        ("$175K+", "in revenue", "from internal lead gen"),
        ("Jun '26", "promoted to PM", "from Data Scientist"),
    ]
    w, h, gap = 276, 130, 24
    x0 = (900 - (3 * w + 2 * gap)) / 2
    body = ""
    for i, (big, label, sub) in enumerate(tiles):
        x = x0 + i * (w + gap)
        body += f"""
  <g>
    <rect x="{x}" y="10" width="{w}" height="{h}" rx="14" fill="{c['surface']}" stroke="{c['border']}" stroke-width="1.5"/>
    <rect x="{x + 22}" y="28" width="24" height="4" rx="2" fill="{c['accent']}"/>
    <text x="{x + 22}" y="74" font-family="{SANS}" font-size="38" font-weight="700" fill="{c['text']}">{big}</text>
    <text x="{x + 22}" y="104" font-family="{SANS}" font-size="19" font-weight="600" fill="{c['text']}">{label}</text>
    <text x="{x + 22}" y="128" font-family="{SANS}" font-size="16" fill="{c['muted']}">{sub}</text>
  </g>"""
    desc = "; ".join(f"{b} {l} {s}" for b, l, s in tiles)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 150" width="900" height="150" role="img" aria-labelledby="title desc">
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
