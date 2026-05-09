# V7labs - Refero Design MD

- Source: https://styles.refero.design/style/1ab79e76-a07f-48fd-8e93-0a0fee12abd7
- Original site: https://www.v7labs.com
- Theme: `mixed`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Slate Operational Hub

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f7f6f5` | neutral | Page background or card surface |
| Charcoal Surface | `#292929` | neutral | Primary text or dark surface |
| Deep Gray | `#1c1c1c` | neutral | Primary text or dark surface |
| Card Gray | `#484848` | neutral | Border, muted text, or supporting surface |
| Muted Ash | `#989897` | neutral | Border, muted text, or supporting surface |
| Link Ink | `#00104e` | brand | Action accent / signal color |
| Action Orange | `#ff683d` | brand | Action accent / signal color |
| Danger Red | `#ec580a` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-white-canvas: #ffffff;
  --ref-ghost-gray: #f7f6f5;
  --ref-charcoal-surface: #292929;
  --ref-deep-gray: #1c1c1c;
  --ref-card-gray: #484848;
  --ref-muted-ash: #989897;
  --ref-link-ink: #00104e;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Martina Plantijn Light**: 300, 400, 24px, 30px, 40px, 60px, 1.00, 1.07, 1.33, 1.40; substitute `serif`.
- **STK Bureau**: 400, 430, 9px, 10px, 12px, 14px, 16px, 18px, 21px, 24px, 1.00, 1.08, 1.11, 1.14, 1.17, 1.25, 1.40, 1.43, 1.56; substitute `Roboto`.

## Spacing / shape
- Section Gap: `39px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `tags: 40px, cards: 8px, forms: 160px, buttons: 160px, circular: 99px, secondaryElements: 2px`

## Component cues
- **Pill Button - Filled**: Primary action button with a rounded, pill-like shape.
- **Pill Button - Outlined**: Secondary action button with a distinct border accent.
- **White Text Button**: Light-themed or ghost button.
- **Standard Content Card**: Container for information modules within a dark section.
- **Compact Content Card**: Smaller variant of the content card for denser information display.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
