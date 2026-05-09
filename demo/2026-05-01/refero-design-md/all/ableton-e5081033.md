# Ableton - Refero Design MD

- Source: https://styles.refero.design/style/e5081033-bd79-479a-aef6-8b002df6086a
- Original site: https://ableton.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital studio. A canvas of stark black and white, illuminated by electric blue.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Studio Gray | `#eeeeee` | neutral | Page background or card surface |
| Electric Violet | `#0000ff` | brand | Action accent / signal color |
| Melody Red | `#ff8389` | accent | Action accent / signal color |
| Synth Teal | `#00d2be` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-studio-gray: #eeeeee;
  --ref-electric-violet: #0000ff;
  --ref-melody-red: #ff8389;
  --ref-synth-teal: #00d2be;
}
```

## Typography direction
- **futura-pt**: 400, 700, 14px, 16px, 20px, 24px, 30px, 40px, 90px, 1.00, 1.20, 1.40, 1.50; substitute `Futura`.

## Spacing / shape
- Section Gap: `69px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Blog Post Card Grid**: Reference component style.
- **Category Tag Collection**: Reference component style.
- **CTA Banner with Input**: Reference component style.
- **Primary Call-to-Action Button**: Action
- **Category Tag Button - Melody Red**: Categorization

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
