# Vivid+Co - Refero Design MD

- Source: https://styles.refero.design/style/8875b14e-c59a-492f-8780-8027a480f21c
- Original site: https://vividand.co
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight refractography. A dark, expansive canvas lit by precise typography and spectral light refractions.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ink | `#000000` | neutral | Primary text or dark surface |
| Refined White | `#fffdf9` | neutral | Page background or card surface |
| Stonewash Gray | `#6f879c` | accent | Action accent / signal color |
| Outline Gray | `#403f3f` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-ink: #000000;
  --ref-refined-white: #fffdf9;
  --ref-stonewash-gray: #6f879c;
  --ref-outline-gray: #403f3f;
}
```

## Typography direction
- **Neue Montreal**: 400, 700, 14px, 15px, 17px, 18px, 20px, 21px, 22px, 32px, 33px, 36px, 56px, 105px, 136px, 1.00, 1.01, 1.13, 1.17, 1.20, 1.24, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `108px`
- Card Padding: `20px`
- Element Gap: `7px`
- Radius: `cards: 15px, default: 0px, navItems: 5px`

## Component cues
- **Navigation Link (Active)**: Primary navigation item, active state
- **Navigation Link (Default)**: Primary navigation item, default state
- **Ghost Button (Primary Action)**: Call-to-action button, outlined style
- **Text Button (Subtle)**: Secondary action or categorized link
- **Feature Card**: Container for content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
