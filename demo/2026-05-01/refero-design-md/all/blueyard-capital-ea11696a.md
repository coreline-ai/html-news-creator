# BlueYard Capital - Refero Design MD

- Source: https://styles.refero.design/style/ea11696a-17c0-41f8-9b08-c820851e0ea9
- Original site: https://www.blueyard.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft-focus intellectual ether.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#090b11` | neutral | Primary text or dark surface |
| Graphite | `#3a3a3e` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Mist | `#b5b0b0` | neutral | Border, muted text, or supporting surface |
| Sunken Gold | `#ffcf9e` | accent | Action accent / signal color |
| Cloud Indigo | `#babfff` | accent | Action accent / signal color |
| Amethyst Haze | `#e3a2ef` | accent | Action accent / signal color |
| Sky Veil | `#bfe0f7` | accent | Action accent / signal color |
| Ocean Whisper | `#8ceae4` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #090b11;
  --ref-graphite: #3a3a3e;
  --ref-canvas-white: #ffffff;
  --ref-pale-mist: #b5b0b0;
  --ref-sunken-gold: #ffcf9e;
  --ref-cloud-indigo: #babfff;
  --ref-amethyst-haze: #e3a2ef;
  --ref-sky-veil: #bfe0f7;
}
```

## Typography direction
- **Instrument Sans**: 400, 500, 12px, 24px, 48px, 54px, 1.00, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `12px`
- Element Gap: `5px`
- Radius: `tags: 0px, cards: 0px, images: 0px, inputs: 0px, buttons: 0px`

## Component cues
- **Primary Navigation Button**: The main menu toggle.
- **Text Only Button (Ghost)**: Used for secondary actions or navigation links with minimal visual weight.
- **Content Card - Default**: A neutral container for various content blocks.
- **Content Card - Canvas**: A base card for information presentation.
- **Category Tag - Sunken Gold**: Categorization tag for content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
