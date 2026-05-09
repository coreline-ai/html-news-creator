# Vectary - Refero Design MD

- Source: https://styles.refero.design/style/dfe5faa4-a108-45a8-a68c-ed19be2db766
- Original site: https://vectary.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Blueprint on Whiteboard. The crisp contrast and precise typography against a clean white background feel like technical specifications brought to life with minimal flourish.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#252525` | neutral | Primary text or dark surface |
| Deep Slate | `#313131` | neutral | Primary text or dark surface |
| Midtone Gray | `#595959` | neutral | Border, muted text, or supporting surface |
| Muted Silver | `#949494` | neutral | Border, muted text, or supporting surface |
| Alabaster White | `#ffffff` | neutral | Page background or card surface |
| Vectary Violet | `#6100ff` | brand | Action accent / signal color |
| Violet Gradient | `#6100ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #252525;
  --ref-deep-slate: #313131;
  --ref-midtone-gray: #595959;
  --ref-muted-silver: #949494;
  --ref-alabaster-white: #ffffff;
  --ref-vectary-violet: #6100ff;
  --ref-violet-gradient: #6100ff;
}
```

## Typography direction
- **Inter**: 400, 700, 900, 14px, 16px, 18px, 22px, 26px, 83px, 1.00, 1.09, 1.30, 1.40, 1.50, 1.69; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `30px`
- Element Gap: `6px`
- Radius: `buttons: 8px, default: 8px, navigation: 0px`

## Component cues
- **Button Group — Primary + Secondary**: Reference component style.
- **Policy Section Card — Acceptable Use**: Reference component style.
- **Prohibited Use Bullet List**: Reference component style.
- **Primary Navigation Link**: Navigation, header
- **Section Heading (Large)**: Primary page title

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
