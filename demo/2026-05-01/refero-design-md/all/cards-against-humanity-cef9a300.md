# Cards Against Humanity - Refero Design MD

- Source: https://styles.refero.design/style/cef9a300-8513-46c2-9c2c-c0016e5a5d30
- Original site: https://www.climatecatastrophepack.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Irreverent, Urgent Distress: High-contrast black and off-white with a jarring red accent, like a bold, distressed propaganda poster.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Catastrophe Red | `#ff4034` | brand | Action accent / signal color |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Aged Paper | `#ebe4d8` | neutral | Page background or card surface |
| Charcoal Haze | `#c3bdb3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-catastrophe-red: #ff4034;
  --ref-pitch-black: #000000;
  --ref-aged-paper: #ebe4d8;
  --ref-charcoal-haze: #c3bdb3;
}
```

## Typography direction
- **Spektra**: 400, 32px, 40px, 100px, 202px, 0.82, 0.88, 1.00, 2.00; substitute `Abril Fatface, or Public Sans Black`.
- **Helvetica Neue LT**: 400, 800, 14px, 16px, 28px, 30px, 1.27, 1.29, 1.50; substitute `Arial, or Inter`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 2520px, inputs: 10px, buttons: 80px`

## Component cues
- **Rounded Primary Button**: Call to action
- **Elongated Primary Button**: Large call to action
- **Pill Outline Button**: Subtle action
- **Circular Card**: Decorative content container
- **Input Field**: User entry field

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
