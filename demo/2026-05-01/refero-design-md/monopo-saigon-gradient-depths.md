# monopo saigon - Refero Design MD

- Source: https://styles.refero.design/style/3e52dd36-6ab1-48c6-bc40-47ef6d33abc2
- Original site: https://monopo.vn
- Theme: `dark`
- Recommended fit: **Visual board / presentation**

## North star
Shifting gradient depths on frosted glass

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary background for pages, cards, and dark-themed sections |
| Frost White | `#ffffff` | neutral | Primary text color, link defaults, borders for ghost components, and accents against dark backgrounds. Used for text on. |
| Deep Shadow | `#181818` | neutral | Secondary text in footers and less prominent information. Subtly darker borders |
| Whisper Gray | `#6d6d6d` | neutral | Muted body text and auxiliary text where lower contrast is desired |
| Misty Gray | `#636363` | neutral | Background for subtle, low-contrast interactive elements like the cookie consent button |
| Deep Ocean Gradient | `#a0e0ab` | brand | Atmospheric background for hero sections and full-bleed visual elements, creating an immersive, fluid environment |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-frost-white: #ffffff;
  --ref-deep-shadow: #181818;
  --ref-whisper-gray: #6d6d6d;
  --ref-misty-gray: #636363;
  --ref-deep-ocean-gradient: #a0e0ab;
}
```

## Typography direction
- Primary: **Roobert**; substitute `system-ui, sans-serif`.
- Secondary/code: **Raleway**; substitute `serif`.

## Spacing / shape
- Section gap: `46px`
- Card padding: `34px`
- Element gap: `14px`
- Radius: `{'cards': '10px', 'buttons': '75.024px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
