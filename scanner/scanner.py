from core.analyzer import Analyzer
from models.market_context import MarketContext


class Scanner:

    def __init__(self):

        self.analyzer = Analyzer()

    def scan(self, symbols):

        results = []

        for symbol in symbols:

            context = MarketContext()

            context.symbol = symbol

            context = self.analyzer.analyze(context)

            results.append(context)

        return results