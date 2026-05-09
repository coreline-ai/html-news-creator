# Deno - Refero Design MD

- Source: https://styles.refero.design/style/973dcf14-2237-4346-81af-3d8c811666c2
- Original site: https://deno.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clean Code Canvas — a pristine digital workspace where clarity and functionality are paramount.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormy Night | `#0a0e1c` | neutral | Primary text or dark surface |
| Cloud Gray | `#cbd1e1` | neutral | Border, muted text, or supporting surface |
| Deno Green | `#70ffaf` | brand | Action accent / signal color |
| Slate Blue | `#a8b2c8` | neutral | Action accent / signal color |
| Ocean Blue | `#0077cc` | accent | Action accent / signal color |
| Code Black | `#000000` | neutral | Primary text or dark surface |
| Frost White | `#ffffff` | neutral | Page background or card surface |
| Pale Gray | `#e5e7eb` | neutral | Page background or card surface |
| Whisper White | `#f8f9fc` | neutral | Page background or card surface |
| Success Green | `#116329` | semantic | Action accent / signal color |

```css
:root {
  --ref-stormy-night: #0a0e1c;
  --ref-cloud-gray: #cbd1e1;
  --ref-deno-green: #70ffaf;
  --ref-slate-blue: #a8b2c8;
  --ref-ocean-blue: #0077cc;
  --ref-code-black: #000000;
  --ref-frost-white: #ffffff;
  --ref-pale-gray: #e5e7eb;
}
```

## Typography direction
- **Inter**: 400, 700, 12px, 14px, 16px, 18px, 20px, 27px, 28px, 36px, 44px, 72px, 1.00, 1.10, 1.25, 1.33, 1.43, 1.50, 1.56, 2.00; substitute `system-ui, sans-serif`.
- **Menlo**: 400, 650, 700, 14px, 16px, 20px, 1.40, 1.45, 1.50; substitute `monospace`.
- **Recursive**: 400, 16px, 18px, 1.50, 1.56; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48-56px`
- Card Padding: `16-32px`
- Element Gap: `8-16px`
- Radius: `cards: 6px, pills: 9997px, buttons: 6px, general: 6px`

## Component cues
- **Button Group — Primary, Secondary, GitHub**: Reference component style.
- **Stats Card — Rating, Community, Ecosystem**: Reference component style.
- **Search Input Field**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Secondary Ghost Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
