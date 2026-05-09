# Apple - Refero Design MD

- Source: https://styles.refero.design/style/a4f123f2-cd4b-4d26-998f-a3d3ee158024
- Original site: https://apple.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Polished lens on innovation — clear, precise, and understated.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#1d1d1f` | neutral | Primary text or dark surface |
| Deep Gray | `#333333` | neutral | Primary text or dark surface |
| Charcoal Grey | `#474747` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#707070` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#858585` | neutral | Border, muted text, or supporting surface |
| Light Silver | `#c7c7c7` | neutral | Border, muted text, or supporting surface |
| Border Silver | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Lightest Gray Background | `#e2e2e5` | neutral | Page background or card surface |
| Canvas White | `#f5f5f7` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-graphite: #1d1d1f;
  --ref-deep-gray: #333333;
  --ref-charcoal-grey: #474747;
  --ref-medium-gray: #707070;
  --ref-light-gray: #858585;
  --ref-light-silver: #c7c7c7;
  --ref-border-silver: #d6d6d6;
  --ref-lightest-gray-background: #e2e2e5;
}
```

## Typography direction
- **SF Pro Text**: 300, 400, 600, 12px, 14px, 17px, 18px, 24px, 26px, 34px, 44px, 1.00, 1.18, 1.24, 1.29, 1.33, 1.47, 1.50, 2.12, 2.41; substitute `system-ui`.
- **SF Pro Display**: 400, 600, 700, 21px, 28px, 40px, 56px, 1.07, 1.10, 1.14, 1.19; substitute `system-ui`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `15px`
- Element Gap: `10px`
- Radius: `cards: 0px, lists: 999px, images: 8px, inputs: 0px, buttons: 980px`

## Surface cues
- **Canvas White** `#f5f5f7`: Dominant page background, providing a clean, bright foundation for all content.
- **Pure White** `#ffffff`: Elevated UI elements, such as navigation backgrounds and certain content blocks, creating a subtle contrast against the primary canvas.
- **Lightest Gray Background** `#e2e2e5`: Subtle background for interactive elements or contained components, indicating a slightly recessed or grouped area.
- **Pale Blue Overlay** `#9fc6f4`: Accent surface for specific sections or product narratives, introducing a soft, branded color block.

## Component cues
- **Primary Filled Button**: Call to action
- **Outline Link Button**: Secondary action or navigation
- **Text Link Button**: Tertiary action, inline navigation
- **Unstyled Text Button**: Minimal interactive element for dense UI
- **Navigation Link**: Global navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
