from core.pipeline import Pipeline
from services.summary import Summary
from services.signal import Signal
from services.state import MarketState
from risk.engine import RiskEngine
from planner.trade_planner import TradePlanner
from decision.engine import DecisionEngine
from validation.trade_validator import TradeValidator


class Analyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.summary = Summary()

        self.signal = Signal()

        self.state = MarketState()

        self.risk = RiskEngine()

        self.trade_planner = TradePlanner()

        self.decision_engine = DecisionEngine()

        self.trade_validator = TradeValidator()

    def analyze(self, context):

        # -------------------------
        # Market Data
        # -------------------------

         context.data = self.pipeline.run(context.symbol)
         context.latest = context.data.iloc[-1]

        # -------------------------
        # Analysis
        # -------------------------

         context.summary = self.summary.generate(context.latest)
         context.state = self.state.generate(context.summary)
         context.signal = self.signal.analyze(context.summary)

        # -------------------------
        # Risk
        # -------------------------

         context.risk = self.risk.analyze(
            account_balance=10000,
            entry=context.latest["close"],
            risk_percent=0.01,
            df=context.data
        )

        # -------------------------
        # Decision
        # -------------------------

         context.decision = self.decision_engine.decide(context)

        # -------------------------
        # Trade Plan
        # -------------------------

         context.trade_plan = self.trade_planner.build(context)

        # -------------------------
        # Validation
        # -------------------------

         context.validation = self.trade_validator.validate(context)

         return context