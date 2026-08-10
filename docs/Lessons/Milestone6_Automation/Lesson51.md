# Lesson 51 - Automation Runner

## Objective

Separate application lifetime management from scheduling and market analysis.

---

## Architecture

Runner

↓

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

The runner controls how long the application lives.

The scheduler decides when scans occur.

---

## Current Features

- Single execution runner

---

## Future Improvements

- Continuous execution
- Graceful shutdown
- Pause / Resume
- Background service

---

## Key Takeaway

Application lifetime should be independent from scan scheduling.