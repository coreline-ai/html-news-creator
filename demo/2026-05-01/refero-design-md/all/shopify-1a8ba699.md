# Shopify - Refero Design MD

- Source: https://styles.refero.design/style/1a8ba699-24cb-4b35-8db1-c595c578199c
- Original site: https://shopify.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Forest Canvas — a digital workspace layered in rich, dark greens and grays, where vivid accents illuminate interactive elements.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Midnight | `#02090a` | neutral | Primary text or dark surface |
| Forest Black | `#000000` | neutral | Primary text or dark surface |
| Lunar White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Slate | `#041e18` | neutral | Primary text or dark surface |
| Border Ash | `#e5e7eb` | neutral | Page background or card surface |
| Steel Gray | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Off Black | `#1e2c31` | neutral | Primary text or dark surface |
| Subtle Violet | `#010624` | neutral | Action accent / signal color |
| Deep Teal | `#072720` | neutral | Primary text or dark surface |
| Text Grey | `#99b3ad` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-midnight: #02090a;
  --ref-forest-black: #000000;
  --ref-lunar-white: #ffffff;
  --ref-charcoal-slate: #041e18;
  --ref-border-ash: #e5e7eb;
  --ref-steel-gray: #a1a1aa;
  --ref-off-black: #1e2c31;
  --ref-subtle-violet: #010624;
}
```

## Typography direction
- **NeueHaasGrotesk**: 330, 400, 500, 550, 600, 14px, 16px, 18px, 20px, 24px, 28px, 48px, 55px, 70px, 96px, 0.83, 0.96, 1.00, 1.14, 1.16, 1.25, 1.28, 1.40, 1.49, 1.50; substitute `Helvetica Neue, Arial`.
- **Inter-Variable**: 400, 420, 450, 550, 12px, 14px, 16px, 18px, 20px, 1.00, 1.20, 1.29, 1.43, 1.50, 1.56; substitute `Inter, Roboto`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `pill: 340px, cards: 12px, large: 20px, medium: 8px, buttons: 9999px, default: 4px`

## Surface cues
- **Canvas Midnight** `#02090a`: Base page background
- **Charcoal Slate** `#041e18`: Primary content cards and section backgrounds
- **Deep Teal** `#072720`: Navigation bar and specific elevated UI elements

## Component cues
- **Primary CTA Button**: Call to action
- **Secondary Outlined Button**: Secondary action
- **Ghost Button**: Minimal interaction
- **Card Surface**: Content container
- **Nav Card**: Informational link container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
