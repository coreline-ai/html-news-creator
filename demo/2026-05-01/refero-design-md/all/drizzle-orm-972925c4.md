# Drizzle ORM - Refero Design MD

- Source: https://styles.refero.design/style/972925c4-0caa-4dc2-9c00-798b5be0ad70
- Original site: https://orm.drizzle.team
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
developer's spirited workbench

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Smoke Gray | `#e5e7eb` | neutral | Page background or card surface |
| Steel Gray | `#f6f6f7` | neutral | Page background or card surface |
| Ink Black | `#222222` | neutral | Primary text or dark surface |
| Charcoal Text | `#444444` | neutral | Border, muted text, or supporting surface |
| Stone Text | `#909090` | neutral | Border, muted text, or supporting surface |
| Deep Sea | `#282b3b` | brand | Action accent / signal color |
| Sky Blue | `#006be6` | brand | Action accent / signal color |
| Amethyst Accent | `#3e7ff0` | accent | Action accent / signal color |
| Action Green | `#4bb74b` | semantic | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-smoke-gray: #e5e7eb;
  --ref-steel-gray: #f6f6f7;
  --ref-ink-black: #222222;
  --ref-charcoal-text: #444444;
  --ref-stone-text: #909090;
  --ref-deep-sea: #282b3b;
  --ref-sky-blue: #006be6;
}
```

## Typography direction
- **ui-sans-serif**: 400, 500, 600, 700, 10px, 11px, 12px, 14px, 16px, 18px, 20px, 32px, 40px, 1.00, 1.17, 1.20, 1.42, 1.50; substitute `system-ui, sans-serif`.
- **FirstTimeWriting**: 600, 700, 14px, 16px, 20px, 30px, 1.50, 1.60; substitute `cursive, sans-serif`.
- **ui-monospace**: 400, 500, 12px, 16px, 1.00, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Element Gap: `8px`
- Radius: `cards: 8px, badges: 3px, images: 2px, inputs: 4px, buttons: 4px`

## Component cues
- **Quick Navigation Cards**: Reference component style.
- **Release Progress & Stats Block**: Reference component style.
- **Performance Benchmark Card**: Reference component style.
- **Primary Action Button**: Calls to action across the site.
- **Default Button**: Secondary actions, navigation links within content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
