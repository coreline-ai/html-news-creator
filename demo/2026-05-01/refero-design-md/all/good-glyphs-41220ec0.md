# Good Glyphs - Refero Design MD

- Source: https://styles.refero.design/style/41220ec0-ca0d-4697-a2fc-7a9a50d52e7c
- Original site: https://goodglyphs.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Playbill on Black Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ghostly Green | `#c7ffcd` | brand | Action accent / signal color |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Slate Text | `#101010` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ghostly-green: #c7ffcd;
  --ref-midnight-ink: #000000;
  --ref-slate-text: #101010;
}
```

## Typography direction
- **Helvetica Neue**: 300, 400, 13px, 14px, 28px, 288px, 0.80, 1.20, 1.50; substitute `Arial`.
- **good-glyphs**: 400, 288px, 1.00, 1.20; substitute `System icons (fallback)`.

## Spacing / shape
- Section Gap: `84px`
- Card Padding: `42px`
- Element Gap: `4px`
- Radius: `cards: 14px, other: 14px, buttons: 140px`

## Surface cues
- **Canvas** `#c7ffcd`: Primary page background and overall content area.
- **Card Surface** `#000000`: Background for major content blocks like contributor cards.

## Component cues
- **Default Button**: Standard interactive element with minimal styling.
- **Inverted Button**: Action-oriented button with high contrast.
- **Download Button**: Primary call to action.
- **Contributor Card**: Displays individual entries for designers.
- **Text Input (Default)**: Basic text input field.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
