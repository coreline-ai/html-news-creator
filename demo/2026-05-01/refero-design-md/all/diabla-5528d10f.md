# Diabla - Refero Design MD

- Source: https://styles.refero.design/style/5528d10f-2e7d-4502-aa49-7bde290e8fe2
- Original site: https://www.diablaoutdoor.com/en
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Tropical Modernism Pop

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Coral Kiss | `#ed2e38` | brand | Action accent / signal color |
| Carbon | `#333333` | neutral | Primary text or dark surface |
| Deep Ink | `#000000` | neutral | Primary text or dark surface |
| Shell Pink | `#fcf0f3` | neutral | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Rosy Clouds | `#f9c2cc` | accent | Action accent / signal color |

```css
:root {
  --ref-coral-kiss: #ed2e38;
  --ref-carbon: #333333;
  --ref-deep-ink: #000000;
  --ref-shell-pink: #fcf0f3;
  --ref-pure-white: #ffffff;
  --ref-rosy-clouds: #f9c2cc;
}
```

## Typography direction
- **Linotype Helvetica Neue LT Std Roman**: 400, 10px, 12px, 14px, 15px, 16px, 18px, 22px, 33px, 1.00, 1.09, 1.13, 1.20, 1.22, 1.29, 1.30, 1.43, 1.50, 1.80, 2.00, 2.33, 2.80; substitute `Helvetica Neue`.
- **Linotype Helvetica Neue LT Std Lt**: 400, 80px, 110px, 0.88, 0.91; substitute `Helvetica Neue Light`.
- **Arial**: 400, 13px, 1.2.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `25px`
- Element Gap: `10px`
- Radius: `links: 14px, inputs: 0px, buttons: 14px`

## Surface cues
- **Shell Pink Canvas** `#fcf0f3`: Primary page background, base for most content blocks.
- **Pure White Panel** `#ffffff`: Elevated card backgrounds, alternative input fields.

## Component cues
- **Outlined Button - Coral Kiss**: Primary action button, often paired with an icon.
- **Outlined Button - Deep Ink**: Secondary action or ghost button.
- **Input - Underlined Coral Kiss**: Text input field with focus.
- **Input - Shell Pink Background Circle**: Small input or selection with a circular, soft background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
