# Carrot - Refero Design MD

- Source: https://styles.refero.design/style/a7a69d27-e1a9-4322-b58f-3c7633fdc60d
- Original site: https://carrot.tech
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast lime canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Lime Zing | `#e7eb5d` | brand | Action accent / signal color |
| Forest Whisper | `#535521` | brand | Action accent / signal color |

```css
:root {
  --ref-black-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-lime-zing: #e7eb5d;
  --ref-forest-whisper: #535521;
}
```

## Typography direction
- **Signifier**: 300, 50px, 72px, 1.15; substitute `Georgia`.
- **DM Sans**: 400, 500, 16px, 17px, 20px, 24px, 29px, 1.25, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Button**: Secondary action
- **Text Link**: Navigation and inline links
- **Navigation Item**: Header and footer navigation
- **Input Field**: Data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
