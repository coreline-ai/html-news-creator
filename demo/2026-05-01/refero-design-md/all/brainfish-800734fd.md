# Brainfish - Refero Design MD

- Source: https://styles.refero.design/style/800734fd-eb95-41f3-b6f4-15fc19e127f0
- Original site: https://www.brainfishai.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful productivity, layered surfaces.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Border | `#171717` | neutral | Primary text or dark surface |
| Shadow Base | `#0a0a0d` | neutral | Primary text or dark surface |
| Pale Ash | `#f5f5f5` | neutral | Page background or card surface |
| Accent Green | `#a3e635` | brand | Action accent / signal color |
| Card Saffron | `#fef3c8` | accent | Action accent / signal color |
| Card Lavender | `#fae9ff` | accent | Action accent / signal color |
| Card Mint | `#d2fae5` | accent | Action accent / signal color |
| Card Pink | `#f5d1fe` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-charcoal-border: #171717;
  --ref-shadow-base: #0a0a0d;
  --ref-pale-ash: #f5f5f5;
  --ref-accent-green: #a3e635;
  --ref-card-saffron: #fef3c8;
  --ref-card-lavender: #fae9ff;
}
```

## Typography direction
- **Satoshi**: 500, 700, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 36px, 48px, 64px, 1.14, 1.16, 1.33, 1.38, 1.40, 1.42, 1.44, 1.50, 1.57, 1.67; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 8px, badges: 100px, buttons: 4px, default: 4px, largeCards: 16px, extraLargeCards: 20px`

## Component cues
- **Primary Action Button**: Main call-to-action button.
- **Ghost Action Button**: Secondary or outlined actions.
- **Text Link Button**: Minimal or inline actions.
- **Content Card**: Information display card.
- **Shadowed Content Card**: Prominent information display card.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
