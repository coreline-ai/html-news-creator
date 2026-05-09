# Kinfolk - Refero Design MD

- Source: https://styles.refero.design/style/ac9b040e-36aa-4881-ada5-72d4744947a4
- Original site: https://www.kinfolk.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Literary magazine, minimal frames

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Paper Gray | `#dbded5` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-paper-gray: #dbded5;
}
```

## Typography direction
- **Kinfolk-Serif-Text**: 400, 15px, 20px, 1.25, 1.33, 1.50; substitute `Lora`.
- **Kinfolk-Serif-Deck**: 400, 25px, 32px, 50px, 60px, 1.00, 1.04, 1.16, 1.19; substitute `Playfair Display`.
- **Kinfolk-Sans**: 400, 13px, 15px, 16px, 20px, 25px, 1.16, 1.31, 1.33, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `links: 2px, default: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for all content.
- **Paper Gray** `#dbded5`: Subtle background for specific sections or UI elements, providing minimal visual separation.
- **Ink Black** `#000000`: Background for footer or full-width feature sections, creating strong contrast and visual anchors.

## Component cues
- **Ghost Button**: Minimal interactive elements with a strong border, common for secondary actions.
- **Outlined Button**: General purpose buttons for secondary actions or links, maintaining a light footprint.
- **Filled Button**: Primary calls to action, providing high contrast and visual weight.
- **Content Card**: Displaying articles or features with a focus on imagery and text.
- **Input Field**: Standard text input fields, visually minimal.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
