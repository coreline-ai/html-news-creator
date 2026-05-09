# Medium - Refero Design MD

- Source: https://styles.refero.design/style/9c92c3d1-a2fe-4a27-a324-826b19501774
- Original site: https://medium.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Literary Cafe, Digital Ink on Vellum.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Vellum Background | `#f7f4ed` | neutral | Page background or card surface |
| Parchment White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#191919` | neutral | Primary text or dark surface |
| Inkwell Black | `#242424` | neutral | Primary text or dark surface |
| Book Text Gray | `#333333` | neutral | Primary text or dark surface |
| Muted Text Gray | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Story Green | `#50b33a` | brand | Action accent / signal color |

```css
:root {
  --ref-vellum-background: #f7f4ed;
  --ref-parchment-white: #ffffff;
  --ref-charcoal-black: #191919;
  --ref-inkwell-black: #242424;
  --ref-book-text-gray: #333333;
  --ref-muted-text-gray: #6b6b6b;
  --ref-story-green: #50b33a;
}
```

## Typography direction
- **medium-content-sans-serif-font**: 400, 16px, 1.20.
- **gt-super**: 400, 120px, 0.83.
- **sohne**: 400, 13px, 14px, 20px, 22px, 1.27, 1.40, 1.43, 1.54.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `buttons: 1386px, pillButtons: 1980px`

## Surface cues
- **Vellum Background** `#f7f4ed`: Base page background
- **Parchment White** `#ffffff`: Subtle surface for minor UI elements or specific content blocks

## Component cues
- **Primary Filled Button**: Call to action button for primary actions.
- **Pill Accent Button**: Secondary call to action button, used primarily in navigation.
- **Header Navigation Link**: Standard text link within the header.
- **Footer Navigation Link**: Muted text links in the footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
