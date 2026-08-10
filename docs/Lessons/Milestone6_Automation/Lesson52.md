# Lesson 52 - Automation Runner

## Objective

Move the complete scan workflow into an Automation Runner.

---

## Architecture

App

↓

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

The application entry point should only start the system.

Workflow orchestration belongs inside a dedicated runner.

---

## Current Features

- Workflow orchestration
- Single scan execution

---

## Future Improvements

- Continuous execution
- Pause / Resume
- Background service
- Graceful shutdown

---

## Key Takeaway

The entry point starts the application.

The runner coordinates the workflow.