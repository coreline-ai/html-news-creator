# Flecto - Refero Design MD

- Source: https://styles.refero.design/style/fdc72952-9b36-443a-9e0c-20b366aee29f
- Original site: https://flecto.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Rounded emerald portal

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Emerald Canvas | `#004737` | brand | Action accent / signal color |
| Mint Accent | `#56f09f` | accent | Action accent / signal color |
| Paper White | `#fffbec` | neutral | Page background or card surface |
| Off Black | `#032019` | neutral | Primary text or dark surface |
| Soft Mint | `#d4ffe8` | accent | Action accent / signal color |
| Muted Sage | `#99b5af` | neutral | Border, muted text, or supporting surface |
| Cream Card | `#faf2d5` | neutral | Page background or card surface |
| Deep Violet | `#8f37ff` | accent | Action accent / signal color |
| True Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-emerald-canvas: #004737;
  --ref-mint-accent: #56f09f;
  --ref-paper-white: #fffbec;
  --ref-off-black: #032019;
  --ref-soft-mint: #d4ffe8;
  --ref-muted-sage: #99b5af;
  --ref-cream-card: #faf2d5;
  --ref-deep-violet: #8f37ff;
}
```

## Typography direction
- **Aeonik**: 400, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 19px, 20px, 24px, 26px, 28px, 32px, 33px, 36px, 56px, 60px, 64px, 66px, 74px, 1.00, 1.10, 1.14, 1.15, 1.20, 1.22, 1.23, 1.29, 1.30, 1.38, 1.40, 1.44, 1.46, 1.50, 1.60, 1.67, 1.86, 1.92, 1.94, 2.03, 2.09, 2.12, 2.79, 2.88; substitute `Inter`.
- **roobert-regular**: 400, 12px, 16px, 1.40, 1.87; substitute `Inter`.
- **Arial**: 400, 16px, 1.2.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `10px`
- Page Max Width: `174px`
- Radius: `pill: 60px, buttons: 10px, default: 19px, sections: 40px, iconButtons: 100%, smallWidgets: 5.76px`

## Surface cues
- **Emerald Canvas** `#004737`: Primary background for full-width thematic sections and visual anchors.
- **Paper White** `#fffbec`: Secondary background for header and content sections, creating visual breathing room.
- **Pure White** `#ffffff`: Elevated card surfaces and interactive element backgrounds on lighter sections.
- **Cream Card** `#faf2d5`: Specialized card backgrounds offering a warmer, slightly differentiated surface.

## Component cues
- **Primary Filled Button**: Call to action button for primary actions
- **Ghost Button**: Secondary action or navigation link
- **Outlined Button (Emerald)**: Call to action with brand emphasis, but not filled.
- **Outlined Button (Soft Mint)**: Call to action with subtle brand emphasis, typically on dark backgrounds.
- **Pill Button (Text)**: Small, rounded control or category tag.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
