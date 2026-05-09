# User Interviews - Refero Design MD

- Source: https://styles.refero.design/style/376baf20-9ace-405d-bf4a-086016f2b1e3
- Original site: https://www.userinterviews.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Teal-accented architectural blueprint on pristine parchment.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#f2f8f7` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Inkwell Black | `#000000` | neutral | Primary text or dark surface |
| Slate Gray | `#283338` | neutral | Primary text or dark surface |
| Cloud Frost | `#e4f0f1` | neutral | Page background or card surface |
| Misty Teal | `#cae1e2` | neutral | Page background or card surface |
| Oceanic Teal | `#1c5d5f` | brand | Action accent / signal color |
| Deep Teal | `#0e4749` | brand | Action accent / signal color |
| Emerald Green | `#156152` | brand | Action accent / signal color |
| Berry Blush | `#d6aec1` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #f2f8f7;
  --ref-polar-white: #ffffff;
  --ref-inkwell-black: #000000;
  --ref-slate-gray: #283338;
  --ref-cloud-frost: #e4f0f1;
  --ref-misty-teal: #cae1e2;
  --ref-oceanic-teal: #1c5d5f;
  --ref-deep-teal: #0e4749;
}
```

## Typography direction
- **sofia-pro**: 400, 500, 700, 12px, 13px, 14px, 16px, 18px, 19px, 20px, 22px, 24px, 1.00, 1.27, 1.33, 1.38, 1.40, 1.43, 1.44, 1.46, 1.50, 1.53, 1.56, 1.71, 2.00; substitute `Montserrat, Lato`.
- **p22-mackinac-pro**: 400, 500, 30px, 44px, 50px, 64px, 1.16, 1.20, 1.32, 1.33; substitute `Merriweather, Playfair Display`.
- **P 22 Mackinac italic**: 700, 30px, 36px, 50px, 1.17, 1.20, 1.33; substitute `Merriweather Italic, Playfair Display Italic`.

## Spacing / shape
- Section Gap: `88px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `tags: 100px, forms: 88px, pills: 1000px, buttons: 48px, largeElements: 88px`

## Component cues
- **Primary Filled Button - Oceanic Teal**: Main call-to-action.
- **Secondary Filled Button - Emerald Green**: Alternative call-to-action, active state for related actions.
- **Ghost Button - Inkwell Black**: Subtle calls to action or navigation links.
- **Outlined Tag Button - Sky Blue**: Filter tags or categorization buttons.
- **Outlined Tag Button - Berry Blush**: Alternative tag style, secondary filter options.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
