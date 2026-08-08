# Lesson 12 - Market Structure Engine

## Objective

Teach the application how to identify Swing Highs and Swing Lows.

---

## Swing High

A candle whose High is greater than both the previous and next candle.

---

## Swing Low

A candle whose Low is lower than both the previous and next candle.

---

## Responsibility

The Market Structure engine analyzes historical candles.

It does not:

- Generate trading signals
- Execute trades
- Detect BOS
- Detect CHOCH

Those features will be built on top of this engine.

---

## Output

Adds two columns:

- swing_high
- swing_low