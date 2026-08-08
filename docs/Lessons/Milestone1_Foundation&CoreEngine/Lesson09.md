# Lesson 9 - Signal Engine

## Objective

Convert technical indicators into a trading signal.

---

## Responsibility

The Signal service interprets market information.

It does not calculate indicators or download market data.

---

## Inputs

Market Summary

---

## Outputs

- Signal
- Confidence
- Reasons

---

## Current Rules

- EMA20 > EMA50
- RSI between 40 and 70
- MACD > 0

---

## Future Improvements

- Liquidity Sweep
- Fair Value Gap
- Break of Structure
- CHOCH
- Order Blocks
- Volume
- Higher Timeframe Confirmation