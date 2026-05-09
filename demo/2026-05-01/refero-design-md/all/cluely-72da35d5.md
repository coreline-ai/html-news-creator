# Cluely - Refero Design MD

- Source: https://styles.refero.design/style/72da35d5-1cfd-41a3-94f6-cb6b8c07a670
- Original site: https://cluely.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Radiant cloud-native intelligence: ethereal gradients, frosted glass, and digital blue accents against a bright canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#e4e4e7` | neutral | Page background or card surface |
| Surface Text | `#000000` | neutral | Primary text or dark surface |
| Paragraph Gray | `#2e3038` | neutral | Primary text or dark surface |
| Muted Text | `#777a88` | neutral | Border, muted text, or supporting surface |
| Sky Canvas | `#f3f8ff` | neutral | Page background or card surface |
| Digital Blue | `#3c83f6` | brand | Action accent / signal color |
| Deep Ocean Gradient Start | `#0544a9` | brand | Action accent / signal color |
| Frost Morning Gradient Start | `#ddefe6` | accent | Action accent / signal color |
| Process Blue Gradient Start | `#1e82e0` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-subtle-gray: #e4e4e7;
  --ref-surface-text: #000000;
  --ref-paragraph-gray: #2e3038;
  --ref-muted-text: #777a88;
  --ref-sky-canvas: #f3f8ff;
  --ref-digital-blue: #3c83f6;
  --ref-deep-ocean-gradient-start: #0544a9;
}
```

## Typography direction
- **Geist**: 300, 400, 500, 600, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 18px, 19px, 20px, 24px, 28px, 30px, 36px, 42px, 48px, 56px, 1.00, 1.11, 1.13, 1.20, 1.25, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.60; substitute `Inter`.
- **EB Garamond**: 500, 80px, 1.02; substitute `Garamond`.
- **ui-monospace**: 400, 10px, 1.5.

## Spacing / shape
- Section Gap: `73px`
- Card Padding: `22px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `tags: 4px, cards: 24px, inputs: 4px, buttons: 1.67772e+07px`

## Component cues
- **Pill Button - Ghost**: Secondary action button, often paired with primary actions or for discrete functionalities.
- **Pill Button - Primary**: Main call-to-action button, visually distinct and inviting interaction.
- **Pill Button - Shadowed Overlay**: Interactive elements within product screenshots, mimicking OS-level controls.
- **Feature Card - Transparent**: Displaying product features or information blocks without heavy visual presence.
- **Content Input Field**: Standard text input for forms, often with a product-like dark aesthetic.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
