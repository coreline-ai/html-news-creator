# Face Formula - Refero Design MD

- Source: https://styles.refero.design/style/78ac71e1-cd4c-4b4d-bac5-e7e6c65cd3fa
- Original site: https://faceformula.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
serene Scandinavian minimalist

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Fog | `#f2f5f8` | neutral | Page background or card surface |
| Border Mist | `#e6ebee` | neutral | Page background or card surface |
| Deep Ocean | `#3b505a` | brand | Action accent / signal color |
| Text Slate | `#202f3b` | neutral | Primary text or dark surface |
| Link Blue | `#58737e` | neutral | Action accent / signal color |
| Light Steel | `#cfdce7` | neutral | Page background or card surface |
| Black Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-fog: #f2f5f8;
  --ref-border-mist: #e6ebee;
  --ref-deep-ocean: #3b505a;
  --ref-text-slate: #202f3b;
  --ref-link-blue: #58737e;
  --ref-light-steel: #cfdce7;
  --ref-black-ink: #000000;
}
```

## Typography direction
- **Libre Caslon Condensed**: 400, 32px, 52px, 120px, 1.00, 1.10, 1.20; substitute `Playfair Display`.
- **Circular Pro**: 400, 12px, 13px, 15px, 16px, 1.00, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `0px`
- Element Gap: `16px`
- Radius: `none: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default content areas.
- **Ghost Fog** `#f2f5f8`: Subtle background for distinct content sections or cards.
- **Border Mist** `#e6ebee`: Slightly darker secondary background panels, offering visual distinction.

## Component cues
- **Ghost Navigation Button (Light)**: Header navigation links, inline text links.
- **Ghost Navigation Button (Dark)**: Contextual navigation links against dark hero backgrounds.
- **Contained Button**: Secondary action button for interactive elements.
- **Product Input Field**: Text input areas with a subtle border for user interaction.
- **Bestseller Label**: Small, contained label for product features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
