# monday.com - Refero Design MD

- Source: https://styles.refero.design/style/77ee57e9-9f8e-4ec1-93f7-cc1c4b84307a
- Original site: https://monday.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant organized workspace — like a digital desk splashed with colorful sticky notes and neatly arranged tools.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Text Primary | `#333333` | neutral | Primary text or dark surface |
| Text Muted | `#676879` | neutral | Border, muted text, or supporting surface |
| Canvas Background | `#ffffff` | neutral | Page background or card surface |
| Surface Accent | `#f5f6f8` | neutral | Page background or card surface |
| Interactive Violet | `#6161ff` | brand | Action accent / signal color |
| Outline Ebony | `#000000` | neutral | Primary text or dark surface |
| Border Silver | `#d0d4e4` | neutral | Border, muted text, or supporting surface |
| Interactive Graphite | `#535768` | neutral | Border, muted text, or supporting surface |
| Card Mint | `#bcfe90` | accent | Action accent / signal color |
| Card Lavender | `#eddff7` | accent | Action accent / signal color |

```css
:root {
  --ref-text-primary: #333333;
  --ref-text-muted: #676879;
  --ref-canvas-background: #ffffff;
  --ref-surface-accent: #f5f6f8;
  --ref-interactive-violet: #6161ff;
  --ref-outline-ebony: #000000;
  --ref-border-silver: #d0d4e4;
  --ref-interactive-graphite: #535768;
}
```

## Typography direction
- **Poppins**: 300, 400, 500, 700, 8px, 12px, 13px, 14px, 16px, 18px, 20px, 22px, 24px, 28px, 32px, 36px, 40px, 48px, 52px, 56px, 64px, 1.15, 1.20, 1.30, 1.31, 1.40, 1.45, 1.50, 1.60, 1.69, 2.00, 2.29, 2.46; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 24px, input: 0px, badges: 6px, images: 12px, buttons: 160px, general: 6px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, primary canvas for content, and general elevated surfaces.
- **Surface Accent Light** `#f5f6f8`: Used for differentiated cards, badges, and subtle background variation, offering a slight visual lift without strong contrast.
- **Card Accents** `#eddff7`: A range of accent background colors like Lavender (#eddff7), Mint (#bcfe90), Sky (#abf0ff), and Sunset (#ff8940) for specific cards to distinguish…

## Component cues
- **Primary Call to Action Button**: Interactive Element
- **Outlined Call to Action Button**: Interactive Element
- **Text Link Button**: Interactive Element
- **Feature Card**: Content Display
- **Basic Card**: Content Display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
