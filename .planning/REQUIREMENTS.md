# Requirements — joshiaditya0511 GitHub Profile README

**Version:** v1
**Created:** 2026-04-22
**Accent color:** `#58A6FF` (GitHub blue) — propagates to all badge and SVG color params

---

## v1 Requirements

### Header (HEADER)

- [ ] **HEADER-01**: Profile displays an animated typing SVG header cycling 3 roles: "Data Scientist", "ML Engineer", "Full-Stack Developer"
- [ ] **HEADER-02**: Typing SVG uses accent color `#58A6FF` and transparent background (no white halo in light theme)
- [ ] **HEADER-03**: Header is centered full-width, rendered via `readme-typing-svg.demolab.com`

### Bio & Role (BIO)

- [ ] **BIO-01**: Profile displays bio text: *"Data scientist by title, engineer by habit. I build ML pipelines, ship full-stack products, and head the tech team at a climate NGO."*
- [ ] **BIO-02**: Bio section includes current role callout — Data Scientist at Revcloud (Alyson AI) and Technical Head at Forengers
- [ ] **BIO-03**: Bio section is centered and appears immediately below the header

### Tech Stack Badges (STACK)

- [ ] **STACK-01**: Tech stack displayed as `shields.io` `for-the-badge` style badges, grouped by category with a label per group
- [ ] **STACK-02**: ML/Data Science group includes: Python, Pandas, NumPy, Scikit-learn, LightGBM, XGBoost, Plotly
- [ ] **STACK-03**: Web & Backend group includes: FastAPI, React, Astro.js, Tailwind CSS, shadcn/ui
- [ ] **STACK-04**: Cloud & DevOps group includes: AWS, Git, GitHub
- [ ] **STACK-05**: All badges use `logoColor=white`; ML/Data badges use `color=58A6FF`; Web badges use brand colors; Cloud badges use brand colors
- [ ] **STACK-06**: Badges with no verified simple-icons slug (LightGBM, XGBoost) fall back to text-only badge (no broken logo)

### Featured Projects (PROJ)

- [ ] **PROJ-01**: Featured projects section uses a 2-column HTML `<table>` layout with flush-left `<td>` tags
- [ ] **PROJ-02**: PuneProp Predict card includes: title, one-line description, `flat-square` tech stack badges, live link (`pune.adityajoshi.in`), GitHub repo link
- [ ] **PROJ-03**: Karnataka Elections Analysis card includes: title, one-line description, `flat-square` tech stack badges, live link (`kea.adityajoshi.in`), GitHub repo link
- [ ] **PROJ-04**: Project card descriptions are specific and outcome-focused (not generic — include model accuracy or data scale)

### Notes & Resources (NOTES)

- [ ] **NOTES-01**: Profile includes a callout section linking to the DS/ML notes repository (`joshiaditya0511/data-science-notes`) with a short description
- [ ] **NOTES-02**: Notes callout is visually distinct (badge-style link, not plain text) but secondary to project cards

### Social & Contact (SOCIAL)

- [ ] **SOCIAL-01**: Footer includes badge-style social links: personal website (`adityajoshi.in`), LinkedIn (`joshiaditya0511`), email (`contact@adityajoshi.in`)
- [ ] **SOCIAL-02**: Social badges use consistent styling (same badge style as rest of profile)

### Visual & Polish (VISUAL)

- [ ] **VISUAL-01**: All major sections are centered using `<div align="center">`
- [ ] **VISUAL-02**: All SVG/badge backgrounds are transparent — no white halos in either GitHub light or dark theme
- [ ] **VISUAL-03**: Horizontal rule (`---`) dividers between each major section
- [ ] **VISUAL-04**: No `style=` attributes on any HTML element (GitHub sanitizer strips them)
- [ ] **VISUAL-05**: Profile README is scannable end-to-end without scrolling past a wall of content — concise copy, visual hierarchy

---

## v2 Requirements (deferred)

- Snake contribution animation via `Platane/snk` GitHub Action — strong differentiator, deferred due to GitHub Actions setup requirement
- Capsule-render wave section dividers — deferred due to reliability concerns (Vercel free tier, solo maintainer)
- Visitor counter badge — explicitly excluded as anti-feature

---

## Out of Scope

- **GitHub stats cards** (github-readme-stats) — no live stat widgets; reliability issues; user decision
- **Streak counter** — same reason as stats cards
- **Trophy cards** — same reason
- **Wakatime / Spotify widgets** — considered "tutorial profile" signals in 2025
- **Visitor counter** — anti-feature; makes profile look dated
- **Open to work badge** — user is not job-seeking
- **Walmart Sales Forecasting project** — excluded by user; quality over quantity
- **`style=` CSS attributes** — GitHub sanitizer strips them; layout via `align=` only

---

## Traceability

| Phase | Requirements Covered | Status |
|-------|---------------------|--------|
| Phase 1: Scaffold | BIO-01, BIO-02, BIO-03, SOCIAL-01, SOCIAL-02, NOTES-01, NOTES-02, VISUAL-01, VISUAL-03, VISUAL-04, VISUAL-05 | Pending |
| Phase 2: Header & Stack | HEADER-01, HEADER-02, HEADER-03, STACK-01, STACK-02, STACK-03, STACK-04, STACK-05, STACK-06, VISUAL-02 | Pending |
| Phase 3: Project Cards | PROJ-01, PROJ-02, PROJ-03, PROJ-04 | Pending |
