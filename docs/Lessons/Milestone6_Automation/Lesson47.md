# Lesson 47 - Configuration Expansion

## Objective

Expand the existing Settings class to support automation modules and begin replacing hardcoded application values with centralized configuration.

---

## Architecture

Settings

↓

Scanner

↓

Trade Filter

↓

Trade Ranker

↓

Presentation

---

## Why?

Configuration already exists.

Rather than creating a second configuration system, we extend the current one so future modules remain configurable.

---

## Current Configuration

- Scanner
- Ranking
- Display
- Risk

---

## Future Improvements

- User Settings
- Strategy Profiles
- Desktop Configuration
- Import / Export Settings

---

## Key Takeaway

Configuration should evolve alongside the application instead of being recreated.