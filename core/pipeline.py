from core.market import Market
from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD
from analysis.structure import MarketStructure
from analysis.bos import BreakOfStructure


class Pipeline:

    def __init__(self):

        self.market = Market()

        self.ema = EMA()

        self.rsi = RSI()

        self.macd = MACD()

        self.structure = MarketStructure()

        self.bos = BreakOfStructure()

    def run(self, symbol: str):

        df = self.market.get_candles(
            symbol=symbol,
            interval="60",
            limit=200
        )

        df = self.ema.calculate(df, period=20)
        df = self.ema.calculate(df, period=50)
        df = self.rsi.calculate(df, period=14)
        df = self.macd.calculate(df)
        df = self.structure.find_swings(df)
        df = self.bos.detect(df)

        return df