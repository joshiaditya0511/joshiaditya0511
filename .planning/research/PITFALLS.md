# Domain Pitfalls: GitHub Profile README

**Domain:** GitHub profile README (animated, dark-themed, badge-based)
**Project:** joshiaditya0511 GitHub profile
**Researched:** 2026-04-21
**Confidence:** HIGH — based on well-documented behaviors of the specific services in use

---

## Critical Pitfalls

Mistakes that cause visible breakage, permanent staleness, or a degraded first impression.

---

### Pitfall 1: SVG Background Opacity Clash (Dark/Light Mode)

**What goes wrong:** GitHub renders profiles in both light and dark mode. An SVG or image with a hardcoded white (`#ffffff`) or light background looks correct in light mode but creates a jarring white box on dark mode. The inverse is equally bad — dark backgrounds on light mode. This affects custom SVG cards, shields.io badges with custom label colors, and any externally-hosted image.

**Why it happens:** The author previews only in their current theme. The image is authored assuming a fixed background. `<img>` tags in GitHub Markdown do not inherit the page theme — they render exactly as served.

**Consequences:** The entire dark aesthetic collapses. White boxes appear around every image, undermining the visual identity before the visitor reads a single word.

**Prevention:**
- Use `style="background:transparent"` is not possible in GitHub Markdown — transparency must be baked into the SVG/image itself.
- For SVGs: ensure the root `<svg>` element has no `background` or `fill` attribute on the outermost rect, or explicitly uses `fill="none"`.
- For shields.io badges: they use transparent backgrounds by default — do not apply custom `labelColor` or `color` values that are pure white or near-white.
- For the typing SVG (readme-typing-svg): use `background=transparent` parameter explicitly. The default is transparent but confirm this when copying URL templates from third-party generators.
- GitHub supports `<picture>` with `prefers-color-scheme` for serving different images per theme — use this for any custom card SVGs that require colored backgrounds.
- Test in both themes using GitHub's theme switcher (Settings → Appearance) before publishing.

**Detection:** Open the profile in GitHub's light mode AND dark mode after any image/SVG is added. Check for white rectangular halos.

**Phase relevance:** Header animation section, tech stack badges section, featured project cards.

---

### Pitfall 2: readme-typing-svg URL Parameter Errors Producing Blank/Broken Header

**What goes wrong:** The `readme-typing-svg` service (`readme-typing-svg.demolab.com`) is sensitive to URL encoding. Common errors: unencoded `+` or `&` in the `lines` parameter, missing `pause` parameter causing no pause between rotations, or `duration` vs `speed` parameter name confusion (the service uses `speed`, not `duration`). The result is either a blank SVG frame, garbled text mid-animation, or text that scrolls without pause.

**Why it happens:** Most people copy a URL from a README generator tool, then hand-edit the `lines` parameter to add their own roles. The edited URL silently breaks when special characters aren't encoded, or when the wrong parameter name is used because documentation was read from an outdated source.

**Consequences:** The headline animation — the single most eye-catching element — shows nothing or garbage. First impression is immediately broken.

**Prevention:**
- Always URL-encode commas as `%2C` and pipes (`|`) as `%7C` when they appear within a `lines` value.
- Use the service's own demo builder at `readme-typing-svg.demolab.com` to generate the URL, then copy the output verbatim — do not hand-construct.
- Test the raw SVG URL directly in a browser tab before embedding: the SVG should render and animate correctly in isolation.
- The correct parameter for animation speed is `speed` (characters per second), not `duration`.
- Wrap the `<img>` tag in a `<div align="center">` to confirm the element renders at all before styling.

**Detection:** Paste the raw SVG URL into a browser. If it shows a blank white/transparent rectangle with no text, a parameter is wrong.

**Phase relevance:** Header animation section. Must be validated before any other section is built around it.

---

### Pitfall 3: shields.io Badge Logo Names That No Longer Resolve

**What goes wrong:** shields.io badges support a `logo=` parameter using Simple Icons slugs. Simple Icons periodically renames slugs when a brand changes its name or capitalization. Badges using renamed slugs silently drop their icon and show a broken logo placeholder, or more often simply omit the icon with no visible error.

**Specific examples of historically problematic slugs:** `amazonaws` (correct) vs `aws` (incorrect); `scikitlearn` (correct) vs `scikit-learn` (incorrect — hyphens are not valid in Simple Icons slugs); `onnx` (correct since added in 2022); `lightgbm` (not in Simple Icons as of mid-2025 — use a fallback custom icon or omit the logo).

