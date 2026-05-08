# Minimalissimo - Refero Design MD

- Source: https://styles.refero.design/style/35ff063b-1fcc-48a2-83b3-56da01e23880
- Original site: https://minimalissimo.com
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
White gallery canvas.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text, core UI elements, strong borders, icon fills. Provides high contrast |
| Canvas | `#f5f5f5` | neutral | Dominant page and section backgrounds, giving a clean, expansive base |
| Sterling | `#999999` | neutral | Medium-contrast borders, control outlines, and structural separators. Do not promote it to the primary CTA color |
| Porcelain | `#ffffff` | neutral | Component backgrounds within sections, elevated surfaces. Provides internal contrast against Canvas |
| Pale Ash | `#e0e0e0` | neutral | Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the pr. |
| Storm Gray | `#a1a1a1` | neutral | Tertiary body text, informational text, less prominent details |
| Whisper White | `#efefef` | neutral | Background for subtle interactive elements like inputs and ghost buttons, providing a slight visual lift |

```css
:root {
  --ref-inkwell: #000000;
  --ref-canvas: #f5f5f5;
  --ref-sterling: #999999;
  --ref-porcelain: #ffffff;
  --ref-pale-ash: #e0e0e0;
  --ref-storm-gray: #a1a1a1;
  --ref-whisper-white: #efefef;
}
```

## Typography direction
- Primary: **GeistSans**; substitute `Inter, Arial, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `96px`
- Card padding: `16px`
- Element gap: `16px`
- Radius: `{'cards': '8px', 'links': '4px', 'inputs': '4px', 'buttons': '4px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
