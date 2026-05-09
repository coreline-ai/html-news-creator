# SaveDay - Refero Design MD

- Source: https://styles.refero.design/style/21da2822-cfe3-4a6a-b333-1be48e855e36
- Original site: https://www.save.day
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial Scanner Clarity

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Black | `#0d0d0d` | neutral | Primary text or dark surface |
| Deepest Ink | `#000000` | neutral | Primary text or dark surface |
| Cool Mist | `#edeef0` | neutral | Page background or card surface |
| Pinstripe Gray | `#e5e4e3` | neutral | Page background or card surface |
| Ash Cloud | `#999999` | neutral | Border, muted text, or supporting surface |
| Cloud Shadow | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Scanner Yellow | `#fbda5f` | brand | Action accent / signal color |
| System Blue | `#006aff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-black: #0d0d0d;
  --ref-deepest-ink: #000000;
  --ref-cool-mist: #edeef0;
  --ref-pinstripe-gray: #e5e4e3;
  --ref-ash-cloud: #999999;
  --ref-cloud-shadow: #cccccc;
  --ref-graphite: #333333;
}
```

## Typography direction
- **Phudu**: 400, 700, 24px, 32px, 56px, 64px, 112px, 0.90, 1.00; substitute `Bebas Neue`.
- **Interdisplay**: 400, 500, 600, 700, 16px, 18px, 20px, 24px, 0.90, 1.00, 1.20, 1.30, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `pill: 1600px, tags: 30px, cards: 16px, input: 12px, buttons: 160px`

## Component cues
- **Primary Navigation Link**: Top navigation item
- **Outline Action Button - Chrome**: Primary call to action in header
- **Filled Action Button - Try Now**: Secondary call to action in header
- **Chrome Web Store Button**: Inline call to action for extension installation
- **Text Section Card - Gray**: Background for descriptive text sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
