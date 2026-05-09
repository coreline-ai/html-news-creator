# Lightship - Refero Design MD

- Source: https://styles.refero.design/style/fdcd4cbb-4db6-4138-9cfd-964795f1e1d6
- Original site: https://lightshiprv.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black & White Canvas: a crisp, high-contrast visual journey on a warm, earthy canvas.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Paper White | `#faf6ef` | neutral | Page background or card surface |
| Subtle Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Outline Gray | `#d9d9d9` | neutral | Page background or card surface |
| Medium Gray | `#a1a1a1` | neutral | Border, muted text, or supporting surface |
| Action Orange | `#fa5c40` | accent | Action accent / signal color |

```css
:root {
  --ref-pure-black: #000000;
  --ref-canvas: #ffffff;
  --ref-paper-white: #faf6ef;
  --ref-subtle-gray: #999999;
  --ref-outline-gray: #d9d9d9;
  --ref-medium-gray: #a1a1a1;
  --ref-action-orange: #fa5c40;
}
```

## Typography direction
- **F37Bolton**: 400, 700, 12px, 14px, 16px, 20px, 22px, 24px, 34px, 48px, 64px, 72px, 75px, 1.00, 1.20, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 0px, links: 20px, inputs: 100px, buttons: 20px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, general container surfaces.
- **Paper White** `#faf6ef`: Secondary background for cards and specific content blocks, providing subtle visual separation.

## Component cues
- **Text Button - Dark**: Ghost
- **Text Button - Light**: Ghost
- **Outlined Button - Light**: Ghost
- **Outlined Button - Dark**: Ghost
- **Default Card**: Content Container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
