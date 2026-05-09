# Textla - Refero Design MD

- Source: https://styles.refero.design/style/fb812ddb-d7c0-4540-82d7-1562dff16f09
- Original site: https://www.textla.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Rustic ledger, illustrated parchment

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#10380b` | brand | Action accent / signal color |
| Buttermilk | `#f2ee98` | brand | Action accent / signal color |
| Sunshine Yellow | `#fce519` | brand | Action accent / signal color |
| Parchment White | `#fefde6` | neutral | Page background or card surface |
| Muted Sage | `#dbe8ac` | brand | Action accent / signal color |
| Vivid Mint | `#30be60` | accent | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-forest-green: #10380b;
  --ref-buttermilk: #f2ee98;
  --ref-sunshine-yellow: #fce519;
  --ref-parchment-white: #fefde6;
  --ref-muted-sage: #dbe8ac;
  --ref-vivid-mint: #30be60;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **RethinkSans**: 600, 700, 800, 16px, 18px, 20px, 1.00, 1.30, 1.33, 1.50, 1.60, 1.71; substitute `system-ui`.
- **National 2 Condensed**: 600, 700, 800, 16px, 18px, 20px, 24px, 32px, 40px, 48px, 56px, 64px, 86px, 104px, 156px, 180px, 0.80, 1.00, 1.13, 1.30, 1.50, 1.67; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `full: 1440px, cards: 40px, forms: 24px, elements: 16px`

## Surface cues
- **Page Canvas** `#f2ee98`: The foundational background for the entire page, providing a warm, soft base.
- **Base Card** `#fefde6`: General purpose card and input field background, offering a slightly lighter, off-white surface.
- **Accent Card** `#dbe8ac`: Secondary card background, adding a muted green variation for visual distinction.

## Component cues
- **Outlined Ghost Button**: Secondary action or navigation item, often paired with a filled button.
- **Primary Filled Button**: Main call-to-action button.
- **Prominent Card**: Highlighted content container, often for testimonials or key data.
- **Informational Card**: General content grouping with a subtle background.
- **Primary Input Field**: User input for forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
