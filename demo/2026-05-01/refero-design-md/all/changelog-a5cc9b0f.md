# Changelog - Refero Design MD

- Source: https://styles.refero.design/style/a5cc9b0f-d274-458a-b990-d18482b70838
- Original site: https://linear.app/changelog
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center behind frosted glass.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Black | `#08090a` | neutral | Primary text or dark surface |
| Surface Dark | `#141516` | neutral | Primary text or dark surface |
| Line Graphite | `#34343a` | neutral | Primary text or dark surface |
| Deep Charcoal | `#1c1c1f` | neutral | Primary text or dark surface |
| Border Carbon | `#23252a` | neutral | Primary text or dark surface |
| Border Ash | `#2d2e31` | neutral | Primary text or dark surface |
| Text Primary | `#f7f8f8` | neutral | Page background or card surface |
| Text Secondary | `#d0d6e0` | neutral | Border, muted text, or supporting surface |
| Text Muted | `#8a8f98` | neutral | Border, muted text, or supporting surface |
| Highlight Fog | `#e4e5e9` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-black: #08090a;
  --ref-surface-dark: #141516;
  --ref-line-graphite: #34343a;
  --ref-deep-charcoal: #1c1c1f;
  --ref-border-carbon: #23252a;
  --ref-border-ash: #2d2e31;
  --ref-text-primary: #f7f8f8;
  --ref-text-secondary: #d0d6e0;
}
```

## Typography direction
- **Inter Variable**: 400, 500, 510, 590, 12px, 13px, 14px, 15px, 16px, 17px, 24px, 32px, 48px, 1.00, 1.13, 1.20, 1.33, 1.40, 1.50, 1.60, 2.46, 2.67, 2.86; substitute `Inter`.
- **Berkeley Mono**: 400, 590, 15px, 21px, 1.30; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 8px, search: 100px, buttons: 9999px, interactive: 4.46px`

## Surface cues
- **Canvas Black** `#08090a`: Dominant page background, providing the base dark theme.
- **Surface Dark** `#1c1c1f`: Slightly elevated component backgrounds, such as the search input or interactive elements on hover.
- **Interactive Surface** `#141516`: Backgrounds for ghost buttons, tags, or other active interactive components, offering a minimal step up from the base canvas.

## Component cues
- **Text Link**: Interactive text, navigation items.
- **Ghost Button (Primary)**: Primary Call to Action, outlines interactiveness without filling.
- **Ghost Button (Secondary)**: Secondary actions that need less visual emphasis.
- **Filled Button (Compact)**: Small, contained action buttons.
- **Search Input**: Input elements for search functionality.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
