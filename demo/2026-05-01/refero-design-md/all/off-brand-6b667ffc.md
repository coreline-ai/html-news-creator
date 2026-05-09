# OFF+BRAND. - Refero Design MD

- Source: https://styles.refero.design/style/6b667ffc-5158-4000-9252-3a107d5161ee
- Original site: https://www.itsoffbrand.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sculpted digital canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1d1d1d` | neutral | Primary text or dark surface |
| Canvas White | `#e5e4e0` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Frost Gray | `#bfbebe` | neutral | Border, muted text, or supporting surface |
| Gradient Aura | `#facb00` | brand | Action accent / signal color |
| Brand Orange | `#ff642f` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1d1d1d;
  --ref-canvas-white: #e5e4e0;
  --ref-pure-white: #ffffff;
  --ref-frost-gray: #bfbebe;
  --ref-gradient-aura: #facb00;
  --ref-brand-orange: #ff642f;
}
```

## Typography direction
- **Ataero Retina OB Edition**: 400, 700, 11px, 15px, 18px, 34px, 46px, 70px, 76px, 103px, 0.80, 1.00, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `76px`
- Card Padding: `19px`
- Element Gap: `19px`
- Radius: `default: 9.52381px, headings: 6.47619px, largeElements: 30.4762px`

## Component cues
- **Hero Headline**: Dominant page titles and impactful statements.
- **Ghost Action Link**: Secondary actions and navigations.
- **Feature Card**: Displaying work examples or service offerings.
- **Brand Logo Grid Item**: Displaying client logos or trusted partners.
- **Muted Body Text**: Descriptive paragraphs and detailed information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
