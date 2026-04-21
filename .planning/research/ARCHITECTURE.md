# Architecture Patterns: GitHub Profile README

**Project:** joshiaditya0511 GitHub Profile README
**Researched:** 2026-04-21
**Confidence basis:** GitHub documented HTML allowlist and `<picture>`-element patterns stable since ~2022; training data through Aug 2025. Verify against current GitHub docs before implementation.

---

## Recommended Layout

This layout is scoped to the exact six sections in PROJECT.md. Section ordering follows a recruiter-and-developer attention arc: identity first, technical proof second, discovery/contact last.

```
┌─────────────────────────────────────────┐
│  1. Animated Header (typing SVG)        │  ← Hook — first screen impression
│  2. Bio + Current Role callout          │  ← Context — who, where, what
│  3. Tech Stack Badges                   │  ← Proof — technologies, no prose
│  4. Featured Projects (PuneProp + KEA)  │  ← Depth — two project cards
│  5. Notes/Resources Callout             │  ← Discovery — DS/ML notes repo
│  6. Social/Contact Footer               │  ← Exit — where to go next
└─────────────────────────────────────────┘
```

---

## Section-by-Section Architecture

### Section 1: Animated Header

**Element:** `readme-typing-svg` via `https://readme-typing-svg.demolab.com`

**Markup pattern:**

```markdown
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=COLOR&center=true&vCenter=true&width=600&lines=Data+Scientist;ML+Engineer;Full-Stack+Developer" alt="Typing SVG" />
</div>
```

**Position:** Top of file, before any Markdown heading. This ensures it renders as the first visual element above the fold.

**Color param:** Set `color=` to the project's chosen neon accent hex (e.g., `58A6FF` for blue-neon, `00D9FF` for cyan). This decision must be made first — it propagates to badges. See Build Order below.

**Dark/light concern:** readme-typing-svg renders as an SVG with a transparent background. The text color is the only relevant parameter. A light-colored accent (neon cyan, neon blue) reads well on GitHub's dark background and has sufficient contrast on the light theme. Avoid pure white or pure black for text color.

---

### Section 2: Bio + Current Role Callout

**Element:** Centered Markdown paragraph with optional role-emphasis using bold or `<kbd>` tags.

**Markup pattern:**

```markdown
<div align="center">

**Data Scientist · ML Engineer · Full-Stack Developer**

I sit at the intersection of data science and software engineering — building systems that are both analytically rigorous and production-ready.

</div>
```

For the current role callout, a simple line break + bold prose is sufficient. A `<table>` with role/org columns can be used if the callout needs visual structure, but for two roles (Revcloud + Forengers), inline prose or two bold lines is cleaner and more mobile-friendly.

**Position:** Immediately below the typing SVG. Same centered container or a new one. Keep to 3–5 lines maximum.

---

### Section 3: Tech Stack Badges

**Element:** Shields.io badges as inline `<img>` tags, grouped by category in centered `<div>` blocks.

**Markup pattern:**

```markdown
<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
...

</div>
```

**Grouping approach:** Stack multiple `<div align="center">` blocks, one per category (e.g., ML/Data, Web, Cloud, Data Engineering). Separate with a blank line between groups and an optional small bold category label above each group. This creates implicit visual rows without requiring a `<table>`.

**Badge parameters for dark/light compatibility:** Use `style=for-the-badge` (high contrast), set `logoColor=white`, and choose `color=` (background) that is a saturated mid-range hex visible on both light and dark backgrounds. Avoid very light badge backgrounds (e.g., `FFFFFF`, `F5F5F5`) which disappear on GitHub's light theme or look flat. Shields.io does not require a `<picture>` wrapper per badge — parameter tuning alone achieves cross-theme readability.

**Do not use:** `style=flat` (too small for profile pages), or `&theme=dark` as a suffix (not a real shields.io parameter — `labelColor` and `color` are the correct params).

