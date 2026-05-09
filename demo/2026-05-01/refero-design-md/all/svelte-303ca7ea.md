# Svelte - Refero Design MD

- Source: https://styles.refero.design/style/303ca7ea-e6fa-4e95-8acb-8008c4d3c068
- Original site: https://svelte.dev
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp editorial elegance

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#141414` | neutral | Primary text or dark surface |
| Graphite | `#262626` | neutral | Primary text or dark surface |
| Pewter | `#666666` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#f2f2f2` | neutral | Page background or card surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Svelte Orange | `#d43008` | brand | Action accent / signal color |

```css
:root {
  --ref-carbon: #141414;
  --ref-graphite: #262626;
  --ref-pewter: #666666;
  --ref-ghost-white: #f2f2f2;
  --ref-snow: #ffffff;
  --ref-svelte-orange: #d43008;
}
```

## Typography direction
- **DM Serif Display**: 500, 54px, 1.20; substitute `DM Serif Display`.
- **EB Garamond**: 400, 10px, 22px, 1.50; substitute `EB Garamond`.
- **Fira Sans**: 400, 10px, 12px, 13px, 14px, 16px, 20px, 1.00, 1.20, 1.50, 1.70; substitute `Fira Sans`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `10px`
- Element Gap: `10px`
- Radius: `default: 4px, navItem: 4px`

## Component cues
- **GET STARTED CTA Button**: Reference component style.
- **Search Bar with Keyboard Shortcut**: Reference component style.
- **Companies Social Proof Block**: Reference component style.
- **Primary Navigation Link**: Main navigation item
- **Default Button**: General interactive button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
