# Astro - Refero Design MD

- Source: https://styles.refero.design/style/e8c604cc-1c8d-42a3-aeca-fcfc25e70344
- Original site: https://astro.build
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space console light show. Gradient-infused dark surfaces illuminated by precise, vibrant accents and high-contrast text.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#060913` | neutral | Primary text or dark surface |
| Void Shadow | `#0c0f19` | neutral | Primary text or dark surface |
| Stardust | `#858b98` | neutral | Border, muted text, or supporting surface |
| Lunar Gray | `#545864` | neutral | Border, muted text, or supporting surface |
| Aurora | `#f2f6fa` | neutral | Page background or card surface |
| White Dwarf | `#ffffff` | neutral | Page background or card surface |
| Interstellar Gradient Alpha | `#b845ed` | brand | Action accent / signal color |
| Interstellar Gradient Beta | `#f041ff` | brand | Action accent / signal color |
| Interstellar Gradient Gamma | `#2f4cb3` | brand | Action accent / signal color |
| Cosmic Sparkle Vivid | `#4bf3c8` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #060913;
  --ref-void-shadow: #0c0f19;
  --ref-stardust: #858b98;
  --ref-lunar-gray: #545864;
  --ref-aurora: #f2f6fa;
  --ref-white-dwarf: #ffffff;
  --ref-interstellar-gradient-alpha: #b845ed;
  --ref-interstellar-gradient-beta: #f041ff;
}
```

## Typography direction
- **ui-sans-serif**: 300, 400, 500, 600, 700, 14px, 16px, 20px, 1.00, 1.40, 1.50, 1.65, 1.81; substitute `Inter`.
- **Obviously**: 300, 400, 700, 20px, 30px, 36px, 48px, 1.10, 1.11, 1.20, 1.40; substitute `Poppins`.
- **ui-monospace**: 300, 400, 14px, 1.65; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `cards: 16px, badges: 8px, buttons: 9999px`

## Component cues
- **Hero CTA Buttons + Version Badge**: Reference component style.
- **Feature Cards — What is Astro?**: Reference component style.
- **Themes Tab Selector + Cards**: Reference component style.
- **Primary Filled Button**: Call to action
- **Subtle Pill Button**: Secondary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
