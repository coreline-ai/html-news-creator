# Studio Gruhl - Refero Design MD

- Source: https://styles.refero.design/style/9e3fde24-cc7d-4b96-a70a-7c172882aa8f
- Original site: https://www.studiogruhl.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Grid, Sharp Light

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#18181b` | neutral | Primary text or dark surface |
| Slate Surface | `#2e2e30` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Muted Gray | `#969696` | neutral | Border, muted text, or supporting surface |
| Shadow Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-charcoal: #18181b;
  --ref-slate-surface: #2e2e30;
  --ref-pure-white: #ffffff;
  --ref-muted-gray: #969696;
  --ref-shadow-ink: #000000;
}
```

## Typography direction
- **GreedStandard**: 400, 700, 10px, 15px, 16px, 80px, 1.00, 1.15, 1.20; substitute `Helvetica Neue`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 9px, buttons: 12px, general: 12px, navItems: 9999px`

## Surface cues
- **Midnight Charcoal Canvas** `#18181b`: The foundational background for the entire application, providing a deep, dark stage for content.
- **Slate Surface Panel** `#2e2e30`: Used for distinct interactive elements like cards, buttons, and navigation, offering a subtle visual lift from the canvas.

## Component cues
- **Primary Filled Button**: Main call-to-action button, dark background with white text.
- **Outlined Text Button**: Secondary action button, white text with a white border, no background fill.
- **Naked Text Button**: Minimalist button for pure textual actions, text only.
- **Transparent Project Card**: Card for displaying project previews without a distinct background, relying on content for definition.
- **Rounded Project Card**: Card for project previews with a subtle rounded corner, no distinct background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
