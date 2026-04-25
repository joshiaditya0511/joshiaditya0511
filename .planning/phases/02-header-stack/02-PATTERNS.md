# Phase 2: Header & Stack — Pattern Map

**Mapped:** 2026-04-25
**Files analyzed:** 1 (README.md — two distinct edits)
**Analogs found:** 1 / 1 (Phase 1 content of the same file; no external analog exists)

---

## Note on This Phase

Phase 2 modifies a single static Markdown file. There are no controllers, services, or components. The role/data-flow taxonomy is adapted accordingly. The "codebase analog" is the Phase 1 content already in README.md. For elements that have no Phase 1 precedent (typing SVG header, emoji+label rows), RESEARCH.md §Code Examples is the authoritative reference.

---

## File Classification

| Modified File | Role | Data Flow | Closest Analog | Match Quality |
|---------------|------|-----------|----------------|---------------|
| `README.md` (edit 1: line 1 — replace `<!-- PHASE-2-HEADER -->`) | markdown-content | static-text | None in Phase 1; see RESEARCH.md §Code Examples → Typing SVG | no analog |
| `README.md` (edit 2: insert stack section between line 9 `</div>` and line 11 `---`) | markdown-content | static-text | `README.md` lines 23–29 (multi-badge centered div) | role-match |

---

## Pattern Assignments

### Edit 1: Replace `<!-- PHASE-2-HEADER -->` on line 1

**Analog:** None — line 1 is a placeholder comment with no Phase 1 structural precedent.

**Action for planner:** Copy the verified URL directly from RESEARCH.md §Code Examples → "Typing SVG — Recommended URL":

```markdown
<div align="center">
<img src="https://readme-typing-svg.demolab.com/render?font=Fira+Code&size=22&duration=1500&pause=750&color=58A6FF&center=true&vCenter=true&width=500&lines=Data+Scientist;ML+Engineer;Full-Stack+Developer" alt="Typing SVG" />
</div>
```

**Key constraints (no Phase 1 analog — all from RESEARCH.md):**
- `readme-typing-svg.demolab.com` endpoint only (D-05; herokuapp.com is dead)
- No `cursor=` param — cursor renders automatically, param does not exist
- No `background=` param — default `00000000` is already fully transparent
- `+` for spaces in `lines` param, `;` as role separator
- `color=58A6FF` (no `#` prefix in URL param)

---

### Edit 2: Insert stack section (between README.md line 9 `</div>` and line 11 `---`)

**Analog:** `README.md` lines 23–29 — the three-badge social row in a `<div align="center">` block. This is the closest Phase 1 match for a multi-badge centered section.

**Centered div wrapper pattern** (lines 23–29):
```markdown
<div align="center">

[![Website](https://img.shields.io/badge/Website-adityajoshi.in-58A6FF?style=for-the-badge&logoColor=white)](https://adityajoshi.in)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-joshiaditya0511-58A6FF?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/joshiaditya0511)
[![Email](https://img.shields.io/badge/Email-contact%40adityajoshi.in-58A6FF?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@adityajoshi.in)

</div>
```

**Key structural rule to copy:** Blank line immediately after `<div align="center">` opening tag and immediately before `</div>` closing tag. All three Phase 1 `<div>` blocks follow this pattern (lines 3–9, 13–19, 23–29).

**Badge URL anatomy to copy** (line 25 — accent color badge without logo):
```markdown
https://img.shields.io/badge/Website-adityajoshi.in-58A6FF?style=for-the-badge&logoColor=white
```
Decomposed: `[LABEL]-[VALUE]-[COLOR]?style=for-the-badge&logoColor=white` — no `logo=` param = text-only badge. This is exactly the text-only fallback pattern for LightGBM, XGBoost, and shadcn/ui (D-14, D-15, D-16).

