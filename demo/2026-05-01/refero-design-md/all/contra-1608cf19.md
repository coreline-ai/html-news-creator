# Contra - Refero Design MD

- Source: https://styles.refero.design/style/1608cf19-b249-46d4-bd37-b4c6a7fc4b56
- Original site: https://contra.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Frosted glass on dark slate; a refined digital workspace.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Slate | `#222834` | neutral | Primary text or dark surface |
| Ash Gray | `#14171f` | neutral | Primary text or dark surface |
| Phantom Gray | `#677084` | neutral | Border, muted text, or supporting surface |
| Silver Pine | `#9ba2b0` | neutral | Border, muted text, or supporting surface |
| Porcelain | `#e5e7eb` | neutral | Page background or card surface |
| Ghost White | `#f5f6f9` | neutral | Page background or card surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#d0d4dc` | neutral | Border, muted text, or supporting surface |
| Contra Violet | `#6a57e3` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-slate: #222834;
  --ref-ash-gray: #14171f;
  --ref-phantom-gray: #677084;
  --ref-silver-pine: #9ba2b0;
  --ref-porcelain: #e5e7eb;
  --ref-ghost-white: #f5f6f9;
  --ref-charcoal-black: #000000;
}
```

## Typography direction
- **GT Standard M**: 400, 500, 600, 12px, 14px, 15px, 16px, 24px, 1.15, 1.20, 1.33, 1.40, 1.43, 1.50, 1.60; substitute `Inter`.
- **GT Standard L**: 400, 500, 600, 8px, 12px, 19px, 23px, 58px, 0.88, 1.05, 1.33, 1.39, 1.47; substitute `Inter`.

## Spacing / shape
- Section Gap: `65px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `tags: 32px, cards: 16px, inputs: 0px, avatars: 50%, buttons: 24px, modules: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background.
- **Ghost White** `#f5f6f9`: Secondary background for discreet sections or hover states.

## Component cues
- **Filled Primary Button**: Calls to action, form submissions.
- **Ghost Button**: Secondary actions, filtering, navigation.
- **Outlined Input Field**: User input for forms, search bars.
- **Compact Filter Button**: Filtering and categorization within content sections.
- **Content Card (Featured)**: Displaying articles, projects, or featured content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
