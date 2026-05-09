# BEHAVE Candy - Refero Design MD

- Source: https://styles.refero.design/style/5cc6e3be-1cbd-4d09-9958-9cb82b2487db
- Original site: https://www.eatbehave.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid candy wrapper

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ultraviolet | `#061fff` | brand | Action accent / signal color |
| Key Lime | `#d3ff56` | brand | Action accent / signal color |
| Lilac Mist | `#efe5ff` | neutral | Page background or card surface |
| Soft Plum | `#ceb3ff` | neutral | Border, muted text, or supporting surface |
| Lavender Haze | `#dfceff` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-ultraviolet: #061fff;
  --ref-key-lime: #d3ff56;
  --ref-lilac-mist: #efe5ff;
  --ref-soft-plum: #ceb3ff;
  --ref-lavender-haze: #dfceff;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Good Sans**: 400, 500, 700, 12px, 14px, 16px, 18px, 22px, 24px, 32px, 53px, 56px, 72px, 86px, 1.00, 1.10, 1.15, 1.20, 1.30, 1.50, 1.51, 2.14, 2.50; substitute `Montserrat`.

## Spacing / shape
- Card Padding: `30px`
- Element Gap: `20px`
- Radius: `cards: 20px, forms: 6.95px, pills: 25px, buttons: 6.95px`

## Surface cues
- **Lilac Mist Canvas** `#efe5ff`: Dominant background for the overall page, creating a soft, expansive base.
- **Soft Plum Card** `#ceb3ff`: Background for secondary content cards and product listings, providing subtle visual depth.
- **Lavender Haze Input** `#dfceff`: Background for form fields and interactive input elements, gently differentiating them.

## Component cues
- **Primary Action Button**: Key Call-to-Action
- **Ghost Button**: Secondary or Navigational Action
- **Pill Button**: Categorization or Tag
- **Reverse Primary Button**: Highlighted Action on Dark Background
- **Standard Content Card**: Content Grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
