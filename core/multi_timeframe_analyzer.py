from core.pipeline import Pipeline
from analysis.timeframe_analyzer import TimeframeAnalyzer
from analysis.bias_aggregator import BiasAggregator


class MultiTimeframeAnalyzer:

    def __init__(self):

        self.pipeline = Pipeline()

        self.timeframe_analyzer = TimeframeAnalyzer()

        self.bias_aggregator = BiasAggregator()

    def analyze(self, context):

        # ----------------------------------------
        # Analyze each timeframe
        # ----------------------------------------

        for name, timeframe in context.timeframes.items():

            timeframe.data = self.pipeline.run_timeframe(

                symbol=context.symbol,

                timeframe=name,

            )

            self.timeframe_analyzer.analyze(timeframe)

        # ----------------------------------------
        # Aggregate market bias
        # ----------------------------------------

        context.bias = self.bias_aggregator.analyze(context)

        return context