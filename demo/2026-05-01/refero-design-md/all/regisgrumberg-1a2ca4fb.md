# Regisgrumberg - Refero Design MD

- Source: https://styles.refero.design/style/1a2ca4fb-1087-4fd0-83ba-590bc63f54ee
- Original site: https://www.regisgrumberg.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black canvas, white light

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Star Dust | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Iron Oxide | `#363636` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-space: #000000;
  --ref-star-dust: #ffffff;
  --ref-ghost-gray: #c4c4c4;
  --ref-iron-oxide: #363636;
}
```

## Typography direction
- **monospace**: 400, 13px, 1.00, 1.20; substitute `'IBM Plex Mono', 'Fira Code', 'JetBrains Mono'`.
- **Times**: 400, 1.00; substitute `'Times New Roman', 'Georgia'`.
- **Montserrat**: 400, 600, 11px, 14px, 18px, 24px, 30px, 36px, 1.00, 1.20, 2.78; substitute `'Inter', 'Lato'`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `23px`
- Element Gap: `23px`
- Page Max Width: `100px`
- Radius: `circle: 100%, elements: 2px`

## Surface cues
- **Deep Space Canvas** `#000000`: Primary page background and default surface for most content.
- **Iron Oxide Secondary** `#363636`: Subtle background for UI elements like navigation bars, providing minimal differentiation.
- **Star Dust Interactive** `#ffffff`: Background for isolated interactive elements like circular buttons, creating a focal point.

## Component cues
- **Text Only Button - default**: Minimal interactive element, common for navigation or secondary actions.
- **Text Only Button - ghost**: Minimal interactive element for navigation or secondary actions on dark backgrounds.
- **Circular Interactive Button**: Prominent interactive element for primary calls to action, like 'Enter'.
- **Navigation Link**: Interactive text link within navigation areas.
- **Hero Headline**: Dominant display text for main page sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
