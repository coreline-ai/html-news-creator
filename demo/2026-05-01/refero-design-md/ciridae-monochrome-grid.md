# Ciridae - Refero Design MD

- Source: https://styles.refero.design/style/a1b78a21-a304-482b-8ce5-f612d95d44fe
- Original site: https://www.ciridae.com
- Theme: `dark`
- Recommended fit: **Dark premium dashboard**

## North star
Monochrome Grid, Abstract Glow. Precision-engineered UI on a dark, almost black canvas, with typography as the primary visual texture and light playing like reflections off dark metal.

## Why this fits html-news-creator
Useful as a high-contrast alternative for operator and executive views.

## Apply to
- Dark dashboard shells
- Premium subscriber surfaces
- Status-heavy UI states

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Black | `#000000` | neutral | Backgrounds, prominent text, icon fills. |
| Deep Charcoal | `#0B0B0B` | neutral | Secondary backgrounds, subtle elevated surfaces. |
| Warm Graphite | `#272A2A` | neutral | Tertiary backgrounds, deeper surface layers. |
| Pure White | `#FFFFFF` | neutral | Primary text, button labels, interactive elements, prominent iconography. Creates high contrast against dark background. |
| Ash Gray | `#CECECE` | neutral | Subtle borders, inactive text, secondary iconography. |
| Steel Gray | `#858585` | neutral | Placeholder text, minor borders, tertiary text. |
| Subtle Orange | `#CC6437` | accent | Rare accent color for specific information hints or subtle emphasis. Its limited use makes any appearance notable. |
| White to Ash Gradient | `#FFFFFF` | neutral | Used for a subtle linear fade, providing a soft transition effect. |

```css
:root {
  --ref-absolute-black: #000000;
  --ref-deep-charcoal: #0B0B0B;
  --ref-warm-graphite: #272A2A;
  --ref-pure-white: #FFFFFF;
  --ref-ash-gray: #CECECE;
  --ref-steel-gray: #858585;
  --ref-subtle-orange: #CC6437;
}
```

## Typography direction
- Primary: **Pragmatica Cond**; substitute `Open Sans Condensed`.
- Secondary/code: **Pragmatica**; substitute `Open Sans`.

## Spacing / shape
- Section gap: `48px`
- Card padding: ``
- Element gap: `4px`
- Radius: `{'badges': '1440px', 'subtle': '4px', 'buttons': '1440px', 'general': '10px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
