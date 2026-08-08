# Upstarts Trader Backlog

> This document contains approved ideas and future enhancements that are intentionally postponed.
>
> Principle #9:
> Capture ideas immediately. Implement them deliberately.

---

# 🚧 Current Milestone

## Milestone 4 — Risk Engine

Current Focus

- Position Sizing
- Dynamic Stop Loss
- Dynamic Take Profit
- Risk / Reward
- Trade Planner

Rule

No new features unless they directly support the current milestone.

---

# 🔴 High Priority (Version 1)

## Risk Engine

Status: Planned Enhancement

### Trader Profile

Purpose

Remove hardcoded account settings from the Risk Engine.

Features

- [ ] Trader Profile
- [ ] Account Balance
- [ ] Maximum Risk %
- [ ] Preferred Risk/Reward
- [ ] Daily Max Loss
- [ ] Weekly Max Loss
- [ ] Monthly Goal

---

### Stop Loss Engine

Status: Planned Enhancement

Current

- ✅ Swing Low Stop

Future

- [ ] Swing High Stop (Shorts)
- [ ] Order Block Stop
- [ ] Fair Value Gap Stop
- [ ] ATR Stop
- [ ] Fixed Percentage Stop
- [ ] Multi-Timeframe Stop
- [ ] Configurable Stop Provider

---

### Take Profit Engine

Status: Planned

- [ ] Swing High Targets
- [ ] Liquidity Targets
- [ ] Fixed RR Targets
- [ ] Multi Target TP
- [ ] Partial Take Profit
- [ ] Trailing Take Profit

---

## Fair Value Gap

Status: Planned Enhancement

Detection

- [ ] Wick-to-Wick (Default)
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
- [ ] BOS Strength Score
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
- [ ] Minimum Risk/Reward
- [ ] Default Risk %

---

## Multi-Timeframe Analysis

Status: Planned Enhancement

- [ ] Populate Multiple Datasets
- [ ] Higher Timeframe Trend
- [ ] Lower Timeframe Entry
- [ ] Timeframe Alignment
- [ ] Cross-Timeframe Confidence

---

## Market Structure Engine

Status: Future Refactor

Current

- BOS
- CHOCH
- Liquidity
- FVG
- Order Block

Future

- [ ] Unified Market Structure Engine

---

## Market Events

Status: Future Refactor

Move away from DataFrame flags.

Future

- [ ] Bullish BOS Event
- [ ] Bearish CHOCH Event
- [ ] Liquidity Event
- [ ] FVG Event
- [ ] Order Block Event

---

# 🔵 Low Priority

## AI Advisor

Status: Version 2

Modules

- [ ] Trading Coach
- [ ] Daily Briefing
- [ ] Journal Assistant
- [ ] Trade Reviewer

Providers

- [ ] Ollama
- [ ] LM Studio
- [ ] OpenAI

---

## Desktop Dashboard

- [ ] Dockable Panels
- [ ] Custom Layouts
- [ ] Dark / Light Themes
- [ ] Multiple Watchlists

---

## Analytics

- [ ] Strategy Comparison
- [ ] Journal Analytics
- [ ] Win Rate by Setup
- [ ] Drawdown Analysis
- [ ] Equity Curve
- [ ] Performance Dashboard

---

# 🅿️ Parking Lot

Ideas that are intentionally postponed.

- [ ] Multi-Symbol Scanner
- [ ] Economic Calendar
- [ ] Broker Integration
- [ ] Portfolio Tracker
- [ ] Cloud Sync
- [ ] Mobile Companion App
- [ ] Multi-Account Support
- [ ] Options Trading
- [ ] Forex Markets
- [ ] Futures Markets

---

# 🧪 Research Ideas

Validate through backtesting.

- [ ] Immediate BOS vs Confirmed BOS
- [ ] Wick vs Body FVG
- [ ] Swing Lookback Comparison
- [ ] EMA Combination Comparison
- [ ] Risk Model Comparison
- [ ] Confidence Weight Optimization
- [ ] Best Stop Loss Provider
- [ ] Best Take Profit Provider

---

# 🔧 Technical Debt

Refactor after Version 1.

- [ ] Event Objects instead of DataFrame Flags
- [ ] Remove Remaining Magic Strings
- [ ] Analyzer Modularization
- [ ] Logging Framework
- [ ] Unit Tests
- [ ] Integration Tests

---

# 🌍 Future Vision (Version 2+)

- [ ] AI Trade Planner
- [ ] AI Journal Analysis
- [ ] Automated Backtesting
- [ ] Walk-Forward Testing
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