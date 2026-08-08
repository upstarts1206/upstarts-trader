# Upstarts Trader Backlog

> This document contains approved ideas and future enhancements that are intentionally postponed.
>
> The goal is to capture ideas without interrupting the current milestone.

---

# Current Milestone

Milestone 4 - Risk Engine

Current Focus

- Position Sizing
- Stop Loss Engine
- Take Profit Engine
- Risk / Reward
- Trade Planner

⚠️ No new feature development unless it directly supports this milestone.

---

# High Priority (Version 1)

## Risk Engine

Status: Planned

### Trader Profile

Purpose

Remove hardcoded account information from the Risk Engine.

Future Features

- [ ] Trader Profile
- [ ] Account Balance
- [ ] Maximum Risk %
- [ ] Preferred Risk/Reward
- [ ] Daily Max Loss
- [ ] Weekly Max Loss
- [ ] Monthly Goal

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
- [ ] FVG Lifespan
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

# Medium Priority

## Trading Profiles

Status: Planned

Profiles

- [ ] Scalping
- [ ] Day Trading
- [ ] Swing Trading
- [ ] Position Trading

Configuration

- [ ] Preferred Timeframes
- [ ] Minimum Confidence
- [ ] Preferred Sessions
- [ ] Default Risk
- [ ] Minimum RR

---

## Multi-Timeframe Analysis

Status: Planned Enhancement

- [ ] Populate multiple datasets
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

- Unified Market Structure Engine

---

## Market Events

Status: Future Refactor

Move from DataFrame columns to Event objects.

Examples

- Bullish BOS Event
- Bearish CHOCH Event
- Liquidity Event
- FVG Event
- Order Block Event

---

# Low Priority

## AI Advisor

Status: Version 2

Modules

- [ ] Trading Coach
- [ ] Trade Reviewer
- [ ] Journal Assistant
- [ ] Daily Planner

Providers

- [ ] Ollama
- [ ] OpenAI
- [ ] LM Studio

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

# Parking Lot

Ideas that are intentionally not prioritized.

- [ ] Multi-Symbol Scanner
- [ ] Economic Calendar
- [ ] Portfolio Tracker
- [ ] Broker Integration
- [ ] Mobile Companion App
- [ ] Cloud Sync
- [ ] Multi-Account Support
- [ ] Options Trading
- [ ] Forex Support
- [ ] Futures Support

---

# Research Ideas

These should be validated through backtesting.

- [ ] Immediate BOS vs Confirmed BOS
- [ ] Wick FVG vs Body FVG
- [ ] Swing Lookback Comparison
- [ ] EMA Combination Comparison
- [ ] Risk Model Comparison
- [ ] Confidence Weight Optimization

---

# Technical Debt

Items intentionally postponed until after Version 1.

- [ ] Replace DataFrame event columns with Event objects
- [ ] Remove remaining magic strings
- [ ] Improve Analyzer modularity
- [ ] Improve logging
- [ ] Unit Test Coverage
- [ ] Integration Tests

---

# Future Vision (Version 2+)

- [ ] AI-assisted Trade Planning
- [ ] AI Journal Review
- [ ] Automated Backtesting
- [ ] Walk-forward Optimization
- [ ] Monte Carlo Analysis
- [ ] Strategy Marketplace

---

# Principles

Before implementing any backlog item, ask:

1. Does it improve trading decisions?
2. Can it be configured?
3. Can it be backtested?
4. Can it be explained?
5. Does it fit the current milestone?

If not, leave it in the backlog.