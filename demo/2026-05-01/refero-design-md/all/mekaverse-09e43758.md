# MekaVerse - Refero Design MD

- Source: https://styles.refero.design/style/09e43758-12c5-4a2b-8ae8-ded156ef66bf
- Original site: https://themekaverse.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space holographic command center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Light Mist | `#b8bab9` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#e2e2e2` | neutral | Page background or card surface |
| Control Gray | `#444345` | neutral | Border, muted text, or supporting surface |
| Page Blue | `#2e9ec3` | brand | Action accent / signal color |
| Page Red | `#bc1010` | brand | Action accent / signal color |
| Page Pink | `#d69dbb` | brand | Action accent / signal color |
| Page Light Blue | `#20b0d7` | brand | Action accent / signal color |
| Page Blue Grey | `#9faac0` | brand | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-cloud-white: #ffffff;
  --ref-light-mist: #b8bab9;
  --ref-ghost-gray: #e2e2e2;
  --ref-control-gray: #444345;
  --ref-page-blue: #2e9ec3;
  --ref-page-red: #bc1010;
  --ref-page-pink: #d69dbb;
}
```

## Typography direction
- **Roobert**: 400, 26px, 30px, 80px, 0.78, 1.00, 1.15; substitute `Montserrat`.
- **GT America Mono Regular**: 400, 10px, 12px, 1.00, 1.30; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 10px, buttons: 2px, navItems: 2px, containers: 20px`

## Surface cues
- **Void Black Canvas** `#000000`: Primary page background, base layer.
- **Control Gray Surface** `#444345`: Solid button backgrounds, slightly elevated interactive elements.
- **Light Mist Panel** `#b8bab9`: Muted background panels or informational sections, offering slight visual separation.
- **Cloud White Accent** `#ffffff`: Highlight for text or borders on selected components against darker surfaces.

## Component cues
- **Primary Ghost Button**: Interactive element for key actions, appearing as a transparent rectangular outline.
- **Text Link Button**: Minimal interactive element, purely text-based without background or visible border.
- **Dark Filled Button**: Standard button for actions that require slightly more visual emphasis.
- **Muted Action Button**: Less prominent action button, typically for secondary or tertiary functions.
- **Navigation Item**: Individual items within the main navigation, with subtle interactive styling.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
