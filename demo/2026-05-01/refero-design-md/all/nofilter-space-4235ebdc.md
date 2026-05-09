# Nofilter.space - Refero Design MD

- Source: https://styles.refero.design/style/4235ebdc-a070-46ef-abbf-692151449bea
- Original site: https://www.nofilter.space
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural grid on newsprint.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Headline Black | `#000000` | neutral | Primary text or dark surface |
| Ink Gray | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-headline-black: #000000;
  --ref-ink-gray: #333333;
}
```

## Typography direction
- **Pragmatica**: 400, 12px, 15px, 24px, 30px, 35px, 1.14, 1.17, 1.25, 1.47, 2.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `none: 0px`

## Component cues
- **Navigation Link**: Primary site navigation items.
- **Basic Content Card**: Container for articles and visual content.
- **Editorial Header**: Headline for articles and sections.
- **Meta Info Text**: Author and date information.
- **Image Card**: Display of visual content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
