from config.settings import Settings

from core.single_timeframe_engine import SingleTimeframeEngine
from core.multi_timeframe_engine import MultiTimeframeEngine


class Analyzer:

    def __init__(self):

        self.single_engine = SingleTimeframeEngine()

        self.multi_engine = MultiTimeframeEngine()

    def analyze(self, context):

        if Settings.MULTI_TIMEFRAME:

            return self.multi_engine.analyze(context)

        return self.single_engine.analyze(context)