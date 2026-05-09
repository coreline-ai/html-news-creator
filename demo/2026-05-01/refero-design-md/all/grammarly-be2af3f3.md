# Grammarly - Refero Design MD

- Source: https://styles.refero.design/style/be2af3f3-3886-4d70-973f-f7b5ab8d1a99
- Original site: https://grammarly.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital parchment

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell Deep | `#0e101a` | neutral | Primary text or dark surface |
| Inkwell Muted | `#1f243c` | neutral | Primary text or dark surface |
| Teal Verdant | `#027e6f` | brand | Action accent / signal color |
| Slate Blue | `#333954` | neutral | Action accent / signal color |
| Stone Gray | `#6d758d` | neutral | Border, muted text, or supporting surface |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Snow Drift | `#f5f5f5` | neutral | Page background or card surface |
| Frost Gray | `#ebebeb` | neutral | Page background or card surface |
| Graphite | `#1c1c1c` | neutral | Primary text or dark surface |
| Ash | `#545454` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-inkwell-deep: #0e101a;
  --ref-inkwell-muted: #1f243c;
  --ref-teal-verdant: #027e6f;
  --ref-slate-blue: #333954;
  --ref-stone-gray: #6d758d;
  --ref-arctic-mist: #ffffff;
  --ref-snow-drift: #f5f5f5;
  --ref-frost-gray: #ebebeb;
}
```

## Typography direction
- **matter**: 670, 20px, 36px, 46px, 52px, 1.09, 1.11, 1.12, 1.20; substitute `Open Sans`.
- **Glyph**: 400, 700, 12px, 13px, 14px, 16px, 18px, 20px, 22px, 1.20, 1.25, 1.43, 1.44, 1.45, 1.50, 1.71, 2.29; substitute `Roboto`.
- **Inter**: 400, 16px, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `cards: 0px, buttons: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Enterprise ROI Banner with Stats**: Reference component style.
- **Cookie Consent Banner**: Reference component style.
- **Primary CTA Button**: Call to action
- **Secondary Button**: Alternative action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
