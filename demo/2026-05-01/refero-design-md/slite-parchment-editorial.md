# Slite - Refero Design MD

- Source: https://styles.refero.design/style/607c2098-bbbb-40bb-b23e-adf2b72c63dd
- Original site: https://slite.com
- Theme: `light`
- Recommended fit: **Editorial report / reading mode**

## North star
Warm parchment editorial desk - a workspace where knowledge feels handwritten, not enterprise-stamped.

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#f9efe4` | neutral | Primary page background and hero - the defining warm cream that separates Slite from the cold-white SaaS default |
| Vellum | `#fdf9f4` | neutral | Secondary surface, slightly cooler than Parchment - used for card interiors and section alternation |
| Chalk | `#fdfdfd` | neutral | Highest-surface level - card backgrounds, modal surfaces, product UI previews |
| Ink | `#3f434a` | neutral | Primary text across all contexts - body, headings, labels, icons |
| Graphite | `#2d2f34` | neutral | Primary filled button background and high-contrast UI elements |
| Slate | `#656565` | neutral | Secondary body text, subheadings, list items |
| Ash | `#9da3af` | neutral | Tertiary text, placeholder labels, muted metadata |
| Silver Mist | `#d9dde6` | neutral | Borders, dividers, card outlines |

```css
:root {
  --ref-parchment: #f9efe4;
  --ref-vellum: #fdf9f4;
  --ref-chalk: #fdfdfd;
  --ref-ink: #3f434a;
  --ref-graphite: #2d2f34;
  --ref-slate: #656565;
  --ref-ash: #9da3af;
}
```

## Typography direction
- Primary: **Garnett**; substitute `DM Sans or Fraunces for warmth, though neither replicates Garnett's geometric-e.`.
- Secondary/code: **UniversalSans**; substitute `Plus Jakarta Sans or Instrument Sans`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: `24-40px`
- Element gap: `8-16px`
- Radius: `{'cards': '12px', 'badges': '50px', 'modals': '24px', 'tooltips': '8px', 'buttons-pill': '42-50px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
