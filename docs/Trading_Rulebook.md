# Upstarts Trader Trading Rulebook v1.0

---

# Purpose

This document defines the trading methodology used by Upstarts Trader.

It is the single source of truth for every trading decision implemented in the system.

If the software behavior and this document ever disagree, this document takes precedence.

---

# Trading Philosophy

The objective of Upstarts Trader is NOT to predict the market.

The objective is to identify high-probability trading opportunities through confluence.

No single indicator, pattern, or concept is sufficient to justify a trade.

Every trade should be supported by multiple independent pieces of evidence.

The system favors quality over quantity.

When in doubt, the bot should WAIT.

---

# Core Trading Principles

## Principle 1

Trade probabilities, not certainties.

There are no guaranteed winning trades.

The objective is positive expectancy over hundreds of trades.

---

## Principle 2

Market structure has higher importance than lagging indicators.

Structure determines market direction.

Indicators confirm execution.

---

## Principle 3

Confluence is stronger than isolated signals.

The more independent concepts pointing in one direction, the higher the confidence.

---

## Principle 4

Risk management overrides every trading opportunity.

A good setup with poor risk management should never become a trade.

---

## Principle 5

The bot should explain every decision.

Every BUY, SELL, WAIT or SKIP should include reasons.

The system should never behave like a black box.

---

# Trading Decision Flow

The bot should think in the following order:

Market Data

↓

Market Structure

↓

Confluence

↓

Market Bias

↓

Trade Confirmation

↓

Trade Decision

↓

Trade Planning

↓

Validation

↓

Alert

---

# Market Structure

Market structure represents objective observations.

It does not decide trades.

It only describes price.

---

## Trend

Possible Values

Bullish

Bearish

Neutral (Future)

---

## Swing High

A candle whose high is higher than neighboring highs based on the configured lookback period.

---

## Swing Low

A candle whose low is lower than neighboring lows based on the configured lookback period.

---

## Break of Structure (BOS)

Definition

A confirmed continuation of the existing trend through a significant swing level.

Possible Values

Bullish

Bearish

None

Purpose

Trend continuation.

---

## Change of Character (CHOCH)

Definition

The first structural indication that market control may be changing.

Possible Values

Bullish

Bearish

None

Purpose

Potential trend reversal.

---

# Liquidity

Markets seek liquidity before moving efficiently.

---

## Buy Side Liquidity

Liquidity resting above previous highs.

---

## Sell Side Liquidity

Liquidity resting below previous lows.

---

## Liquidity Sweep

A temporary move beyond liquidity followed by rejection.

Possible Values

Buy Side Sweep

Sell Side Sweep

None

Purpose

Indicates possible institutional accumulation or distribution.

---

# Fair Value Gap (FVG)

Definition

An imbalance created by aggressive price movement.

Possible Values

Bullish

Bearish

None

Purpose

Potential area for price retracement before continuation.

---

# Premium / Discount

Premium

Price trading above equilibrium.

Generally preferred area for SELL setups.

---

Discount

Price trading below equilibrium.

Generally preferred area for BUY setups.

---

Equilibrium

Fair value.

Future implementation.

---

# Confluence

Purpose

Measure how much evidence supports each market direction.

Confluence does NOT execute trades.

Confluence does NOT determine entries.

Confluence only evaluates evidence.

---

## Bullish Evidence

Examples

Bullish Trend

Bullish BOS

Bullish CHOCH

Bullish FVG

Discount Zone

Sell Side Liquidity Sweep

Order Block (Future)

---

## Bearish Evidence

Examples

Bearish Trend

Bearish BOS

Bearish CHOCH

Bearish FVG

Premium Zone

Buy Side Liquidity Sweep

Order Block (Future)

---

# Market Bias

Purpose

Determine which side currently has the strongest market thesis.

Possible Values

BUY

SELL

NEUTRAL

Bias is determined from Confluence.

Bias does NOT use indicators directly.

---

# Trade Confirmation

Purpose

Confirm whether the current market is ready for execution.

Confirmation indicators should never determine market direction.

---

## EMA

Purpose

Trend alignment.

Supports execution only.

---

## MACD

Purpose

Momentum confirmation.

Supports execution only.

---

## RSI

Purpose

Market health.

Supports execution only.

---

## Future Confirmation

Volume

Candlestick Confirmation

ATR

VWAP

---

# Trade Decision

The decision engine combines

Market Bias

Trade Confirmation

Risk

Trading Session

Possible Outputs

BUY

SELL

WAIT

SKIP

---

# Trade Planning

The planner produces

Entry

Stop Loss

Take Profit

Risk Reward Ratio

Position Size

The planner never determines direction.

---

# Trade Validation

Final safety checks before alert generation.

Examples

Risk acceptable

Minimum RR achieved

Stop Loss valid

Take Profit valid

Trade still active

---

# Trade Quality

Every opportunity should eventually receive a quality grade.

Grades

A+

A

B

C

Invalid

Trade quality should be determined by:

Confluence

Risk

Confirmation

Session

Future statistical performance

---

# Current Features

✅ Market Structure

✅ BOS

✅ CHOCH

✅ Liquidity Sweep

✅ Fair Value Gap

✅ Premium / Discount

✅ EMA

✅ RSI

✅ MACD

---

# Planned Features

Order Blocks

Breaker Blocks

Equal Highs

Equal Lows

Volume Profile

SMT Divergence

Market Sessions

Economic Calendar

Multi-Timeframe Analysis

AI Commentary

Backtesting

---

# Engineering Rules

Trading concepts should never be duplicated across multiple engines.

Each concept should have one owner.

Example

Market Structure
→ Analysis Engine

Confluence
→ Confluence Engine

Bias
→ Bias Engine

Confirmation
→ Signal Engine

Execution
→ Decision Engine

Planning
→ Trade Planner

---

# Guiding Principle

The bot should never trade because of a single indicator.

The bot should only trade when multiple independent market concepts align into a coherent trading thesis.

When uncertainty is high,

the correct decision is to WAIT.