# Apollographql - Refero Design MD

- Source: https://styles.refero.design/style/65b30976-3663-40b2-8751-7a360ba74539
- Original site: https://apollographql.com
- Theme: `mixed`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space operations center: dark, high-contrast UI with a single vibrant accent for critical actions, like indicator lights on a mission control panel.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#15252d` | neutral | Primary text or dark surface |
| Comet Dust | `#f8f8f8` | neutral | Page background or card surface |
| Nebula Gray | `#e2e8f0` | neutral | Page background or card surface |
| Crater Gray | `#9fb2bc` | neutral | Border, muted text, or supporting surface |
| Off-White Cloud | `#efefef` | neutral | Page background or card surface |
| Fusion Orange | `#e75e15` | accent | Action accent / signal color |
| Subtle Dark Gray | `#254250` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #15252d;
  --ref-comet-dust: #f8f8f8;
  --ref-nebula-gray: #e2e8f0;
  --ref-crater-gray: #9fb2bc;
  --ref-off-white-cloud: #efefef;
  --ref-fusion-orange: #e75e15;
  --ref-subtle-dark-gray: #254250;
}
```

## Typography direction
- **Inter**: 400, 12px, 14px, 16px, 20px, 24px, 30px, 38px, 50px, 0.94, 1.00, 1.10, 1.25, 1.30, 1.33, 1.40, 1.43, 1.50; substitute `Inter`.
- **Fira Code**: 500, 18px, 1.25; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 24px, inputs: 8px, buttons: 999px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Feature Content Card with Buttons**: Reference component style.
- **Primary Call to Action Button**: Main interactive button
- **Secondary Outlined Button**: Secondary action or ghost button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
