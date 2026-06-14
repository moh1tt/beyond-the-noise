# Thesis: AI Infrastructure Buildout — Picks & Shovels

**Status:** Active
**Conviction:** High (with valuation caveats — see Risks)
**Created:** 2026-05-11 (positions opened); formalized in repo 2026-06-14
**Last updated:** 2026-06-14

## Core Thesis

The AI compute/memory demand surge (AMD, Micron, SanDisk all running hot in 2026) is driving a capex supercycle in semiconductor fabrication and AI datacenter buildout. Rather than betting directly on the chipmakers — which have already re-rated sharply — this thesis targets the "picks and shovels" layer that benefits from the *spending*, regardless of which chip company wins: semiconductor equipment/materials suppliers (ENTG, ICHR), electrical infrastructure for fabs and datacenters (POWL), optical interconnect for datacenter networking (GLW), and baseload power for AI datacenter electricity demand (CEG).

For this to keep working: fab capex and hyperscaler datacenter spend need to keep growing through 2026–2027, and these second-derivative suppliers need to keep converting that spend into revenue/margin without giving it all back to valuation multiple compression.

## Supporting Data

- Micron (MU) fiscal Q2 2026 revenue $23.86B, 74.4% gross margin; guided fiscal Q3 to ~$33.5B revenue, ~81% gross margin, driven by HBM/DRAM/NAND pricing on AI server demand — Parameter.io / market reports, ~May 2026.
- SanDisk (SNDK) Q3 2026 revenue +96% sequentially to $5.95B; data center revenue +233% sequentially on AI infra adoption (Stargate SSD line) — Motley Fool, 2026-05-11 & 2026-05-24.
- AMD Q1 FY2026 data center revenue +57% YoY to $5.8B; management projects Data Center segment growth >60%/yr for 3–5 years, anchored by OpenAI's 6GW MI400 deal — CNBC, 2026-05-05.
- MU and SNDK stock up 154% and 493% YTD as of 2026-05-15 (AlphaSpread) — illustrates how much optimism is already priced into the direct chip names, reinforcing the case for the derivative plays in this thesis.

## Tickers

| Ticker | Role in Thesis | Status | Shares (Core Book) | Avg Cost | Current | P&L % | Rating |
|---|---|---|---|---|---|---|---|
| [ENTG](../tickers/ENTG.md) | Semiconductor materials/contamination control — direct fab-capex play, capex cycle largely behind it (operating leverage ahead) | Held | 3.000000 | $147.91 | $150.46 | +1.7% | Hold |
| [ICHR](../tickers/ICHR.md) | Fluid-delivery subsystems for WFE OEMs (Lam, Applied) — pure-play leverage to the wafer-fab-equipment upcycle | Held | 2.000000 | $70.00 | $86.87 | +24.1% | Hold (consider trim) |
| [POWL](../tickers/POWL.md) | Electrical switchgear/distribution for datacenters & utilities — direct beneficiary of datacenter electrification | Held | 3.000000 | $313.80 | $294.74 | -6.1% | Hold |
| [GLW](../tickers/GLW.md) | Optical fiber & connectivity for AI datacenter networking | Held | 2.002839 | $204.79 | $179.3815 | -12.4% | Hold |
| [CEG](../tickers/CEG.md) | Nuclear baseload power, increasingly contracted directly to AI datacenter operators | Held | 1.001570 | $295.40 | $253.76 | -14.1% | Accumulate |

*(Data as of 2026-06-12 close.)*

## Risks

- **Valuation/extrapolation risk**: POWL, ICHR (and the direct names MU/SNDK) have had explosive run-ups priced for a continued upcycle. ICHR's recent 30-day +58% run has pushed it above most analyst targets (~$60–66 vs. $86.87 current). POWL has been flagged by GuruFocus as ~287% overvalued vs. GF Value, with a forward P/E ~62.6x and ~$32.5M of insider selling in the last 3 months with no offsetting buys.
- **Single demand-driver concentration**: ENTG, ICHR, POWL, GLW, and (partially) CEG all ultimately depend on continued fab capex / hyperscaler datacenter spend — this is a correlated bet across five tickers, not five independent ones.
- **Wide analyst disagreement on ENTG**: targets range from a Goldman Sachs Sell at $95 to a Mizuho Outperform at $180 — over a 90% spread, signaling genuine uncertainty about cycle durability.
- **Margin/execution risk**: POWL's gross/operating margins compressed in Q2 FY2026 despite record backlog (supply-chain costs); ICHR remains GAAP-unprofitable.
- **CEG sentiment disconnect**: fundamentals are strong (Q1 2026 adjusted EPS $2.74, +28% YoY, beat consensus; FY26 guidance reaffirmed $11–12) but one source (TIKR) cites CEG down ~20% YTD 2026 — possibly rate-sensitivity / utility-sector rotation independent of the AI story. Unverified, flagged for monitoring.
- **Macro overlay**: the Fed is in a "higher-for-longer" stance (see [macro/dashboard.md](../macro/dashboard.md)) with the next FOMC decision 2026-06-16/17. Capex-heavy, rate-sensitive names (CEG, POWL) are more exposed to a "no cuts, longer" outcome than the materials/equipment names.

## Catalysts to Watch

- 2026-06-16/17 — FOMC decision (rate-sensitive names: CEG, POWL).
- ICHR Q2 2026 results — guided revenue $290–310M with positive GAAP and non-GAAP EPS; a beat/miss here is a read on whether the WFE upcycle is broadening or narrow.
- POWL — integration progress on the >$400M data-center infrastructure award (runs through FY2028) and whether margins stabilize.
- GLW — capacity scale-up on the NVIDIA optical-connectivity partnership (announced 2026-05-06, stock +14% on the news) and whether the two new hyperscaler agreements get quantified.
- CEG — any news on the ~1GW nuclear uprate plan (incl. Braidwood/Byron 135MW) and new PPA announcements.

## Changelog

- 2026-05-11: Thesis opened. Sold PLTR (13.486836 sh @ $135.0671) and BKNG (2.678021 sh @ $160.697) on Core Book, rotated proceeds into ENTG (3 @ $147.91), POWL (2 @ $320.21), GLW (2 @ $204.80), CEG (1 @ $295.43).
- 2026-05-14: Added POWL (+1 @ $300.99) and ICHR (2 @ $70.00). (LIN was also bought this day but tagged Unassigned — see `portfolio/core-book.md`.)
- 2026-05-20: CEG DRIP +0.001570 sh.
- 2026-06-03: GLW DRIP +0.002839 sh.
- 2026-06-14: Thesis formalized in repo with full research pass; all five tickers rated, CEG moved to Accumulate given fundamentals/price disconnect (flagged for re-check).
