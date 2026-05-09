# DICE - Refero Design MD

- Source: https://styles.refero.design/style/f4af4c42-2cba-4aa6-8d06-2f728bce702d
- Original site: https://dice.fm
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast monochrome canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#d9d9d9` | neutral | Page background or card surface |
| Cloud White | `#eeeeee` | neutral | Page background or card surface |
| Medium Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Dark Gray | `#595959` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#333333` | neutral | Primary text or dark surface |
| Electric Blue | `#0000fe` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-arctic-white: #ffffff;
  --ref-ash-gray: #d9d9d9;
  --ref-cloud-white: #eeeeee;
  --ref-medium-gray: #808080;
  --ref-dark-gray: #595959;
  --ref-charcoal: #333333;
  --ref-electric-blue: #0000fe;
}
```

## Typography direction
- **Favorit**: 350, 400, 700, 12px, 14px, 16px, 18px, 24px, 28px, 1.15, 1.19, 1.21, 1.22, 1.25, 1.33, 1.40, 1.50; substitute `Inter`.
- **Foggy**: 400, 106px, 0.83; substitute `Impact`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `misc: 20px, cards: 4px, images: 8px, buttons: 40px, navigation: 20px`

## Component cues
- **Primary Action Button**: Main call-to-action
- **Secondary Ghost Button**: Alternative actions or less prominent calls
- **SearchBar Input**: Global site search and filtering
- **Event Card**: Displaying event listings
- **App Download Button**: Link to app stores

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
