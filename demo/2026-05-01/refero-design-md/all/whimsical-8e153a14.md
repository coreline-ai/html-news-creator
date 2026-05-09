# Whimsical - Refero Design MD

- Source: https://styles.refero.design/style/8e153a14-40a9-4793-b94b-c144d325c730
- Original site: https://whimsical.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Plush Violet Cloud

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Plum | `#250835` | brand | Action accent / signal color |
| Soft Mauve | `#473054` | neutral | Primary text or dark surface |
| Faded Violet | `#ab2fed` | accent | Action accent / signal color |
| Sky Blue | `#0283ec` | accent | Action accent / signal color |
| Luminous Grape | `#4b38ee` | accent | Action accent / signal color |
| Fuschia Delight Gradient | `#ba59ff` | brand | Action accent / signal color |
| Cosmic Bloom Gradient | `#3ca1ff` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#ebe6ee` | neutral | Page background or card surface |
| Silver Mist | `#f5f4f5` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-plum: #250835;
  --ref-soft-mauve: #473054;
  --ref-faded-violet: #ab2fed;
  --ref-sky-blue: #0283ec;
  --ref-luminous-grape: #4b38ee;
  --ref-fuschia-delight-gradient: #ba59ff;
  --ref-cosmic-bloom-gradient: #3ca1ff;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Agrandir**: 700, 24px, 48px, 64px, 96px, 1.00, 1.10; substitute `Montserrat`.
- **Manrope**: 400, 500, 600, 700, 9px, 10px, 12px, 13px, 14px, 16px, 32px, 1.00, 1.20, 1.40, 2.67; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, buttons: 12px, containers: 16px, largeElements: 120px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for the entire page, providing a bright, clean foundation.
- **Base Surface** `#f5f4f5`: Slightly elevated background for minor sections or subtle container separation, providing minimal visual break.
- **Card Surface** `#ebe6ee`: Primary background for cards and feature blocks, offering a clear visual boundary against the page canvas.
- **Accent Surface** `#decaff`: Decorative background for specific cards or sections, adding a soft, branded color wash.
- **Decorative Highlight** `#e9bded`: Stronger decorative background to draw attention to key sections, often paired with gradients.

## Component cues
- **Primary Filled Button**: Main call to action, interactive controls
- **Menu Ghost Button**: Secondary navigation links, discreet actions
- **Large Feature Button**: Prominent feature calls to action within content sections
- **Standard Content Card**: Organizes content blocks, visual features
- **Decorative Background Card (Washed Lavender)**: Background visual elements, abstract shapes

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
