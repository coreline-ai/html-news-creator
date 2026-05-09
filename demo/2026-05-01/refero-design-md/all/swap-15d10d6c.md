# Swap - Refero Design MD

- Source: https://styles.refero.design/style/15d10d6c-1844-46c6-ae69-c99a56e6ad41
- Original site: https://www.swap-commerce.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp AI Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite Inset | `#2d3637` | neutral | Primary text or dark surface |
| Shadow Green BG | `#0d5b3b` | neutral | Action accent / signal color |
| Deep Forest BG | `#083a26` | neutral | Primary text or dark surface |
| Stone Beige | `#e9e7e2` | neutral | Page background or card surface |
| Outline Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Muted Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Mint Accent | `#a3fda7` | brand | Action accent / signal color |
| Subtle Sage | `#9cb0a8` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-graphite-inset: #2d3637;
  --ref-shadow-green-bg: #0d5b3b;
  --ref-deep-forest-bg: #083a26;
  --ref-stone-beige: #e9e7e2;
  --ref-outline-gray: #cccccc;
  --ref-text-black: #000000;
  --ref-muted-ash: #999999;
}
```

## Typography direction
- **mainFont**: 400, 500, 700, 9px, 12px, 15px, 16px, 18px, 24px, 30px, 1.00, 1.20, 1.40, 1.50; substitute `Inter`.
- **secondaryFont**: 100, 300, 72px, 80px, 120px, 0.95, 1.00; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `cards: 24px, inputs: 100px, buttons: 200px, general: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Card with Shadow** `#ffffff`: Default elevated content cards
- **Dark Content Card** `#2d3637`: Dark background for feature sections or distinct content blocks
- **Accent Gradient Card** `#083a26`: Accent colored background for specific content cards or sections

## Component cues
- **Ghost Text Button**: Navigation links and secondary actions
- **Pill Accent Button**: Primary call-to-actions
- **Pill Ghost Button**: Secondary and descriptive actions
- **Card with Shadow**: Content containers with subtle elevation
- **Dark Content Card**: Prominent content blocks, often for feature showcases

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
