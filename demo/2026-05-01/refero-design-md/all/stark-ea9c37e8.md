# Stark - Refero Design MD

- Source: https://styles.refero.design/style/ea9c37e8-c56c-42aa-8e81-9b55222a5cd3
- Original site: https://www.getstark.co
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid Purple Actuator

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#10284b` | brand | Action accent / signal color |
| Stark Violet | `#381fd1` | brand | Action accent / signal color |
| Seafoam Mint | `#99d6cc` | brand | Action accent / signal color |
| Stark Gold | `#fedb63` | accent | Action accent / signal color |
| Lavender Mist | `#e5e0ff` | accent | Action accent / signal color |
| Linen Canvas | `#faf5ff` | neutral | Page background or card surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Outline Gray | `#e5e7eb` | neutral | Page background or card surface |
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Bone White | `#f6f6eb` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #10284b;
  --ref-stark-violet: #381fd1;
  --ref-seafoam-mint: #99d6cc;
  --ref-stark-gold: #fedb63;
  --ref-lavender-mist: #e5e0ff;
  --ref-linen-canvas: #faf5ff;
  --ref-cloud-white: #ffffff;
  --ref-outline-gray: #e5e7eb;
}
```

## Typography direction
- **ArminGrotesk**: 400, 500, 600, 900, 14px, 16px, 20px, 24px, 28px, 48px, 56px, 110px, 1.10, 1.43, 1.50, 1.70; substitute `Inter`.
- **RobotoMono**: 700, 13px, 16px, 1.40; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `tags: 20px, cards: 12px, buttons: 6px`

## Component cues
- **Primary Action Button**: Filled button for primary calls to action.
- **Secondary Action Button**: Filled button for secondary calls to action.
- **Ghost Internal Link Button**: Minimal button for internal navigation links, often in headers or footers.
- **Information Card Button**: Larger area button used for descriptive information, often within a card layout.
- **Feature Card (Teal)**: Informational card highlighted with a distinct background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
