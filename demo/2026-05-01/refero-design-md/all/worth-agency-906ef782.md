# Worth Agency - Refero Design MD

- Source: https://styles.refero.design/style/906ef782-4be7-45ee-9800-0514d46e7518
- Original site: https://worth.agency
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant canvas, bold statements.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f9f9f9` | neutral | Page background or card surface |
| Midnight Text | `#282828` | neutral | Primary text or dark surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Blush Pink | `#f8d4d4` | accent | Action accent / signal color |
| Zest Orange | `#eb4726` | brand | Action accent / signal color |
| Muted Sage | `#d2fdd1` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f9f9f9;
  --ref-midnight-text: #282828;
  --ref-pitch-black: #000000;
  --ref-blush-pink: #f8d4d4;
  --ref-zest-orange: #eb4726;
  --ref-muted-sage: #d2fdd1;
}
```

## Typography direction
- **-apple-system**: 400, 16px, 1.00; substitute `system-ui`.
- **custom_47163**: 400, 500, 600, 16px, 22px, 28px, 42px, 52px, 1.00, 1.14, 1.27, 1.29, 1.31, 1.33, 1.44, 1.45, 1.50, 2.50; substitute `Poppins, Montserrat`.
- **custom_47178**: 400, 400px, 0.75; substitute `Bebas Neue, Impact`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 16px, large: 30px, small: 12px, default: 20px`

## Component cues
- **Primary Heading Display**: Large, eye-catching text for hero sections.
- **Body Text**: Standard paragraph text.
- **Accent Link**: Interactive text links for navigation and calls to action.
- **Navigation Tag**: Small, rounded tags for categorical navigation or labels.
- **Content Card - Default White**: Standard content containers for features or portfolio items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
