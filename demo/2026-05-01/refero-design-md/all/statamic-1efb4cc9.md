# Statamic - Refero Design MD

- Source: https://styles.refero.design/style/1efb4cc9-0923-4d4f-884a-b06d4fca4db2
- Original site: https://statamic.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cloud-nine productivity with subtle magic.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#191a1b` | neutral | Primary text or dark surface |
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#beb9b3` | neutral | Border, muted text, or supporting surface |
| Smoked Pearl | `#5e5a5a` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Charcoal Text | `#4e5154` | neutral | Border, muted text, or supporting surface |
| Subtle Grey | `#cbd5e0` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#3f3f46` | neutral | Primary text or dark surface |
| Sky Tint | `#d7e5fe` | brand | Action accent / signal color |
| Amethyst Aura | `#4c305a` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #191a1b;
  --ref-cloud-canvas: #ffffff;
  --ref-slate-mist: #beb9b3;
  --ref-smoked-pearl: #5e5a5a;
  --ref-stone-gray: #c2c2c2;
  --ref-charcoal-text: #4e5154;
  --ref-subtle-grey: #cbd5e0;
  --ref-steel-gray: #3f3f46;
}
```

## Typography direction
- **p22-mackinac-pro**: 100, 300, 400, 700, 20px, 24px, 30px, 60px, 80px, 96px, 1.00, 1.20, 1.40, 1.50; substitute `Georgia`.
- **Lexend**: 300, 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 36px, 1.00, 1.11, 1.25, 1.33, 1.43, 1.50, 1.56, 1.63, 2.00; substitute `Inter`.
- **code-saver**: 300, 700, 12px, 14px, 16px, 20px, 1.33, 1.43, 1.50, 2.00; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 16px, pills: 9999px, buttons: 8px, default: 8px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary background for the entire page.
- **Card Base** `#ffffff`: Background for standard cards, slightly elevated via shadow.
- **Frosted Card** `#ffffff`: Slightly translucent card backgrounds for a layered, atmospheric effect.
- **Dark Section** `#191a1b`: Background for hero sections or content blocks that require high contrast.

## Component cues
- **Primary Filled Button**: Main call to action
- **Secondary Outlined Button**: Alternative action, less emphasis
- **Tertiary Lavender Button**: Prominent interactive elements with a brand accent
- **Accent Rounded Button**: Specific interactive moments, often within a UI card
- **Clean Product Card**: Showcasing features or content with clear separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