**Badge URL anatomy to copy** (line 26 — badge with logo):
```markdown
https://img.shields.io/badge/LinkedIn-joshiaditya0511-58A6FF?style=for-the-badge&logo=linkedin&logoColor=white
```
Decomposed: `[LABEL]-[VALUE]-[COLOR]?style=for-the-badge&logo=[SLUG]&logoColor=white`. For stack badges the value segment is omitted (label-only format): `[LABEL]-[COLOR]?style=for-the-badge&logo=[SLUG]&logoColor=white`.

**URL encoding precedent** (line 15 — `DS%2FML%20Notes`):
```markdown
https://img.shields.io/badge/DS%2FML%20Notes-data--science--notes-58A6FF?style=for-the-badge&logo=github&logoColor=white
```
`%2F` encodes `/` — apply to `shadcn%2Fui` label. `%40` encodes `@` (line 27). `_` or `%20` for spaces in multi-word labels.

**Emoji + bold label rows:** No Phase 1 analog. Copy structure from RESEARCH.md §Architecture Patterns → "Recommended README Section Structure":
```markdown
📊 **ML / Data Science**

[badge row]

🛠️ **Web & Backend**

[badge row]

🚀 **Cloud & DevOps**

[badge row]
```
Labels go on their own line with a blank line separating each label from the badge row below it, all inside a single `<div align="center">` wrapper.

**HR divider rhythm** (lines 11, 21 — `---` on its own line with blank lines either side):
```markdown

---

```
The stack section inserts *before* the existing `---` on line 11 (which precedes the Notes callout). Stack section structure: `</div>` → blank → `---` → blank → `<div align="center">` [stack content] `</div>` → blank → `---` [Notes callout existing divider].

---

## Shared Patterns

### `<div>` Centering
**Source:** `README.md` lines 3, 13, 23 (all three Phase 1 div blocks)
**Apply to:** Both the typing SVG wrapper (edit 1) and the stack section wrapper (edit 2)
```markdown
<div align="center">
```
Rule: `align="center"` attribute on `<div>` only. Never `style=` attributes anywhere — GitHub sanitizer strips them (STATE.md Critical Technical Notes).

### Accent Color in Badges
**Source:** `README.md` lines 15, 25, 26, 27
**Apply to:** All ML/Data Science group badges (D-10), Website badge in social (precedent)
```
color=58A6FF
```
No `#` prefix in URL params. Accent `58A6FF` used for ML group and all custom-color overrides.

### `for-the-badge` Style on All Stack Rows
**Source:** `README.md` lines 15, 25, 26, 27 — every Phase 1 standalone badge
**Apply to:** All 15 tech stack badges in edit 2
```
?style=for-the-badge
```

### `logoColor=white` on All Badged Items
**Source:** `README.md` lines 15, 26, 27
**Apply to:** All stack badges (both logo and text-only variants)
```
&logoColor=white
```

### Blank Line Padding Inside `<div>` Blocks
**Source:** `README.md` lines 3–9 structure
**Apply to:** Stack section `<div align="center">` wrapper
```markdown
<div align="center">
                     ← blank line here
[content]
                     ← blank line here
</div>
```

---

## No Analog Found

| Edit | Role | Data Flow | Reason |
|------|------|-----------|--------|
| Edit 1: Typing SVG `<img>` header | markdown-content | static-text | No `<img>` or external SVG service used anywhere in Phase 1; line 1 is a comment placeholder |
| Emoji + bold label rows (`📊 **ML / Data Science**`) | markdown-content | static-text | No label-then-row stacking pattern exists in Phase 1 |

**Planner fallback for these:** Use RESEARCH.md §Code Examples verbatim. The research document contains verified, ready-to-paste URL patterns for both the typing SVG and all 15 badge URLs.

---

## Metadata

**Analog search scope:** `README.md` (sole source file); `.planning/STATE.md`, `.planning/phases/02-header-stack/02-CONTEXT.md`, `.planning/phases/02-header-stack/02-RESEARCH.md`
**Files scanned:** 4
**Pattern extraction date:** 2026-04-25
