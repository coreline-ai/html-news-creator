# Repeat - Refero Design MD

- Source: https://styles.refero.design/style/53538d2d-d5a1-4719-9c7a-d7ab1f3a8c8a
- Original site: https://www.getrepeat.io
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast lime punch

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#171717` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Parchment | `#ede7e2` | neutral | Page background or card surface |
| Deep Charcoal | `#37352f` | neutral | Primary text or dark surface |
| Sour Lime | `#f5ff7d` | brand | Action accent / signal color |
| Serene Sky | `#c3d5fc` | accent | Action accent / signal color |
| Soft Lilac | `#e2d8ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #171717;
  --ref-canvas-white: #ffffff;
  --ref-warm-parchment: #ede7e2;
  --ref-deep-charcoal: #37352f;
  --ref-sour-lime: #f5ff7d;
  --ref-serene-sky: #c3d5fc;
  --ref-soft-lilac: #e2d8ff;
}
```

## Typography direction
- **Montserrat**: 400, 500, 600, 13px, 15px, 17px, 34px, 0.75, 1.20, 1.29, 1.50, 1.60, 2.00; substitute `system-ui`.
- **Poppins**: 400, 500, 600, 17px, 20px, 24px, 29px, 37px, 1.00, 1.20, 1.30; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `15px`
- Element Gap: `4px`
- Radius: `tags: 3px, cards: 25px, images: 20px, buttons: 50px, navItems: 8px, heroButton: 100px`

## Surface cues
- **Warm Parchment** `#ede7e2`: Base page background, neutral canvas for varying content sections.
- **Canvas White** `#ffffff`: Default card backgrounds, elevated content areas, and core UI elements.
- **Sour Lime** `#f5ff7d`: Primary hero and accent sections, drawing attention and signalling energy.
- **Serene Sky** `#c3d5fc`: Alternating section background, offering subtle visual breaks without high contrast.
- **Soft Lilac** `#e2d8ff`: Alternating section background, offering subtle visual breaks without high contrast.

## Component cues
- **Primary Action CTA (Text Button)**: Call to action for hero sections and primary navigation. Text color indicates action, but background is transparent.
- **Navigation Button (Filled)**: Prominent call to action in the main navigation. Uses the brand's 'Sour Lime' to stand out.
- **Ghost Icon Button**: Interactive elements with minimal visual weight, like branded company logos.
- **Information Card (Large Radius)**: Displaying testimonials or featured brands, with a soft, approachable aesthetic.
- **Link Button (Underlined)**: Secondary action or internal navigation, subtle and integrated into text content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
