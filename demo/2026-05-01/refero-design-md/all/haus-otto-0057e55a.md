# Haus Otto - Refero Design MD

- Source: https://styles.refero.design/style/0057e55a-8a66-4ffc-9c21-f0b757e580b3
- Original site: https://hausotto.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Monolith — A single, massive black typographic form commands attention against an expansive white background.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute White | `#ffffff` | neutral | Page background or card surface |
| Deep Black | `#000000` | neutral | Primary text or dark surface |
| Desert Ochre | `#af7653` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-white: #ffffff;
  --ref-deep-black: #000000;
  --ref-desert-ochre: #af7653;
}
```

## Typography direction
- **Monument-Regular**: 400, 13px, 20px, 23px, 1.15, 1.16, 1.23, 1.77, 2.00; substitute `IBM Plex Sans`.
- **Monument-Medium**: 400, 216px, normal; substitute `IBM Plex Sans`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `buttons: 0px, default: 0px`

## Component cues
- **Cookie Consent Banner**: Reference component style.
- **Navigation Bar**: Reference component style.
- **Footer Meta Bar**: Reference component style.
- **Global Navigation Link**: Primary site navigation
- **Main Display Headline**: Brand identity, section titles

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
