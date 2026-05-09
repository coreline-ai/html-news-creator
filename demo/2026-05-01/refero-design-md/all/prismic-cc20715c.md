# Prismic - Refero Design MD

- Source: https://styles.refero.design/style/cc20715c-e9ab-42a7-a34b-d43d76677219
- Original site: https://prismic.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#151515` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#505050` | neutral | Border, muted text, or supporting surface |
| Moonlight Gray | `#eeeeee` | neutral | Page background or card surface |
| Light Taupe | `#f7f7f7` | neutral | Page background or card surface |
| Sky Burst | `#59b5f8` | brand | Action accent / signal color |
| Deep Plum | `#8e44ec` | brand | Action accent / signal color |
| Jade Glow | `#3bbb96` | brand | Action accent / signal color |
| Cool Mint | `#e8f8f3` | accent | Action accent / signal color |
| Pale Peach | `#fef1e9` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #151515;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #505050;
  --ref-moonlight-gray: #eeeeee;
  --ref-light-taupe: #f7f7f7;
  --ref-sky-burst: #59b5f8;
  --ref-deep-plum: #8e44ec;
  --ref-jade-glow: #3bbb96;
}
```

## Typography direction
- **copyFont**: 500, 600, 700, 14px, 16px, 18px, 22px, 1, 1.14, 1.43, 1.45, 1.5, 1.56.
- **Inter**: use as primary family; substitute `system-ui, sans-serif`.
- **Inter**: use as primary family; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `40px`
- Element Gap: `16px`
- Page Max Width: `1280px`
- Radius: `cards: 12px, icons: 9999px, links: 2px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for content sections
- **Light Taupe** `#f7f7f7`: Subtle background for alternating sections or elevated content blocks
- **Accent Card Backgrounds** `#fff`: Specialized cards and testimonials, using hues like #f5e6ff, #e8f8f3, #fef1e9, #e6f7fe for thematic grouping
- **Midnight Charcoal Deep** `#151515`: Overlapping dark sections, footer, or focused informational panels

## Component cues
- **Primary Filled Button**: Main call-to-action button for initiating key actions.
- **Ghost Button**: Secondary calls-to-action, or less emphasized actions.
- **Navigation Link**: Primary navigation items in the header and footer.
- **Branded Accordion Card**: Informational cards presenting features or testimonials, often with a unique accent background.
- **Outlined Accent Button**: Action buttons emphasizing connection to specific brand colors.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
