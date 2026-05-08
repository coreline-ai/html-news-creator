# Superintelligence for work - Refero Design MD

- Source: https://styles.refero.design/style/1db2adc9-2f10-4f20-af1b-27fa4b25f729
- Original site: https://sanalabs.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
AI Blueprint on Polished Glass

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page backgrounds, card backgrounds, button backgrounds for ghost/outlined states, text on dark backgrounds |
| Ghost Fog | `#efefed` | neutral | Subtle background for UI sections and elevated cards, providing gentle visual separation from the main canvas |
| Midnight Ink | `#090909` | neutral | Primary text, headings, most iconography, borders, and input text - a core color for content and structure |
| Abyssal Black | `#000000` | neutral | Headings on light backgrounds, filled button backgrounds, and strong accent borders for interactive elements |
| Sterling Gray | `#d9d9d9` | neutral | Subtle borders, dividers, and background elements, especially in footers or less prominent UI areas |
| Action Blue | `#0057f3` | brand | Primary call-to-action buttons - a vivid, energetic blue that draws immediate attention |
| Warning Orange | `#ff5102` | accent | Orange action color for filled buttons, selected navigation states, and focused conversion moments |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-fog: #efefed;
  --ref-midnight-ink: #090909;
  --ref-abyssal-black: #000000;
  --ref-sterling-gray: #d9d9d9;
  --ref-action-blue: #0057f3;
  --ref-warning-orange: #ff5102;
}
```

## Typography direction
- Primary: **Sana Sans**; substitute `Inter`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `40px`
- Element gap: `16px`
- Radius: `{'cards': '16px', 'buttons': '32px', 'navigation': '6px', 'largeFeatures': '24px', 'specialButtons': '36px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
