# Freytag Anderson - Refero Design MD

- Source: https://styles.refero.design/style/2d4fc4ba-2ea4-465f-8644-f3ff5c6713a2
- Original site: https://www.freytaganderson.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black canvas, stark typography

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Dark | `#000000` | neutral | Primary text or dark surface |
| Canvas Light | `#fafafa` | neutral | Page background or card surface |
| Elevated Dark | `#1c1c1c` | neutral | Primary text or dark surface |
| Subtle Dark | `#141109` | neutral | Primary text or dark surface |
| Muted UI Gray | `#dcdcdc` | neutral | Page background or card surface |
| Warm Hint Gray | `#c2b5ae` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-dark: #000000;
  --ref-canvas-light: #fafafa;
  --ref-elevated-dark: #1c1c1c;
  --ref-subtle-dark: #141109;
  --ref-muted-ui-gray: #dcdcdc;
  --ref-warm-hint-gray: #c2b5ae;
}
```

## Typography direction
- **FAVORIT**: 300, 400, 15px, 17px, 41px, 1.00, 1.18, 1.20, 1.40, 1.70; substitute `Inter`.
- **Clarkson**: 300, 400, 17px, 1.40, 1.70; substitute `Open Sans`.
- **halyard-display**: 300, 15px, 17px, 1.20, 1.40; substitute `Roboto`.

## Spacing / shape
- Section Gap: `43px`
- Card Padding: `0px`
- Element Gap: `17px`
- Radius: `cards: 0px, buttons: 300px`

## Surface cues
- **Base Canvas** `#000000`: Dominant background for the entire page, providing a dark, immersive base.
- **Subtle Layer** `#1c1c1c`: Used for subtle background shifts to differentiate content sections without adding visual weight.
- **Highlight Surface** `#fafafa`: Used for reversed text elements, or very specific UI points when the content calls for a light treatment.

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying prominence through fill.
- **Ghost Button**: Secondary action or navigation element, minimal visual weight.
- **Feature Card**: Group related content without adding visual noise.
- **Text Link**: Interactive text for navigation or references.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
