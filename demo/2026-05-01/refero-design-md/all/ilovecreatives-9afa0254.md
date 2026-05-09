# ilovecreatives - Refero Design MD

- Source: https://styles.refero.design/style/9afa0254-423b-4354-a852-8894c33d2e6b
- Original site: https://ilovecreatives.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black & White Zine

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Code Black | `#000000` | neutral | Primary text or dark surface |
| Text Gray | `#222222` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-code-black: #000000;
  --ref-text-gray: #222222;
}
```

## Typography direction
- **SuisseRegular**: 100, 400, 500, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 32px, 49px, 54px, 0.83, 1.00, 1.05, 1.10, 1.17, 1.20, 1.40, 1.43, 1.80; substitute `Inter`.
- **romana**: 100, 20px, 35px, 53px, 59px, 0.95, 1.00, 1.06, 1.27; substitute `Playfair Display`.
- **Arial**: 100, 10px, 18px, 32px, 1.00, 1.10, 1.40, 2.52.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `4px`
- Radius: `cards: 20px, icons: 8px, buttons: 450px, circularElements: 300px`

## Component cues
- **Pill Button**: Primary Call to Action, interactive elements.
- **Ghost Button**: Secondary actions, inline links disguised as buttons.
- **Rounded Corner Button**: Small, contained interactive elements.
- **Large Ghost Button**: Prominent ghost links or buttons.
- **Feature Card**: Content containers for courses, profiles, or features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
