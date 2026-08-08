from core.pipeline import Pipeline
from services.summary import Summary
from services.signal import Signal
from services.state import MarketState
from risk.engine import RiskEngine


class Analyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.summary = Summary()

        self.signal = Signal()

        self.state = MarketState()

        self.risk = RiskEngine()

    def analyze(self, context):

        context.data = self.pipeline.run(context.symbol)

        context.latest = context.data.iloc[-1]

        context.summary = self.summary.generate(context.latest)

        context.state = self.state.generate(context.summary)

        context.signal = self.signal.analyze(context.summary)

        context.risk = self.risk.analyze(
            account_balance=10000,
            entry=context.latest["close"],
            stop_loss=context.latest["close"] * 0.99,
            take_profit=context.latest["close"] * 1.03,
            risk_percent=0.01,
        )

        return context