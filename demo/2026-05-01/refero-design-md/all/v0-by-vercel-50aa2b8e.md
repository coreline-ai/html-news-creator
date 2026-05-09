# v0 by Vercel - Refero Design MD

- Source: https://styles.refero.design/style/50aa2b8e-4760-4379-a3c1-59b65d8576a7
- Original site: https://v0.dev
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
A Machinist's Blueprint. Precision and function are paramount, with every element serving a clear purpose on a clean, technical surface.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Canvas | `#fafafa` | neutral | Page background or card surface |
| Line | `#eaeaea` | neutral | Page background or card surface |
| Subtext | `#666666` | neutral | Border, muted text, or supporting surface |
| Icon | `#7d7d7d` | neutral | Border, muted text, or supporting surface |
| Ink | `#171717` | neutral | Primary text or dark surface |
| Onyx | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-paper-white: #ffffff;
  --ref-canvas: #fafafa;
  --ref-line: #eaeaea;
  --ref-subtext: #666666;
  --ref-icon: #7d7d7d;
  --ref-ink: #171717;
  --ref-onyx: #000000;
}
```

## Typography direction
- **GeistSans**: 400, 500, 600, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 32px, 48px, 1.00, 1.17, 1.25, 1.30, 1.33, 1.43, 1.50, 1.56; substitute `Inter`.
- **GeistMono**: 400, 10px, 1.50; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1440px`
- Radius: `cards: 12px, pills: 9999px, inputs: 12px, buttons: 8px`

## Component cues
- **Main Prompt Input**: Reference component style.
- **Template Filter Pills**: Reference component style.
- **Button Group — Action Hierarchy**: Reference component style.
- **Primary CTA Button**: The main action on a page, like 'Sign Up'.
- **Ghost Navigation Link**: Secondary navigation actions like 'Sign In'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
