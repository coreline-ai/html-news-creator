# 큰그림컴퍼니 - Refero Design MD

- Source: https://styles.refero.design/style/eafe33bf-6f53-4619-b279-686ad5869799
- Original site: https://www.bpco.kr
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
crumpled paper manifesto

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#121212` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Aged Paper | `#f1f1f1` | neutral | Page background or card surface |
| Faded Ink | `#e1e1e1` | neutral | Page background or card surface |

```css
:root {
  --ref-ink-black: #121212;
  --ref-paper-white: #ffffff;
  --ref-aged-paper: #f1f1f1;
  --ref-faded-ink: #e1e1e1;
}
```

## Typography direction
- **Helvetica Neue**: 400, 500, 700, 14px, 15px, 16px, 17px, 20px, 75px, 274px, 1.00, 1.05, 1.06, 1.14, 1.20, 1.29, 1.30, 1.60; substitute `Arial`.
- **PPSupplyMono**: 400, 13px, 16px, 17px, 1.00, 1.20, 2.00; substitute `Space Mono`.
- **PPSupplySans**: 400, 17px, 22px, 1.00, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `10-40px`
- Element Gap: `10px`
- Radius: `image: 288px, button: 40px, default: 20px, navigation: 28px`

## Surface cues
- **Paper White Canvas** `#ffffff`: Primary page background layer, providing the base 'paper' texture.
- **Aged Paper Surface** `#f1f1f1`: Secondary background layer for cards, content blocks, or subtle panels, creating a visual separation from the canvas.

## Component cues
- **Ghost Navigation Button**: Top navigation items and secondary actions.
- **Rounded Button**: General purpose buttons and tags.
- **Text Block Container**: Grouped content sections, text-heavy cards.
- **Accent Star**: Decorative divider or visual break.
- **Hero Text Block**: Large, attention-grabbing typographic display.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
