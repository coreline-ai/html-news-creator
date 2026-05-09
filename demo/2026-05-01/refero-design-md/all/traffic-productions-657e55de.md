# Traffic Productions - Refero Design MD

- Source: https://styles.refero.design/style/657e55de-8cff-4d24-9a4e-17d3b7593a55
- Original site: https://traffic.productions
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial Print Workshop: stark black, off-white, and sharp yellow accents on bold, condensed type.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#151515` | neutral | Primary text or dark surface |
| Canvas White | `#f3f3f3` | neutral | Page background or card surface |
| Highlight Yellow | `#fff824` | brand | Action accent / signal color |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Faded Gray | `#e5e5e5` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #151515;
  --ref-canvas-white: #f3f3f3;
  --ref-highlight-yellow: #fff824;
  --ref-pure-black: #000000;
  --ref-faded-gray: #e5e5e5;
}
```

## Typography direction
- **Suisse**: 400, 700, 12px, 18px, 30px, 54px, 84px, 108px, 0.89, 0.93, 0.96, 1.00, 1.17; substitute `Open Sans Condensed / Source Sans 3 (condensed weights)`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `9px`
- Element Gap: `4px`
- Radius: `buttons: 9999px, default: 0px`

## Component cues
- **Cookie Bar**: Reference component style.
- **About Section — Non-Agency Offer**: Reference component style.
- **Work Card — Project Listing**: Reference component style.
- **Text Link Button**: Basic navigation and call to action.
- **Pill Button**: Primary action button, standing out with its distinctive shape.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
