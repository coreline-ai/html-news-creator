# Basedash - Refero Design MD

- Source: https://styles.refero.design/style/77b723ca-9583-4349-9b5e-2ef8b4fde002
- Original site: https://www.basedash.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data studio.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Canvas | `#000000` | neutral | Primary text or dark surface |
| Eclipse Surface | `#050607` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Carbon Detail | `#333333` | neutral | Primary text or dark surface |
| Illumination White | `#e8eaee` | neutral | Page background or card surface |
| Vivid Violet | `#9984d8` | brand | Action accent / signal color |
| Gradient Violet | `#6b5aa8` | brand | Action accent / signal color |
| Alert Green | `#3fcb7f` | semantic | Action accent / signal color |

```css
:root {
  --ref-obsidian-canvas: #000000;
  --ref-eclipse-surface: #050607;
  --ref-ghost-white: #ffffff;
  --ref-ash-gray: #b3b3b3;
  --ref-steel-gray: #808080;
  --ref-carbon-detail: #333333;
  --ref-illumination-white: #e8eaee;
  --ref-vivid-violet: #9984d8;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 18px, 30px, 34px, 48px, 1.00, 1.20, 1.33, 1.38, 1.43, 1.50, 1.56; substitute `system-ui`.
- **Alpha Lyrae**: 400, 48px, 1.00.
- **Iowan Old Style**: 300, 24px, 1.25; substitute `serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `tags: 999px, cards: 16px, fields: 6px, buttons: 6px`

## Component cues
- **Primary Filled Button**: Call to action button for starting free trials or sign-ups.
- **Ghost Accent Button**: Secondary call to action button, or action that needs subtle visual emphasis.
- **Navigation Link Button**: Links within the main navigation bar.
- **Small Dark Button**: Compact utility buttons, often for logging in or secondary actions in header.
- **Content Card**: Containers for content blocks like testimonials or feature descriptions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
