# REKKI - Refero Design MD

- Source: https://styles.refero.design/style/65b8df27-36a3-47a6-be53-735d1f6a485d
- Original site: https://rekki.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Deep Space | `#040910` | neutral | Primary text or dark surface |
| Charcoal Grey | `#0d0d0d` | neutral | Primary text or dark surface |
| Input Charcoal | `#1f1f1f` | neutral | Primary text or dark surface |
| Dark Card | `#2b2c2e` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Steel Gray | `#858585` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Blue Neon | `#0063e1` | brand | Action accent / signal color |
| Mid Grey | `#979797` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-deep-space: #040910;
  --ref-charcoal-grey: #0d0d0d;
  --ref-input-charcoal: #1f1f1f;
  --ref-dark-card: #2b2c2e;
  --ref-cloud-white: #ffffff;
  --ref-steel-gray: #858585;
  --ref-light-steel: #8c8c8c;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Diatype REKKI Medium**: 400, 16px, 18px, 56px, 72px, 86px, 1.00, 1.25, 1.33.
- **Diatype REKKI Regular**: 400, 600, 12px, 16px, 18px, 20px, 24px, 1.33, 1.40, 1.50, 1.67.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `32px`
- Element Gap: `20px`
- Radius: `cards: 8px, inputs: 100px, buttons: 59px, largeImages: 24px, asymmetricCards: 30px, navigationItems: 2px, topRoundedCards: 38px 38px 0px 0px`

## Surface cues
- **Absolute Zero Canvas** `#000000`: Primary page background, the deepest tonal layer.
- **Deep Space Surface** `#040910`: Slightly elevated card backgrounds, providing minimal depth over the canvas.
- **Charcoal Card Surface** `#0d0d0d`: Dominant card backgrounds, a step brighter than Deep Space.
- **Dark Card Elevated** `#2b2c2`: Most prominent card background, provides clear separation from lower layers.
- **Input Charcoal Field** `#1f1f1f`: Dedicated background for input fields, sitting above typical card layers.

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Action Button**: Alternative call to action
- **Ghost Text Button**: Subtle UI interaction
- **Dark Base Card**: Content container
- **Semi-Transparent Card**: Overlay content, context cards

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
