# Diogo Akio - Refero Design MD

- Source: https://styles.refero.design/style/55509c15-4b34-489e-9a81-bfa5468ffd37
- Original site: https://www.diogoakio.com.br
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shadowbox gallery display

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Slate Canvas | `#151515` | neutral | Primary text or dark surface |
| Deep Plum | `#1c2763` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-slate-canvas: #151515;
  --ref-deep-plum: #1c2763;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Helvetica Neue LT Pro**: 400, 16px, 34px, 1.20, 1.40; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `19px`
- Radius: `default: 0px`

## Component cues
- **Ghost Header CTA Button**: Primary call to action in the header.
- **Project Card**: Showcases individual portfolio projects.
- **Footer Detail List**: Provides secondary navigation and information at the page bottom.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
