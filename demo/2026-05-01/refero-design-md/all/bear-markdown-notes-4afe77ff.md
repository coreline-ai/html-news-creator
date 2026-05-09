# Bear Markdown Notes - Refero Design MD

- Source: https://styles.refero.design/style/4afe77ff-e7fa-41d8-96d6-ce8cdc159f97
- Original site: https://bear.app
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Notebook Page — where every element is legible and inviting.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Bear Red | `#dd4c4f` | brand | Action accent / signal color |
| Blueprint Blue | `#456aa3` | accent | Action accent / signal color |
| Leaf Green | `#2b6451` | accent | Action accent / signal color |
| Orchid Pink | `#884aa8` | accent | Action accent / signal color |
| Content Teal | `#9fd7e4` | accent | Action accent / signal color |
| Highlight Yellow | `#fcb827` | semantic | Action accent / signal color |
| Badge Blue | `#44a2e5` | semantic | Action accent / signal color |
| Ink Black | `#444444` | neutral | Border, muted text, or supporting surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f3f5f7` | neutral | Page background or card surface |

```css
:root {
  --ref-bear-red: #dd4c4f;
  --ref-blueprint-blue: #456aa3;
  --ref-leaf-green: #2b6451;
  --ref-orchid-pink: #884aa8;
  --ref-content-teal: #9fd7e4;
  --ref-highlight-yellow: #fcb827;
  --ref-badge-blue: #44a2e5;
  --ref-ink-black: #444444;
}
```

## Typography direction
- **bearsansheadline**: 400, 16px, 30px, 42px, 51px, 1.10, 1.70, 1.80; substitute `system-ui`.
- **bearsans**: 400, 700, 13px, 14px, 16px, 18px, 19px, 20px, 22px, 24px, 29px, 40px, 1.13, 1.20, 1.36, 1.40, 1.42, 1.45, 1.60, 1.70, 1.80, 1.89; substitute `system-ui`.

## Spacing / shape
- Element Gap: `11px`
- Page Max Width: `960px`
- Radius: `badges: 3.84px, default: 8px, largeItems: 16px, organicShapes: 40px`

## Component cues
- **Pricing Cards — Free vs Bear Pro**: Reference component style.
- **Platform Selector Tabs**: Reference component style.
- **Awards Row**: Reference component style.
- **Primary Navigation Link**: Navigation
- **Basic Input Field**: Form Element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
