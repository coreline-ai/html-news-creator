# Reclaim - Refero Design MD

- Source: https://styles.refero.design/style/71c7b9ad-44cc-483f-9c53-3cf73e0522a4
- Original site: https://reclaim.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant AI workspace

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White | `#ffffff` | neutral | Page background or card surface |
| Charcoal | `#2b2b2b` | neutral | Primary text or dark surface |
| Graphite | `#474747` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#c2c4d0` | neutral | Border, muted text, or supporting surface |
| Electric Violet | `#5562eb` | brand | Action accent / signal color |
| AI Green | `#7ac17b` | brand | Action accent / signal color |
| Zenith Gradient | `#5562eb` | accent | Action accent / signal color |
| Growth Gradient | `#7ac17b` | accent | Action accent / signal color |

```css
:root {
  --ref-white: #ffffff;
  --ref-charcoal: #2b2b2b;
  --ref-graphite: #474747;
  --ref-light-steel: #c2c4d0;
  --ref-electric-violet: #5562eb;
  --ref-ai-green: #7ac17b;
  --ref-zenith-gradient: #5562eb;
  --ref-growth-gradient: #7ac17b;
}
```

## Typography direction
- **Poppins**: 300, 400, 500, 600, 700, all, all; substitute `system-ui`.
- **Inter**: 400, 500, 12px, 13px, 18px, all; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40-70px`
- Card Padding: `20-30px`
- Element Gap: `5-15px`
- Radius: `cards: 0px, buttons: 100px, default: 10px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Impact Statistics Block**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Primary Pill Button**: Primary call to action.
- **Secondary Outline Button**: Secondary call to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
