# Readwise - Refero Design MD

- Source: https://styles.refero.design/style/34c8dbee-f5d9-4495-a0e0-a25c6ca4b95b
- Original site: https://readwise.io
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Scholarly Workspace Blueprint. It feels like an organized desk with a clear task list.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1f1f1f` | neutral | Primary text or dark surface |
| Page Canvas | `#ffffff` | neutral | Page background or card surface |
| Ash Cloud | `#f1f5f8` | neutral | Page background or card surface |
| Highlight Yellow | `#fff7ca` | accent | Action accent / signal color |
| Action Blue | `#478cd0` | brand | Action accent / signal color |
| Status Orange | `#fb9100` | accent | Action accent / signal color |
| Sky Gradient | `#7496f7` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1f1f1f;
  --ref-page-canvas: #ffffff;
  --ref-ash-cloud: #f1f5f8;
  --ref-highlight-yellow: #fff7ca;
  --ref-action-blue: #478cd0;
  --ref-status-orange: #fb9100;
  --ref-sky-gradient: #7496f7;
}
```

## Typography direction
- **Mulish**: 400, 600, 700, 800, 11px, 14px, 16px, 18px, 22px, 1.09, 1.25, 1.50; substitute `system-ui, sans-serif`.
- **Charter**: 400, 600, 22px, 29px, 50px, 1.00, 1.13, 1.25; substitute `serif`.

## Spacing / shape
- Section Gap: `30-35px`
- Card Padding: `12px`
- Element Gap: `5-24px`
- Page Max Width: `1440px`
- Radius: `cards: 10px, buttons: 10px, navItems: 16px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **How Readwise Works — Feature Steps**: Reference component style.
- **User Testimonial Cards**: Reference component style.
- **Primary Action Button**: Interactive element
- **Navigation Link**: Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
