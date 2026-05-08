# Linear - Refero Design MD

- Source: https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1
- Original site: https://linear.app
- Theme: `dark`
- Recommended fit: **Admin Review / Run monitor / Signal Desk**
- Priority: **P1**

## Why this fits html-news-creator
Best dark command-center reference for operator and review surfaces: layered dark panels, compact radius, one high-energy accent.

## Apply to
- Review active states and primary CTAs
- Run progress and global indicators
- Dark report cards and nested evidence panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#08090a` | neutral | Page background, primary surface for base elements, subtly integrated into shadows for depth. |
| Graphite | `#0f1011` | neutral | Elevated card backgrounds, slightly lighter than the canvas to denote layering. |
| Deep Slate | `#161718` | neutral | Secondary elevated card backgrounds, providing another layer of visual hierarchy. |
| Charcoal Grey | `#23252a` | neutral | Borders and some shadowed card surfaces, framing elements with a subtle distinction. |
| Muted Ash | `#323334` | neutral | Subtle borders and dividers, indicating soft separations within the dark theme. |
| Gunmetal | `#383b3f` | neutral | Tertiary background elements and input borders, a darker neutral for functional elements. |
| Porcelain | `#f7f8f8` | neutral | Primary text and icons, providing strong contrast for readability against dark backgrounds. |
| Light Steel | `#d0d6e0` | neutral | Secondary text and borders, for less prominent information or structural lines. |

```css
:root {
  --ref-pitch-black: #08090a;
  --ref-graphite: #0f1011;
  --ref-deep-slate: #161718;
  --ref-charcoal-grey: #23252a;
  --ref-muted-ash: #323334;
  --ref-gunmetal: #383b3f;
  --ref-porcelain: #f7f8f8;
}
```

## Typography direction
- Primary: **Inter Variable**; substitute `Inter`.
- Secondary/code: **Berkeley Mono**; substitute `IBM Plex Mono`.

## Spacing / shape
- Section gap: `24px`
- Card padding: `12px`
- Element gap: `8px`
- Radius: `{'pill': '9999px', 'tags': '2px', 'cards': '6px', 'badges': '4px', 'inputs': '6px', 'buttons': '6px', 'default': '6px'}`

## Agent notes
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- Keep the project content hierarchy first: section title, why it matters, source evidence, confidence, and image evidence.
