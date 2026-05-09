# sweetgreen - Refero Design MD

- Source: https://styles.refero.design/style/d91841cf-c717-43ef-97a2-400778fa6e1a
- Original site: https://www.sweetgreen.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Farmer's market clarity

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Fresh Sprout | `#e6ff55` | brand | Action accent / signal color |
| Garden Patch | `#00473c` | brand | Action accent / signal color |
| Soil Shadow | `#0e150e` | neutral | Primary text or dark surface |
| Field Cream | `#f4f3e7` | neutral | Page background or card surface |
| Willow Mist | `#d8e5d6` | neutral | Page background or card surface |
| Grain Sand | `#e8dcc6` | neutral | Page background or card surface |
| Stone Grey | `#8c8c82` | neutral | Border, muted text, or supporting surface |
| Charcoal Haze | `#9fa19f` | neutral | Border, muted text, or supporting surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-fresh-sprout: #e6ff55;
  --ref-garden-patch: #00473c;
  --ref-soil-shadow: #0e150e;
  --ref-field-cream: #f4f3e7;
  --ref-willow-mist: #d8e5d6;
  --ref-grain-sand: #e8dcc6;
  --ref-stone-grey: #8c8c82;
  --ref-charcoal-haze: #9fa19f;
}
```

## Typography direction
- **SweetSansText**: 400, 700, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.20, 1.25, 1.33, 1.38, 2.21, 2.64; substitute `Inter`.
- **SweetSans | Grenette**: 400, 40px, 70px, 80px, 0.85, 1.00; substitute `Montserrat`.
- **SweetSansText-Regular**: 400, 12px, 14px, 1.29, 1.33.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1440px`
- Radius: `cards: 24px, links: 4px, badges: 20px, images: 20px, inputs: 8px, buttons: 1000px`

## Surface cues
- **Field Cream** `#f4f3e7`: Dominant page background canvas, providing a clean and bright stage for content.
- **Willow Mist** `#d8e5d6`: Secondary background for content sections and various card surfaces, offering a subtle green tint.
- **Grain Sand** `#e8dcc6`: Tertiary background for specific cards or content blocks, introducing a slightly warmer, earthy tone.

## Component cues
- **Primary Action Button**: Main call-to-action button for initiating key processes.
- **Ghost Link Button**: Secondary action or navigation link within content.
- **Navigation Action Button**: Compact primary action within navigation bars.
- **Product Card**: Display for individual menu items or feature blocks.
- **Interactive Input Field**: Used for user data entry in forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