**Why it happens:** Copying badge Markdown from old READMEs or generator sites that reference stale slug names.

**Consequences:** Tech stack section has inconsistently-sized badges (some with icons, some without), destroying the visual uniformity that makes badge grids impressive.

**Prevention:**
- Cross-reference every `logo=` value against the current Simple Icons slug list at `simpleicons.org` before use. The slug is the page title lowercased with spaces removed.
- For technologies not in Simple Icons (LightGBM, ONNX, TesseractOCR, SageMaker): either omit the logo and rely on the text label, or use `logo=data:image/svg+xml;base64,...` with an inline SVG if a small branded icon is available.
- `logo=amazonsagemaker` is the correct slug for AWS SageMaker (uses the Amazon prefix, not AWS).
- Render all badges in a preview before committing — check every icon appears as expected.

**Detection:** In the rendered README, any badge missing its icon while adjacent badges show icons correctly. The badge text will still appear, but the left icon slot will be empty.

**Phase relevance:** Tech stack badges section.

---

### Pitfall 4: HTML Centering That Works Locally But Breaks on GitHub

**What goes wrong:** GitHub's Markdown renderer sanitizes HTML. It permits `<div align="center">`, `<p align="center">`, and `<img>` tags, but strips `style=` attributes, `class=` attributes, and any non-allowlisted HTML elements (`<span>`, `<figure>`, `<section>`, etc.). Developers often write richer HTML locally (using a Markdown previewer that does not apply GitHub's sanitizer) and find it stripped to plain text on the actual profile.

**Why it happens:** VS Code's built-in Markdown preview, Typora, and most browser-based Markdown previewers do NOT apply GitHub's sanitization rules. What renders fine locally can be stripped completely on GitHub.

**Consequences:** Layout falls apart. Centered sections become left-aligned. Custom colors via `style="color:#..."` are silently removed. Tables of images using nested `<div>` elements collapse.

**Prevention:**
- Only use `align="center"` attribute on `<div>`, `<p>`, and `<td>` — this attribute is allowlisted.
- Do not use `style=` on any HTML element — GitHub strips it.
- Do not use `<span>` with color or font attributes.
- Use `<br>` for line breaks (allowlisted), not `<br/>` vs `<br />` — either works but be consistent.
- The only reliable preview is GitHub itself: push to a branch and view the rendered README at `github.com/[user]/[repo]/blob/[branch]/README.md` before merging to main.
- Alternatively, use the GitHub REST API endpoint `POST /markdown` to test rendering without pushing.

**Detection:** Preview directly on GitHub. If sections are left-aligned that should be centered, an HTML element is being stripped.

**Phase relevance:** All sections using `<div align="center">`, especially the header and project cards.

---

### Pitfall 5: Overcrowding — Badge Grid Becomes Visual Noise

**What goes wrong:** The tech stack section lists every technology the developer has ever touched, resulting in 40–60 badges across 6+ rows. The visual signal collapses — the eye cannot find a focal point, and the section communicates "I've heard of many things" rather than "I'm expert in these specific things."

**Why it happens:** It feels like omitting a technology is underselling skills. The README generator tools make it trivially easy to add badges — no cost per badge creates no incentive to curate.

**Consequences:** Recruiters skim past. Fellow developers get no clear read on the developer's actual stack. The dark neon aesthetic is overwhelmed by a wall of multi-colored rectangles.

**Prevention:**
- Group badges by category (Languages, ML/AI, Web, Cloud, Tools) and cap each group at 6–8 badges maximum.
- Include only technologies used in the featured projects or currently used professionally — the projects themselves are the evidence, the badges are the index.
- For Aditya's profile specifically: Python, FastAPI, Astro.js, React, AWS (SageMaker/EC2/Lambda), Docker, LightGBM/Scikit-learn are the load-bearing skills. Supporting tools (Pandas, Selenium, OpenCV) are secondary and could be grouped or omitted.
- Use consistent badge `style=` values (prefer `flat-square` or `for-the-badge` — pick one and do not mix).

**Detection:** Count total badges. More than 30 is an overcrowding risk. More than 40 is certain visual noise.

**Phase relevance:** Tech stack badges section — enforce curation during initial drafting.

---

### Pitfall 6: Featured Project Cards That Require External Hosting

**What goes wrong:** Developers create project cards as PNG/SVG images hosted on personal servers, AWS S3, or third-party image hosting. When the server is down, the CDN URL changes, or the hosting bill lapses, the cards show broken image icons. The README becomes permanently degraded with no easy fix.

