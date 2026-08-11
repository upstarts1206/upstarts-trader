from core.market import Market

from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD

from analysis.structure import MarketStructure
from analysis.bos import BreakOfStructure
from analysis.choch import ChangeOfCharacter
from analysis.fvg import FairValueGap
from analysis.order_block import OrderBlock
from analysis.premium_discount import PremiumDiscount
from analysis.liquidity_sweep import LiquiditySweep

from config.settings import Settings


class Pipeline:

    def __init__(self):

        self.market = Market()

        self.ema = EMA()
        self.rsi = RSI()
        self.macd = MACD()

        self.structure = MarketStructure()
        self.bos = BreakOfStructure()
        self.choch = ChangeOfCharacter()
        self.fvg = FairValueGap()
        self.order_block = OrderBlock()
        self.premium_discount = PremiumDiscount()
        self.liquidity_sweep = LiquiditySweep()

    # --------------------------------------------------
    # Version 1
    # --------------------------------------------------

    def run(self, symbol: str):

        return self.run_timeframe(

            symbol=symbol,

            timeframe="structure",

        )

    # --------------------------------------------------
    # Version 2
    # --------------------------------------------------

    def run_multi_timeframe(self, symbol: str):

        return {

            "macro": self.run_timeframe(

                symbol=symbol,

                timeframe="macro",

            ),

            "structure": self.run_timeframe(

                symbol=symbol,

                timeframe="structure",

            ),

            "entry": self.run_timeframe(

                symbol=symbol,

                timeframe="entry",

            ),

        }

    # --------------------------------------------------
    # Generic Pipeline
    # --------------------------------------------------

    def run_timeframe(

        self,

        symbol: str,

        timeframe: str,

    ):

        interval = Settings.TIMEFRAMES[timeframe]

        df = self.market.get_candles(

            symbol=symbol,

            interval=interval,

            limit=200,

        )

        # -------------------------
        # Indicators
        # -------------------------

        df = self.ema.calculate(df, period=20)
        df = self.ema.calculate(df, period=50)

        df = self.rsi.calculate(df, period=14)

        df = self.macd.calculate(df)

        # -------------------------
        # Market Structure
        # -------------------------

        df = self.structure.analyze(df)

        df = self.bos.detect(df)

        df = self.choch.detect(df)

        # -------------------------
        # Smart Money Concepts
        # -------------------------

        df = self.fvg.detect(df)

        df = self.premium_discount.detect(df)

        df = self.liquidity_sweep.detect(df)

        df = self.order_block.detect(df)

        return df