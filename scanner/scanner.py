from core.analyzer import Analyzer
from models.market_context import MarketContext


class Scanner:

    def __init__(self):

        self.analyzer = Analyzer()

    def scan(self, symbols):

        scan_results = []

        scan_errors = []

        for symbol in symbols:

            try:

                context = MarketContext()

                context.symbol = symbol

                context = self.analyzer.analyze(context)

                scan_results.append(context)

            except Exception as e:

                scan_errors.append({

                    "symbol": symbol,

                    "error": str(e),

                })

        return {

            "results": scan_results,

            "errors": scan_errors,

        }