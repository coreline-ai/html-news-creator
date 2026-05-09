# Koox - Refero Design MD

- Source: https://styles.refero.design/style/d1ca41ff-1bcc-4081-b1fd-bdcf380ba749
- Original site: https://koox.co.uk
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
kitchen laboratory blueprint

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Noir | `#000000` | neutral | Primary text or dark surface |
| Tile White | `#ffffff` | neutral | Page background or card surface |
| Laboratory Gray | `#efefef` | neutral | Page background or card surface |
| Deep Forest | `#113722` | brand | Action accent / signal color |
| Spiced Orange | `#d25a24` | accent | Action accent / signal color |
| Berry Rouge | `#6b1229` | accent | Action accent / signal color |
| Charcoal Text | `#232323` | neutral | Primary text or dark surface |
| Border Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Input Border | `#d7d7d7` | neutral | Border, muted text, or supporting surface |
| Placeholder Gray | `#646464` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-noir: #000000;
  --ref-tile-white: #ffffff;
  --ref-laboratory-gray: #efefef;
  --ref-deep-forest: #113722;
  --ref-spiced-orange: #d25a24;
  --ref-berry-rouge: #6b1229;
  --ref-charcoal-text: #232323;
  --ref-border-gray: #cccccc;
}
```

## Typography direction
- **Helvetica**: 400, 500, 600, 700, 900, 14px, 16px, 18px, 20px, 24px, 26px, 30px, 32px, 40px, 46px, 48px, 0.70, 0.80, 0.88, 1.00, 1.03, 1.10, 1.20, 1.30, 1.38, 1.44, 1.50, 1.57, 1.63, 1.71, 1.75, 1.79, 2.19, 2.50; substitute `Arial`.

## Spacing / shape
- Section Gap: `27px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1800px`
- Radius: `cards: 5px, links: 5px, lists: 5px, inputs: 0px, buttons: 0px`

## Component cues
- **Primary Action Button**: Main call-to-action button, directing users to core functions.
- **Secondary Action Button**: Alternative call-to-action, visually distinct but still impactful.
- **Text Link Button**: Minimal interactive element, appearing as simple text.
- **Product Card**: Container for product listings or category previews.
- **Input Field**: Standard form input element.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