---

### Section 4: Featured Projects

**Element:** `<table>` with two `<td>` columns for side-by-side project cards. Each card is a Markdown block inside a `<td>`.

**CRITICAL parser rule:** HTML tags must be flush-left (no leading spaces or indentation). A blank line is required immediately after the opening `<td>` tag before any Markdown content. Markdown content inside `<td>` must have no leading whitespace. Indented `<td>` tags or indented content inside `<td>` can cause the Markdown parser to treat content as a code block or render raw HTML instead of parsed Markdown.

**Markup pattern:**

```markdown
## Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### PuneProp Predict
[`pune.adityajoshi.in`](https://pune.adityajoshi.in)

LightGBM price prediction with content-based recommendations and ONNX in-browser inference.

![LightGBM](https://img.shields.io/badge/LightGBM-2c7bb6?style=flat-square&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX-005CED?style=flat-square&logoColor=white)

</td>
<td width="50%" valign="top">

### Karnataka Elections Analysis
[`kea.adityajoshi.in`](https://kea.adityajoshi.in)

Interactive political data journalism: 57k PDFs processed, Plotly visualizations, AWS EC2 + NGINX.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

</td>
</tr>
</table>
```

**Why `<table>` not two-column Markdown:** GitHub Markdown has no native multi-column layout. `<table>` is the only supported mechanism for side-by-side content.

**Column width:** `width="50%"` on each `<td>` ensures equal split on desktop. On mobile (narrow viewport), two-column tables may squish columns or scroll horizontally depending on content width. For a 2-column layout this is acceptable; the columns remain readable. 3+ column tables are problematic on mobile.

**No screenshots:** PROJECT.md constrains to GitHub-native or CDN-hosted assets only. Self-hosted project screenshots break when the hosting changes. Use text description + badges only.

**`style=flat-square`** for project card badges: Slightly smaller than `for-the-badge`, fits better inside the constrained `<td>` column without wrapping as aggressively.

---

### Section 5: Notes/Resources Callout

**Element:** Short centered text block with a prominent linked resource badge or plain Markdown link.

**Markup pattern:**

```markdown
<div align="center">

**DS/ML Notes & Resources**

A living collection of notes, implementations, and references from my data science journey.

[![Notes Repo](https://img.shields.io/badge/View%20Notes-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joshiaditya0511/ds-ml-notes)

</div>
```

**Position:** After featured projects, before social footer. Acts as a soft discovery call-to-action without being the primary CTA (that role belongs to the social links).

---

### Section 6: Social/Contact Footer

**Element:** Row of linked badges for each social channel, centered.

**Markup pattern:**

```markdown
<div align="center">

[![Personal Site](https://img.shields.io/badge/Website-FF5722?style=for-the-badge&logo=About.me&logoColor=white)](https://adityajoshi.in)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/joshiaditya0511)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joshiaditya0511@gmail.com)

</div>
```

**Position:** Last section. GitHub profile pages show a truncated view on initial load — the footer reliably appears when a visitor scrolls down; it should not be relied upon for critical first-impression information.

---

## Section Dividers and Visual Hierarchy

GitHub Markdown supports a limited but sufficient set of divider techniques:

| Technique | Syntax | Use case |
|-----------|--------|----------|
| Horizontal rule | `---` on its own line | Major section breaks between H2 headings |
| `<br>` | `<br>` | Extra vertical spacing within a `<div>` block |
| Blank line between divs | (blank line) | Required for Markdown to parse inside HTML containers |
| Bold category labels | `**Category**` | Sub-grouping within tech stack section |
| `<div align="center">` | HTML | Centering blocks; `style="text-align:center"` is stripped |
| `<kbd>` | `<kbd>text</kbd>` | Inline emphasis for short labels (role titles, location) |

**H2 headings** (`##`) anchor sections and appear in GitHub's rendered page structure. Use `##` for major sections (Tech Stack, Featured Projects, etc.) and `###` within project cards.

