# Timescale - Refero Design MD

- Source: https://styles.refero.design/style/ae175f23-1ec7-47ea-9380-7bff7041028b
- Original site: https://www.timescale.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial Blueprint on stark white.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Shadow Gray | `#6c6c6c` | neutral | Border, muted text, or supporting surface |
| Silverline | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Action Orange | `#ff5b29` | brand | Action accent / signal color |
| Highlight Yellow | `#f5ff80` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-midnight-ink: #000000;
  --ref-shadow-gray: #6c6c6c;
  --ref-silverline: #b3b3b3;
  --ref-action-orange: #ff5b29;
  --ref-highlight-yellow: #f5ff80;
}
```

## Typography direction
- **Geist**: 400, 600, 700, 14px, 16px, 18px, 20px, 24px, 52px, 80px, 1.10, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `Inter`.
- **Geist Mono**: 400, 500, 600, 700, 14px, 16px, 20px, 24px, 28px, 40px, 50px, 1.10, 1.20, 1.33, 1.40, 1.43, 1.50; substitute `JetBrains Mono`.
- **ui-sans-serif**: 400, 600, 16px, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 9999px, cards: 12px, links: 8px, inputs: 4px, buttons: 4px`

## Surface cues
- **Canvas White** `#fafafa`: Primary page background and base surface for cards and UI elements.
- **Highlight Yellow** `#f5ff80`: Ephemeral banners and active state backgrounds.
- **Midnight Ink** `#000000`: Dominant background for footer and filled interactive elements, providing high contrast.

## Component cues
- **Outlined Primary Button**: Main call to action, ghost style
- **Filled Secondary Button**: Alternative call to action, solid fill
- **Highlight Action Button**: Prominent, distinct call to action
- **Feature Card**: Content container for features or integrations
- **Basic Card**: Simple content container without aggressive shadowing

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
