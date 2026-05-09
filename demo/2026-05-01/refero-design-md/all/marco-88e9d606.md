# Marco - Refero Design MD

- Source: https://styles.refero.design/style/88e9d606-7e8f-479c-9508-1b081e254ed9
- Original site: https://www.marco.fyi
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized content on frosted glass

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Card Frost | `#f7f7f9` | neutral | Page background or card surface |
| Whisper Gray | `#f2f2f2` | neutral | Page background or card surface |
| Cloud Tint | `#eff0ff` | neutral | Page background or card surface |
| Warm Paper | `#fff9ed` | neutral | Page background or card surface |
| Text Primary | `#333333` | neutral | Primary text or dark surface |
| Text Secondary | `#707070` | neutral | Border, muted text, or supporting surface |
| Text Dim | `#949494` | neutral | Border, muted text, or supporting surface |
| Divider Gray | `#cccccf` | neutral | Border, muted text, or supporting surface |
| Outline Blue | `#1685c7` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-card-frost: #f7f7f9;
  --ref-whisper-gray: #f2f2f2;
  --ref-cloud-tint: #eff0ff;
  --ref-warm-paper: #fff9ed;
  --ref-text-primary: #333333;
  --ref-text-secondary: #707070;
  --ref-text-dim: #949494;
}
```

## Typography direction
- **Maison Neue**: 400, 600, 12px, 14px, 40px, 1.00, 1.43, 1.67; substitute `Inter`.
- **Graphik**: 400, 500, 600, 14px, 16px, 20px, 31px, 1.00, 1.25, 1.38, 1.43, 1.50; substitute `Figtree`.
- **Neue Montreal**: 400, 500, 8px, 10px, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 26px, 1.00, 1.11, 1.13, 1.20, 1.25, 1.45, 1.67; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1400px`
- Radius: `cards: 32px, badges: 100px, inputs: 8px, buttons: 230px, default: 12px, thumbnails: 18px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary page background, expansive white space
- **Content Frost** `#f7f7f9`: Default background for main content cards and sections
- **Interactive Tint** `#eff0ff`: Background for active or emphasized cards and interactive elements
- **Elevated Shadow** `#fff9ed`: Background for visually distinct cards that appear slightly lifted, often with custom shadows

## Component cues
- **Pill Navigation Button**: Top-level navigation and filter controls.
- **Outline Action Button**: Secondary calls-to-action or subtle interactive elements.
- **Default Content Card**: Container for primary content blocks.
- **Layered Detail Card**: Elevated information or interactive listings within larger content areas.
- **Ghost Card**: Purely structural grouping without visual adornment.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
