# Vapi - Refero Design MD

- Source: https://styles.refero.design/style/bab34295-03fc-4993-ae42-b440fe78647b
- Original site: https://vapi.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight console, glowing accents

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Midnight | `#0e0e13` | neutral | Primary text or dark surface |
| Charcoal Slate | `#27272a` | neutral | Primary text or dark surface |
| Silver Moonlight | `#d8d7d4` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#fffaea` | neutral | Page background or card surface |
| Faded Steel | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Interface Gray | `#d9e6ef` | neutral | Page background or card surface |
| Soft Black | `#09090b` | neutral | Primary text or dark surface |
| Sunken Black | `#18181b` | neutral | Primary text or dark surface |
| Vapi Orange | `#e96b34` | brand | Action accent / signal color |
| Vapi Mint | `#62f6b5` | brand | Action accent / signal color |

```css
:root {
  --ref-deep-midnight: #0e0e13;
  --ref-charcoal-slate: #27272a;
  --ref-silver-moonlight: #d8d7d4;
  --ref-whisper-white: #fffaea;
  --ref-faded-steel: #a1a1aa;
  --ref-interface-gray: #d9e6ef;
  --ref-soft-black: #09090b;
  --ref-sunken-black: #18181b;
}
```

## Typography direction
- **seasonSans**: 300, 400, 500, 510, 570, 650, 11px, 12px, 14px, 15px, 16px, 18px, 22px, 24px, 32px, 40px, 44px, 56px, 68px, 96px, 120px, 144px, 1.00, 1.09, 1.10, 1.12, 1.14, 1.20, 1.25, 1.32, 1.33, 1.36, 1.43, 1.50, 1.56, 1.60, 1.71; substitute `Inter`.
- **Geist Mono**: 400, 500, 12px, 14px, 16px, 20px, 1.00, 1.30, 1.33, 1.43, 1.50, 1.57, 1.67; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 5.6px, input: 12px, buttons: 9999px, general: 24px`

## Surface cues
- **Base Canvas** `#0e0e13`: Primary page background, deepest layer.
- **Sectional Panel** `#27272a`: Alternating background for content sections, footer background, subtle elevation from base.
- **Interactive Surface** `#09090b`: Background for specific interactive list items or internal UI components, slightly lighter than base canvas but darker than general panels.
- **Light Overlay** `#fffaea`: Background for highly interactive elements like specific buttons or emphasized input fields, creating high contrast against dark text.

## Component cues
- **Header Action Button - Outline**: Secondary action button in the header.
- **Ghost Text Button**: Tertiary action, often within component bodies or navigation.
- **Primary Call-to-Action Button**: Main call to action, typically a filled button.
- **Secondary Call-to-Action Button**: Alternative call to action, typically a filled button.
- **Text Input / Search oval**: Interactive text input field in hero area.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
