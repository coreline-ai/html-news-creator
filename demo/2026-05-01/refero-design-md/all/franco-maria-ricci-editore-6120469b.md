# Franco Maria Ricci Editore - Refero Design MD

- Source: https://styles.refero.design/style/6120469b-a1c8-46d3-b7fd-8aa6dc22c0d9
- Original site: https://www.francomariaricci.com/en
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ivory Page, Golden Inscription

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Paper | `#f6f6f6` | neutral | Page background or card surface |
| Faded Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Baroque Gold | `#bc9c5c` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-warm-paper: #f6f6f6;
  --ref-faded-gray: #b3b3b3;
  --ref-midnight-ink: #000000;
  --ref-baroque-gold: #bc9c5c;
}
```

## Typography direction
- **BodoniSvntytwoITCStd-Book**: 400, 12px, 14px, 16px, 18px, 22px, 42px, 0.95, 1.25; substitute `serif`.
- **BodoniSvntytwoITCStd-BookIt**: 400, 16px, 22px, 42px, 1.25; substitute `serif`.
- **Arial**: 400, 700, 12px, 14px, 1.25; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `none: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Dominant page background, providing a clean, expansive foundation.
- **Warm Paper** `#f6f6f6`: Secondary background for content sections, subtly breaking up the main canvas without strong contrast.
- **Faded Gray** `#b3b3b3`: Background for specific, muted hero or decorative sections, offering a gentle visual shift.

## Component cues
- **Ghost Button**: Interactive elements with minimal visual footprint, often acting as links or secondary actions. Their visual weight is conveyed through text and a…
- **Outlined Accent Button**: Primary Call-to-action or important interactive elements, distinguished by the Baroque Gold border.
- **Product Display Card**: Used to showcase individual product items like books, emphasizing the product image itself.
- **Text Input (Underlined)**: Standard input field for forms, with minimal styling.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
