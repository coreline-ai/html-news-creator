# Mobbin - Refero Design MD

- Source: https://styles.refero.design/style/ef44a995-6745-4dc7-86ab-f7227f108f81
- Original site: https://mobbin.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Grayscale specimen board — a printer's proof sheet where typographic weight IS color.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#141414` | neutral | Primary text or dark surface |
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#707070` | neutral | Border, muted text, or supporting surface |
| Ash | `#adadad` | neutral | Border, muted text, or supporting surface |
| Fog | `#ededed` | neutral | Page background or card surface |
| Mist | `#f2f2f2` | neutral | Page background or card surface |
| Silver | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Slate Shadow | `#e0e0e0` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #141414;
  --ref-pure-canvas: #ffffff;
  --ref-graphite: #707070;
  --ref-ash: #adadad;
  --ref-fog: #ededed;
  --ref-mist: #f2f2f2;
  --ref-silver: #c2c2c2;
  --ref-slate-shadow: #e0e0e0;
}
```

## Typography direction
- **saans**: 400, 440, 456, 600, 652, 12px, 14px, 16px, 20px, 32px, 56px, 80px, 1.00–1.50 (tight 1.00–1.15 at display, looser 1.38–1.50 at body); substitute `Inter Variable or Geist (closest variable-axis fallbacks with comparable optical geometry)`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16-24px`
- Element Gap: `8-16px`
- Page Max Width: `1280px`
- Radius: `tags: 9999px, cards: 16-24px, inputs: 9999px, modals: 24px, buttons: 9999px, thumbnails: 16px`

## Surface cues
- **Page** `#ffffff`: Root page background
- **Card** `#ffffff`: Gallery cards, testimonial cards — differentiated from page by 1px #ededed border, not background change
- **Input / Chip** `#f2f2f2`: Search bars, nav tint, inner UI fills
- **Overlay Dropdown** `#ffffff`: Category mega-menu, floating panels — elevated via rgba(0,0,0,0.04) 0px 8px 40px shadow

## Component cues
- **Button Group — Primary, Outlined & Muted**: Reference component style.
- **Search Input with Filter Pills**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Filled Button**: Main CTA — 'Join for free'
- **Outlined Pill Button**: Secondary action — 'See our plans'

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
