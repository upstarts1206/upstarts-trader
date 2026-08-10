# Lesson 42 - Multi-Symbol Scanner

## Objective

Display analysis results for every symbol in the configured watchlist.

---

## Flow

Watchlist

↓

Scanner

↓

Analyzer

↓

Trade Plans

↓

Console Output

---

## Why?

The scanner should process an entire watchlist rather than a single market.

This prepares the application for filtering, ranking, and notifications.

---

## Future Improvements

- Parallel scanning
- Progress indicator
- Scan timing
- Error handling
- Retry failed symbols

---

## Key Takeaway

A scanner should iterate over markets consistently without changing the analysis logic.