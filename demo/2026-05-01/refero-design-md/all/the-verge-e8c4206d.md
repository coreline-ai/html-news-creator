# The Verge - Refero Design MD

- Source: https://styles.refero.design/style/e8c4206d-9a2a-4c08-9524-6f14a25e792f
- Original site: https://theverge.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Newsprint, Laser-Etched Text. A dark, information-dense canvas with sharp typographic contrasts and electric accents.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#131313` | neutral | Primary text or dark surface |
| Light Ash | `#313131` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#e9e9e9` | neutral | Page background or card surface |
| Faded Steel | `#949494` | neutral | Border, muted text, or supporting surface |
| Voltage Teal | `#3cffd0` | brand | Action accent / signal color |
| Neon Violet | `#5200ff` | accent | Action accent / signal color |
| Blaze Orange | `#ff3d00` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #000000;
  --ref-deep-graphite: #131313;
  --ref-light-ash: #313131;
  --ref-ghost-white: #ffffff;
  --ref-silver-mist: #e9e9e9;
  --ref-faded-steel: #949494;
  --ref-voltage-teal: #3cffd0;
  --ref-neon-violet: #5200ff;
}
```

## Typography direction
- **Poly Sans**: 300, 400, 500, 700, 10px, 11px, 12px, 13px, 15px, 16px, 18px, 19px, 20px, 24px, 34px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60; substitute `Inter`.
- **Manuka**: 900, 60px, 90px, 107px, 0.80; substitute `Playfair Display`.
- **Fk Roman Standard**: 400, 16px, 20px, 24px, 1.20, 1.30; substitute `Libre Baskerville`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `buttons: 24px, default: 0px, card_image_corners: 3px`

## Component cues
- **Top Stories List**: Reference component style.
- **Today's Stream Tab Bar + Feed Item**: Reference component style.
- **Podcasts Most Popular Block**: Reference component style.
- **Navigation Link**: Primary navigation elements
- **Primary Action Button**: Call To Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
