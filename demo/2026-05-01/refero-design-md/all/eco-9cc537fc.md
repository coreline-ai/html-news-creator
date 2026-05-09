# Eco - Refero Design MD

- Source: https://styles.refero.design/style/9cc537fc-97d8-4632-8703-f9aa296c2206
- Original site: https://eco.com
- Theme: `mixed`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural tech blueprint. Polished surfaces and precise typography overlay an expansive, slightly muted cityscape.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Smoke | `#ffffff` | neutral | Page background or card surface |
| Off-White Mist | `#efefef` | neutral | Page background or card surface |
| Midnight Ink | `#0f111a` | neutral | Primary text or dark surface |
| Dark Charcoal | `#000000` | neutral | Primary text or dark surface |
| Near Black | `#141414` | neutral | Primary text or dark surface |
| Light Steel | `#aeaeae` | neutral | Border, muted text, or supporting surface |
| Graphite Grey | `#2a2a2a` | neutral | Primary text or dark surface |
| Mid Grey | `#222222` | neutral | Primary text or dark surface |
| Pale Ash | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Skybound Gradient | `#1c53bd` | brand | Action accent / signal color |

```css
:root {
  --ref-white-smoke: #ffffff;
  --ref-off-white-mist: #efefef;
  --ref-midnight-ink: #0f111a;
  --ref-dark-charcoal: #000000;
  --ref-near-black: #141414;
  --ref-light-steel: #aeaeae;
  --ref-graphite-grey: #2a2a2a;
  --ref-mid-grey: #222222;
}
```

## Typography direction
- **Interdisplay**: 400, 14px, 16px, 24px, 40px, 84px, 90px, 96px, 0.90, 0.95, 1.06, 1.20, 1.43, 1.50; substitute `Inter`.
- **Roobert**: 400, 16px, 48px, 84px, 96px, 0.95, 1.06, 1.20, 1.33; substitute `Montserrat`.
- **Inter**: 400, 14px, 16px, 22px, 1.00, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `large: 128px, inputs: 8px, buttons: 8px, default: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Stat Block**: Reference component style.
- **Feature Cards Row**: Reference component style.
- **Primary Filled Button**: Main call to action for interactive steps.
- **Secondary Filled Button**: Alternative call to action, less prominent than primary.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
