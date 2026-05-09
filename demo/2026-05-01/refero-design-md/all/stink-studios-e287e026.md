# Stink Studios - Refero Design MD

- Source: https://styles.refero.design/style/e287e026-3433-4a1d-9b23-9a65f8b9c138
- Original site: https://www.stinkstudios.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black canvas, stark typography

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Deep Charcoal | `#050505` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-deep-charcoal: #050505;
}
```

## Typography direction
- **Helvetica**: 300, 400, 700, 16px, 19px, 23px, 52px, 0.90, 1.00, 1.15, 1.30; substitute `Arial`.
- **Times New Roman**: 400, 60px, 1.00; substitute `serif`.
- **Courier New**: 400, 14px, 1.43; substitute `monospace`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `16px`
- Element Gap: `20px`
- Radius: `inputs: 10px, formElements: 10px`

## Component cues
- **Ghost Button (Text)**: Interactive element, navigation links
- **Ghost Button (Outlined)**: Interactive element, navigation links
- **Input Field**: Form input elements
- **Minimal Badge**: Categorization and tagging

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
