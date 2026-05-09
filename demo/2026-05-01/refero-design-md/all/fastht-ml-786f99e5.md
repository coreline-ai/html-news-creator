# fastht.ml - Refero Design MD

- Source: https://styles.refero.design/style/786f99e5-8c40-4205-a878-bf006b330f4e
- Original site: https://fastht.ml
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight dev playground

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Canvas | `#3a2234` | neutral | Primary text or dark surface |
| Deep Aubergine | `#333333` | neutral | Primary text or dark surface |
| Charcoal Smoke | `#808080` | neutral | Border, muted text, or supporting surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f3f3f3` | neutral | Page background or card surface |
| Off-White Mist | `#e5e7eb` | neutral | Page background or card surface |
| Soft Stone | `#e8e8fc` | neutral | Page background or card surface |
| Muted Lavender | `#939eeb` | accent | Action accent / signal color |
| Electric Green | `#3cdd8c` | accent | Action accent / signal color |
| Goldenrod Pop | `#ffc435` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian-canvas: #3a2234;
  --ref-deep-aubergine: #333333;
  --ref-charcoal-smoke: #808080;
  --ref-bright-white: #ffffff;
  --ref-ash-gray: #f3f3f3;
  --ref-off-white-mist: #e5e7eb;
  --ref-soft-stone: #e8e8fc;
  --ref-muted-lavender: #939eeb;
}
```

## Typography direction
- **Geist**: 400, 500, 16px, 20px, 24px, 32px, 60px, 72px, 1.10, 1.22, 1.25, 1.33, 1.40, 1.50; substitute `Inter`.
- **Geist Mono**: 500, 14px, 16px, 1.80; substitute `SF Mono`.
- **Arial Black**: 400, 700, 16px, 20px, 1.50; substitute `Impact`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `tabs: 1000px, cards: 24px, buttons: 9999px, accentShapes: 20px, 24px, 40px`

## Surface cues
- **Obsidian Canvas** `#3a2234`: Primary page background, especially for hero sections.
- **Deep Aubergine** `#333333`: General content section backgrounds, providing a subtle shift from the canvas.
- **Soft Stone** `#e8e8fc`: Elevated cards and interactive components, with a slight tint away from pure white.
- **Ash Gray** `#f3f3f3`: Lightest surface for specific cards and decorative fills, providing maximum contrast on a dark background.

## Component cues
- **Pill Button - Transparent**: Secondary action button, typically for 'Read docs' or similar navigation.
- **Pill Button - Filled**: Primary action button, often for 'Learn more' or calls to action.
- **Pill Button - Light**: Interactive elements within specific modules, like 'Watch intro'.
- **Text Link Button (Ghost)**: Minimal interactive elements where focus is on text and not a prominent button shape.
- **Decorative Accent Card**: Large, irregularly shaped background elements used for visual interest rather than content containment.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
