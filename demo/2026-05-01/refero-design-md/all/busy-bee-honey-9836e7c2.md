# Busy Bee Honey - Refero Design MD

- Source: https://styles.refero.design/style/9836e7c2-ac8e-453d-bdef-2677eb078d59
- Original site: https://www.busybeehoney.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Golden Harvest Comfort: a sun-drenched, natural warmth with a handmade touch.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Honeycomb Gold | `#ffca50` | accent | Action accent / signal color |
| Earth Brown | `#3b2722` | brand | Action accent / signal color |
| Sky Blue | `#6aacc2` | accent | Action accent / signal color |
| Warm Cream | `#f2ebd0` | neutral | Page background or card surface |
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Harvest Green | `#6fa162` | accent | Action accent / signal color |
| Cacao Red | `#a0342a` | accent | Action accent / signal color |

```css
:root {
  --ref-honeycomb-gold: #ffca50;
  --ref-earth-brown: #3b2722;
  --ref-sky-blue: #6aacc2;
  --ref-warm-cream: #f2ebd0;
  --ref-black-ink: #000000;
  --ref-harvest-green: #6fa162;
  --ref-cacao-red: #a0342a;
}
```

## Typography direction
- **TayMakawao**: 400, 28px, 90px, 135px, 209px, 238px, 0.80, 0.82, 1.00; substitute `Merriweather, Playfair Display`.
- **TayBirdie**: 400, 12px, 14px, 16px, 20px, 1.00, 1.10, 1.50.
- **Times**: 400, 16px, 1.20; substitute `Georgia, Lora`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `body: 42.75px, buttons: 500px`

## Component cues
- **Primary Filled Button**: Main call-to-action button.
- **Ghost Outlined Button (Earth Brown)**: Secondary action or subtle navigation.
- **Ghost Outlined Button (Black)**: Neutral tertiary action.
- **Basic Card**: Container for content where no elevation or strong visual separation is needed.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
