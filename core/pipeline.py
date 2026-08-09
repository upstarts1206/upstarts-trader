from core.market import Market
from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD
from analysis.structure import MarketStructure
from analysis.bos import BreakOfStructure
from analysis.choch import ChangeOfCharacter
from analysis.liquidity import LiquiditySweep
from analysis.fvg import FairValueGap
from analysis.order_block import OrderBlock
from analysis.premium_discount import PremiumDiscount
from analysis.liquidity_sweep import LiquiditySweep

class Pipeline:

    def __init__(self):

        self.market = Market()

        self.ema = EMA()

        self.rsi = RSI()

        self.macd = MACD()

        self.structure = MarketStructure()

        self.bos = BreakOfStructure()

        self.choch = ChangeOfCharacter()

        self.liquidity = LiquiditySweep()

        self.fvg = FairValueGap()

        self.order_block = OrderBlock()

        self.premium_discount = PremiumDiscount()

        self.liquidity_sweep = LiquiditySweep()

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
        df = self.choch.detect(df)
        df = self.fvg.detect(df)
        df = self.premium_discount.detect(df)
        df = self.liquidity_sweep.detect(df)
        df = self.order_block.detect(df)

        return df