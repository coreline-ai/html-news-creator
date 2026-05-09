# Groq - Refero Design MD

- Source: https://styles.refero.design/style/8efa9029-b39c-48db-a8ec-c97c645a7a58
- Original site: https://groq.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision orange glow on matte gray. Like a control panel's critical warning light in a sophisticated machine.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Slate | `#2d2f33` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Mist | `#f3f3ee` | neutral | Page background or card surface |
| Ash Concrete | `#e8e8de` | neutral | Page background or card surface |
| Deep Pewter | `#2a2a25` | neutral | Primary text or dark surface |
| Steel Gray | `#c2c2be` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#69695d` | neutral | Border, muted text, or supporting surface |
| Faded Quartz | `#9c9c90` | neutral | Border, muted text, or supporting surface |
| Neon Zest | `#f43e01` | brand | Action accent / signal color |
| Deep Ember | `#c23101` | brand | Action accent / signal color |

```css
:root {
  --ref-obsidian-slate: #2d2f33;
  --ref-canvas-white: #ffffff;
  --ref-warm-mist: #f3f3ee;
  --ref-ash-concrete: #e8e8de;
  --ref-deep-pewter: #2a2a25;
  --ref-steel-gray: #c2c2be;
  --ref-soft-stone: #69695d;
  --ref-faded-quartz: #9c9c90;
}
```

## Typography direction
- **Space Grotesk**: 300, 400, 13px, 14px, 15px, 17px, 19px, 21px, 24px, 28px, 32px, 36px, 46px, 0.90, 1.00, 1.30, 1.40, 1.57; substitute `system-ui, sans-serif`.
- **IBM Plex Mono**: 400, 500, 10px, 12px, 14px, 1.17, 1.20, 1.30, 1.40, 1.57; substitute `monospace`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `0px`
- Element Gap: `4-16px`
- Page Max Width: `1440px`
- Radius: `misc: 5px, cards: 0px, forms: 10px, buttons: 1000px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Dark Feature Section Block**: Reference component style.
- **Primary Action Button**: Call to action
- **Ghost Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
