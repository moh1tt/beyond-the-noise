# Beyond the Noise

A personal, markdown-based investment ops repo. Run Claude Code from this directory and it acts as a portfolio analyst: it knows current holdings (across two Robinhood accounts), live prices, the active investment theses behind each position, a watchlist of potential buys, and the current macro backdrop — and keeps all of it in sync as the world (and the portfolio) changes.

## Layout

- `CLAUDE.md` — the operating manual. Start here to understand how Claude should behave in this repo.
- `portfolio/` — current holdings, P&L, and the transaction log for both accounts:
  - **Core Book** (••••8652) — existing long-term holdings, ~$4,000+, recommend-only.
  - **Tactical Sleeve** (••••3551) — fresh $100 account, semi-automated trading with confirmation.
- `theses/` — one file per investment thesis: the conviction, the data behind it, every ticker tied to it, and a rating per ticker.
- `tickers/` — one file per tracked ticker with company snapshot, fundamentals, news log, and rating history.
- `watchlist.md` — names being considered that aren't in a thesis yet or aren't bought yet.
- `macro/dashboard.md` — Fed policy, inflation, rates, and the current market regime.
- `journal/` — dated session notes and briefings.

## Workflow

1. Tell Claude what you're thinking ("I'm bullish on X because Y") — it builds out a thesis doc with research.
2. Tell Claude what you bought/sold and at what price — it updates the portfolio and transaction log.
3. Ask for a portfolio check anytime — Claude refreshes live prices, recomputes P&L, and flags anything that needs attention.
4. For the $100 tactical sleeve, Claude can draft and (with your explicit go-ahead each time) place trades directly.

Goal: disciplined, thesis-driven, data-backed investing — grow the account and beat the market over the long run.
