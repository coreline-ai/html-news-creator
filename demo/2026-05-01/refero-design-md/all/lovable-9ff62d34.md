# Lovable - Refero Design MD

- Source: https://styles.refero.design/style/9ff62d34-e48d-4fcb-9fd9-c018e2747542
- Original site: https://lovable.dev
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting gradient nebula

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fcfbf8` | neutral | Page background or card surface |
| Text Primary | `#1c1c1c` | neutral | Primary text or dark surface |
| Border Light | `#eceae4` | neutral | Page background or card surface |
| Text Secondary | `#5f5f5d` | neutral | Border, muted text, or supporting surface |
| Text Ghost | `#2e2e2d` | neutral | Primary text or dark surface |
| Accent Gradient | `#1f55f1` | accent | Action accent / signal color |
| Text Callout | `#030303` | neutral | Primary text or dark surface |
| Focus Border | `#c5c4c2` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fcfbf8;
  --ref-text-primary: #1c1c1c;
  --ref-border-light: #eceae4;
  --ref-text-secondary: #5f5f5d;
  --ref-text-ghost: #2e2e2d;
  --ref-accent-gradient: #1f55f1;
  --ref-text-callout: #030303;
  --ref-focus-border: #c5c4c2;
}
```

## Typography direction
- **Camera Plain Variable**: 400, 480, 600, 12px, 14px, 15px, 16px, 18px, 20px, 36px, 48px, 60px, 1.00, 1.10, 1.25, 1.38, 1.50, 1.60; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `20px`
- Element Gap: `6px`
- Page Max Width: `1280px`
- Radius: `cards: 16px, links: 12px, buttons: 8px, inputField: 28px`

## Surface cues
- **Canvas Base** `#fcfbf8`: Dominant background for the entire page, providing a bright, clean foundation. Used for main content areas and default surfaces.
- **Card Surface** `#fcfbf8`: Used for content cards and elevated blocks, maintaining the Canvas Base color but distinguished by border-radius and subtle shadowing or padding.
- **Input / Interactive Surface** `#fcfbf8`: Applied to input fields and interactive elements. Shares the Canvas Base color, but interaction is visually indicated through distinct border-radii,…

## Component cues
- **Primary Navigation Link**: Top navigation items and footer links that guide users through the site structure.
- **Ghost Header Button**: Call to action buttons in the header, encouraging login or getting started.
- **Pill Accent Button**: Small, informational buttons or tags with a rounded 'pill' shape.
- **Hero Input Field**: Prominent text input for primary action on the hero section.
- **Feature Card**: Displays featured content or product examples in a grid layout.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
