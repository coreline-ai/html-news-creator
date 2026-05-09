# Rivian - Refero Design MD

- Source: https://styles.refero.design/style/a5dc5626-1103-42e3-9edb-a6d52fb9a210
- Original site: https://rivian.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Subtle Power, Precision Engineering.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | brand | Action accent / signal color |
| Arctic White | `#ffffff` | brand | Action accent / signal color |
| Slate Gray | `#151515` | neutral | Primary text or dark surface |
| Cloud Drifter | `#f2f2f2` | neutral | Page background or card surface |
| Ash Concrete | `#e5e7eb` | neutral | Page background or card surface |
| Dark Asphalt | `#212121` | neutral | Primary text or dark surface |
| Chrome Accent | `#cfd0d0` | neutral | Border, muted text, or supporting surface |
| Sunbeam Yellow | `#ffac00` | accent | Action accent / signal color |
| Forest Green | `#629b5c` | accent | Action accent / signal color |
| Desert Orange | `#e84826` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-arctic-white: #ffffff;
  --ref-slate-gray: #151515;
  --ref-cloud-drifter: #f2f2f2;
  --ref-ash-concrete: #e5e7eb;
  --ref-dark-asphalt: #212121;
  --ref-chrome-accent: #cfd0d0;
  --ref-sunbeam-yellow: #ffac00;
}
```

## Typography direction
- **Adventure**: 400, 500, 600, 10px, 11px, 12px, 14px, 16px, 20px, 24px, 32px, 36px, 44px, 56px, 72px, 120px, 0.93, 1.00, 1.07, 1.09, 1.11, 1.13, 1.14, 1.17, 1.20, 1.25, 1.33, 1.40, 1.43, 1.50, 1.55; substitute `system-ui, sans-serif`.
- **Liga**: 500, 360px, 1.00; substitute `system-ui, sans-serif`.
- **Sohne**: 500, 12px, 1.33; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24-48px`
- Card Padding: `0px`
- Element Gap: `4-28px`
- Radius: `inputs: 4px, buttons: 40px, general: 8px`

## Component cues
- **Hero Promo Banner with CTA Buttons**: Reference component style.
- **Vehicle Info Card — R1S**: Reference component style.
- **Location Selector Dropdown**: Reference component style.
- **Primary Filled Button - Arctic White**: Primary Call-to-Action
- **Primary Filled Button - Midnight Ink**: Inverted Primary Call-to-Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
