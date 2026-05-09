# Yung Studio - Refero Design MD

- Source: https://styles.refero.design/style/2d43b251-ad01-4e59-9068-502457aa0592
- Original site: https://yung.studio
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic Command Center. Pure black canvas where sharp white elements punctuate with precision and ample negative space.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Accent Violet | `#c692ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghost-white: #ffffff;
  --ref-accent-violet: #c692ff;
}
```

## Typography direction
- **PolySans-Slim**: 400, 16px, 20px, 30px, 40px, 1.00, 1.10, 1.35; substitute `Inter`.
- **PolySans-Neutral**: 400, 60px, 160px, 0.90, 1.10; substitute `Inter`.
- **PolySans-Bulky**: 400, 28px, 1.01; substitute `Inter`.

## Spacing / shape
- Section Gap: `60-124px`
- Card Padding: `0px`
- Element Gap: `20-24px`
- Radius: `cards: 0px, buttons: 9999px, default: 10px`

## Component cues
- **Primary Action Button Group**: Reference component style.
- **Stat / Metric Block**: Reference component style.
- **Service / Feature Cards**: Reference component style.
- **Primary Action Button**: Interactive element
- **Naked Content Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
