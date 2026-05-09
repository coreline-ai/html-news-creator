# Runway - Refero Design MD

- Source: https://styles.refero.design/style/874aaea0-c718-454e-8a58-f3beed1284ec
- Original site: https://runway.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, analytical canvas.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#261b07` | neutral | Primary text or dark surface |
| Stone | `#61594a` | neutral | Border, muted text, or supporting surface |
| Off-White | `#f8f7f5` | neutral | Page background or card surface |
| Pearl | `#ffffff` | neutral | Page background or card surface |
| Faded Stone | `#e3dfd5` | neutral | Page background or card surface |
| Shadow Tint | `#aca89f` | neutral | Border, muted text, or supporting surface |
| Amber Action | `#f9a600` | accent | Action accent / signal color |
| Sunset Orange | `#e89b01` | accent | Action accent / signal color |
| Warning Red | `#f0624f` | accent | Action accent / signal color |
| Grape Badge | `#d5befa` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #261b07;
  --ref-stone: #61594a;
  --ref-off-white: #f8f7f5;
  --ref-pearl: #ffffff;
  --ref-faded-stone: #e3dfd5;
  --ref-shadow-tint: #aca89f;
  --ref-amber-action: #f9a600;
  --ref-sunset-orange: #e89b01;
}
```

## Typography direction
- **Interphases Pro Variable**: 400, 492, 584, 12px, 14px, 16px, 20px, 24px, 36px, 56px, 65px, 72px, 1.00, 1.13, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `32px`
- Element Gap: `4px`
- Page Max Width: `1216px`
- Radius: `cards: 12px, badges: 6px, buttons: 8px, formFields: 4px, interactiveElements: 8px`

## Surface cues
- **Off-White** `#f8f7f5`: Base page background and general canvas.
- **Faded Stone** `#e3dfd5`: Secondary background for subtle section breaks.
- **Pearl** `#ffffff`: Primary surface for cards and elevated components, offering a crisp white base.

## Component cues
- **Primary Action Button (Filled)**: Main call-to-action
- **Secondary Action Button (Outlined)**: Secondary calls-to-action and ghost buttons.
- **Navigation Link Button**: Primary navigation items in header/footer.
- **Standard Card**: Information containers, feature blocks.
- **Elevated Card**: Interactive data panels or forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
