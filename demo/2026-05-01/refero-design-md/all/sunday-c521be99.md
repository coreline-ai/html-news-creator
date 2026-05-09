# Sunday - Refero Design MD

- Source: https://styles.refero.design/style/c521be99-14af-4d57-8f8f-34c76c9ade61
- Original site: https://www.sunday.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, bright, inviting future.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Snowfield | `#ffffff` | neutral | Page background or card surface |
| Coal | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#1a1a1a` | neutral | Primary text or dark surface |
| Silver Mist | `#eeeeee` | neutral | Page background or card surface |
| Pebble | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Frost | `#f3f3f0` | neutral | Page background or card surface |
| Aqua Haze | `#d9ecee` | neutral | Page background or card surface |
| Buttery Yellow | `#f7e731` | brand | Action accent / signal color |
| Earthen Creme | `#eadcce` | accent | Action accent / signal color |
| Sage Whisper | `#aec2b8` | accent | Action accent / signal color |

```css
:root {
  --ref-snowfield: #ffffff;
  --ref-coal: #000000;
  --ref-graphite: #1a1a1a;
  --ref-silver-mist: #eeeeee;
  --ref-pebble: #6f6f6f;
  --ref-frost: #f3f3f0;
  --ref-aqua-haze: #d9ecee;
  --ref-buttery-yellow: #f7e731;
}
```

## Typography direction
- **sans**: 400, 16px, 18px, 20px, 24px, 32px, 42px, 84px, 104px, 120px, 142px, 1.00, 1.10, 1.15, 1.20, 1.30, 1.33, 1.40, 1.50; substitute `Inter`.
- **mono**: 400, 12px, 14px, 1.00, 1.14, 1.20, 1.33, 1.43; substitute `IBM Plex Mono`.
- **helvetica neue**: 700, 14px, 1.71; substitute `Arial Bold`.

## Spacing / shape
- Section Gap: `160px`
- Card Padding: `12-24px`
- Element Gap: `4px`
- Radius: `cards: 12px, other: 8px, 24px, buttons: 4px`

## Component cues
- **Hero CTA Banner**: Reference component style.
- **Feature Intro Block**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **Ghost Header Button**: Navigation, secondary actions.
- **Text Link Button**: Inline actions, simple navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
