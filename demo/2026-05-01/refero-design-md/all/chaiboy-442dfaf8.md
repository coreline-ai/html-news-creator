# CHAIBOY - Refero Design MD

- Source: https://styles.refero.design/style/442dfaf8-c0c6-467b-a8d4-54e953c049f3
- Original site: https://wearechaiboy.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic minimalist canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Frost Gray | `#afafaf` | neutral | Border, muted text, or supporting surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-frost-gray: #afafaf;
  --ref-arctic-white: #ffffff;
}
```

## Typography direction
- **NeueHaasGroteskTP55R**: 400, 11px, 14px, 18px, 54px, 0.89, 1.11, 1.27, 1.29.
- **Neue Haas Grotesk Text**: use as primary family; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `16px`
- Element Gap: `5px`
- Radius: `cards: 4px, links: 4px, buttons: 4px, overall: 4px`

## Surface cues
- **Base Canvas** `#000000`: Dominant background for pages and sections, creating a deep, dark foundation.
- **Subtle Surface** `#131313`: Slightly lighter dark surface, offering minimal differentiation for secondary content areas or hover states.
- **Interactive Layer** `#afafaf`: Used for interactive elements like input borders, ghost buttons, and subtle separators, providing a muted interactive layer.
- **Emphasis Layer** `#ffffff`: Reserved for primary text, active states, and crisp borders, providing high contrast and visual emphasis.

## Component cues
- **Ghost Border Button - Frost**: Secondary action button
- **Underlined Input - Frost**: Standard text input field
- **Underlined Input - Arctic**: Prominent text input field
- **Header Navigation Link**: Primary navigation item
- **Footer Action Link - Muted**: Footer utility links

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
