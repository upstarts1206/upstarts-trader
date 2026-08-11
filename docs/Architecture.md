# Upstarts Trader Architecture v1.0

---

# Vision

Build a professional trading assistant that thinks like a discretionary trader.

The system should separate:

- Market Analysis
- Market Interpretation
- Trade Confirmation
- Trade Execution

Each engine owns exactly one responsibility.

No engine should duplicate another engine's responsibility.

---

# Trading Pipeline

Market Data
    ↓
Pipeline
    ↓
Summary
    ↓
Market State
    ↓
Confluence
    ↓
Bias
    ↓
Signal
    ↓
Decision
    ↓
Trade Planner
    ↓
Validation

---

# Engine Responsibilities

## Pipeline

### Responsibility

Download market data and calculate all indicators.

### Input

- Symbol

### Output

- Candlestick DataFrame

### Must NEVER

- Decide trades
- Score markets

---

## Summary

### Responsibility

Extract the latest market snapshot.

### Input

- Latest candle

### Output

Example

- EMA20
- EMA50
- RSI
- MACD
- BOS
- CHOCH
- FVG
- Liquidity
- Premium / Discount

### Must NEVER

- Recommend trades

---

## Market State

### Responsibility

Describe the current market.

### Input

Summary

### Output

Example

Trend
Momentum
Strength

### Must NEVER

- Decide BUY or SELL
- Score anything

---

## Confluence

### Responsibility

Collect all market evidence.

Confluence answers:

"How much evidence supports BUY?"

and

"How much evidence supports SELL?"

### Input

Market State

Market Structure

Liquidity

FVG

Premium / Discount

Order Blocks (Future)

### Output

Example

BUY Score

SELL Score

BUY Reasons

SELL Reasons

### Must NEVER

- Decide direction
- Check EMA
- Check RSI
- Check MACD
- Consider Risk
- Consider Session

---

## Bias

### Responsibility

Interpret Confluence.

Bias answers:

"Which side currently has the advantage?"

### Input

Confluence

### Output

Direction

BUY

SELL

NEUTRAL

Confidence

Winning Reasons

### Must NEVER

- Analyze BOS
- Analyze CHOCH
- Analyze FVG
- Analyze Liquidity

---

## Signal

### Responsibility

Determine whether the current market is ready for execution.

Signal answers:

"Is this a valid setup?"

### Input

Bias

EMA

MACD

RSI

Volume (Future)

Candlestick Confirmation (Future)

### Output

Valid

Confidence

Reasons

### Must NEVER

- Decide BUY or SELL
- Analyze BOS
- Analyze Liquidity
- Analyze FVG

---

## Decision

### Responsibility

Determine whether a trade should be executed.

### Input

Bias

Signal

Risk

Session

### Output

BUY

SELL

WAIT

SKIP

Decision Score

Reasons

### Must NEVER

- Analyze market structure
- Analyze indicators

---

## Trade Planner

### Responsibility

Generate the complete trading plan.

### Input

Decision

Risk

Bias

### Output

Entry

Stop Loss

Take Profit

Risk Reward

Position Size

### Must NEVER

- Decide trade direction

---

## Validation

### Responsibility

Final safety checks.

### Input

Trade Plan

### Output

Valid

Errors

Warnings

### Must NEVER

- Recommend trades

---

# Design Principles

## 1.

Each engine owns one responsibility.

---

## 2.

Every engine consumes outputs from previous engines.

No engine should repeat work already completed.

---

## 3.

Market Analysis comes before Trade Confirmation.

---

## 4.

Trade Direction is determined before Trade Execution.

---

## 5.

Execution indicators never determine market direction.

Indicators such as:

- EMA
- MACD
- RSI

confirm the market thesis.

They do not create it.

---

## 6.

Every engine should be replaceable without rewriting the rest of the system.

---

## 7.

Prefer evolution over rewrites.

New interfaces should coexist with old interfaces until migration is complete.

---

# Future Modules

Order Blocks

Breaker Blocks

Volume Profile

SMT Divergence

Economic Calendar

Multi-Timeframe Analysis

AI Commentary

Backtesting

Desktop Application

Telegram Bot

---

# Current Goal

Complete the trading engine before adding new features.

The objective is correctness first.

Optimization comes later.