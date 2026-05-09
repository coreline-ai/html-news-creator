# Obsidian - Refero Design MD

- Source: https://styles.refero.design/style/e793a53c-537e-46b0-881d-b15b63b9ff26
- Original site: https://obsidian.md
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crystalline Knowledge Vault. A sharp, faceted digital space built for clarity and focus, with glowing violet veins of interaction.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White | `#ffffff` | neutral | Page background or card surface |
| Bright Gray | `#eeeeee` | neutral | Page background or card surface |
| Medium Gray | `#bcbcbc` | neutral | Border, muted text, or supporting surface |
| Muted Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Graphite | `#3f3f3f` | neutral | Primary text or dark surface |
| Abyss | `#171717` | neutral | Primary text or dark surface |
| Amethyst | `#7c3aed` | brand | Action accent / signal color |
| Lavender | `#a78bfa` | accent | Action accent / signal color |
| Tag Background | `#8a5cf5` | accent | Action accent / signal color |
| Success Green | `#4ade80` | semantic | Action accent / signal color |

```css
:root {
  --ref-white: #ffffff;
  --ref-bright-gray: #eeeeee;
  --ref-medium-gray: #bcbcbc;
  --ref-muted-gray: #a3a3a3;
  --ref-graphite: #3f3f3f;
  --ref-abyss: #171717;
  --ref-amethyst: #7c3aed;
  --ref-lavender: #a78bfa;
}
```

## Typography direction
- **ui-sans-serif, system-ui**: 400, 500, 600, 700, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 28px, 36px, 60px, 1.25-1.5; substitute `"SF Pro Display", "Roboto", "Segoe UI", sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1120px`
- Radius: `tags: 9999px, cards: 12px, inputs: 8px, buttons: 8px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Tag Badge Collection**: Reference component style.
- **Feature List Cards**: Reference component style.
- **Primary CTA Button**: The main call-to-action button.
- **Secondary Ghost Button**: A less prominent action, often for secondary choices like 'More platforms'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
