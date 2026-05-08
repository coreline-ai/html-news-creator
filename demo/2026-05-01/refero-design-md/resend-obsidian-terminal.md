# Resend - Refero Design MD

- Source: https://styles.refero.design/style/0d914ef0-fa84-4c60-a9aa-cef0b5eb6e5d
- Original site: https://resend.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Obsidian developer terminal - every surface reads like polished black glass under a focused beam of white type.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Page canvas, card backgrounds - the dominant surface across every section |
| Graphite Rail | `#292d30` | neutral | Component borders, dividers, image frames - hairline structural separation on black |
| Smoke | `#464a4d` | neutral | Subtle secondary borders and muted text-adjacent strokes |
| Ash | `#6c6c6c` | neutral | Tertiary text, badge labels, de-emphasized body content |
| Steel | `#6e727a` | neutral | Secondary body text, icon strokes at reduced opacity |
| Fog | `#a1a4a5` | neutral | Primary muted body text, icon fills, badge borders |
| Mist | `#abafb4` | neutral | Slightly brighter secondary UI text, active badge outlines |
| Frost | `#f0f0f0` | neutral | Primary content text - headings, body copy, nav labels - the single high-contrast text color on black |

```css
:root {
  --ref-void-black: #000000;
  --ref-graphite-rail: #292d30;
  --ref-smoke: #464a4d;
  --ref-ash: #6c6c6c;
  --ref-steel: #6e727a;
  --ref-fog: #a1a4a5;
  --ref-mist: #abafb4;
}
```

## Typography direction
- Primary: **Inter**; substitute `Inter (free via Google Fonts)`.
- Secondary/code: **Domaine**; substitute `DM Serif Display, Playfair Display`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: `32px`
- Element gap: `16px`
- Radius: `{'tags': '10px', 'cards': '16px', 'large': '24px', 'badges': '6px', 'modals': '16px', 'buttons': '6px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
