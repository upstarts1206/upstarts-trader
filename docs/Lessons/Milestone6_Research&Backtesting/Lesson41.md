# Lesson 41 - Watchlists

## Objective

Introduce configurable watchlists as the input source for market scanning.

---

## Architecture

Watchlist

↓

Scanner

↓

Analyzer

↓

Trade Plans

---

## Why?

Separating watchlists from the scanner allows users to organize symbols by trading style or preference without modifying application logic.

---

## Future Improvements

- Swing Watchlist
- Scalp Watchlist
- Futures Watchlist
- User-defined Watchlists
- Load watchlists from JSON/YAML

---

## Key Takeaway

The scanner should analyze whatever symbols it is given. It should not decide which symbols belong in a watchlist.