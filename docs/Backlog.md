# Upstarts Trader Backlog

> Approved features and improvements intentionally postponed.
>
> Principle #9
>
> Capture ideas immediately.
> Implement them deliberately.

---

# 🚧 Current Milestone

Milestone 4 — Risk Engine

Current Focus

- Position Sizing
- Dynamic Stop Loss
- Dynamic Take Profit
- Trade Planning
- Decision Engine

Rule

No new features unless they directly support the current milestone.

---

# 🔴 High Priority (Version 1)

## Risk Engine

### Trader Profile

Status: Planned

Purpose

Remove hardcoded trader settings.

Features

- [ ] Trader Profile
- [ ] Account Balance
- [ ] Maximum Risk %
- [ ] Preferred Risk %
- [ ] Preferred Risk / Reward
- [ ] Daily Max Loss
- [ ] Weekly Max Loss
- [ ] Monthly Goal

---

### Stop Loss Engine

Status: In Progress

Current

- ✅ Swing Low Stop

Future

- [ ] Direction-aware stops (BUY / SELL)
- [ ] Validate stop is on the correct side of entry
- [ ] Previous valid swing fallback
- [ ] Order Block Stop
- [ ] Fair Value Gap Stop
- [ ] ATR Stop
- [ ] Fixed Stop
- [ ] Multi-Timeframe Stop
- [ ] Configurable Stop Providers

---

### Take Profit Engine

Status: In Progress

Current

- ✅ Swing High Target

Future

- [ ] Liquidity Targets
- [ ] Order Block Targets
- [ ] Fair Value Gap Targets
- [ ] Fixed RR Targets
- [ ] Multi Target TP
- [ ] Partial Take Profit
- [ ] Trailing Take Profit
- [ ] Configurable Take Profit Providers

---

### Trade Planner

Status: Completed ✅

Future Enhancements

- [ ] Trade Decision
- [ ] Confluence Summary
- [ ] Strategy Name
- [ ] Session Information
- [ ] Trade Notes
- [ ] Risk Warnings
- [ ] Multi-Timeframe Summary
- [ ] Screenshot Export
- [ ] PDF Export

---

## Fair Value Gap

Status: Planned Enhancement

Detection

- [ ] Wick-to-Wick
- [ ] Body-to-Body
- [ ] Hybrid Detection

Filters

- [ ] Minimum Displacement
- [ ] ATR Filter
- [ ] Volume Filter
- [ ] Trend Alignment

Lifecycle

- [ ] Mitigation
- [ ] Partial Fill
- [ ] Full Fill
- [ ] Lifespan Tracking
- [ ] Multi-Timeframe FVG

---

## Liquidity

Status: Planned Enhancement

- [ ] Equal Highs
- [ ] Equal Lows
- [ ] Session Liquidity
- [ ] Weekly Liquidity
- [ ] Monthly Liquidity
- [ ] Liquidity Strength Score

---

## Break of Structure

Status: Planned Enhancement

- [ ] Failed BOS
- [ ] BOS Strength
- [ ] Internal BOS
- [ ] External BOS

---

## CHOCH

Status: Planned Enhancement

- [ ] Trend-aware CHOCH
- [ ] Bullish CHOCH
- [ ] Bearish CHOCH
- [ ] Internal CHOCH

---

## Trade Validator

- [ ] Direction-aware validation (BUY/SELL)
- [ ] Strategy-specific validation
- [ ] Multi-timeframe validation
- [ ] Session validation
- [ ] News event validation

---

## Confluence Engine

Status: In Progress

Current

- ✅ Confluence Score
- ✅ Confluence Strength

Future

- [ ] Liquidity Sweep Confluence
- [ ] Order Block Confluence
- [ ] Premium / Discount Confluence
- [ ] Multi-Timeframe Confluence
- [ ] Strategy-specific Confluence
- [ ] Weighted Confluence Scoring

---

## Premium / Discount

Status: In Progress

Current

- ✅ Premium Detection
- ✅ Discount Detection
- ✅ Equilibrium

Future

- [ ] Multi-Timeframe Premium/Discount
- [ ] External Structure Premium/Discount
- [ ] Internal Structure Premium/Discount
- [ ] Premium/Discount Visualization

---

## Liquidity

Status: In Progress

