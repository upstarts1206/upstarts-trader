from core.pipeline import Pipeline

from analysis.timeframe_analyzer import TimeframeAnalyzer
from analysis.bias_aggregator import BiasAggregator

from risk.engine import RiskEngine
from sessions.engine import SessionEngine

from services.signal import Signal

from setups.engine import SetupEngine
from decision.engine import DecisionEngine

from planner.trade_planner import TradePlanner
from validation.trade_validator import TradeValidator


class MultiTimeframeEngine:

    def __init__(self):

        self.pipeline = Pipeline()

        self.timeframe_analyzer = TimeframeAnalyzer()

        self.bias_aggregator = BiasAggregator()

        self.risk = RiskEngine()

        self.session_engine = SessionEngine()

        self.signal = Signal()

        self.setup_engine = SetupEngine()

        self.decision_engine = DecisionEngine()

        self.trade_planner = TradePlanner()

        self.trade_validator = TradeValidator()

    def analyze(self, context):

        # ----------------------------------------
        # Analyze each timeframe
        # ----------------------------------------

        for name, timeframe in context.timeframes.items():

            timeframe.data = self.pipeline.run_timeframe(

                symbol=context.symbol,

                timeframe=name,

            )

            self.timeframe_analyzer.analyze(

                timeframe

            )

        # ----------------------------------------
        # Entry timeframe becomes execution context
        # ----------------------------------------

        entry = context.timeframes["entry"]

        context.data = entry.data

        context.latest = entry.latest

        context.summary = entry.summary

        context.state = entry.state

        # ----------------------------------------
        # Aggregate bias
        # ----------------------------------------

        context.bias = self.bias_aggregator.analyze(

            context

        )

        # ----------------------------------------
        # Risk
        # ----------------------------------------

        context.risk = self.risk.analyze(

            account_balance=10000,

            entry=context.latest["close"],

            risk_percent=0.01,

            df=context.data,

        )

        # ----------------------------------------
        # Session
        # ----------------------------------------

        context.session = self.session_engine.detect()

        # ----------------------------------------
        # Signal
        # ----------------------------------------

        context.signal = self.signal.analyze(

            context

        )

        # ----------------------------------------
        # Setup
        # ----------------------------------------

        context.setup = self.setup_engine.detect(

            context

        )

        # ----------------------------------------
        # Decision
        # ----------------------------------------

        context.decision = self.decision_engine.decide(

            context

        )

        # ----------------------------------------
        # Trade Plan
        # ----------------------------------------

        context.trade_plan = self.trade_planner.build(

            context

        )

        # ----------------------------------------
        # Validation
        # ----------------------------------------

        context.validation = self.trade_validator.validate(

            context

        )

        return context