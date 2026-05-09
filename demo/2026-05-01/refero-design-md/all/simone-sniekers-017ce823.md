# Simone Sniekers - Refero Design MD

- Source: https://styles.refero.design/style/017ce823-c338-417d-849d-497c97701c4c
- Original site: https://www.simonesniekers.com
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting theatrical backdrop.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ember Gradient | `#f9532d` | brand | Action accent / signal color |
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Winter Mist | `#bcbcbc` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Accelerator Yellow | `#eae800` | accent | Action accent / signal color |
| Cloud Gray | `#cccbbb` | neutral | Border, muted text, or supporting surface |
| Desert Rose | `#926560` | accent | Action accent / signal color |
| Harvest Gold | `#d0a43e` | accent | Action accent / signal color |
| Fiery Crimson | `#e01365` | accent | Action accent / signal color |
| Ginger Bread | `#b18759` | accent | Action accent / signal color |

```css
:root {
  --ref-ember-gradient: #f9532d;
  --ref-black-ink: #000000;
  --ref-winter-mist: #bcbcbc;
  --ref-pure-white: #ffffff;
  --ref-accelerator-yellow: #eae800;
  --ref-cloud-gray: #cccbbb;
  --ref-desert-rose: #926560;
  --ref-harvest-gold: #d0a43e;
}
```

## Typography direction
- **Neue Haas Grotesk**: 400, 16px, 1.00, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `16px`
- Radius: `none: 0px`

## Component cues
- **Ghost Navigation Button**: Tertiary navigation element, typically found in footers or global info sections.
- **Image Card**: Primary content display for portfolio pieces.
- **Header Title**: Main brand identification and page title.
- **Information Link**: General links for contact and external profiles.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
