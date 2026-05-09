# Leonid Kostetskyi - Refero Design MD

- Source: https://styles.refero.design/style/5a7ba5ff-0476-4f3f-99f9-0b920534dde5
- Original site: https://leonidkostetskyi.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-driven architectural minimalism: a stark, high-contrast typographic landscape on a warm, textured canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#fdfaf3` | neutral | Page background or card surface |
| Cocoa Ink | `#472425` | brand | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Absolute Black | `#000000` | neutral | Primary text or dark surface |
| Deep Charcoal | `#121212` | neutral | Primary text or dark surface |
| Alert Crimson | `#e73737` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #fdfaf3;
  --ref-cocoa-ink: #472425;
  --ref-pure-white: #ffffff;
  --ref-absolute-black: #000000;
  --ref-deep-charcoal: #121212;
  --ref-alert-crimson: #e73737;
}
```

## Typography direction
- **SFUIDisplay**: 300, 400, 8px, 9px, 11px, 12px, 15px, 18px, 19px, 20px, 21px, 1.00, 1.10, 1.33, 1.40, 1.60; substitute `system-ui`.
- **NeueHaasDisplay**: 400, 11px, 12px, 15px, 27px, 135px, 143px, 165px, 188px, 0.86, 1.00; substitute `system-ui`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `200px`
- Card Padding: `12px`
- Element Gap: `16px`
- Radius: `none: 0px, extraLarge: 9999px`

## Component cues
- **Text Only Button (Cocoa Ink)**: Interactive navigation and thematic switches.
- **Circular Toggle Button (Dark)**: Theme switcher.
- **Circular Toggle Button (Light)**: Theme switcher.
- **Outlined Input Field (Dark Text)**: User input fields.
- **Outlined Input Field (Cocoa Ink)**: User input fields.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
