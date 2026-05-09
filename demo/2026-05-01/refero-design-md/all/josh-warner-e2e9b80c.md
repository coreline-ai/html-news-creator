# Josh Warner - Refero Design MD

- Source: https://styles.refero.design/style/e2e9b80c-b548-4f86-a4d7-7a6b07d1c2e1
- Original site: https://www.joshwarner.design
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight gallery, sculpted light

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#0f0f0f` | neutral | Primary text or dark surface |
| Inky Void | `#000000` | neutral | Primary text or dark surface |
| Pure Canvas | `#f0f0f0` | neutral | Page background or card surface |
| Medium Gray | `#696969` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#b8b8b8` | neutral | Border, muted text, or supporting surface |
| Darkened Canvas | `#1a1a1a` | neutral | Primary text or dark surface |
| Shadow Base | `#080808` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-space: #0f0f0f;
  --ref-inky-void: #000000;
  --ref-pure-canvas: #f0f0f0;
  --ref-medium-gray: #696969;
  --ref-light-gray: #b8b8b8;
  --ref-darkened-canvas: #1a1a1a;
  --ref-shadow-base: #080808;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui, 'Helvetica Neue', Arial, sans-serif`.
- **Inter Display**: 400, 14px, 16px, 20px, 32px, 40px, 1.00, 1.20, 1.25, 1.43, 1.50, 1.56; substitute `'Inter', sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `14px`
- Element Gap: `10px`
- Radius: `tags: 40px, cards: 4px, icons: 12px, inputs: 8px, buttons: 100px`

## Surface cues
- **Main Canvas** `#0f0f0f`: Primary page background, base for content sections.
- **Footer Canvas** `#1a1a1a`: Dedicated background for footer sections, slightly darker for visual separation.

## Component cues
- **Ghost Header Button**: Navigation button, pill-shaped
- **Hire Me Button**: Primary action button, filled and subtly rounded
- **Avatar Button**: Profile or identity button
- **Project Card**: Item display in a grid, image-focused
- **Interactive Link**: Inline textual link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
