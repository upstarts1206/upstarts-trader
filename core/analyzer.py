from core.pipeline import Pipeline
from services.summary import Summary
from services.signal import Signal
from services.state import MarketState
from risk.engine import RiskEngine
from planner.trade_planner import TradePlanner


class Analyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.summary = Summary()

        self.signal = Signal()

        self.state = MarketState()

        self.risk = RiskEngine()

        self.trade_planner = TradePlanner()

    def analyze(self, context):

        context.data = self.pipeline.run(context.symbol)

        context.latest = context.data.iloc[-1]

        context.summary = self.summary.generate(context.latest)

        context.state = self.state.generate(context.summary)

        context.signal = self.signal.analyze(context.summary)

        context.risk = self.risk.analyze(
            account_balance=10000,
            entry=context.latest["close"],
            risk_percent=0.01,
            df=context.data
        )

        context.trade_plan = self.trade_planner.build(context)

        return context