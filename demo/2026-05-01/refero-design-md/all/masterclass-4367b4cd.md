# MasterClass - Refero Design MD

- Source: https://styles.refero.design/style/4367b4cd-b002-4719-a418-cbce020f0d33
- Original site: https://www.masterclass.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Stage Presence

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Canvas | `#222326` | neutral | Primary text or dark surface |
| Graphite Base | `#0d0d0e` | neutral | Primary text or dark surface |
| Deep Slate | `#272c33` | neutral | Primary text or dark surface |
| Subtle Ash | `#191c21` | neutral | Primary text or dark surface |
| Muted Stone | `#211d0d` | neutral | Primary text or dark surface |
| Iron Gray | `#43454c` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#9ea0a9` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#d4d5d9` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-charcoal-canvas: #222326;
  --ref-graphite-base: #0d0d0e;
  --ref-deep-slate: #272c33;
  --ref-subtle-ash: #191c21;
  --ref-muted-stone: #211d0d;
  --ref-iron-gray: #43454c;
  --ref-silver-mist: #9ea0a9;
}
```

## Typography direction
- **Sohne**: 400, 600, 8px, 12px, 14px, 16px, 20px, 22px, 24px, 32px, 48px, 1.00, 1.25, 1.33, 1.45, 1.50, 1.60, 2.50; substitute `Inter`.
- **Sohne Schmal**: 500, 64px, 80px, 0.85, 0.90; substitute `condensed sans-serif like Oswald or Anton`.
- **Ivar Display Condensed**: 400, 64px, 1.10; substitute `Condensed serif like Playfair Display SC or IBM Plex Serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `48px`
- Element Gap: `16px`
- Radius: `cards: 8px, links: 8px, badges: 20px, images: 4px, inputs: 0px, buttons: 8px`

## Surface cues
- **Pitch Black Base** `#000000`: Expansive background for footer and full-width sections.
- **Charcoal Canvas** `#222326`: Primary page background and default card background.
- **Deep Slate Cards** `#272c33`: Elevated card surfaces and specific input containers.
- **Graphite Modules** `#0d0d0`: Background for navigation tabs and interactive modules.

## Component cues
- **Ghost Navigation Button**: Navigation and secondary actions that need to remain subtle.
- **Icon Button (filled)**: Functional icons that require a background.
- **Navigation Tab Button**: Top-level navigation items or filters.
- **Flat Interactive Input**: Search bars and form fields.
- **Hero Checkbox/Radio Button**: Choices within hero sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
