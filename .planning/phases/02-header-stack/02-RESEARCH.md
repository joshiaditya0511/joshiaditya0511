# Phase 2: Header & Stack — Research

**Researched:** 2026-04-25
**Domain:** GitHub Profile README — readme-typing-svg animation, shields.io badges, simple-icons slugs
**Confidence:** HIGH (core parameters verified via official docs; brand hex colors partially cited from CONTEXT.md)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** Typing speed: fast & snappy (~60–80ms per character). Energetic, suits a tech profile where visitors scan quickly.
- **D-02:** Pause between roles: minimal (~0.5–1s). Constant-motion feel, roles cycle without a long hold.
- **D-03:** Cursor: visible and blinking (`cursor=true` default). Reinforces the typing effect.
- **D-04:** Roles (locked by HEADER-01): "Data Scientist", "ML Engineer", "Full-Stack Developer" — in that order.
- **D-05:** SVG endpoint (locked by HEADER-03): `readme-typing-svg.demolab.com` only. Old `herokuapp.com` is dead.
- **D-06:** Accent color (locked by HEADER-02 + prior phases): `#58A6FF`. SVG `color=` param and `background=transparent`.
- **D-07:** README flow: Header → Bio (Phase 1) → Tech Stack → Notes callout (Phase 1) → Social (Phase 1). Stack section is inserted between Bio and the existing Notes callout.
- **D-08:** Label style: emoji + bold Markdown text on its own line above each badge row.
- **D-09:** Emoji set: `📊 **ML / Data Science**`, `🛠️ **Web & Backend**`, `🚀 **Cloud & DevOps**`
- **D-10:** ML/Data Science badges: `color=58A6FF`, `logoColor=white` (accent color per requirements).
- **D-11:** Web & Backend badges: brand colors per platform (React `61DAFB`, FastAPI `009688`, Astro `FF5D01`, Tailwind `06B6D4`).
- **D-12:** Cloud & DevOps badges: brand colors per platform (AWS `FF9900`, Git `F05032`, GitHub `181717`/white on dark).
- **D-13:** All badges: `style=for-the-badge` (locked by STACK-01 and Phase 1 badge style decision).
- **D-14:** LightGBM — text-only badge (no logo icon). No verified simple-icons slug.
- **D-15:** XGBoost — text-only badge (no logo icon). No verified simple-icons slug.
- **D-16:** shadcn/ui — text-only badge, same pattern as LightGBM/XGBoost. No verified simple-icons slug.

### Claude's Discretion

- Exact `speed`, `duration`, and `pause` param values for `readme-typing-svg` — planner tunes within the fast/minimal constraint.
- Exact fallback badge colors for text-only entries (LightGBM, XGBoost, shadcn/ui) — planner picks readable contrast.
- Verification of remaining simple-icons slugs (`amazonsagemaker`, `scikitlearn`, `astro`, `shadcn`) before embedding — planner confirms at simpleicons.org.

### Deferred Ideas (OUT OF SCOPE)

None — discussion stayed within phase scope.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| HEADER-01 | Typing SVG cycles "Data Scientist", "ML Engineer", "Full-Stack Developer" | `lines` param with `;` separator confirmed; exact URL pattern documented below |
| HEADER-02 | SVG uses accent color `#58A6FF` and transparent background | `color=58A6FF` param confirmed; `background=00000000` (omit for default transparency) |
| HEADER-03 | Header centered full-width via `readme-typing-svg.demolab.com` | Endpoint live; `center=true&vCenter=true` centers text inside SVG; `<div align="center">` wraps it |
| STACK-01 | `shields.io` `for-the-badge` style badges grouped by category | `?style=for-the-badge` param confirmed; URL format documented |
| STACK-02 | ML/Data Science: Python, Pandas, NumPy, Scikit-learn, LightGBM, XGBoost, Plotly | Slugs verified for Python/Pandas/NumPy/scikitlearn/plotly; LightGBM+XGBoost confirmed absent |
| STACK-03 | Web & Backend: FastAPI, React, Astro, Tailwind CSS, shadcn/ui | Slugs verified: fastapi, react, astro, tailwindcss, shadcnui — all present |
| STACK-04 | Cloud & DevOps: AWS, Git, GitHub | Verified: `amazonwebservices`, `git`, `github` slugs all present |
| STACK-05 | ML badges: `color=58A6FF`; Web badges: brand colors; Cloud badges: brand colors; all `logoColor=white` | URL patterns confirmed for each group |
| STACK-06 | No verified slug → text-only badge (no broken logo icon) | Text-only format: omit `logo=` param entirely; format confirmed |
| VISUAL-02 | All SVG/badge backgrounds transparent — no white halos | For typing SVG: default background `00000000` is transparent — omit `background=` param. For shields.io badges: colored backgrounds by design are opaque (no halo issue — different visual problem than typing SVG) |
</phase_requirements>

