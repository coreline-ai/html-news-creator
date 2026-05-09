# Ashleyandco - Refero Design MD

- Source: https://styles.refero.design/style/645d7583-8391-455b-83d2-c95fb7fe91dc
- Original site: https://ashleyandco.co
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm gray minimalism on unbleached paper.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f6f3f0` | neutral | Page background or card surface |
| Ink | `#3c3c3c` | neutral | Primary text or dark surface |
| Onyx | `#000000` | neutral | Primary text or dark surface |
| Mist | `#dedfdb` | neutral | Page background or card surface |
| Porcelain | `#ffffff` | neutral | Page background or card surface |
| Ash | `#434343` | neutral | Border, muted text, or supporting surface |
| Stone | `#939393` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas: #f6f3f0;
  --ref-ink: #3c3c3c;
  --ref-onyx: #000000;
  --ref-mist: #dedfdb;
  --ref-porcelain: #ffffff;
  --ref-ash: #434343;
  --ref-stone: #939393;
}
```

## Typography direction
- **Neue Haas Grotesk Text**: 400, 500, 11px, 12px, 18px, 24px, 1.10, 1.20; substitute `Helvetica Neue, Arial`.
- **Martina Plant**: 400, 500, 20px, 24px, 42px, 0.72, 1.10.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `20px`
- Element Gap: `15px`
- Radius: `default: 10px`

## Component cues
- **Ghost Button - Light Text**: Default interactive element, often for secondary actions or navigation.
- **Ghost Button - Muted Text**: Subtle interactive elements, often found in footers or less prominent areas.
- **Ghost Button - Hero White Text**: Interactive elements against dark or image backgrounds.
- **Primary Filled Button**: Key call-to-action button for initiating primary actions.
- **Untouched Card/Media Holder**: Container for images, product listings, or informational content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
