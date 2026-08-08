class MarketContext:

    def __init__(self):

        # Symbol

        self.symbol = ""

        # Raw Market Data

        self.data = None

        self.timeframes = {}

        # Current Candle

        self.latest = None

        # Analysis

        self.summary = None

        self.state = None

        self.signal = None

        self.events = []

        # Trading

        self.trade_plan = None