# Phase 1: Scaffold - Context

**Gathered:** 2026-04-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Static content skeleton for the GitHub profile README. Delivers: bio text, current role callout, social/contact links, DS/ML notes callout, and all visual baseline rules (centering, HR dividers, no `style=` attributes). No animated or dynamic elements — those are Phase 2 and 3.

</domain>

<decisions>
## Implementation Decisions

### Bio & Roles
- **D-01:** Bio text is locked — exact copy: *"Data scientist by title, engineer by habit. I build ML pipelines, ship full-stack products, and head the tech team at a climate NGO."*
- **D-02:** Bio section is centered (`<div align="center">`) and sits below where the Phase 2 header will go.
- **D-03:** Role callout names both positions explicitly: Data Scientist at Revcloud (Alyson AI) and Technical Head at Forengers.

### Social Links
- **D-04:** Social links use `for-the-badge` style shields.io badges (consistent with the project badge style decision).
- **D-05:** Links cover exactly three destinations: personal website (`adityajoshi.in`), LinkedIn (`joshiaditya0511`), and email (`contact@adityajoshi.in`).

### Notes Callout
- **D-06:** Notes callout links to `joshiaditya0511/data-science-notes` repository.
- **D-07:** Notes callout is visually secondary to project cards — a short description line + badge link, not a full section header treatment.

### Visual Rules
- **D-08:** All major sections wrapped in `<div align="center">`.
- **D-09:** Horizontal rule (`---`) separates every major section.
- **D-10:** Zero `style=` attributes anywhere in the file — GitHub sanitizer strips them.
- **D-11:** Accent color `#58A6FF` propagates to any colored badges in this phase.

### Claude's Discretion
- Role callout visual treatment (bold inline text, emoji-prefixed line, or badge row) — planner decides
- Social badge color choice (uniform accent vs. brand colors per platform) — planner decides
- Notes callout visual design within "visually distinct but secondary" constraint — planner decides
- Exact section ordering for bio, roles, notes, social footer — planner decides, optimizing for scannability

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Requirements
- `.planning/REQUIREMENTS.md` — All v1 requirements; Phase 1 covers BIO-01 through BIO-03, SOCIAL-01, SOCIAL-02, NOTES-01, NOTES-02, VISUAL-01, VISUAL-03, VISUAL-04, VISUAL-05

### Project context
- `.planning/PROJECT.md` — Identity, tech footprint, style choices, constraints, key decisions table
- `.planning/STATE.md` §Critical Technical Notes — GitHub sanitizer rules, badge style split, typing SVG endpoint, shields.io gotchas

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- None — greenfield. No prior README.md exists.

### Established Patterns
- `for-the-badge` badge style decided for standalone badge rows (from STATE.md)
- `flat-square` badge style reserved for inside `<td>` tags (Phase 3)
- `align=` attribute on `<div>` only — no `style=` attributes
- Accent color `#58A6FF` for any accent-colored badge `color=` params

### Integration Points
- Phase 1 creates the README.md file. Phase 2 inserts the typing SVG header at the top. Phase 3 appends the project cards table. Phase 1 must leave a clear placeholder comment or section break at the top where the Phase 2 header will go.

</code_context>

<specifics>
## Specific Ideas

No specific requirements beyond what the requirements doc locks — open to standard GitHub profile README approaches for layout and visual hierarchy.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 01-scaffold*
*Context gathered: 2026-04-23*
