# Gocardless - Refero Design MD

- Source: https://styles.refero.design/style/48ae4f04-21cb-4ab3-8752-33b626a48c95
- Original site: https://gocardless.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm canvas, confident yellow

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1c1b18` | neutral | Primary text or dark surface |
| Stone Slate | `#545048` | neutral | Border, muted text, or supporting surface |
| Canvas Ecru | `#efece7` | neutral | Page background or card surface |
| Pebble Gray | `#d4d1cd` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Grounded Gold | `#f1f252` | brand | Action accent / signal color |
| Rich Umber | `#3c3428` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #1c1b18;
  --ref-stone-slate: #545048;
  --ref-canvas-ecru: #efece7;
  --ref-pebble-gray: #d4d1cd;
  --ref-pure-white: #ffffff;
  --ref-grounded-gold: #f1f252;
  --ref-rich-umber: #3c3428;
}
```

## Typography direction
- **Haffer**: 400, 600, 700, 14px, 16px, 18px, 20px, 24px, 28px, 36px, 1.21, 1.22, 1.33, 1.38, 1.40, 1.43; substitute `Inter`.
- **DM Mono**: 400, 18px, 24px, 1.33; substitute `IBM Plex Mono`.
- **Para**: 300, 48px, 1.21; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 24px, inputs: 4px, buttons: 32px, actions-small: 4px`

## Surface cues
- **Canvas Ecru** `#efece7`: Base page background
- **Pure White** `#ffffff`: Card backgrounds, elevated UI components like cookie banners
- **Midnight Ink** `#1c1b18`: Primary dark hero sections, prominent background for key content blocks

## Component cues
- **Primary Action Button**: The main call-to-action button for conversion and key user flows.
- **Ghost Outline Button**: Secondary action button, typically paired with a primary button or for less critical actions.
- **Navigation Link Button**: Button-like links within navigation.
- **Navigation Accent Button**: High-visibility navigation item, often a 'Sign Up' or 'Register' type of action.
- **Information Card**: Container for content, features, or product showcases.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
