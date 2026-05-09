# Dezeen - Refero Design MD

- Source: https://styles.refero.design/style/9e2dceb8-0c87-45db-8830-9df961b02b32
- Original site: https://dezeen.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on Crisp White. This metaphor evokes the precision and clarity of architectural drawings and the pristine nature of a fresh page.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f0f0f0` | neutral | Page background or card surface |
| Silver Ash | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Concrete Gray | `#757575` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#eaeaea` | neutral | Page background or card surface |
| Indigo Accent | `#556e9b` | brand | Action accent / signal color |
| Sunset Orange | `#ff7617` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-fog-gray: #f0f0f0;
  --ref-silver-ash: #d8d8d8;
  --ref-concrete-gray: #757575;
  --ref-soft-stone: #eaeaea;
  --ref-indigo-accent: #556e9b;
  --ref-sunset-orange: #ff7617;
}
```

## Typography direction
- **StandardCT**: 700, 19px, 27px, 40px, 0.95, 1.00, 1.10, 1.20, 1.25, 1.37, 1.38; substitute `Open Sans, Montserrat`.
- **Chronicle Text G1 A**: 400, 700, 14px, 16px, 1.23, 1.25, 1.29, 1.50; substitute `Georgia, Merriweather`.
- **Arial**: 400, 700, 13px, 14px, 16px, 1.00, 1.20, 1.29; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `9px`
- Page Max Width: `1212px`
- Radius: `cards: 0px, inputs: 0px, buttons: 0px, accentCircular: 100%`

## Component cues
- **Newsletter Signup Modal**: Reference component style.
- **Article Card List**: Reference component style.
- **Most Commented Sidebar Block**: Reference component style.
- **Circular Play Button**: Interaction
- **Underlined Text Button**: Navigation/Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
