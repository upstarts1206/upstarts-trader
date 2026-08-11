from core.context import MarketContext
from core.analyzer import Analyzer


class BacktestEngine:

    def __init__(self):

        self.analyzer = Analyzer()

    def run(self, symbol):

        context = MarketContext(symbol)

        context = self.analyzer.analyze(context)

        return context