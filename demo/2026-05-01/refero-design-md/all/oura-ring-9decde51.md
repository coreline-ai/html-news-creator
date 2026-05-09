# Oura Ring - Refero Design MD

- Source: https://styles.refero.design/style/9decde51-2a8b-4212-bba5-be9457efc62e
- Original site: https://ouraring.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, diffused elegance. Like light filtering through linen onto brushed metal.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Linen Mist | `#f7f1e8` | neutral | Page background or card surface |
| Graphite | `#4a4741` | neutral | Border, muted text, or supporting surface |
| Ebony | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#ececec` | neutral | Page background or card surface |
| Stone | `#a8a5a0` | neutral | Border, muted text, or supporting surface |
| Off-White | `#ffffff` | neutral | Page background or card surface |
| Deep Space | `#1c1b1a` | neutral | Primary text or dark surface |
| Twilight Indigo | `#5b6550` | accent | Action accent / signal color |
| Ocean Glimmer | `#1f72cd` | accent | Action accent / signal color |
| Warm Bronze Gradient | `#af751b` | brand | Action accent / signal color |

```css
:root {
  --ref-linen-mist: #f7f1e8;
  --ref-graphite: #4a4741;
  --ref-ebony: #000000;
  --ref-cloud-gray: #ececec;
  --ref-stone: #a8a5a0;
  --ref-off-white: #ffffff;
  --ref-deep-space: #1c1b1a;
  --ref-twilight-indigo: #5b6550;
}
```

## Typography direction
- **AkkuratLL**: 200, 300, 400, 500, 700, 12px, 14px, 16px, 18px, 24px, 40px, 48px, 80px, 96px, 1.00, 1.25, 1.33, 1.38, 1.50; substitute `Inter`.
- **Editorial New**: 100, 300, 500, 30px, 40px, 80px, 96px, 1.00, 1.25, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 8px, input: 12px, buttons: 16777215px, general: 4px`

## Component cues
- **Product Display Cards**: Reference component style.
- **Tab Bar — Activity Selector**: Reference component style.
- **Button Group + Announcement Banner**: Reference component style.
- **Primary Filled Button**: Call to action.
- **Secondary Outlined Button**: Secondary actions or navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
