# Decision 007

Title

Event-Driven Scanner

Status

Accepted

Context

The application currently requires manual execution of market analysis.

Decision

Future versions will include an event-driven Scanner Engine that automatically analyzes configured markets after candle close.

The scanner will feed symbols into the existing Analyzer rather than implementing a separate analysis pipeline.

Consequences

Positive

- Reuses existing Analyzer architecture.
- Supports multiple notification providers.
- Keeps analysis logic centralized.
- Enables passive market monitoring.

Negative

- Requires scheduling infrastructure.
- Requires notification management.
- Requires watchlist management.