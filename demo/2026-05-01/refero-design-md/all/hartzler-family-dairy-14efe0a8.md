# Hartzler Family Dairy - Refero Design MD

- Source: https://styles.refero.design/style/14efe0a8-5abf-441c-919d-add271317bf9
- Original site: https://www.hartzlerdairy.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Farm-Fresh Bold Text

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Shadow Graphite | `#333333` | neutral | Primary text or dark surface |
| Pasture Green | `#035542` | brand | Action accent / signal color |
| Sky Blue | `#2b7bb9` | accent | Action accent / signal color |
| Dairy Teal | `#56dddb` | accent | Action accent / signal color |
| Buttercream Yellow | `#f9e9a9` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-shadow-graphite: #333333;
  --ref-pasture-green: #035542;
  --ref-sky-blue: #2b7bb9;
  --ref-dairy-teal: #56dddb;
  --ref-buttercream-yellow: #f9e9a9;
}
```

## Typography direction
- **Work Sans**: 400, 500, 900, 14px, 17px, 18px, 40px, 290px, 333px, 0.70, 1.00, 1.06, 1.45; substitute `system-ui`.
- **Font Awesome 5 Brands**: 400, 40px, 1.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `12px`
- Element Gap: `20px`
- Radius: `buttons-pill: 100px, content-boxes: 4px, buttons-rounded: 20px`

## Surface cues
- **Canvas Background** `#ffffff`: Dominant page background, providing a clean, uncluttered base.

## Component cues
- **Primary Ghost Button**: Interactive element
- **Rounded Filled Button**: Interactive element
- **Minimal Link Button**: Interactive element
- **Product Highlight Badge**: Informational tag
- **Featured Label**: Decorative brand element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
