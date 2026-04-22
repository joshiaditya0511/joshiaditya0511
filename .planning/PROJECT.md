# GitHub Profile README — joshiaditya0511

## What This Is

A richly styled GitHub profile README for the `joshiaditya0511/joshiaditya0511` special repository. It serves as a personal landing page on GitHub — the first thing anyone sees when visiting the profile. The goal is to communicate Aditya's identity as a data-science-meets-software-engineering hybrid through a visually impressive dark-themed profile with animated elements, curated tech stack badges, featured project cards, and a short personal bio.

## Core Value

A visitor — whether a recruiter or a fellow developer — should immediately understand who Aditya is, what he builds, and where to go next.

## Requirements

### Validated

- [x] Short personal bio blurb — validated in Phase 1
- [x] Current role callout: Data Scientist at Revcloud (Alyson AI) + Tech Head at Forengers — validated in Phase 1
- [x] Social/contact links: Personal website, LinkedIn, Email — validated in Phase 1
- [x] Notes/resources callout linking to DS/ML notes repo — validated in Phase 1
- [x] Dark-themed aesthetic (visual baseline rules: centered divs, HR dividers, no style= attributes) — validated in Phase 1

### Active

- [ ] Animated header with typing SVG (rotating roles: Data Scientist · ML Engineer · Full-Stack Developer)
- [ ] Short personal bio blurb ("I sit at the intersection of data science and software engineering")
- [ ] Current role callout: Data Scientist at Revcloud (Alyson AI / Experiments Manager) + Tech Head at Forengers
- [ ] Tech stack section with shields.io badge icons — no stats cards, badges only
- [ ] Featured projects section: PuneProp Predict + Karnataka Elections Analysis (custom markdown cards with live links)
- [ ] Social/contact links: Personal website, LinkedIn, GitHub, Email
- [ ] Dark-themed aesthetic with neon/accent color highlights
- [ ] Notes/resources callout linking to DS/ML notes repo

### Out of Scope

- GitHub stats cards / streak counter — user prefers badge-only, no live-updating stat widgets
- Walmart Sales Forecasting project — not featured (user decision)
- "Open to work" badge or framing — user is not job-seeking
- Profile photo or external image hosting (keep it GitHub-native)

## Context

- **Platform:** GitHub profile README — rendered as Markdown on `github.com/joshiaditya0511`. Supports standard Markdown, HTML img tags, and third-party SVG services (shields.io, readme-typing-svg).
- **Identity:** Aditya Joshi, Pune, India. Data Scientist at Revcloud (full-time, Aug 2025–present). Technical Head at Forengers NGO (part-time). IIT Roorkee Executive PG Cert in Data Science & AI (July 2025). BE Chemical Engineering, SPPU.
- **Tech footprint:** Python-first, works across ML pipelines (LightGBM, Scikit-learn, ONNX, AWS SageMaker), full-stack web (FastAPI, Astro.js, React), cloud/devops (AWS EC2/Lambda/SageMaker, Docker, Vercel), data engineering (Pandas, Selenium, OpenCV, TesseractOCR).
- **Style chosen:** Rich & animated, dark theme. Audience: both recruiters and fellow developers equally.
- **Personal touch:** Short bio only. Hobbies intentionally light (badminton, staff spinning) — enough personality without overshadowing the technical content.
- **Featured projects:**
  - *PuneProp Predict* (`pune.adityajoshi.in`) — LightGBM price prediction + content-based recommendations, ONNX in-browser inference, Astro.js/React + Vercel
  - *Karnataka Elections Analysis* (`kea.adityajoshi.in`) — interactive political data journalism, 57k PDFs processed, Plotly visualizations, AWS EC2 + NGINX

## Constraints

- **Platform:** GitHub Markdown only — no React, no custom CSS beyond what GitHub renders. HTML `<img>` tags and `<div align="center">` work; JavaScript does not.
- **Animation:** Limited to SVG-based services (readme-typing-svg, shields.io, snake contribution graph). No JS animations.
- **Image hosting:** Use GitHub-served assets or reliable CDN services (shields.io, github-readme-typing-svg). Avoid self-hosted images that could break.
- **Length:** Profile README should be scannable — not a wall of text. Concise sections, visual hierarchy.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Badge-only, no stats cards | User prefers minimal dynamic elements — keeps profile clean | — Pending |
| Dark theme with neon accents | Matches dev aesthetic; consistent with rich & animated goal | — Pending |
| Two featured projects only | Walmart project excluded by user — quality over quantity | — Pending |
| Typing SVG for header animation | Best GitHub-compatible animation for role cycling | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-23 — Phase 1 complete*
