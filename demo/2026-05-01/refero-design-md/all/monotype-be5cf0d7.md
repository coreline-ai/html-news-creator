# Monotype. - Refero Design MD

- Source: https://styles.refero.design/style/be5cf0d7-fc29-4b7f-bf86-f87185b122fc
- Original site: https://variable-fonts.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type Foundry Blueprint: precision on a clean canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#1e242c` | neutral | Primary text or dark surface |
| Ocean Blue | `#1a73e8` | brand | Action accent / signal color |
| Pewter Slate | `#576579` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Light Fog | `#e7eaee` | neutral | Page background or card surface |
| Silver Dust | `#cfd5dd` | neutral | Border, muted text, or supporting surface |
| Ash Grey | `#dbdfe5` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-graphite: #1e242c;
  --ref-ocean-blue: #1a73e8;
  --ref-pewter-slate: #576579;
  --ref-pure-white: #ffffff;
  --ref-light-fog: #e7eaee;
  --ref-silver-dust: #cfd5dd;
  --ref-ash-grey: #dbdfe5;
}
```

## Typography direction
- **sans-serif**: 400, 16px, 1.2.
- **HelveticaNowMTTextRegular**: 400, 13px, 14px, 16px, 1.20, 1.23, 1.38, 1.50; substitute `Arial`.
- **HelveticaNowMTTextBold**: 400, 13px, 16px, 1.23, 1.50; substitute `Arial Bold`.

## Spacing / shape
- Section Gap: `104px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 8px, images: 16px, buttons: 8px`

## Surface cues
- **Page Canvas** `#ffffff`: The primary background for all page content.
- **Card Surface** `#ffffff`: Background for content cards, visually distinct by its subtle shadow and border.

## Component cues
- **Primary Action Button**: Main call to action.
- **Navigation Button (Dark)**: Primary navigation item, especially in header.
- **Ghost Button (Muted)**: Secondary or auxiliary actions, often text-only.
- **Ghost Button (Dark)**: Text-based navigation or subtle interactive elements.
- **Resource Card**: Content presentation for articles and resources.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
