# Michael Wandelmaier - Refero Design MD

- Source: https://styles.refero.design/style/5b405eec-67ba-4dd0-8dab-ace000151a78
- Original site: https://wandelmaier.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark canvas, bold blobs

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas Dark | `#191816` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Soft Gray | `#a9a9a9` | neutral | Border, muted text, or supporting surface |
| Deep Graphite | `#302f2d` | neutral | Primary text or dark surface |
| Spring Bud | `#34a847` | brand | Action accent / signal color |
| Flamingo Pink | `#fbcbcb` | accent | Action accent / signal color |
| Sunset Orange | `#f27851` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-dark: #191816;
  --ref-cloud-white: #ffffff;
  --ref-soft-gray: #a9a9a9;
  --ref-deep-graphite: #302f2d;
  --ref-spring-bud: #34a847;
  --ref-flamingo-pink: #fbcbcb;
  --ref-sunset-orange: #f27851;
}
```

## Typography direction
- **PolySans**: 100, 12px, 24px, 32px, 187px, 0.90, 1.00, 1.33, 2.50, 2.67; substitute `system-ui`.
- **Canela Web**: 100, 40px, 50px, 80px, 1.20, 1.30, 2.40; substitute `Playfair Display`.
- **sans-serif**: 400, 16px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `32px`
- Element Gap: `22px`
- Page Max Width: `1760px`
- Radius: `cards: 10000px, badges: 48px, buttons: 72px`

## Surface cues
- **Canvas Dark** `#191816`: Primary page and section backgrounds, dominant theme for the entire experience.
- **Accent Blob Surface** `#fbcbcb`: Decorative, irregularly shaped background for specific content blocks, introducing bursts of color.

## Component cues
- **Primary Action Button**: Main call to action, visually distinct and interactive.
- **Ghost Outline Button**: Secondary action or navigation link, subtle and integrates with the dark theme.
- **Accent Blob Card - Flamingo Pink**: Decorative background for featured items or visual breaks.
- **Accent Blob Card - Sunset Orange**: Decorative background for featured items or visual breaks.
- **Accent Blob Card - Spring Bud**: Decorative background for featured items or visual breaks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
