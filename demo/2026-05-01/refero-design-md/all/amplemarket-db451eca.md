# Amplemarket - Refero Design MD

- Source: https://styles.refero.design/style/db451eca-8de6-43a9-a5d5-35271befdffd
- Original site: https://www.amplemarket.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Subtle dynamism on a crisp canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Surface Charcoal | `#272625` | neutral | Primary text or dark surface |
| Muted Ash | `#6d6c6b` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#f4f3ef` | neutral | Page background or card surface |
| Light Taupe | `#ecebea` | neutral | Page background or card surface |
| Phoenix Orange | `#e8400d` | brand | Action accent / signal color |
| Cyan Glow | `#99fff9` | brand | Action accent / signal color |
| Deep Indigo | `#10054d` | brand | Action accent / signal color |
| Petal Pink | `#ffd7f0` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-canvas-white: #ffffff;
  --ref-surface-charcoal: #272625;
  --ref-muted-ash: #6d6c6b;
  --ref-whisper-gray: #f4f3ef;
  --ref-light-taupe: #ecebea;
  --ref-phoenix-orange: #e8400d;
  --ref-cyan-glow: #99fff9;
}
```

## Typography direction
- **Labil Grotesk Variable**: 400, 500, 700, 900, 8px, 10px, 12px, 14px, 16px, 20px, 24px, 28px, 36px, 44px, 56px, 84px, 0.80, 1.00, 1.10, 1.20, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `cards: 12px, icons: 12px, badges: 12px, images: 12px, inputs: 12px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background layer, providing a clean neutral base.
- **Whisper Gray** `#f4f3ef`: Slightly elevated background for content sections or client logo grids, adding subtle depth.
- **Surface Charcoal** `#272625`: Background for secondary containers like input fields on dark themes, or informational badges, providing distinct contrast.

## Component cues
- **Primary Filled Button - Dark**: Call to action button for primary actions.
- **Default Button - Light**: Secondary action button, standard interactive element.
- **Ghost Button**: Tertiary actions, navigation items, or subtle interactive elements.
- **Card - Elevated Light**: Container for featured content, testimonials, or key information.
- **Card - Client Logo**: Container for client logos with light background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
