# Getclockwise - Refero Design MD

- Source: https://styles.refero.design/style/6024d069-8a74-4534-917f-5f5b11224cc5
- Original site: https://www.getclockwise.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Evergreen clarity on a clean slate

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fdf9f7` | neutral | Page background or card surface |
| Midnight Pine | `#003f2e` | brand | Action accent / signal color |
| Forest Link | `#039861` | accent | Action accent / signal color |
| Slate Text | `#333333` | neutral | Primary text or dark surface |
| Ash Gray | `#6e7673` | neutral | Border, muted text, or supporting surface |
| Steel Border | `#a6a6a6` | neutral | Border, muted text, or supporting surface |
| Light Gray Border | `#d6d6d6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fdf9f7;
  --ref-midnight-pine: #003f2e;
  --ref-forest-link: #039861;
  --ref-slate-text: #333333;
  --ref-ash-gray: #6e7673;
  --ref-steel-border: #a6a6a6;
  --ref-light-gray-border: #d6d6d6;
}
```

## Typography direction
- **PP Mori**: 600, 700, 23px, 52px, 64px, 66px, 0.95, 1.00, 1.10, 1.20; substitute `Montserrat`.
- **Inter**: 400, 500, 700, 16px, 18px, 20px, 23px, 24px, 1.30, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `soft: 800px, circular: 9999px`

## Surface cues
- **Canvas White** `#fdf9f7`: Primary background for the entire page, providing a spacious, light base.

## Component cues
- **Primary Headline**: Dominant page titles and hero content.
- **Section Heading**: Titles for major content sections, establishing hierarchy.
- **Body Text Paragraph**: Standard paragraph content for readability.
- **Muted Subheading**: Descriptive text under headlines or for secondary information.
- **Link Text**: Hyperlinks within body copy or navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
