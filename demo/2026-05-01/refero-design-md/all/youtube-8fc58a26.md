# YouTube - Refero Design MD

- Source: https://styles.refero.design/style/8fc58a26-47be-406e-8429-37925551c0ec
- Original site: https://youtube.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp White Canvas; an expansive, information-first interface on a stark white background with minimal ornamentation.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#0f0f0f` | neutral | Primary text or dark surface |
| Medium Gray | `#606060` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#909090` | neutral | Border, muted text, or supporting surface |
| Border Gray | `#c6c6c6` | neutral | Border, muted text, or supporting surface |
| Accent Blue | `#065fd4` | brand | Action accent / signal color |
| YouTube Red | `#ff0033` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #0f0f0f;
  --ref-medium-gray: #606060;
  --ref-light-gray: #909090;
  --ref-border-gray: #c6c6c6;
  --ref-accent-blue: #065fd4;
  --ref-youtube-red: #ff0033;
}
```

## Typography direction
- **Roboto**: 400, 500, 700, 900, 10px, 12px, 13px, 14px, 16px, 1.20, 1.38, 1.43, 1.50, 2.57; substitute `system-ui`.
- **Arial**: 400, 13px, 1.20; substitute `Helvetica, sans-serif`.
- **YouTube Sans**: 600, 20px, 1.40; substitute `Roboto, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1185px`
- Radius: `subtle: 40px, buttons: 18px, default: 10px`

## Component cues
- **History Off — Dialogue Card**: Reference component style.
- **Sidebar Navigation — Explore Section**: Reference component style.
- **Sign In Prompt — Sidebar Card**: Reference component style.
- **Navigation Link**: Interactive element
- **Search Input Field**: Data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
