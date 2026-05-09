# Mike Matas - Refero Design MD

- Source: https://styles.refero.design/style/04f6cb02-de90-4d78-9c5f-0eb52f826484
- Original site: https://mikematas.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist textual canvas. Information presented with monastic simplicity against an expansive white background.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Muted Gray | `#999999` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-muted-gray: #999999;
}
```

## Typography direction
- **Lab Grotesque**: 100, 400, 600, 18px, 20px, 40px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Page Max Width: `900px`
- Radius: `none: 0px`

## Component cues
- **Project Card — California Plants**: Reference component style.
- **Site Navigation Header**: Reference component style.
- **Portfolio Project List**: Reference component style.
- **Main Navigation Link**: Unadorned textual links for navigation.
- **Secondary Navigation Link**: Subtle links for 'About', 'Twitter', 'Instagram'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
