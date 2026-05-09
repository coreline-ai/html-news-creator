# DNCO - Refero Design MD

- Source: https://styles.refero.design/style/c072c00a-ee7f-4160-bd06-645cca12f7a8
- Original site: https://dnco.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic exhibition space.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Concrete Gray | `#e5e7eb` | neutral | Page background or card surface |
| Muted Ash | `#a3a3a3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-concrete-gray: #e5e7eb;
  --ref-muted-ash: #a3a3a3;
}
```

## Typography direction
- **Neue Haas Unica Pro**: 400, 16px, 18px, 22px, 72px, 1.00, 1.25, 1.33, 1.50, 1.56; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `24px`
- Element Gap: `24px`
- Radius: `tags: 9999px, buttons: 9999px, interactiveElements: 9999px`

## Surface cues
- **Midnight Base** `#000000`: Primary background for hero sections and footer, creating a strong initial impression and grounding the page.
- **Canvas White Content** `#ffffff`: Dominant background for main content areas, providing a clean, bright canvas for text and imagery.
- **Concrete Gray Accent** `#e5e7eb`: Subtle background for specific UI elements or sections requiring slight differentiation from Canvas White, often also serving as borders.

## Component cues
- **Navigation Link**: Main navigation and footer links
- **Filter Button (Text Only)**: Category/filter selection
- **Outlined Filter Button**: Categorization or filtering, visually separating options
- **Body Text Link**: Contextual navigation or references within body content
- **Hero Headline**: Page-level and major section headlines

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
