# Lottielab - Refero Design MD

- Source: https://styles.refero.design/style/1f782141-d407-4c27-8cee-2246720a9f42
- Original site: https://www.lottielab.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, violet spark

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormy Indigo | `#2f2b4a` | brand | Action accent / signal color |
| Midnight Charcoal | `#1c1a2c` | neutral | Primary text or dark surface |
| Electric Violet | `#7270ff` | brand | Action accent / signal color |
| Deep Sea Blue | `#1560fb` | brand | Action accent / signal color |
| Soft Gray | `#4b5563` | neutral | Border, muted text, or supporting surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#e5e7eb` | neutral | Page background or card surface |
| Light Mist | `#f3f4f6` | neutral | Page background or card surface |
| Stone Gray | `#9ca3af` | neutral | Border, muted text, or supporting surface |
| Pale Silver | `#d9dbda` | neutral | Page background or card surface |

```css
:root {
  --ref-stormy-indigo: #2f2b4a;
  --ref-midnight-charcoal: #1c1a2c;
  --ref-electric-violet: #7270ff;
  --ref-deep-sea-blue: #1560fb;
  --ref-soft-gray: #4b5563;
  --ref-bright-white: #ffffff;
  --ref-ash-gray: #e5e7eb;
  --ref-light-mist: #f3f4f6;
}
```

## Typography direction
- **Plus Jakarta Sans**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 36px, 48px, 60px, 1.00, 1.11, 1.33, 1.43, 1.50, 1.56, 1.71, 1.78; substitute `system-ui, sans-serif`.
- **Google Sans Code**: 400, 16px, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `24px`
- Radius: `tags: 9999px, cards: 8px, inputs: 4px, buttons: 12px`

## Surface cues
- **Bright White Canvas** `#ffffff`: Primary page background, default surface for most content.
- **Light Mist Section** `#f3f4f6`: Secondary background for alternating sections, providing a subtle contrast and visual rhythm.
- **Snow Drift Card** `#f9fafb`: Background for elevated cards or specific UI components, offering a slightly lighter visual plane.

## Component cues
- **Primary Filled Button**: Interactive element, calls to action
- **Navigation Link**: Primary navigation, secondary actions
- **Image Card**: Content display, feature showcases
- **Search/Input Field**: User input, search functionality
- **Branded Logo**: Identity mark, decorative branding

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
