# Lesson 45 - Scan Summary

## Objective

Generate statistics for an entire market scan.

---

## Architecture

Watchlist

↓

Scanner

↓

Scan Summary

↓

Trade Filter

↓

Presentation

---

## Why?

A scanner should report both the scan results and the filtered trade candidates.

This provides confidence that the system is working even when no trades qualify.

---

## Current Metrics

- Symbols Scanned
- BUY Count
- WAIT Count
- SKIP Count
- Highest Confidence
- Average Confidence

---

## Future Improvements

- Scan Duration
- Markets per Second
- Filter Pass Rate
- Average Risk/Reward
- Best Setup

---

## Key Takeaway

Summaries describe the overall scan, while filters decide what to display.