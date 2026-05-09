# Uber - Refero Design MD

- Source: https://styles.refero.design/style/caf8d2ef-4173-4431-9d26-05be0272e9f8
- Original site: https://uber.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp monochrome canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f6f6f6` | neutral | Page background or card surface |
| Charcoal Text | `#333333` | neutral | Primary text or dark surface |
| Input Border Gray | `#767676` | neutral | Border, muted text, or supporting surface |
| Subtle Silver | `#afafaf` | neutral | Border, muted text, or supporting surface |
| Slate Shadow | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Lagoon Mist | `#9dcdd6` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f6f6f6;
  --ref-charcoal-text: #333333;
  --ref-input-border-gray: #767676;
  --ref-subtle-silver: #afafaf;
  --ref-slate-shadow: #d6d6d6;
  --ref-lagoon-mist: #9dcdd6;
}
```

## Typography direction
- **UberMoveText**: 400, 500, 12px, 14px, 16px, 18px, 24px, 1.00, 1.14, 1.20, 1.25, 1.33, 1.43, 1.50, 1.67, 2.00; substitute `system-ui`.
- **UberMove**: 400, 700, 20px, 24px, 36px, 52px, 1.22, 1.23, 1.33, 1.40; substitute `system-ui`.
- **sans-serif**: 400, 16px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `12-24px`
- Element Gap: `4-24px`
- Radius: `misc: 12px, cards: 8px, buttons: 8px, capsule: 999px`

## Component cues
- **Ride Booking Form**: Reference component style.
- **Suggestions Feature Cards**: Reference component style.
- **Log In Account CTA**: Reference component style.
- **Primary Action Button**: Main call to action
- **Capsule Button**: Compact action button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
