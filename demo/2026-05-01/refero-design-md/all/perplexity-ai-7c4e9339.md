# Perplexity AI - Refero Design MD

- Source: https://styles.refero.design/style/7c4e9339-591c-46c3-ac3d-20c1b5b5a568
- Original site: https://www.perplexity.ai/products/computer
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Garden of computational flora — technical interface blooming through botanical haze

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Aged Sepia | `#271a00` | brand | Action accent / signal color |
| Parchment | `#faf8f5` | neutral | Page background or card surface |
| Fog | `#d1cfc7` | neutral | Border, muted text, or supporting surface |
| Absolute Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Moss Shadow | `#7c7464` | neutral | Border, muted text, or supporting surface |
| Deep Forest | `#23291b` | neutral | Primary text or dark surface |
| Teal Accent | `#0f3639` | accent | Action accent / signal color |
| Ash Mist | `#e5e5e3` | neutral | Page background or card surface |
| Slate Edge | `#121516` | neutral | Primary text or dark surface |

```css
:root {
  --ref-aged-sepia: #271a00;
  --ref-parchment: #faf8f5;
  --ref-fog: #d1cfc7;
  --ref-absolute-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-moss-shadow: #7c7464;
  --ref-deep-forest: #23291b;
  --ref-teal-accent: #0f3639;
}
```

## Typography direction
- **pplxSans**: 300, 400, 500, 11-96px, 1.00-1.50; substitute `Inter, -apple-system, sans-serif`.
- **pplxSansMono**: 400, 500, 600, 10-14px, 1.00-1.50; substitute `JetBrains Mono, Consolas, monospace`.
- **pplxSerif**: 300, 400, 24-96px, 1.00-1.12; substitute `Georgia, Times New Roman, serif`.

## Spacing / shape
- Section Gap: `28px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 12px, other: 4px, badges: 4px, inputs: 4px, buttons: 40px`

## Surface cues
- **Parchment Canvas** `#faf8f5`: Page background — the cream foundation upon which all content rests
- **Pure White Card** `#ffffff`: Primary content cards — pristine white floats 2-3% above Parchment base
- **Fog Divider** `#d1cfc7`: Borders, button fills, subtle separators — midtone bridging layer
- **Deep Forest Overlay** `#23291b`: Nav on scroll, elevated dark surfaces — near-black with botanical tint

## Component cues
- **Task Cards — Workflow Step Stack**: Reference component style.
- **Button Group — CTA Variants**: Reference component style.
- **Feature Card — White on Parchment**: Reference component style.
- **Ghost Nav Button**: Transparent navigation links
- **Pill CTA Button**: Primary action (Try Computer)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
