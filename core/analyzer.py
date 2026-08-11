from core.pipeline import Pipeline
from services.summary import Summary
from services.state import MarketState
from services.signal import Signal
from risk.engine import RiskEngine
from sessions.engine import SessionEngine
from confluence.engine import ConfluenceEngine
from bias.engine import BiasEngine
from setups.engine import SetupEngine
from decision.engine import DecisionEngine
from planner.trade_planner import TradePlanner
from validation.trade_validator import TradeValidator


class Analyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.summary = Summary()

        self.market_state = MarketState()

        self.signal = Signal()

        self.risk = RiskEngine()

        self.session_engine = SessionEngine()

        self.confluence_engine = ConfluenceEngine()   

        self.bias_engine = BiasEngine()     

        self.setup_engine = SetupEngine()

        self.decision_engine = DecisionEngine()

        self.trade_planner = TradePlanner()

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
         context.state = self.market_state.generate(context.summary)
         context.signal = self.signal.analyze(context)

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
        # Session
        # -------------------------

         context.session = self.session_engine.detect()

        # -------------------------
        # Confluence
        # -------------------------

         context.confluence = self.confluence_engine.analyze(context) 

        # -------------------------
        # Market Bias
        # -------------------------

         context.bias = self.bias_engine.analyze(context) 

        # ------------------------
        # Setup
        # ------------------------
        
         context.setup = self.setup_engine.detect(context)

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