# NaN - Refero Design MD

- Source: https://styles.refero.design/style/71db2a51-118e-42b1-879d-29872d52142f
- Original site: https://www.nan.xyz
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Acid-Green Canvas: A hyper-digital screen, like a glowing terminal displaying custom fonts on a luminous green background.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Screen Mint | `#b7ffb4` | brand | Action accent / signal color |
| Code Green | `#00ff00` | brand | Action accent / signal color |
| Chromatic Blue | `#0000ff` | brand | Action accent / signal color |
| Midnight Graphite | `#262626` | neutral | Primary text or dark surface |
| Absolute Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Mercury Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#efefef` | neutral | Page background or card surface |
| Input Gray | `#767676` | neutral | Border, muted text, or supporting surface |
| Hologram Gradient | `#ffb005` | accent | Action accent / signal color |

```css
:root {
  --ref-screen-mint: #b7ffb4;
  --ref-code-green: #00ff00;
  --ref-chromatic-blue: #0000ff;
  --ref-midnight-graphite: #262626;
  --ref-absolute-black: #000000;
  --ref-paper-white: #ffffff;
  --ref-mercury-gray: #999999;
  --ref-light-steel: #efefef;
}
```

## Typography direction
- **NaN Holo Mono**: 300, 400, 500, 700, 800, 900, 12px, 13px, 14px, 16px, 20px, 24px, 26px, 32px, 45px, 1.00, 1.20, 1.50, 2.00, 2.25, 3.00; substitute `Space Mono`.
- **NaN Holo**: 300, 400, 700, 12px, 16px, 45px, 86px, 1.20, 1.50; substitute `Poppins`.
- **NaNSuperXSerifTextThinItalicPREVIEW**: 400, 216px, 1.00; substitute `Playfair Display Italic`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `29px`
- Element Gap: `5px`
- Radius: `links: 18px, images: 8px, default: 2px, massiveButton: 29.4px`

## Surface cues
- **Page Canvas** `#b7ffb4`: The dominant, luminous background color for the entire site, creating a digital and energetic atmosphere.
- **Secondary Surface** `#262626`: Used for the footer background and sometimes as a contrasting background for interactive elements or cards against the main canvas.
- **Input Surface** `#ffffff`: Pure white background for input fields, offering a clean, distinct area for user interaction.

## Component cues
- **Primary Navigation Link**: Navigational element with underline on hover
- **Primary Button (Filled)**: Call to action button for primary interactions
- **Primary Button (Filled, Left Rounded)**: Used for sequenced or grouped actions, rounded on the left
- **Ghost Button**: Secondary action or subtle navigation
- **Hologram Action Button**: High-impact call to action, often for 'Discover More'

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
