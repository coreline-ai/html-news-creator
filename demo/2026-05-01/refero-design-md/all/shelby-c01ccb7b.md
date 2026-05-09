# Shelby - Refero Design MD

- Source: https://styles.refero.design/style/c01ccb7b-46c9-487c-8a4e-0e9d6627f0d6
- Original site: https://shelby.ashfall.studio
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cacao and neon pink. A dark, rich canvas illuminated by electric, playful accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Shelby Cacao | `#322312` | neutral | Primary text or dark surface |
| Shelby Rose Dust | `#ffdfef` | neutral | Page background or card surface |
| Shelby Hibiscus Pink | `#ff77c9` | brand | Action accent / signal color |
| Shelby Plum | `#470b64` | neutral | Primary text or dark surface |
| Shelby Mauve | `#ffc2e1` | neutral | Border, muted text, or supporting surface |
| Shelby Lavender Mist | `#eee2ff` | neutral | Page background or card surface |
| Shelby Deep Rose | `#481d2a` | neutral | Primary text or dark surface |
| Shelby Steel Grey | `#5b4f41` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-shelby-cacao: #322312;
  --ref-shelby-rose-dust: #ffdfef;
  --ref-shelby-hibiscus-pink: #ff77c9;
  --ref-shelby-plum: #470b64;
  --ref-shelby-mauve: #ffc2e1;
  --ref-shelby-lavender-mist: #eee2ff;
  --ref-shelby-deep-rose: #481d2a;
  --ref-shelby-steel-grey: #5b4f41;
}
```

## Typography direction
- **Times**: 400, 10px, 1.
- **GT-Planar**: 300, 400, 500, 700, 10px, 16px, 18px, 22px, 42px, 48px, 59px, 95px, 0.90, 0.95, 1.00, 1.15, 1.20, 1.40; substitute `Inter`.
- **SuisseIntl**: 400, 10px, 1.00, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `cards: 9.89583px, badges: 3.95833px, buttons: 3.95833px, default: 3.95833px, secondaryButtons: 11.875px`

## Component cues
- **Ghost Button - Hot Pink**: Primary Call to Action
- **Outline Button - Rounded Hot Pink**: Secondary Call to Action
- **Filled Button - Plum**: Alternative Call to Action on Dark Backgrounds
- **Card - Hot Pink**: Highlight Card
- **Card - Muted Pink**: Information Card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
