# Lesson 49 - Scan Scheduler

## Objective

Introduce a scheduler responsible for deciding when scans should execute.

---

## Architecture

Scheduler

↓

Scanner

↓

Summary

↓

Filter

↓

Ranking

↓

Presentation

---

## Why?

Scheduling should be independent from market analysis.

This prepares the application for timed automation without changing the trading engine.

---

## Current Features

- Manual scan mode
- Scheduler abstraction

---

## Future Improvements

- Every 15 minutes
- Configurable intervals
- Trading session schedules
- Pause / Resume

---

## Key Takeaway

The scheduler decides *when* to scan, not *how* to scan.