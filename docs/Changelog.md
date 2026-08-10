# Changelog

All notable changes to Upstarts Trader are documented in this file.

The format is inspired by "Keep a Changelog", but focused on product evolution rather than Git commits.

---

# v0.1.0 — Foundation & Core Engine

## Added

- Initial project architecture
- Market data module
- Pipeline architecture
- EMA indicator
- RSI indicator
- MACD indicator
- Signal Engine
- Strategy architecture
- Market Summary service

## Improved

- Cleaner project structure
- Modular indicator system
- Dynamic indicator pipeline

---

# v0.2.0 — Market Structure

## Added

- Swing High detection
- Swing Low detection
- Break of Structure (BOS)
- Confirmed BOS
- Change of Character (CHOCH)
- Analyzer
- MarketContext model

## Improved

- Centralized analysis flow
- Analyzer orchestration
- Cleaner application entry point

---

# v0.3.0 — Smart Money Concepts

## Added

- Liquidity Sweep detection
- Fair Value Gap (FVG) detection
- Order Block detection

## Improved

- Smart Money analysis pipeline
- Market Structure architecture
- Version 0.1 code cleanup
- Constants
- Configuration organization

---

# v0.4.0 — Risk Engine & Trade Planning (In Progress)

## Added

- Risk Engine
- Position Sizing Engine
- Dynamic Stop Loss Engine
- Dynamic Take Profit Engine
- Trade Planner
- Decision Engine
- Confidence Engine
- Watchlist Architecture
- Scanner Engine
- TradeFilter module
- Trade candidate filtering pipeline
- ScanSummary module
- Scan statistics before filtering
- Console summary display
- TradeRanker module
- Trade candidate prioritization
- Top Trade Today summary
- Fault-tolerant scanner
- Per-symbol exception handling
- Error reporting during scans
- Scheduler module
- Manual scheduling abstraction
- Configurable scan interval
- Dynamic next scan calculation
- AutomationRunner abstraction


## Improved

- Risk / Reward calculation
- Market structure-based stop loss
- Market structure-based take profit
- Weighted decision confidence
- Separation of Risk, Decision, and Planning responsibilities
- Trade quality evaluation using confluence scoring
- Analyzer can now process multiple symbols through a unified scanner
- Scanner output now supports filtering before presentation.
- Scanner now reports overall market conditions even when no trades qualify.
- Trade candidates are now ranked before presentation.
- Expanded Settings class to support automation modules.
- Scanner now completes scans even when individual symbols fail.
- Scan execution now routes through the scheduler.
- Scheduler now derives timing from application settings.
- Application execution is now separated from scheduling.


## Fixed

- Stop-loss validation now only considers swing lows below the current price for long trades.

## Planned

- Trader Profile
- Direction-aware stop loss
- Multiple stop providers
- Multiple take profit providers

## Refactored

- Moved terminal output from app.py into ConsoleView.
- Separated presentation from business logic.
- Began replacing hardcoded application values with centralized configuration.