# Cake Equity - Refero Design MD

- Source: https://styles.refero.design/style/4c33d8fe-81d5-46cb-9dc1-dd231be1c9ec
- Original site: https://www.cakeequity.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
precision ledger on a clean slate

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#18161a` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#fafaf8` | neutral | Page background or card surface |
| Stone Slate | `#333333` | neutral | Primary text or dark surface |
| Ash Mist | `#898b91` | neutral | Border, muted text, or supporting surface |
| Lilac Gray | `#ede9ff` | neutral | Page background or card surface |
| Lavender Hue | `#d9d2ff` | neutral | Border, muted text, or supporting surface |
| Plum Royal | `#4823ff` | brand | Action accent / signal color |
| Vivid Violet | `#6d67fb` | brand | Action accent / signal color |
| Soft Indigo | `#7e78ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #18161a;
  --ref-polar-white: #ffffff;
  --ref-cloud-gray: #fafaf8;
  --ref-stone-slate: #333333;
  --ref-ash-mist: #898b91;
  --ref-lilac-gray: #ede9ff;
  --ref-lavender-hue: #d9d2ff;
  --ref-plum-royal: #4823ff;
}
```

## Typography direction
- **Plus Jakarta Sans**: 700, 63px, 77px, 1.00; substitute `Inter`.
- **Inter**: 300, 400, 500, 600, 700, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 31px, 0.86, 1.00, 1.10, 1.20, 1.29, 1.30, 1.40, 1.45, 1.50, 1.53, 1.60, 1.80, 2.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `71px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `tags: 999px, cards: 20px, icons: 50px, links: 12px, buttons: 100px, general: 16px`

## Surface cues
- **Page Background** `#ffffff`: The foundational canvas for most page content.
- **Subtle Section Background** `#fafaf8`: Used for alternating content sections and subtle visual separation.
- **Card Surface** `#ffffff`: Default background for information cards and embedded UI components.
- **Accent Card Surface** `#e7ff6`: Used for prominent features or call-out sections, providing visual emphasis.

## Component cues
- **Primary Filled Button**: Call to action.
- **Secondary Outlined Button**: Secondary call to action, ghost buttons.
- **Navigation Link**: Primary navigation items.
- **Default Card**: General content container.
- **Highlight Card (Lime Spritz)**: Promotional or featured content container.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
