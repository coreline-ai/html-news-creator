# Slush - Refero Design MD

- Source: https://styles.refero.design/style/8b6b547f-a357-4f1b-9842-4579c62dd42b
- Original site: https://slush.app
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful crypto minimalism with an electric hum.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#dceeff` | neutral | Page background or card surface |
| Ink | `#000000` | neutral | Primary text or dark surface |
| Paper | `#ffffff` | neutral | Page background or card surface |
| Pale Ash | `#e9e9e9` | neutral | Page background or card surface |
| Vivid Blue | `#4da2ff` | accent | Action accent / signal color |
| Vivid Green | `#55db9c` | accent | Action accent / signal color |
| Muted Violet | `#e9ccff` | accent | Action accent / signal color |
| Flame Orange | `#fb4903` | accent | Action accent / signal color |
| Golden Rod | `#ffd731` | accent | Action accent / signal color |
| Royal Purple | `#5c4ade` | brand | Action accent / signal color |

```css
:root {
  --ref-sky-canvas: #dceeff;
  --ref-ink: #000000;
  --ref-paper: #ffffff;
  --ref-pale-ash: #e9e9e9;
  --ref-vivid-blue: #4da2ff;
  --ref-vivid-green: #55db9c;
  --ref-muted-violet: #e9ccff;
  --ref-flame-orange: #fb4903;
}
```

## Typography direction
- **Lateral**: 800, 70px, 110px, 160px, 200px, 281px, 640px, 0.75; substitute `Bebas Neue`.
- **Aeonik Pro**: 500, 700, 12px, 13px, 14px, 15px, 16px, 24px, 30px, 64px, 1.00, 1.10, 1.20, 1.25, 1.39, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `48px`
- Element Gap: `4px`
- Radius: `cards: 40px, links: 20px, buttons: 40px, circular: 1600px, bodyElements: 30px`

## Component cues
- **Primary Filled Button**: Call to action button for key flows.
- **Ghost Button**: Secondary action or navigation items.
- **Subtle Grey Button**: Tertiary actions or subtle interactive elements.
- **Download Button with Icon**: Specific download actions for web or mobile.
- **Featured Content Card**: Prominent information display.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
