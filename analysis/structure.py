import pandas as pd


class MarketStructure:

    def find_swings(self, df: pd.DataFrame):

        df["swing_high"] = False
        df["swing_low"] = False

        for i in range(1, len(df) - 1):

            previous = df.iloc[i - 1]
            current = df.iloc[i]
            next_candle = df.iloc[i + 1]

            if (
                current["high"] > previous["high"]
                and current["high"] > next_candle["high"]
            ):
                df.at[df.index[i], "swing_high"] = True

            if (
                current["low"] < previous["low"]
                and current["low"] < next_candle["low"]
            ):
                df.at[df.index[i], "swing_low"] = True

        return df