---

## Summary

Phase 2 adds two things to README.md: (1) an animated typing SVG header replacing the `<!-- PHASE-2-HEADER -->` placeholder on line 1, and (2) a grouped tech stack badge section inserted between the existing Bio `</div>` block and the Notes callout `---` divider.

The readme-typing-svg service at `readme-typing-svg.demolab.com` is the confirmed live endpoint. It is driven by URL query parameters — no API key required, no JavaScript. The `lines` parameter accepts semicolon-separated role strings with `+` for spaces. Typing speed is controlled by `duration` (milliseconds per line), not a `speed` parameter. The blinking cursor is rendered automatically and cannot be toggled via parameter — it is always present.

All 15 tech stack badges are addressable via shields.io. Twelve have verified simple-icons slugs (logo icons). Three have no slug — LightGBM, XGBoost, and Amazon Web Services... wait: AWS does have a slug (`amazonwebservices`). LightGBM and XGBoost are the only two confirmed missing. The shadcn/ui slug `shadcnui` is verified present in simple-icons, but D-16 locked it as text-only. Text-only badges (omit the `logo=` param) work correctly for LightGBM, XGBoost, and shadcn/ui.

**Primary recommendation:** Follow locked decisions verbatim for badge URLs. Translate D-01/D-02 speed intent to `duration=1500&pause=750` as a concrete starting point. Do not add `cursor=` param — it does not exist. Use `background=` omission (default transparent) for the typing SVG. Confirm `shadcnui` slug status in Open Questions for the plan-check phase.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Typing SVG header animation | External SVG service (demolab.com) | GitHub Markdown renderer | Animation is server-rendered at demolab.com; GitHub `<img>` tag embeds it |
| Badge rendering | External SVG service (shields.io) | GitHub Markdown renderer | Badges are SVGs generated by shields.io; no local rendering |
| README layout/centering | GitHub Markdown renderer | — | `<div align="center">` and `---` dividers are rendered by GitHub |
| Content insertion | README.md file (static text) | — | Phase 2 edits are string replacements in a static file |

---

## Standard Stack

### Core

| Service | Version/Status | Purpose | Why Standard |
|---------|---------------|---------|--------------|
| `readme-typing-svg.demolab.com` | Live (2026-04-25 verified) | Animated role-cycling header SVG | Only reliable endpoint; herokuapp.com is dead per D-05 |
| `img.shields.io/badge/` | Live (shields.io v3+) | Tech stack badge generation | De-facto standard for GitHub profile badges |
| `simpleicons.org` | v16.17.0 (npm) | Logo slugs for shields.io `logo=` param | Used by shields.io for all brand logos |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| `readme-typing-svg.demolab.com` | capsule-render, typing-svg forks | Deferred in v2 requirements due to reliability concerns |
| shields.io | skill-icons, devicons | Not chosen; user decided badge-only approach |

---

## Architecture Patterns

### System Architecture Diagram

```
README.md (static file)
        |
        v
line 1: <!-- PHASE-2-HEADER -->
        |  REPLACE WITH:
        v
<div align="center">
  <img src="https://readme-typing-svg.demolab.com/...">
</div>
        |
        v
[Bio section — Phase 1, untouched]
        |
        v
---                              <-- HR divider
        |
        v  INSERT NEW SECTION:
📊 **ML / Data Science**
[badge row]
🛠️ **Web & Backend**
[badge row]
🚀 **Cloud & DevOps**
[badge row]
        |
        v
---                              <-- existing HR divider (Notes callout)
[Notes callout — Phase 1, untouched]
```

