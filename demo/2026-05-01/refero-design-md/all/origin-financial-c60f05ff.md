# Origin Financial - Refero Design MD

- Source: https://styles.refero.design/style/c60f05ff-2420-4a24-92db-80c4b6a74683
- Original site: https://www.useorigin.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center – screens glowing with data against a dark, seamless backdrop.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0f1011` | neutral | Primary text or dark surface |
| Elevated Charcoal | `#2e2e2e` | neutral | Primary text or dark surface |
| Slate Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Faded Mist | `#f5f5f7` | neutral | Page background or card surface |
| Subtle Ash | `#cacaca` | neutral | Border, muted text, or supporting surface |
| Whisper Blue | `#6a6b6b` | neutral | Action accent / signal color |
| Ocean Glimmer | `#00b3dd` | accent | Action accent / signal color |
| Violet Haze | `#847dff` | accent | Action accent / signal color |
| Lavender Mist | `#d1c9ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0f1011;
  --ref-elevated-charcoal: #2e2e2e;
  --ref-slate-canvas: #000000;
  --ref-ghost-white: #ffffff;
  --ref-faded-mist: #f5f5f7;
  --ref-subtle-ash: #cacaca;
  --ref-whisper-blue: #6a6b6b;
  --ref-ocean-glimmer: #00b3dd;
}
```

## Typography direction
- **Lyondisplay App**: 300, 400, 38px, 80px, 96px, 0.90, 1.00; substitute `Playfair Display, Lora`.
- **Suisseintltrial**: 400, 11px, 14px, 16px, 1.00, 1.50, 1.67, 2.18; substitute `Montserrat, Lato`.
- **Suisseintl**: 300, 400, 12px, 14px, 16px, 18px, 1.00, 1.41, 1.43, 1.50, 2.00; substitute `Inter, Roboto`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, buttons: 8px, largeCards: 30px, pillButtons: 1440px, circularElements: 14385.6px`

## Surface cues
- **Midnight Ink Canvas** `#0f1011`: Primary base background for the entire application, providing a deep, consistent dark theme.
- **Elevated Charcoal Card** `#2e2e2`: Background for cards and secondary content blocks, slightly elevating them from the base canvas without heavy shadows.
- **Slate Canvas Input** `#000000`: Used for interactive elements like input fields and some button backgrounds, providing a distinct contrast for usability against deeper neutrals.

## Component cues
- **Primary Ghost Button**: Main call to action on dark backgrounds.
- **Light Filled Button**: Call to action on dark backgrounds where immediate strong contrast is needed.
- **Circular Micro Button**: Small, interactive buttons for secondary actions or toggles.
- **Pill Input Field**: Search bars or prominent single-line text inputs.
- **Themed Content Card**: Displaying data or information with a unique thematic background color.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
