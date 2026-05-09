# Stellar - Refero Design MD

- Source: https://styles.refero.design/style/98a1ad40-90e2-4665-b49f-e5ffd4d4b90b
- Original site: https://www.stellar.work
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight canvas, violet beacon.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Stellar Black | `#171718` | neutral | Primary text or dark surface |
| Storm Gray | `#2c2c2e` | neutral | Primary text or dark surface |
| Ultraviolet | `#6a48f2` | brand | Action accent / signal color |
| Spectral White | `#f3f3f3` | neutral | Page background or card surface |
| Cloudburst | `#888888` | neutral | Border, muted text, or supporting surface |
| Lunar White | `#ffffff` | neutral | Page background or card surface |
| Glimmer White | `#e9e9e9` | neutral | Page background or card surface |
| Dusty Gray | `#dddddd` | neutral | Page background or card surface |
| Cosmic Dust | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-stellar-black: #171718;
  --ref-storm-gray: #2c2c2e;
  --ref-ultraviolet: #6a48f2;
  --ref-spectral-white: #f3f3f3;
  --ref-cloudburst: #888888;
  --ref-lunar-white: #ffffff;
  --ref-glimmer-white: #e9e9e9;
}
```

## Typography direction
- **Neue Montreal**: 400, 500, 14px, 15px, 16px, 18px, 19px, 21px, 22px, 40px, 70px, 72px, 104px, 1.00, 1.10, 1.20, 1.43, 1.50, 1.55; substitute `Inter`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 6px, buttons: 50px, default: 6px, circular: 100%, roundCards: 10px`

## Surface cues
- **Absolute Zero Canvas** `#000000`: Primary page background and deepest surface level.
- **Stellar Black Card** `#171718`: Slightly elevated card backgrounds, offering a subtle visual break from the canvas.
- **Storm Gray Input** `#2c2c2`: Elevated UI controls like input fields and ghost buttons, indicating interactivity against deeper surfaces.

## Component cues
- **Primary Action Button**: Calls to action, e.g., 'Reserve your sprint'.
- **Ghost Card Button**: Secondary action within card interfaces.
- **Informational Button**: Callouts or navigation within sections, e.g., 'Learn More'.
- **Content Card - Neutral**: Container for showcasing projects, designers, or information.
- **Content Card - Rounded**: Container for showcasing work examples.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
