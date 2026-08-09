class MarketContext:

    def __init__(self):

        # Symbol

        self.symbol = ""

        # Raw Market Data

        self.data = None

        self.timeframes = {}

        # Market Session

        self.session = None

        # Current Candle

        self.latest = None

        # Analysis

        self.summary = None

        self.state = None

        self.signal = None

        self.risk = None

        self.trade_plan = None

        self.decision = None

        self.validation = None

        self.confluence = None

        self.events = []

        # Trading

        self.trade_plan = None