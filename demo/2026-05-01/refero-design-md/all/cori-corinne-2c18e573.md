# Cori Corinne - Refero Design MD

- Source: https://styles.refero.design/style/2c18e573-0ffb-4f0d-848c-ff72a5839fd3
- Original site: https://www.coricorinne.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial grand typography

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f6f5f0` | neutral | Page background or card surface |
| Ink Obsidian | `#292a2c` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Midnight | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #f6f5f0;
  --ref-ink-obsidian: #292a2c;
  --ref-pure-white: #ffffff;
  --ref-deep-midnight: #000000;
}
```

## Typography direction
- **Open Sans**: 400, 18px, 30px, 1.67, 2.33; substitute `system-ui, sans-serif`.
- **neue-haas-grotesk-text**: 400, 18px, 30px, 1.00, 2.33; substitute `'EB Garamond', serif`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `30px`
- Element Gap: `30px`
- Radius: `none: 0px`

## Component cues
- **Header Navigation Link**: Top-level navigation items
- **Hero Headline**: Dominant page titles and primary visual impact
- **Social Link**: Footer or section-level links to external platforms

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
