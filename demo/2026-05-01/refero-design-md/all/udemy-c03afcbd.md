# Udemy - Refero Design MD

- Source: https://styles.refero.design/style/c03afcbd-96ed-4b7f-8d0a-277fc0042ba7
- Original site: https://www.udemy.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ordered campus noticeboard.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Background | `#e9eaf2` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#2a2b3f` | neutral | Primary text or dark surface |
| Dark Overlay | `#202230` | neutral | Primary text or dark surface |
| Dusty Blue | `#b7b9cd` | neutral | Action accent / signal color |
| Medium Gray | `#9194ac` | neutral | Border, muted text, or supporting surface |
| Muted Indigo | `#3d4055` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#595c73` | neutral | Border, muted text, or supporting surface |
| Subtle Dark Background | `#33364a` | neutral | Primary text or dark surface |
| Regal Violet | `#6d28d2` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-background: #e9eaf2;
  --ref-surface-white: #ffffff;
  --ref-deep-graphite: #2a2b3f;
  --ref-dark-overlay: #202230;
  --ref-dusty-blue: #b7b9cd;
  --ref-medium-gray: #9194ac;
  --ref-muted-indigo: #3d4055;
  --ref-steel-gray: #595c73;
}
```

## Typography direction
- **Udemy Sans**: 300, 400, 500, 700, 12px, 14px, 16px, 18px, 24px, 32px, 1.10, 1.20, 1.40, 1.50, 1.60; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 16px, cards: 8px, inputs: 4px, buttons: 1000px, general: 8px`

## Surface cues
- **Canvas Background** `#e9eaf2`: Base page background
- **Surface White** `#ffffff`: Primary content areas, cards
- **Muted Indigo** `#3d4055`: Elevated cards or distinct content groupings within dark sections
- **Dark Overlay** `#202230`: Sections with strong visual separation, often with reversed text color

## Component cues
- **Solid Button**: Primary action button, often for categories or filters.
- **Pill Button**: Filter or tag button, indicating selectable options without high emphasis.
- **Ghost Button (Text Primary)**: Secondary action or link-style button, often within cards or content areas.
- **Ghost Button (Text Accent)**: Subtle interactive element, typically used for navigation or in-context links.
- **Quote Card**: Testimonial or review card.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
