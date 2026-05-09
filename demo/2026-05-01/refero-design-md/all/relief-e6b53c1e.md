# Relief - Refero Design MD

- Source: https://styles.refero.design/style/e6b53c1e-644b-4300-b42f-0e64905d1443
- Original site: https://www.relief.app
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Oceanic clarity on a paper white canvas. Illustrations and confident blues guide the user through a clear, calm financial journey.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#f9f7f0` | neutral | Page background or card surface |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Deep Ocean | `#13426f` | brand | Action accent / signal color |
| Hope Blue | `#2e96ff` | brand | Action accent / signal color |
| Subtle Gray | `#616c8a` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#333333` | neutral | Primary text or dark surface |
| Input Charcoal | `#202634` | neutral | Primary text or dark surface |
| Powder Blue | `#bde1f9` | semantic | Action accent / signal color |
| Cerulean Link | `#0254a5` | accent | Action accent / signal color |
| Shadow Tint | `#cde7fb` | neutral | Page background or card surface |

```css
:root {
  --ref-sky-canvas: #f9f7f0;
  --ref-arctic-mist: #ffffff;
  --ref-deep-ocean: #13426f;
  --ref-hope-blue: #2e96ff;
  --ref-subtle-gray: #616c8a;
  --ref-slate-text: #333333;
  --ref-input-charcoal: #202634;
  --ref-powder-blue: #bde1f9;
}
```

## Typography direction
- **Gilroy**: 400, 500, 600, 700, 800, 12px, 14px, 16px, 18px, 20px, 32px, 40px, 49px, 53px, 58px, 0.94, 1.00, 1.10, 1.11, 1.20, 1.29, 1.38, 1.40, 1.43, 1.50, 1.60, 1.63, 1.67, 1.70; substitute `system-ui`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `28px`
- Element Gap: `14px`
- Radius: `cards: 18px, badges: 100px, buttons: 70px, hero-elements: 49px`

## Surface cues
- **Sky Canvas** `#f9f7f0`: Dominant page background, providing a warm, inviting canvas.
- **Arctic Mist** `#ffffff`: Primary surface for cards, input fields, and elevated components, appearing brighter and slightly lifted.
- **Deep Ocean** `#13426f`: Background for feature cards and distinct content blocks, creating a section of visual weight and contrast.
- **Powder Blue** `#bde1f9`: Background for badges and small informational tags, providing a soft chromatic accent on surfaces.

## Component cues
- **Primary Action Button**: Call-to-action button
- **Compact Action Button**: Secondary call-to-action button
- **Dark Feature Card**: Informational display card
- **Review Testimonial Card**: User testimonial display
- **Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
