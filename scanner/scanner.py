from core.analyzer import Analyzer
from models.market_context import MarketContext


class Scanner:

    def __init__(self):

        self.analyzer = Analyzer()

    def scan(self, symbols):

        results = []

        errors = []

        for symbol in symbols:

            try:

                context = MarketContext()

                context.symbol = symbol

                context = self.analyzer.analyze(context)

                results.append(context)

            except Exception as e:

                errors.append({

                    "symbol": symbol,

                    "error": str(e),

                })

        return {

            "results": results,

            "errors": errors,

        }