# Roadmap: joshiaditya0511 GitHub Profile README

## Overview

A single README.md file transforms the GitHub profile into a personal landing page. Phase 1 lays the static scaffold — bio, roles, social links, notes callout, and visual baseline rules that govern the whole file. Phase 2 adds the animated header and all tech stack badges, which require external SVG services and careful accent-color propagation. Phase 3 delivers the featured project cards using an HTML table layout, closing out the profile with the most technically tricky piece (the `<td>` flush-left gotcha).

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Scaffold** - Static structure, bio, role callout, social links, notes callout, and visual baseline rules
- [ ] **Phase 2: Header & Stack** - Animated typing SVG header and grouped shields.io tech stack badges with accent color applied
- [ ] **Phase 3: Project Cards** - Featured project HTML table with flush-left `<td>` layout, descriptions, badges, and live links

## Phase Details

### Phase 1: Scaffold
**Goal**: A visitor loading the profile sees a coherent, readable structure with bio, current roles, social links, and notes callout — the full static content skeleton with visual rules in place
**Depends on**: Nothing (first phase)
**Requirements**: BIO-01, BIO-02, BIO-03, SOCIAL-01, SOCIAL-02, NOTES-01, NOTES-02, VISUAL-01, VISUAL-03, VISUAL-04, VISUAL-05
**Success Criteria** (what must be TRUE):
  1. Visitor reads the exact bio text and sees both current roles (Revcloud / Forengers) clearly identified, centered below where the header will go
  2. Badge-style social links for personal website, LinkedIn, and email are all clickable and resolve to the correct destinations
  3. The DS/ML notes callout is visually distinct from surrounding text and links to the correct repository
  4. Every section is separated by a horizontal rule, all major blocks are centered, and no HTML `style=` attribute appears anywhere in the file
**Plans**: 1 plan
Plans:
- [ ] 01-01-PLAN.md — Write and verify the full static README.md skeleton (bio, roles, notes callout, social badges, visual rules)

### Phase 2: Header & Stack
**Goal**: The profile opens with an animated role-cycling header and displays a grouped, correctly colored tech stack — all external SVG services verified working in both GitHub themes
**Depends on**: Phase 1
**Requirements**: HEADER-01, HEADER-02, HEADER-03, STACK-01, STACK-02, STACK-03, STACK-04, STACK-05, STACK-06, VISUAL-02
**Success Criteria** (what must be TRUE):
  1. Visitor sees three role labels cycling in the header (Data Scientist / ML Engineer / Full-Stack Developer) in accent color `#58A6FF` with no white halo in either GitHub light or dark theme
  2. Tech stack badges are grouped under labeled categories (ML/Data Science, Web & Backend, Cloud & DevOps), all use `for-the-badge` style, and every badge renders without a broken-logo icon
  3. Badges with no verified simple-icons slug (LightGBM, XGBoost) display as text-only badges rather than broken images
  4. All badge and SVG backgrounds are transparent — no white box artifact visible when toggling between GitHub light and dark themes
**Plans**: TBD
**UI hint**: yes

### Phase 3: Project Cards
**Goal**: Visitor sees two featured project cards side-by-side in a 2-column layout, each with an outcome-specific description, tech badges, and working live and GitHub links
**Depends on**: Phase 2
**Requirements**: PROJ-01, PROJ-02, PROJ-03, PROJ-04
**Success Criteria** (what must be TRUE):
  1. PuneProp Predict and Karnataka Elections Analysis cards render side-by-side (not stacked) in GitHub's Markdown renderer
  2. Each card description names a concrete outcome (model accuracy or data scale) — not a generic summary
  3. All live links (`pune.adityajoshi.in`, `kea.adityajoshi.in`) and GitHub repo links open the correct destinations
  4. Badge content inside `<td>` renders as Markdown (not as a code block) — confirming the flush-left `<td>` gotcha is resolved
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Scaffold | 0/1 | Not started | - |
| 2. Header & Stack | 0/TBD | Not started | - |
| 3. Project Cards | 0/TBD | Not started | - |
