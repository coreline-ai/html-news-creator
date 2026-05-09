# Sigmaphoto - Refero Design MD

- Source: https://styles.refero.design/style/67c60ee4-ac38-41ee-834e-ed2a92146417
- Original site: https://www.sigmaphoto.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision engineered, high-contrast monochrome

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Gray | `#333333` | neutral | Primary text or dark surface |
| Cadet Blue | `#0048ff` | brand | Action accent / signal color |
| Cool Gray | `#707070` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#999999` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-gray: #333333;
  --ref-cadet-blue: #0048ff;
  --ref-cool-gray: #707070;
  --ref-silver-mist: #999999;
}
```

## Typography direction
- **Sigma Sans**: 400, 13px, 16px, 1.10, 1.20, 1.25, 1.54.
- **Sigma Serif**: 400, 16px, 24px, 1.10, 1.25.
- **Sigma Serif head**: 400, 48px, 88px, 1.10, 1.25; substitute `Palatino`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `15px`
- Element Gap: `16px`
- Radius: `inputs: 1px`

## Surface cues
- **Canvas Background** `#ffffff`: Dominant page background for most content sections.
- **Card Surface** `#ffffff`: Background for self-contained content blocks, often within the main canvas.
- **Interactive Background** `#333333`: Dark backgrounds for interactive components like filled buttons or navigation bars that require white text for contrast.

## Component cues
- **Ghost Button**: Secondary action or discrete navigation trigger.
- **Solid Button (Dark)**: Standard action button for primary or important actions.
- **Blue Circular Button**: Distinctive interactive element, possibly for a specific function like an accessibility toggle.
- **Muted Ghost Button**: An action button with lower visual emphasis, for less critical functions.
- **Standard Input Field**: Form input element for text entry.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
