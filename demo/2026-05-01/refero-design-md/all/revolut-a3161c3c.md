# Revolut - Refero Design MD

- Source: https://styles.refero.design/style/a3161c3c-26d4-425b-aaa3-4fc3f06b77ee
- Original site: https://revolut.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
financial passport to the world

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Revolut Black | `#191c1f` | neutral | Primary text or dark surface |
| Cloud White | `#f4f4f4` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Onyx Black | `#000000` | neutral | Primary text or dark surface |
| Ash | `#505a63` | neutral | Border, muted text, or supporting surface |
| Pebble | `#c9c9cd` | neutral | Border, muted text, or supporting surface |
| Light-Tint | `#ebebf0` | neutral | Page background or card surface |

```css
:root {
  --ref-revolut-black: #191c1f;
  --ref-cloud-white: #f4f4f4;
  --ref-pure-white: #ffffff;
  --ref-onyx-black: #000000;
  --ref-ash: #505a63;
  --ref-pebble: #c9c9cd;
  --ref-light-tint: #ebebf0;
}
```

## Typography direction
- **Aeonik Pro**: 400, 500, 16px, 18px, 24px, 32px, 40px, 53px, 89px, 1.00, 1.17, 1.19, 1.20, 1.33, 1.38; substitute `Sohne, Neue Haas Grotesk`.
- **Inter**: 400, 600, 700, 12px, 14px, 16px, 1.20, 1.50, 1.57; substitute `Inter, San Francisco, Roboto`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Page Max Width: `1200px`
- Radius: `cards: 20px, inputs: 12px, buttons: 9999px, ui-mockups: 22.5px`

## Component cues
- **Button Group — Primary Dark, Primary Light, Ghost**: Reference component style.
- **Social Proof — Stats & Awards Block**: Reference component style.
- **Savings Feature Card — Interest Rate CTA**: Reference component style.
- **Primary CTA Button (Light)**: The main sign-up and affirmative action button.
- **Primary CTA Button (Dark)**: The main action button for use on dark or photographic backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
