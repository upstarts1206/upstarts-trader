from services.summary import Summary
from services.state import MarketState
from analysis.market_phase import MarketPhase


class TimeframeAnalyzer:

    def __init__(self):

        self.summary = Summary()
        self.market_state = MarketState()
        self.market_phase = MarketPhase()

    def analyze(self, timeframe):

        timeframe.latest = timeframe.data.iloc[-1]

        timeframe.summary = self.summary.generate(
            timeframe.latest
        )

        timeframe.state = self.market_state.generate(
            timeframe.summary
        )

        # NEW
        timeframe.phase = self.market_phase.analyze(
            timeframe.latest
        )

        return timeframe