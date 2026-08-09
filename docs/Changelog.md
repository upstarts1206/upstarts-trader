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

# v0.4.0 — Risk Engine (In Progress)

## Added

- Risk Engine
- Position Sizing Engine
- Dynamic Stop Loss Engine
- Dynamic Take Profit Engine
- Trade Planner

## Improved

- Risk / Reward calculation
- Market structure-based stop loss
- Market structure-based take profit
- Separation of Risk Engine responsibilities

## Fixed

- Stop-loss validation now only considers swing lows below the current price for long trades.

## Planned

- Decision Engine
- Trader Profile
- Direction-aware stop loss
- Multiple stop providers
- Multiple take profit providers