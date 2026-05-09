# Limón - Refero Design MD

- Source: https://styles.refero.design/style/f1b6a7d6-1ecb-4f1c-95b0-e03323363999
- Original site: https://limonoslo.no
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Earthy vibrancy

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Forest | `#1d0b0d` | neutral | Primary text or dark surface |
| Fresh Lime | `#103b15` | neutral | Primary text or dark surface |
| Marigold Zest | `#f7ea48` | accent | Action accent / signal color |
| Vanilla Cream | `#fcf9f0` | neutral | Page background or card surface |
| Soft Mist | `#dbe2dc` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-deep-forest: #1d0b0d;
  --ref-fresh-lime: #103b15;
  --ref-marigold-zest: #f7ea48;
  --ref-vanilla-cream: #fcf9f0;
  --ref-soft-mist: #dbe2dc;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **VenusCom**: 300, 400, 500, 600, 700, 14px, 16px, 19px, 20px, 26px, 30px, 36px, 46px, 54px, 68px, 75px, 1.00, 1.01, 1.15, 1.20, 1.25, 1.30, 1.35, 1.37, 1.40, 1.45, 1.60; substitute `Montserrat, Open Sans`.
- **Times**: 400, 19px, 1.01; substitute `serif`.
- **Font Awesome 6 Brands**: 400, 36px, 1.00; substitute `Font Awesome 6 Brands`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `body: 1px, other: 40px, buttons: 1px`

## Surface cues
- **Page Canvas** `#1d0b0d`: Primary background for the hero section and full-bleed content, providing a deep, grounding tone.
- **Content Canvas** `#fcf9f0`: Main background for content sections, cards, and textual information, offering a warm, light surface.
- **Interactive Accent** `#f7ea48`: Reserved for primary calls to action and prominent headings, designed to stand out against any background.

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Action Button (Dark)**: Secondary action on dark backgrounds
- **Ghost Action Button (Light)**: Secondary action on light backgrounds
- **Icon Button**: Standalone decorative or functional icon
- **Product Description Card**: Displaying individual product details

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
