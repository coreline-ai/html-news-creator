# Mockups made easy - Refero Design MD

- Source: https://styles.refero.design/style/ef545f0f-e7ad-4296-b3eb-65f8d045a5d9
- Original site: https://maneken.app
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
blueprint on white marble

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Slate | `#10151c` | neutral | Primary text or dark surface |
| Soft Fog | `#f4f4f4` | neutral | Page background or card surface |
| Light Steel | `#eaeaea` | neutral | Page background or card surface |
| Muted Stone | `#86868b` | neutral | Border, muted text, or supporting surface |
| Cadet Blue | `#0050b7` | brand | Action accent / signal color |
| Dark Charcoal | `#3e3e3e` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-deep-slate: #10151c;
  --ref-soft-fog: #f4f4f4;
  --ref-light-steel: #eaeaea;
  --ref-muted-stone: #86868b;
  --ref-cadet-blue: #0050b7;
  --ref-dark-charcoal: #3e3e3e;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 800, 10px, 14px, 15px, 18px, 24px, 28px, 40px, 200px, 1.00, 1.20, 1.25, 1.40; substitute `system-ui`.
- **TWKEverett**: 400, 500, 16px, 22px, 24px, 28px, 55px, 60px, 77px, 110px, 1.00, 1.10, 1.20, 1.45; substitute `Montserrat`.
- **Arial**: 400, 500, 13px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `10px`
- Element Gap: `10px`
- Radius: `cards: 10px, images: 10px, buttons: 10px, circular: 100px, heroCards: 15px, cookiesBanner: 12px, smallElements: 3px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and primary card surfaces.
- **Soft Fog** `#f4f4f4`: Secondary background for distinct content sections and elevated card surfaces.
- **Deep Slate** `#10151c`: Dark mode content cards and background surfaces, creating strong contrast for visual content.

## Component cues
- **Primary Action Button**: Main call to action
- **Image Card (Base)**: Displaying product mockups
- **Feature Highlight Card (Light)**: Section highlight cards
- **Feature Highlight Card (Dark)**: Section highlight cards
- **Cookie Consent Button**: Secondary action for dismissals

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
