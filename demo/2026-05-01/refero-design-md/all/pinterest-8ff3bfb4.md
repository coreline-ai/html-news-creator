# Pinterest - Refero Design MD

- Source: https://styles.refero.design/style/8ff3bfb4-6f5e-4e07-83be-56e62ce80d2f
- Original site: https://pinterest.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bright Workshop Canvas — A clean, spacious white background provides the stage for vibrant, curated content, like a well-lit studio.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#211922` | neutral | Primary text or dark surface |
| Ash Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Muted Slate | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#e5e5e0` | neutral | Page background or card surface |
| Pinterest Red | `#e60023` | brand | Action accent / signal color |
| Idea Violet | `#9270d7` | accent | Action accent / signal color |
| Discovery Blue | `#2b48d4` | accent | Action accent / signal color |
| Highlight Yellow | `#fffd92` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-jet-black: #000000;
  --ref-graphite: #211922;
  --ref-ash-gray: #666666;
  --ref-muted-slate: #8c8c8c;
  --ref-whisper-gray: #e5e5e0;
  --ref-pinterest-red: #e60023;
  --ref-idea-violet: #9270d7;
}
```

## Typography direction
- **Pin Sans**: 400, 500, 600, 700, 900, 12px, 14px, 16px, 20px, 32px, 38px, 50px, 70px, 1.00, 1.20, 1.40, 1.50; substitute `Open Sans, Arial`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `cards: 20px, inputs: 16px, buttons: 16px, navigationItems: 12px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Search Bar with Filter Tags**: Reference component style.
- **Cookie Notice Banner**: Reference component style.
- **Primary CTA Button**: Call to action
- **Secondary Ghost Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
