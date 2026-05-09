# Superlist - Refero Design MD

- Source: https://styles.refero.design/style/13f27e7a-d84f-4ff9-a030-ae4e2c930757
- Original site: https://superlist.com
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Nebula with Neon Traces. A cosmic expanse of deep grays and violet, punctuated by sharp, vivid bursts of color that guide the eye.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#181824` | neutral | Primary text or dark surface |
| Charcoal Surface | `#26253b` | neutral | Primary text or dark surface |
| Nebula Gray | `#696f81` | neutral | Border, muted text, or supporting surface |
| Ghostly Grey | `#8e8da0` | neutral | Border, muted text, or supporting surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |
| Stardust White | `#f7f7ff` | neutral | Page background or card surface |
| Comet Tail Violet | `#535676` | accent | Action accent / signal color |
| Rocket Orange | `#ff4a36` | brand | Action accent / signal color |
| Flare Orange | `#ff3a26` | brand | Action accent / signal color |
| Galaxy Violet | `#9087ff` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #181824;
  --ref-charcoal-surface: #26253b;
  --ref-nebula-gray: #696f81;
  --ref-ghostly-grey: #8e8da0;
  --ref-snow-drift: #ffffff;
  --ref-stardust-white: #f7f7ff;
  --ref-comet-tail-violet: #535676;
  --ref-rocket-orange: #ff4a36;
}
```

## Typography direction
- **Haffer XH SemiBold**: 400, 600, 16px, 18px, 24px, 30px, 48px, 70px, 88px, 0.95, 1.00, 1.10, 1.20, 1.50; substitute `Montserrat`.
- **Haffer XH SemiBold**: 400, 600, 16px, 18px, 24px, 30px, 48px, 70px, 88px, 0.95, 1.00, 1.10, 1.20, 1.50; substitute `Montserrat`.
- **Jersey 10**: 400, 70px, 0.90; substitute `Oswald`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 20px, badges: 8px, inputs: 100px, buttons: 100px`

## Surface cues
- **Deep Space** `#181824`: Primary page background layer
- **Charcoal Surface** `#26253b`: Elevated card backgrounds, navigation panels, interactive elements, creating visible separation from the main page.

## Component cues
- **CTA Button Group**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Cookie Consent Banner**: Reference component style.
- **Navigation Link**: Header navigation items
- **Hero Section Headline**: Prominent page titles

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
