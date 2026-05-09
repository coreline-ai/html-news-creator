# Studio Oker - Refero Design MD

- Source: https://styles.refero.design/style/e045b276-ae8d-442e-98de-fa8650e284de
- Original site: https://oker.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery at Dusk

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Charcoal Edge | `#484848` | neutral | Border, muted text, or supporting surface |
| Brand Red | `#cf2e20` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ghost-white: #ffffff;
  --ref-whisper-gray: #a0a0a0;
  --ref-charcoal-edge: #484848;
  --ref-brand-red: #cf2e20;
}
```

## Typography direction
- **NextBook**: 300, 400, 16px, 24px, 32px, 80px, 1.00, 1.13, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `969px`
- Radius: `cards: 0px, images: 0px, buttons: 0px`

## Surface cues
- **Midnight Canvas** `#000000`: Primary page background and base surface for all content.

## Component cues
- **Ghost Navigation Link**: Primary navigation elements in the header.
- **Grid Content Card**: Displaying portfolio items or features on the main content area.
- **Muted Text Block**: Secondary details or related information, often with links.
- **Section Divider (Subtle)**: Separating major content sections with a minimalist approach.
- **Accent Read More Link**: Prominent click targets for detailed content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
