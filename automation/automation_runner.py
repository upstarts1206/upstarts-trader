import time

from scanner.scanner import Scanner
from scheduler.scan_scheduler import ScanScheduler
from summary.scan_summary import ScanSummary
from filters.trade_filter import TradeFilter
from ranking.trade_ranker import TradeRanker
from presentation.console_view import ConsoleView
from watchlists.default import WATCHLIST


class AutomationRunner:

    def __init__(self):

        self.scheduler = ScanScheduler()

        self.scanner = Scanner()

        self.scan_summary = ScanSummary()

        self.trade_filter = TradeFilter()

        self.trade_ranker = TradeRanker()

        self.console_view = ConsoleView()

    def run_once(self):

        if not self.scheduler.should_scan():

            return

        self.execute_scan()

    def run_forever(self):

        print()
        print("========================================")
        print(" UPSTARTS TRADER AUTOMATION STARTED")
        print("========================================")
        print()

        while True:

            if self.scheduler.should_scan():

                self.execute_scan()

            time.sleep(1)

    def execute_scan(self):

        scan = self.scanner.scan(WATCHLIST)

        self.scheduler.mark_scan_complete()

        results = scan["results"]

        errors = scan["errors"]

        summary = self.scan_summary.generate(

            results,

            errors,

            self.scheduler,

        )

        results = self.trade_filter.filter(results)

        results = self.trade_ranker.rank(results)

        self.console_view.display(

            results,

            summary,

            errors,

        )