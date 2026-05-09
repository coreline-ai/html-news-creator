# Hungry Tiger - Refero Design MD

- Source: https://styles.refero.design/style/47f15da7-8905-45b3-bcab-06a4277c6168
- Original site: https://www.eathungrytiger.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Spiced Amber Glow

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Mahogany Canvas | `#281006` | neutral | Primary text or dark surface |
| Burnt Sienna | `#402011` | neutral | Primary text or dark surface |
| Spiced Orange | `#823513` | neutral | Action accent / signal color |
| Curry Yellow | `#faae33` | brand | Action accent / signal color |
| Cinnamon Brown | `#9f531b` | brand | Action accent / signal color |
| Chili Red | `#d1255c` | accent | Action accent / signal color |
| Subtle Radial Glow | `#f7ac32` | accent | Action accent / signal color |

```css
:root {
  --ref-mahogany-canvas: #281006;
  --ref-burnt-sienna: #402011;
  --ref-spiced-orange: #823513;
  --ref-curry-yellow: #faae33;
  --ref-cinnamon-brown: #9f531b;
  --ref-chili-red: #d1255c;
  --ref-subtle-radial-glow: #f7ac32;
}
```

## Typography direction
- **Salmond**: 400, 500, 700, 11px, 12px, 13px, 14px, 18px, 29px, 42px, 43px, 65px, 68px, 72px, 101px, 130px, 144px, 195px, 213px, 0.70, 0.80, 0.88, 0.90, 0.93, 0.95, 1.00, 1.10, 1.20, 1.30, 1.40, 1.43; substitute `Bebas Neue (display), Montserrat (body)`.
- **Graphikx**: 500, 13px, 1.00, 1.20, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `173px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `cards: 6px, badges: 1080px, inputs: 1224px, buttons: 1296px, secondaryButtons: 1152px`

## Surface cues
- **Mahogany Canvas** `#281006`: Base page background and deepest surface level.
- **Burnt Sienna** `#402011`: Secondary surface for cards and distinct content blocks, slightly elevated from the canvas.
- **Spiced Orange** `#823513`: Accent surface for badges and input borders, providing a warmer, more vibrant layer.
- **Curry Yellow** `#faae33`: Highlight surface for cards and primary interactive elements, representing the highest visual prominence.

## Component cues
- **Primary Call to Action Button**: Main interactive element
- **Ghost Inverse Action Button**: Secondary interactive element
- **Navigation Button**: Top navigation links
- **Dark Content Card**: Container for content sections
- **Light Highlight Card**: Highlighted content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
