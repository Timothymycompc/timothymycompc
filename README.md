<p align="center"><img src="assets/banner.svg" alt="Timothy — portfolio" width="100%"></p>

<p align="center">

![Pull Shark](https://img.shields.io/badge/GitHub_achievement-Pull_Shark-dfc58a?style=flat-square&labelColor=0a0f19&logo=github&logoColor=dfc58a)
![YOLO](https://img.shields.io/badge/GitHub_achievement-YOLO-cfab66?style=flat-square&labelColor=0a0f19&logo=github&logoColor=cfab66)
![Merged PRs](https://img.shields.io/badge/merged_PRs-5-10b981?style=flat-square&labelColor=0a0f19)
![Bug reports](https://img.shields.io/badge/issues_filed-37-f59e0b?style=flat-square&labelColor=0a0f19)
![Fixes merged](https://img.shields.io/badge/upstream_fixes_from_my_reports-6_projects-10b981?style=flat-square&labelColor=0a0f19)

[![Solana Pulse on Glama](https://glama.ai/mcp/connectors/io.github.Timothymycompc/solana-pulse-gateway/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.Timothymycompc/solana-pulse-gateway)
[![mcptry](https://mcptry.com/badge/io.github.Timothymycompc/solana-pulse-gateway)](https://mcptry.com/servers/io.github.Timothymycompc/solana-pulse-gateway)

</p>

I build **safety tools for AI agents and people who move money on Solana**, and I test them honestly. Since August 2026,
in my off-work hours and mostly from a phone, I've shipped a production API on Google Cloud, five Telegram bots, an
ecosystem-wide bug investigation that got fixes merged in other teams' code, and a public, fully reproducible trading
research project.

## Featured work
| Project | What it is | Highlights |
|---|---|---|
| **[Solana Pulse](https://github.com/Timothymycompc/solana-pulse-ai-agent-gateway)** | Safety gateway for AI agents: "is this transaction what I asked for? is this token a known trap?" Plain HTTP + MCP, paid per call with x402 (USDC) | Live on Cloud Run · public benchmark 9/9 attack cases, 0 false alarms · 200/200 real transactions checked with exact fees · official MCP registry + 4 curated lists (all merged) |
| **Version 1 transaction investigation** | Found that ~35–44% of Solana swaps had moved to a transaction format many apps couldn't read | Measured it, fixed my own API the same night, filed 32 reports; **fixes merged in 6 projects** (incl. elizaOS, rotki, Agent402), plus 3 fix PRs of my own |
| **[Base Pulse](https://github.com/Timothymycompc/base-pulse)** | The same safety layer for agents paying on Base (EVM): recipient checks, approvals, sanctions list, x402 checks | Live since Oct 14 |
| **[CashOut Check](https://github.com/Timothymycompc/cashout-check)** | Paste an online casino, play-to-earn app or deposit wallet, get a plain scam-risk answer with sources | Built from real scam investigations; tests use recorded real cases |
| **Telegram bots** | Public Pulse checker, a firewood-buyer finder (free public data), grant/bounty scanner, freelance job assistant | 2 live, 3 built |
| **[Trading Review](https://github.com/Timothymycompc/trading-review)** | Honest backtests of memecoin bots, stock rules and forex systems — all code and raw data public | Locked test years, hidden data, tests committed before they ran; reports what *failed* |
| **[Dev Log](https://github.com/Timothymycompc/dev-log)** | The full story: what I built, what broke, how I fixed it, what I learned | Timeline, lessons, security practices |

## Time invested
**≈ 250 hours from Aug 30 to Nov 9, 2026**, about six full work weeks, all in off-work hours. Since Oct 10 I've worked on
this **every day (31 of 31), about 7 hours a day.**

| Project | ≈ Hours |
|---|---|
| Solana Pulse | ~165 |
| Trade Desk (memecoins) | ~40 |
| V1 Ready + bug reports | ~19 |
| Phone setup + AI tooling | ~17 |
| CashOut Check | ~10 |
| Base Pulse | ~9 |
| Freelance tools (Gig Bidder, gigs) | ~6 |
| Night Desk (stocks + forex) | ~5 |
| Firewood Buyers | ~4 |
| Dev log + portfolio | ~4 |
| Rug Check, Money Scan, Clip Drop | ~2 |
| **Total** | **≈ 250** (rows add to ~281 because some sessions overlap) |

<sub>Estimated from git commit sessions and AI-session history ([method + script](https://github.com/Timothymycompc/dev-log#time-spent-estimated)). Per-project rows overlap slightly where sessions ran in parallel.</sub>

## Strengths
- **I ship complete systems.** API, database, payments, scheduled jobs, alerts, deploys with one-command rollback — on
  Google Cloud Run, Cloud SQL, Scheduler, Secret Manager and Cloud Build.
- **I measure instead of claiming.** Recorded real-world test cases, public benchmarks, track records that include misses,
  and backtests built to catch my own luck.
- **I find real problems in real data.** The version 1 transaction bug came from reading mainnet blocks, not from an issue
  someone else filed.
- **Security-minded with money.** Secrets only in Secret Manager, hard spending limits and kill switches on wallets,
  check-before-sign on every transaction, no IP addresses stored. ([how](https://github.com/Timothymycompc/dev-log/blob/master/security.md))
- **I get a lot out of AI tools, and I check their work.** Claude Code and Gemini as pair-programmer and reviewer, with
  tests and numbers as the referee. ([what I learned](https://github.com/Timothymycompc/dev-log/blob/master/apis-cloud-ai.md))
- **Resourceful.** Most of this was built on a phone, with free data sources wherever possible.

## Still working on
- **Writing code without AI help.** I direct and review AI-written code well; my hand-coding fundamentals are what I'm
  building up next.
- **Getting real users.** Pulse has handled 180k+ calls, but those were directories, monitors and tests, not customers.
  Distribution is the skill I'm learning now.
- **Finishing before starting.** A few bots are built but not yet deployed, so I'm working to one project at a time.

## Tools I use
`TypeScript` `Node.js / Express` `Python` `PostgreSQL` `Google Cloud Run · Cloud SQL · Scheduler · Secret Manager · Cloud Build · Storage`
`Solana (web3.js, kit, Jupiter, Helius)` `Base / EVM` `MCP` `x402 payments` `Telegram Bot API` `GitHub Actions (OIDC publishing)`
`Claude Code` `Gemini / Antigravity`

<sub>Every number on this page comes from real data and the linked repos. Nothing here is financial advice.</sub>
