# Join Parker - Refero Design MD

- Source: https://styles.refero.design/style/f08f9870-2018-4c0b-80d4-0b2e525ff49c
- Original site: https://www.getparker.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Matte bluescreen material

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Off-Black | `#1b1d20` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Medium Gray | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#f2f1ec` | neutral | Page background or card surface |
| Border Gray | `#e1dfd8` | neutral | Page background or card surface |
| Input Border | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Parker Blue | `#5196fe` | brand | Action accent / signal color |
| Parker Orange | `#f9754e` | brand | Action accent / signal color |
| Alert Blue | `#f4ebff` | accent | Action accent / signal color |

```css
:root {
  --ref-off-black: #1b1d20;
  --ref-pure-white: #ffffff;
  --ref-medium-gray: #6e6e6e;
  --ref-ash-gray: #f2f1ec;
  --ref-border-gray: #e1dfd8;
  --ref-input-border: #a3a3a3;
  --ref-parker-blue: #5196fe;
  --ref-parker-orange: #f9754e;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 14px, 16px, 18px, 19px, 20px, 32px, 48px, 64px, 1.05, 1.13, 1.16, 1.42, 1.43, 1.50, 1.55; substitute `system-ui`.
- **Gambetta**: 500, 51px, 64px, 1.05, 1.16; substitute `Georgia`.
- **system-ui**: 400, 500, 600, 14px, 16px, 1.42, 1.5.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, badges: 12.8px, inputs: 12px, buttons: 1584px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for the overall page, providing a clean, bright foundation.
- **Accent Surface** `#f2f1ec`: A subtle, slightly off-white background for specific sections or contained UI elements to add visual texture without strong contrast.
- **Interactive Surface** `#5196fe`: Background for selected interactive elements or larger brand-accented blocks, creating visual prominence.

## Component cues
- **Primary Action Button (Orange)**: Call to action
- **Outlined Action Button (Blue)**: Secondary action or link
- **Neutral Ghost Button**: Tertiary action or navigation
- **Feature Card**: Content container
- **Input Field**: User input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
