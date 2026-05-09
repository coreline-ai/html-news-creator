# Aninix - Refero Design MD

- Source: https://styles.refero.design/style/653b7b25-f610-4a46-90e1-e3eed98b1f24
- Original site: https://www.aninix.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Utility Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Text | `#0b1118` | neutral | Primary text or dark surface |
| Charcoal Text | `#171717` | neutral | Primary text or dark surface |
| Ink Grey | `#333333` | neutral | Primary text or dark surface |
| Figma Grey | `#f0f0f0` | neutral | Page background or card surface |
| Muted Slate | `#5c6574` | neutral | Border, muted text, or supporting surface |
| Ghost Shadow | `#ced3d9` | neutral | Border, muted text, or supporting surface |
| Dusty Blue | `#c4d2db` | neutral | Action accent / signal color |
| Subtle Grey | `#89909a` | neutral | Border, muted text, or supporting surface |
| Action Violet | `#374fd5` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-text: #0b1118;
  --ref-charcoal-text: #171717;
  --ref-ink-grey: #333333;
  --ref-figma-grey: #f0f0f0;
  --ref-muted-slate: #5c6574;
  --ref-ghost-shadow: #ced3d9;
  --ref-dusty-blue: #c4d2db;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Arial, Helvetica, sans-serif`.
- **system-ui**: 400, 500, 700, 800, 16px, 18px, 1.44; substitute `Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif`.
- **P22 Mackinac Pro Medium**: 400, 20px, 1.40; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `10px`
- Radius: `cards: 16px, buttons: 8px, largeCards: 24px`

## Component cues
- **Ghost Primary Button**: Main call to action for the plugin installation.
- **Feature Content Card**: Displaying individual features or content blocks.
- **Elevated Content Card**: Prominent content card, often used for testimonials or key information.
- **Branded Label**: Small, distinct labels with brand recognition.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
