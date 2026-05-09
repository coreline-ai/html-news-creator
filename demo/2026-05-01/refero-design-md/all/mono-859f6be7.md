# mono - Refero Design MD

- Source: https://styles.refero.design/style/859f6be7-9d2d-4da6-a9b7-baa658172696
- Original site: https://mono.frm.fm/en
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural grid on white

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#292929` | neutral | Primary text or dark surface |
| Deep Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #292929;
  --ref-deep-black: #000000;
}
```

## Typography direction
- **NH**: 100, 300, 400, 16px, 18px, 25px, 32px, 40px, 43px, 1.20, 1.25, 1.27, 1.34, 1.50; substitute `Helvetica Neue`.
- **S-Condensed**: 300, 400, 500, 12px, 14px, 40px, 0.90, 1.18, 1.20, 1.34; substitute `Impact`.
- **EV**: 100, 28px, 0.90; substitute `Roboto Thin`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `none: 0px`

## Component cues
- **Outline Button**: Primary and secondary actions with minimal visual weight.
- **Minimal Input Field**: Standard text input fields.
- **Navigation Link**: Top-level navigation items and language selectors.
- **Section Heading**: Major content section titles.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
