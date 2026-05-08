# OpenAI - Refero Design MD

- Source: https://styles.refero.design/style/dc541737-8bf2-4b31-b729-0352f696e82f
- Original site: https://openai.com
- Theme: `light`
- Recommended fit: **Editorial report / reading mode**

## North star
Blank page before the first word - a design that treats white space as the most powerful element, reserving all color for user-generated and editorial content.

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void | `#000000` | brand | Primary text, nav labels, filled CTA button background, icon fills - the singular chromatic anchor of the entire system |
| Fog Border | `#e5e7eb` | neutral | All dividing lines, card outlines, input borders, nav underlines - the lightest possible mark that still reads as a sep. |
| Chalk | `#f1f1f1` | neutral | Hover-state button backgrounds, subtle surface fills - one step off pure white without introducing warmth |
| Graphite | `#666666` | neutral | Supporting body text, icon strokes, secondary labels - muted but still readable |
| Ash | `#8f8f8f` | neutral | Tertiary labels, disabled states, fine-grain icon strokes |
| Canvas | `#ffffff` | neutral | Page background, card surfaces, all primary surfaces - absolute white with no warm or cool tint |

```css
:root {
  --ref-void: #000000;
  --ref-fog-border: #e5e7eb;
  --ref-chalk: #f1f1f1;
  --ref-graphite: #666666;
  --ref-ash: #8f8f8f;
  --ref-canvas: #ffffff;
}
```

## Typography direction
- Primary: **OpenAI Sans**; substitute `Inter, DM Sans`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `64-80px`
- Card padding: `32px`
- Element gap: `8-16px`
- Radius: `{'cards': '6.08px', 'chips': '9999px', 'input': '9999px', 'links': '4px', 'buttons': '9999px', 'softButton': '40px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
