# Aesop - Refero Design MD

- Source: https://styles.refero.design/style/24c0de95-295d-42aa-8240-4e36683cf35b
- Original site: https://aesop.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
NGLORA - Apothecary's Formulary. A meticulously organized space where typography and product photography are treated with scientific precision.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#fffef2` | neutral | Page background or card surface |
| Charcoal | `#333333` | neutral | Primary text or dark surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Carbon | `#252525` | neutral | Primary text or dark surface |
| Stone | `#666666` | neutral | Border, muted text, or supporting surface |
| Slate | `#d6d5cc` | neutral | Border, muted text, or supporting surface |
| Alabaster | `#ffffff` | neutral | Page background or card surface |
| Umber | `#945c26` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment: #fffef2;
  --ref-charcoal: #333333;
  --ref-ink-black: #000000;
  --ref-carbon: #252525;
  --ref-stone: #666666;
  --ref-slate: #d6d5cc;
  --ref-alabaster: #ffffff;
  --ref-umber: #945c26;
}
```

## Typography direction
- **SuisseIntl**: 400, 700, 11px, 12px, 14px, 16px, 18px, 30px, 1.20-2.86; substitute `Inter, Helvetica Neue`.
- **Zapf-Humanist**: 400, 31px, 1.33; substitute `Optima, Palatino`.

## Spacing / shape
- Section Gap: `96-128px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1600px`
- Radius: `tags: 0px, cards: 0px, inputs: 0px, buttons: 0px`

## Component cues
- **Product Card — Animal**: Reference component style.
- **Product Carousel Section — New and Notable**: Reference component style.
- **Hero CTA Banner**: Reference component style.
- **Dark Action Button**: Primary call-to-action, such as 'Add to Cart'.
- **Outline Navigation Button**: Secondary header actions like 'Email sign up' or 'Search'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
