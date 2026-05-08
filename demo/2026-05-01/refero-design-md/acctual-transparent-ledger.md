# Acctual - Refero Design MD

- Source: https://styles.refero.design/style/aeefc294-a8f7-443d-b76a-538dddc29afe
- Original site: https://acctual.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Architectural blueprint on white marble. Precision, clarity, and transparent flow of information.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page backgrounds, card surfaces, primary text contrast. |
| Ink Black | `#000000` | neutral | Primary text, critical headings, strong brand emphasis. Its absolute blackness provides uncompromising legibility again. |
| Graphite | `#0f0f0f` | neutral | Prominent headings and body text, a slightly softer variant of Ink Black. |
| Deep Slate | `#1e1e1` | neutral | Secondary body text and descriptions, offering a subtle visual break from pure black without sacrificing contrast. |
| Ash Gray | `#8d8d8d` | neutral | Subtle text, metadata, disabled states. Provides gentle visual hierarchy. |
| Button Black | `#0d111b` | neutral | Primary action buttons, providing a solid, grounded feel against the white background. |
| Sky Teal | `#0098f2` | accent | Interactive elements, links, checkmarks, highlights - the sole vibrant accent for key user actions and positive indicat. |
| Hot Pink | `#f200ca` | brand | Decorative elements or specific brand highlights within icons, a secondary accent for visual interest. |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #0f0f0f;
  --ref-deep-slate: #1e1e1;
  --ref-ash-gray: #8d8d8d;
  --ref-button-black: #0d111b;
  --ref-sky-teal: #0098f2;
}
```

## Typography direction
- Primary: **sans-serif**; substitute `system-ui, 'Segoe UI', Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif`.
- Secondary/code: **Open Runde**; substitute `Inter`.

## Spacing / shape
- Section gap: `40-80px`
- Card padding: `24px`
- Element gap: `4-24px`
- Radius: `{'cards': '20px', 'badges': '1250px', 'images': '32px', 'buttons': '100px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
