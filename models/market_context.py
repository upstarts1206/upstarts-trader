from models.timeframe import Timeframe

class MarketContext:

    def __init__(self):

        # --------------------------------------------------
        # Symbol
        # --------------------------------------------------

        self.symbol = ""

        # --------------------------------------------------
        # Version 1 (Current Engine)
        # --------------------------------------------------

        self.data = None
        self.latest = None

        # --------------------------------------------------
        # Version 2 (Multi-Timeframe Engine)
        # --------------------------------------------------

        self.timeframes = {

            "macro": Timeframe("macro"),

            "structure": Timeframe("structure"),

            "entry": Timeframe("entry"),

        }

        # --------------------------------------------------
        # Shared Analysis
        # --------------------------------------------------

        self.summary = None

        self.state = None

        self.signal = None

        self.bias = None

        self.confluence = None

        self.setup = None

        self.decision = None

        self.risk = None

        self.validation = None

        self.trade_plan = None

        # --------------------------------------------------
        # Market Session
        # --------------------------------------------------

        self.session = None

        # --------------------------------------------------
        # Misc
        # --------------------------------------------------

        self.events = []