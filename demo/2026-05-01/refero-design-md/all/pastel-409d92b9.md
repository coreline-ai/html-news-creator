# Pastel - Refero Design MD

- Source: https://styles.refero.design/style/409d92b9-00a8-4e21-a430-ab95ea48204f
- Original site: https://usepastel.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on White Marble. The layout is structured and precise, rendered in a palette that feels both clean and substantial.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text or dark surface |
| Storm Gray | `#222222` | neutral | Primary text or dark surface |
| Ghost White | `#f5f5f4` | neutral | Page background or card surface |
| Cloud Cover | `#e6e3e2` | neutral | Page background or card surface |
| Deep Sea Blue | `#165dfb` | brand | Action accent / signal color |
| Whisper Gray | `#78716b` | neutral | Border, muted text, or supporting surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-storm-gray: #222222;
  --ref-ghost-white: #f5f5f4;
  --ref-cloud-cover: #e6e3e2;
  --ref-deep-sea-blue: #165dfb;
  --ref-whisper-gray: #78716b;
  --ref-snow-drift: #ffffff;
}
```

## Typography direction
- **Figtree**: 400, 500, 600, 14px, 16px, 18px, 21px, 35px, 45px, 58px, 1.00, 1.07, 1.10, 1.25, 1.29, 1.33, 1.37, 1.43, 1.50, 1.52, 1.70, 2.00; substitute `Inter`.

## Spacing / shape
- Card Padding: `0px`
- Radius: `tags: 4px, round: 120px, buttons: 10px, default: 8.8px, prominent: 15px`

## Component cues
- **CTA Button Group with Trust Signals**: Reference component style.
- **Testimonial Card with Attribution**: Reference component style.
- **Social Proof — Trusted By Section**: Reference component style.
- **Ghost Button**: Interactive element
- **Secondary Action Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
