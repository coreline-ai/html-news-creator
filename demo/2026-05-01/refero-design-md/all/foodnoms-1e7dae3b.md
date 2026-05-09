# Foodnoms - Refero Design MD

- Source: https://styles.refero.design/style/1e7dae3b-cb34-4fcf-8c32-051152aebbab
- Original site: https://foodnoms.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant Data Clarity – like a meticulously organized information dashboard lit by colorful indicator lights.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Graphite Text | `#2f2f2f` | neutral | Primary text or dark surface |
| Raven Black | `#000000` | neutral | Primary text or dark surface |
| Warm Gray | `#f5f5f5` | neutral | Page background or card surface |
| Tangerine Accent | `#ff5406` | brand | Action accent / signal color |
| Sunshine Orange | `#ff6d00` | brand | Action accent / signal color |
| Crimson | `#ff3400` | brand | Action accent / signal color |
| Vivid Green | `#00b33f` | semantic | Action accent / signal color |
| Sky Blue | `#00a9dd` | semantic | Action accent / signal color |
| Deep Purple | `#5856de` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-graphite-text: #2f2f2f;
  --ref-raven-black: #000000;
  --ref-warm-gray: #f5f5f5;
  --ref-tangerine-accent: #ff5406;
  --ref-sunshine-orange: #ff6d00;
  --ref-crimson: #ff3400;
  --ref-vivid-green: #00b33f;
}
```

## Typography direction
- **Aquawax Pro**: 700, 18px, 22px, 30px, 60px, 1.20, 1.40; substitute `Montserrat Bold, Lato Bold`.
- **Aquawax Pro**: 500, 17px, 20px, 1.60, 1.80; substitute `Montserrat Medium, Lato Medium`.
- **Aquawax Pro**: 600, 14px, 16px, 1.20, 1.40; substitute `Montserrat SemiBold, Lato SemiBold`.

## Spacing / shape
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `all: 26px, cards: 26px, buttons: 26px`

## Component cues
- **Primary CTA Banner**: Reference component style.
- **Feature Stats / Metric Cards**: Reference component style.
- **Nutrition Goal Cards (Calories / Carbs / Fat / Protein)**: Reference component style.
- **Primary Action Button**: Primary Calls to Action
- **Secondary Action Button**: Secondary Calls to Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
