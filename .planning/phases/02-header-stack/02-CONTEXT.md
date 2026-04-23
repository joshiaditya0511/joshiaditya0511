# Phase 2: Header & Stack - Context

**Gathered:** 2026-04-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Animated typing SVG header + grouped tech stack badges. Replaces the `<!-- PHASE-2-HEADER -->` placeholder on line 1 of README.md and inserts a new stack section between Bio and the Notes callout. No static content changes — Phase 1 content is untouched.

</domain>

<decisions>
## Implementation Decisions

### Header Animation
- **D-01:** Typing speed: fast & snappy (~60–80ms per character). Energetic, suits a tech profile where visitors scan quickly.
- **D-02:** Pause between roles: minimal (~0.5–1s). Constant-motion feel, roles cycle without a long hold.
- **D-03:** Cursor: visible and blinking (`cursor=true` default). Reinforces the typing effect.
- **D-04:** Roles (locked by HEADER-01): "Data Scientist", "ML Engineer", "Full-Stack Developer" — in that order.
- **D-05:** SVG endpoint (locked by HEADER-03): `readme-typing-svg.demolab.com` only. Old `herokuapp.com` is dead.
- **D-06:** Accent color (locked by HEADER-02 + prior phases): `#58A6FF`. SVG `color=` param and `background=transparent`.

### Stack Section Placement
- **D-07:** README flow: Header → Bio (Phase 1) → Tech Stack → Notes callout (Phase 1) → Social (Phase 1). Stack section is inserted between Bio and the existing Notes callout.

### Stack Group Labels
- **D-08:** Label style: emoji + bold Markdown text on its own line above each badge row.
- **D-09:** Emoji set:
  - `📊 **ML / Data Science**`
  - `🛠️ **Web & Backend**`
  - `🚀 **Cloud & DevOps**`

### Badge Colors (per STACK-05)
- **D-10:** ML/Data Science badges: `color=58A6FF`, `logoColor=white` (accent color per requirements).
- **D-11:** Web & Backend badges: brand colors per platform (React `61DAFB`, FastAPI `009688`, Astro `FF5D01`, Tailwind `06B6D4`).
- **D-12:** Cloud & DevOps badges: brand colors per platform (AWS `FF9900`, Git `F05032`, GitHub `181717`/white on dark).
- **D-13:** All badges: `style=for-the-badge` (locked by STACK-01 and Phase 1 badge style decision).

### Text-Only Fallback Badges (per STACK-06)
- **D-14:** LightGBM — text-only badge (no logo icon). No verified simple-icons slug.
- **D-15:** XGBoost — text-only badge (no logo icon). No verified simple-icons slug.
- **D-16:** shadcn/ui — text-only badge, same pattern as LightGBM/XGBoost. No verified simple-icons slug.

### Claude's Discretion
- Exact `speed`, `duration`, and `pause` param values for `readme-typing-svg` — planner tunes within the fast/minimal constraint.
- Exact fallback badge colors for text-only entries (LightGBM, XGBoost, shadcn/ui) — planner picks readable contrast.
- Verification of remaining simple-icons slugs (`amazonsagemaker`, `scikitlearn`, `astro`, `shadcn`) before embedding — planner confirms at simpleicons.org.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Requirements
- `.planning/REQUIREMENTS.md` — HEADER-01, HEADER-02, HEADER-03, STACK-01, STACK-02, STACK-03, STACK-04, STACK-05, STACK-06, VISUAL-02

### Project context
- `.planning/PROJECT.md` — Identity, tech footprint (badge inventory), style choices, constraints
- `.planning/STATE.md` §Critical Technical Notes — typing SVG endpoint, simple-icons slugs to verify, GitHub sanitizer rules, badge style split

### Integration point
- `README.md` line 1 — `<!-- PHASE-2-HEADER -->` is the insertion contract. Phase 2 replaces this comment with the `<img>` tag for the typing SVG, then inserts the stack section before the Notes callout.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `README.md` (Phase 1 output) — existing Bio, Notes callout, and Social sections stay intact; Phase 2 prepends the header and inserts the stack section.

### Established Patterns
- `for-the-badge` badge style for standalone rows (from Phase 1 / STATE.md decision)
- `align="center"` on `<div>` only — no `style=` attributes anywhere (VISUAL-04)
- Accent color `#58A6FF` in all badge `color=` params
- HR divider (`---`) between every major section

### Integration Points
- Line 1 `<!-- PHASE-2-HEADER -->`: replace with `<div align="center"><img src="https://readme-typing-svg.demolab.com/..." /></div>`
- Stack section inserts between the Bio `</div>` block and the Notes callout `---` divider

</code_context>

<specifics>
## Specific Ideas

No specific visual references beyond requirements. Animation feel agreed: fast-cycle with minimal pause between roles.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 02-header-stack*
*Context gathered: 2026-04-23*
