import pandas as pd
from config.settings import Settings


class MarketStructure:

    def analyze(self, df: pd.DataFrame):

        df = self.find_swings(df)

        df = self.detect_structure(df)

        return df

    def find_swings(
        self,
        df: pd.DataFrame,
        lookback=Settings.SWING_LOOKBACK,
    ):

        df["swing_high"] = False
        df["swing_low"] = False

        for i in range(lookback, len(df) - lookback):

            current = df.iloc[i]

            left_candles = df.iloc[i - lookback:i]
            right_candles = df.iloc[i + 1:i + lookback + 1]

            if (
                current["high"] > left_candles["high"].max()
                and current["high"] > right_candles["high"].max()
            ):

                df.at[df.index[i], "swing_high"] = True

            if (
                current["low"] < left_candles["low"].min()
                and current["low"] < right_candles["low"].min()
            ):

                df.at[df.index[i], "swing_low"] = True

        return df

    def detect_structure(self, df: pd.DataFrame):

        df["structure"] = None

        current_structure = "Bullish"

        for i in range(len(df)):

            df.at[df.index[i], "structure"] = current_structure

        return df