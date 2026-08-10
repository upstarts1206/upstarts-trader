# Lesson 43 - Presentation Layer

## Objective

Separate application logic from presentation.

---

## Architecture

Scanner

↓

Analyzer

↓

Trade Plans

↓

Presentation Layer

↓

Console

---

## Why?

The application should not mix business logic with output formatting.

This allows future presentation layers such as Discord, Telegram, Web UI, and APIs.

---

## Future Improvements

- Discord View
- Telegram View
- HTML Dashboard
- JSON Export
- Rich Terminal UI

---

## Key Takeaway

Business logic should produce data. Presentation layers decide how to display it.