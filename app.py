from core.analyzer import Analyzer
from models.market_context import MarketContext

context = MarketContext()

context.symbol = "SOLUSDT"

analyzer = Analyzer()

context = analyzer.analyze(context)