# bella Kitchen Appliances - Refero Design MD

- Source: https://styles.refero.design/style/e327d332-270d-4779-a55c-cd82b8624d2a
- Original site: https://bellakitchenware.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm kitchen canvas

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ebeadf` | neutral | Page background or card surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Sandstone | `#d5cec0` | neutral | Border, muted text, or supporting surface |
| Tangerine | `#f04923` | brand | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas: #ebeadf;
  --ref-snow: #ffffff;
  --ref-sandstone: #d5cec0;
  --ref-tangerine: #f04923;
}
```

## Typography direction
- **Times**: 400, 700, 16px, 32px, 1.00; substitute `Times New Roman`.
- **Supreme LL TT**: 400, 700, 13px, 14px, 16px, 18px, 22px, 24px, 40px, 0.89, 1.10, 1.40, 1.50, 1.83; substitute `Arial`.

## Spacing / shape
- Section Gap: `167px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `cards: 12px, buttons: 999px, general: 12px`

## Component cues
- **Text Link**: Navigational and descriptive links.
- **Pill Button**: Primary interaction button for calls to action.
- **Ghost Button**: Secondary or alternative actions where visual weight is less important.
- **Product Highlight Card**: Showcasing featured products or promotions with high visual impact.
- **General Content Card**: Standard container for product listings and informational blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
