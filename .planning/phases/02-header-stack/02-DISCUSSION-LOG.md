# Phase 2: Header & Stack - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-23
**Phase:** 02-header-stack
**Areas discussed:** Header animation feel, Stack section placement, Stack group label style, shadcn/ui badge handling

---

## Header Animation Feel

| Option | Description | Selected |
|--------|-------------|----------|
| Fast & snappy | ~60–80ms per character, energetic | ✓ |
| Deliberate & readable | ~100–120ms per character, cinematic | |
| You decide | Claude picks default | |

**Pause between roles:**

| Option | Description | Selected |
|--------|-------------|----------|
| Yes — pause noticeably | ~2–3s pause after each role | |
| Minimal pause | ~0.5–1s, constant-motion feel | ✓ |

**Cursor:**

| Option | Description | Selected |
|--------|-------------|----------|
| Yes, cursor visible | Blinking `\|` during typing/erasing | ✓ |
| No cursor | Cleaner, no blinking element | |
| You decide | Claude decides | |

**User's choice:** Fast typing speed, minimal pause between cycles, cursor visible.
**Notes:** No additional clarifications.

---

## Stack Section Placement

| Option | Description | Selected |
|--------|-------------|----------|
| Header → Bio → Stack → Notes → Social | Resume-like reading order | ✓ |
| Header → Bio → Notes → Stack → Social | Notes before skills | |

**User's choice:** Stack immediately after Bio — Header → Bio → Stack → Notes → Social.
**Notes:** No additional clarifications.

---

## Stack Group Label Style

**Label style:**

| Option | Description | Selected |
|--------|-------------|----------|
| Bold Markdown text | `**ML / Data Science**` on its own line | |
| Emoji + bold text | e.g., 🧠 **ML / Data Science** | ✓ |
| You decide | Claude picks the style | |

**Emoji set:**

| Option | Description | Selected |
|--------|-------------|----------|
| 🧠 / 🌐 / ☁️ | Brain / Globe / Cloud — semantic | |
| 📊 / 🛠️ / 🚀 | Chart / Wrench / Rocket — tool/action oriented | ✓ |
| You decide | Claude picks | |

**User's choice:** Emoji + bold text; emojis: 📊 ML/Data Science, 🛠️ Web & Backend, 🚀 Cloud & DevOps.
**Notes:** No additional clarifications.

---

## shadcn/ui Badge Handling

| Option | Description | Selected |
|--------|-------------|----------|
| Text-only badge, same as LightGBM/XGBoost | Consistent with STACK-06 fallback pattern | ✓ |
| Skip it from Web group | Don't include shadcn/ui | |
| Custom logo URL | Pass SVG via shields.io `logo=` base64 | |

**User's choice:** Text-only badge, consistent with LightGBM/XGBoost STACK-06 pattern.
**Notes:** No additional clarifications.

---

## Claude's Discretion

- Exact `readme-typing-svg` param values (speed, duration, pause ms)
- Fallback badge colors for text-only entries
- Simple-icons slug verification for remaining ambiguous slugs

## Deferred Ideas

None.