**Do not use** `<div style="...">` or `<span style="...">` — GitHub's sanitizer strips all `style=` attributes.

---

## Dark Mode and Light Mode Compatibility

### The `<picture>` element approach (for themed images)

GitHub supports the `<picture>` HTML element with `prefers-color-scheme` media queries. This is the documented approach for serving different images per theme (e.g., a dark-background logo vs. a light-background logo):

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://example.com/logo-dark.svg">
  <img src="https://example.com/logo-light.svg" alt="Logo" width="200">
</picture>
```

**Confidence:** HIGH that the pattern is supported; MEDIUM that it is currently the active recommendation (verify in GitHub docs — the deprecated `#gh-dark-mode-only` URL fragment may still appear in older resources, do not use it).

**For this README:** The `<picture>` element is unlikely to be needed. No custom logo or hero image is planned. The primary theme-sensitive elements are:
- Typing SVG (handled via color param)
- Shields.io badges (handled via `color=` and `logoColor=` params)

### Shields.io badge dark/light compatibility

Shields.io badges do not respond to `prefers-color-scheme` natively. They are static images with fixed colors. Strategy:

1. **Use saturated, medium-brightness badge backgrounds** (`0D1117` is too dark on dark theme; `FFFFFF` is invisible on light; aim for brand colors like `3776AB`, `009688`, `FF6F00`)
2. **Always set `logoColor=white`** — white logos read on all backgrounds
3. **Avoid `labelColor=` that creates very light left halves** — they look washed out on light theme

This parameterization approach makes a single badge render acceptably in both themes without `<picture>` wrappers.

### Typing SVG color

Pick a neon accent color that:
- Has sufficient contrast on GitHub dark background (`#0D1117` or `#161B22`)
- Has sufficient contrast on GitHub light background (`#FFFFFF` or `#F6F8FA`)
- Examples that work well in both: `00D9FF` (cyan), `58A6FF` (blue), `7CFC00` (green-neon — caution, lower contrast on light)
- Examples that fail on light: `FFFFFF` (invisible), `E0E0E0` (near-invisible), `00FF00` (harsh on both)

The accent hex must be decided before implementing badges and typing SVG — it is a global dependency.

---

## Mobile Rendering Considerations

| Element | Desktop behavior | Mobile behavior | Mitigation |
|---------|-----------------|-----------------|------------|
| `<div align="center">` blocks | Centered, full width | Centered, full width | None needed |
| Inline badge rows | Wrap naturally | Wrap naturally | None needed — wrapping is fine |
| 2-column `<table>` | Side-by-side | Columns squish or scroll on very narrow screens | Acceptable for 2 columns; avoid 3+ |
| `<img width="...">` | Respected | Scales down proportionally | Keep images at ≤600px width |
| Markdown `---` | Thin rule | Thin rule | None |
| `<details>`/`<summary>` | Expandable | Expandable on mobile browser; mobile app support may vary | Do not rely on for critical content |
| Long prose lines | Wraps at column | Wraps at column | None needed |

**Key constraint:** GitHub applies responsive CSS globally — `<img width="600">` renders at 600px on desktop and scales down proportionally on narrow screens. Do not set widths above 800px for inline images.

**Typing SVG:** The `width=` param in the URL should match the intended display width. `width=600` is a safe default.

---

## Build Order and Section Dependencies

Dependencies flow top-to-bottom. Lock upstream decisions before implementing downstream elements.

