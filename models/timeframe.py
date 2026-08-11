class Timeframe:

    def __init__(self, name: str):

        # ----------------------------------------
        # Metadata
        # ----------------------------------------

        self.name = name

        # ----------------------------------------
        # Market Data
        # ----------------------------------------

        self.data = None

        self.latest = None

        # ----------------------------------------
        # Analysis
        # ----------------------------------------

        self.summary = None

        self.state = None

        self.bias = None

        self.signal = None

        self.confluence = None

        self.setup = None

        # ----------------------------------------
        # Structure
        # ----------------------------------------

        self.trend = None

        self.structure = None

        # ----------------------------------------
        # Debug
        # ----------------------------------------

        self.notes = []