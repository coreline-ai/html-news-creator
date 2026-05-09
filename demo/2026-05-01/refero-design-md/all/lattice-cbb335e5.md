# Lattice - Refero Design MD

- Source: https://styles.refero.design/style/cbb335e5-c8df-49be-a0fc-0ec5dfa0d61f
- Original site: https://lattice.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gradient-kissed productivity palette: an orderly white canvas brought to life by vibrant, organic color washes and structured forms.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Matter Black | `#001f1f` | neutral | Primary text or dark surface |
| Sandstone | `#f7f6f2` | neutral | Page background or card surface |
| Ash Gray | `#6a7878` | neutral | Border, muted text, or supporting surface |
| Slate Gray | `#455252` | neutral | Border, muted text, or supporting surface |
| Pale Green | `#cdface` | brand | Action accent / signal color |
| Forest Green | `#366625` | brand | Action accent / signal color |
| Teal Ink | `#006666` | brand | Action accent / signal color |
| Oceanic Teal | `#003d3d` | accent | Action accent / signal color |
| Moss Green | `#515c0b` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-matter-black: #001f1f;
  --ref-sandstone: #f7f6f2;
  --ref-ash-gray: #6a7878;
  --ref-slate-gray: #455252;
  --ref-pale-green: #cdface;
  --ref-forest-green: #366625;
  --ref-teal-ink: #006666;
}
```

## Typography direction
- **Matter**: 400, 500, 11px, 13px, 14px, 16px, 17px, 18px, 19px, 22px, 47px, 72px, 0.90, 1.00, 1.10, 1.20, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `58px`
- Element Gap: `7px`
- Page Max Width: `1299px`
- Radius: `pill: 9999px, cards: 21.6576px, badges: 21.6576px, buttons: 28.8768px, default: 14.4384px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page and content background.
- **Sandstone** `#f7f6f2`: Secondary background for sections and cards that need subtle visual separation.
- **Violet Echo Card** `#624ee5`: Distinct card background for highlighted content, often with a subtle shadow.

## Component cues
- **Primary Filled Button**: Call to Action
- **Ghost Button**: Secondary Action
- **Navigation Link Button**: Navigation Item
- **Accent Gradient Hero Card**: Showcase Card
- **Testimonial Card**: Content Showcase

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
