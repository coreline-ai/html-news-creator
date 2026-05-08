# Column - Refero Design MD

- Source: https://styles.refero.design/style/a76ec6ba-20b3-495c-9d89-1e58281e79e7
- Original site: https://column.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Architectural blueprint on white marble. Subtle background patterns convey structure beneath a pristine, luminous surface, punctuated by precise, high-contrast markers.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Blue | `#011821` | neutral | Primary text color for headings and body copy, grounding the design. |
| Code Black | `#000000` | neutral | Used for critical text elements and strong outlines, providing maximum contrast and emphasis. |
| Ghost White | `#ffffff` | neutral | Primary background for pages and cards, fostering a sense of openness and purity. |
| Fog Gray | `#f6f6f8` | neutral | Secondary background for sections and subtle content groupings, almost imperceptibly off-white to provide visual separa. |
| Steel Gray | `#e3e4e8` | neutral | Subtle borders and separators, defining boundaries without starkness. |
| Charcoal Text | `#232730` | neutral | Text on lighter backgrounds for softer contrast than pure black, often used in navigation and body text. |
| Slate Text | `#7c7f88` | neutral | Contextual body text and secondary labels, offering readability without competing with primary elements. |
| Graphite | `#12161` | neutral | Darker shades for text and icons, particularly on hero sections, for depth. |

```css
:root {
  --ref-ink-blue: #011821;
  --ref-code-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-fog-gray: #f6f6f8;
  --ref-steel-gray: #e3e4e8;
  --ref-charcoal-text: #232730;
  --ref-slate-text: #7c7f88;
}
```

## Typography direction
- Primary: **SuisseIntl**; substitute `Inter`.
- Secondary/code: **SFMono**; substitute `IBM Plex Mono`.

## Spacing / shape
- Section gap: `48px`
- Card padding: ``
- Element gap: ``
- Radius: `{'cards': '8px', 'subtle': '2px', 'buttons': '8px', 'default': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
