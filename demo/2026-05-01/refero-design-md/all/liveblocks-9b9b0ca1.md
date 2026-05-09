# Liveblocks - Refero Design MD

- Source: https://styles.refero.design/style/9b9b0ca1-5067-4115-b62f-ee0e43d1f37f
- Original site: https://liveblocks.io
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data stream. Dark surfaces meet sharp textual readouts and subtle, glowing accents.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghostly White | `#ffffff` | neutral | Page background or card surface |
| Graphite Base | `#111111` | neutral | Primary text or dark surface |
| Ash Gray | `#918d8d` | neutral | Border, muted text, or supporting surface |
| Light Concrete | `#edecee` | neutral | Page background or card surface |
| Distant Gray | `#b7b4b4` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#635f5f` | neutral | Border, muted text, or supporting surface |
| Digital Blue | `#0090ff` | brand | Action accent / signal color |
| Cosmic Violet | `#9f8dfc` | accent | Action accent / signal color |
| System Teal | `#70e1c8` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghostly-white: #ffffff;
  --ref-graphite-base: #111111;
  --ref-ash-gray: #918d8d;
  --ref-light-concrete: #edecee;
  --ref-distant-gray: #b7b4b4;
  --ref-slate-text: #635f5f;
  --ref-digital-blue: #0090ff;
}
```

## Typography direction
- **suisse**: 400, 10px, 11px, 12px, 14px, 16px, 20px, 24px, 32px, 48px, 52px, 60px, 64px, 1.00, 1.05, 1.10, 1.20, 1.25, 1.33, 1.38, 1.43, 1.50; substitute `system-ui`.
- **JetBrains Mono**: 400, 500, 10px, 14px, 1.00, 1.43; substitute `monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `large: 12px, buttons: 6px, default: 4px, containers: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Trusted By Logo Strip**: Reference component style.
- **Comment Thread Card**: Reference component style.
- **Navigation Link**: Interactive elements in the header and footers.
- **Primary Ghost Button**: Secondary call-to-action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
