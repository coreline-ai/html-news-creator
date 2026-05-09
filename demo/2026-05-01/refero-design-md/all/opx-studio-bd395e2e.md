# OPX Studio - Refero Design MD

- Source: https://styles.refero.design/style/bd395e2e-58a8-4626-acfa-9be8d6cdf604
- Original site: https://opx.studio
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep night canvas

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#020202` | neutral | Primary text or dark surface |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#292a2c` | neutral | Primary text or dark surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#9b9b9b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight: #020202;
  --ref-void-black: #000000;
  --ref-ghost-gray: #292a2c;
  --ref-snow: #ffffff;
  --ref-slate-mist: #9b9b9b;
}
```

## Typography direction
- **Open Sans**: 400, 18px, 1.67; substitute `Noto Sans`.
- **OPX-Medium**: 400, 18px, 20px, 26px, 35px, 50px, 80px, 111px, 1.00, 1.07, 1.21, 1.29, 1.38, 1.40, 1.42, 1.73; substitute `Montserrat`.
- **Untitled**: 500, 14px, 1.67; substitute `Inter`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 45px, buttons: 45px`

## Component cues
- **Ghost Button**: Outlined clickable element for secondary actions and case study links.
- **Navigation Link**: Primary navigation item.
- **Footer Link**: Informational links in the footer.
- **Content Card Headline**: Headline for project previews.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
