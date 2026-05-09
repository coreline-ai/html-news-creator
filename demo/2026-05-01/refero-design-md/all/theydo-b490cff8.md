# TheyDo - Refero Design MD

- Source: https://styles.refero.design/style/b490cff8-9d2c-4225-9118-6468e4f3213d
- Original site: https://www.theydo.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp geometry, playful pink.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#fce7f3` | neutral | Page background or card surface |
| Graphite | `#131110` | neutral | Primary text or dark surface |
| Charcoal | `#000000` | neutral | Primary text or dark surface |
| Stone Gray | `#c6c3c3` | neutral | Border, muted text, or supporting surface |
| Muted Sage | `#7b7674` | neutral | Border, muted text, or supporting surface |
| Light Pink Wash | `#fad6e9` | accent | Action accent / signal color |
| Bubblegum Burst | `#f9b4db` | accent | Action accent / signal color |
| Magenta Zing | `#e82183` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-ash-gray: #fce7f3;
  --ref-graphite: #131110;
  --ref-charcoal: #000000;
  --ref-stone-gray: #c6c3c3;
  --ref-muted-sage: #7b7674;
  --ref-light-pink-wash: #fad6e9;
  --ref-bubblegum-burst: #f9b4db;
}
```

## Typography direction
- **Times**: 400, 15px, 16px, 1.20, 1.25, 1.50; substitute `Times New Roman`.
- **DM Sans**: 400, 500, 600, 700, 14px, 15px, 16px, 17px, 18px, 1.00, 1.10, 1.20, 1.25, 1.33, 1.44, 1.47, 1.50, 1.53, 1.56, 1.60, 2.12.
- **wulkan**: 400, 500, 19px, 24px, 32px, 36px, 40px, 48px, 60px, 72px, 1.10, 1.11, 1.16, 1.17, 1.19, 1.20, 1.25.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `20px`
- Element Gap: `15px`
- Radius: `cards: 8px, buttons: 5px, default: 8px`

## Surface cues
- **Canvas** `#ffffff`: Base page background and primary card surfaces.
- **Ash Gray Panel** `#fce7f3`: Secondary background areas and accented card surfaces.
- **Dark Overlay** `#131110`: Used for filled buttons acting as primary actions against light backgrounds.

## Component cues
- **Primary Navigation Text Button**: Unfilled text button for main navigation items with subtle ':hover' state
- **Outline Nav Item Button**: Outlined button for secondary actions in header (e.g., login)
- **Ghost Outline Button**: Ghost (transparent background) buttons with subtle borders.
- **Filled Dark Button**: Primary action button with a dark background.
- **Subtle Information Card**: Cards for displaying information, often with a light background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
