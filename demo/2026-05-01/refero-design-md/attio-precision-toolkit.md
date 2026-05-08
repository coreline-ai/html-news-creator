# Attio - Refero Design MD

- Source: https://styles.refero.design/style/08c8700c-f278-42bc-812e-f60dc6ce996e
- Original site: https://attio.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Precision Digital Toolkit. A design system built on a foundation of high-contrast monochrome, where soft serif headlines provide a human touch to a clinical, tool-like interface.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White | `#ffffff` | neutral | Primary page background, text on dark surfaces |
| Ash | `#f3f4f6` | neutral | Subtle background panels, button pressed state |
| Stone | `#e4e7ec` | neutral | Light borders, dividers |
| Slate | `#d3d8df` | neutral | Default borders, inactive UI elements |
| Lead | `#b5bdc9` | neutral | Placeholder text, disabled text |
| Overcast | `#8f99a8` | neutral | Secondary body text, supporting labels |
| Metal | `#6f7988` | neutral | Tertiary body text, icons |
| Carbon | `#505967` | neutral | Icons, subtle interactive elements |

```css
:root {
  --ref-white: #ffffff;
  --ref-ash: #f3f4f6;
  --ref-stone: #e4e7ec;
  --ref-slate: #d3d8df;
  --ref-lead: #b5bdc9;
  --ref-overcast: #8f99a8;
  --ref-metal: #6f7988;
}
```

## Typography direction
- Primary: **Tiempos Text**; substitute `Newsreader, Lora`.
- Secondary/code: **Inter Display**; substitute `Inter`.

## Spacing / shape
- Section gap: `96px`
- Card padding: `16px`
- Element gap: `8px`
- Radius: `{'tabs': '0px', 'tags': '4px', 'cards': '8px', 'inputs': '7px', 'buttons': '10px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
