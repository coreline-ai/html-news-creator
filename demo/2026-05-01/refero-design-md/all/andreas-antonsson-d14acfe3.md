# Andreas Antonsson - Refero Design MD

- Source: https://styles.refero.design/style/d14acfe3-20ea-4c18-be22-aba396b4fa80
- Original site: https://andreasantonsson.dev
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shadow Gallery, Spotlit Art. The website feels like stepping into a dark art gallery with carefully curated, dramatically lit pieces.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-void-black: #000000;
  --ref-ghost-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 700, 11px, 13px, 22px, 1.50; substitute `system-ui, sans-serif`.
- **Dahlia**: 400, 144px, 1.00; substitute `serif`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `22px`
- Radius: `nav-items: 2px, interactive-tags: 9999px`

## Component cues
- **Project Card**: Reference component style.
- **Available for Work Badge**: Reference component style.
- **Scroll Index Navigator**: Reference component style.
- **Navigation Link**: Primary navigation elements in the header and footer.
- **Headline Project Title**: Prominent, artistic titles for each project section.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
