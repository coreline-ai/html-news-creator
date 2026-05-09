# Fold - Refero Design MD

- Source: https://styles.refero.design/style/4d1d50ff-18b8-4acf-a356-48eb5c414711
- Original site: https://fold.money
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Softly lit, data-rich canvas

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f0f1f5` | neutral | Page background or card surface |
| Ash Gray | `#c7cbdb` | neutral | Border, muted text, or supporting surface |
| Graphite | `#dddfe9` | neutral | Page background or card surface |
| Midnight Ink | `#20294c` | brand | Action accent / signal color |
| Deep Violet | `#375390` | neutral | Action accent / signal color |
| Active Blue | `#459af8` | accent | Action accent / signal color |
| Muted Slate | `#676b89` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#979db5` | neutral | Border, muted text, or supporting surface |
| Ocean Tint | `#0a2d67` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f0f1f5;
  --ref-ash-gray: #c7cbdb;
  --ref-graphite: #dddfe9;
  --ref-midnight-ink: #20294c;
  --ref-deep-violet: #375390;
  --ref-active-blue: #459af8;
  --ref-muted-slate: #676b89;
}
```

## Typography direction
- **GT Walsheim Pro**: 400, 600, 700, 10px, 14px, 16px, 17px, 18px, 20px, 24px, 26px, 32px, 64px, 100px, 0.85, 0.91, 1.00, 1.18, 1.19, 1.20, 1.25, 1.33, 1.41, 1.43, 1.50, 1.75; substitute `system-ui`.
- **GT America**: 400, 500, 24px, 42px, 1.00, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 12px, images: 8px, buttons: 9999px, pillShape: 9999px, navigation: 24px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, light and airy primary surface.
- **Whisper Gray** `#f0f1f5`: Secondary background for cards and subtle section breaks, slightly receded from the primary canvas.
- **Ash Gray** `#c7cbdb`: Tertiary background for less prominent elements like list items, or for providing a subtle border effect that separates content.

## Component cues
- **Filled Primary Button**: Call to action button for critical actions.
- **Ghost Button**: Secondary action or navigational link with minimal visual weight.
- **Pill Button**: Tertiary action, status labels, or filters.
- **Subtle Pill Button**: Less prominent pill-shaped actions, for category tags or non-critical actions.
- **Light Card Default**: Standard informational card, often used for content display.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
