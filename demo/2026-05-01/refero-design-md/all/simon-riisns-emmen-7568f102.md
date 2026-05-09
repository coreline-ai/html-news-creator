# Simon Riisnæs Emmen - Refero Design MD

- Source: https://styles.refero.design/style/7568f102-d6e4-4113-92a1-4fd53fe5ea47
- Original site: https://xn--smon-vpa.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant billboard minimalism.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Sunset Blush | `#fd8878` | accent | Action accent / signal color |
| Electric Yellow | `#e8fe04` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-sunset-blush: #fd8878;
  --ref-electric-yellow: #e8fe04;
}
```

## Typography direction
- **Tex Gyre Heros**: 300, 400, 29px, 32px, 67px, 173px, 0.90, 1.20; substitute `Helvetica Neue`.
- **Editorial New**: 400, 29px, 1.10, 1.44; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `95px`
- Card Padding: `6px`
- Element Gap: `6px`
- Radius: `default: 0px, displayBlocks: 720px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Electric Yellow** `#e8fe04`: Prominent content blocks / accents
- **Sunset Blush** `#fd8878`: Prominent content blocks / accents

## Component cues
- **Header Navigation Link**: Interactive text link in the page header.
- **Main Navigation/List Item**: Interactive element for the main content list, indicating projects or articles.
- **Headline Display Block - Words**: Primary attention-grabbing headline element, visually distinct product name.
- **Headline Display Block - Designed**: Secondary attention-grabbing headline element, visually distinct product noun.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
