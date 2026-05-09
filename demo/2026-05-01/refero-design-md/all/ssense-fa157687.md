# Ssense - Refero Design MD

- Source: https://styles.refero.design/style/fa157687-ee42-443e-a992-5f8a3fcdd48f
- Original site: https://ssense.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Blueprint – A precisely gridded display of curated visuals on a clean, unobtrusive canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Gray | `#333333` | neutral | Primary text or dark surface |
| Silver Thread | `#888888` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#979797` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Paper White | `#f4f4f4` | neutral | Page background or card surface |
| Alabaster | `#e8e8e8` | neutral | Page background or card surface |

```css
:root {
  --ref-ink-black: #000000;
  --ref-charcoal-gray: #333333;
  --ref-silver-thread: #888888;
  --ref-ash-gray: #979797;
  --ref-canvas-white: #ffffff;
  --ref-paper-white: #f4f4f4;
  --ref-alabaster: #e8e8e8;
}
```

## Typography direction
- **JHA Times Now**: 100, 400, 15px, 20px, 56px, 1.07, 1.20, 1.30, 2.00; substitute `Playfair Display, Lora`.
- **Favorit SSENSE Inter**: 400, 11px, 1.36; substitute `Inter, Arial`.
- **Favorit SSENSE Inter1**: 100, 400, 14px, 19px, 29px, 38px, 95px, 0.99, 1.16, 1.19, 1.26, 1.37; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `10-30px`
- Radius: `small: 10px, default: 0px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Recent Editorial Cards**: Reference component style.
- **Editorial CTA Block**: Reference component style.
- **Primary Navigation Link**: Top-level menu items
- **Editorial Hero Title**: Main feature headline

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
