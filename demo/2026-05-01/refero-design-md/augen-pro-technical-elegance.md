# Augen Pro - Refero Design MD

- Source: https://styles.refero.design/style/0f7da1b2-9d06-4ef5-b5a8-ef7f92e57ab2
- Original site: https://augen.pro
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Architectural Blueprint on White Marble. Every element is immaculately placed against a pristine, bright background, creating a sense of technical elegance.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0f1012` | neutral | Primary text, darkest UI elements, default borders. Provides sharp contrast against lighter backgrounds. |
| Ghost White | `#f2f2f4` | neutral | Dominant page and card backgrounds. Creates a luminous, expansive stage for content. |
| Canvas | `#fdfdfd` | neutral | Secondary background surfaces, slightly brighter than Ghost White, offering subtle layering. |
| Skyline Gray | `#868788` | neutral | Subtle background tones, offering a soft visual break without introducing strong chromaticism. |
| Slate Comment | `#8f8f8f` | neutral | Secondary text, button labels, and subtle UI strokes. Provides visual hierarchy without being muted. |
| Deep Graphite | `#020201` | neutral | Accented text elements, button states, and fine strokes. Offers the highest contrast. |
| Future Blue | `#0071e3` | accent | Interactive elements like links, buttons, and active states. Commands attention as the sole chromatic accent. |

```css
:root {
  --ref-midnight-ink: #0f1012;
  --ref-ghost-white: #f2f2f4;
  --ref-canvas: #fdfdfd;
  --ref-skyline-gray: #868788;
  --ref-slate-comment: #8f8f8f;
  --ref-deep-graphite: #020201;
  --ref-future-blue: #0071e3;
}
```

## Typography direction
- Primary: **PP Neue Montreal**; substitute `Inter, Arial`.
- Secondary/code: **PP Neue Montreal**; substitute `Inter, Arial`.

## Spacing / shape
- Section gap: `94px`
- Card padding: ``
- Element gap: `6px`
- Radius: `{'misc': '54px', 'buttons': '10px', 'pillButtons': '26px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
