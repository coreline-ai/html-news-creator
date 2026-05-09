# Savvycal - Refero Design MD

- Source: https://styles.refero.design/style/83b71dd8-de08-4c57-80b2-9fced17a0ca5
- Original site: https://savvycal.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organic Green Engine. A lush, vibrant green landscape where every element functions with precision.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| SavvyGreen | `#0d542b` | brand | Action accent / signal color |
| LimeAccent | `#b9ff78` | accent | Action accent / signal color |
| BurntOrange | `#f54320` | accent | Action accent / signal color |
| Parchment | `#fcf7ed` | neutral | Page background or card surface |
| Coal | `#1c1917` | neutral | Primary text or dark surface |
| ForestGreen | `#008236` | brand | Action accent / signal color |
| SubtleGreenTint | `#dcfce7` | neutral | Action accent / signal color |
| Slate | `#44403b` | neutral | Border, muted text, or supporting surface |
| LightBorder | `#e5e7eb` | neutral | Page background or card surface |
| CrimsonPattern | `#ffe3e3` | neutral | Page background or card surface |

```css
:root {
  --ref-savvygreen: #0d542b;
  --ref-limeaccent: #b9ff78;
  --ref-burntorange: #f54320;
  --ref-parchment: #fcf7ed;
  --ref-coal: #1c1917;
  --ref-forestgreen: #008236;
  --ref-subtlegreentint: #dcfce7;
  --ref-slate: #44403b;
}
```

## Typography direction
- **GT-Alpina-Condensed**: 700, 96px, 136px, 1.00, 1.08; substitute `Playfair Display`.
- **GT-America-Condensed**: 400, 18px, 38px, 1.38, 1.56; substitute `Oswald`.
- **GT-America-Standard**: 400, 700, 16px, 18px, 20px, 24px, 30px, 1.33, 1.38, 1.50, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `48-64px`
- Element Gap: `16px`
- Radius: `cards: 8px, badges: 24px, buttons: 8px, default: 8px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Pricing Card**: Reference component style.
- **Feature Section Block**: Reference component style.
- **Primary CTA Button**: Main call to action button (e.g., 'Try SavvyCal risk-free')
- **Secondary CTA Button - Orange**: Alternative call to action button for specific, emphasized actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
