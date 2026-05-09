# Nomen Nescio - Refero Design MD

- Source: https://styles.refero.design/style/2fd71e12-12fc-4346-8281-52afe12bb951
- Original site: https://nomennescio.fi
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic architectural canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#2b2b2e` | neutral | Primary text or dark surface |
| Arctic Canvas | `#fdfdfa` | neutral | Page background or card surface |
| Whisper Gray | `#f5f3ee` | neutral | Page background or card surface |
| Limestone | `#bebcb4` | neutral | Border, muted text, or supporting surface |
| Dusty Road | `#deddd8` | neutral | Page background or card surface |
| Porcelain Whisper | `#d9d7c9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-charcoal: #2b2b2e;
  --ref-arctic-canvas: #fdfdfa;
  --ref-whisper-gray: #f5f3ee;
  --ref-limestone: #bebcb4;
  --ref-dusty-road: #deddd8;
  --ref-porcelain-whisper: #d9d7c9;
}
```

## Typography direction
- **nomennescio**: 400, 14px, 15px, 16px, 18px, 19px, 28px, 36px, 0.71, 1.00, 1.05, 1.11, 1.20, 1.25, 1.26, 1.33, 1.43; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `39px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `all: 0px`

## Component cues
- **Ghost Border Button**: Interactive elements, secondary actions, and navigational links.
- **Minimal Card**: Content containers for product listings, informational blocks.
- **Transparent Input Field**: Data entry fields within forms.
- **Ghost Badge**: Informational labels, category tags, promotional indicators.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
