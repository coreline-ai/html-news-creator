# until - Refero Design MD

- Source: https://styles.refero.design/style/ded6d7c4-2801-45f4-8b8a-089f1b37842d
- Original site: https://www.untillabs.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment, dark charcoal type

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#f7f3ec` | neutral | Page background or card surface |
| Charcoal | `#121212` | neutral | Primary text or dark surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Soft Stone | `#bebebe` | neutral | Border, muted text, or supporting surface |
| Olive Grove | `#6c853b` | accent | Action accent / signal color |
| Sunset Fade | `#c6350f` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment: #f7f3ec;
  --ref-charcoal: #121212;
  --ref-midnight-ink: #000000;
  --ref-snow: #ffffff;
  --ref-soft-stone: #bebebe;
  --ref-olive-grove: #6c853b;
  --ref-sunset-fade: #c6350f;
}
```

## Typography direction
- **neueHaasText**: 400, 500, 14px, 16px, 1.00, 1.43, 1.50; substitute `Inter`.
- **neueHaasDisplay**: 400, 500, 16px, 24px, 32px, 39px, 56px, 69px, 0.90, 0.95, 1.00, 1.10, 1.50; substitute `Graphik`.
- **Geist Mono**: 400, 500, 12px, 14px, 1.00, 1.40, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1283px`
- Radius: `pill: 50px, cards: 32px, input: 6px, images: 24px, buttons: 64px`

## Surface cues
- **Parchment** `#f7f3ec`: Base page background, light sections
- **Snow** `#ffffff`: Elevated card backgrounds, interactive elements

## Component cues
- **Ghost Header Button**: Navigation button in the header, visually transparent until hover.
- **Primary Filled Button**: Key action buttons, such as 'Join Us' or 'Join the team'.
- **Secondary Filled Button**: Less prominent actions, often alongside a primary button.
- **Information Card**: Content containers for text and images, often used in grids.
- **Header Navigation**: Top-level navigation element for page sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
