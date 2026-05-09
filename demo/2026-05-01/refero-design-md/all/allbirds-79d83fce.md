# Allbirds - Refero Design MD

- Source: https://styles.refero.design/style/79d83fce-84bf-4e12-8039-5d283c98917c
- Original site: https://allbirds.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft Natural Palette. Like hand-woven textiles and smoothed river stones.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| White Linen | `#ffffff` | neutral | Page background or card surface |
| Charcoal Slate | `#212121` | neutral | Primary text or dark surface |
| Warm Mist | `#e0dacf` | neutral | Page background or card surface |
| Storm Gray | `#525252` | neutral | Border, muted text, or supporting surface |
| Muted Olive | `#222519` | neutral | Primary text or dark surface |
| Desert Clay | `#a57e75` | brand | Action accent / signal color |
| Sky Dust | `#879aab` | brand | Action accent / signal color |
| Sandstone Tan | `#d1b0a4` | brand | Action accent / signal color |
| Sunlit Ochre | `#9e8949` | brand | Action accent / signal color |

```css
:root {
  --ref-black-ink: #000000;
  --ref-white-linen: #ffffff;
  --ref-charcoal-slate: #212121;
  --ref-warm-mist: #e0dacf;
  --ref-storm-gray: #525252;
  --ref-muted-olive: #222519;
  --ref-desert-clay: #a57e75;
  --ref-sky-dust: #879aab;
}
```

## Typography direction
- **Geograph**: 400, 500, 700, 12px, 14px, 16px, 20px, 24px, 1.00, 1.25, 1.33, 1.40, 1.43, 1.50, 1.67; substitute `Inter`.
- **Self Modern**: 400, 18px, 40px, 1.00, 1.20, 1.50, 1.78; substitute `Playfair Display`.
- **HurmeGeometricSans3-Regular**: 400, 14px, 1.14; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `42-90px`
- Element Gap: `4px`
- Radius: `cards: 16px, small: 4px, inputs: 1.67772e+07px, buttons: 1.67772e+07px`

## Component cues
- **Announcement Banner + Button Group**: Reference component style.
- **Category Navigation Cards**: Reference component style.
- **New Arrivals Product Cards with Utility Chips**: Reference component style.
- **Primary Filled Button**: Call to action.
- **Secondary Filled Button**: Alternative call to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
