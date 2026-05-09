# Haley Park - Refero Design MD

- Source: https://styles.refero.design/style/c47654a9-7d7a-4b2c-8e0a-cd9296719c69
- Original site: https://haleys.design
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gothic manuscript on dark parchment

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canopy | `#143930` | neutral | Primary text or dark surface |
| Parchment White | `#f8f2de` | neutral | Page background or card surface |
| Moss Line | `#456859` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-forest-canopy: #143930;
  --ref-parchment-white: #f8f2de;
  --ref-moss-line: #456859;
}
```

## Typography direction
- **EditorialOld**: 200, 16px, 19px, 21px, 22px, 27px, 32px, 1.20, 1.30, 1.50; substitute `Lora`.
- **Wispy**: 100, 96px, 1.00; substitute `Recursive Sans`.
- **Old Standard TT**: 200, 13px, 16px, 1.50; substitute `Old Standard TT`.

## Spacing / shape
- Section Gap: `26px`
- Card Padding: `26px`
- Element Gap: `11px`
- Radius: `circle: 64px, default: 4.8px`

## Component cues
- **Ghost Navigation Link**: Header navigation items and project links
- **Project Card (Outlined)**: Containers for project listings, often appearing in grid layouts.
- **Section Divider with Text**: Visual separation between content sections, enhanced with centered text
- **Ornamental Icon**: Decorative crosses or geometric patterns

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
