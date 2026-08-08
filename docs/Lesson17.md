# Lesson 17 - Market Context

## Objective

Introduce a MarketContext model to centralize all information about the current market analysis.

---

## Why?

As the application grows, passing multiple objects between services becomes difficult to maintain.

MarketContext acts as a container for:

- Symbol
- Market Data
- Latest Candle
- Summary
- Signal
- Events
- Trade Plan

---

## Benefits

- Cleaner function signatures
- Easier to extend
- Better separation of concerns
- One object represents one analysis session

---

## Key Takeaway

Instead of passing many variables, pass one context object that contains everything related to the current market.