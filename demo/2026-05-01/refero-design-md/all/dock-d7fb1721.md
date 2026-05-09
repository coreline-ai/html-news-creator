# Dock - Refero Design MD

- Source: https://styles.refero.design/style/d7fb1721-1878-4cbb-a24b-051800557c75
- Original site: https://dock.us
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital workbench illuminated by electric blue. The experience is like working in a crisp, highly functional digital environment with precise tools.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#121722` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Horizon Gray | `#faf9f7` | neutral | Page background or card surface |
| Skyline Gray | `#efefef` | neutral | Page background or card surface |
| Mist Gray | `#a5a5a5` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0068f9` | brand | Action accent / signal color |
| Deep Royal | `#024bb1` | brand | Action accent / signal color |
| Lavender Mist | `#f4f0ff` | neutral | Page background or card surface |
| Mint Green | `#046645` | accent | Action accent / signal color |
| Periwinkle | `#d5ecff` | neutral | Page background or card surface |

```css
:root {
  --ref-inkwell: #121722;
  --ref-cloud-white: #ffffff;
  --ref-horizon-gray: #faf9f7;
  --ref-skyline-gray: #efefef;
  --ref-mist-gray: #a5a5a5;
  --ref-electric-blue: #0068f9;
  --ref-deep-royal: #024bb1;
  --ref-lavender-mist: #f4f0ff;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 40px, 48px, 57px, 84px, 1.06, 1.08, 1.09, 1.20, 1.25, 1.29, 1.33, 1.38, 1.43, 1.50, 1.56, 1.60; substitute `system-ui, sans-serif`.

## Spacing / shape
- Radius: `cards: 16px, pills: 100px, images: 8px, buttons: 48px, default: 16px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Product Tab Bar**: Reference component style.
- **Customer Stat Cards**: Reference component style.
- **Secondary Outlined Button**: Secondary Action
- **Feature Card Primary**: Content Display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
