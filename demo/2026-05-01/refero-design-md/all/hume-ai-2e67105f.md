# Hume AI - Refero Design MD

- Source: https://styles.refero.design/style/2e67105f-9f9a-45b5-9281-29734e753bd6
- Original site: https://hume.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm pastel research lab. Soft, rounded elements meet crisp technical details within a muted, inviting color scheme.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pale Ivory | `#fff9f3` | neutral | Page background or card surface |
| Graphite | `#222222` | neutral | Primary text or dark surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Light Mauve | `#fce0ee` | neutral | Page background or card surface |
| Soft Lilac | `#e6d1ed` | neutral | Border, muted text, or supporting surface |
| Mint Cream | `#cef1e1` | neutral | Page background or card surface |
| Sky Mist | `#ccdff1` | neutral | Page background or card surface |
| Muted Apricot | `#ffdfb8` | neutral | Page background or card surface |
| Dusty Peach | `#fcd4bd` | neutral | Page background or card surface |
| Deep Plum | `#c094e4` | brand | Action accent / signal color |

```css
:root {
  --ref-pale-ivory: #fff9f3;
  --ref-graphite: #222222;
  --ref-bright-white: #ffffff;
  --ref-light-mauve: #fce0ee;
  --ref-soft-lilac: #e6d1ed;
  --ref-mint-cream: #cef1e1;
  --ref-sky-mist: #ccdff1;
  --ref-muted-apricot: #ffdfb8;
}
```

## Typography direction
- **Fellix**: 400, 520, 12px, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 48px, 1.00, 1.11, 1.20, 1.25, 1.33, 1.43, 1.50, 1.56, 1.63; substitute `system-ui, sans-serif`.
- **PP Fraktion Mono**: 400, 10px, 12px, 14px, 1.33, 1.43, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `12px`
- Radius: `cards: 8px, input: 1.67772e+07px, buttons: 1.67772e+07px, default: 8px`

## Component cues
- **Stat Block — Research Metrics**: Reference component style.
- **Tab Bar + Data Bar Chart**: Reference component style.
- **Dataset Composition Card + Feature Cards**: Reference component style.
- **Navigation Link**: Navigation element
- **Pill Button**: Segmented control or tag

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
