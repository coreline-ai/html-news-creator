# Stability AI - Refero Design MD

- Source: https://styles.refero.design/style/f532c703-1179-465d-9933-7736df44d0ae
- Original site: https://stability.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center; a sophisticated dark UI with precise information delivery.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Cloud | `#383838` | neutral | Primary text or dark surface |
| Off-White Text | `#e5e7e6` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Deep Plum Accent | `#a381ff` | brand | Action accent / signal color |
| Luminous Violet | `#776cff` | brand | Action accent / signal color |
| Slate Gray | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Lavender Mist | `#b6a9c6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-storm-cloud: #383838;
  --ref-off-white-text: #e5e7e6;
  --ref-polar-white: #ffffff;
  --ref-deep-plum-accent: #a381ff;
  --ref-luminous-violet: #776cff;
  --ref-slate-gray: #bbbbbb;
  --ref-lavender-mist: #b6a9c6;
}
```

## Typography direction
- **Archivo**: 400, 600, 700, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 25px, 30px, 32px, 40px, 42px, 50px, 72px, 0.98-2.22; substitute `Open Sans`.
- **Figtree**: 600, 14px, 16px, 1.20; substitute `Montserrat`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `10-18px`
- Radius: `cards: 15px, input: 99px, buttons: 300px, default: 11px`

## Component cues
- **Announcement Banner**: Reference component style.
- **CTA Button Group**: Reference component style.
- **Mailing List Signup Form**: Reference component style.
- **Primary Call to Action Button**: Primary interactive element for key actions
- **Navigation Link Button**: Navigation items in header and footer

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
