# Zed - Refero Design MD

- Source: https://styles.refero.design/style/a541789c-36e7-45a4-9d1d-143921a82a8b
- Original site: https://zed.dev
- Theme: `light`
- Recommended fit: **Admin operations / developer tooling**

## North star
precision-engineered dark mode text editor

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Blue | `#1348dc` | brand | Primary brand color for prominent headings, active links, and key interactive elements. Conveys a sense of depth and au. |
| Sky Blue | `#2b7fff` | brand | Illustrative fill and stroke color, often seen in abstract graphics or larger UI elements. Provides a brighter contrast. |
| Deep Harbor | `#464b57` | neutral | Dark primary text, button text on lighter backgrounds, and subtle borders. Forms the backbone of the typographic hierar. |
| Iceberg Blue | `#8ec5ff` | brand | Button states, secondary accents, and illustrative fills. Provides a lighter, more interactive shade of blue. |
| Pale Arctic | `#bedbff` | brand | Subtle borders and background tints for UI elements, offering a very light blue accent. |
| Cerulean Haze | `#74ade8` | brand | Secondary text in body, icons, and less prominent interactive states. A mid-tone blue that supports the primary brand c. |
| Carbon Gray | `#5d636f` | neutral | Subtle text, navigation items, and icon strokes. A darker gray for less prominent semantic information. |
| Pine Green | `#a1c181` | semantic | Semantic positive indicators and specific body text highlights. Infrequent use provides impact. |

```css
:root {
  --ref-midnight-blue: #1348dc;
  --ref-sky-blue: #2b7fff;
  --ref-deep-harbor: #464b57;
  --ref-iceberg-blue: #8ec5ff;
  --ref-pale-arctic: #bedbff;
  --ref-cerulean-haze: #74ade8;
  --ref-carbon-gray: #5d636f;
}
```

## Typography direction
- Primary: **Writer**; substitute `Inter`.
- Secondary/code: **Zed Mono**; substitute `IBM Plex Mono`.

## Spacing / shape
- Section gap: `64px`
- Card padding: ``
- Element gap: ``
- Radius: `{'cards': '2px', 'buttons': '2px', 'default': '2px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
