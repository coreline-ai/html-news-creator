# ddna - Refero Design MD

- Source: https://styles.refero.design/style/0e8e546b-004c-46b6-a960-5dd88968ae07
- Original site: https://d-d-n-a.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment whispers

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#dacabf` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#efe3dc` | neutral | Page background or card surface |
| Deep Slate | `#444242` | neutral | Border, muted text, or supporting surface |
| Muted Ash | `#595552` | neutral | Border, muted text, or supporting surface |
| Faded Quarry | `#938a83` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-parchment: #dacabf;
  --ref-soft-stone: #efe3dc;
  --ref-deep-slate: #444242;
  --ref-muted-ash: #595552;
  --ref-faded-quarry: #938a83;
}
```

## Typography direction
- **Basis**: 400, 10px, 14px, 15px, 17px, 1.00, 1.50; substitute `Inter`.
- **Favorit**: 400, 30px, 1.30, 2.00; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `135px`
- Element Gap: `20px`
- Radius: `all: 0px`

## Component cues
- **Ghost Button**: Primary action button for 'Explore Collections'.
- **Navigation Link**: Top navigation and footer links.
- **Transparent Card**: Content containers for product listings or features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
