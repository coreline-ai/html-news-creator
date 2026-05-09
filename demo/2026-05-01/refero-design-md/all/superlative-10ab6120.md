# Superlative - Refero Design MD

- Source: https://styles.refero.design/style/10ab6120-3d03-48ff-aebe-0b4910edc046
- Original site: https://playsuperlative.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision instrument interface—white text glowing on a matte gray panel.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Superlative Black | `#141414` | neutral | Primary text or dark surface |
| Instrument Gray | `#232323` | neutral | Primary text or dark surface |
| Panel Gray | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Signal Orange | `#e66f27` | brand | Action accent / signal color |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Surface White | `#f6f4f2` | neutral | Page background or card surface |
| Divider Gray | `#e4e3e2` | neutral | Page background or card surface |
| Absolute Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-superlative-black: #141414;
  --ref-instrument-gray: #232323;
  --ref-panel-gray: #8c8c8c;
  --ref-signal-orange: #e66f27;
  --ref-ghost-white: #ffffff;
  --ref-surface-white: #f6f4f2;
  --ref-divider-gray: #e4e3e2;
  --ref-absolute-black: #000000;
}
```

## Typography direction
- **SL-Regular-Condensed**: 400, 15px, 23px, 90px, 1.00, 1.33; substitute `Bebas Neue`.
- **SL-Light**: 400, 25px, 90px, 1.00, 1.20; substitute `Open Sans Light`.
- **SL-Regular**: 400, 15px, 1.00; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `30px`
- Element Gap: `15px`
- Radius: `badges: 15px, buttons: 3px`

## Surface cues
- **Superlative Black Canvas** `#141414`: Dominant page background, providing a dark, immersive base for content.
- **Instrument Gray Panel** `#232323`: Used for background of content blocks within the main canvas, offering slight visual separation.
- **Surface White** `#f6f4f2`: Reserved for occasional use as a contrasting content block background, such as specific badges or info cards.

## Component cues
- **Ghost Primary Button**: Main call to action, outlining key interactive elements.
- **Ghost Secondary Button**: Secondary calls to action, maintaining visual weight with interaction.
- **Input Field**: User input areas for forms.
- **New Badge**: Highlighting new features or products.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
