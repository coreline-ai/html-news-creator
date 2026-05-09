# robot.com - Refero Design MD

- Source: https://styles.refero.design/style/30dfffb4-ff6d-4128-b3e5-39046ba258f0
- Original site: https://www.robot.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial clarity, digital spark.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#262626` | neutral | Primary text or dark surface |
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |
| Buttered Toast | `#f8f6f3` | neutral | Action accent / signal color |
| Deepest Ink | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#727272` | neutral | Border, muted text, or supporting surface |
| Card Shadow | `#2d2d2d` | neutral | Primary text or dark surface |
| Dusty Lead | `#8f8e8d` | neutral | Border, muted text, or supporting surface |
| Robot Yellow | `#fff65d` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #262626;
  --ref-pure-canvas: #ffffff;
  --ref-buttered-toast: #f8f6f3;
  --ref-deepest-ink: #000000;
  --ref-subtle-gray: #727272;
  --ref-card-shadow: #2d2d2d;
  --ref-dusty-lead: #8f8e8d;
  --ref-robot-yellow: #fff65d;
}
```

## Typography direction
- **Yellix**: 400, 500, 600, 10px, 12px, 14px, 15px, 16px, 18px, 24px, 32px, 38px, 41px, 52px, 72px, 100px, 0.96, 1.00, 1.06, 1.10, 1.16, 1.22, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `173px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `tag: 9999px, buttons: 30px, default: 24px, navItem: 4px`

## Component cues
- **Primary Action Button**: Main call to action
- **Ghost Action Button**: Secondary action or subtle navigation
- **Outline Text Button**: Tertiary navigation or interactive text
- **Dark Card**: Content container on light backgrounds
- **Light Card**: Content container on light backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
