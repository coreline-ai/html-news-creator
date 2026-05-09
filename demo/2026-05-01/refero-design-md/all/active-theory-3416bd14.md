# Active Theory - Refero Design MD

- Source: https://styles.refero.design/style/3416bd14-96bb-4c23-bd01-b2ea178ba5ce
- Original site: https://activetheory.net
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Console. Deep, dark surfaces punctuated by precise, glowing UI elements.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#c6c6c6` | neutral | Border, muted text, or supporting surface |
| Subtle Violet | `#343755` | brand | Action accent / signal color |
| Highlight Violet | `#9ca5ff` | brand | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-ash-gray: #4d4d4d;
  --ref-pure-white: #ffffff;
  --ref-silver-mist: #c6c6c6;
  --ref-subtle-violet: #343755;
  --ref-highlight-violet: #9ca5ff;
}
```

## Typography direction
- **nbarchitekt**: 400, 700, 10px, 12px, 14px, 1.20, 1.50, 3.00; substitute `Montserrat`.
- **Arial**: 400, 13px, 1.20; substitute `Arial`.
- **Times**: 400, 16px, 1.20, 1.88; substitute `Times New Roman`.

## Spacing / shape
- Radius: `max: 500px, min: 5px, cards: 12px, buttons: 5px or 500px`

## Component cues
- **Cookie Consent Box**: Reference component style.
- **Button Group — Ghost + Primary + Secondary**: Reference component style.
- **Navigation Bar — Ghost Pill**: Reference component style.
- **Standard Ghost Button**: Navigation and secondary actions
- **Primary Pill Button**: Key calls to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