**Why it happens:** Richer visuals (custom fonts, gradients, real screenshots) require external image generation. The developer optimizes for aesthetics at authoring time and ignores hosting permanence.

**Consequences:** Featured projects section — the most important section for demonstrating work — shows broken images to every visitor indefinitely until the author notices and fixes it.

**Prevention:**
- For this project: use pure Markdown tables or HTML tables with `<a>` + `<img>` linking to **GitHub-hosted** screenshots (uploaded via the GitHub UI to the repository's `/assets/` folder — these are served from `raw.githubusercontent.com` which has GitHub's uptime guarantee).
- If using SVG cards: embed them directly in the repository and reference with a relative path (`./assets/pune-prop-card.svg`). GitHub renders repository-local SVGs reliably.
- Avoid linking to `adityajoshi.in` subdomains for images — these are personal-domain hosted and can go down or change.
- Live website URLs (`pune.adityajoshi.in`, `kea.adityajoshi.in`) in text links are acceptable — a dead link is less damaging than a broken image placeholder.

**Detection:** Replace the image URL with a known-bad URL and confirm the fallback (`alt` text) is meaningful. Then verify the actual URL returns 200 with a `Content-Type: image/*` response.

**Phase relevance:** Featured projects section.

---

## Moderate Pitfalls

---

### Pitfall 7: Typing SVG `lines` Parameter Truncated by URL Length Limits

**What goes wrong:** `readme-typing-svg` encodes all cycling text into the URL query string. When adding many roles or long phrases, the URL exceeds the GitHub Markdown renderer's safe URL length (~2000 characters), causing the image to fail silently or load the first line only.

**Prevention:** Keep each line in the `lines` parameter under 40 characters and use no more than 5–6 rotating lines. For Aditya's three roles ("Data Scientist · ML Engineer · Full-Stack Developer"), this is well within limits. Verify by counting the final encoded URL character length.

**Phase relevance:** Header animation.

---

### Pitfall 8: Hardcoded Role/Company Information That Goes Stale

**What goes wrong:** The README includes "Data Scientist at Revcloud" as a static string. When the role changes, it remains in the README indefinitely — a recruiter reads an outdated professional status. GitHub profile READMEs have no "last updated" timestamp visible to visitors.

**Prevention:** Keep job-specific callouts in a separate clearly-labeled section that is easy to find and update. Include the start date inline ("Data Scientist at Revcloud · Aug 2025–present") so staleness is self-evident. Set a calendar reminder to review the README at each job change. Avoid encoding the company name into the animated typing SVG — if the animation says "Data Scientist @ Revcloud" and the role changes, the SVG URL must be reconstructed entirely.

**Detection:** Check if role information is duplicated in multiple places — duplication increases maintenance burden.

**Phase relevance:** Bio/current role section.

---

### Pitfall 9: Inconsistent Badge Styles Across Sections

**What goes wrong:** The tech stack section uses `style=flat-square` badges, but badges copied from the project's own repositories or from other README generators use `style=flat` or `style=for-the-badge`. The mixed sizes and corner radii look amateurish.

**Prevention:** Define a single badge style before writing the first badge URL. `flat-square` is the most compact and cleanest for dense grids. `for-the-badge` is larger, bolder, better for 6–10 prominent badges but poor for large grids. Pick one. Enforce it across every badge URL in the file.

**Phase relevance:** Tech stack badges section.

---

### Pitfall 10: `<picture>` Tag Dark/Light Mode Switching Not Supported in All Contexts

**What goes wrong:** GitHub supports `<picture>` with `media="(prefers-color-scheme: dark)"` for switching images by theme. However, this only works when the image is viewed in the GitHub web UI. When the README is viewed in GitHub Mobile, the VS Code GitHub Pull Requests extension, or embedded in other tools, the `<picture>` media query may not apply and only one variant is shown.

**Prevention:** Prefer transparent-background SVGs over `<picture>` switching — a single transparent SVG looks acceptable in both modes. Reserve `<picture>` only for assets where the content meaningfully differs between themes (e.g., a diagram with white text on dark vs dark text on light). For badges and typing SVGs: test that the transparent variant is acceptable in both modes before reaching for `<picture>`.

**Phase relevance:** Header, any decorative SVG elements.

---

### Pitfall 11: Emoji Use That Renders as Missing Character on Some Systems

