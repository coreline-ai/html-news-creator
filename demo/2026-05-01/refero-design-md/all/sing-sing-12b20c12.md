# Sing-sing - Refero Design MD

- Source: https://styles.refero.design/style/12b20c12-27f8-4938-89ba-569404d36fe8
- Original site: https://sing-sing.co
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
sunny minimal exhibition

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Canvas | `#fcd579` | brand | Action accent / signal color |
| Midnight Ink | `#171717` | neutral | Primary text or dark surface |
| Jade Accent | `#81d6b9` | accent | Action accent / signal color |

```css
:root {
  --ref-amber-canvas: #fcd579;
  --ref-midnight-ink: #171717;
  --ref-jade-accent: #81d6b9;
}
```

## Typography direction
- **untitledsans**: 400, 700, 16px, 23px, 24px, 147px, 1.00, 1.15, 1.22; substitute `Arial`.
- **signifier**: 400, 20px, 21px, 1.15, 1.20, 1.30; substitute `Georgia`.

## Spacing / shape
- Section Gap: `35px`
- Card Padding: `23px`
- Element Gap: `5px`
- Radius: `none: 0px`

## Component cues
- **Primary Navigation Link (Default)**: Interactive text link within the main navigation.
- **Navigation Divider (Active State)**: Subtle visual indicator for active or highlighted navigation items.
- **Decorative Headline**: Large, attention-grabbing text for main titles or section headers.
- **Body Text Block (Untitled Sans)**: Standard body copy for general information.
- **Body Text Block (Signifier)**: Secondary body copy or descriptive text, often with a more traditional feel.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
