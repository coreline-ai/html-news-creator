# Luffu - Refero Design MD

- Source: https://styles.refero.design/style/3da7b444-ded8-406b-90b7-96851604b92b
- Original site: https://luffu.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Family almanac printed on cream linen — editorial restraint meets intimate warmth, executed in two weights of a single serif-adjacent type system on a near-parchment ground.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Ink | `#192830` | brand | Action accent / signal color |
| Parchment | `#f5f5ee` | neutral | Page background or card surface |
| Linen | `#e4e7da` | neutral | Page background or card surface |
| Pressed Cotton | `#d7d7cb` | neutral | Border, muted text, or supporting surface |
| Graphite | `#2f3136` | neutral | Primary text or dark surface |
| Slate | `#535557` | neutral | Border, muted text, or supporting surface |
| Dusk | `#424e52` | neutral | Border, muted text, or supporting surface |
| White | `#ffffff` | neutral | Page background or card surface |
| Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-ink: #192830;
  --ref-parchment: #f5f5ee;
  --ref-linen: #e4e7da;
  --ref-pressed-cotton: #d7d7cb;
  --ref-graphite: #2f3136;
  --ref-slate: #535557;
  --ref-dusk: #424e52;
  --ref-white: #ffffff;
}
```

## Typography direction
- **ABC Arizona Sans**: 400, 14px, 16px, 20px, 1.0–1.2; substitute `Freight Sans Pro or Cormorant SC`.
- **ABC Arizona Flare**: 400, 40px, 48px, 64px, 1.0; substitute `Playfair Display or Cormorant Garamond`.

## Spacing / shape
- Card Padding: `32-34px`
- Element Gap: `16-24px`
- Page Max Width: `1200px`
- Radius: `cards: 6px, buttons: 4-6px, avatarCircles: 9999px`

## Surface cues
- **Page Ground** `#f5f5ee`: Default section background — the warm cream anchor of the entire system
- **Section Lift** `#e4e7da`: Subtle section differentiation without color shift
- **Card Surface** `#d7d7cb`: Feature card backgrounds and UI mock containers
- **Dark Anchor** `#192830`: Primary button fill and footer background — the only true dark surfaces

## Component cues
- **Button Group (Primary CTA + Ghost + Inline Waitlist)**: Reference component style.
- **Section Heading Block with Caregiver Questions**: Reference component style.
- **Feature Cards — Health Logging 3-Up Grid**: Reference component style.
- **Primary CTA Button (Dark Fill)**: Main conversion action — waitlist signup
- **Ghost Navigation Button (Outlined)**: Secondary actions in the navigation bar

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
