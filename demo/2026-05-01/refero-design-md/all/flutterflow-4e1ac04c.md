# FlutterFlow - Refero Design MD

- Source: https://styles.refero.design/style/4e1ac04c-02ae-41cf-b588-3f6226a882f8
- Original site: https://flutterflow.io
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Command Center. Expansive dark surfaces punctuated by vivid violet glows, like stars in a night sky.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#060311` | neutral | Primary text or dark surface |
| Slate Deep | `#161320` | neutral | Primary text or dark surface |
| White Star | `#ffffff` | neutral | Page background or card surface |
| Mist Gray | `#9ba1ae` | neutral | Border, muted text, or supporting surface |
| Dark Star | `#333333` | neutral | Primary text or dark surface |
| Deep Violet | `#5800fd` | brand | Action accent / signal color |
| Cosmic Indigo | `#2415c6` | brand | Action accent / signal color |
| Dawn Violet | `#7066ed` | brand | Action accent / signal color |
| Flare Violet | `#882fe8` | brand | Action accent / signal color |
| Action Violet | `#6d5ef9` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #060311;
  --ref-slate-deep: #161320;
  --ref-white-star: #ffffff;
  --ref-mist-gray: #9ba1ae;
  --ref-dark-star: #333333;
  --ref-deep-violet: #5800fd;
  --ref-cosmic-indigo: #2415c6;
  --ref-dawn-violet: #7066ed;
}
```

## Typography direction
- **Urbanist**: 400, 500, 600, 14px, 16px, 18px, 20px, 24px, 32px, 72px, 100px, 120px, 1.00, 1.20, 1.30, 1.50, 1.60; substitute `system-ui`.
- **Inter**: 300, 400, 700, 13px, 14px, 16px, 18px, 20px, 24px, 1.50, 1.60; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `40px`
- Element Gap: `24px`
- Radius: `cards: 24px, links: 16px, buttons: 1440px, minorElements: 12px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Trusted By Banner**: Reference component style.
- **Text Only Button (Nav)**: Navigation and secondary actions
- **Basic Card**: Information grouping without visual distinction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
