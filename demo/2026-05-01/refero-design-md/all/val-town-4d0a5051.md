# Val Town - Refero Design MD

- Source: https://styles.refero.design/style/4d0a5051-1c4c-4338-8406-2babdc97915c
- Original site: https://val.town
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp developer console

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f1f5f9` | neutral | Page background or card surface |
| Steel Gray | `#e2e8f0` | neutral | Page background or card surface |
| Cadet Blue | `#cad5e2` | neutral | Action accent / signal color |
| Charcoal Text | `#000000` | neutral | Primary text or dark surface |
| Charcoal UI | `#314158` | neutral | Primary text or dark surface |
| Dark Slate | `#45556c` | neutral | Border, muted text, or supporting surface |
| Deep Midnight | `#1d293d` | neutral | Primary text or dark surface |
| Faded Stone | `#99a1af` | neutral | Border, muted text, or supporting surface |
| Cerulean Sky | `#00bcff` | brand | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-ghost-gray: #f1f5f9;
  --ref-steel-gray: #e2e8f0;
  --ref-cadet-blue: #cad5e2;
  --ref-charcoal-text: #000000;
  --ref-charcoal-ui: #314158;
  --ref-dark-slate: #45556c;
  --ref-deep-midnight: #1d293d;
}
```

## Typography direction
- **IBM Plex Sans**: 400, 10px, 12px, 14px, 16px, 18px, 24px, 36px, 48px, 60px, 128px, 1.00, 1.11, 1.14, 1.25, 1.30, 1.33, 1.43, 1.50, 1.56, 1.60; substitute `system-ui, sans-serif`.
- **IBM Plex Sans**: 700, 10px, 12px, 14px, 16px, 18px, 24px, 36px, 48px, 60px, 128px, 1.00, 1.11, 1.14, 1.25, 1.30, 1.33, 1.43, 1.50, 1.56, 1.60; substitute `system-ui, sans-serif`.
- **iA Writer Mono**: 400, 14px, 16px, 20px, 24px, 60px, 1.00, 1.33, 1.40, 1.43, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16-24px`
- Element Gap: `4px`
- Radius: `cards: 8px, 12px, badges: 4px, buttons: 8px, 12px, default: 8px`

## Component cues
- **Blog Post Alert Banner**: Reference component style.
- **CTA Button Group**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Navigation Link**: Interactive element
- **Primary CTA Button**: Call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
