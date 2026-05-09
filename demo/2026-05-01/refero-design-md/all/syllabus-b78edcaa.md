# Syllabus - Refero Design MD

- Source: https://styles.refero.design/style/b78edcaa-6754-41d7-ac00-0119b41ad88a
- Original site: https://syllabus.io
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital blueprint on cream paper

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Cream | `#fffcf7` | neutral | Page background or card surface |
| Inkwell Violet | `#0d0129` | brand | Action accent / signal color |
| Teal Basin | `#19615c` | brand | Action accent / signal color |
| Glow Yellow | `#fae59b` | accent | Action accent / signal color |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-cream: #fffcf7;
  --ref-inkwell-violet: #0d0129;
  --ref-teal-basin: #19615c;
  --ref-glow-yellow: #fae59b;
  --ref-pitch-black: #000000;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Roobert**: 400, 700, 16px, 20px, 24px, 40px, 48px, 56px, 64px, 1.25, 1.27, 1.40, 1.60, 1.67, 2.00; substitute `system-ui`.
- **Supply**: 400, 20px, 1.60; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `24px`
- Page Max Width: `1280px`
- Radius: `cards: 0px, buttons: 0px, default: 0px, waitlistButton: 4px`

## Component cues
- **Primary Navigation**: The main menu for site navigation.
- **Hero Headline**: Dominant text for the main page introduction.
- **Ghost Waitlist Button**: A primary call to action, outlined, for joining a waitlist.
- **Section Title**: Headline for major content sections, within a distinct background.
- **Callout Block**: Highlights key problems or solutions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
