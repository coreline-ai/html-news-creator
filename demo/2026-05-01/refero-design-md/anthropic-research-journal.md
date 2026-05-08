# Anthropic - Refero Design MD

- Source: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
- Original site: https://anthropic.com
- Theme: `light`
- Recommended fit: **Editorial Report / Executive Brief**
- Priority: **P1**

## Why this fits html-news-creator
Best reading-mode reference for the final AI report: warm paper base, strong typography, minimal decoration, and research-institution tone.

## Apply to
- Long-form HTML report reading mode
- Executive/PDF brief typography
- Research and policy sections that need extra trust

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Slate Dark | `#141413` | neutral | Primary text, borders, nav items, icon fills, card backgrounds - the near-black that appears on both light and dark surfaces, making it function as both foreground and background |
| Ivory Light | `#faf9f5` | neutral | Page background, button fills, light surface base - the warm off-white that gives the site its parchment character instead of clinical white |
| Ivory Medium | `#f0eee6` | neutral | Nav backgrounds, secondary surface level, border highlights |
| Ivory Dark | `#e8e6dc` | neutral | Body text on dark backgrounds, dividers, subtle borders |
| Oat | `#e3dacc` | neutral | Tertiary surface backgrounds, warm mid-tone fills |
| Cloud Medium | `#b0aea5` | neutral | Disabled/muted borders, secondary interactive borders, subdued UI chrome |
| Cloud Light | `#d1cfc5` | neutral | Dividers, hairline borders, inactive states |
| Cloud Dark | `#87867f` | neutral | Secondary text, meta labels, timestamps |

```css
:root {
  --ref-slate-dark: #141413;
  --ref-ivory-light: #faf9f5;
  --ref-ivory-medium: #f0eee6;
  --ref-ivory-dark: #e8e6dc;
  --ref-oat: #e3dacc;
  --ref-cloud-medium: #b0aea5;
  --ref-cloud-light: #d1cfc5;
}
```

## Typography direction
- Primary: **Anthropic Sans**; substitute `Inter, DM Sans`.
- Secondary/code: **Anthropic Serif**; substitute `Playfair Display, Lora`.

## Spacing / shape
- Section gap: `61px`
- Card padding: `31px`
- Element gap: `8-16px`
- Radius: `{'cards': '8px', 'badges': '0px', 'panels': '16px', 'buttons': '0px', 'featuredCards': '24px'}`

## Agent notes
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- Keep the project content hierarchy first: section title, why it matters, source evidence, confidence, and image evidence.
