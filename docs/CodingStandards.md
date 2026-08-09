# Upstarts Trader Coding Standards

This document defines the coding conventions used throughout Upstarts Trader.

The objective is consistency, readability, and maintainability.

Before contributing code, read this document and ensure new code follows these standards.

> Code is read more often than it is written.

---

# Core Principles

## 1. Single Responsibility Principle

Every class should have one clear responsibility.

Good

- RiskEngine
- DecisionEngine
- TradePlanner
- ConfidenceEngine

Avoid

- Mega classes that perform multiple unrelated tasks.

---

## 2. Composition Over Duplication

Large modules should delegate work to smaller modules.

Example

RiskEngine

- StopLossEngine
- TakeProfitEngine
- PositionSizer

DecisionEngine

- ConfidenceEngine

---

## 3. Feature-Based Architecture

Organize files by feature, not by technical layer.

Good

analysis/
risk/
decision/
planner/

Avoid

helpers/
misc/
random/

---

# Naming Conventions

## Classes

Classes are nouns.

Examples

MarketContext

RiskEngine

TradePlanner

ConfidenceEngine

PositionSizer

Avoid

CalculateRisk

AnalyzeTrade

Helper

---

## Methods

Methods are verbs.

Examples

calculate()

generate()

build()

analyze()

decide()

detect()

run()

Avoid

risk()

summary()

decision()

---

## Variables

Variables should describe exactly what they contain.

Good

entry_price

stop_price

take_profit_price

risk_amount

confidence_result

trade_plan

market_context

Avoid

data

result

temp

value

x

---

## Result Objects

Methods that return multiple values should return Result Objects.

Good

stop_result

take_profit_result

confidence_result

Example

{
    "price": 72.80,
    "reason": "Below Swing Low"
}

Avoid returning multiple unrelated variables.

---

# File Organization

Each file should represent one concept.

Example

risk/

    engine.py

    stop_loss.py

    take_profit.py

    position_size.py

Avoid

risk.py

that contains everything.

---

# Method Layout

Methods should follow a logical flow.

Example

def analyze():

    # Input

    # Processing

    # Validation

    # Calculation

    # Return

Use section comments when methods become longer than ~20 lines.

Example

# -------------------------
# Risk
# -------------------------

---

# Comments

Use comments to separate logical sections.

Good

# -------------------------
# Stop Loss
# -------------------------

Avoid explaining obvious code.

Bad

# Add one

score += 1

---

# Configuration

Avoid hardcoded values.

Preferred

Settings.DEFAULT_RISK

Settings.STOP_BUFFER

Avoid

0.01

0.10

Hardcoded values are acceptable temporarily during development but should eventually move into Settings or user-configurable profiles.

---

# Constants

Repeated strings should become constants.

Good

BUY

WAIT

SKIP

BULLISH

BEARISH

Avoid

"BUY"

"Bullish"

throughout the project.

---

# Models

Models should represent data only.

Examples

MarketContext

TradePlan (Future)

TraderProfile (Future)

Models should not contain business logic.

---

# Engine Responsibilities

Each engine has one responsibility.

Pipeline

Retrieve and prepare market data.

Analyzer

Coordinate the analysis workflow.

RiskEngine

Evaluate trade risk.

DecisionEngine

Determine the recommended action.

ConfidenceEngine

Calculate confidence.

TradePlanner

Assemble the final trade plan.

---

# Architectural Rules

Business logic belongs inside the appropriate engine.

Avoid putting calculations inside

app.py

TradePlanner

MarketContext

The application should orchestrate, not calculate.

---

# Error Handling

Return None only when analysis cannot continue.

Avoid silently ignoring errors.

Future versions should introduce custom exceptions where appropriate.

---

# Future Standards

These standards will be adopted in later versions.

- Type hints
- Dataclasses / Pydantic models
- Unit testing
- Logging framework
- Dependency Injection
- Event-driven architecture

---

# Development Philosophy

Build the simplest solution that is:

- Correct
- Readable
- Testable
- Extensible

Avoid premature optimization.

Implement features only when they provide clear value.

---

# Product Philosophy

Every feature should answer at least one question.

Does it improve trading decisions?

Can it be configured?

Can it be backtested?

Can it be explained?

Does it fit the current milestone?

If the answer is no, it belongs in the backlog—not in the current implementation.

---

# Preferred Patterns

## Orchestrator Pattern

Large modules coordinate smaller modules.

Examples

Analyzer

↓

RiskEngine

↓

DecisionEngine

↓

TradePlanner

---

## Strategy Pattern

Behavior should be replaceable.

Examples

Trading Strategies

Future

Stop Loss Providers

Take Profit Providers

---

## Result Object Pattern

Return objects instead of multiple variables.

Examples

stop_result

take_profit_result

confidence_result

---

## Context Pattern

Pass a context object instead of many unrelated parameters.

Example

MarketContext

Future

TradeContext

TraderProfile