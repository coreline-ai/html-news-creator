# Miti Navi - Refero Design MD

- Source: https://styles.refero.design/style/887f0c74-c696-4589-82ae-85705ecda919
- Original site: https://miti-navi.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Nautical parchment and polished brass.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#e6dece` | neutral | Page background or card surface |
| Deep Charcoal | `#000e13` | neutral | Primary text or dark surface |
| Ebony | `#232323` | neutral | Primary text or dark surface |
| Linen | `#999999` | neutral | Border, muted text, or supporting surface |
| Amber Glaze | `#ffdead` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment: #e6dece;
  --ref-deep-charcoal: #000e13;
  --ref-ebony: #232323;
  --ref-linen: #999999;
  --ref-amber-glaze: #ffdead;
}
```

## Typography direction
- **Voyage**: 400, 16px, 46px, 72px, 130px, 180px, 0.90, 0.92, 0.94, 1.40; substitute `Playfair Display`.
- **GTSectraDisplay**: 400, 26px, 1.20; substitute `Tiempos Text`.
- **Times**: 400, 14px, 1.40; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `15px`
- Element Gap: `16px`
- Page Max Width: `1320px`
- Radius: `cards: 0px, buttons: 0px`

## Component cues
- **Primary Navigation Link**: Top-level navigation items
- **Filled Button (Deep Charcoal)**: Call to action for primary actions like 'Brochure MITI One'
- **Outlined Link (Amber Glaze)**: Distinguished interactive links, often for social media or legal pages
- **Ghost Card**: Content containers with no visual boundaries

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
