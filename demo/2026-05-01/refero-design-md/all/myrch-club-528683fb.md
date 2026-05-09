# Myrch Club - Refero Design MD

- Source: https://styles.refero.design/style/528683fb-6b17-4fc6-b37e-d831ee1b20e2
- Original site: https://www.myrch.club
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Archival white space

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Gray Surface | `#f9f9f9` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Ink Detail | `#111111` | neutral | Primary text or dark surface |
| Muted Gray Text | `#cfcfcf` | neutral | Border, muted text, or supporting surface |
| Dark Gray Text | `#888888` | neutral | Border, muted text, or supporting surface |
| Archive Red | `#ff0000` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-pale-gray-surface: #f9f9f9;
  --ref-text-black: #000000;
  --ref-ink-detail: #111111;
  --ref-muted-gray-text: #cfcfcf;
  --ref-dark-gray-text: #888888;
  --ref-archive-red: #ff0000;
}
```

## Typography direction
- **Times**: 400, 16px, 1.20; substitute `Times New Roman`.
- **Arial Narrow**: 400, 14px, 20px, 42px, 1.24, 1.33, 1.40, 1.43.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `30px`
- Element Gap: `20px`
- Radius: `misc: 23px, cards: 10px, buttons: 10px`

## Component cues
- **Navigation Button**: Ghost interactive element
- **Active Navigation Button**: Filled interactive element
- **Product Card**: Display individual merchandise items
- **Minimal Badge**: Informational label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
