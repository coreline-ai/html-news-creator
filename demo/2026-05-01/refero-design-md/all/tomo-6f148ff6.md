# TOMO - Refero Design MD

- Source: https://styles.refero.design/style/6f148ff6-ae72-496a-a21d-84d7779825ff
- Original site: https://tomoseattle.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deconstructed Collage Zine

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Found Paper | `#eee2d4` | neutral | Page background or card surface |
| Button Gray | `#efefef` | neutral | Page background or card surface |
| Warning Red | `#ff6347` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-found-paper: #eee2d4;
  --ref-button-gray: #efefef;
  --ref-warning-red: #ff6347;
}
```

## Typography direction
- **Recife**: 300, 400, 26px, 32px, 1.00, 1.30; substitute `Playfair Display`.
- **Times**: 400, 13px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `0px`
- Element Gap: `13px`
- Radius: `none: 0px`

## Component cues
- **Standard Button**: Default interactive button style.
- **Transparent Card**: Container for content, often layered directly on the background.
- **Subtle Transparent Card**: Used for slightly more pronounced content blocks that still maintain a lightweight feel.
- **Navigation Link Strip**: Interactive text links for navigation or content categories.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
