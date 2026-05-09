# Forner - Refero Design MD

- Source: https://styles.refero.design/style/2a830d03-cebc-48f0-a50f-ad78168c5026
- Original site: https://forner.studio
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Earthy, typographic canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Ink | `#484036` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ecece4` | neutral | Page background or card surface |
| Stone Gray | `#cacab0` | neutral | Border, muted text, or supporting surface |
| Warm Mist | `#d5d5c4` | neutral | Border, muted text, or supporting surface |
| Pale Linen | `#f2e9cf` | neutral | Page background or card surface |
| Ash Gray | `#666e72` | neutral | Border, muted text, or supporting surface |
| Deep Charcoal | `#212529` | neutral | Primary text or dark surface |
| Rich Wood | `#33302c` | neutral | Primary text or dark surface |

```css
:root {
  --ref-carbon-ink: #484036;
  --ref-canvas-white: #ecece4;
  --ref-stone-gray: #cacab0;
  --ref-warm-mist: #d5d5c4;
  --ref-pale-linen: #f2e9cf;
  --ref-ash-gray: #666e72;
  --ref-deep-charcoal: #212529;
  --ref-rich-wood: #33302c;
}
```

## Typography direction
- **ClashDisplay**: 400, 17px, 30px, 52px, 56px, 0.97, 0.98, 1.10, 1.13; substitute `General Sans`.
- **Surt**: 400, 22px, 29px, 45px, 56px, 112px, 0.98, 1.00, 1.03, 1.10, 1.35, 1.50; substitute `Archivo Expanded`.
- **BigDailyShort**: 400, 17px, 37px, 45px, 0.98, 1.00, 1.03; substitute `Playfair Display Italic`.

## Spacing / shape
- Section Gap: `86px`
- Card Padding: `29px`
- Element Gap: `14px`
- Radius: `default: 4px`

## Component cues
- **Ghost Navigation Button**: Menu navigation icon/button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
