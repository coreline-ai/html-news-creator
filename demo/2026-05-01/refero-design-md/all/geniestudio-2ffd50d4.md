# Geniestudio - Refero Design MD

- Source: https://styles.refero.design/style/2ffd50d4-93b7-4acf-9bc2-e86e61b63f27
- Original site: https://geniestudio.app
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, friendly illustrations.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#181d27` | brand | Action accent / signal color |
| Arctic Mist | `#fafdff` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Obsidian | `#0a0d12` | neutral | Primary text or dark surface |
| Silver Pine | `#535862` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#93979f` | neutral | Border, muted text, or supporting surface |
| Sky Wash | `#ebf5ff` | neutral | Page background or card surface |
| Ghostly Blue | `#cce7ff` | accent | Action accent / signal color |
| Electric Blue | `#0069e0` | accent | Action accent / signal color |
| Lavender Mist | `#f1e6ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #181d27;
  --ref-arctic-mist: #fafdff;
  --ref-canvas-white: #ffffff;
  --ref-obsidian: #0a0d12;
  --ref-silver-pine: #535862;
  --ref-ash-gray: #93979f;
  --ref-sky-wash: #ebf5ff;
  --ref-ghostly-blue: #cce7ff;
}
```

## Typography direction
- **Geist**: 500, 600, 10px, 12px, 14px, 16px, 18px, 20px, 1.14, 1.33, 1.35, 1.40, 1.50; substitute `Inter`.
- **Aeonik**: 500, 20px, 24px, 32px, 48px, 72px, 148px, 1.05, 1.11, 1.17, 1.20, 1.25; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `40px`
- Element Gap: `24px`
- Radius: `cards: 32px, icons: 16px, badges: 90px, images: 16px, buttons: 32px`

## Surface cues
- **Sky Wash Canvas** `#ebf5ff`: The foundational background color for the entire page, providing an ethereal, cool tint.
- **Canvas White Base** `#ffffff`: The primary background for most sections and content areas, offering a clean, bright foundation.
- **Arctic Mist Card** `#fafdff`: Elevated card backgrounds, creating subtle visual separation and depth.

## Component cues
- **Primary Action Button**: Call to action
- **Small Primary Action Button**: Secondary call to action
- **Header Action Button**: Navigation action
- **Feature Card**: Informational display
- **Decorative Icon Card (Round)**: Visual accent container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
