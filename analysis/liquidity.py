import pandas as pd


class LiquiditySweep:

    def detect(self, df: pd.DataFrame):

        df["liquidity"] = None

        last_swing_high = None
        last_swing_low = None

        for i in range(len(df)):

            current = df.iloc[i]

            # Update latest swing levels
            if current["swing_high"]:
                last_swing_high = current["high"]

            if current["swing_low"]:
                last_swing_low = current["low"]

            # Bullish Liquidity Sweep
            if (
                last_swing_high is not None
                and current["high"] > last_swing_high
                and current["close"] < last_swing_high
            ):
                df.at[df.index[i], "liquidity"] = "Bullish Sweep"

            # Bearish Liquidity Sweep
            if (
                last_swing_low is not None
                and current["low"] < last_swing_low
                and current["close"] > last_swing_low
            ):
                df.at[df.index[i], "liquidity"] = "Bearish Sweep"

        return df