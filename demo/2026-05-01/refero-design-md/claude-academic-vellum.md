# Claude - Refero Design MD

- Source: https://styles.refero.design/style/47cb86b6-cb2d-41c8-94ba-8607cd7c41cd
- Original site: https://claude.ai
- Theme: `light`
- Recommended fit: **Editorial report / reading mode**

## North star
Academic Journal on Vellum - a soft, tactile precision.

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Vellum White | `#faf9f5` | neutral | Page backgrounds, card surfaces, navigation background. Provides a warm, inviting canvas. |
| Ink Black | `#141413` | neutral | Primary text, main headings, button text on light backgrounds. Creates high contrast and strong legibility. |
| Onyx | `#1f1e1d` | neutral | Borders, secondary text, darker accents within UI elements. Contributes to definition without harshness. |
| Graphite | `#3d3d3a` | neutral | Subtle text for secondary information like navigation links and body copy. Softer than Ink Black, but still highly read. |
| Dusty Gray | `#73726c` | neutral | Tertiary text, descriptive labels, and subtle UI elements. Less prominent for supporting content. |
| Stone | `#9c9a92` | neutral | Placeholder text, inactive states, faint iconography. Blends into the background more for assistive elements. |
| Parchment | `#dedcd1` | neutral | Subtle borders, dividers, subtle background shades. Offers a slight visual separation without drawing attention. |
| Snow White | `#ffffff` | neutral | Input fields, selected states, and very occasional text on dark backgrounds. A brighter white for interactive elements. |

```css
:root {
  --ref-vellum-white: #faf9f5;
  --ref-ink-black: #141413;
  --ref-onyx: #1f1e1d;
  --ref-graphite: #3d3d3a;
  --ref-dusty-gray: #73726c;
  --ref-stone: #9c9a92;
  --ref-parchment: #dedcd1;
}
```

## Typography direction
- Primary: **Anthropic Serif**; substitute `Lora`.
- Secondary/code: **Anthropic Serif**; substitute `Lora`.

## Spacing / shape
- Section gap: `32-40px`
- Card padding: `24px`
- Element gap: `8-24px`
- Radius: `{'cards': '9.6px', 'inputs': '9.6px', 'buttons': '9.6px', 'heroElements': '24px', 'jumboSeparators': '32px', 'largeContainers': '16px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
