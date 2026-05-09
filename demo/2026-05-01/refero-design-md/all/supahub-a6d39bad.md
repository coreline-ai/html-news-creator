# Supahub - Refero Design MD

- Source: https://styles.refero.design/style/a6d39bad-6e32-462e-afce-67c9cb76cf40
- Original site: https://grabee.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
whispering tech meadow

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111827` | neutral | Primary text or dark surface |
| Ghost Gray | `#3f4654` | neutral | Border, muted text, or supporting surface |
| Mist Gray | `#6b7589` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Cloud | `#f1f5f9` | neutral | Page background or card surface |
| Mint Glaze | `#d6fcf4` | neutral | Page background or card surface |
| Lavender Mist | `#d8e0ea` | neutral | Page background or card surface |
| Royal Amethyst | `#862fe7` | brand | Action accent / signal color |
| Soft Amethyst | `#ad6df4` | accent | Action accent / signal color |
| Muted Amethyst | `#bd8ff0` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #111827;
  --ref-ghost-gray: #3f4654;
  --ref-mist-gray: #6b7589;
  --ref-canvas-white: #ffffff;
  --ref-pale-cloud: #f1f5f9;
  --ref-mint-glaze: #d6fcf4;
  --ref-lavender-mist: #d8e0ea;
  --ref-royal-amethyst: #862fe7;
}
```

## Typography direction
- **BricolageGrotesque**: 400, 600, 16px, 20px, 22px, 24px, 32px, 48px, 56px, 1.00, 1.20, 1.30, 1.50, 1.75; substitute `Montserrat`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 1.14, 1.25, 1.33, 1.50, 1.60, 1.80; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `12px`
- Radius: `cards: 24px, badges: 9999px, images: 16px, inputs: 12px, avatars: 9999px, buttons: 12px, navItems: 8px`

## Component cues
- **Primary Action Button**: Filled button
- **Secondary Action Button**: Outlined button
- **Ghost Navigation Button**: Text button with minimal styling
- **Feature Card**: Card container for content blocks
- **Accent Feature Card (Violet)**: Decorative card container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
