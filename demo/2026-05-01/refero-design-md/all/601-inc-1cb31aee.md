# 601 Inc. - Refero Design MD

- Source: https://styles.refero.design/style/1cb31aee-608e-4dec-a44d-5745e4fd6bab
- Original site: https://www.rokumaruichi.tokyo
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural film canvas

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Matte | `#090909` | neutral | Primary text or dark surface |
| Greyscale Concrete | `#4f4d3c` | neutral | Border, muted text, or supporting surface |
| Aged Gold | `#ece4b4` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-matte: #090909;
  --ref-greyscale-concrete: #4f4d3c;
  --ref-aged-gold: #ece4b4;
}
```

## Typography direction
- **changeling-neo**: 400, 42px, 230px, 280px, normal; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `21px`
- Element Gap: `9px`
- Radius: `default: 11.9952px`

## Surface cues
- **Midnight Matte** `#090909`: Base page background – the deepest layer.
- **Greyscale Concrete** `#4f4d3c`: Primary surface for individual sections and cards, providing a raised platform against the base.

## Component cues
- **Navigation Link**: Interactive text link for primary navigation.
- **Display Number Block**: Large, decorative numerical text for section headers or visual markers.
- **Interactive Text Button**: Text-based calls to action or navigation elements.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
