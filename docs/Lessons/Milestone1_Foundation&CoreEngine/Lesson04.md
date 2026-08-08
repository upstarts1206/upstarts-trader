# Lesson 4 - RSI Indicator 

## Goal

Create a reusable RSI indicator that can be used by any trading strategy.

## What is an RSI?

EMA vs RSI
EMA tells the direction of the price
RSI tells how fast the price goes to that direction
RSI Ranges from 0 to 100 
In general 70+ is overbought, and 30- is oversold
You dont base on this alone as RSI can hold above 70 for days to months but still not get the sell off


---

## Input

Calculation was written manually instead of using Pandas.
A Pandas DataFrame containing historical OHLCV market data.

A period value (example: 14).
---

## Output

The same DataFrame with an additional RSI column.

Example:

Timestamp
Open
High
Low
Close
Volume
EMA_20
RSI_14

---

## Responsibility

The RSI class should ONLY calculate the RSI.

It should not:

- Download market data
- Execute trades
- Save files
- Analyze strategies

Those responsibilities belong to other modules.

---

## Why?

Keeping each module responsible for one task makes the project easier to maintain and extend.