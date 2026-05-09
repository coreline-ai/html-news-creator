# Circle - Refero Design MD

- Source: https://styles.refero.design/style/ab8450d9-1b42-4395-aa24-9e277f021aa1
- Original site: https://www.circle.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Galactic UI with soft glow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Eclipse | `#0a0a0a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Border | `#e4e7eb` | neutral | Page background or card surface |
| Dark Knight | `#191b1f` | neutral | Primary text or dark surface |
| Silver Whisper | `#737373` | neutral | Border, muted text, or supporting surface |
| Deep Indigo | `#3e1bc9` | brand | Action accent / signal color |
| Sky Burst | `#408fed` | brand | Action accent / signal color |
| Periwinkle Mist | `#e0eafc` | accent | Action accent / signal color |
| Lavender Haze | `#f2dbf5` | accent | Action accent / signal color |
| Peach Cream | `#fff0d8` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-eclipse: #0a0a0a;
  --ref-canvas-white: #ffffff;
  --ref-slate-border: #e4e7eb;
  --ref-dark-knight: #191b1f;
  --ref-silver-whisper: #737373;
  --ref-deep-indigo: #3e1bc9;
  --ref-sky-burst: #408fed;
  --ref-periwinkle-mist: #e0eafc;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 10px, 11px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 48px, 56px, 64px, 1.10, 1.20, 1.21, 1.25, 1.28, 1.29, 1.30, 1.33, 1.40, 1.43, 1.45, 1.50, 1.56; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `93px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `1376px`
- Radius: `cards: 24px, inputs: 9999px, buttons: 9999px, decorativeElements: 32px`

## Surface cues
- **Canvas White** `#ffffff`: Dominant page background, primary stage for content.
- **Accent Pale Rose** `#fef2f2`: Lightest accent background for subtle segmentation or content blocks.
- **Accent Peach Tint** `#fff0d8`: Mid-level accent background, providing a slightly warmer tone.
- **Accent Aqua Mist** `#e4f6f4`: Another mid-level accent background, offering a cool, refreshing tint.
- **Accent Periwinkle** `#e0eafc`: A deeper accent background, used for more pronounced content separation or card backgrounds.

## Component cues
- **Ghost Navigation Button**: Primary navigation and secondary actions in headers and footers.
- **Accent Filled Button**: Calls to action or categorical filters.
- **Product Feature Card**: Displaying product features or content blocks.
- **Translucent Highlight Card**: Elevated, semi-transparent content areas within contrasting backgrounds.
- **Input Field**: Standard text input for forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
