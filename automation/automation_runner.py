import time

from scanner.scanner import Scanner
from scheduler.scan_scheduler import ScanScheduler
from summary.scan_summary import ScanSummary
from filters.trade_filter import TradeFilter
from ranking.trade_ranker import TradeRanker
from presentation.console_view import ConsoleView
from alerts.alert_manager import AlertManager
from watchlists.default import WATCHLIST


class AutomationRunner:

    def __init__(self):

        self.scheduler = ScanScheduler()

        self.scanner = Scanner()

        self.scan_summary = ScanSummary()

        self.trade_filter = TradeFilter()

        self.trade_ranker = TradeRanker()

        self.console_view = ConsoleView()

        self.alert_manager = AlertManager()

    def run_once(self):

        if not self.scheduler.should_scan():

            return

        self.execute_scan_cycle()

    def run_forever(self):

        print()
        print("========================================")
        print(" UPSTARTS TRADER AUTOMATION STARTED")
        print("========================================")
        print()

        while True:

            if self.scheduler.should_scan():

                self.execute_scan_cycle()

            time.sleep(1)

    def execute_scan_cycle(self):

        scan_result = self.scanner.scan(WATCHLIST)

        self.scheduler.mark_scan_complete()

        results = scan_result["results"]

        errors = scan_result["errors"]

        summary = self.scan_summary.generate(

            results,

            errors,

            self.scheduler,

        )

        trade_candidates = self.trade_filter.filter(results)

        trade_candidates = self.trade_ranker.rank(trade_candidates)

        trade_alerts = []

        for context in trade_candidates:

            if self.alert_manager.should_alert(context):

                trade_alerts.append(context)

        self.console_view.display(

            results=trade_alerts,

            summary=summary,

            errors=errors,

            all_results=results,

        )