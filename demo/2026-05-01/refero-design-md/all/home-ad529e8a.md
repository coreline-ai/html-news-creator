# Home - Refero Design MD

- Source: https://styles.refero.design/style/ad529e8a-3427-4152-bed9-6ec5097f25b6
- Original site: https://moderne.st
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Art-filled creative canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Almond | `#f3eae5` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Surface Snow | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#3e3c43` | neutral | Primary text or dark surface |
| Stone Whisper | `#7a7780` | neutral | Border, muted text, or supporting surface |
| Input Pale | `#cfc7c5` | neutral | Border, muted text, or supporting surface |
| Hero Violet | `#0e1889` | brand | Action accent / signal color |
| Creative Peach | `#ff7e85` | brand | Action accent / signal color |
| Lively Rose | `#ff7399` | brand | Action accent / signal color |
| Insight Teal | `#206871` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-almond: #f3eae5;
  --ref-midnight-ink: #000000;
  --ref-surface-snow: #ffffff;
  --ref-ash-gray: #3e3c43;
  --ref-stone-whisper: #7a7780;
  --ref-input-pale: #cfc7c5;
  --ref-hero-violet: #0e1889;
  --ref-creative-peach: #ff7e85;
}
```

## Typography direction
- **Mabry Pro**: 400, 500, 16px, 19px, 20px, 27px, 43px, 52px, 56px, 69px, 83px, 0.93, 0.95, 1.00, 1.02, 1.06, 1.20; substitute `Montserrat`.
- **Helvetica Neue**: 400, 500, 600, 700, 14px, 15px, 16px, 18px, 20px, 22px, 26px, 1.07, 1.18, 1.19, 1.20, 1.33, 1.40, 1.56; substitute `Arial`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1200px`
- Radius: `card: 4px, badge: 4px, input: 4px, button: 4px, default: 4px, largeCard: 15px`

## Surface cues
- **Canvas Almond** `#f3eae5`: Base page background
- **Surface Snow** `#ffffff`: Primary card and content surfaces
- **Accent Orange** `#ffb283`: Elevated, distinctly colored cards
- **Insight Teal** `#206871`: Alternative elevated, distinctly colored cards

## Component cues
- **Primary Action Button**: Filled Call-to-Action button
- **Secondary Action Button**: Ghost or subtle action button
- **Outlined Link Button**: Link button with a distinct outline
- **Standard Card**: Content container for features or information
- **Accent Card - Orange**: Prominent content card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
