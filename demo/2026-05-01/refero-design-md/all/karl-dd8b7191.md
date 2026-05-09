# Karl - Refero Design MD

- Source: https://styles.refero.design/style/dd8b7191-a992-4dab-88f8-f67e8819b461
- Original site: https://karlgonsalves.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
joyful circus tent, bright and in motion

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sunshine Yellow | `#ffff00` | brand | Action accent / signal color |
| Ocean Blue | `#007fff` | brand | Action accent / signal color |
| Midnight Graphite | `#333333` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-sunshine-yellow: #ffff00;
  --ref-ocean-blue: #007fff;
  --ref-midnight-graphite: #333333;
  --ref-polar-white: #ffffff;
}
```

## Typography direction
- **Changa One**: 400, 12px, 20px, 32px, 50px, 75px, 0.72, 0.80, 1.00, 1.25, 1.67; substitute `Bebas Neue`.
- **Arial**: 400, 14px, 1.43; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `circular: 1440px`

## Component cues
- **Navigation Link**: Primary navigation item
- **Curved Background Card**: Decorative background element
- **Main Headline**: Primary page title or major section heading.
- **Supporting Text Block**: Introductory or explanatory text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
