# Peloton - Refero Design MD

- Source: https://styles.refero.design/style/355e8465-df7d-486a-9d76-2ace37d076a2
- Original site: https://onepeloton.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Studio, Focused Power. Like a high-end fitness studio dimmed for an intense session, with performance data brightly illuminated.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Peloton Red | `#df1c2f` | brand | Action accent / signal color |
| Charcoal Black | `#181a1d` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Cool Gray | `#65666a` | neutral | Border, muted text, or supporting surface |
| Light Pearl | `#f7f7f7` | neutral | Page background or card surface |
| Silver Mist | `#e4e6e7` | neutral | Page background or card surface |
| Stone Gray | `#a8acb1` | neutral | Border, muted text, or supporting surface |
| Concrete Gray | `#888b93` | neutral | Border, muted text, or supporting surface |
| Shadow Gradient | `#a8acb1` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-peloton-red: #df1c2f;
  --ref-charcoal-black: #181a1d;
  --ref-pure-white: #ffffff;
  --ref-cool-gray: #65666a;
  --ref-light-pearl: #f7f7f7;
  --ref-silver-mist: #e4e6e7;
  --ref-stone-gray: #a8acb1;
  --ref-concrete-gray: #888b93;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 700, 12px, 14px, 15px, 16px, 18px, 20px, 26px, 32px, 36px, 48px, 1.07, 1.20, 1.25, 1.30, 1.33, 1.38, 1.39, 1.50, 1.69, 1.71; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `pill: 204px, cards: 0px, images: 6px, inputs: 2px, buttons: 28px, default: 6px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Product Lineup Cards**: Reference component style.
- **Promo Announcement Banner**: Reference component style.
- **Primary Filled Button**: Primary Call to Action
- **Text Link Button (Invisible)**: Navigation and subtle interactions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
