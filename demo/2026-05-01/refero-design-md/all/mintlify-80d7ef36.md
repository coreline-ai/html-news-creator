# Mintlify - Refero Design MD

- Source: https://styles.refero.design/style/80d7ef36-ed7e-48bb-b558-f772eb40106f
- Original site: https://mintlify.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital librarian's desk. Precise information architecture meets subtle brand identity through selective color accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Coal | `#08090a` | neutral | Primary text or dark surface |
| Platinum | `#f2f2f2` | neutral | Page background or card surface |
| Steel | `#dddddd` | neutral | Page background or card surface |
| Emerald Glow | `#00dc8d` | accent | Action accent / signal color |
| Deep Cobalt | `#0052ff` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-white-canvas: #ffffff;
  --ref-coal: #08090a;
  --ref-platinum: #f2f2f2;
  --ref-steel: #dddddd;
  --ref-emerald-glow: #00dc8d;
  --ref-deep-cobalt: #0052ff;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 40px, 57px, 1.10, 1.15, 1.30, 1.33, 1.50, 1.71; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16-24px`
- Radius: `tags: 4px, cards: 16px, inputs: 0px, buttons: 1.67772e+07px, largeElements: 24px`

## Component cues
- **Email CTA Input**: Reference component style.
- **Feature Cards — Built for the Intelligence Age**: Reference component style.
- **Customer Story Cards**: Reference component style.
- **Text Link**: Navigation, inline links, secondary actions
- **Outline Button**: Call to action, navigation items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
