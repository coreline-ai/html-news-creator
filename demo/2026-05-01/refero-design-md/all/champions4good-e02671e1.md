# Champions4good - Refero Design MD

- Source: https://styles.refero.design/style/e02671e1-ba31-465f-bb7f-b124bf91ab5e
- Original site: https://www.champions4good.club
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric purple, condensed statements. A punchy, digital-neon aesthetic on a dark, rich canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Royal Plum | `#23002b` | brand | Action accent / signal color |
| Hot Pink | `#e894ff` | accent | Action accent / signal color |
| Neon Green | `#93ffe4` | accent | Action accent / signal color |
| Sunburst Orange | `#ffac47` | accent | Action accent / signal color |
| Forest Shard | `#002629` | brand | Action accent / signal color |
| Espresso Chip | `#291900` | brand | Action accent / signal color |
| Ink Black | `#121212` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Deep Plum | `#db99f7` | accent | Action accent / signal color |

```css
:root {
  --ref-royal-plum: #23002b;
  --ref-hot-pink: #e894ff;
  --ref-neon-green: #93ffe4;
  --ref-sunburst-orange: #ffac47;
  --ref-forest-shard: #002629;
  --ref-espresso-chip: #291900;
  --ref-ink-black: #121212;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Druk Condensed Super Desktop**: 400, 500, 24px, 29px, 32px, 43px, 44px, 151px, 187px, 317px, 0.78, 0.85, 1.00; substitute `Anton`.
- **Neue Montreal**: 400, 500, 600, 12px, 14px, 15px, 16px, 58px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.43; substitute `Inter`.
- **Arial**: 400, 14px, 1.43; substitute `Arial`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `cards: 14px, buttons: 0px, default: 6px`

## Component cues
- **Join CTA Button Group**: Reference component style.
- **Feature Cards — Triptych**: Reference component style.
- **Sound Toggle + Navigation Pills**: Reference component style.
- **Ghost Navigation Link**: Primary navigation links
- **Hero Text Button**: Call to action in hero

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
