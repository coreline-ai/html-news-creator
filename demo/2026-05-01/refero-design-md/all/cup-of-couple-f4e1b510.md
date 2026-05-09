# Cup of Couple - Refero Design MD

- Source: https://styles.refero.design/style/f4e1b510-6085-4fb8-8597-05d479d3c00c
- Original site: https://www.cupofcouple.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Editorial Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#303030` | neutral | Primary text or dark surface |
| Ash Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#f0f0f0` | neutral | Page background or card surface |
| Subtle Gray | `#767676` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink: #303030;
  --ref-ash-gray: #808080;
  --ref-canvas-white: #f0f0f0;
  --ref-subtle-gray: #767676;
}
```

## Typography direction
- **ITCFranklinGothicStdBook**: 400, 10px, 16px, 1.00, 1.05, 1.20; substitute `Franklin Gothic Book`.
- **Garamond**: 400, 17px, 28px, 1.00, 1.20; substitute `Garamond`.
- **PerpetuaTitlingMT**: 400, 25px, 32px, 40px, 48px, 1.20; substitute `Perpetua Titling MT`.

## Spacing / shape
- Section Gap: `36px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 0px, inputs: 0px, buttons: 0px`

## Surface cues
- **Canvas White** `#f0f0f0`: Primary page background and default surface for content.

## Component cues
- **Ghost Navigation Button**: Navigation and interactive links with a subtle underline effect on hover/active.
- **Content Grid Card**: Container for visual diary and project entries.
- **Minimal Search Input**: Search field with a discreet bottom border.
- **Featured Project Header**: Header for prominent content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
