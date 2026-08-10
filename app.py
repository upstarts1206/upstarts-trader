from scanner.scanner import Scanner
from watchlists.default import WATCHLIST
from presentation.console_view import ConsoleView
from summary.scan_summary import ScanSummary
from filters.trade_filter import TradeFilter
from ranking.trade_ranker import TradeRanker
from scheduler.scan_scheduler import ScanScheduler

# Scanner 

scheduler = ScanScheduler()

if scheduler.should_scan():

    scanner = Scanner()

    scan = scanner.scan(WATCHLIST)

    scheduler.mark_scan_complete()

else:

    print("Skipping scan.")

results = scan["results"]

errors = scan["errors"]

# Summary

scan_summary = ScanSummary()

summary = scan_summary.generate(results, errors, scheduler)

# Filter

trade_filter = TradeFilter()

results = trade_filter.filter(results)

# Ranking

ranker = TradeRanker()

results = ranker.rank(results)

# Final Output

view = ConsoleView()

view.display(results, summary, errors)