# Raycast - Refero Design MD

- Source: https://styles.refero.design/style/3b6a17f0-3bdf-418c-a95e-0b89e5a8b2f8
- Original site: https://raycast.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Obsidian command terminal - a near-black void where UI surfaces emerge like backlit glass panels, depth created by shadow layering rather than color contrast.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#040506` | neutral | Dominant page canvas and deepest shadow color - the ground state everything floats above |
| Deep Charcoal | `#07080a` | neutral | Primary card and section backgrounds; the first surface level above canvas |
| Graphite 700 | `#111214` | neutral | Secondary surface and elevated card backgrounds |
| Graphite 600 | `#1b1c1e` | neutral | Observed in other boxShadow, link boxShadow, badge backgroundColor. Extracted usage does not support a distinct primary. |
| Graphite 500 | `#363739` | neutral | Border color for dividers, shadow tones on elevated components |
| Graphite 400 | `#454647` | neutral | Subtle borders, muted button borders, body divider lines |
| Slate 300 | `#6a6b6c` | neutral | Secondary body text, icon fills, disabled states |
| Slate 200 | `#9c9c9d` | neutral | Tertiary text, muted links, placeholder-level labels |

```css
:root {
  --ref-void-black: #040506;
  --ref-deep-charcoal: #07080a;
  --ref-graphite-700: #111214;
  --ref-graphite-600: #1b1c1e;
  --ref-graphite-500: #363739;
  --ref-graphite-400: #454647;
  --ref-slate-300: #6a6b6c;
}
```

## Typography direction
- Primary: **Inter**; substitute `Inter (Google Fonts) - identical; this is the Google-hosted version`.
- Secondary/code: **GeistMono**; substitute `JetBrains Mono or IBM Plex Mono`.

## Spacing / shape
- Section gap: `80px`
- Card padding: `24px`
- Element gap: `15px`
- Radius: `{'cards': '11px', 'icons': '99999px', 'badges': '6px', 'inputs': '8px', 'modals': '16px', 'buttons': '8px', 'cardLarge': '20px', 'buttonPill': '86px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
