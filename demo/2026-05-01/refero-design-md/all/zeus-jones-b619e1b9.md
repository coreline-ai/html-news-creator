# Zeus Jones - Refero Design MD

- Source: https://styles.refero.design/style/b619e1b9-86ee-4a10-b6e6-47b10927c3a2
- Original site: https://zeusjones.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ethereal canvas with typographic gravitas. A sun-drenched, off-white digital gallery where bold typography and artful backgrounds coalesce.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#fcfaf3` | neutral | Page background or card surface |
| Greyscale Architect | `#1a1c2c` | neutral | Primary text or dark surface |
| Card Dove | `#ebe9e4` | neutral | Page background or card surface |
| Night Icon | `#000000` | neutral | Primary text or dark surface |
| Hero Gradient | `#9c8ec4` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #fcfaf3;
  --ref-greyscale-architect: #1a1c2c;
  --ref-card-dove: #ebe9e4;
  --ref-night-icon: #000000;
  --ref-hero-gradient: #9c8ec4;
}
```

## Typography direction
- **ZJSansDisplay**: 400, 500, 12px, 16px, 18px, 24px, 40px, 48px, 60px, 90px, 1.00, 1.07, 1.11, 1.20, 1.25, 1.30, 1.50, 1.60; substitute `Inter`.
- **FeatureDeckLight**: 100, 60px, 90px, 1.07, 1.11; substitute `Lora Light`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `16px`
- Radius: `all: 20px, cards: 20px, buttons: 1584px, headings: 1000px`

## Surface cues
- **Canvas Parchment** `#fcfaf3`: Primary page background layer
- **Card Dove** `#ebe9e4`: Secondary background layer for cards and contained content
- **Greyscale Architect** `#1a1c2c`: Deepest surface layer, used for interactive elements like filled buttons or navigation panels that appear on top of other surfaces

## Component cues
- **Ghost Navigation Link**: Navigation item and basic textual link.
- **Pill Button**: Primary call to action.
- **Work Showcase Card**: Displaying work examples.
- **Underlined Input Field**: Standard text input.
- **Header Navigation**: Top-level site navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