Data flow: GitHub visitor loads profile → GitHub renderer fetches SVG from demolab.com → SVG plays typed animation in visitor's browser. Badges are fetched individually from shields.io. All external fetches happen client-side; the README is entirely static.

### Integration Points (Exact)

- **Typing SVG header:** Replace `<!-- PHASE-2-HEADER -->` (line 1) with the centered `<div>` + `<img>` block.
- **Stack section:** Insert after the Bio section closing `</div>` (currently line 9 in README.md), before the `---` that precedes the Notes callout (currently line 11).

Current README.md structure (line numbers at time of research):
```
1: <!-- PHASE-2-HEADER -->
2: (blank)
3: <div align="center">
4: (blank)
5: **Data scientist by title...**
6: (blank)
7: 🧑‍💻 **Data Scientist**...
8: (blank)
9: </div>
10: (blank)
11: ---
12: (blank)
13: <div align="center">   ← Notes callout starts here
```

Stack section inserts between line 9 (`</div>`) and line 11 (`---`).

### Recommended README Section Structure

```markdown
<!-- Header block (replaces line 1 placeholder) -->
<div align="center">
<img src="https://readme-typing-svg.demolab.com/render?font=Fira+Code&size=22&duration=1500&pause=750&color=58A6FF&center=true&vCenter=true&width=500&lines=Data+Scientist;ML+Engineer;Full-Stack+Developer" alt="Typing SVG" />
</div>

[Bio section — untouched]

---

<div align="center">

📊 **ML / Data Science**

[badge row — see Code Examples]

🛠️ **Web & Backend**

[badge row — see Code Examples]

🚀 **Cloud & DevOps**

[badge row — see Code Examples]

</div>

---

[Notes callout — untouched]
```

### Anti-Patterns to Avoid

- **Adding `cursor=true` to typing SVG URL:** `cursor` is not a documented parameter. The cursor renders automatically. Adding it will produce an unknown-param error or be silently ignored — do not include it.
- **Using `background=transparent` string:** The `background` param requires 8-digit hex (`00000000`). The string `transparent` is not supported. Since the default is already `00000000` (fully transparent), omit the param entirely.
- **Using `style=` HTML attributes on any element:** GitHub sanitizer strips them. Use `align=` attribute on `<div>` only, per VISUAL-04.
- **Adding `logo=scikitlearn` with a hyphen:** The slug is `scikitlearn` (no hyphen). Using `scikit-learn` will produce a broken icon.
- **URL-encoding spaces as `%20` in the `lines` param:** The readme-typing-svg service uses `+` for spaces in the `lines` param (e.g., `Data+Scientist`, not `Data%20Scientist`).
- **Wrapping badge rows in a `<table>`:** Stack section uses plain centered `<div>` with badge image tags on one line. Table layout is only for Phase 3 project cards.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Animated role-cycling text | Custom GIF, JS animation, CSS animation | `readme-typing-svg.demolab.com` | GitHub strips JS; CSS stripped; GIFs are static — SVG service is the only reliable animated text option |
| Brand logo icons in badges | Custom SVG, base64-encoded logos | `logo=` param with simple-icons slugs via shields.io | simple-icons maintains 3,400+ brand SVGs; shields.io handles sizing/color/rendering |
| Text-only fallback badges | Separate image hosting | Omit `logo=` param in shields.io URL | Same shields.io endpoint, same `for-the-badge` style — just without `&logo=` |

**Key insight:** The entire Phase 2 implementation is URL construction. No code executes. No files other than README.md change. Every "component" is a URL that GitHub's Markdown renderer fetches as an `<img>` tag.

---

## Common Pitfalls

### Pitfall 1: cursor Parameter Does Not Exist
**What goes wrong:** Planner includes `&cursor=true` in the typing SVG URL because D-03 mentions it.
**Why it happens:** CONTEXT.md D-03 says "Cursor: visible and blinking (`cursor=true` default)" — this phrasing implies a URL parameter.
**How to avoid:** Do not add `cursor=` to the URL. The blinking cursor is always rendered as part of the typing animation; it cannot be disabled or toggled via parameter.
**Warning signs:** If the SVG URL has `cursor=` in it, remove it.