Current

- ✅ Buy-side Liquidity Sweep
- ✅ Sell-side Liquidity Sweep

Future

- [ ] Equal High / Low Detection
- [ ] Internal Liquidity
- [ ] External Liquidity
- [ ] Multi-Candle Sweeps
- [ ] Multi-Timeframe Liquidity

---

## Setup Engine

Status: In Progress

Current

- ✅ Bullish Continuation
- ✅ Wait for Pullback
- ✅ No Valid Setup

Future

- [ ] Liquidity Grab Reversal
- [ ] Breakout Retest
- [ ] Range Expansion
- [ ] Trend Exhaustion
- [ ] Strategy-specific Setups
- [ ] Setup Confidence Scoring

---

## Scanner

Status: In Progress

Current

- ✅ Default Watchlist
- ✅ Scanner Engine

Next

- [ ] Scan Entire Watchlist
- [ ] Filter Trade Candidates
- [ ] Sort by Confidence
- [ ] Scheduler
- [ ] Notification Providers

Future

- [ ] Custom Watchlists
- [ ] Dynamic Watchlists
- [ ] Sector-based Watchlists

---

## Presentation Layer

Status: In Progress

Current

- ✅ Console View

Next

- [ ] Discord View
- [ ] Telegram View
- [ ] HTML Dashboard
- [ ] JSON Export

Future

- [ ] Rich Terminal UI
- [ ] Web Dashboard

---

## Trade Filter

Status: In Progress

Current

- ✅ Filter by BUY decision

Next

- [ ] Minimum confidence filter
- [ ] Minimum confluence filter
- [ ] Minimum risk/reward filter
- [ ] Session filter
- [ ] Strategy filter

Future

- [ ] User-configurable filters
- [ ] Saved filter presets

---

## Scan Summary

Status: In Progress

Current

- ✅ Symbols Scanned
- ✅ BUY / WAIT / SKIP Counts
- ✅ Highest Confidence
- ✅ Average Confidence

Next

- [ ] Scan Duration
- [ ] Filter Pass Rate
- [ ] Best Setup
- [ ] Average Risk/Reward
- [ ] Symbols per Second

Future

- [ ] Historical Scan Analytics
- [ ] Daily Scanner Statistics

---

## Trade Ranking

Status: In Progress

Current

- ✅ Decision confidence ranking
- ✅ Confluence weighting
- ✅ Risk/Reward weighting

Next

- [ ] Session weighting
- [ ] Strategy weighting
- [ ] Liquidity weighting
- [ ] Market regime weighting

Future

- [ ] AI-assisted ranking
- [ ] Personalized ranking profiles

---

## Fault Tolerance

Status: In Progress

Current

- ✅ Per-symbol exception handling
- ✅ Continue scanning after failures
- ✅ Failed symbol reporting

Next

- [ ] Retry failed symbols
- [ ] Timeout handling
- [ ] Rate limit handling
- [ ] Scan duration tracking

Future

- [ ] Exchange failover
- [ ] Health monitoring
- [ ] Automatic recovery

---

## Scheduler

Status: In Progress

Current

- ✅ Scheduler abstraction
- ✅ Manual scheduling mode
- ✅ Scheduler abstraction
- ✅ Configurable scan interval
- ✅ Next scan calculation

Next

- [ ] Scheduled execution
- [ ] Session-aware scheduling
- [ ] Pause / Resume
- [ ] Continuous scheduler loop
- [ ] Persistent last scan
- [ ] Session-aware scheduling

Future

- [ ] Holiday calendars
- [ ] Exchange maintenance windows
- [ ] Cron expressions
- [ ] Exchange calendars

---

# 🟡 Medium Priority

## Trading Profiles

Status: Planned

Profiles

- [ ] Scalping
- [ ] Day Trading
- [ ] Swing Trading
- [ ] Position Trading

Configuration

- [ ] Preferred Timeframes
- [ ] Preferred Sessions
- [ ] Minimum Confidence
- [ ] Minimum Risk / Reward
- [ ] Default Risk %

---

## Multi-Timeframe Analysis

- [ ] Higher Timeframe Trend
- [ ] Lower Timeframe Entry
- [ ] Timeframe Alignment
- [ ] Cross-Timeframe Confidence

---

