# Fingerprint - Refero Design MD

- Source: https://styles.refero.design/style/da6ad92d-4f29-4f92-a59a-3a46295d0d1c
- Original site: https://fingerprint.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data Sheet Precision. A clean, well-organized technical document with key elements highlighted in a single, vivid accent.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafaf8` | neutral | Page background or card surface |
| Ink Black | `#141415` | neutral | Primary text or dark surface |
| Graphite | `#454542` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#f0f0ef` | neutral | Page background or card surface |
| Border Ash | `#e4e5e1` | neutral | Page background or card surface |
| Faded Stone | `#8c8c89` | neutral | Border, muted text, or supporting surface |
| Warm White | `#ffffff` | neutral | Page background or card surface |
| Accent Orange | `#f35b22` | brand | Action accent / signal color |
| Success Green | `#62b06d` | semantic | Action accent / signal color |
| Deep Teal | `#88d2c3` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fafaf8;
  --ref-ink-black: #141415;
  --ref-graphite: #454542;
  --ref-light-gray: #f0f0ef;
  --ref-border-ash: #e4e5e1;
  --ref-faded-stone: #8c8c89;
  --ref-warm-white: #ffffff;
  --ref-accent-orange: #f35b22;
}
```

## Typography direction
- **Inter**: 400, 10px, 11px, 12px, 13px, 14px, 16px, 1.4, 1.5, 1.6, 1.7; substitute `system-ui, sans-serif`.
- **Inter**: 600, 16px, 30px, 36px, 48px, 1.15, 1.22, 1.30; substitute `system-ui, sans-serif`.
- **JetBrains Mono**: 400, 10px, 11px, 12px, 13px, 14px, 1.45, 1.5, 1.57, 1.6; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1232px`
- Radius: `cards: 12px, buttons: 6px, default: 4px, modules: 12px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Visitor Data Console**: Reference component style.
- **Stats Block**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Ghost Button**: Alternative action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
