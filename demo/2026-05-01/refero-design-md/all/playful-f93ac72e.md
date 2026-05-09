# Playful - Refero Design MD

- Source: https://styles.refero.design/style/f93ac72e-73b2-4b2c-80eb-351ddfa56f4d
- Original site: https://playful.software
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gradient Playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0f172a` | neutral | Primary text or dark surface |
| Vivacious Pink | `#ff2e95` | brand | Action accent / signal color |
| Frost Canvas | `#f6f2ee` | neutral | Page background or card surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#111111` | neutral | Primary text or dark surface |
| Coal Text | `#202126` | neutral | Primary text or dark surface |
| Pale Ash | `#e8e5e0` | neutral | Page background or card surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#414040` | neutral | Border, muted text, or supporting surface |
| Light Taupe | `#e2dcd6` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #0f172a;
  --ref-vivacious-pink: #ff2e95;
  --ref-frost-canvas: #f6f2ee;
  --ref-pitch-black: #000000;
  --ref-deep-graphite: #111111;
  --ref-coal-text: #202126;
  --ref-pale-ash: #e8e5e0;
  --ref-cloud-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 900, 14px, 16px, 18px, 26px, 30px, 70px, 79px, 1.00, 1.15, 1.19, 1.20, 1.23, 1.33, 1.70; substitute `system-ui, sans-serif`.
- **Arial**: 400, 600, 700, 13px, 15px, 16px, 20px, 1.20, 1.40; substitute `Helvetica Neue, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `113px`
- Card Padding: `12px`
- Element Gap: `10px`
- Page Max Width: `1500px`
- Radius: `tags: 999px, cards: 44px, images: 16px, buttons: 99px`

## Component cues
- **Ghost Button**: Navigational or secondary actions where visual weight should be minimal.
- **Primary Action Button**: Main calls to action.
- **Circular Secondary Button**: Icon-only or small, focused interactive elements.
- **Feature Card**: Displaying product features or content blocks.
- **Input Field**: Collecting user data.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
