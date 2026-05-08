# Titan - Refero Design MD

- Source: https://styles.refero.design/style/964b9215-396b-492c-abec-7bd778d7b1c9
- Original site: https://www.titan.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
monochrome financial ledger

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text, darkest surface. Creates stark contrast against lighter backgrounds |
| Canvas White | `#ffffff` | neutral | Page backgrounds, card surfaces, ghost button text. The primary backdrop for all content |
| Off-White Sage | `#f3efeb` | neutral | Subtle background for card variants and secondary sections, provides a soft, warm surface distinction |
| Faded Stone | `#e9eaeb` | neutral | Subtle borders and dividers, navigation backgrounds, a very light gray that acts as an almost invisible separator |
| Gunmetal Gray | `#615e5b` | neutral | Secondary text, muted helper text, and subtle icon details. Provides lower contrast for less prominent information |
| Soft Concrete | `#d8d3cc` | neutral | Subtle borders for ghost buttons and card containers, provides minimal visual separation |
| Action Black | `#000000` | brand | Primary button backgrounds, key interactive elements. The pure black stands out against the near-white canvas |
| Highlight Orange | `#ff9900` | accent | Decorative strokes and subtle highlights, often within SVG elements. A small splash of vivid color |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-canvas-white: #ffffff;
  --ref-off-white-sage: #f3efeb;
  --ref-faded-stone: #e9eaeb;
  --ref-gunmetal-gray: #615e5b;
  --ref-soft-concrete: #d8d3cc;
  --ref-action-black: #000000;
}
```

## Typography direction
- Primary: **Geist**; substitute `Inter`.
- Secondary/code: **Geist Mono**; substitute `JetBrains Mono`.

## Spacing / shape
- Section gap: `80px`
- Card padding: `28px`
- Element gap: `24px`
- Radius: `{'cards': '32px', 'small': '10px', 'medium': '20px', 'buttons': '160px', 'navigation': '140px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
