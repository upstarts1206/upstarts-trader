import pandas as pd


class FairValueGap:

    def detect(self, df: pd.DataFrame):

        df["fvg"] = None

        for i in range(1, len(df) - 1):

            candle_a = df.iloc[i - 1]
            candle_c = df.iloc[i + 1]

            # Bullish FVG
            if candle_c["low"] > candle_a["high"]:

                df.at[df.index[i], "fvg"] = "Bullish"

            # Bearish FVG
            elif candle_c["high"] < candle_a["low"]:

                df.at[df.index[i], "fvg"] = "Bearish"

        return df