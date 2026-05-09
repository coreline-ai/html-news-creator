# Outseta - Refero Design MD

- Source: https://styles.refero.design/style/859d51e6-fc3f-45e0-a4c4-fe280c400ca7
- Original site: https://www.outseta.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gradient-infused SaaS canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Plum | `#240029` | neutral | Primary text or dark surface |
| Whisper Gray | `#d4ccd4` | neutral | Border, muted text, or supporting surface |
| Input Border Gray | `#767676` | neutral | Border, muted text, or supporting surface |
| Deep Plum Text | `#333333` | neutral | Primary text or dark surface |
| Rose Bloom | `#df37a7` | brand | Action accent / signal color |
| Muted Orchid | `#6d526d` | brand | Action accent / signal color |
| Sunshine Gold | `#ffcc11` | accent | Action accent / signal color |
| Vivid Cobalt | `#635bff` | accent | Action accent / signal color |
| Deep Pink Accent | `#d0339c` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-plum: #240029;
  --ref-whisper-gray: #d4ccd4;
  --ref-input-border-gray: #767676;
  --ref-deep-plum-text: #333333;
  --ref-rose-bloom: #df37a7;
  --ref-muted-orchid: #6d526d;
  --ref-sunshine-gold: #ffcc11;
}
```

## Typography direction
- **Inter Var**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 20px, 24px, 36px, 1.00, 1.20, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Kaio**: 700, 36px, 56px, 80px, 1.00, 1.10, 1.20; substitute `sans-serif`.
- **Jetbrains Mono**: 400, 12px, 14px, 16px, 1.20, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 14px, input: 4px, badges: 999px, buttons: 4px, default: 6px, heroCards: 22px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary background for most page content.
- **Faded Card Surface** `#29002905`: Subtle background for grouped content, offering a slight visual offset from the canvas.
- **Standard Card Surface** `#ffffff`: Elevated white cards with subtle shadow for main content blocks.

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Button**: Secondary action (light background)
- **Inverted Ghost Button (Dark Background)**: Secondary action (dark background)
- **Main Navigation Link Button**: Navigation button
- **Standard Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
