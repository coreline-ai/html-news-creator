# General Intelligence Company - Refero Design MD

- Source: https://styles.refero.design/style/34baa524-5d5b-4165-bbab-d01f05e6d6b9
- Original site: https://www.generalintelligencecompany.com
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Architectural Night Sky

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Night Sky | `#1f1f29` | brand | Dark base for hero sections and occasional accent backgrounds; creates a deep, contemplative atmosphere |
| Cofounder Blue | `#0081c0` | accent | Highlight elements, card backgrounds for featured content, and active interface states. Its vivid hue draws attention w. |
| Action Azure | `#41a1cf` | accent | Border color for ghost buttons and interactive elements, providing a clear but understated active state |
| Pitch Black | `#000000` | neutral | Primary text for headings and bold statements against light backgrounds, emphasizing core information |
| Canvas White | `#ffffff` | neutral | Main page background, component backgrounds, and primary text on dark elements, maintaining brightness and spaciousness |
| Off White | `#fefffc` | neutral | Subtle alternative background for secondary sections and cards, creating a slight visual separation from the main canvas |
| Ash Gray | `#f9faf7` | neutral | Background for input fields and navigation elements, providing a soft contrast |
| Cool Gray | `#eef1ed` | neutral | Subtle border for UI elements and dividers, offering minimal distinction |

```css
:root {
  --ref-night-sky: #1f1f29;
  --ref-cofounder-blue: #0081c0;
  --ref-action-azure: #41a1cf;
  --ref-pitch-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-off-white: #fefffc;
  --ref-ash-gray: #f9faf7;
}
```

## Typography direction
- Primary: **PPMondwest**; substitute `system-ui`.
- Secondary/code: **af**; substitute `monospace`.

## Spacing / shape
- Section gap: `32px`
- Card padding: `16px`
- Element gap: `8px`
- Radius: `{'nav': '50.496px', 'none': '0px', 'buttons': '4px', 'cardsLarge': '24px', 'cardsSmall': '12px', 'cardsMedium': '16px', 'navItemsSmall': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
