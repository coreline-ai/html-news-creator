# Vibrants - Refero Design MD

- Source: https://styles.refero.design/style/f73ce3e0-4452-4b21-b36f-6fde27de2cd6
- Original site: https://vibrants.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
white canvas, vibrant accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#021422` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#e6e8e9` | neutral | Page background or card surface |
| Canvas Ice | `#f2f6ff` | neutral | Page background or card surface |
| Smoke Stone | `#ccd2d7` | neutral | Border, muted text, or supporting surface |
| Forest Green | `#00852e` | accent | Action accent / signal color |
| Sky Blue | `#91c3ff` | accent | Action accent / signal color |
| Deep Ocean | `#001f38` | neutral | Primary text or dark surface |
| Asphalt Gray | `#808f9c` | neutral | Border, muted text, or supporting surface |
| Charcoal Haze | `#6a7c89` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #021422;
  --ref-cloud-white: #ffffff;
  --ref-fog-gray: #e6e8e9;
  --ref-canvas-ice: #f2f6ff;
  --ref-smoke-stone: #ccd2d7;
  --ref-forest-green: #00852e;
  --ref-sky-blue: #91c3ff;
  --ref-deep-ocean: #001f38;
}
```

## Typography direction
- **Montserrat**: 400, 500, 600, 700, 10px, 12px, 14px, 15px, 16px, 20px, 1.00, 1.14, 1.20, 1.33, 1.38, 1.50, 1.71, 1.80; substitute `Arial`.
- **new-kansas**: 400, 500, 600, 700, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 28px, 32px, 36px, 44px, 48px, 1.00, 1.13, 1.17, 1.20, 1.22, 1.25, 1.29, 1.33, 1.43, 1.50, 1.75, 2.00; substitute `Georgia`.
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 16px, 1.00, 1.08, 1.20, 1.23, 1.25, 1.33; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `39px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `pill: 20px, cards: 8px, badges: 3px, inputs: 8px, buttons: 8px`

## Surface cues
- **Cloud White Canvas** `#ffffff`: Primary page background and default surface for most content cards.
- **Canvas Ice Card** `#f2f6ff`: Subtle background for specific card sections, indicating a slight elevation or different content grouping.

## Component cues
- **Primary Filled Button**: Highlight key actions.
- **Outline Accent Button**: Secondary calls to action, prominent links.
- **Dark Filled Button**: Primary Call to action, often in hero sections.
- **Pill Outline Button**: Filter options, secondary choices.
- **Product Card**: Display individual patch products.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
