# Extract - Refero Design MD

- Source: https://styles.refero.design/style/c4e125b6-e3a3-4509-b06f-f0169216a394
- Original site: https://extract.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Editorial Canvas — grounded in bold typography and rich imagery.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#070707` | neutral | Primary text or dark surface |
| Accent Green | `#e7feda` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #070707;
  --ref-accent-green: #e7feda;
}
```

## Typography direction
- **Feature Deck**: 400, 44px, 104px, 1.25, 1.50; substitute `Anton`.
- **ABC Diatype**: 400, 700, 18px, 19px, 21px, 34px, 1.25, 1.40, 1.50, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `59px`
- Card Padding: `19px`
- Element Gap: `19px`
- Radius: `cards: 9.27273px, images: 9.27273px, inputs: 4.63636px, buttons: 4.63636px, navigation: 9.27273px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base for content.
- **Accent Green** `#e7feda`: Secondary background for distinct sections, often used in the footer.
- **Ink Black** `#070707`: Elevated surfaces, card backgrounds, and interactive elements. Provides strong contrast against the lighter canvases.

## Component cues
- **Solid Navigation Button**: Primary navigation item or active state.
- **Outlined Navigation Button**: Secondary navigation items or inactive states.
- **Project Card**: Container for individual project showcases.
- **Newsletter Input Field**: Email subscription input.
- **Newsletter Submit Button**: Call to action for newsletter subscription.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
