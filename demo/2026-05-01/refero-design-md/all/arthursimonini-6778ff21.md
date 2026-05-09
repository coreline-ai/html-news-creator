# Arthursimonini - Refero Design MD

- Source: https://styles.refero.design/style/6778ff21-44eb-40f3-ba85-2ee7de935f8f
- Original site: https://arthursimonini.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dramatic typographic stage

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ghost-white: #ffffff;
}
```

## Typography direction
- **LifeLTStd-Roman**: 400, 18px, 1.00, 1.20; substitute `serif`.
- **RomieLigatures-Regular**: 400, 18px, 65px, 167px, 0.73, 0.90, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `cards: 0px, media: 0px, inputs: 0px, buttons: 0px`

## Component cues
- **Navigation Link**: Primary site navigation
- **Tracklist Item**: Displays music tracks with duration
- **Media Grid Card**: Displays album or movie covers in a grid layout
- **Hero Headline**: Dominant page title

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
