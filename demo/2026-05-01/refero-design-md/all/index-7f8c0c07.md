# Index - Refero Design MD

- Source: https://styles.refero.design/style/7f8c0c07-86e9-4b7c-a042-a7563b169143
- Original site: https://index.app
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Grid Command

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#1c1c1c` | neutral | Primary text or dark surface |
| Alabaster | `#ffffff` | neutral | Page background or card surface |
| Medium Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#ababab` | neutral | Border, muted text, or supporting surface |
| Dark Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Soft Violet | `#7089ba` | accent | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-deep-graphite: #1c1c1c;
  --ref-alabaster: #ffffff;
  --ref-medium-gray: #808080;
  --ref-light-gray: #ababab;
  --ref-dark-gray: #4d4d4d;
  --ref-soft-violet: #7089ba;
}
```

## Typography direction
- **Raveo Variable**: 400, 500, 1000, 12px, 14px, 16px, 24px, 32px, 70px, 1.10, 1.20, 1.40, 1.50, 1.60, 1.70, 1.80; substitute `Inter Variable`.
- **Geist Mono**: 500, 9px, 12px, 1.60; substitute `JetBrains Mono`.
- **sans-serif**: 400, 12px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `max: 188px, fluid: 100px, small: 6px, larger: 20px, buttons: 50px`

## Component cues
- **Navigation Link**: Interactive text link in header, footer, and inline content.
- **Ghost Button**: Primary and secondary actions with minimal visual weight.
- **Early Preview Badge**: Small informational tag for new features.
- **Feature Card**: Container for showcasing product benefits or steps.
- **Interactive Icon Circle**: Used for 'get started' steps, showcasing a visual cue.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
