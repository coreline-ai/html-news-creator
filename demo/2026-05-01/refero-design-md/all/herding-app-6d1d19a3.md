# herding.app - Refero Design MD

- Source: https://styles.refero.design/style/6d1d19a3-294d-4bad-9f8b-f775cb24b47a
- Original site: https://herdi.ng
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphite workshop under a soft spotlight. Surfaces are not black, but deep charcoal, illuminated by concentrated white text and a single vibrant highlight for interactive elements.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Slate | `#232320` | neutral | Primary text or dark surface |
| Deep Graphite | `#1c1c1a` | neutral | Primary text or dark surface |
| Ash Stone | `#2e2e2b` | neutral | Primary text or dark surface |
| Iron Oxide | `#35352f` | neutral | Primary text or dark surface |
| Zinc Gray | `#3e3e38` | neutral | Primary text or dark surface |
| Ghost White | `#fffffe` | neutral | Page background or card surface |
| Silver Thread | `#a3a29c` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#75746c` | neutral | Border, muted text, or supporting surface |
| Active Charcoal | `#7f7e77` | accent | Action accent / signal color |

```css
:root {
  --ref-storm-slate: #232320;
  --ref-deep-graphite: #1c1c1a;
  --ref-ash-stone: #2e2e2b;
  --ref-iron-oxide: #35352f;
  --ref-zinc-gray: #3e3e38;
  --ref-ghost-white: #fffffe;
  --ref-silver-thread: #a3a29c;
  --ref-whisper-gray: #75746c;
}
```

## Typography direction
- **Styrene**: 400, 11px, 14px, 15px, 20px, 27px, 45px, 1.12; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `pills: 9999px, buttons: 16px, default: 7.5px`

## Surface cues
- **Page Canvas** `#232320`: The primary background for the entire application, providing a deep, consistent canvas.
- **Base Card** `#2e2e2b`: Standard content containers, slightly raised from the page canvas, indicating primary content blocks.
- **Nested Card** `#1c1c1a`: Containers for content nested within Base Cards or for visually distinct, slightly recessed sections.

## Component cues
- **Sign Up / Log In Button Group with CTA**: Reference component style.
- **How It Works — Steps with CTA**: Reference component style.
- **Collect Content Types — Feature Card**: Reference component style.
- **Primary Action Button**: Interactive element
- **Text Link Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
