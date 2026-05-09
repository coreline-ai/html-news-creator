# Jitter - Refero Design MD

- Source: https://styles.refero.design/style/ab1e41e9-7d21-4762-b498-51b8c63ae7ce
- Original site: https://jitter.video
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic design studio on bleached white paper. A brightly lit, expansive canvas with meticulously placed, rounded interface elements and sharp, bold typography.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#19171c` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Lunar Dust | `#f2f1f3` | neutral | Page background or card surface |
| Gravel | `#e5e4e7` | neutral | Page background or card surface |
| Ash | `#97979b` | neutral | Border, muted text, or supporting surface |
| Slate | `#6e6e73` | neutral | Border, muted text, or supporting surface |
| Jitter Violet | `#7a40ed` | brand | Action accent / signal color |
| Sky Blue | `#00b2ff` | accent | Action accent / signal color |
| Lemon Drop | `#f5ff63` | accent | Action accent / signal color |
| Soft Violet | `#a981ff` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #19171c;
  --ref-white-canvas: #ffffff;
  --ref-lunar-dust: #f2f1f3;
  --ref-gravel: #e5e4e7;
  --ref-ash: #97979b;
  --ref-slate: #6e6e73;
  --ref-jitter-violet: #7a40ed;
  --ref-sky-blue: #00b2ff;
}
```

## Typography direction
- **TWK Lausanne**: 500, 600, 700, 750, 800, 16px, 18px, 20px, 21px, 24px, 36px, 40px, 48px, 72px, 80px, 200px, 0.85, 0.90, 0.95, 1.00, 1.20, 1.38, 1.50, 2.50; substitute `Montserrat`.
- **Inter**: 400, 500, 600, 700, 800, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 26px, 1.10, 1.14, 1.15, 1.20, 1.25, 1.40, 1.41, 1.50, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `12px`
- Page Max Width: `860px`
- Radius: `badges: 40px, inputs: 0px 50px 50px 0px, buttons: 50px, default: 40px`

## Component cues
- **Announcement Badge + CTA Button Group**: Reference component style.
- **Templates Section — Pill Badge + Description Block**: Reference component style.
- **Feature Statement Card**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Call-to-Action Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
