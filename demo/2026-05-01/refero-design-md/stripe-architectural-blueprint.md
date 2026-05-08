# Stripe - Refero Design MD

- Source: https://styles.refero.design/style/48e5de76-05d5-4c4e-a269-c7c245b291ec
- Original site: https://stripe.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Architectural blueprint on white marble.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#061b31` | neutral | Primary text, critical headings, icons, primary button text for ghost buttons |
| Slate Blue | `#50617a` | neutral | Secondary text, muted links, subtle borders, descriptive captions |
| Ghost Gray | `#64748d` | neutral | Tertiary text, placeholder text, inactive states, subtle dividers |
| Platinum White | `#ffffff` | neutral | Page backgrounds, card surfaces, primary button text against dark backgrounds |
| Porcelain White | `#f8fafd` | neutral | Secondary card surfaces, subtle background variations |
| Powder Blue | `#e5edf5` | neutral | Background for secondary sections, light card backgrounds |
| Stone Gray | `#d8d6df` | neutral | Horizontal rules, subtle borders, graphical elements |
| Deep Violet | `#533afd` | brand | Primary calls to action (buttons, links), active states, significant icons - establishes brand presence and emphasizes. |

```css
:root {
  --ref-midnight-ink: #061b31;
  --ref-slate-blue: #50617a;
  --ref-ghost-gray: #64748d;
  --ref-platinum-white: #ffffff;
  --ref-porcelain-white: #f8fafd;
  --ref-powder-blue: #e5edf5;
  --ref-stone-gray: #d8d6df;
}
```

## Typography direction
- Primary: **sohne-var**; substitute `system-ui, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `12px`
- Element gap: `8px`
- Radius: `{'tags': '4px', 'cards': '6px', 'images': '4px', 'inputs': '4px', 'buttons': '4px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
