# Prisma - Refero Design MD

- Source: https://styles.refero.design/style/8e9e585f-5ad4-4273-8418-e1f82cdb51cf
- Original site: https://prisma.io
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Light, precise structures with sharp accents.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f3f4f6` | neutral | Page background or card surface |
| Border Frost | `#e2e8f0` | neutral | Page background or card surface |
| Charcoal Black | `#111827` | neutral | Primary text or dark surface |
| Obsidian Text | `#1d242f` | neutral | Primary text or dark surface |
| Muted Stone | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#718096` | neutral | Border, muted text, or supporting surface |
| Subtle Ash | `#9ca3af` | neutral | Border, muted text, or supporting surface |
| Prisma Teal | `#14b8a6` | brand | Action accent / signal color |
| Deep Teal | `#0d9488` | brand | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-ghost-gray: #f3f4f6;
  --ref-border-frost: #e2e8f0;
  --ref-charcoal-black: #111827;
  --ref-obsidian-text: #1d242f;
  --ref-muted-stone: #6b7280;
  --ref-soft-stone: #718096;
  --ref-subtle-ash: #9ca3af;
}
```

## Typography direction
- **Inter**: 375, 400, 500, 600, 700, 11px, 12px, 14px, 16px, 18px, 22px, 1.10-1.50; substitute `system-ui, sans-serif`.
- **Mona Sans VF**: 400, 650, 700, 900, 16px, 18px, 24px, 30px, 36px, 40px, 64px, 1.13-1.56; substitute `Arial, sans-serif`.
- **Mona Sans Mono VF**: 400, 16px, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `large: 10px, default: 6px, buttonPill: 1.67772e+07px`

## Component cues
- **Feature Cards Row**: Reference component style.
- **CTA Button Group with Code Snippet**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Ghost Button**: Secondary action button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
