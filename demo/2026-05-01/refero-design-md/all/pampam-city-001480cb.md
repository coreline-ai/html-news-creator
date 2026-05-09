# pampam.city - Refero Design MD

- Source: https://styles.refero.design/style/001480cb-05f4-4802-be39-84b942169481
- Original site: https://www.pampam.city
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft Canvas Typography

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Buttermilk | `#faf2ec` | neutral | Page background or card surface |
| Ash Gray | `#e5e5e5` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#1b1917` | neutral | Primary text or dark surface |
| Cool Gray | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Slate Blue | `#9894a8` | neutral | Action accent / signal color |
| Field Green | `#2b3ea7` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-buttermilk: #faf2ec;
  --ref-ash-gray: #e5e5e5;
  --ref-ink-black: #000000;
  --ref-charcoal: #1b1917;
  --ref-cool-gray: #8f8f8f;
  --ref-slate-blue: #9894a8;
  --ref-field-green: #2b3ea7;
}
```

## Typography direction
- **-apple-system**: 400, 500, 600, 16px, 18px, 24px, 1.00, 1.20, 1.56; substitute `system-ui`.
- **inter**: 400, 550, 14px, 16px, 18px, 19px, 1.43, 1.47, 1.50, 1.56; substitute `Inter`.
- **nineties**: 400, 28px, 48px, 80px, 1.08; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 12px, buttons: 16px, general: 20px`

## Surface cues
- **Canvas White Base** `#ffffff`: Primary page background layer, providing high contrast for text.
- **Buttermilk Canvas** `#faf2ec`: Secondary background layer for most content areas, cards, and sections.
- **Ash Gray Detail** `#e5e5e5`: Subtle background for specific UI elements, dividers, or very light container backgrounds.

## Component cues
- **Standard Button**: Primary interaction button
- **Outlined Muted Button**: Secondary interaction or ghost button
- **Feature Card**: Content container for features or examples
- **Standard Input Field**: Form input elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
