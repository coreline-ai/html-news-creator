# Air - Refero Design MD

- Source: https://styles.refero.design/style/d3289fe7-a85e-42d8-96b7-eb7faa62a104
- Original site: https://air.inc
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Expansive sky, clean canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#1b1b1b` | neutral | Primary text or dark surface |
| Vapor Gray | `#f5f5f5` | neutral | Page background or card surface |
| Charcoal Void | `#000000` | neutral | Primary text or dark surface |
| Sky Blue | `#426188` | brand | Action accent / signal color |
| Vivid Azure | `#2b7fff` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-canvas: #ffffff;
  --ref-midnight-ink: #1b1b1b;
  --ref-vapor-gray: #f5f5f5;
  --ref-charcoal-void: #000000;
  --ref-sky-blue: #426188;
  --ref-vivid-azure: #2b7fff;
}
```

## Typography direction
- **Control**: 500, 12px, 13px, 14px, 16px, 20px, 1.10, 1.40, 1.50; substitute `Inter`.
- **Control Compressed**: 900, 259px, 0.85; substitute `Oswald`.
- **Control Cursive**: 400, 500, 20px, 32px, 56px, 1.00, 1.10, 1.50; substitute `Dancing Script`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 14px, images: 11px, inputs: 4px, buttons: 8px`

## Surface cues
- **Page Base** `#fff8dc`: The foundational, immersive background color that gives the landing page its atmospheric feel. Note: This color is not part of the UI component…
- **Haze Surface** `#f5f5f5`: Subtle backgrounds for input fields and secondary card surfaces, providing a gentle lift from the page base.
- **Cloud Canvas** `#ffffff`: Primary surface for cards, modals, and other prominent UI elements, providing a clean, bright canvas against text.

## Component cues
- **Ghost Navigation Button**: Primary navigation and subtle calls to action.
- **Outlined Action Button**: Primary calls to action for interactive elements.
- **Basic Card**: Content grouping for informational blocks with minimal visual adornment.
- **Elevated Content Card**: Card for featuring key content sections.
- **Hero Image Card**: Large, immersive card for images or visual content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
