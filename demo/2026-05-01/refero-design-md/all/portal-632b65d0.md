# Portal - Refero Design MD

- Source: https://styles.refero.design/style/632b65d0-17de-4972-a3d1-63d5ab062ab8
- Original site: https://portalgaming.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center, glowing violet portals.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Twilight Ink | `#0f0f13` | neutral | Primary text or dark surface |
| Graphite Border | `#292929` | neutral | Primary text or dark surface |
| Dark Indigo | `#2a2a36` | neutral | Primary text or dark surface |
| Off-White Text | `#e6e6e6` | neutral | Page background or card surface |
| Muted Silver | `#9e9e9e` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Portal Violet | `#b296f8` | brand | Action accent / signal color |
| Violet Shadow | `#241e32` | accent | Action accent / signal color |
| Lavender Mist | `#dbeafe` | semantic | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-twilight-ink: #0f0f13;
  --ref-graphite-border: #292929;
  --ref-dark-indigo: #2a2a36;
  --ref-off-white-text: #e6e6e6;
  --ref-muted-silver: #9e9e9e;
  --ref-pure-white: #ffffff;
  --ref-portal-violet: #b296f8;
}
```

## Typography direction
- **Suisse Intl**: 400, 500, 600, 900, 12px, 14px, 16px, 18px, 36px, 48px, 72px, 1.00, 1.11, 1.33, 1.43, 1.50, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 10px, badges: 0px, buttons: 10px, default: 10px`

## Surface cues
- **Void Black Canvas** `#000000`: Base background for the entire application, and high-DURABILITY cards.
- **Twilight Ink Panel** `#0f0f13`: Main background for elevated cards and UI components, providing a subtle lift from the canvas.
- **Gradient Backdrop** `#231f2f`: Decorative base for sections, adding depth with a subtle linear gradient from dark tones.

## Component cues
- **Filled Violet Button**: Primary call to action.
- **Outline Ghost Button**: Secondary action or subtle navigation.
- **Subtle Action Button**: Tertiary action or minor interactive elements, often within larger components.
- **Padded Elevated Card**: Content container for features or articles, providing visual separation and emphasis.
- **Transparent Content Card**: Containers for imagery or specific content blocks, integrated seamlessly into the background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
