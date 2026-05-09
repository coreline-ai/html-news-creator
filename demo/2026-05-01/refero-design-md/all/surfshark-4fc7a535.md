# Surfshark - Refero Design MD

- Source: https://styles.refero.design/style/4fc7a535-3c99-4ffe-8365-7d025d33274e
- Original site: https://surfshark.com
- Theme: `mixed`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Animated aquatic security

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#16191c` | neutral | Primary text or dark surface |
| Stormy Night | `#1e2327` | neutral | Primary text or dark surface |
| Deep Graphite | `#393e41` | neutral | Primary text or dark surface |
| Charcoal Grey | `#5b6065` | neutral | Border, muted text, or supporting surface |
| Light Grey | `#bfbfc0` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#dadadd` | neutral | Page background or card surface |
| Cloud White | `#f9f9f9` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Primary Black | `#000000` | neutral | Primary text or dark surface |
| Shark Red | `#fa3556` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #16191c;
  --ref-stormy-night: #1e2327;
  --ref-deep-graphite: #393e41;
  --ref-charcoal-grey: #5b6065;
  --ref-light-grey: #bfbfc0;
  --ref-silver-mist: #dadadd;
  --ref-cloud-white: #f9f9f9;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 600, 700, 12px, 14px, 16px, 18px, 24px, 32px, 40px, 48px, 60px, 1.00, 1.07, 1.14, 1.15, 1.21, 1.30, 1.33, 1.50, 1.67, 1.71, 1.75; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `hero: 64px, cards: 48px, links: 8px, buttons: 12px, default: 32px`

## Surface cues
- **Cloud White Canvas** `#f9f9f9`: Default page background for light sections.
- **Pure White Elevated** `#ffffff`: Background for elevated components such as navigation menus or modal overlays.
- **Midnight Ink Canvas** `#16191c`: Primary background for dark sections, providing strong contrast.
- **Stormy Night Card** `#1e2327`: Surfaces for cards or content blocks within dark sections, creating subtle depth.

## Component cues
- **Primary Action Button**: Critical call to action.
- **Accent Promotion Button**: Highlighting special offers or deals.
- **Ghost Navigation Button**: Secondary navigation or interactive elements.
- **Text Link Button**: Minimal interactive elements without strong visual emphasis.
- **Dark Hero Card**: Prominent information blocks on dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
