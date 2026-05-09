# Clipdrop - Refero Design MD

- Source: https://styles.refero.design/style/935f22cb-04ec-48c8-a6da-aa8c2c5abe8b
- Original site: https://clipdrop.co
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#ededed` | neutral | Page background or card surface |
| Graphite Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#2d2d2d` | neutral | Primary text or dark surface |
| Slate Steel | `#404040` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#767676` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Subtle Blue | `#c9d7f5` | neutral | Action accent / signal color |
| Midnight Ink | `#171717` | neutral | Primary text or dark surface |
| Cerulean Blue | `#1c60f6` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #ededed;
  --ref-graphite-black: #000000;
  --ref-charcoal: #2d2d2d;
  --ref-slate-steel: #404040;
  --ref-silver-mist: #767676;
  --ref-medium-gray: #8f8f8f;
  --ref-subtle-blue: #c9d7f5;
}
```

## Typography direction
- **Primary**: 400, 500, 600, 700, 12px, 14px, 16px, 20px, 1.00, 1.20, 1.40, 1.50.
- **SecondaryFont**: 400, 60px, 96px, 1.10.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `pills: 9999px, buttons: 12px, default: 16px`

## Component cues
- **Primary Filled Button**: Call to action button
- **Secondary Filled Button**: Call to action button
- **Ghost Button**: Subtle action button
- **Soft Gray Button**: Neutral action button
- **Image Card**: Content container for media

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
