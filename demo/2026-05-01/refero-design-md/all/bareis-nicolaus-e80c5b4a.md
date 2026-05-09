# Bareis + Nicolaus - Refero Design MD

- Source: https://styles.refero.design/style/e80c5b4a-fd03-460e-a577-49928a4ab5db
- Original site: https://www.bareis-nicolaus.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic Monochrome Canvas: crisp, high-contrast, typographic art.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Black | `#000000` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#a9a9a9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-black: #000000;
  --ref-arctic-white: #ffffff;
  --ref-subtle-gray: #a9a9a9;
}
```

## Typography direction
- **Lausanne**: 400, 24px, 72px, 1.00, 1.20; substitute `Inter`.
- **Victor Serif**: 400, 24px, 1.20; substitute `Lora`.
- **Black Tie**: 400, 24px, 1.00; substitute `DM Mono`.

## Spacing / shape
- Section Gap: `29px`
- Card Padding: `13px`
- Element Gap: `13px`
- Page Max Width: `721px`
- Radius: `all: 120px`

## Surface cues
- **Page Canvas** `#000000`: Dominant background for the entire page, setting the dark theme.
- **Interactive Surface** `#ffffff`: Used for selected states of buttons and navigation, providing visual emphasis through color inversion.

## Component cues
- **Pill Button - Dark Filled**: Primary action, navigation items
- **Pill Button - Light Filled**: Active state or selected filter
- **Pill Button - Ghost**: Secondary actions, filters, navigation
- **Content Card - Default**: Project showcase, content containers
- **Footer Link**: Informational links in the footer

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