```
1. Choose accent color hex
      │
      ├─► Typing SVG color= param
      └─► All shields.io badge color= params

2. Confirm dark/light badge param strategy (saturated colors + logoColor=white)
      │
      └─► Badge rows in Section 3 (Tech Stack) and Section 4 (Project cards)

3. Confirm live URLs
      │  (already confirmed: pune.adityajoshi.in, kea.adityajoshi.in, adityajoshi.in)
      └─► Section 4 project card links + Section 6 social footer links

4. Write section text content (bio, role callout, project descriptions)
      │
      └─► Section 2 and Section 4 prose

5. Assemble layout (combine sections 1–6 in order)
      │
      └─► Full README

6. Mobile check (render in browser + GitHub mobile app or narrow window)
      │
      └─► Adjust table widths, image widths, badge row density if needed
```

**No circular dependencies.** Accent color is the single root dependency.

---

## Supported HTML Elements in GitHub Markdown

The following HTML elements survive GitHub's sanitizer (HIGH confidence — GitHub's allowlist is well-documented and stable):

| Element | Supported | Notes |
|---------|-----------|-------|
| `<div align="center">` | Yes | `style=` attribute stripped; `align=` preserved |
| `<img width="..." height="..." src="..." alt="...">` | Yes | `style=` stripped; width/height attributes preserved |
| `<picture>` + `<source>` | Yes | Enables `prefers-color-scheme` dark/light image swapping |
| `<table>`, `<tr>`, `<td>`, `<th>` | Yes | Standard table layout; primary multi-column tool |
| `<details>` + `<summary>` | Yes | Collapsible sections |
| `<br>` | Yes | Inline line break |
| `<hr>` | Yes | Same as Markdown `---` |
| `<kbd>` | Yes | Keyboard-key rendering style |
| `<a href="...">` | Yes | Links |
| `<strong>`, `<em>`, `<code>` | Yes | Inline formatting |
| `<script>` | No — stripped | No JS |
| `<style>` | No — stripped | No CSS injection |
| `<iframe>` | No — stripped | No embeds |
| `style="..."` attribute | No — stripped | On any element |

---

## Anti-Patterns

| Anti-pattern | What goes wrong | What to do instead |
|--------------|----------------|-------------------|
| Indented `<td>` or `<tr>` tags | GitHub's Markdown parser treats indented HTML as code blocks; Markdown inside `<td>` fails to render | Use flush-left HTML tags; blank line required after `<td>` before content |
| `style="color: #..."` on any tag | GitHub sanitizer strips all `style=` | Use `align=` attr on divs, width/height attrs on imgs |
| GitHub stats/streak cards | Excluded per PROJECT.md; adds dynamic dependencies | Badge-only approach per project decision |
| More than 2 table columns for project cards | Overflows on mobile; becomes unreadable | 2-column max; stack vertically if 3+ projects |
| Self-hosted project screenshots | Breaks when hosting changes; excluded by PROJECT.md constraint | Text description + badges only |
| `#gh-dark-mode-only` URL fragment | Deprecated approach — do not build on it | Use `<picture>` + `prefers-color-scheme` for themed images |
| Very dark badge colors (`#0D1117`) | Invisible on dark theme profile background | Use saturated mid-range brand colors |
| Typing SVG `width=` mismatch | SVG clips or overflows its container | Set `width=` in URL to match `<img width="">` attribute |
| Raw GitHub URL for assets in other repos | Camo proxy can delay; URLs may break on branch changes | Use shields.io or readme-typing-svg CDN; avoid raw.githubusercontent for decorative assets |

---

## Sources

- GitHub documentation: "Managing your profile README" and "Basic writing and formatting syntax" — verify `<picture>` element support status against current docs before implementation
- GitHub's HTML sanitizer allowlist documented in `github/markup` and `jch/html-pipeline` repositories; stable since ~2022
- shields.io documentation: `https://shields.io` — badge parameter reference
- readme-typing-svg: `https://github.com/DenverCoder1/readme-typing-svg` — param reference for `color=`, `width=`, `center=`, `vCenter=`
- Confidence: HIGH for HTML element support (stable, well-documented); MEDIUM for `<picture>` being current best practice (verify deprecation status of `#gh-dark-mode-only`); HIGH for shields.io param approach
