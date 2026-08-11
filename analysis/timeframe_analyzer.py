from services.summary import Summary
from services.state import MarketState


class TimeframeAnalyzer:

    def __init__(self):

        self.summary = Summary()

        self.market_state = MarketState()

    def analyze(self, timeframe):

        timeframe.latest = timeframe.data.iloc[-1]

        timeframe.summary = self.summary.generate(

            timeframe.latest

        )

        timeframe.state = self.market_state.generate(

            timeframe.summary

        )

        return timeframe