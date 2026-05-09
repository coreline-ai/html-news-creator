# Render - Refero Design MD

- Source: https://styles.refero.design/style/c14bfde7-6f08-4b54-bd9b-39989d10cfef
- Original site: https://render.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp canvas, gradient fireworks. A bright, white backdrop that provides contrast for a constellation of colorful gradients and powerful typography.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#0d0d0d` | neutral | Primary text or dark surface |
| Asphalt Gray | `#272727` | neutral | Primary text or dark surface |
| Pebble Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Smoke Gray | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Silver Lining | `#e3e3e3` | neutral | Page background or card surface |
| Lavender Mist | `#e6daff` | neutral | Page background or card surface |
| Arctic Blue Tint | `#e0f4ff` | neutral | Action accent / signal color |
| Grape Glow | `#8a05ff` | accent | Action accent / signal color |
| Digital Emerald | `#009e7a` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-charcoal-text: #0d0d0d;
  --ref-asphalt-gray: #272727;
  --ref-pebble-gray: #4d4d4d;
  --ref-smoke-gray: #6b6b6b;
  --ref-silver-lining: #e3e3e3;
  --ref-lavender-mist: #e6daff;
  --ref-arctic-blue-tint: #e0f4ff;
}
```

## Typography direction
- **Roobert**: 300, 400, 20px, 32px, 40px, 48px, 56px, 64px, 80px, 1.00, 1.05, 1.06, 1.07, 1.08, 1.10, 1.15, 1.20; substitute `Inter`.
- **PPNeueMontreal**: 400, 500, 12px, 14px, 16px, 18px, 20px, 24px, 1.12, 1.21, 1.25, 1.33, 1.38, 1.40, 1.44, 1.50; substitute `System UI`.
- **PPNeueMontrealMono**: 400, 500, 11px, 12px, 14px, 1.27, 1.33, 1.43; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `tags: 937px, buttons: 0px, default: 0px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Feature Steps — Click, click, done**: Reference component style.
- **Announcement Banner + Pill Tags**: Reference component style.
- **Primary Dark Button**: Call to Action
- **Outline Button**: Secondary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
