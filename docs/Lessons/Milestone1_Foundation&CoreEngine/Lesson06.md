# Lesson 6 - MACD Indicator

## Objective

Implement a reusable MACD indicator and integrate it into the processing pipeline.

---

## What is MACD?

MACD (Moving Average Convergence Divergence) is a momentum indicator that measures the relationship between two Exponential Moving Averages (EMAs).

---

## Components

### MACD Line

Difference between the fast EMA and slow EMA.

Default:

- Fast EMA: 12
- Slow EMA: 26

Formula:

MACD = EMA12 - EMA26

---

### Signal Line

An EMA of the MACD Line.

Default period:

9

---

### Histogram

Difference between the MACD Line and the Signal Line.

Formula:

Histogram = MACD - Signal Line

---

## Input

Pandas DataFrame containing historical OHLCV data.

---

## Output

The original DataFrame with three additional columns:

- MACD
- MACD_SIGNAL
- MACD_HISTOGRAM

---

## Project Architecture

Market Data
→ EMA
→ RSI
→ MACD
→ Strategy Engine (future)

The MACD indicator is implemented as an independent module inside the `indicators` package and is executed by the Pipeline.

---

## Responsibility

The MACD class is responsible only for calculating MACD values.

It does not:

- Download market data
- Execute trades
- Generate trading signals
- Save files

These responsibilities belong to other modules.

---

## Result

The processing pipeline now enriches market data with:

- EMA 20
- EMA 50
- RSI 14
- MACD
- Signal Line
- Histogram

This prepares the dataset for future strategy evaluation and AI analysis.