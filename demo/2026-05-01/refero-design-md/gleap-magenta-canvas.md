# Gleap - Refero Design MD

- Source: https://styles.refero.design/style/2eab438d-32cd-40c2-b160-1e4127dac569
- Original site: https://gleap.io
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Crisp canvas, magenta highlight

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#f5f2f0` | neutral | Primary page background, provides a soft, warm base for all content |
| Porcelain Surface | `#ffffff` | neutral | Card backgrounds, elevated content areas, ensuring high contrast with text |
| Graphite Text | `#333333` | neutral | Primary text color for body copy, links, and detailed information |
| Ink Text | `#000000` | neutral | Headlines, navigation items, and strong textual elements for maximum emphasis |
| Platinum Border | `#d6d6d6` | neutral | Subtle borders and dividers for UI separation without harsh lines |
| Silver Detail | `#bcbcbc` | neutral | Muted helper text, secondary borders, and subtle accent lines |
| Deep Plum | `#7b7b7b` | neutral | Tertiary text, less prominent links and meta information |
| Amethyst Accent | `#f1ccff` | brand | Primary action buttons, prominent links, and accents within cards - it's the brand's signature interaction color, signa. |

```css
:root {
  --ref-cloud-canvas: #f5f2f0;
  --ref-porcelain-surface: #ffffff;
  --ref-graphite-text: #333333;
  --ref-ink-text: #000000;
  --ref-platinum-border: #d6d6d6;
  --ref-silver-detail: #bcbcbc;
  --ref-deep-plum: #7b7b7b;
}
```

## Typography direction
- Primary: **PP Editorial New**; substitute `Playfair Display`.
- Secondary/code: **Switzer**; substitute `Inter`.

## Spacing / shape
- Section gap: `30px`
- Card padding: `40px`
- Element gap: `16px`
- Radius: `{'cards': '24px', 'badges': '10px', 'buttons': '10px', 'largeElements': '42px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
