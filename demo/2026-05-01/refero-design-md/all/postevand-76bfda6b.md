# Postevand - Refero Design MD

- Source: https://styles.refero.design/style/76bfda6b-125f-4d9b-96c0-356de1e9fc10
- Original site: https://postevand.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on stark white canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Whisper Gray | `#f0f1ef` | neutral | Page background or card surface |
| Ash Slate | `#333333` | neutral | Primary text or dark surface |
| Border Silver | `#d7d7d7` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-whisper-gray: #f0f1ef;
  --ref-ash-slate: #333333;
  --ref-border-silver: #d7d7d7;
}
```

## Typography direction
- **Nimbus Sans D OT**: 400, 700, 10px, 12px, 16px, 32px, 56px, 80px, 1.00, 1.20, 1.40; substitute `Inter`.
- **Helvetica**: 300, 400, 13px, 16px, 30px, 1.00, 1.54, 1.60; substitute `Arial`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `all: 0px`

## Component cues
- **Primary Filled Button**: Submit actions, main calls to action.
- **Ghost Header Button**: Header links and navigation elements.
- **Text Link Button**: Inline actions and secondary navigation at the bottom of sections.
- **Default Card**: Content grouping without visual emphasis.
- **Subtle Section Card**: Grouping related content with a slight background distinction.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
