# HyperAktiv - Refero Design MD

- Source: https://styles.refero.design/style/d19c6fc3-1fc6-44a0-9c22-a0a82f7f79b4
- Original site: https://hyperaktiv.li
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast stark blueprint

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Muted Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Dark Text Gray | `#333333` | neutral | Primary text or dark surface |
| Action Blue | `#0000ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-text-black: #000000;
  --ref-muted-gray: #cccccc;
  --ref-dark-text-gray: #333333;
  --ref-action-blue: #0000ff;
}
```

## Typography direction
- **Studiofeixensans**: 400, 700, 14px, 16px, 20px, 22px, 25px, 28px, 42px, 72px, 80px, 90px, 0.89, 1.00, 1.20, 1.22, 1.43, 1.50, 2.00; substitute `Arial Black, Impact`.
- **DM Sans**: 400, 14px, 16px, 20px, 1.25, 1.43; substitute `Inter, Lato`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `15px`
- Element Gap: `10px`
- Radius: `inputs: 0px, buttons: 0px, round-button: 20px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary background for all content, maintaining a high-contrast foundation.
- **Input Surface** `#ffffff`: Background for interactive input fields, slightly bordered to define its area.
- **Actionable Surface** `#0000ff`: Solid, vibrant background for primary interactive elements and specific section footers.

## Component cues
- **Primary Filled Button**: Main call-to-action button, direct and prominent.
- **Outline Button**: Secondary action or informational button.
- **Pill Button**: Small, distinct interactive element for specific actions or navigation.
- **Input Field**: Standard form input for collecting user data.
- **Feature Card (Text Only)**: Divisive content section for features or conceptual blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
