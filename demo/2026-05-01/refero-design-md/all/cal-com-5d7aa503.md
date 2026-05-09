# Cal.com - Refero Design MD

- Source: https://styles.refero.design/style/5d7aa503-8cfa-49a4-bd3b-0c2f0f075c70
- Original site: https://cal.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Utility, Human Touch. A system that prioritizes clarity and function with a stark black-and-white palette, but softens it with friendly typography and rounded forms.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#101010` | brand | Action accent / signal color |
| Action Blue | `#0099ff` | accent | Action accent / signal color |
| White | `#ffffff` | neutral | Page background or card surface |
| Paper | `#f4f4f4` | neutral | Page background or card surface |
| Graphite | `#242424` | neutral | Primary text or dark surface |
| Slate | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Stone | `#898989` | neutral | Border, muted text, or supporting surface |
| Silver | `#e5e7eb` | neutral | Page background or card surface |
| Info Banner BG | `#eff6fe` | neutral | Page background or card surface |
| Google Blue | `#4285f4` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #101010;
  --ref-action-blue: #0099ff;
  --ref-white: #ffffff;
  --ref-paper: #f4f4f4;
  --ref-graphite: #242424;
  --ref-slate: #6b7280;
  --ref-stone: #898989;
  --ref-silver: #e5e7eb;
}
```

## Typography direction
- **Cal Sans**: 600, 20px, 24px, 48px, 64px, 1.10 - 1.30; substitute `Poppins, Gilroy`.
- **Cal Sans UI Variable Light**: 300, 14px, 16px, 18px, 1.40 - 1.50; substitute `Inter Light`.
- **Inter**: 400, 500, 600, 10px, 12px, 14px, 16px, 1.14 - 1.43; substitute `system-ui, -apple-system, sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Page Max Width: `1200px`
- Radius: `tags: 9999px, cards: 12px, inputs: 8px, buttons: 9999px (pills), 8px (rectangular)`

## Component cues
- **Compliance Info Banner**: Reference component style.
- **How It Works — Feature Cards**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Primary CTA Button**: The main call-to-action on the page.
- **Secondary Ghost Button**: A secondary call-to-action, often next to the primary.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
