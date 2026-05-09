# Ditto - Refero Design MD

- Source: https://styles.refero.design/style/2db41cd9-c898-4f59-b704-3042c0d87f45
- Original site: https://www.dittowords.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#f7f5f3` | neutral | Page background or card surface |
| Graphite | `#6a6559` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#e2e2e2` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Harvest Gold | `#ffdd33` | accent | Action accent / signal color |
| Power Red | `#ff6137` | accent | Action accent / signal color |
| Royal Blue | `#0097e6` | accent | Action accent / signal color |
| Fresh Green | `#3e6b15` | semantic | Action accent / signal color |
| Rich Violet | `#b26dc2` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #f7f5f3;
  --ref-graphite: #6a6559;
  --ref-warm-gray: #e2e2e2;
  --ref-pure-white: #ffffff;
  --ref-harvest-gold: #ffdd33;
  --ref-power-red: #ff6137;
  --ref-royal-blue: #0097e6;
}
```

## Typography direction
- **ABC Social**: 300, 400, 700, 13px, 16px, 18px, 25px, 26px, 35px, 72px, 108px, 0.89, 1.00, 1.05, 1.10, 1.20, 1.43; substitute `Inter`.
- **ABC Social Extended**: 400, 700, 16px, 18px, 24px, 36px, 40px, 43px, 86px, 0.88, 1.00, 1.05, 2.63; substitute `Inter`.
- **ABC Social Condensed**: 900, 35px, 1.20; substitute `Inter Condensed`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 1000px, images: 12px, inputs: 28px, buttons: 100px`

## Surface cues
- **Canvas White** `#f7f5f3`: Dominant page background.
- **Pure White** `#ffffff`: Background for elevated elements like certain inputs or overlay content.
- **Harvest Gold** `#ffdd33`: Background for specific highlighted cards or decorative elements.

## Component cues
- **Primary Filled Button**: Main call to action button.
- **Ghost Outline Button**: Secondary call to action, less prominent than primary.
- **Ghost Border Button (Pill)**: Tertiary action or navigational elements requiring minimal visual weight.
- **Badge with Background**: Highlighting status or keyword.
- **Success Status Badge**: Indicating a positive status.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
