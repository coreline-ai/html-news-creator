# Ui - Refero Design MD

- Source: https://styles.refero.design/style/0fd67ec5-7e9c-4ca9-b368-5d9c7388477a
- Original site: https://ui.shadcn.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Monochromatic architectural blueprint - precise, functional forms on a stark, bright canvas.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background, primary card surfaces, popovers. The foundational bright base. |
| Ghost Gray | `#f2f2f2` | neutral | Secondary background for segmented sections or subtle card differentiation. Lighter than default background. |
| Subtle Ash | `#e5e5e5` | neutral | Border colors for inputs, cards, and dividers. Provides definition without harshness. |
| Midtone Gray | `#737373` | neutral | Muted text, placeholder text in inputs, secondary icons. Recedes into the background. |
| Rich Black | `#0a0a0a` | neutral | Primary text color for body copy, standard icons, badges with white text. High contrast for readability. |
| Deep Black | `#000000` | neutral | Headings, active state button backgrounds, highlighted text. The darkest tone for strong emphasis. |
| Callout Red | `#c22b10` | semantic | Destructive actions, error states. A muted, serious red. |
| Success Green | `#10c22b` | semantic | Success states, positive confirmations. A muted, serious green. |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #f2f2f2;
  --ref-subtle-ash: #e5e5e5;
  --ref-midtone-gray: #737373;
  --ref-rich-black: #0a0a0a;
  --ref-deep-black: #000000;
  --ref-callout-red: #c22b10;
}
```

## Typography direction
- Primary: **Geist**; substitute `Inter`.
- Secondary/code: **Geist Mono**; substitute `IBM Plex Mono`.

## Spacing / shape
- Section gap: `83px`
- Card padding: `16px`
- Element gap: `8px`
- Radius: `{'pill': '9999px', 'badge': '26px', 'cards': '14px', 'input': '10px', 'buttons': '10px', 'default': '10px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
