# Equals - Colorful Refero Design MD

- Source: https://styles.refero.design/style/dae7cbf2-0485-433b-8f63-eea8716ad14d
- Original site: https://equals.com
- Theme: `light`
- Color rank: **43**
- Colorfulness score: `29.4`
- Recommended fit: **Color-coded data dashboard**

## North star
Broadsheet meets spreadsheet - editorial serif authority on warm cream, punctuated by floating pastel data cells.

## Why this fits html-news-creator
Use for source health, cluster scores, confidence labels, and stateful admin screens that need clearer semantic color.

## Apply to
- Source ledger states
- Cluster/category badges
- Run status and alert panels

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Analyst Yellow | `#FFCC00` | brand | Announcement bar background only - saturated yellow on near-black text creates maximum urgency at minimal surface area,. |
| Orchid CTA | `#B074CE` | brand | Primary CTA buttons - warm violet against cream background reads as inviting rather than urgent, distinguishing CTAs fr. |
| Brand Green | `#20A277` | accent | Finance category accent swatch - one of three role-coded indicator blocks (RevOps red, Founders navy, Finance green) fl. |
| Glacier | `#2DCBDC` | accent | Background decorative color block in hero, part of the floating pastel spreadsheet-cell visual language |
| Midnight Ink | `#000000` | neutral | All headings, body text, borders, nav links, icons - full black with zero softening; the high contrast against cream is. |
| Warm Cream | `#FAF9F5` | neutral | Page background, section backgrounds - the slight warm yellow tint separates this from clinical white and reinforces th. |
| Cloud White | `#FFFFFF` | neutral | Button text on orchid CTAs, nav hover states, input field backgrounds |
| Slate Body | `#646462` | neutral | Body copy, nav secondary text, descriptive subtexts under headings |

```css
:root {
  --colorful-analyst-yellow: #FFCC00;
  --colorful-orchid-cta: #B074CE;
  --colorful-brand-green: #20A277;
  --colorful-glacier: #2DCBDC;
  --colorful-midnight-ink: #000000;
  --colorful-warm-cream: #FAF9F5;
  --colorful-cloud-white: #FFFFFF;
}
```

## Typography direction
- Primary: **Serrif Condensed**; substitute `Freight Display Condensed, or Playfair Display with condensed tracking`.
- Secondary/code: **Unica77**; substitute `Inter, Aktiv Grotesk`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
