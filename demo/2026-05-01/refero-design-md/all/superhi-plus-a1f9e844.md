# SuperHi Plus - Refero Design MD

- Source: https://styles.refero.design/style/a1f9e844-c4b6-4526-9cfc-81208c50aee1
- Original site: https://superhi.plus
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric Blue Canvas: crisp text, confident forms.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| SuperHi Blue | `#0033e5` | brand | Action accent / signal color |
| Canvas White | `#f0f7ff` | neutral | Page background or card surface |
| Action Highlight Blue | `#527ceb` | accent | Action accent / signal color |
| Text Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-superhi-blue: #0033e5;
  --ref-canvas-white: #f0f7ff;
  --ref-action-highlight-blue: #527ceb;
  --ref-text-black: #000000;
}
```

## Typography direction
- **Haas Grot Disp Web**: 400, 16px, 18px, 24px, 32px, 42px, 56px, 85px, 1.13, 1.14, 1.20, 1.25, 1.33, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `22-24px`
- Element Gap: `6-16px`
- Page Max Width: `60px`
- Radius: `cards: 16px, inputs: 2.4px, buttons: 16px, pillButtons: 72px, largeElements: 50px`

## Surface cues
- **SuperHi Blue Canvas** `#0033e5`: Primary background for the application and major sections.
- **Canvas White Panel** `#f0f7ff`: Elevated content areas, detail cards, and explanatory sections that contrast with the main blue canvas.

## Component cues
- **Ghost Navigation Button**: Navigation and secondary actions
- **Filled Primary Button**: Primary calls to action
- **Pill Primary Button**: Prominent, primary calls to action with extreme roundedness
- **Accent Filled Button (Inactive/Decorative)**: Decorative or inactive button style
- **Blue Information Card**: Information display or feature highlights

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
