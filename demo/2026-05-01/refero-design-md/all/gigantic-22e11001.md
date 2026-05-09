# Gigantic - Refero Design MD

- Source: https://styles.refero.design/style/22e11001-8786-4af7-bdb9-f9419ce8ad1a
- Original site: https://giganticcandy.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw Urban Energy: Oversized typography and high-contrast visuals on a clean backdrop evoke direct, impactful communication.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Asphalt Black | `#231f20` | neutral | Primary text or dark surface |
| Street Chalk | `#f0ede7` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Flavor Burst Red | `#ff634b` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-asphalt-black: #231f20;
  --ref-street-chalk: #f0ede7;
  --ref-ink-black: #000000;
  --ref-flavor-burst-red: #ff634b;
}
```

## Typography direction
- **neue-haas-grotesk-display**: 400, 450, 500, 700, 12px, 14px, 16px, 18px, 24px, 25px, 32px, 1.00, 1.20, 1.30, 1.44, 1.56, 1.70, 1.80; substitute `Inter`.
- **GTStandard-M**: 400, 16px, 1.50; substitute `Roboto Mono`.
- **Arial**: 400, 13px, 1.2.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `30px`
- Element Gap: `19px`
- Radius: `none: 0px`

## Surface cues
- **Page Canvas** `#ffffff`: The primary background for all page content.
- **Subtle Panel** `#f0ede7`: Used for alternative background sections to gently break up visual flow, often for informational blocks.
- **Actionable Surface** `#231f20`: Background for primary interactive elements like buttons, providing strong visual call to action.

## Component cues
- **Filled Primary Button**: Call to action
- **Text Link Button**: Secondary action
- **Outlined Text Button**: Tertiary action
- **Product Shop Buttons**: Product navigation action
- **Utility Top Bar**: Informational banner

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
