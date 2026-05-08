# N8n - Refero Design MD

- Source: https://styles.refero.design/style/8601c8ef-e1ea-4186-adb2-6f9a74caf436
- Original site: https://n8n.io
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Workflow engine at midnight - the feeling of a live automation canvas running in a dark server room, lit by status indicators and data flows.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Base | `#0e0918` | neutral | Primary page background and hero section - the near-black violet creates depth without being neutral charcoal |
| Elevated Surface | `#1a1624` | neutral | Card backgrounds (rgb(26,22,36)) - one step above void, visible as panels |
| Deep Panel | `#1b1728` | neutral | Secondary card surface (rgb(27,23,40)) - close to Elevated Surface, used for 24px-radius feature cards |
| Muted Shell | `#2c2834` | neutral | Ghost button backgrounds - semi-transparent frosted layer over dark surfaces |
| Border Smoke | `#3e3a46` | neutral | Nav and container borders - low-contrast edge definition on dark surfaces |
| Ash Text | `#d1cece` | neutral | Primary body and UI text - warm-gray rather than pure white, reducing harshness against dark bg |
| Fog Text | `#9d9797` | neutral | Secondary body text, captions, de-emphasized labels |
| Silver Rail | `#e5e7eb` | neutral | Border lines across components and nav - light border on dark background creates fine hairline edges |

```css
:root {
  --ref-void-base: #0e0918;
  --ref-elevated-surface: #1a1624;
  --ref-deep-panel: #1b1728;
  --ref-muted-shell: #2c2834;
  --ref-border-smoke: #3e3a46;
  --ref-ash-text: #d1cece;
  --ref-fog-text: #9d9797;
}
```

## Typography direction
- Primary: **geomanist**; substitute `DM Sans, Inter (variable, set to weight 300 for display)`.
- Secondary/code: **geomanist-book**; substitute `DM Sans 500`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: ``
- Element gap: `16-24px`
- Radius: `{'cards': '16px', 'nodes': '12px', 'pills': '9999px', 'badges': '24px', 'inputs': '8px', 'buttons': '8px', 'cardsLarge': '24px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
