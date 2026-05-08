# Apple - Refero Design MD

- Source: https://styles.refero.design/style/764b6a64-c233-4e0f-b8e1-bc01e2f8aa16
- Original site: https://www.apple.com/macbook-pro
- Theme: `dark`
- Recommended fit: **Visual board / presentation**

## North star
Precision instrument in shadow - where meticulously crafted typography navigates high-contrast realms of light and dark.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary background for dark sections, especially hero content and full-bleed product showcases, absorbing light to make. |
| Space Gray | `#1d1d1f` | neutral | Secondary dark surface color and default text color for light theme content, offering a subtle lift from Pitch Black. |
| Cloud White | `#ffffff` | neutral | Text color on dark backgrounds, icon fills, and an alternative background for information-dense sections, providing ext. |
| Ghost White | `#f5f5f7` | neutral | Primary background color for light theme sections (e.g. legal text) and subtle contrast surfaces, nearly achromatic for. |
| Cool Gray | `#86868b` | neutral | Secondary text and placeholder color in dark contexts, providing a softer alternative to White for less prominent infor. |
| Deep Graphite | `#161617` | neutral | Subtle, slightly darker background for deeply nested elements within dark sections, adding a layer of depth. |
| Storm Gray | `#333336` | neutral | Interactive element backgrounds in dark mode for controls like dropdowns or hover states in navigation. |
| Dark Charcoal | `#424245` | neutral | Tertiary text color for fine print or less emphasized details on dark backgrounds. |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-space-gray: #1d1d1f;
  --ref-cloud-white: #ffffff;
  --ref-ghost-white: #f5f5f7;
  --ref-cool-gray: #86868b;
  --ref-deep-graphite: #161617;
  --ref-storm-gray: #333336;
}
```

## Typography direction
- Primary: **SF Pro Text**; substitute `Inter`.
- Secondary/code: **SF Pro Display**; substitute `Inter`.

## Spacing / shape
- Section gap: `40px`
- Card padding: `28px`
- Element gap: `10px`
- Radius: `{'cards': '28px', 'inputs': '210px', 'buttons': '999px', 'standard': '10px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
