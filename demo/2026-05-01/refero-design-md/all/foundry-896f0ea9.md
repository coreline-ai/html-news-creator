# Foundry - Refero Design MD

- Source: https://styles.refero.design/style/896f0ea9-6f1a-40a6-aba7-fdaa579c7352
- Original site: https://foundry.basement.studio
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Typeface Dungeon, Glowing Console

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#121212` | neutral | Primary text or dark surface |
| Ghostly Gray | `#efefef` | neutral | Page background or card surface |
| Wireframe White | `#e2e8f0` | neutral | Page background or card surface |
| Shadow Border | `#3a3a3a` | neutral | Primary text or dark surface |
| Muted Text | `#747474` | neutral | Border, muted text, or supporting surface |
| Basement Orange | `#ff4d00` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #121212;
  --ref-ghostly-gray: #efefef;
  --ref-wireframe-white: #e2e8f0;
  --ref-shadow-border: #3a3a3a;
  --ref-muted-text: #747474;
  --ref-basement-orange: #ff4d00;
}
```

## Typography direction
- **JetBrains Mono**: 400, 700, 12px, 14px, 18px, 1.14, 1.29, 1.30, 1.32, 1.40, 1.50; substitute `monospace`.
- **Inter**: 400, 14px, 16px, 18px, 1.29, 1.30, 1.50; substitute `system-ui`.
- **Basement Grotesque Black Expanded**: 400, 120px, 0.95; substitute `Impact`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `15px`
- Element Gap: `8px`
- Page Max Width: `270px`
- Radius: `cards: 8px, default: 2.8px, interactive: 50%`

## Component cues
- **Text Link**: Navigation and informational links within body text.
- **Typeface Navigation Button (Inactive)**: Navigation item for browsing typeface categories.
- **Typeface Navigation Button (Active)**: Currently selected typeface category.
- **Buy Now Button (Outlined)**: Primary action for purchasing typefaces.
- **Mode Toggle Button**: Interaction for switching display modes within a typeface showcase.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
