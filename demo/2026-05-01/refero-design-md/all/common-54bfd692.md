# Common - Refero Design MD

- Source: https://styles.refero.design/style/54bfd692-3299-48ab-8cf5-784e632227b1
- Original site: https://www.common.xyz
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard with digital neon accents

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Silver Pine | `#e0dfe1` | neutral | Page background or card surface |
| Charcoal Slate | `#282729` | neutral | Primary text or dark surface |
| Frost Gray | `#c1c0c2` | neutral | Border, muted text, or supporting surface |
| Ash Cloud | `#a09da1` | neutral | Border, muted text, or supporting surface |
| Dark Granite | `#3d3a3e` | neutral | Primary text or dark surface |
| Deep Ink | `#141315` | neutral | Primary text or dark surface |
| Stone Dust | `#757575` | neutral | Border, muted text, or supporting surface |
| Gallery White | `#f0eff0` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight: #000000;
  --ref-snowdrift: #ffffff;
  --ref-silver-pine: #e0dfe1;
  --ref-charcoal-slate: #282729;
  --ref-frost-gray: #c1c0c2;
  --ref-ash-cloud: #a09da1;
  --ref-dark-granite: #3d3a3e;
  --ref-deep-ink: #141315;
}
```

## Typography direction
- **NeueHaasUnica**: 400, 500, 600, 14px, 16px, 24px, 32px, 36px, 1.00, 1.15, 1.43, 1.50, 1.71; substitute `system-ui, sans-serif`.
- **Silka**: 400, 700, 20px, 24px, 28px, 1.17, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `cards: 5px, inputs: 6px, buttons: 6px, default: 6px`

## Component cues
- **Primary Filled Button**: Action
- **Ghost Button**: Action
- **Monochrome Card**: Container
- **Outline Card**: Container
- **Transparent Card**: Container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
