# Watch new Originals - Refero Design MD

- Source: https://styles.refero.design/style/e586b296-bfac-4e93-add2-daa384712b39
- Original site: https://www.disneyplus.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: Dark, immersive interfaces punctuated by vivid interactive highlights.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Midnight | `#040714` | neutral | Primary text or dark surface |
| Cool Graphite | `#282a36` | neutral | Primary text or dark surface |
| Sky Blue | `#33ddff` | brand | Action accent / signal color |
| Electric Teal | `#02d6e8` | accent | Action accent / signal color |
| Text Dark | `#02172a` | neutral | Primary text or dark surface |
| Muted Silver | `#e5e7eb` | neutral | Page background or card surface |
| Light Gray | `#c0c0c0` | neutral | Border, muted text, or supporting surface |
| Off-White | `#fafafa` | neutral | Page background or card surface |
| Deep Space | `#0e0b14` | neutral | Primary text or dark surface |
| Ghost Gray | `#b7b8bd` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-midnight: #040714;
  --ref-cool-graphite: #282a36;
  --ref-sky-blue: #33ddff;
  --ref-electric-teal: #02d6e8;
  --ref-text-dark: #02172a;
  --ref-muted-silver: #e5e7eb;
  --ref-light-gray: #c0c0c0;
  --ref-off-white: #fafafa;
}
```

## Typography direction
- **Inspire**: 400, 700, 12px, 14px, 16px, 18px, 20px, 28px, 40px, 1.20, 1.38, 1.40, 1.50, 1.83; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 12px, inputs: 8px, buttons: 8px`

## Surface cues
- **Canvas Blue Black** `#010104`: Base layer for global navigation.
- **Deep Midnight** `#040714`: Primary page background and main content container.
- **Accent Gray** `#1e1f24`: Slightly elevated background for some UI elements that need mild distinction.
- **Cool Graphite** `#282a36`: Backgrounds for interactive elements like input fields, providing slight elevation.

## Component cues
- **Ghost Button**: Navigation, secondary actions, in-content links
- **Primary Action Button**: Main calls to action, form submissions
- **Signup CTA Button**: Specific call to action, usually in hero or signup forms.
- **Default Card**: Content presentation, media cards.
- **Black Background Card**: Emphasized content cards, often for media previews.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
