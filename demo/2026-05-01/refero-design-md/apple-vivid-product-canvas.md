# Apple - Refero Design MD

- Source: https://styles.refero.design/style/a48ef430-8c6a-42d8-8c53-ab7bb43cf33b
- Original site: https://www.apple.com/ipad-air
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Precise Canvas, Vivid Product. A stark white presentation surface designed to make premium product imagery pop with singular focus.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#1d1d1f` | neutral | Primary heading and body text, button text, icon default. |
| Cloud Mist | `#6b6c6c` | neutral | Secondary body text, supporting links, muted icons, footer text. |
| Pure White | `#ffffff` | neutral | Primary page background, elevated card surfaces, clean sections. |
| Frost Gray | `#f3f6f6` | neutral | Subtle background for navigation, subtle section dividers, tertiary surface. |
| Steel Accent | `#cccfcf` | neutral | Delicate border colors, subtle outlines for form elements. |
| Dark Charcoal | `#313131` | neutral | Tertiary text, certain icon elements, dark button text. |
| Slate Echo | `#444545` | neutral | Navigation links, secondary link states, sometimes icon fills. |
| Alabaster | `#e8e8ed` | neutral | Button backgrounds in certain states, subtle background tint. |

```css
:root {
  --ref-midnight-graphite: #1d1d1f;
  --ref-cloud-mist: #6b6c6c;
  --ref-pure-white: #ffffff;
  --ref-frost-gray: #f3f6f6;
  --ref-steel-accent: #cccfcf;
  --ref-dark-charcoal: #313131;
  --ref-slate-echo: #444545;
}
```

## Typography direction
- Primary: **SF Pro Text**; substitute `system-ui, sans-serif`.
- Secondary/code: **SF Pro Display**; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section gap: `70px`
- Card padding: `14px`
- Element gap: `10px`
- Radius: `{'cards': '28px', 'buttons': '28px', 'default': '12px', 'navigation': '980px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
