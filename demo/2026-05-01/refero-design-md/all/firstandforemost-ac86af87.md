# Firstandforemost - Refero Design MD

- Source: https://styles.refero.design/style/ac86af87-6f60-42a2-b805-87a168792e55
- Original site: https://firstandforemost.co
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Orange Canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Blaze | `#ff4501` | brand | Action accent / signal color |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Vanilla Cream | `#ffefe9` | neutral | Page background or card surface |
| Dusty Rose | `#ffc2a9` | neutral | Border, muted text, or supporting surface |
| Obsidian Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-amber-blaze: #ff4501;
  --ref-arctic-mist: #ffffff;
  --ref-vanilla-cream: #ffefe9;
  --ref-dusty-rose: #ffc2a9;
  --ref-obsidian-ink: #000000;
}
```

## Typography direction
- **NeueMontreal**: 100, 400, 700, 16px, 22px, 26px, 36px, 58px, 80px, 200px, 0.80, 1.00, 1.20, 1.36, 1.40, 1.45; substitute `Montserrat, system-ui`.

## Spacing / shape
- Section Gap: `160px`
- Card Padding: `40-60px`
- Element Gap: `30-50px`
- Radius: `buttons: 80px`

## Surface cues
- **Vanilla Cream Canvas** `#ffefe9`: Primary page background and foundational surface
- **Amber Blaze Surface** `#ff4501`: Prominent background sections, acting as a vibrant canvas for inverted text
- **Arctic Mist Card** `#ffffff`: Secondary background for components like buttons or internal cards within Amber Blaze sections

## Component cues
- **Text Link**: Standard inline link for navigation and supplementary information.
- **Hero Text Button**: Purely text-based button variant, often used for secondary actions or navigation within hero sections.
- **Filled Primary Button**: High-emphasis call to action for key user behaviors.
- **Filled Secondary Button**: Alternative filled button for actions of lesser prominence, or when Amber Blaze is the background.
- **Avatar Button**: Circular button for profile images or icons.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
