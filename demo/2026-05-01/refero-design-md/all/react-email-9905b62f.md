# React Email - Refero Design MD

- Source: https://styles.refero.design/style/9905b62f-007b-4b3a-9357-84e85c07ef96
- Original site: https://react.email
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal Glow

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#000000` | neutral | Primary text or dark surface |
| Inkwell | `#0f0f10` | neutral | Primary text or dark surface |
| Charcoal | `#27272a` | neutral | Primary text or dark surface |
| Porcelain | `#ffffff` | neutral | Page background or card surface |
| Starlight | `#e5e7eb` | neutral | Page background or card surface |
| Cloudburst | `#abafb4` | neutral | Border, muted text, or supporting surface |
| #6e727a | `#6e727a` | neutral | Border, muted text, or supporting surface |
| Skyline Gray | `#99a1af` | neutral | Border, muted text, or supporting surface |
| Lunar Dust | `#cad5e2` | neutral | Border, muted text, or supporting surface |
| Code Orange | `#ffb86a` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #000000;
  --ref-inkwell: #0f0f10;
  --ref-charcoal: #27272a;
  --ref-porcelain: #ffffff;
  --ref-starlight: #e5e7eb;
  --ref-cloudburst: #abafb4;
  --ref-6e727a: #6e727a;
  --ref-skyline-gray: #99a1af;
}
```

## Typography direction
- **Inter**: 400, 460, 500, 12px, 14px, 16px, 18px, 20px, 24px, 35px, 68px, 0.94, 1.00, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 2.00; substitute `system-ui`.
- **CommitMono**: 400, 13px, 14px, 1.30, 1.33, 1.40, 1.43, 1.55; substitute `monospace`.
- **-apple-system**: 400, 600, 700, 14px, 25px, 1.44, 1.55; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `lg: 18px, md: 12px, sm: 8px, xl: 24px, xs: 2px`

## Surface cues
- **Charcoal** `#27272a`: Primary page background, base canvas.
- **Inkwell** `#0f0f10`: Secondary background for cards with subtle elevation.
- **Carbon** `#000000`: Dominant card backgrounds, code editor panels, and floating modals.

## Component cues
- **Ghost Button - Default**: Interactive element
- **Ghost Button - Rounded Cyan Text**: Interactive element
- **Action Button - Filled**: Primary Call-to-action
- **Ghost Button - Hero Large**: Prominent ghost action
- **Card - Basic**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
