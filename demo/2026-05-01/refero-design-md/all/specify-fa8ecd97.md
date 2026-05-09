# Specify - Refero Design MD

- Source: https://styles.refero.design/style/fa8ecd97-5052-4909-a4b4-50419ad9d00a
- Original site: https://specifyapp.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Subdued white canvas, violet sparks

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#000000` | neutral | Primary text or dark surface |
| Carbon Surface | `#1a1d1e` | neutral | Primary text or dark surface |
| Ash Gray | `#f6f7f9` | neutral | Page background or card surface |
| Cloud Gray | `#ebedef` | neutral | Page background or card surface |
| Medium Gray | `#8d8e8f` | neutral | Border, muted text, or supporting surface |
| Graphite | `#5f6162` | neutral | Border, muted text, or supporting surface |
| Subtle Dark Background | `#151718` | neutral | Primary text or dark surface |
| Specify Violet | `#624de3` | brand | Action accent / signal color |
| Highlight Violet | `#8d4af7` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-charcoal-text: #000000;
  --ref-carbon-surface: #1a1d1e;
  --ref-ash-gray: #f6f7f9;
  --ref-cloud-gray: #ebedef;
  --ref-medium-gray: #8d8e8f;
  --ref-graphite: #5f6162;
  --ref-subtle-dark-background: #151718;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Inter**: 400, 8px, 10px, 12px, 14px, 16px, 20px, 24px, 32px, 48px, 64px, 1.00, 1.13, 1.17, 1.20, 1.25, 1.50, 1.60, 1.71, 2.00, 2.40, 3.00; substitute `system-ui, sans-serif`.
- **Fira Code**: 400, 14px, 1.57; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, small: 6px, buttons: 6px, default: 6px, circular: 100px, pillButtons: 40px`

## Surface cues
- **White Canvas** `#ffffff`: Primary page background and base surface.
- **Ash Gray** `#f6f7f9`: Secondary background for sections and content blocks, providing subtle visual separation.
- **Standard Card** `#ffffff`: Elevated card surfaces with shadows, used for distinct content containers.
- **Subtle Dark Background** `#151718`: Hero sections or banners, creating a strong visual break and contrast.

## Component cues
- **Primary Filled Button**: Main call to action button.
- **Ghost Button (dark text)**: Secondary action button for less prominent interactions.
- **Pill Button (Dark Background)**: Specialized button for small actions or tags.
- **Standard Card**: Information container, feature display.
- **Ghost Card**: Decorative or less prominent information display, often on dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
