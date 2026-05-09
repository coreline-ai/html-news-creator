# Kajabi - Refero Design MD

- Source: https://styles.refero.design/style/a6bf8730-6515-4a47-9d5f-927e1e0c67d5
- Original site: https://kajabi.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp monochrome command panel on a limitless white canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0a0a0a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Surface | `#1f1f1e` | neutral | Primary text or dark surface |
| Ash Gray | `#e9e8e7` | neutral | Page background or card surface |
| Slate Text | `#535250` | neutral | Border, muted text, or supporting surface |
| Silver Border | `#e0dedc` | neutral | Page background or card surface |
| Stone Accent | `#949189` | neutral | Border, muted text, or supporting surface |
| Green Accent | `#405b50` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0a0a0a;
  --ref-canvas-white: #ffffff;
  --ref-charcoal-surface: #1f1f1e;
  --ref-ash-gray: #e9e8e7;
  --ref-slate-text: #535250;
  --ref-silver-border: #e0dedc;
  --ref-stone-accent: #949189;
  --ref-green-accent: #405b50;
}
```

## Typography direction
- **Haffer**: 400, 500, 600, 12px, 14px, 16px, 20px, 24px, 28px, 32px, 40px, 48px, 60px, 1.00, 1.10, 1.20, 1.43, 1.45, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `pill: 15984px, default: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Ash Gray** `#e9e8e7`: Subtle background for differentiating content sections
- **Green Accent** `#405b50`: Accent background for specific content blocks
- **Charcoal Surface** `#1f1f1`: Elevated card backgrounds within dark sections
- **Midnight Ink** `#0a0a0a`: Dominant dark background for hero sections and footers

## Component cues
- **Primary Dark Button**: Call-to-action button for initiating key actions.
- **Ghost Light Button**: Secondary action or navigational link with low visual hierarchy.
- **Light Button**: Positive action button where contrast is needed against a dark background.
- **Input Field**: Standard input for user data entry.
- **Dark Card**: Container for content within dark sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
