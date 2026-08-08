# Lesson 3 - EMA Indicator

## Goal

Create a reusable EMA indicator that can be used by any trading strategy.

---

## Input

A Pandas DataFrame containing historical OHLCV market data.

A period value (example: 20, 50, 200).

---

## Output

The same DataFrame with an additional EMA column.

Example:

Timestamp
Open
High
Low
Close
Volume
EMA_20

---

## Responsibility

The EMA class should ONLY calculate the EMA.

It should not:

- Download market data
- Execute trades
- Save files
- Analyze strategies

Those responsibilities belong to other modules.

---

## Why?

Keeping each module responsible for one task makes the project easier to maintain and extend.