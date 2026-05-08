# Slash - Refero Design MD

- Source: https://styles.refero.design/style/7c38e84b-aea0-4c8f-b3e9-60b994ee6c6b
- Original site: https://www.slash.com
- Theme: `dark`
- Recommended fit: **Data dashboard / source ledger**

## North star
Midnight Ledger, Obsidian Surfaces

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Page background, deepest surface level. Creates a sense of depth and seriousness |
| Obsidian Surface | `#030304` | neutral | Elevated card backgrounds, deeper shadows. A subtle lift from the main background |
| Charcoal Canvas | `#08080a` | neutral | Primary surface background, such as panels and main content areas |
| Pewter Accent | `#121317` | neutral | Subtle background for card, button, and other interactive elements, providing a soft lift |
| Slate Gray | `#1c1d22` | neutral | Component backgrounds, such as card details and selected states. Less saturated than Charcoal Canvas |
| Ash Text | `#5e616e` | neutral | Muted secondary text, placeholder text, subtle borders. For less prominent information |
| Stone Text | `#777a88` | neutral | Tertiary text, subtle icons, inactive navigation items. Lower hierarchy content |
| Silver Text | `#acafb9` | neutral | Helper text, slightly more prominent than Stone Text |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-obsidian-surface: #030304;
  --ref-charcoal-canvas: #08080a;
  --ref-pewter-accent: #121317;
  --ref-slate-gray: #1c1d22;
  --ref-ash-text: #5e616e;
  --ref-stone-text: #777a88;
}
```

## Typography direction
- Primary: **Inter**; substitute `system-ui`.
- Secondary/code: **Ivy Presto**; substitute `Playfair Display`.

## Spacing / shape
- Section gap: `160px`
- Card padding: `32px`
- Element gap: `6px`
- Radius: `{'md': '10px', 'sm': '2px', 'none': '0px', 'pill': '9999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
