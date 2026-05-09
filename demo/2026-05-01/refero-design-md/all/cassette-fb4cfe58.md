# Cassette - Refero Design MD

- Source: https://styles.refero.design/style/fb4cfe58-00b5-4e6a-b251-0c65e60b6649
- Original site: https://cassettemusic.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Granular sonic texture

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Oil | `#19181a` | neutral | Primary text or dark surface |
| Cassette Yellow | `#f0e226` | brand | Action accent / signal color |
| Ghostly Gray | `#d9d7ce` | neutral | Border, muted text, or supporting surface |
| True Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#f5f4f0` | neutral | Page background or card surface |
| Subtle Line | `#272727` | neutral | Primary text or dark surface |
| Pop Pink | `#fac4f0` | accent | Action accent / signal color |
| Tangelo Dream | `#ff8461` | accent | Action accent / signal color |
| Sky Blue | `#2896f3` | accent | Action accent / signal color |
| Evergreen | `#0db55b` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-oil: #19181a;
  --ref-cassette-yellow: #f0e226;
  --ref-ghostly-gray: #d9d7ce;
  --ref-true-black: #000000;
  --ref-paper-white: #f5f4f0;
  --ref-subtle-line: #272727;
  --ref-pop-pink: #fac4f0;
  --ref-tangelo-dream: #ff8461;
}
```

## Typography direction
- **Apercu Pro**: 400, 15px, 37px, 56px, 60px, 1.08, 1.20; substitute `system-ui`.
- **Apercu Mono Pro**: 400, 13px, 14px, 1.00, 1.16, 1.30; substitute `Menlo, Monaco, 'Courier New', monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `13px`
- Element Gap: `8px`
- Radius: `other: 900px, buttons: 900px`

## Surface cues
- **Midnight Oil Canvas** `#19181a`: Primary page background, dark surfaces with a subtle texture.
- **Paper White Surface** `#f5f4f0`: Background for badges and lighter content blocks.
- **Cassette Yellow Accent** `#f0e226`: Interactive elements, primary button fills, and bold highlight areas.

## Component cues
- **Primary Filled Button**: Main call to action
- **Ghost Button**: Secondary call to action, navigation items
- **Info Badge**: Informational labels, status indicators
- **Outline Badge**: Subtle categories or labels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
