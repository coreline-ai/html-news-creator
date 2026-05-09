# Coinbase - Refero Design MD

- Source: https://styles.refero.design/style/df5e2be4-c2bd-42bb-bbc7-409bae6355c3
- Original site: https://coinbase.com
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Trust, Blueprinted. A system built on the clarity of an architectural plan, energized by a single, electric blue neuron.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Coinbase Blue | `#0052ff` | brand | Action accent / signal color |
| Interactive Blue | `#578bfa` | accent | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Midnight | `#0a0b0d` | neutral | Primary text or dark surface |
| Frost | `#f7f8f9` | neutral | Page background or card surface |
| Cloud | `#eef0f3` | neutral | Page background or card surface |
| Pewter | `#dedfe2` | neutral | Page background or card surface |
| Charcoal | `#141519` | neutral | Primary text or dark surface |
| Positive Green | `#27ad75` | semantic | Action accent / signal color |
| Negative Red | `#f0616d` | semantic | Action accent / signal color |

```css
:root {
  --ref-coinbase-blue: #0052ff;
  --ref-interactive-blue: #578bfa;
  --ref-pure-white: #ffffff;
  --ref-midnight: #0a0b0d;
  --ref-frost: #f7f8f9;
  --ref-cloud: #eef0f3;
  --ref-pewter: #dedfe2;
  --ref-charcoal: #141519;
}
```

## Typography direction
- **CoinbaseDisplay**: 400, 44px, 52px, 64px, 80px, 1.0-1.09; substitute `Manrope`.
- **CoinbaseSans**: 400, 600, 13px, 16px, 18px, 20px, 28px, 36px, 64px, 1.11-1.50; substitute `Inter`.
- **CoinbaseText**: 400, 700, 13px, 16px, 18px, 1.50-1.56; substitute `Inter`.

## Spacing / shape
- Card Padding: `24px`
- Page Max Width: `1200px`
- Radius: `tags: 100000px, cards: 24px, inputs: 8px, buttons: 56px`

## Component cues
- **Primary & Secondary Button Group**: Reference component style.
- **Crypto Price List Card**: Reference component style.
- **Earn APY Feature Banner**: Reference component style.
- **Primary CTA Button**: The main call-to-action on any page.
- **Secondary Pill Button**: Secondary action, often on a dark background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
