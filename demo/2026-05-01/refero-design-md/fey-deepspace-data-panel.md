# Fey - Refero Design MD

- Source: https://styles.refero.design/style/733e6475-892a-4138-8835-bf40344df317
- Original site: https://feyapp.com
- Theme: `dark`
- Recommended fit: **Data dashboard / source ledger**

## North star
Deep-space observatory control panel. Functionality, precision, and high-contrast data visualization on a near-black canvas.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0b0b0b` | neutral | Major surface backgrounds, card bases. |
| Obsidian Deep | `#131313` | neutral | Elevated card backgrounds, modal backdrops, adding subtle surface differentiation. |
| Coal Dust | `#191919` | neutral | Accent backgrounds, subtle dividers. |
| Slate Text | `#868f97` | neutral | Secondary body text, disabled states, iconography. |
| Ash Gray | `#999999` | neutral | Tertiary text, subtle descriptions. |
| Silver Accents | `#cccccc` | neutral | Subtle interactive elements, subtle outlines. |
| Light Smoke | `#e6e6e6` | neutral | Near-white elements in dark mode, button text for dark buttons. |
| Pure White | `#ffffff` | neutral | Primary text, prominent iconography, active states, key data readouts. |

```css
:root {
  --ref-midnight-ink: #0b0b0b;
  --ref-obsidian-deep: #131313;
  --ref-coal-dust: #191919;
  --ref-slate-text: #868f97;
  --ref-ash-gray: #999999;
  --ref-silver-accents: #cccccc;
  --ref-light-smoke: #e6e6e6;
}
```

## Typography direction
- Primary: **calibre**; substitute `Inter, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: ``
- Card padding: ``
- Element gap: ``
- Radius: `{'cards': '16px', 'general': '10px', 'input-sm': '6px', 'buttons-pill': '99px', 'buttons-square': '6px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
