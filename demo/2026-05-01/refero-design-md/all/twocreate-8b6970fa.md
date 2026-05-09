# Twocreate - Refero Design MD

- Source: https://styles.refero.design/style/8b6970fa-3478-4c1b-aadf-41ffe1ef68e6
- Original site: https://twocreate.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery brochure on textured paper. A pristine, off-white matte surface serves as the canvas, with sharp, meticulously placed charcoal text drawing the eye to curated content.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#f9f7f4` | neutral | Page background or card surface |
| Charcoal Text | `#0c0c0c` | neutral | Primary text or dark surface |
| Deepest Ink | `#000000` | neutral | Primary text or dark surface |
| Pale Stone Divider | `#e3e1dd` | neutral | Page background or card surface |

```css
:root {
  --ref-greige-canvas: #f9f7f4;
  --ref-charcoal-text: #0c0c0c;
  --ref-deepest-ink: #000000;
  --ref-pale-stone-divider: #e3e1dd;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 10px, 22px, 33px, 44px, 67px, 111px, 1.00, 1.02, 1.10; substitute `Inter`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `20px`
- Element Gap: `10-20px`
- Radius: `all: 0px`

## Component cues
- **Hero Headline Block**: Reference component style.
- **Client List with Image**: Reference component style.
- **Work Project Title Card**: Reference component style.
- **Primary Navigation Link**: Navigational elements in the header and footer.
- **Section Heading**: Subheadings introducing new content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
