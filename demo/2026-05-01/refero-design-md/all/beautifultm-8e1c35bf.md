# Beautiful™ - Refero Design MD

- Source: https://styles.refero.design/style/8e1c35bf-f0e8-4889-b869-d9883bb76767
- Original site: https://cookwithbeautiful.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Home Goods Catalog: pages feel like browsing a tactile, sunlit lifestyle brand.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Creamy Canvas | `#fff5e6` | neutral | Page background or card surface |
| Buttermilk | `#e8e8e1` | neutral | Page background or card surface |
| Deep Licorice | `#000000` | neutral | Primary text or dark surface |
| Truffle | `#282828` | neutral | Primary text or dark surface |
| White Linen | `#ffffff` | neutral | Page background or card surface |
| Pebble Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Ash Mist | `#707070` | neutral | Border, muted text, or supporting surface |
| Coral Kiss | `#fa7864` | brand | Action accent / signal color |
| Desert Rose | `#dc8264` | brand | Action accent / signal color |

```css
:root {
  --ref-creamy-canvas: #fff5e6;
  --ref-buttermilk: #e8e8e1;
  --ref-deep-licorice: #000000;
  --ref-truffle: #282828;
  --ref-white-linen: #ffffff;
  --ref-pebble-gray: #cccccc;
  --ref-ash-mist: #707070;
  --ref-coral-kiss: #fa7864;
}
```

## Typography direction
- **Basis Grotesque Pro**: 400, 10px, 13px, 14px, 16px, 18px, 21px, 1.20, 1.30; substitute `Inter`.
- **BasisGrotesquePro-Mono**: 400, 14px, 16px, 18px, 19px, 1.30, 1.42; substitute `Space Mono`.
- **GascogneTS**: 400, 500, 25px, 28px, 30px, 32px, 39px, 43px, 52px, 1.00, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `10px`
- Element Gap: `10px`
- Radius: `cards: 50%, buttons: 999px, navigation: 20px`

## Surface cues
- **Buttermilk Base** `#e8e8e1`: Primary page background and foundational surface for many sections.
- **Creamy Canvas** `#fff5e6`: Slightly elevated surface for content blocks, text backgrounds, and subtle distinctions from the base.
- **White Linen Card** `#ffffff`: Brightest surface for cards and select component backgrounds that require maximum contrast or a clean break.

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Rounded Button**: Alternate call to action
- **Ghost Action Button**: Subtle, outlined action
- **Navigation Link Button**: Navigational element
- **Circular Category Card**: Product category navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
