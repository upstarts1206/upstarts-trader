# Lesson 53 - Continuous Automation

## Objective

Allow the application to continuously monitor the market.

---

## Architecture

Automation Runner

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

Automation requires the application to remain active.

The runner continuously asks the scheduler if a scan should occur.

---

## Current Features

- Continuous execution
- Shared scan workflow
- Reusable execution pipeline

---

## Future Improvements

- Graceful shutdown
- Pause / Resume
- Background service

---

## Key Takeaway

The runner controls the application lifetime while the scheduler controls scan timing.