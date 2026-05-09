# Streamtime - Refero Design MD

- Source: https://styles.refero.design/style/9be20798-843b-424c-bc87-192edc0cce22
- Original site: https://streamtime.net
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized chaos, vibrant collage

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Off Black | `#2f2c29` | neutral | Primary text or dark surface |
| Vanilla Cream | `#fbf8f5` | neutral | Page background or card surface |
| Warm Mist | `#f1e8de` | neutral | Page background or card surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Light Steel | `#999999` | neutral | Border, muted text, or supporting surface |
| Warm Clay | `#eadcce` | neutral | Page background or card surface |
| Stone Buff | `#c3b7ac` | neutral | Border, muted text, or supporting surface |
| Canary Yellow | `#ffde3b` | brand | Action accent / signal color |
| Shocking Pink | `#ff4dd5` | brand | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-off-black: #2f2c29;
  --ref-vanilla-cream: #fbf8f5;
  --ref-warm-mist: #f1e8de;
  --ref-whisper-white: #ffffff;
  --ref-light-steel: #999999;
  --ref-warm-clay: #eadcce;
  --ref-stone-buff: #c3b7ac;
}
```

## Typography direction
- **Ease Display**: 400, 16px, 28px, 30px, 68px, 100px, 1.00, 1.10, 1.20; substitute `Montserrat, system-ui`.
- **Ease Standard**: 400, 12px, 16px, 18px, 1.10, 1.20; substitute `Inter, system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `30px`
- Element Gap: `16px`
- Radius: `button: 160px, default: 5px, navigation: 96px`

## Surface cues
- **Warm Mist Canvas** `#f1e8de`: Primary page background, the foundational layer for all content.
- **Vanilla Cream Surface** `#fbf8f5`: Elevated card backgrounds, offering a subtle visual break from the canvas.
- **Whisper White Panel** `#ffffff`: Pure white backgrounds for navigation, headers, or specific content blocks requiring maximum brightness.
- **Off Black Deep Surface** `#2f2c29`: Distinct dark sections, typically for hero banners or feature blocks, providing strong contrast.

## Component cues
- **Primary Action Button**: Main call to action
- **Rounded Button**: Secondary action or menu button
- **Content Card - Default**: Standard content containers with a subtle background
- **Content Card - Stone Buff**: Alternative content container for visual variation
- **Navigation Item - Canary Yellow**: Highlights active or selected navigation states

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
