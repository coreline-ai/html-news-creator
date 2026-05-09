# Liquid Death - Refero Design MD

- Source: https://styles.refero.design/style/b6f2b036-e48e-452f-b003-941c491015c0
- Original site: https://liquiddeath.com
- Theme: `mixed`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Heavy Metal Vending Machine

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Death Black | `#000000` | neutral | Primary text or dark surface |
| Bone White | `#ffffff` | neutral | Page background or card surface |
| Off-Black | `#151515` | neutral | Primary text or dark surface |
| Ash Gray | `#e3e3e3` | neutral | Page background or card surface |
| Gravel Gray | `#727272` | neutral | Border, muted text, or supporting surface |
| Light Ash | `#f5f5f5` | neutral | Page background or card surface |
| Charcoal | `#232323` | neutral | Primary text or dark surface |
| Input Border | `#999999` | neutral | Border, muted text, or supporting surface |
| Polished Gold | `#d2ac5a` | accent | Action accent / signal color |
| Antique Gold | `#8a6d35` | accent | Action accent / signal color |

```css
:root {
  --ref-death-black: #000000;
  --ref-bone-white: #ffffff;
  --ref-off-black: #151515;
  --ref-ash-gray: #e3e3e3;
  --ref-gravel-gray: #727272;
  --ref-light-ash: #f5f5f5;
  --ref-charcoal: #232323;
  --ref-input-border: #999999;
}
```

## Typography direction
- **Acumin Pro**: 400, 500, 700, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 36px, 40px, 56px, 60px, 1.00, 1.05, 1.13, 1.20, 1.29, 1.50, 1.67, 2.00; substitute `'Inter', 'Roboto', sans-serif`.
- **acumin-pro-condensed**: 400, 700, 10px, 16px, 18px, 20px, 45px, 1.00, 1.05, 1.20, 1.30; substitute `'Roboto Condensed', sans-serif`.

## Spacing / shape
- Card Padding: `24px`
- Radius: `tags: 0px, cards: 0px, inputs: 0px, buttons: 0px`

## Component cues
- **Product Cards — Beverage Grid**: Reference component style.
- **Merch Product Card Row**: Reference component style.
- **Full-Width Banner CTAs + Email Capture**: Reference component style.
- **Primary Action Button**: Key CTAs like 'Shop Now' or 'Add to Cart'.
- **Secondary Action Button**: Less prominent actions like 'Join the Contest'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
