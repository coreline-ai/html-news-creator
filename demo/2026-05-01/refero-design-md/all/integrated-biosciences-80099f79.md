# Integrated Biosciences - Refero Design MD

- Source: https://styles.refero.design/style/80099f79-72b7-4367-b2e9-6a3d4a3e9e6a
- Original site: https://integratedbiosciences.com
- Theme: `mixed`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Academia Laboratory: A meticulously organized workbench under a cool, precise spotlight.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Carbon | `#222f30` | neutral | Primary text or dark surface |
| Fog | `#4d5757` | neutral | Border, muted text, or supporting surface |
| Sage Mist | `#c9cbbe` | neutral | Border, muted text, or supporting surface |
| Cloud Canvas | `#e7e8e1` | neutral | Page background or card surface |
| Light Gray | `#eeeeee` | neutral | Page background or card surface |
| Off-White | `#f7f7f5` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Bio-Green | `#cef79e` | accent | Action accent / signal color |
| Deep Sea | `#445e5f` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-carbon: #222f30;
  --ref-fog: #4d5757;
  --ref-sage-mist: #c9cbbe;
  --ref-cloud-canvas: #e7e8e1;
  --ref-light-gray: #eeeeee;
  --ref-off-white: #f7f7f5;
  --ref-polar-white: #ffffff;
}
```

## Typography direction
- **Aspekta**: 400, 16px, 18px, 19px, 22px, 24px, 36px, 42px, 58px, 75px, 89px, 111px, 158px, 1.00, 1.10, 1.20, 1.30; substitute `Inter`.
- **Roboto Mono**: 400, 13px, 14px, 15px, 1.00, 1.23; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `tags: 20px, cards: 40px, buttons: 8px, default: 8px`

## Surface cues
- **Midnight Base** `#000000`: Primary page background, especially in hero sections and immersive experiences.
- **Off-White Canvas** `#f7f7f5`: Dominant background for content sections in light mode, primary light canvas.
- **Cloud Card** `#e7e8e1`: Background for secondary content cards or containers, offering a warm subtle contrast to Off-White.
- **Light Gray Card** `#eeeeee`: Background for additional content cards, providing a cooler, more neutral variation.

## Component cues
- **Navigation Button**: Outlined Button
- **Header Action Button**: Filled Button
- **Primary Action CTA Button (Text-only)**: Text Button
- **News Article Card**: Content Grid Item
- **Text Input**: Form Element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
