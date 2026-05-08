# Steep - Refero Design MD

- Source: https://styles.refero.design/style/75fdb89f-ca64-41b3-af36-7a78bd09448e
- Original site: https://steep.app
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Warm, Crisp Canvas

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Primary page and surface background, text color for dark elements. Used for the main content area, cards, and prominent. |
| Ink | `#17191c` | neutral | Primary text color, background for filled buttons, navigation elements. A dominant dark neutral that provides strong co. |
| Graphite | `#000000` | neutral | Fallback dark text, outline for ghost buttons, decorative borders |
| Warm Mist | `#fbe1d1` | brand | Subtle background for specific cards and sections, providing a soft, almost imperceptible warmth to the interface |
| Terracotta | `#5d2a1a` | brand | Accent for borders, strokes, and decorative elements within cards. A warm brown-orange that serves as a secondary brand. |
| Fog | `#f7f7f8` | neutral | Secondary surface background, used for subtle differentiation of cards or sections that are slightly less prominent tha. |
| Muted Stone | `#4c4c4c` | neutral | Secondary text and icon color, used for less prominent information or subtle UI details |
| Light Steel | `#777b86` | neutral | Muted link color, subtle icon fills, and quiet UI elements - used for non-essential text that aids readability without. |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-ink: #17191c;
  --ref-graphite: #000000;
  --ref-warm-mist: #fbe1d1;
  --ref-terracotta: #5d2a1a;
  --ref-fog: #f7f7f8;
  --ref-muted-stone: #4c4c4c;
}
```

## Typography direction
- Primary: **Sohne**; substitute `system-ui, sans-serif`.
- Secondary/code: **Signifier**; substitute `serif`.

## Spacing / shape
- Section gap: `80px`
- Card padding: `20px`
- Element gap: `8px`
- Radius: `{'cards': '24px', 'images': '12px', 'inputs': '16px', 'buttons': '1.67772e+07px', 'default': '24px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
