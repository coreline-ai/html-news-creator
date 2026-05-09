# Anna Jóna - Refero Design MD

- Source: https://styles.refero.design/style/71717c5a-324a-40ed-8a09-9a35df74f1d3
- Original site: https://annajona.is
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Raspberry Vignette – a soft, inviting space defined by gentle curves and heartfelt reds.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Blush | `#fce1e3` | neutral | Page background or card surface |
| Heartfelt Red | `#db404f` | brand | Action accent / signal color |
| Midnight Ink | `#0e1736` | brand | Action accent / signal color |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-blush: #fce1e3;
  --ref-heartfelt-red: #db404f;
  --ref-midnight-ink: #0e1736;
  --ref-pitch-black: #000000;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Sansita**: 700, 28px, 39px, 49px, 70px, 1.06, 1.11, 1.14, 1.17, 1.40; substitute `DM Serif Display`.
- **Nunito Sans**: 400, 700, 18px, 25px, 72px, 1.20, 1.50; substitute `Open Sans`.
- **Nunito Sans**: 400, 700, 18px, 25px, 72px, 1.20, 1.50; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `115px`
- Card Padding: `40px`
- Element Gap: `11px`
- Radius: `buttons: 300px, decorativeElements: 90px`

## Component cues
- **Primary Action Button**: Crucial calls to action
- **Ghost Button**: Secondary actions or navigation
- **Curved Information Card**: Content container with an organic shape

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
