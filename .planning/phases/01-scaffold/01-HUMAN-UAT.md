---
status: partial
phase: 01-scaffold
source: [01-VERIFICATION.md]
started: 2026-04-23T00:00:00Z
updated: 2026-04-23T00:00:00Z
---

## Current Test

[awaiting human testing]

## Tests

### 1. GitHub Markdown rendering in light and dark themes
expected: Bio text, role callout with emoji, DS/ML notes badge + description line, and three social badges all render as formatted Markdown inside the centered divs — not as escaped HTML. The blank lines adjacent to each `<div align="center">` tag cause GitHub's renderer to process the contained Markdown inline.
result: [pending]

### 2. Social link resolution — click all three badge links
expected: Website badge opens https://adityajoshi.in. LinkedIn badge opens https://linkedin.com/in/joshiaditya0511. Email badge opens the system mail client addressed to contact@adityajoshi.in.
result: [pending]

### 3. VISUAL-05: Scannability and visual hierarchy as first-time visitor
expected: Visitor can parse the full profile in a single viewport scan — bio is one sentence, role callout is one line, notes callout is one badge plus one sentence, social footer is three badges. Sections feel distinct and hierarchically ordered.
result: [pending]

## Summary

total: 3
passed: 0
issues: 0
pending: 3
skipped: 0
blocked: 0

## Gaps
