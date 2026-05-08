# Sociotype - Refero Design MD

- Source: https://styles.refero.design/style/973332dc-4e10-4e90-85d8-3bce9c3cd3ed
- Original site: https://socio-type.com
- Theme: `light`
- Recommended fit: **Editorial report / reading mode**

## North star
Editorial White Canvas

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page backgrounds, card surfaces, primary text on dark hero sections |
| Ink Black | `#000000` | neutral | Primary text, borders, active states for ghost buttons and navigation, accent markings |
| Medium Gray | `#818181` | neutral | Muted text, secondary information, placeholder text, inactive link borders |
| Light Gray | `#d6d6d6` | neutral | Subtle dividers, borders between content sections |
| Faded Gray | `#9d9d9d` | neutral | Tertiary text, list item borders |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-medium-gray: #818181;
  --ref-light-gray: #d6d6d6;
  --ref-faded-gray: #9d9d9d;
}
```

## Typography direction
- Primary: **Main Onsite**; substitute `system-ui`.
- Secondary/code: **Onsite**; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section gap: `120px`
- Card padding: `0px`
- Element gap: `12px`
- Radius: `{'none': '0px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
