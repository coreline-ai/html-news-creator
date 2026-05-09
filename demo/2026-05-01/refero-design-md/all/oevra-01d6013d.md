# Oevra - Refero Design MD

- Source: https://styles.refero.design/style/01d6013d-a176-4a22-b7dd-fbd113592956
- Original site: https://oevra.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Misty Forest Canvas — a serene, expansive background in soft green hues, grounding light, transparent elements.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Moss Green | `#778643` | brand | Action accent / signal color |
| Charcoal Gray | `#4e4e4e` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#c8c8c8` | neutral | Border, muted text, or supporting surface |
| Pale Mist | `#efefef` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-black: #000000;
  --ref-moss-green: #778643;
  --ref-charcoal-gray: #4e4e4e;
  --ref-whisper-gray: #c8c8c8;
  --ref-pale-mist: #efefef;
}
```

## Typography direction
- **space-regular**: 400, 8px, 12px, 14px, 15px, 1.2, 1.25, 1.3, 1.5.
- **Suisse Light**: 400, 34px, 45px, 75px, 90px, 1.00, 1.10; substitute `Helvetica Neue`.
- **Suisse Regular**: 400, 12px, 14px, 15px, 1.20, 1.25, 1.30; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `30px`
- Element Gap: `15px`
- Page Max Width: `1425px`
- Radius: `cards: 15px, buttons: 22.5px`

## Surface cues
- **Canvas White** `#ffffff`: The primary background for the page, providing a clean base that occasionally overlaps with the background gradient.
- **Pale Mist** `#efefef`: Alternative background for sections requiring a subtle differentiation from the main canvas.
- **Smoke Glass** `#ffffff1a`: Transparent card backgrounds, creating a layered, frosted glass effect.
- **Light Card** `#ffffffe6`: More opaque card backgrounds for content that needs to stand out more prominently.

## Component cues
- **Ghost Button (White)**: Header navigation links and secondary calls to action.
- **Ghost Button (Charcoal)**: Muted actions or tertiary navigation.
- **Primary Action Button**: Key interactions and calls to action.
- **Transparent Card**: Layered content containers over background sections.
- **Light Card**: Prominent content containers requiring more visual weight.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
