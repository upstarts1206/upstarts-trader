# Lesson 18 - Analyzer

## Objective

Introduce an Analyzer that orchestrates the entire market analysis workflow.

---

## Responsibility

The Analyzer coordinates all services.

It does not contain trading logic.

---

## Benefits

- Keeps app.py simple.
- Centralizes orchestration.
- Makes adding future analysis steps easy.
- Reduces duplication.

---

## Key Takeaway

Orchestration is different from implementation.

The Analyzer tells components when to execute.

Each component remains responsible for its own logic.