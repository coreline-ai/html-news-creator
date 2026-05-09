# Simon Liesinger - Refero Design MD

- Source: https://styles.refero.design/style/a90dbcb6-e42c-4992-a83b-94879699dd4f
- Original site: https://www.liesingers.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on warm grey

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#f2f2f2` | neutral | Page background or card surface |
| Midnight Graphite | `#181818` | neutral | Primary text or dark surface |
| Deep Ink | `#000000` | neutral | Primary text or dark surface |
| Muted Slate | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Navigation Ember | `#fc523b` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-fog: #f2f2f2;
  --ref-midnight-graphite: #181818;
  --ref-deep-ink: #000000;
  --ref-muted-slate: #6e6e6e;
  --ref-navigation-ember: #fc523b;
}
```

## Typography direction
- **Times**: 400, 10px, 1.20; substitute `serif`.
- **GaramondRg**: 400, 25px, 29px, 36px, 0.86, 1.00, 1.22, 1.28; substitute `Garamond`.
- **HelveticaRg**: 400, 12px, 0.83, 1.20, 1.67; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `160px`
- Card Padding: `30px`
- Element Gap: `10-40px`
- Radius: `default: 0px`

## Surface cues
- **Canvas Fog** `#f2f2f2`: Base page background, light sections, and default component surface.
- **Midnight Graphite** `#181818`: Footer background, distinct content blocks, and areas of higher visual prominence.

## Component cues
- **Navigation Link**: Primary site navigation links at the footer.
- **Contact Link**: Interactive contact information links.
- **Section Divider Panel**: Separating content sections and categories.
- **Work/Award List Item**: Displaying entries in lists of work or awards.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
