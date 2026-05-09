# Studio Emmerer - Refero Design MD

- Source: https://styles.refero.design/style/670869ea-9576-4f9d-af3a-038910f8b9b8
- Original site: https://emmerer.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint, Night Mode

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Steel Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Preview White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-steel-gray: #999999;
  --ref-preview-white: #ffffff;
}
```

## Typography direction
- **NHaasGrotesk**: 400, 15px, 16px, 20px, 30px, 0.90, 1.16; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `5px`
- Radius: `none: 0px`

## Component cues
- **Navigation Link**: Interactive text link for site navigation.
- **Read More Link**: Text link for expanding content.
- **Project Table Row**: A single row within the tabular project listing.
- **Project List Item**: A single project entry in the main list. Behaves like a link.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
