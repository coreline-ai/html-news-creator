# Relate dot App - Refero Design MD

- Source: https://styles.refero.design/style/6bc9448b-5d39-4aba-9007-25c7a2aedbad
- Original site: https://relate.app
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Utility-first information panels with minimal fuss.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Text | `#444444` | neutral | Border, muted text, or supporting surface |
| Deep Text | `#222222` | neutral | Primary text or dark surface |
| Graphite Accent | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#eeeeee` | neutral | Page background or card surface |
| Success Green | `#7bd428` | accent | Action accent / signal color |
| Action Blue | `#2484f2` | accent | Action accent / signal color |
| Link Blue | `#2374c4` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-text: #444444;
  --ref-deep-text: #222222;
  --ref-graphite-accent: #000000;
  --ref-ghost-gray: #eeeeee;
  --ref-success-green: #7bd428;
  --ref-action-blue: #2484f2;
  --ref-link-blue: #2374c4;
}
```

## Typography direction
- **Roboto**: 400, 700, 14px, 16px, 18px, 1.20, 1.31; substitute `system-ui`.
- **Georgia**: 400, 16px, 1.20; substitute `serif`.
- **Proxima Nova**: 300, 400, 500, 800, 17px, 20px, 21px, 22px, 31px, 33px, 1.20, 1.21, 1.41; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `36px`
- Card Padding: `15px`
- Element Gap: `20px`
- Radius: `default: 0px`

## Component cues
- **Ghost Buy Now Button**: Primary action button for purchasing domains.
- **Information Card with Buy Now Button**: Contains domain details and purchase options.
- **GoDaddy Secure Transaction Label**: Indicates secure purchasing.
- **Learn More Link**: Secondary action for more information.
- **Highlighted Status Tag**: Draws attention to key status like 'Available!' or 'Extra:'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
