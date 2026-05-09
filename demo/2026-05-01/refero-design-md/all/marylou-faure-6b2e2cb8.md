# Marylou Faure - Refero Design MD

- Source: https://styles.refero.design/style/6b2e2cb8-b217-4395-a664-8795b6002315
- Original site: https://maryloufaure.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant canvas, graphic stories

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Illustrative Red | `#ff0000` | brand | Action accent / signal color |
| Playful Pink | `#ffbbff` | brand | Action accent / signal color |
| Sky Blue | `#72c2f2` | brand | Action accent / signal color |
| Blush Pink | `#f7b2de` | brand | Action accent / signal color |
| Vivid Pink | `#ffa3fe` | brand | Action accent / signal color |
| Lime Green | `#32c24d` | brand | Action accent / signal color |
| Cyan Blue | `#96d6ff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-gray: #737373;
  --ref-illustrative-red: #ff0000;
  --ref-playful-pink: #ffbbff;
  --ref-sky-blue: #72c2f2;
  --ref-blush-pink: #f7b2de;
  --ref-vivid-pink: #ffa3fe;
}
```

## Typography direction
- **Helvetica Now**: 400, 600, 12px, 16px, 20px, 22px, 40px, 0.80, 1.00, 1.20, 1.25, 1.35, 1.38, 1.50; substitute `Arial`.
- **GTStandard-M**: 400, 12px, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `33px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for UI elements.
- **Subtle Gray** `#f5f5f5`: Slightly off-white primary tint, used for subtle visual breaks or backgrounds.
- **Muted Blue** `#e7f2f7`: Secondary tint for distinct sections or background accents.

## Component cues
- **Primary Action Button**: Interactive element for key calls to action.
- **Ghost Circular Icon Button**: Minimal interactive element, typically for navigation or utility icons.
- **Client Logo Grid Item**: Display individual client logos.
- **Project Thumbnail Card**: Visually rich preview for portfolio projects.
- **Top Navigation Link**: Primary navigation items in the header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