**What goes wrong:** GitHub renders emoji via its own Joypixels-based renderer, but some newer Unicode emoji (added after Unicode 15, i.e., 2023+) may render as a box or question mark on older systems viewing the raw Markdown or in certain GitHub integrations.

**Prevention:** Stick to common, high-coverage emoji (stars, circles, arrows, standard symbols). Avoid skin tone modifiers, very new emoji, or emoji sequences that require ZWJ (zero-width joiner). When in doubt, use GitHub's `:emoji_name:` syntax (`:star:`, `:zap:`) rather than the raw Unicode codepoint — GitHub's renderer maps these to its own CDN assets and guarantees display.

**Phase relevance:** Bio section, section headers.

---

## Minor Pitfalls

---

### Pitfall 12: GitHub Markdown Table Rendering for Project Cards

**What goes wrong:** Markdown tables are often used to create side-by-side project cards. GitHub renders `|` tables but does not allow HTML inside table cells in all contexts — specifically, nested `<div>` blocks inside table cells are unreliable and may collapse to plain text.

**Prevention:** Use `<table>` HTML directly (GitHub allows it) with `<td>` cells instead of Markdown `| |` table syntax when you need image + text combinations inside cells. Plain `<img>` tags inside `<td>` cells work; block-level `<div>` tags inside `<td>` cells do not.

**Phase relevance:** Featured projects section.

---

### Pitfall 13: Anchor Link IDs Conflicting With GitHub's Auto-Generated Heading IDs

**What goes wrong:** GitHub auto-generates `id` attributes for every heading, following a slug rule (lowercase, spaces to hyphens, special characters stripped). If the README has two headings with the same slug (e.g., two sections both named "Projects"), the second anchor link `#projects` becomes ambiguous. The page still renders but internal navigation (if any links to sections) breaks.

**Prevention:** Keep section headings unique and avoid relying on internal anchor links in a profile README — the page is short enough to scroll, and anchor links add maintenance complexity with no user benefit.

**Phase relevance:** All sections — ensure heading names are unique.

---

### Pitfall 14: Large Total README File Size Slowing Profile Load

**What goes wrong:** Embedding base64-encoded images directly in the Markdown (a common suggestion from README generators for "no external dependency" setups) results in a README file that is hundreds of kilobytes. GitHub has a soft rendering limit — READMEs over ~500KB may be truncated or warned.

**Prevention:** Never base64-encode images inline in the README. Always use URLs to externally-served assets (GitHub raw, shields.io, readme-typing-svg). For this project: the badge-only approach naturally avoids this — shields.io URLs are short strings.

**Phase relevance:** Any section where custom images are considered.

---

## Phase-Specific Warnings

| Phase / Section | Likely Pitfall | Mitigation |
|-----------------|---------------|------------|
| Header animation (typing SVG) | Blank SVG from bad URL parameters | Test raw URL in browser before embedding; use demolab builder |
| Header animation (typing SVG) | White background box in dark mode | Confirm `background=transparent` parameter is set |
| Tech stack badges | Missing icons from invalid Simple Icons slugs | Verify every `logo=` slug against simpleicons.org |
| Tech stack badges | Style inconsistency across badge rows | Choose one style (`flat-square` or `for-the-badge`) before writing first badge |
| Tech stack badges | Visual overcrowding | Cap each category at 8 badges; 30 total maximum |
| Featured projects | Broken images from external hosting | Host all images in repo `/assets/`; use relative paths |
| Featured projects | HTML in table cells not rendering | Use `<table><td>` HTML, not Markdown `| |` tables, for image+text combos |
| Bio/current role | Stale company name in animation | Keep role in editable text, not baked into SVG URL |
| All HTML sections | CSS stripped by GitHub sanitizer | Never use `style=` attribute; use only `align=` |
| All image elements | Dark/light mode clash | Test both themes; use transparent SVGs as first choice |

---

## Sources

- Knowledge drawn from GitHub's documented Markdown sanitization behavior (allowlist confirmed in github/markup and gjtorikian/html-pipeline repositories)
- shields.io badge URL schema and Simple Icons slug conventions (documented at shields.io/docs and simpleicons.org)
- readme-typing-svg service parameters (documented at readme-typing-svg.demolab.com)
- GitHub profile README rendering constraints confirmed against GitHub Docs: "About your profile README"
- Confidence: HIGH for all platform-specific rendering behavior (well-established, unchanged since 2022); MEDIUM for specific Simple Icons slug states (slug names change with brand updates — verify at authoring time)
