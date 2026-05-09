# Peak Design - Refero Design MD

- Source: https://styles.refero.design/style/6f3fb64d-d4c9-4ec1-86a1-7983e5180985
- Original site: https://peakdesign.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Photographic gallery on architectural black and white. Product precision through high-contrast typography.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#eef1f0` | neutral | Page background or card surface |
| Charcoal Black | `#0c0c0c` | neutral | Primary text or dark surface |
| Graphite | `#606562` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#cccfcd` | neutral | Border, muted text, or supporting surface |
| Alert Red | `#cc2e39` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-cloud-white: #ffffff;
  --ref-ash-gray: #eef1f0;
  --ref-charcoal-black: #0c0c0c;
  --ref-graphite: #606562;
  --ref-slate-border: #cccfcd;
  --ref-alert-red: #cc2e39;
}
```

## Typography direction
- **Exposure-10**: 400, 40px, 48px, 80px, 1.10; substitute `Playfair Display`.
- **Geist**: 400, 600, 700, 14px, 16px, 1.0, 1.2, 1.4, 1.5; substitute `Inter`.
- **bryant**: 700, 14px, 16px, 24px, 32px, 1.0, 1.1, 1.2, 1.4; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `cards: 8px, badges: 9999px, inputs: 4px, buttons: 4px, 32px`

## Component cues
- **Category Tab Bar with Product Cards**: Reference component style.
- **Announcement Banner + Button Group**: Reference component style.
- **Search Input + New Arrivals Promo Card**: Reference component style.
- **Primary Ghost Button**: Primary action button on dark backgrounds
- **Solid Standard Button**: Standard action button on light backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
