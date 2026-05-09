# Zora - Refero Design MD

- Source: https://styles.refero.design/style/5c4eb249-fa38-4254-81e0-a32ee22766e2
- Original site: https://zora.co
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw Concrete Gallery

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite Dark | `#121212` | neutral | Primary text or dark surface |
| Slate Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#878787` | neutral | Border, muted text, or supporting surface |
| Fog Contrast | `#e6e6e6` | neutral | Page background or card surface |
| Signal Green | `#00df00` | brand | Action accent / signal color |
| Vivid Magenta | `#ff00f0` | accent | Action accent / signal color |
| Electro Pink Gradient | `#ff00d9` | accent | Action accent / signal color |
| Luminous Green Gradient | `#62ff00` | accent | Action accent / signal color |
| Monochrome Stripe Gradient | `#d2d2d2` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-graphite-dark: #121212;
  --ref-slate-gray: #4d4d4d;
  --ref-ash-gray: #878787;
  --ref-fog-contrast: #e6e6e6;
  --ref-signal-green: #00df00;
  --ref-vivid-magenta: #ff00f0;
  --ref-electro-pink-gradient: #ff00d9;
}
```

## Typography direction
- **MonumentGrotesk**: 410, 450, 500, 600, 11px, 13px, 15px, 16px, 17px, 1.09, 1.23, 1.25, 1.33, 1.41; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `20px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `cards: 12px, badges: 999px, buttons: 8px, round-elements: 50%`

## Component cues
- **Suggested Follows Panel**: Reference component style.
- **Content Card with Buy Action**: Reference component style.
- **NFT Card with Price Bar**: Reference component style.
- **Ghost Button**: Functional text buttons for navigation and secondary actions.
- **Rectangular Text Button**: Secondary action buttons, often inline.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
