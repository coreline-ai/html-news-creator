# Transform - Refero Design MD

- Source: https://styles.refero.design/style/91939ad3-9e22-4256-a396-a1716a064ac4
- Original site: https://transformfestival.org
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric theater spotlight

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Plum | `#340068` | brand | Action accent / signal color |
| Neon Magenta | `#fb00c2` | brand | Action accent / signal color |
| Live Event Red | `#ff1e00` | brand | Action accent / signal color |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Paper Beige | `#f4ede9` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Concrete Gray | `#d9d9d9` | neutral | Page background or card surface |
| Input Border Gray | `#767676` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-plum: #340068;
  --ref-neon-magenta: #fb00c2;
  --ref-live-event-red: #ff1e00;
  --ref-coal-black: #000000;
  --ref-paper-beige: #f4ede9;
  --ref-canvas-white: #ffffff;
  --ref-concrete-gray: #d9d9d9;
  --ref-input-border-gray: #767676;
}
```

## Typography direction
- **Walsheim**: 400, 700, 800, 900, 16px, 18px, 22px, 24px, 40px, 56px, 80px, 1.00, 1.10, 1.20, 1.38, 1.45; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48-56px`
- Card Padding: `16px`
- Element Gap: `8-16px`
- Radius: `circular: 50px`

## Component cues
- **Primary Action Button**: Fills and calls to action prominently
- **Subtle Circular Button**: Decorative page navigation, subtle actions
- **Footer Action Button**: Call to action within dark footer sections
- **Monochromatic Feature Card**: Displays related content, news, or blog posts
- **Subtle Feature Card**: Displays related content using a lighter background

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
