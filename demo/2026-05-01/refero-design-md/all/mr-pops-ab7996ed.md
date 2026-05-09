# Mr. Pops - Refero Design MD

- Source: https://styles.refero.design/style/ab7996ed-e0ed-40a0-81a5-d37f19ef35b0
- Original site: https://mrpops.ua/en
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Indulgence on a White Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Snow | `#ffffff` | neutral | Page background or card surface |
| Licorice | `#000000` | neutral | Primary text or dark surface |
| Candy Apple | `#b00e2f` | brand | Action accent / signal color |
| Nude Peach | `#fee5ca` | neutral | Page background or card surface |

```css
:root {
  --ref-snow: #ffffff;
  --ref-licorice: #000000;
  --ref-candy-apple: #b00e2f;
  --ref-nude-peach: #fee5ca;
}
```

## Typography direction
- **Cervo**: 400, 500, 16px, 18px, 22px, 42px, 64px, 72px, 144px, 0.75, 0.90, 1.00; substitute `Georgia`.
- **HelveticaNeueCyr**: 400, 12px, 15px, 16px, 18px, 1.15, 1.20, 1.30, 1.40; substitute `Arial`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `30px`
- Element Gap: `10px`
- Radius: `buttons: 50%, default: 40px, circularElements: 300px`

## Surface cues
- **Canvas** `#ffffff`: Primary page background
- **Card Base** `#fee5ca`: Secondary background for cards, slight elevation, or subtle segmentation
- **Accent Fill** `#b00e2f`: Dominant interactive elements and hero backgrounds

## Component cues
- **Primary Filled Button**: Call to action button for core tasks
- **Secondary Ghost Button**: Alternative actions or navigation elements
- **Navigation Menu Button**: Toggle for site navigation
- **Form Input Field**: User input fields for forms
- **Circular Callout Button**: Small interactive circular elements, often for quantity or selection

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
