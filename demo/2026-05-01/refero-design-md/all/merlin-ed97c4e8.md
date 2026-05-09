# Merlin - Refero Design MD

- Source: https://styles.refero.design/style/ed97c4e8-4b0c-46b7-9957-c814854229f7
- Original site: https://www.merlin.computer
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, sharp focus

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper White | `#fdf8f7` | neutral | Page background or card surface |
| Powder White | `#f5f5f4` | neutral | Page background or card surface |
| Snowdrift | `#eeeeee` | neutral | Page background or card surface |
| Silver Mist | `#dddddd` | neutral | Page background or card surface |
| Platinum Grey | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Carbon | `#1c1d1f` | neutral | Primary text or dark surface |
| Lead | `#333333` | neutral | Primary text or dark surface |
| Anthracite | `#6a6b6c` | neutral | Border, muted text, or supporting surface |
| Slate | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-whisper-white: #fdf8f7;
  --ref-powder-white: #f5f5f4;
  --ref-snowdrift: #eeeeee;
  --ref-silver-mist: #dddddd;
  --ref-platinum-grey: #cccccc;
  --ref-carbon: #1c1d1f;
  --ref-lead: #333333;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 9px, 10px, 12px, 13px, 14px, 16px, 20px, 23px, 25px, 26px, 30px, 40px, 60px, 70px, 1.00, 1.13, 1.15, 1.17, 1.40, 1.50, 1.55; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 15px, input: 12.5px, buttons: 100px, largeCards: 40px`

## Surface cues
- **Powder White** `#f5f5f4`: Base page background, a subtle, almost unnoticeable off-white.
- **Canvas White** `#ffffff`: Primary surface for cards, content blocks, and main UI elements.
- **Whisper White** `#fdf8f7`: Slightly elevated card backgrounds, adding a minor perceptual layer without significant contrast.

## Component cues
- **Primary Filled Button**: Action button for critical conversions
- **Success Filled Button**: Positive action or primary CTA button
- **Ghost Button**: Secondary actions or links with minimal visual weight
- **Subtle Ghost Button**: Tertiary actions, less prominent than ghost buttons
- **Callout Card**: Feature highlights or interactive educational content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
