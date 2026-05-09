# Home - Refero Design MD

- Source: https://styles.refero.design/style/606d4af9-9d8c-41ea-a122-f515f38f20e5
- Original site: https://www.fluidtouch.biz
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space productivity

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Astral | `#121318` | neutral | Primary text or dark surface |
| Void Shadow | `#212529` | neutral | Primary text or dark surface |
| Star Dust | `#ffffff` | neutral | Page background or card surface |
| Fuchsia Flare | `#ed1672` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-astral: #121318;
  --ref-void-shadow: #212529;
  --ref-star-dust: #ffffff;
  --ref-fuchsia-flare: #ed1672;
}
```

## Typography direction
- **Poppins**: 400, 700, 14px, 16px, 110px, 1.00, 1.20, 1.25; substitute `sans-serif`.
- **Muli**: 300, 400, 18px, 22px, 1.00, 1.50; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `128px`
- Card Padding: `20px`
- Element Gap: `15px`
- Radius: `buttons: 100px, headings: 100px`

## Component cues
- **Primary Action Button**: Command, navigation
- **Navigation Link**: Site navigation
- **Hero Headline**: Primary page title
- **Body Text**: General content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
