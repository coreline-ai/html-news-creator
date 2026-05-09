# Evergreen - Refero Design MD

- Source: https://styles.refero.design/style/a4314209-7688-4750-842a-432c3918a21b
- Original site: https://www.evergreen.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment, dark ink, verdant accent

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Rich Earth | `#000000` | neutral | Primary text or dark surface |
| Parchment | `#edede2` | neutral | Page background or card surface |
| Cloud Whisper | `#ffffff` | neutral | Page background or card surface |
| Forest Fern | `#beedc0` | brand | Action accent / signal color |
| Deep Slate | `#333333` | neutral | Primary text or dark surface |
| Soft Vanilla | `#fffff3` | neutral | Page background or card surface |

```css
:root {
  --ref-rich-earth: #000000;
  --ref-parchment: #edede2;
  --ref-cloud-whisper: #ffffff;
  --ref-forest-fern: #beedc0;
  --ref-deep-slate: #333333;
  --ref-soft-vanilla: #fffff3;
}
```

## Typography direction
- **Arial**: 400, 12px, 1.6.
- **ivypresto-headline**: 600, 54px, 74px, 1.40, 1.48, 1.49; substitute `Playfair Display`.
- **Rubik**: 400, 500, 600, 700, 12px, 17px, 18px, 19px, 20px, 21px, 23px, 28px, 30px, 1.00, 1.41, 1.54, 1.70, 1.90; substitute `Inter`.

## Spacing / shape
- Section Gap: `165px`
- Card Padding: `17px`
- Element Gap: `14px`
- Radius: `cards: 10px, input: 7px, links: 30px, other: 46px, buttons: 40.5px`

## Surface cues
- **Parchment** `#edede2`: Dominant page background, main canvas.
- **Soft Vanilla** `#fffff3`: Card backgrounds, elevated content containers.
- **Cloud Whisper** `#ffffff`: Input fields, foreground elements against Soft Vanilla.
- **Forest Fern** `#beedc0`: Circular accent cards, decorative background areas for visual interest.
- **Rich Earth** `#000000`: Top banner background.

## Component cues
- **Filled Primary Button**: Primary calls to action
- **Navigation Link Button**: Secondary calls to action or navigation links within headers
- **Product Feature Card**: Highlighting features or testimonials effectively.
- **Circular Accent Card**: Decorative elements or image containers.
- **Text Input Field**: Forms and data entry.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
