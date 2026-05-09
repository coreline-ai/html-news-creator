# Vivid Spain - Refero Design MD

- Source: https://styles.refero.design/style/c25e8eb5-634d-4aca-b30b-d8ba5a50dc5a
- Original site: https://vivid.money
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
diffused lavender light

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#24282d` | neutral | Primary text or dark surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Ash Gray | `#79797f` | neutral | Border, muted text, or supporting surface |
| Pale Lavender | `#f4edff` | neutral | Page background or card surface |
| Cloud Gray | `#eceef2` | neutral | Page background or card surface |
| Desert Sand | `#f5f5f4` | neutral | Page background or card surface |
| Frosty Pearl | `#bbbbc1` | neutral | Border, muted text, or supporting surface |
| Vivid Violet | `#7d33f6` | brand | Action accent / signal color |
| Hero Gradient | `#e9d4fb` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #24282d;
  --ref-snowdrift: #ffffff;
  --ref-graphite: #333333;
  --ref-ash-gray: #79797f;
  --ref-pale-lavender: #f4edff;
  --ref-cloud-gray: #eceef2;
  --ref-desert-sand: #f5f5f4;
  --ref-frosty-pearl: #bbbbc1;
}
```

## Typography direction
- **Satoshi**: 400, 500, 600, 700, 10px, 12px, 13px, 14px, 15px, 16px, 20px, 24px, 36px, 40px, 52px, 56px, 60px, 1.00, 1.10, 1.14, 1.17, 1.20, 1.25, 1.29, 1.30, 1.33, 1.38, 1.50, 1.57, 1.60, 2.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `full: 48px, cards: 24px, buttons: 100px, elements: 10px`

## Component cues
- **Pricing Cards**: Reference component style.
- **Feature Cards**: Reference component style.
- **Achievements Banner**: Reference component style.
- **Navigation Link**: Interactive element
- **Nav Pill Button**: Secondary action / Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
