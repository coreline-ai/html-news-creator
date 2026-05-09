# Humble - Refero Design MD

- Source: https://styles.refero.design/style/a6950b49-8ce4-4330-9499-26ca08061599
- Original site: https://humbleops.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precise White Lab

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Obsidian Text | `#1c1c1c` | neutral | Primary text or dark surface |
| Granite Gray | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#f1f1f1` | neutral | Page background or card surface |
| Alabaster Gray | `#ecebe8` | neutral | Page background or card surface |
| Electric Orange | `#ff4000` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-obsidian-text: #1c1c1c;
  --ref-granite-gray: #6e6e6e;
  --ref-ink-black: #000000;
  --ref-ghost-white: #f1f1f1;
  --ref-alabaster-gray: #ecebe8;
  --ref-electric-orange: #ff4000;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Bricolage Grotesque**: 500, 600, 16px, 18px, 20px, 24px, 32px, 42px, 44px, 50px, 58px, 0.70, 1.10, 1.20, 1.40, 1.50.
- **Geist**: 500, 600, 13px, 14px, 15px, 16px, 24px, 1.30, 1.40.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `10px`
- Radius: `cards: 30px, images: 40px, buttons: 100px, controls: 6px, largeBlock: 70px`

## Component cues
- **Ghost Button**: Primary call to action in hero sections or when a less prominent action is needed. Its inverse color scheme suggests a 'build' action for dark…
- **Product Features Card**: Standard card for content grouping, features, or product showcases. Characterized by soft elevation.
- **Enclosed Content Block**: A variant for structured content with internal padding, like forms or detailed information panels, maintaining the elevated card aesthetic.
- **Subtle Background Card**: Used for secondary information panels or a background for elements that need less visual weight, blending more into the canvas.
- **Hero Section Callout**: A distinct background shape within a hero section, often for a title or subtitle. Its rounded and translucent nature makes it suitable for overlays.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
