from core.pipeline import Pipeline
from services.summary import Summary
from services.signal import Signal
from services.state import MarketState


class Analyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.summary = Summary()

        self.signal = Signal()

        self.state = MarketState()

    def analyze(self, context):

        context.data = self.pipeline.run(context.symbol)

        context.latest = context.data.iloc[-1]

        context.summary = self.summary.generate(context.latest)

        context.state = self.state.generate(context.summary)

        context.signal = self.signal.analyze(context.summary)

        return context