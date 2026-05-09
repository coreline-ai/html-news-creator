# Square - Refero Design MD

- Source: https://styles.refero.design/style/86a6814d-2485-4fad-b6fd-56c2d0a23620
- Original site: https://squareup.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Utility, Intuitive Flow. The UI emphasizes clarity and direct interaction, like operating a well-designed tool.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Blue | `#006aff` | brand | Action accent / signal color |
| Ink Black | `#1a1a1a` | neutral | Primary text or dark surface |
| Graphite | `#737373` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Black | `#030303` | neutral | Primary text or dark surface |
| Light Fog | `#f2f2f2` | neutral | Page background or card surface |
| Ash Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#d9d9d9` | neutral | Page background or card surface |
| Stone Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-sky-blue: #006aff;
  --ref-ink-black: #1a1a1a;
  --ref-graphite: #737373;
  --ref-pure-white: #ffffff;
  --ref-deep-black: #030303;
  --ref-light-fog: #f2f2f2;
  --ref-ash-gray: #cccccc;
  --ref-silver-mist: #d9d9d9;
}
```

## Typography direction
- **Square Sans Display VF**: 400, 500, 16px, 20px, 24px, 32px, 50px, 62px, 86px, 0.97, 1.10, 1.12, 1.19, 1.25, 1.30, 1.33, 1.42, 1.50; substitute `Inter`.
- **Square Sans Text VF**: 400, 500, 12px, 14px, 16px, 1.38, 1.43, 1.50, 1.71, 1.75, 2.00, 2.63; substitute `Inter`.
- **Cash Sans**: 500, 18px, 1.00, 1.50; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `20px`
- Element Gap: `10-20px`
- Radius: `none: 0px, large: 20px, small: 4px, medium: 5px, circular: 32px, extraLarge: 24px`

## Component cues
- **Button Group**: Reference component style.
- **Feature Cards**: Reference component style.
- **Email Signup Form**: Reference component style.
- **Primary Action Button**: Main call to action.
- **Secondary Outline Button**: Secondary calls to action, navigation links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
