# Lesson 50 - Dynamic Scan Intervals

## Objective

Allow the scheduler to calculate future scan times using configurable intervals.

---

## Architecture

Settings

↓

Scheduler

↓

Scanner

---

## Why?

Scheduling should be configurable instead of hardcoded.

This prepares the application for continuous automation.

---

## Current Features

- Configurable scan interval
- Next scan calculation

---

## Future Improvements

- Persistent last scan
- Cron scheduling
- Session-aware scheduling
- Market-hour scheduling

---

## Key Takeaway

Schedulers should derive timing from configuration rather than fixed values.