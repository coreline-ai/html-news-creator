# Duolingo - Refero Design MD

- Source: https://styles.refero.design/style/95b472c5-fc07-46a8-a11f-c5432e290fcd
- Original site: https://www.duolingo.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Green Arcade

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Duolingo Green | `#58cc02` | brand | Action accent / signal color |
| Background Green Accent | `#d7ffb8` | brand | Action accent / signal color |
| Action Blue | `#1cb0f6` | brand | Action accent / signal color |
| Dark Heading Blue | `#042c60` | brand | Action accent / signal color |
| Deep Violet Accent | `#000437` | brand | Action accent / signal color |
| Shadowed Pine | `#3c3c3c` | neutral | Primary text or dark surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#777777` | neutral | Border, muted text, or supporting surface |
| Charcoal Text | `#4b4b4b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-duolingo-green: #58cc02;
  --ref-background-green-accent: #d7ffb8;
  --ref-action-blue: #1cb0f6;
  --ref-dark-heading-blue: #042c60;
  --ref-deep-violet-accent: #000437;
  --ref-shadowed-pine: #3c3c3c;
  --ref-jet-black: #000000;
  --ref-arctic-white: #ffffff;
}
```

## Typography direction
- **din-round**: 500, 700, 13px, 14px, 15px, 17px, 19px, 32px, 1.15, 1.18, 1.20, 1.21, 1.23, 1.33, 1.40, 1.41, 1.47; substitute `system-ui`.
- **feather**: 700, 48px, 64px, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `101px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `links: 12px, buttons: 12px`

## Component cues
- **Primary Action Button (Filled)**: Main call to action
- **Secondary Action Button (Outlined)**: Secondary call to action, alternative options
- **Ghost Button (Neutral)**: Tertiary action, navigation
- **Muted Navigation Button**: Language switcher, secondary navigation
- **Primary Headline**: Page title, main section headings

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
