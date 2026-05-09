# Depot - Refero Design MD

- Source: https://styles.refero.design/style/f4636c5b-1342-48b2-b9b1-a82e2182440e
- Original site: https://depot.dev
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space console: focused intensity.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#04040b` | neutral | Primary text or dark surface |
| Night Sky | `#121113` | neutral | Primary text or dark surface |
| Ash Gray | `#323035` | neutral | Primary text or dark surface |
| Storm Gray | `#3c393f` | neutral | Primary text or dark surface |
| Cloud Burst | `#b5b2bc` | neutral | Border, muted text, or supporting surface |
| Snow Drift | `#eeeef0` | neutral | Page background or card surface |
| Terminal Green | `#71d083` | brand | Action accent / signal color |
| Canopy Green | `#366740` | brand | Action accent / signal color |
| Link Blue | `#70b8ff` | accent | Action accent / signal color |
| Twilight Purple | `#473876` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon-black: #04040b;
  --ref-night-sky: #121113;
  --ref-ash-gray: #323035;
  --ref-storm-gray: #3c393f;
  --ref-cloud-burst: #b5b2bc;
  --ref-snow-drift: #eeeef0;
  --ref-terminal-green: #71d083;
  --ref-canopy-green: #366740;
}
```

## Typography direction
- **Red Hat Display Variable**: 400, 500, 600, 700, 14px, 16px, 18px, 20px, 36px, 48px, 60px, 1.00, 1.11, 1.38, 1.40, 1.50; substitute `Segoe UI, sans-serif`.
- **Red Hat Text Variable**: 400, 500, 600, 700, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 1.00, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Roboto, Arial, sans-serif`.
- **Red Hat Mono Variable**: 400, 14px, 18px, 1.43, 1.56; substitute `SFMono-Regular, monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 6px, buttons: 6px, default: 6px, smallElements: 2px, interactiveElements: 10px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Product Tab Selector Cards**: Reference component style.
- **Announcement Banner + Highlight Badge**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Action Button**: Secondary call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