## Market Structure Engine

Future Refactor

- [ ] Unified Market Structure Engine

---

## Market Events

Future Refactor

- [ ] Event Objects instead of DataFrame Flags

---

## Scanner & Notification Engine

Status: Planned

Scanner

- [ ] Multi-symbol scanning
- [ ] Watchlist management
- [ ] Automatic scheduled scanning
- [ ] Candle-close scanning
- [ ] Configurable scan intervals
- [ ] Scan history

Notifications

- [ ] Discord Webhooks
- [ ] Telegram Bot
- [ ] Desktop Notifications
- [ ] Email Notifications
- [ ] Notification History

Future

- [ ] Custom alert conditions
- [ ] Per-symbol alert rules
- [ ] Alert cooldowns
- [ ] Alert priorities

---

## Session Awareness

Status: Planned Enhancement

- [x] Current Session Detection
- [ ] London/New York Overlap
- [ ] Weekend Detection
- [ ] Holiday Detection
- [ ] Session Volatility Profiles
- [ ] User-configurable Sessions

---

## Decision Engine

Status: In Progress

Current

- ✅ Weighted Scoring
- ✅ Confidence Percentage

Future

- [ ] Strategy-specific Weights
- [ ] Dynamic Market Weights
- [ ] AI Weight Optimization
- [ ] Historical Performance Weighting

---

## Presentation Layer

Status: In Progress

Current

- ✅ ConsoleView
- ✅ Separated presentation from business logic
- ✅ Consistent context-based display methods

Next

- [ ] DiscordView
- [ ] TelegramView
- [ ] JSON Export
- [ ] HTML Dashboard

Future

- [ ] Rich Terminal UI
- [ ] Web Dashboard
- [ ] Theme support

---

## Configuration

Status: In Progress

Current

- ✅ Expanded Settings class
- ✅ Scanner settings
- ✅ Ranking settings
- ✅ Display settings

Next

- [ ] Migrate Trade Filter
- [ ] Migrate Trade Ranker
- [ ] Migrate Presentation Layer

Future

- [ ] User Settings
- [ ] Strategy Profiles
- [ ] Desktop Configuration
- [ ] Import / Export

---

# 🔵 Low Priority

## AI Advisor

Version 2

- [ ] Trading Coach
- [ ] Daily Brief
- [ ] Journal Assistant
- [ ] Trade Reviewer

Providers

- [ ] Ollama
- [ ] LM Studio
- [ ] OpenAI

---

## Desktop Dashboard

- [ ] Dockable Panels
- [ ] Watchlists
- [ ] Layouts
- [ ] Themes

---

## Analytics

- [ ] Strategy Comparison
- [ ] Journal Analytics
- [ ] Drawdown Analysis
- [ ] Equity Curve
- [ ] Performance Dashboard

---

# 🅿️ Parking Lot

- [ ] Multi Symbol Scanner
- [ ] Economic Calendar
- [ ] Broker Integration
- [ ] Portfolio Tracker
- [ ] Cloud Sync
- [ ] Mobile Companion App
- [ ] Multi Account Support
- [ ] Options Trading
- [ ] Forex
- [ ] Futures

---

# 🧪 Research

- [ ] Immediate BOS vs Confirmed BOS
- [ ] Wick vs Body FVG
- [ ] Swing Lookback Comparison
- [ ] EMA Comparison
- [ ] Risk Model Comparison
- [ ] Confidence Weight Optimization
- [ ] Best Stop Loss Provider
- [ ] Best Take Profit Provider

---

# 🔧 Technical Debt

- [ ] Event Objects instead of DataFrame Flags
- [ ] Remove Remaining Magic Strings
- [ ] Analyzer Modularization
- [ ] Logging Framework
- [ ] Unit Tests
- [ ] Integration Tests

---

# 🌍 Future Vision

- [ ] AI Trade Planner
- [ ] AI Journal Analysis
- [ ] Automated Backtesting
- [ ] Walk Forward Testing
- [ ] Monte Carlo Analysis
- [ ] Strategy Marketplace

---

# 📜 Product Principles

Before implementing any backlog item ask:

1. Does it improve trading decisions?
2. Can it be configured?
3. Can it be backtested?
4. Can it be explained?
5. Does it fit the current milestone?