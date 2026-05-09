# Dennis Snellenberg - Refero Design MD

- Source: https://styles.refero.design/style/28e8e762-8d8c-4e88-84ed-858f9917cb58
- Original site: https://dennissnellenberg.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
midnight command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1c1d20` | neutral | Primary text or dark surface |
| Frosted Glass | `#ffffff` | neutral | Page background or card surface |
| Neutral Stone | `#999d9e` | neutral | Border, muted text, or supporting surface |
| Graphite Shadow | `#494a4d` | neutral | Border, muted text, or supporting surface |
| Vivid Violet | `#455ce9` | brand | Action accent / signal color |
| Deep Violet | `#334bd3` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1c1d20;
  --ref-frosted-glass: #ffffff;
  --ref-neutral-stone: #999d9e;
  --ref-graphite-shadow: #494a4d;
  --ref-vivid-violet: #455ce9;
  --ref-deep-violet: #334bd3;
}
```

## Typography direction
- **Dennis Sans**: 450, 10px, 12px, 14px, 15px, 17px, 33px, 60px, 76px, 88px, 216px, 1.00, 1.06, 1.07, 1.20, 1.40, 1.45, 1.60, 1.66; substitute `Inter`.

## Spacing / shape
- Element Gap: `12px`
- Radius: `body: 10px, links: 36.72px`

## Surface cues
- **Page Base** `#1c1d20`: Primary background for the entire page, providing a foundational dark canvas.
- **Card Surface** `#494a4d`: Slightly elevated background for cards or distinct content blocks.
- **Accent Surface** `#334bd3`: A vivid violet background for interactive elements or highlighted cards.
- **Highlighted Accent Surface** `#455ce9`: A brighter vivid violet for primary interactive elements, standing out boldly.
- **Muted Background** `#999d9`: A lighter neutral background for specific sections or elements requiring less contrast.

## Component cues
- **Located Tag**: Informational tag showing location context.
- **Navigation Link**: Primary navigation item in headers and footers.
- **Circular Brand Card - Vivid Violet**: Highlighting specific project categories or services with brand color.
- **Circular Brand Card - Deep Violet**: Supporting brand elements with a darker variation of the accent.
- **Circular Neutral Card - Midnight Ink**: General purpose neutral card for categorization or grouping.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
