# Lesson 34 - Trade Validator

## Objective

Validate a generated trade plan before it can be considered actionable.

---

## Current Validation Rules

- Stop Loss must be below Entry
- Take Profit must be above Entry
- Position Size must be greater than zero
- Risk / Reward must meet the minimum threshold

---

## Why?

Even a strong trading signal should not produce an invalid trade plan.

The Trade Validator acts as the final quality gate before a notification or recommendation is sent.

---

## Future Improvements

- Direction-aware validation (BUY / SELL)
- Strategy-specific validation
- Market session validation
- News event validation
- Volatility validation

---

## Key Takeaway

A recommendation should not only be intelligent—it must also be internally consistent and safe to present.