# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-04-21)

**Core value:** A visitor — whether a recruiter or a fellow developer — should immediately understand who Aditya is, what he builds, and where to go next.
**Current focus:** Phase 1 — Scaffold

## Current Position

Phase: 1 of 3 (Scaffold)
Plan: 0 of TBD in current phase
Status: Ready to plan
Last activity: 2026-04-21 — Roadmap created (3 phases, 25 requirements mapped)

Progress: [░░░░░░░░░░] 0%

## Performance Metrics

**Velocity:**
- Total plans completed: 0
- Average duration: —
- Total execution time: 0 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 1. Scaffold | 0/TBD | - | - |
| 2. Header & Stack | 0/TBD | - | - |
| 3. Project Cards | 0/TBD | - | - |

**Recent Trend:**
- Last 5 plans: —
- Trend: —

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- Roadmap: Accent color locked at `#58A6FF` — propagates to all typing SVG `color=` and shields.io `color=` params
- Roadmap: Badge style split — `for-the-badge` for standalone rows; `flat-square` inside project card `<td>`
- Roadmap: VISUAL requirements distributed across phases by natural fit (not a separate polish phase)
- Roadmap: 3 phases at coarse granularity — Scaffold → Header & Stack → Project Cards

### Critical Technical Notes

- **`<td>` flush-left rule**: `<td>` opening tags must have NO leading whitespace, and Markdown content inside needs a blank line after the opening tag. Indented tags cause code-block rendering. This is enforced in Phase 3.
- **Typing SVG endpoint**: Use `readme-typing-svg.demolab.com` only — the old `herokuapp.com` endpoint is dead.
- **Simple-icons slugs to verify**: `lightgbm`, `xgboost`, `amazonsagemaker`, `scikitlearn` (no hyphen) — verify at simpleicons.org before embedding. LightGBM and XGBoost likely need text-only fallback badges.
- **GitHub sanitizer**: `style=` attributes are stripped. Use `align=` on `<div>` and `<td>` only.
- **SVG backgrounds**: Set `background=transparent` on typing SVG. Test both GitHub light and dark themes before publishing.

### Pending Todos

None yet.

### Blockers/Concerns

- Simple-icons slug availability for ML libraries (LightGBM, XGBoost) — plan for text-only badge fallback per STACK-06.
- DS/ML notes repo name and public status to confirm before Phase 1 implementation (`joshiaditya0511/data-science-notes` assumed).

## Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| v2 | Snake contribution animation (Platane/snk) | Deferred — requires GitHub Actions setup | Roadmap init |
| v2 | Capsule-render wave dividers | Deferred — reliability concerns (Vercel free tier) | Roadmap init |

## Session Continuity

Last session: 2026-04-21
Stopped at: Roadmap created. Ready to plan Phase 1 (Scaffold).
Resume file: None
