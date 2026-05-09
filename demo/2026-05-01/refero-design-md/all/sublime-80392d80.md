# Sublime - Refero Design MD

- Source: https://styles.refero.design/style/80392d80-3970-46f0-a7ed-f213f316c933
- Original site: https://sublime.app
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard of Ideas: bold strokes on a bright, uncluttered surface, punctuated by sharp, focused annotations.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Charcoal Text | `#181816` | neutral | Primary text or dark surface |
| Fog Gray | `#efefef` | neutral | Page background or card surface |
| Zinc Gray | `#908f8e` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#a29e9c` | neutral | Border, muted text, or supporting surface |
| Sage Green | `#38744d` | accent | Action accent / signal color |
| Mint Accent | `#e0f5ff` | accent | Action accent / signal color |
| Lime Highlight | `#cbffa6` | accent | Action accent / signal color |
| Slate Text | `#6a6967` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-charcoal-text: #181816;
  --ref-fog-gray: #efefef;
  --ref-zinc-gray: #908f8e;
  --ref-ash-gray: #a29e9c;
  --ref-sage-green: #38744d;
  --ref-mint-accent: #e0f5ff;
}
```

## Typography direction
- **Control Upright**: 400, 12px, 14px, 16px, 18px, 24px, 28px, 64px, 142px, 0.90, 1.00, 1.13, 1.16, 1.39; substitute `Arial Bold`.
- **Times New Roman**: 400, 14px, 16px, 18px, 1.20, 1.39; substitute `serif`.

## Spacing / shape
- Section Gap: `200px`
- Card Padding: `18px`
- Element Gap: `15px`
- Radius: `tags: 999px, cards: 5px, footer: 40px, buttons: 5px`

## Component cues
- **Primary Action Button (Filled)**: Call-to-action button
- **Secondary Action Button (Ghost)**: Subtle button for secondary actions or navigation
- **Neutral Button**: General utility button
- **Text Link Button**: Interactive text link that behaves like a button
- **Small Pill Tag**: Informational tag for related content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
