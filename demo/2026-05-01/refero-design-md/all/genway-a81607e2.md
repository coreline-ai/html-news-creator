# Genway - Refero Design MD

- Source: https://styles.refero.design/style/a81607e2-254f-4f53-b357-68c39c9cfc03
- Original site: https://www.genway.ai
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft violet hazes, crisp text highlights

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Violet | `#0a0449` | brand | Action accent / signal color |
| Cool Gray | `#706e87` | neutral | Border, muted text, or supporting surface |
| Soft Lilac | `#efb9fd` | accent | Action accent / signal color |
| Vivid Amethyst | `#6b5ee0` | brand | Action accent / signal color |
| Deep Plum | `#0a0163` | brand | Action accent / signal color |
| Muted Lavender | `#a89fc7` | accent | Action accent / signal color |
| Soft Pinkish Gray | `#a085a6` | neutral | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f7f6fd` | neutral | Page background or card surface |
| Faded Lilac Gradient | `#e2e0f9` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-violet: #0a0449;
  --ref-cool-gray: #706e87;
  --ref-soft-lilac: #efb9fd;
  --ref-vivid-amethyst: #6b5ee0;
  --ref-deep-plum: #0a0163;
  --ref-muted-lavender: #a89fc7;
  --ref-soft-pinkish-gray: #a085a6;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Geist Regular**: 400, 10px, 12px, 14px, 16px, 20px, 24px, 1.2, 1.3, 1.5.
- **Geist**: 400, 500, 12px, 1.20.
- **Geist**: 400, 500, 12px, 1.20.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `cards: 12px, images: 120px, buttons: 32px, default: 12px, circular: 2000px, largeCards: 16px, specialCardTop: 16px 16px 0px 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for most content sections.
- **Whisper Gray** `#f7f6fd`: Background for distinct card-like sections or subtle content groupings, offering a slight visual offset from the main canvas.
- **Muted Lavender** `#a89fc7`: Used in some background gradients or as a very subtle elevated surface effect, providing an ethereal quality.
- **Deep Plum** `#0a0163`: The darkest tone in background gradients, creating deeper visual depth or as a base for hero sections.

## Component cues
- **Primary Headline**: Hero headline text
- **Body Text**: General paragraph content
- **Ghost Button**: Secondary action button
- **Primary Card (Subtle Elevation)**: Informational container
- **Background Card (No Elevation)**: Decorative or background informational container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
