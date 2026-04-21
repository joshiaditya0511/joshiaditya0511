# Research Summary — joshiaditya0511 GitHub Profile README

**Synthesized:** 2026-04-21
**Research coverage:** STACK.md, FEATURES.md, ARCHITECTURE.md, PITFALLS.md, PROJECT.md

> **Research caveat:** Web access was unavailable during research. All service availability and slug data is drawn from training knowledge (cutoff Aug 2025, ~8 months delta). Verify service URLs and simple-icons slugs in browser before implementing.

---

## 1. Recommended Tech Stack / Services

| Service | Purpose | Confidence | Caveat |
|---------|---------|-----------|--------|
| readme-typing-svg (demolab.com) | Animated role-cycling header | HIGH | Use demolab.com endpoint only — old herokuapp.com is dead |
| shields.io + simple-icons | Tech stack badges (all sections) | HIGH | Verify every `logo=` slug against simpleicons.org — ML-specific slugs are unreliable |
| Pure HTML/Markdown | Bio, role callout, project cards, social links | N/A | No external dependency; use `div align=center`, `table`, `td` — never `style=` attributes |

**Considered but outside current scope:**

| Service | Status | Note |
|---------|--------|------|
| capsule-render (Vercel) | Deferred | MEDIUM reliability — Vercel free tier, solo maintainer. Add as polish only if endpoint verifies live |
| Platane/snk (snake animation) | Deferred | Requires GitHub Actions setup. Strong differentiator but not in Active spec |
| skillicons.dev | Deferred | Alternative icon grid; not in scope per project decision |

**Explicitly excluded:** github-readme-stats, streak counters, trophy cards — no live stat widgets.

---

## 2. Key Features

### Table Stakes (must have)

| Feature | Implementation |
|---------|---------------|
| Descriptive header | Animated typing SVG cycling 3 roles |
| Current role / affiliation | Plain bold text — Revcloud (Data Scientist) + Forengers (Tech Head) |
| Tech stack display | shields.io `for-the-badge` badges grouped by category |
| Featured projects with links | 2-column HTML table — PuneProp Predict + Karnataka Elections Analysis |
| Social / contact links | Badge-style links — personal site, LinkedIn, email |
| Visual hierarchy | Section headers, centered div blocks, horizontal rules |

### Chosen Differentiators

| Feature | Why It Works | Implementation |
|---------|-------------|---------------|
| Animated typing SVG header | Motion signals intentionality; role cycling communicates hybrid identity | readme-typing-svg, 3 roles, chosen accent color |
| Dark-theme-consistent badge palette | Most devs miss this; few profiles get it right | Saturated brand colors + `logoColor=white` throughout |
| Custom project cards | Tells a story — description, stack, live link; auto-pins don't do this | 2-column HTML table, `flat-square` badges inside, live URLs |
| Structured short bio with personality | Specific true detail beats generic filler | 3 lines max; intersection statement + one personal note |
| Notes/resources callout | Signals intellectual generosity beyond job-seeking | Badge-link to DS/ML notes repo |
| Consistent visual accent color | Single hex propagated everywhere signals intentionality | Root dependency — decide first |

### Anti-Features (actively avoided)

- GitHub stats cards / streak counters — excluded in PROJECT.md
- Visitor counter badge
- Wall-of-badges (40+ ungrouped) — cap each category at 6–8 badges
- Multiple typing SVGs on one page
- Generic filler ("coffee + coding" clichés)
- Emoji overload — 1 per section header max
- Spotify / Wakatime widgets

---

## 3. Layout / Section Order

Ordering follows recruiter-and-developer attention arc: identity → proof → discovery → exit.

1. **Animated Header (typing SVG)** — full width, centered; 3 roles cycling: Data Scientist / ML Engineer / Full-Stack Developer
2. **Bio + Current Role Callout** — 3–5 lines max, centered; intersection statement + Revcloud + Forengers
3. **Tech Stack Badges** — grouped by category, 6–8 per group; groups: ML/Data Science | Web & Backend | Cloud & DevOps | Tools; style: `for-the-badge`
4. **Featured Projects** — 2-column HTML table (flush-left `td` tags, blank line after `td` opening, `flat-square` style inside); Card 1: PuneProp Predict; Card 2: Karnataka Elections Analysis
5. **Notes / Resources Callout** — short centered block, badge-link to DS/ML notes repo
6. **Social / Contact Footer** — badge row: personal site, LinkedIn, email

**Key build constraint:** Accent color hex must be decided first — it propagates to typing-SVG `color=` and every shields.io `color=` param.

**Critical HTML gotcha:** `<td>` tags must be flush-left (no indentation) and Markdown inside `<td>` needs a blank line after the opening tag. Indented tags render content as a code block.

---

## 4. Top 5 Pitfalls

| # | Pitfall | Prevention |
|---|---------|------------|
| 1 | **Dark/light SVG background clash** | Set `background=transparent` on typing SVG. Test both GitHub themes before publishing. |
| 2 | **Typing SVG URL encoding errors** | Generate URL from demolab builder; test raw SVG URL in browser tab before embedding. |
| 3 | **Simple-icons slug drift** | Verify every `logo=` at simpleicons.org. At-risk: `onnx`, `lightgbm` (likely absent), `amazonsagemaker`, `scikitlearn` (no hyphen). |
| 4 | **GitHub sanitizer strips `style=`** | Never use `style=` on any element. Use only `align=` on `div`/`p`/`td`. Preview on actual GitHub, not local previewer. |
| 5 | **Badge overcrowding** | Cap each category at 6–8 badges (30 total max). Only include techs from featured projects or current work. |

---

## 5. Open Decisions

Resolve before or during implementation, in priority order.

| # | Decision | Options | Blocker For |
|---|---------|---------|------------|
| 1 | **Accent color hex** | `58A6FF` (GitHub blue), `00D9FF` (cyan), `56D364` (green), or custom | Everything — lock this first |
| 2 | **Badge style split** | `for-the-badge` for standalone rows; `flat-square` inside project card `td` | Consistency across all badge URLs |
| 3 | **ML-specific slug verification** | Browser-check: `onnx`, `lightgbm`, `tesseract`, `amazonsagemaker` at simpleicons.org | Tech stack + project card badges |
| 4 | **DS/ML notes repo URL** | Confirm repo name and public status | Notes/Resources callout section |
| 5 | **Bio exact wording** | Draft: intersection statement + one specific personal detail, 3 lines max | Bio section |
| 6 | **Capsule-render wave dividers** | Include if endpoint verifies live; skip if adds maintenance risk | Visual polish only — not blocking |
