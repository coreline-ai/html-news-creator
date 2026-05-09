# Windsurf - Refero Design MD

- Source: https://styles.refero.design/style/cfab7b43-ed24-41e9-9272-c858700b865b
- Original site: https://windsurf.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#011c42` | neutral | Primary text or dark surface |
| Arctic Mist | `#f8f1e5` | neutral | Page background or card surface |
| Platinum White | `#ffffff` | neutral | Page background or card surface |
| Slate Text | `#696962` | neutral | Border, muted text, or supporting surface |
| Ash Border | `#c0c1c6` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#0b100f` | neutral | Primary text or dark surface |
| Neon Cyan | `#34e8bb` | brand | Action accent / signal color |
| Electric Magenta | `#fb9ce5` | brand | Action accent / signal color |
| Plasma Pink Gradient | `#a95af8` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #011c42;
  --ref-arctic-mist: #f8f1e5;
  --ref-platinum-white: #ffffff;
  --ref-slate-text: #696962;
  --ref-ash-border: #c0c1c6;
  --ref-charcoal-black: #0b100f;
  --ref-neon-cyan: #34e8bb;
  --ref-electric-magenta: #fb9ce5;
}
```

## Typography direction
- **ui-sans-serif**: 400, 14px, 16px, 1.43, 1.5.
- **tomatoGrotesk**: 300, 400, 500, 40px, 48px, 64px, 72px, 96px, 1.00; substitute `system-ui`.
- **DM Sans**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 20px, 28px, 40px, 1.00, 1.30, 1.33, 1.50, 1.56, 1.71, 2.40; substitute `Arial, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `tags: 9999px, cards: 8px, buttons: 2px, navigation: 9999px`

## Component cues
- **Primary Action Button**: Calls to action that drive key user behavior (e.g., download, submit).
- **Ghost Accent Button**: Secondary actions or links that need visual emphasis without overwhelming the primary action.
- **Download Banner Button**: Prominent, often full-width or oversized, call to action in hero sections.
- **Content Card**: Container for feature descriptions, process steps, or grouped information.
- **Tag/Pill**: Small, distinct labels for categories, statuses, or new features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
