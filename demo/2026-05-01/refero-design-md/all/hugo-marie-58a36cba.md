# Hugo & Marie - Refero Design MD

- Source: https://styles.refero.design/style/58a36cba-3fc4-48fa-a7d9-7f14592b7857
- Original site: https://www.hugoandmarie.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid on Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#0a0a0a` | neutral | Primary text or dark surface |
| Ash Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Input Border Gray | `#767676` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #0a0a0a;
  --ref-ash-gray: #b3b3b3;
  --ref-silver-mist: #cccccc;
  --ref-input-border-gray: #767676;
}
```

## Typography direction
- **soehne**: 300, 400, 14px, 16px, 20px, 22px, 1.00, 1.15, 1.20, 1.40, 1.44, 1.64, 1.80; substitute `system-ui`.
- **saol-display**: 100, 100px, 0.95; substitute `serif`.
- **soehne-mono**: 400, 13px, 1.31; substitute `monospace`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `20px`
- Element Gap: `5px`
- Radius: `badges: 9999px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, providing a pristine, open base for content.
- **Input Surface** `#cccccc`: Subtle background for badges or other low-prominence UI elements.
- **Hero Overlay** `#000000`: Background for full-bleed hero sections or image overlays, creating contrast.

## Component cues
- **Ghost Text Button**: Interactive element, navigation
- **Pill Badge - Light Text**: Categorization, status indicator
- **Pill Badge - Gray Border**: Categorization, status indicator
- **Text Input - Dark**: Data entry
- **Text Input - Light**: Data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
