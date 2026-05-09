# Home - Refero Design MD

- Source: https://styles.refero.design/style/84c9c7ab-c0b5-437f-b2bf-dc2fd8a61681
- Original site: https://www.savor.it
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm artisanal luxury

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Buttermilk Cream | `#fff9eb` | neutral | Page background or card surface |
| Toasted Oat | `#f0e7d7` | neutral | Page background or card surface |
| Balsamic Black | `#000000` | neutral | Primary text or dark surface |
| Cacao Ink | `#370808` | brand | Action accent / signal color |

```css
:root {
  --ref-buttermilk-cream: #fff9eb;
  --ref-toasted-oat: #f0e7d7;
  --ref-balsamic-black: #000000;
  --ref-cacao-ink: #370808;
}
```

## Typography direction
- **Roslindale Display Condensed**: 300, 120px, 140px, 0.86, 0.90; substitute `Playfair Display`.
- **Suisse Intl**: 400, 700, 14px, 16px, 18px, 21px, 22px, 28px, 40px, 1.24, 1.25, 1.35, 1.45; substitute `Inter`.

## Spacing / shape
- Section Gap: `95px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `forms: 5px, buttons: 5px, toggles: 5px`

## Component cues
- **Primary Filled Button**: Call to action button
- **Secondary Outlined Button**: Alternative action button
- **Subtle Ghost Button**: Tertiary action, internal link button
- **Feature Card**: Content container for features or articles
- **Badge/Tag**: Informational labels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
