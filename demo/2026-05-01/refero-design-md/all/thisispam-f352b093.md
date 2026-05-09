# Thisispam - Refero Design MD

- Source: https://styles.refero.design/style/f352b093-1ba7-49c7-9ce3-ad73cf9a1aee
- Original site: https://thisispam.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic Blueprint on Muted Yellow Canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Yellow | `#fff3b8` | brand | Action accent / signal color |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Input Pale Yellow | `#f1e4a4` | semantic | Action accent / signal color |
| Accent Red | `#ff0000` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-yellow: #fff3b8;
  --ref-midnight-black: #000000;
  --ref-paper-white: #ffffff;
  --ref-input-pale-yellow: #f1e4a4;
  --ref-accent-red: #ff0000;
}
```

## Typography direction
- **OT Neue Montreal**: 500, 700, 11px, 16px, 32px, 58px, 0.90, 1.00, 1.20, 1.43, 2.55; substitute `Montserrat`.
- **ABC Diatype**: 400, 700, 13px, 14px, 1.20, 1.43, 2.15; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `none: 0px, small: 2px`

## Component cues
- **Ghost Navigation Button**: Primary site navigation and contextual actions where visual weight should be minimal.
- **Primary Canvas Button**: Secondary action buttons, often appearing on the Canvas Yellow background.
- **Inverse Ghost Button**: Buttons on dark backgrounds requiring a reversed text and outline color.
- **Input Field**: Interactive text input fields.
- **Feature Card**: Displaying project previews or feature blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
