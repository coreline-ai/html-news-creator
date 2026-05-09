# Revenue-Grade Automation - Refero Design MD

- Source: https://styles.refero.design/style/eeeb6ac9-fc07-4965-935a-e1989ed831f1
- Original site: https://www.default.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Engineered Control Panel: precise, monochromatic, with a focused electric accent.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#202020` | neutral | Primary text or dark surface |
| Cloud Canvas | `#f5f5f5` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Muted Ash | `#333333` | neutral | Primary text or dark surface |
| Ghost Border | `#f7f5fd` | neutral | Page background or card surface |
| Electric Violet | `#5757f8` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #202020;
  --ref-cloud-canvas: #f5f5f5;
  --ref-paper-white: #ffffff;
  --ref-muted-ash: #333333;
  --ref-ghost-border: #f7f5fd;
  --ref-electric-violet: #5757f8;
}
```

## Typography direction
- **NB International Pro**: 500, 700, 26px, 36px, 48px, 64px, 72px, 0.97, 1.00, 1.20; substitute `Montserrat`.
- **Saans Trial**: 500, 700, 14px, 16px, 18px, 20px, 1.20, 1.40, 1.43; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `24px`
- Page Max Width: `1400px`
- Radius: `images: 12px, inputs: 10px, buttons: 1425.6px, default: 8px`

## Surface cues
- **Cloud Canvas** `#f5f5f5`: Base page background, large content sections, primary card backgrounds.
- **Paper White** `#ffffff`: Elevated and interactive elements like input fields, header navigation backgrounds, and secondary card backgrounds.
- **Midnight Ink** `#202020`: Darker, functional surfaces like secondary button backgrounds or specific UI components (though not broadly used as a prominent surface).

## Component cues
- **Primary Action Button**: Main call to action
- **Secondary Action Button**: Secondary call to action or ghost button
- **Navigation Link Button**: Small, informational links
- **Navigation Outlined Button**: Header navigation with subtle styling
- **Default Card**: Information container, background for content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
