# customer.io - Refero Design MD

- Source: https://styles.refero.design/style/abbaa70a-5fe2-44a9-9c5f-272e68c450c3
- Original site: https://customer.io
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Architectural Blueprint on Frosted Glass

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#00262b` | neutral | Primary text, prominent headings, dark button backgrounds, navigation text. This near-black provides strong contrast ag. |
| Oceanic Deep | `#0b363b` | neutral | Secondary text, active navigation elements, button outlines, subtle borders. A deep, cool gray that maintains readabili. |
| Sky Mist | `#e0f4ff` | neutral | Decorative background accents, subtle borders on cards and images. A very light, cool gray with a hint of blue |
| Amber Pop | `#8b3911` | accent | Highlight text within body copy, decorative indicators. A vivid orange that draws attention to specific words |
| Indigo Pop | `#0a3890` | accent | Highlight text within body copy, decorative indicators. A vivid violet that draws attention to specific words |
| Slate Grille | `#354d51` | neutral | Muted text, less prominent body copy, icon fills. A medium-dark gray for secondary information |
| Stone Whisper | `#4f6466` | neutral | Subtle text for secondary buttons or helper text. A mid-tone gray that recedes |
| Ash Cloud | `#a1c2c6` | neutral | Lightest secondary text, faint borders, inactive states. A very light gray for tertiary information |

```css
:root {
  --ref-midnight-ink: #00262b;
  --ref-oceanic-deep: #0b363b;
  --ref-sky-mist: #e0f4ff;
  --ref-amber-pop: #8b3911;
  --ref-indigo-pop: #0a3890;
  --ref-slate-grille: #354d51;
  --ref-stone-whisper: #4f6466;
}
```

## Typography direction
- Primary: **saansFont**; substitute `Inter`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `96px`
- Card padding: `32px`
- Element gap: `8px`
- Radius: `{'images': '6px', 'buttons': '1.67772e+07px', 'default': '2px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
