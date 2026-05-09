# PostHog - Refero Design MD

- Source: https://styles.refero.design/style/56cd3725-3ff0-459e-894d-5da58d1fc549
- Original site: https://posthog.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Workbench with playful tools. A clean, light canvas anchored by a single vibrant accent color.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Canvas Sand | `#eeefe9` | neutral | Page background or card surface |
| Pale Granite | `#e5e7e0` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Black | `#111827` | neutral | Primary text or dark surface |
| Graphite Grey | `#374151` | neutral | Border, muted text, or supporting surface |
| Faded Grey | `#4d4f46` | neutral | Border, muted text, or supporting surface |
| Warm Gray Tint | `#e1d7c2` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#2f80fa` | brand | Action accent / signal color |
| Marigold Yellow | `#f1a82c` | brand | Action accent / signal color |

```css
:root {
  --ref-surface-white: #ffffff;
  --ref-canvas-sand: #eeefe9;
  --ref-pale-granite: #e5e7e0;
  --ref-ink-black: #000000;
  --ref-charcoal-black: #111827;
  --ref-graphite-grey: #374151;
  --ref-faded-grey: #4d4f46;
  --ref-warm-gray-tint: #e1d7c2;
}
```

## Typography direction
- **IBM Plex Sans Variable**: 400, 500, 600, 700, 800, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 20px, 21px, 24px, 36px, 1.00, 1.25, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.71; substitute `system-ui, sans-serif`.
- **ui-monospace**: 400, 14px, 1.43; substitute `monospace`.
- **Source Code Pro**: 500, 14px, 1.43; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Element Gap: `8px`
- Page Max Width: `958px`
- Radius: `pills: 9999px, accent: 8px, buttons: 4px, default: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Tab Bar**: Reference component style.
- **Sidebar Navigation Links**: Reference component style.
- **Primary CTA Button**: Main call-to-action
- **Ghost Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
