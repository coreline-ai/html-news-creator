# Antimetal - Refero Design MD

- Source: https://styles.refero.design/style/9f9a4a4f-1a27-47ca-a65b-68b9850a84e4
- Original site: https://antimetal.com
- Theme: `mixed`
- Recommended fit: **Data dashboard / source ledger**

## North star
Electric storm over a blueprint - vivid neon signal cutting through deep navy atmosphere, then snapping to precise technical daylight.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Navy | `#1b2540` | brand | Primary text, heading color on light surfaces, nav text, icon fills, input text, border color across cards and form ele. |
| Deep Cosmos | `#001033` | brand | Blue action color for filled buttons, selected navigation states, and focused conversion moments. |
| Chartreuse Pulse | `#d0f100` | accent | Green action color for filled buttons, selected navigation states, and focused conversion moments. |
| Ice Veil | `#e0f6ff` | accent | Ghost button borders in dark hero mode, subtle icon stroke tints, very-light atmospheric surface wash in the hero region |
| Ghost Canvas | `#f8f9fc` | neutral | Primary page background, card fill for feature sections, section backgrounds in the light product UI |
| Pure Surface | `#ffffff` | neutral | Elevated card surfaces above the ghost canvas - product UI cards, floating pill badges, modal-level surfaces |
| Slate Ink | `#6b7184` | neutral | Secondary body text, muted labels, icon fills at reduced emphasis |
| Ash Medium | `#7c8293` | neutral | Tertiary text, hairline border fills, subtle strokes on dividers and icon outlines |

```css
:root {
  --ref-midnight-navy: #1b2540;
  --ref-deep-cosmos: #001033;
  --ref-chartreuse-pulse: #d0f100;
  --ref-ice-veil: #e0f6ff;
  --ref-ghost-canvas: #f8f9fc;
  --ref-pure-surface: #ffffff;
  --ref-slate-ink: #6b7184;
}
```

## Typography direction
- Primary: **abcdFont**; substitute `Inter Variable or DM Sans`.
- Secondary/code: **ivarTextFont**; substitute `Freight Display Pro or Fraunces`.

## Spacing / shape
- Section gap: `80px`
- Card padding: `20px`
- Element gap: `8px`
- Radius: `{'cards': '20px', 'badges': '16px', 'inputs': '0px', 'buttons': '9999px', 'pillLarge': '60px', 'cardsSmall': '6px', 'cardsMedium': '16px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