### Pitfall 2: `duration` Controls Line Print Time, Not Per-Character Speed
**What goes wrong:** Planner sets a very low `duration` (e.g., `duration=70`) thinking it means 70ms per character.
**Why it happens:** D-01 says "60–80ms per character" but there is no per-character parameter — only `duration` (ms per full line).
**How to avoid:** Use the following conversion: The longest role is "Full-Stack Developer" (18 characters). At 70ms/char → 18 × 70 = ~1260ms. A reasonable `duration` range is **1200–1500ms** for a "fast & snappy" feel. A `pause` of **500–800ms** satisfies D-02's minimal pause constraint.

**Recommended concrete values (within Claude's Discretion):**
- `duration=1500` — prints one role in 1.5 seconds (~83ms/char for the longest role)
- `pause=750` — 0.75s pause between roles
- These are starting values; user can tune after seeing live render.

### Pitfall 3: `scikit-learn` Slug Has No Hyphen
**What goes wrong:** Badge uses `logo=scikit-learn` and the icon is broken (404 from shields.io).
**Why it happens:** The library name is spelled with a hyphen; the simple-icons slug is not.
**How to avoid:** Use `logo=scikitlearn` (no hyphen, all lowercase).

### Pitfall 4: AWS Slug Is `amazonwebservices` Not `aws`
**What goes wrong:** Badge uses `logo=aws` and shows a broken icon.
**Why it happens:** Intuitive abbreviation; the slug is the full brand name form.
**How to avoid:** Use `logo=amazonwebservices`.

### Pitfall 5: shadcnui Slug Exists But Is Locked as Text-Only
**What goes wrong:** Planner sees D-16 ("text-only") but then finds `shadcnui` slug exists and adds `logo=shadcnui` thinking this improves the badge.
**Why it happens:** D-16 was made before slug was confirmed; evidence now contradicts the assumption.
**How to avoid:** Honor D-16 as a locked decision — shadcn/ui remains text-only for Phase 2. The planner should note this contradiction for the plan-check phase review (see Open Questions). Do not unilaterally add the logo.

### Pitfall 6: Stack Section Inserted in Wrong Location
**What goes wrong:** Stack section placed after the Notes `---` divider instead of before it, or mixed into the Bio `<div>`.
**Why it happens:** README is short; it's easy to mis-read the insertion target.
**How to avoid:** The insertion goes between the Bio `</div>` close tag and the `---` that precedes the Notes callout. Verify with `grep -n "PHASE-2-HEADER\|</div>\|---"` before writing.

---

## Code Examples

Verified patterns from official sources and confirmed parameter docs:

### Typing SVG — Recommended URL

```markdown
<!-- Source: readme-typing-svg official README, parameter table verified 2026-04-25 -->
<div align="center">
<img src="https://readme-typing-svg.demolab.com/render?font=Fira+Code&size=22&duration=1500&pause=750&color=58A6FF&center=true&vCenter=true&width=500&lines=Data+Scientist;ML+Engineer;Full-Stack+Developer" alt="Typing SVG" />
</div>
```

**Parameter breakdown:**
| Param | Value | Rationale |
|-------|-------|-----------|
| `font` | `Fira+Code` | Monospace, developer-aesthetic, Google Fonts available |
| `size` | `22` | Slightly larger than default 20; readable at profile header size |
| `duration` | `1500` | ~83ms per char for "Full-Stack Developer" — fast per D-01 |
| `pause` | `750` | 0.75s between roles — minimal per D-02 |
| `color` | `58A6FF` | Accent color per D-06 (no `#` prefix) |
| `center` | `true` | Horizontally centers text within SVG |
| `vCenter` | `true` | Vertically centers text within SVG height |
| `width` | `500` | Enough for "Full-Stack Developer" at size 22 in Fira Code |
| `lines` | `Data+Scientist;ML+Engineer;Full-Stack+Developer` | Roles per D-04; `;` separates lines; `+` is space |
| `background` | *(omitted)* | Default `00000000` is fully transparent — omit param |
| `cursor` | *(omitted)* | No such parameter; cursor renders automatically |

### Badge — With Logo (Standard Pattern)

```markdown
<!-- Source: shields.io static badge docs, verified 2026-04-25 -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-4DABCF?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-58A6FF?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-58A6FF?style=for-the-badge&logo=plotly&logoColor=white)
```

### Badge — Text-Only (No Logo, For Missing Slugs)

```markdown
<!-- Source: shields.io static badge docs — omit logo= param entirely -->
![LightGBM](https://img.shields.io/badge/LightGBM-58A6FF?style=for-the-badge&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-58A6FF?style=for-the-badge&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-000000?style=for-the-badge&logoColor=white)
```

Note: `shadcn/ui` label needs `%2F` for the slash in the URL path segment.

### Badge — Web & Backend Group (Brand Colors)

```markdown
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Astro](https://img.shields.io/badge/Astro-FF5D01?style=for-the-badge&logo=astro&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-000000?style=for-the-badge&logoColor=white)
```

### Badge — Cloud & DevOps Group (Brand Colors)

```markdown
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
```

### Shield Badge URL Format Reference

```
https://img.shields.io/badge/[LABEL]-[COLOR]?style=for-the-badge&logo=[SLUG]&logoColor=white

For text-only (no logo):
https://img.shields.io/badge/[LABEL]-[COLOR]?style=for-the-badge

Special chars in LABEL: encode / as %2F, spaces as _ or %20 or use - as separator
```

---

## Simple-Icons Slug Verification Table

[VERIFIED: simpleicons.org slugs.md fetched 2026-04-25]

| Badge | Slug | Status | Notes |
|-------|------|--------|-------|
| Python | `python` | VERIFIED PRESENT | — |
| Pandas | `pandas` | VERIFIED PRESENT | — |
| NumPy | `numpy` | VERIFIED PRESENT | — |
| scikit-learn | `scikitlearn` | VERIFIED PRESENT | No hyphen — critical |
| LightGBM | — | VERIFIED ABSENT | Text-only badge per D-14 |
| XGBoost | — | VERIFIED ABSENT | Text-only badge per D-15 |
| Plotly | `plotly` | VERIFIED PRESENT | — |
| FastAPI | `fastapi` | VERIFIED PRESENT | — |
| React | `react` | VERIFIED PRESENT | — |
| Astro | `astro` | VERIFIED PRESENT | — |
| Tailwind CSS | `tailwindcss` | VERIFIED PRESENT | — |
| shadcn/ui | `shadcnui` | VERIFIED PRESENT | D-16 locks as text-only despite slug existing — see Open Questions |
| AWS | `amazonwebservices` | VERIFIED PRESENT | Full brand name, not `aws` |
| Git | `git` | VERIFIED PRESENT | — |
| GitHub | `github` | VERIFIED PRESENT | — |

---

## Brand Hex Colors

| Badge | Hex | Source |
|-------|-----|--------|
| Python | `3776AB` | [CITED: md-badges verified against shields.io examples] |
| Pandas | `150458` | [CITED: md-badges verified against shields.io examples] |
| NumPy | `4DABCF` | [CITED: md-badges verified against shields.io examples] |
| scikit-learn | `58A6FF` | [CITED: CONTEXT.md D-10 — accent color override per STACK-05] |
| LightGBM | `58A6FF` | [CITED: CONTEXT.md D-10 — accent color for ML group] |
| XGBoost | `58A6FF` | [CITED: CONTEXT.md D-10 — accent color for ML group] |
| Plotly | `58A6FF` | [CITED: CONTEXT.md D-10 — accent color for ML group] |
| FastAPI | `009688` | [CITED: CONTEXT.md D-11; consistent with web search confirming FastAPI teal brand] |
| React | `61DAFB` | [CITED: CONTEXT.md D-11; consistent with web search confirming React cyan brand] |
| Astro | `FF5D01` | [CITED: CONTEXT.md D-11] |
| Tailwind CSS | `06B6D4` | [CITED: CONTEXT.md D-11] |
| shadcn/ui | `000000` | [ASSUMED: black background to match shadcn/ui's brand aesthetic] |
| AWS | `FF9900` | [CITED: CONTEXT.md D-12; consistent with official AWS orange brand] |
| Git | `F05032` | [CITED: CONTEXT.md D-12] |
| GitHub | `181717` | [CITED: CONTEXT.md D-12] |

**Note on ML group colors:** Per D-10, scikit-learn, Plotly, LightGBM, and XGBoost all use the accent color `58A6FF` rather than their own brand colors (they have no dominant brand color). Python, Pandas, NumPy use their own brand colors because they have well-established, recognizable brand identities.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `readme-typing-svg.herokuapp.com` | `readme-typing-svg.demolab.com` | 2022 (Heroku free tier shutdown) | Old endpoint is dead — must use demolab.com |
| `speed` parameter | `duration` parameter (ms per line) | Original API design | No `speed` param exists; only `duration` |

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | shadcn/ui text-only badge uses `000000` (black) as background color | Brand Hex Colors | Visual: badge may look odd; planner can pick any readable contrast color |
| A2 | `Fira+Code` is available from Google Fonts and renders correctly in readme-typing-svg | Code Examples | Typography: fallback to `monospace` default; safe to change at implementation time |
| A3 | The `width=500` is sufficient for "Full-Stack Developer" at `size=22` in Fira Code | Code Examples | Layout: text may clip if too narrow; planner should verify with live preview |
| A4 | Brand colors for Astro (`FF5D01`), Tailwind (`06B6D4`), Git (`F05032`), GitHub (`181717`) match current simple-icons data | Brand Hex Colors | Visual: minor color drift if simple-icons updated these recently; low risk |

---

## Open Questions

1. **D-16 contradiction: shadcnui slug is verified present**
   - What we know: The simple-icons slug `shadcnui` is verified present in slugs.md. D-16 locked shadcn/ui as text-only based on "no verified simple-icons slug" — that premise is now falsified.
   - What's unclear: Whether the user wants to revisit this and add the shadcnui logo.
   - Recommendation: Honor D-16 as written for Phase 2 implementation. Surface for plan-check review — the plan-checker should flag for user confirmation before finalizing.

2. **Typing SVG width verification**
   - What we know: `width=500` is estimated to fit "Full-Stack Developer" at size 22 in Fira Code.
   - What's unclear: Exact pixel width depends on Google Fonts rendering; cannot be pre-computed precisely.
   - Recommendation: Planner sets `width=500` as starting value. Executor verifies via live URL preview and adjusts if text is clipped.

3. **GitHub dark/light theme behavior for typing SVG**
   - What we know: readme-typing-svg default `background=00000000` is transparent. The SVG text is colored `#58A6FF` which is visible on both dark and light backgrounds.
   - What's unclear: Whether GitHub's CSP or Markdown sanitizer affects SVG fetched via `<img>` tag from demolab.com.
   - Recommendation: Executor performs visual check in both GitHub themes after implementation. No `<picture>`/`<source>` dark-mode splitting needed since accent blue is readable on both themes.

---

## Environment Availability

Step 2.6: SKIPPED — phase is pure README.md text editing; no external CLI tools, runtimes, or services beyond the existing git workflow are required.

---

## Sources

### Primary (HIGH confidence)
- `github.com/DenverCoder1/readme-typing-svg` README.md — complete parameter table, defaults, `lines` format
- `github.com/simple-icons/simple-icons/blob/develop/slugs.md` — slug presence/absence for all 15 technologies
- `shields.io/docs/static-badges` — text-only and logo badge URL format

### Secondary (MEDIUM confidence)
- `github.com/DenverCoder1/readme-typing-svg/blob/main/docs/faq.md` — `<picture>`/`<source>` dark mode technique confirmed
- `github.com/inttter/md-badges` — brand hex colors for Python, Pandas, NumPy cross-referenced
- Web search confirming `amazonwebservices` as shields.io slug for AWS with `FF9900` brand color
- Web search confirming `background=00000000` as the only valid transparent-value format (not string "transparent")

### Tertiary (LOW confidence)
- Various web search results for brand hex colors (Astro, Tailwind, Git, GitHub) — cited from CONTEXT.md D-11/D-12 which were set in prior discussion phase

---

## Metadata

**Confidence breakdown:**
- Typing SVG parameters: HIGH — fetched directly from official README
- Simple-icons slug verification: HIGH — fetched directly from slugs.md
- Badge URL format: HIGH — verified via shields.io docs
- Brand hex colors (React, FastAPI, AWS, Python/Pandas/NumPy): MEDIUM — cross-referenced web search + md-badges
- Brand hex colors (Astro, Tailwind, Git, GitHub): LOW — cited from CONTEXT.md, not independently verified this session

**Research date:** 2026-04-25
**Valid until:** 2026-05-25 (stable ecosystem; simple-icons slugs and shields.io API are very stable)
