# Technology Stack — GitHub Profile README

**Project:** joshiaditya0511 GitHub Profile README
**Researched:** 2026-04-21
**Research mode:** Ecosystem

---

> **Verification notice:** Web access (WebSearch, WebFetch, Bash/CLI) was unavailable during this
> research session. All entries below are drawn from training-data knowledge (cutoff Aug 2025);
> current date is Apr 2026 (~8 months delta). Each entry carries an explicit confidence flag.
> Run the [Verification Checklist](#verification-checklist) before implementing any service.

---

## Recommended Stack

| Service | Purpose | Confidence |
|---------|---------|-----------|
| `readme-typing-svg` (demolab.com) | Animated typing header — role cycling | HIGH |
| `shields.io` + simple-icons | Tech stack badges with logos | HIGH |
| `capsule-render` (Vercel) | Decorative wave/header/footer banners | MEDIUM |
| `Platane/snk` (GitHub Action) | Contribution snake animation | MEDIUM |
| `skill-icons` (skillicons.dev) | Alternative to shields badges — colorful tech icons | MEDIUM |

---

## 1. readme-typing-svg

**Repo:** `DenverCoder1/readme-typing-svg`
**Canonical endpoint:** `https://readme-typing-svg.demolab.com/`
**Confidence:** HIGH

### Background

The original service ran on Heroku free tier (`readme-typing-svg.herokuapp.com`). That endpoint
is **dead** — Heroku eliminated free dynos in November 2022. The canonical URL since then is
`readme-typing-svg.demolab.com`. Any tutorial still pointing to the Heroku URL will silently 404.

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `font` | Font family | `Fira+Code`, `JetBrains+Mono` |
| `size` | Font size (px) | `22` |
| `pause` | Pause duration between strings (ms) | `1000` |
| `color` | Text color (hex, no `#`) | `58A6FF` |
| `background` | Background color or `00000000` for transparent | `00000000` |
| `width` | SVG width (px) | `500` |
| `height` | SVG height (px) | `50` |
| `lines` | Semicolon-separated strings to cycle | `Data+Scientist%3BML+Engineer` |
| `center` | Center-align text | `true` |
| `vCenter` | Vertical center text | `true` |
| `repeat` | Loop animation | `true` |
| `duration` | Per-character typing speed (ms) | `50` |

**URL encoding note:** Semicolons (`;`) separating lines must be `%3B`, not raw `;`.
Spaces are `+`. Pipe `|` is `%7C`.

### Working Example — This Project

```markdown
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=58A6FF&background=00000000&center=true&vCenter=true&width=500&height=50&lines=Data+Scientist%3BML+Engineer%3BFull-Stack+Developer)](https://git.io/typing-svg)
```

Decoded strings: `Data Scientist | ML Engineer | Full-Stack Developer`

### Dark-Theme Config

- `background=00000000` — fully transparent, renders over GitHub's dark background
- `color=58A6FF` — GitHub's blue accent on dark theme; alternatives: `79C0FF` (bright blue), `56D364` (green), `F78166` (red-orange)

### Reliability: HIGH

Self-hosted on DemoLab infrastructure; no commercial dependency. Has been stable since the
Heroku migration. The project is actively maintained with a visual editor at
`readme-typing-svg.demolab.com/demo/`.

---

## 2. shields.io + simple-icons

**Endpoint:** `https://img.shields.io/badge/`
**Confidence:** HIGH

### Badge URL Structure

```
https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>?style=<STYLE>&logo=<ICON>&logoColor=<COLOR>
```

- `LABEL` — left side text (can be empty: `--` gives no label)
- `MESSAGE` — right side text (the technology name)
- `COLOR` — right side background color (hex without `#`, or named: `blue`, `green`, etc.)
- `style` — `flat`, `flat-square`, `for-the-badge`, `plastic`, `social`
- `logo` — icon slug from [simple-icons.org](https://simpleicons.org/) or custom base64
- `logoColor` — icon color (hex without `#`, or `white`, `black`)

### Recommended Style for This Project

`style=for-the-badge` — bold, high-contrast, most visually impressive on dark backgrounds.
`logoColor=white` — universally readable on any badge color.

### Simple-Icons Coverage for This Stack

| Technology | simple-icons slug | Brand Color | Confidence |
|------------|------------------|-------------|-----------|
| Python | `python` | `3776AB` | HIGH |
| React | `react` | `61DAFB` | HIGH |
| FastAPI | `fastapi` | `009688` | HIGH |
| Astro | `astro` | `FF5D01` | HIGH |
| Docker | `docker` | `2496ED` | HIGH |
| Amazon AWS | `amazonaws` | `FF9900` | HIGH |
| Vercel | `vercel` | `000000` | HIGH |
| Pandas | `pandas` | `150458` | HIGH |
| NumPy | `numpy` | `013243` | HIGH |
| scikit-learn | `scikitlearn` | `F7931E` | HIGH |
| Selenium | `selenium` | `43B02A` | HIGH |
| OpenCV | `opencv` | `5C3EE8` | HIGH |
| Jupyter | `jupyter` | `F37626` | HIGH |
| PostgreSQL | `postgresql` | `4169E1` | HIGH |
| Git | `git` | `F05032` | HIGH |
| VS Code | `visualstudiocode` | `007ACC` | HIGH |
| ONNX | `onnx` | `005CED` | MEDIUM — slug may be `onnx`; verify at simpleicons.org |
| Amazon SageMaker | `amazonsagemaker` | `FF9900` | LOW — likely no dedicated icon; falls back to generic AWS |
| LightGBM | `lightgbm` | — | LOW — niche ML lib, unlikely to have a simple-icons entry |
| TesseractOCR | `tesseract` | — | LOW — niche OCR lib, unlikely to have a simple-icons entry |

### Fallback for Missing Icons

For technologies without simple-icons entries, use one of:

**Option A — Custom SVG base64 logo:**
```
&logo=data:image/svg+xml;base64,<BASE64_ENCODED_SVG>
```

**Option B — Text-only badge (no logo):**
```
https://img.shields.io/badge/LightGBM-Model-brightgreen?style=for-the-badge
```

**Option C — Use the parent brand:**
For SageMaker, use the AWS logo (`logo=amazonaws`).

### Working Examples — This Project

```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Astro](https://img.shields.io/badge/Astro-FF5D01?style=for-the-badge&logo=astro&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
```

### Dark-Theme Config

On dark backgrounds, prefer badge colors that use the technology's own brand color (dark or
saturated), with `logoColor=white`. Avoid very light badge colors (`&color=lightgrey`) — they
disappear on GitHub's dark theme `#0d1117` background.

### Reliability: HIGH

shields.io is one of the most stable CDN services in the open-source ecosystem. It is backed by
a nonprofit (badge.design foundation equivalent) and has served billions of badges for a decade.
Simple-icons is similarly mature. Occasional brief outages occur but recovery is fast.

---

## 3. capsule-render

**Repo:** `kyechan99/capsule-render`
**Canonical endpoint:** `https://capsule-render.vercel.app/api`
**Confidence:** MEDIUM

### Background

Capsule-render generates decorative wave, egg, shark, cylinder, and other SVG banners — commonly
used as animated top-of-README headers and bottom footers. It is hosted on Vercel's free tier,
which means cold-start latency is possible and reliability is dependent on Vercel's free plan
policies (which have changed over time).

**Reliability flag:** This is the flakiest service in the stack. Vercel free-tier cold starts can
cause 2-5 second load delays. There have been periodic outages and the maintainer is a solo
developer. Verify the endpoint is live before implementing.

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `type` | Banner shape | `waving`, `rect`, `egg`, `shark`, `cylinder`, `soft` |
| `color` | Background color or gradient | `0:EEFF00,100:a82da8` (gradient) or `timeAuto` (time-based) |
| `height` | Banner height (px) | `200` |
| `section` | Position | `header` (waves down), `footer` (waves up) |
| `text` | Text overlaid on banner | `Hi%20there` |
| `fontColor` | Text color (hex, no `#`) | `FFFFFF` |
| `fontSize` | Font size | `40` |
| `animation` | Text animation | `twinkling`, `fadeIn`, `blinking`, `scaleIn` |
| `fontAlignX` | Horizontal text position (%) | `50` |
| `fontAlignY` | Vertical text position (%) | `40` |
| `rotate` | Text rotation (degrees) | `13` |
| `desc` | Subtitle text | `Data+Scientist` |
| `descAlignX` | Subtitle horizontal position (%) | `50` |
| `descAlignY` | Subtitle vertical position (%) | `60` |

### Working Examples — This Project

Header wave banner (dark gradient):
```markdown
![header](https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:1a1b27&height=200&section=header&text=Aditya%20Joshi&fontColor=58A6FF&fontSize=50&animation=fadeIn&fontAlignY=40&desc=Data%20Scientist%20%7C%20ML%20Engineer%20%7C%20Full-Stack%20Dev&descAlignY=60&descAlignX=50)
```

Footer wave (no text):
```markdown
![footer](https://capsule-render.vercel.app/api?type=waving&color=0:1a1b27,100:0d1117&height=100&section=footer)
```

### Dark-Theme Config

- `color=0:0d1117,100:1a1b27` — gradient from GitHub dark bg (`#0d1117`) to a slightly lighter
  dark (`#1a1b27`), a common pairing used in profile READMEs
- `fontColor=58A6FF` — matches the typing-SVG accent color for visual coherence

### Reliability: MEDIUM

Hosted on Vercel free tier — cold starts are possible. The service has been running since ~2021.
As of training cutoff (Aug 2025), the repo was still active. In 2026 this should be verified
before use. See Verification Checklist below.

---

## 4. Platane/snk — Snake Contribution Animation

**Repo:** `Platane/snk`
**Type:** GitHub Actions workflow (NOT a URL service — must be set up per-repo)
**Confidence:** MEDIUM (workflow setup), HIGH (concept)

### Background

The snake animation reads the GitHub contribution graph grid and generates an SVG of a snake
"eating" the contribution squares. It is implemented as a GitHub Action that:
1. Runs on schedule (or manual trigger)
2. Writes SVG output files to a branch (e.g., `output` branch)
3. README references the raw GitHub URL to the SVG on that branch

This means there is no external service to depend on — the SVG is served from GitHub itself
(via raw.githubusercontent.com or github.io), which is maximally reliable.

### Setup: GitHub Actions Workflow

Create `.github/workflows/snake.yml` in the profile repo:

```yaml
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 */12 * * *"  # every 12 hours
  workflow_dispatch:  # allow manual trigger

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: Push snake to output branch
        uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### README Reference

After the workflow runs and pushes to the `output` branch:

```markdown
![Snake animation](https://raw.githubusercontent.com/joshiaditya0511/joshiaditya0511/output/github-contribution-grid-snake-dark.svg)
```

Or via GitHub Pages if enabled:
```markdown
![Snake animation](https://joshiaditya0511.github.io/joshiaditya0511/github-contribution-grid-snake-dark.svg)
```

### Key Notes

- Use `svg-only@v3` (not the full `snk@v3`) — lighter action, just the SVG generator
- Use `?palette=github-dark` output variant for dark theme
- The `crazy-max/ghaction-github-pages` action version should be checked; `@v3` was current as of
  training cutoff but may have a newer version
- Repo must have Actions enabled and the `GITHUB_TOKEN` permissions set to allow writes

### Reliability: HIGH (once set up)

Since the SVG is served from GitHub's own raw file hosting, rendering reliability is as good as
GitHub itself. The only failure mode is if the Action stops running (e.g., GitHub disables
scheduled workflows on inactive repos — push a commit every few months or use workflow_dispatch).

---

## 5. skill-icons (Alternative to shields.io)

**Repo:** `tandpfun/skill-icons`
**Canonical endpoint:** `https://skillicons.dev/icons?i=<comma-separated-slugs>`
**Confidence:** MEDIUM

### Background

Skill-icons renders a row of colored circular/square icons for technology logos. It produces a
single SVG URL that displays multiple icons in a clean grid, which is a popular alternative to
individual shields.io badges when you want a denser visual display.

**Note for this project:** PROJECT.md specifies "shields.io badge icons" explicitly. Skill-icons
is documented here as an alternative — consider it for a supplemental "Also proficient in" row
of minor tools rather than the primary tech stack display.

### URL Structure

```
https://skillicons.dev/icons?i=python,react,fastapi,docker,aws&theme=dark&perline=8
```

| Parameter | Description | Example |
|-----------|-------------|---------|
| `i` | Comma-separated icon slugs | `python,react,fastapi` |
| `theme` | `dark` or `light` | `dark` |
| `perline` | Icons per row | `8` |

### Coverage for This Stack

Common slugs that work: `python`, `react`, `fastapi`, `astro`, `docker`, `aws`, `vercel`,
`sklearn` (scikit-learn), `opencv`, `selenium`, `git`, `github`, `postgres`, `vscode`

Less certain: `pandas` (may not exist), `lightgbm` (likely absent), `sagemaker` (likely absent)

### Working Example

```markdown
[![My Skills](https://skillicons.dev/icons?i=python,react,fastapi,astro,docker,aws&theme=dark)](https://skillicons.dev)
```

### Reliability: MEDIUM

Community-maintained, single-developer project. Has been stable but has fewer guarantees than
shields.io. The Vercel deployment has good uptime historically.

---

## Explicitly Excluded Services

Per PROJECT.md `Out of Scope` — these should NOT be added to the README:

| Service | Why Excluded |
|---------|-------------|
| `anuraghazra/github-readme-stats` | Stats cards excluded — user wants badge-only, no live stat widgets |
| `DenverCoder1/github-readme-streak-stats` | Streak counters excluded |
| `ryo-ma/github-profile-trophy` | Trophy cards excluded |
| `lowlighter/metrics` | Full metrics report card — too heavy, excluded |

---

## Quick Dark-Theme Color Reference

GitHub's dark mode background is `#0d1117`. These accent colors work well over it:

| Color | Hex | Use |
|-------|-----|-----|
| GitHub blue | `58A6FF` | Primary accent (links, typing text) |
| Bright blue | `79C0FF` | Emphasis |
| Green (merged/success) | `56D364` | Positive status |
| Orange | `E3B341` | Warning / highlights |
| Red-orange | `F78166` | Danger / featured |
| Purple | `BC8CFF` | Accent variation |

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Typing animation | readme-typing-svg (demolab) | github-readme-typing (other forks) | DenverCoder1 is the canonical, most maintained version |
| Tech badges | shields.io + simple-icons | skill-icons | User specified shields.io; more customizable for dark theme |
| Snake animation | Platane/snk | manual GIF | snk produces clean SVG, no external hosting needed |
| Header banner | capsule-render | Static PNG header | capsule-render is animated and parameterized; lower maintenance |
| Header banner | capsule-render | readme-typing-svg for header text | Can combine both — capsule for background, typing-svg for text |

---

## Verification Checklist

Run these checks before implementing any service (can be done in a browser in 2 minutes):

1. **readme-typing-svg endpoint:**
   Open `https://readme-typing-svg.demolab.com/?lines=Test&color=58A6FF` in browser.
   Expected: animated SVG renders. If 404/error, the service URL has changed — check
   `github.com/DenverCoder1/readme-typing-svg` for current endpoint.

2. **capsule-render endpoint:**
   Open `https://capsule-render.vercel.app/api?type=waving&color=auto&height=100` in browser.
   Expected: SVG wave renders. This is the flakiest service — if it fails to load within 5s,
   it may be cold-starting or down. Check `github.com/kyechan99/capsule-render/issues` for
   active outage reports.

3. **snk action version:**
   Visit `github.com/Platane/snk/releases` — confirm `v3` is still the latest release tag.
   Check `crazy-max/ghaction-github-pages/releases` — confirm the version used in the workflow.

4. **simple-icons slugs (ML-specific):**
   Visit `simpleicons.org` and search for: `onnx`, `lightgbm`, `sagemaker`, `tesseract`.
   Missing slugs → use text-only badges for those technologies (Option B fallback above).

5. **skill-icons (if used):**
   Open `https://skillicons.dev/icons?i=python,react,sklearn&theme=dark` in browser.
   Expected: icon row renders. Also check `github.com/tandpfun/skill-icons` last commit date.

---

## Sources

- Training data knowledge (cutoff Aug 2025) — MEDIUM to HIGH confidence for stable services
- `github.com/DenverCoder1/readme-typing-svg` — endpoint migration (Heroku → DemoLab) is well-documented
- `shields.io` documentation — badge URL format is stable for years
- `github.com/kyechan99/capsule-render` — service and parameter reference
- `github.com/Platane/snk` — GitHub Actions workflow pattern
- `simpleicons.org` — icon slug reference (verify ML-specific slugs before use)
