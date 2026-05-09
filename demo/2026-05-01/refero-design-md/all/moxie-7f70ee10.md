# Moxie - Refero Design MD

- Source: https://styles.refero.design/style/7f70ee10-123b-43cc-bd04-498cfc5b5ac0
- Original site: https://moxiegrouppr.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight velvet, shimmering ink

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Background Ink | `#000000` | neutral | Primary text or dark surface |
| Parchment White | `#f4efd4` | neutral | Page background or card surface |
| Twilight Gray | `#626055` | neutral | Border, muted text, or supporting surface |
| Deep Shadow | `#333333` | neutral | Primary text or dark surface |
| Authority Blue | `#84acfb` | brand | Action accent / signal color |

```css
:root {
  --ref-background-ink: #000000;
  --ref-parchment-white: #f4efd4;
  --ref-twilight-gray: #626055;
  --ref-deep-shadow: #333333;
  --ref-authority-blue: #84acfb;
}
```

## Typography direction
- **IBM Plex Serif**: 300, 400, 500, 17px, 22px, 26px, 28px, 43px, 55px, 1.10, 1.20; substitute `Source Serif Pro`.
- **IBM Plex Sans**: 300, 400, 500, 10px, 12px, 14px, 16px, 17px, 24px, 1.00, 1.20, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `107px`
- Card Padding: `19px`
- Element Gap: `21px`
- Radius: `tags: 1000px, cards: 13.8417px, buttons: 1000px, smallCards: 8.65108px`

## Component cues
- **Primary Action Button**: Interactive element
- **Ghost Outline Button**: Interactive element
- **Soft Border Card**: Content container
- **Client Logo Card**: Display brand logos
- **Quote Card**: Testimonial display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
