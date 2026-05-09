# Telepathic Instruments - Refero Design MD

- Source: https://styles.refero.design/style/5183054c-4c6e-4ecf-bd90-f7d794d5eb17
- Original site: https://telepathicinstruments.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Techno-futurist laboratory

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#e5e7eb` | neutral | Page background or card surface |
| Charcoal | `#000000` | neutral | Primary text or dark surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Steel | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Ash | `#191919` | neutral | Primary text or dark surface |
| Mercury | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Powder | `#dddee2` | neutral | Page background or card surface |
| Muted Sage | `#d7cdb8` | neutral | Border, muted text, or supporting surface |
| Amber Glow | `#ff6c2f` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas: #e5e7eb;
  --ref-charcoal: #000000;
  --ref-snow: #ffffff;
  --ref-steel: #a3a3a3;
  --ref-ash: #191919;
  --ref-mercury: #c2c2c2;
  --ref-powder: #dddee2;
  --ref-muted-sage: #d7cdb8;
}
```

## Typography direction
- **Suisse Intl**: 400, 12px, 16px, 18px, 20px, 24px, 100px, 0.85, 1.20, 1.25, 1.40, 1.50; substitute `Inter`.
- **Suisse Intl Mono**: 400, 12px, 14px, 16px, 1.00, 1.20, 1.25, 1.33, 1.43, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 0px, large: 32px, buttons: 24px, default: 2px, circular: 9999px`

## Surface cues
- **Canvas** `#e5e7eb`: Primary page and content background.
- **Card Surface** `#ffffff`: Elevated content blocks on the canvas.
- **Base Dark Surface** `#000000`: Navbar background, dark content sections, primary buttons.

## Component cues
- **Primary Action Button**: Call to action button for primary actions.
- **Amber Glow Action Button**: Highlighting a key action for immediate visibility.
- **Ghost Button**: Secondary and tertiary actions that require less visual emphasis.
- **Text Link Button**: Low-prominence inline actions or navigation.
- **Product Card**: Displaying product information or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
