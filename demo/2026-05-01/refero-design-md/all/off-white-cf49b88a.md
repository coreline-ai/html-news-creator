# OFF WHITE - Refero Design MD

- Source: https://styles.refero.design/style/cf49b88a-fb38-4520-8fbb-ab3efa983517
- Original site: https://off-white.valeriafrancis.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Glitch Arcade — stark black canvas with pixelated neon blocks.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghost Canvas | `#ffffff` | neutral | Page background or card surface |
| Muted Grey | `#aba4a4` | neutral | Border, muted text, or supporting surface |
| Glitch Green | `#00fb34` | brand | Action accent / signal color |
| Warning Red | `#ff0000` | brand | Action accent / signal color |
| Digital Yellow | `#fff500` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghost-canvas: #ffffff;
  --ref-muted-grey: #aba4a4;
  --ref-glitch-green: #00fb34;
  --ref-warning-red: #ff0000;
  --ref-digital-yellow: #fff500;
}
```

## Typography direction
- **Offwhite**: 400, 600, 700, 11px, 18px, 20px, 36px, 38px, 42px, 48px, 56px, 72px, 96px, 180px, 500px, 1.00, 1.10, 1.15, 1.19, 1.25, 1.30, 1.31, 1.35, 1.40, 1.45, 1.54, 1.55, 1.56; substitute `Arial Bold`.
- **Times**: 400, 16px, 1.20; substitute `Times New Roman`.
- **Arial**: 400, 13px, 1.20; substitute `Helvetica`.

## Spacing / shape
- Section Gap: `60-120px`
- Card Padding: `0px`
- Element Gap: `40px`
- Radius: `links: 30px, buttons: 30px`

## Component cues
- **Ghost Brand Button**: Interactive element
- **Filled Brand Button**: Primary action
- **Rounded Link**: Navigation or secondary interaction
- **Hero Headline Text Block**: Primary page title
- **Image Collage Block**: Content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
