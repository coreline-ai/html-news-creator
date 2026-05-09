# Microsoft AI - Refero Design MD

- Source: https://styles.refero.design/style/46781641-8afd-4b01-9f67-06046b6eda71
- Original site: https://microsoft.ai
- Theme: `mixed`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm academic parchment

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Estate | `#000000` | neutral | Primary text or dark surface |
| Greated Parchment | `#fef9ed` | neutral | Page background or card surface |
| Faded Linen | `#f5f0e4` | neutral | Page background or card surface |
| Warm Clay | `#5d524b` | neutral | Border, muted text, or supporting surface |
| Dusty Rose Gradient | `#fbd3be` | brand | Action accent / signal color |
| Sunset Glaze Gradient | `#e7b191` | brand | Action accent / signal color |
| Worn Velvet | `#8c5462` | brand | Action accent / signal color |
| Forest Shade | `#2e4d4d` | brand | Action accent / signal color |
| Antique Brass | `#a67c52` | accent | Action accent / signal color |
| Cerulean Link | `#0066ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-estate: #000000;
  --ref-greated-parchment: #fef9ed;
  --ref-faded-linen: #f5f0e4;
  --ref-warm-clay: #5d524b;
  --ref-dusty-rose-gradient: #fbd3be;
  --ref-sunset-glaze-gradient: #e7b191;
  --ref-worn-velvet: #8c5462;
  --ref-forest-shade: #2e4d4d;
}
```

## Typography direction
- **Bradford LL**: 400, 450, 15px, 20px, 25px, 35px, 40px, 45px, 100px, 125px, 1.00, 1.13, 1.20, 1.25, 1.40; substitute `Playfair Display`.
- **Red Hat Mono**: 400, 450, 500, 12px, 13px, 15px, 20px, 1.00, 1.20, 1.25, 1.60; substitute `IBM Plex Mono`.
- **MWF-MDL2**: 400, 16px, 1.25; substitute `Segoe MDL2 Assets`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `17px`
- Element Gap: `8-20px`
- Radius: `lg: 6.66667px, md: 4.16667px, sm: 2.5px, pills: 65px, images: 25px, inputs: 50px, buttons: 85.8333px`

## Component cues
- **Accessibility Toggle**: Reference component style.
- **Product Tab Selector**: Reference component style.
- **Mission Statement Banner**: Reference component style.
- **Primary Navigation Link**: Main site navigation
- **Pill Search Input**: Global search functionality

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
