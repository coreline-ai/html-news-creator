# Frontier AI LLMs - Refero Design MD

- Source: https://styles.refero.design/style/d3caa7bf-2e2e-489a-845d-5cab274e7a92
- Original site: https://mistral.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Desert Dawn — a stark, warm landscape where technology meets the wild.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Desert Canvas | `#fffaeb` | neutral | Page background or card surface |
| Midnight Ink | `#1f1f1f` | neutral | Primary text or dark surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Void Deep | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#3c3c3c` | neutral | Primary text or dark surface |
| Sandstone Slab | `#fff0c2` | neutral | Page background or card surface |
| Pale Ochre | `#ecdaa2` | neutral | Page background or card surface |
| Horizon Gradient | `#b35d20` | brand | Action accent / signal color |
| Frontier Accent | `#fa520f` | accent | Action accent / signal color |
| Golden Streak | `#ffd900` | accent | Action accent / signal color |

```css
:root {
  --ref-desert-canvas: #fffaeb;
  --ref-midnight-ink: #1f1f1f;
  --ref-snowdrift: #ffffff;
  --ref-void-deep: #000000;
  --ref-graphite: #3c3c3c;
  --ref-sandstone-slab: #fff0c2;
  --ref-pale-ochre: #ecdaa2;
  --ref-horizon-gradient: #b35d20;
}
```

## Typography direction
- **Arial**: 400, 14px, 16px, 24px, 32px, 38px, 48px, 56px, 82px, 0.95, 1.00, 1.15, 1.33, 1.43, 1.50; substitute `Helvetica Neue, sans-serif`.

## Spacing / shape
- Section Gap: `89px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `all: 0px`

## Surface cues
- **Desert Canvas** `#fffaeb`: Base page background, light sections, content containers.
- **Sandstone Slab** `#fff0c2`: Secondary background for UI elements, alternating section backgrounds, subtle dividers.
- **Void Deep** `#000000`: Elevated buttons, dark foreground elements against lighter backgrounds.
- **Horizon Gradient** `#b35d20`: Hero sections and highly prominent background treatments.

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature List Cards**: Reference component style.
- **Autonomous Work Feature Selector**: Reference component style.
- **Primary Dark Button**: Call-to-action button for critical user journeys.
- **Ghost Accent Link Button**: Secondary action or navigation highlight, often appearing in hero or footer zones.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
