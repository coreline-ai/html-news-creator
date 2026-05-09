# FeedHive - Refero Design MD

- Source: https://styles.refero.design/style/45080e55-1fbe-4726-be23-4c9f54e442aa
- Original site: https://feedhive.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
AI-powered clarity on a pristine canvas. Like crisp architecture outlined in electric blue, housing playful, rounded forms.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| UI Platinum | `#f3f5ff` | neutral | Page background or card surface |
| Cloud Mist | `#e5e7eb` | neutral | Page background or card surface |
| Warm Stone | `#c7c8e2` | neutral | Border, muted text, or supporting surface |
| Deep Midnight | `#181c31` | brand | Action accent / signal color |
| Subtle Stone | `#757693` | neutral | Border, muted text, or supporting surface |
| Cloudy Sky | `#dbeafe` | neutral | Page background or card surface |
| Vivid Cobalt | `#4457ff` | brand | Action accent / signal color |
| Electric Lavender | `#596aff` | brand | Action accent / signal color |
| Hyper Blue Gradient | `#4457ff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ui-platinum: #f3f5ff;
  --ref-cloud-mist: #e5e7eb;
  --ref-warm-stone: #c7c8e2;
  --ref-deep-midnight: #181c31;
  --ref-subtle-stone: #757693;
  --ref-cloudy-sky: #dbeafe;
  --ref-vivid-cobalt: #4457ff;
}
```

## Typography direction
- **Thicccboi**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 34px, 36px, 44px, 60px, 1.00, 1.11, 1.25, 1.32, 1.33, 1.40, 1.41, 1.43, 1.56, 1.57, 1.60, 1.63; substitute `Inter`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `16-24px`
- Element Gap: `4px`
- Radius: `misc: 24px, cards: 24px, images: 12px, buttons: 9999px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Social Proof Rating Strip**: Reference component style.
- **Ghost Navigation Button**: Navigation links
- **Main Headline**: Key page titles

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
