# Payments - Refero Design MD

- Source: https://styles.refero.design/style/123a15b8-4e17-4812-83ec-899cce45db5b
- Original site: https://lemonsqueezy.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Grape Soda & Lemon Zest. A bold purple lake with bright yellow accents floating atop.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Grape Soda | `#5423e7` | brand | Action accent / signal color |
| Lemon Zest | `#ffc233` | brand | Action accent / signal color |
| Forest Canopy | `#1e874c` | semantic | Action accent / signal color |
| Ocean Deep | `#0075ad` | semantic | Action accent / signal color |
| Bubblegum Pink | `#cf75ff` | accent | Action accent / signal color |
| Midnight Ink | `#121217` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Driftwood | `#6c6c89` | neutral | Border, muted text, or supporting surface |
| Parchment | `#f7f7f8` | neutral | Page background or card surface |
| Cloud Grey | `#d1d1db` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-grape-soda: #5423e7;
  --ref-lemon-zest: #ffc233;
  --ref-forest-canopy: #1e874c;
  --ref-ocean-deep: #0075ad;
  --ref-bubblegum-pink: #cf75ff;
  --ref-midnight-ink: #121217;
  --ref-ghost-white: #ffffff;
  --ref-driftwood: #6c6c89;
}
```

## Typography direction
- **Circularpro Book**: 400, 18px, 26px, 36px, 38px, 48px, 56px, 80px, 1.00, 1.13, 1.14, 1.20, 1.22, 1.25; substitute `Montserrat, Gotham`.
- **Inter**: 400, 500, 14px, 15px, 16px, 18px, 1.29, 1.40, 1.60, 1.70, 1.80; substitute `Inter`.
- **Inter**: 400, 500, 14px, 15px, 16px, 18px, 1.29, 1.40, 1.60, 1.70, 1.80; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `0px`
- Element Gap: `8-16px`
- Page Max Width: `1233px`
- Radius: `cards: 48px, other: 20px, buttons: 8px, navigation: 40px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Button Group**: Reference component style.
- **Feature List Section**: Reference component style.
- **Primary Call to Action Button**: Primary interactive element.
- **Outline Button - Default**: Secondary and tertiary actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
