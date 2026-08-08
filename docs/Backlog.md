# Upstarts Trader Backlog

This document contains ideas, enhancements, and future improvements that are intentionally postponed.

The purpose of this backlog is to capture ideas without disrupting the current milestone.

---

# High Priority

These items are expected to be part of Version 1 after the current milestone.

## Fair Value Gap (FVG)

Status: Planned Enhancement

### Detection Methods

- [ ] Wick-to-Wick (Industry Standard)
- [ ] Body-to-Body
- [ ] Hybrid Detection

### Quality Filters

- [ ] Minimum displacement filter
- [ ] ATR filter
- [ ] Volume confirmation
- [ ] Trend alignment

### Lifecycle

- [ ] Track mitigation
- [ ] Track partial fills
- [ ] Track full fills
- [ ] Track FVG lifespan
- [ ] Multi-timeframe FVG detection

---

## Liquidity

Status: Planned Enhancement

- [ ] Equal High detection
- [ ] Equal Low detection
- [ ] Session High liquidity
- [ ] Session Low liquidity
- [ ] Weekly High/Low liquidity
- [ ] Monthly High/Low liquidity
- [ ] Liquidity strength scoring

---

## Break of Structure (BOS)

Status: Planned Enhancement

- [ ] Failed BOS detection
- [ ] BOS strength scoring
- [ ] Internal BOS
- [ ] External BOS

---

## Change of Character (CHOCH)

Status: Planned Enhancement

- [ ] Trend-aware CHOCH
- [ ] Bullish CHOCH
- [ ] Bearish CHOCH
- [ ] Internal CHOCH

---

# Medium Priority

## Trading Profiles

Status: Planned Feature

Purpose:
Configure the platform based on trading style rather than strategy.

Profiles

- [ ] Scalping
- [ ] Intraday
- [ ] Swing Trading
- [ ] Position Trading

Possible Profile Settings

- [ ] Preferred timeframes
- [ ] Default risk percentage
- [ ] Minimum confidence
- [ ] Minimum Risk/Reward
- [ ] Preferred market sessions

---

## Market Structure Engine

Status: Future Refactor

Combine market structure modules into one engine.

Current

- BOS
- CHOCH
- Liquidity
- FVG

Future

- Unified Market Structure Engine

---

## Market Events

Status: Future Refactor

Move from DataFrame columns to event objects.

Current

bos = True

Future

- Bullish BOS Event
- Bearish CHOCH Event
- Liquidity Event
- FVG Event

---

## AI Advisor

Status: Planned Feature

AI should enhance—not replace—the trading engine.

Modules

- [ ] Trading Coach
- [ ] Trade Reviewer
- [ ] Journal Assistant
- [ ] Daily Planner

Support

- [ ] Local LLM
- [ ] OpenAI
- [ ] Ollama
- [ ] LM Studio

---

# Low Priority

## Desktop Enhancements

- [ ] Custom dashboard layouts
- [ ] Dark/Light themes
- [ ] Multiple watchlists

---

## Analytics

- [ ] Strategy comparison
- [ ] Monthly performance reports
- [ ] Win-rate by setup
- [ ] Risk analytics
- [ ] Trading journal insights

---

# Research Ideas

Ideas that should be validated through backtesting before implementation.

- [ ] Compare Immediate BOS vs Confirmed BOS
- [ ] Compare Wick vs Body FVG
- [ ] Compare different Swing Lookbacks
- [ ] Compare EMA combinations
- [ ] Compare Risk models
- [ ] Compare confidence weighting systems

---

# Notes

Remember Principle #9

Capture ideas immediately.
Implement them deliberately.

---

# Parking Lot

- [ ] Multi-symbol scanner
- [ ] Economic calendar integration
- [ ] Broker integration
- [ ] Mobile companion app
- [ ] Portfolio tracker
- [ ] Multi-account support
- [ ] Options trading support