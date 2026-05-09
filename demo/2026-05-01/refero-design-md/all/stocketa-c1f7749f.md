# Stocketa - Refero Design MD

- Source: https://styles.refero.design/style/c1f7749f-319b-491b-8243-22050e85994f
- Original site: https://stocketa.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft-edged transparency on cloud-white

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#e0dde2` | neutral | Page background or card surface |
| Ash | `#f0f0f0` | neutral | Page background or card surface |
| Graphite | `#000000` | neutral | Primary text or dark surface |
| Stone Gray | `#abbdcf` | neutral | Border, muted text, or supporting surface |
| Slate | `#9aa1b2` | neutral | Border, muted text, or supporting surface |
| Cloud Mist | `#a5afcb` | neutral | Border, muted text, or supporting surface |
| Blue Violet | `#5b638c` | accent | Action accent / signal color |
| Luminescent Violet | `#995bb9` | brand | Action accent / signal color |
| Midnight Indigo Outline | `#3a4766` | accent | Action accent / signal color |
| Highlight Gradient | `#60eb8c` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #e0dde2;
  --ref-ash: #f0f0f0;
  --ref-graphite: #000000;
  --ref-stone-gray: #abbdcf;
  --ref-slate: #9aa1b2;
  --ref-cloud-mist: #a5afcb;
  --ref-blue-violet: #5b638c;
  --ref-luminescent-violet: #995bb9;
}
```

## Typography direction
- **averta standard**: 400, 500, 600, 700, 800, 14px, 15px, 16px, 17px, 19px, 27px, 28px, 50px, 53px, 62px, 98px, 1.00, 1.10, 1.15, 1.20, 1.25, 1.35, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `14px`
- Element Gap: `16px`
- Radius: `pill: 100px, cards: 18px, buttons: 100px, default: 22px`

## Surface cues
- **Canvas** `#e0dde2`: Primary background for the entire application, serving as the base layer.
- **Ash Surface** `#f0f0f0`: A slightly elevated background color for larger UI elements or sections, providing subtle differentiation.
- **Soft Card** `#537498`: Interactive cards or information panels that float above the base, distinguished by a subtle shadow and rounded corners.

## Component cues
- **Ghost Action Button**: Secondary call to action or navigation link.
- **Soft Card**: Container for content, elevated slightly from the background.
- **Feature List Item**: Padded container for individual features or information blocks.
- **Content Card (No Shadow)**: Simple, flat content area on the page background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
