# Charlie - Refero Design MD

- Source: https://styles.refero.design/style/34aa811f-6084-484c-b4c0-f587b514e970
- Original site: https://charlielemaignan.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast editorial experimentalism

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Concrete Gray | `#838383` | neutral | Border, muted text, or supporting surface |
| Alert Red | `#ff0000` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-concrete-gray: #838383;
  --ref-alert-red: #ff0000;
}
```

## Typography direction
- **NeueHaas**: 400, 700, 19px, 20px, 40px, 1.08, 1.25, 1.32; substitute `Helvetica Neue`.
- **Brasparz Variable**: 400, 145px, 360px, 0.70; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `59px`
- Card Padding: `20px`
- Element Gap: `30px`
- Page Max Width: `1306px`
- Radius: `buttons: 100px`

## Component cues
- **Ghost Navigation Button**: Ghost button for primary navigation
- **Filled Navigation Button**: Filled button for active navigation states
- **Footer Link**: Secondary interactive elements in the footer
- **Hero Banner - Red**: Full-width background section for dramatic visual impact

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
