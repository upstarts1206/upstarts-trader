import pandas as pd


class LiquiditySweep:

    def detect(self, df: pd.DataFrame):

        df["liquidity_sweep"] = False
        df["liquidity_side"] = None

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
                df.at[df.index[i], "liquidity_sweep"] = True
                df.at[df.index[i], "liquidity_side"] = "Buy Side"

            # Bearish Liquidity Sweep
            if (
                last_swing_low is not None
                and current["low"] < last_swing_low
                and current["close"] > last_swing_low
            ):
                df.at[df.index[i], "liquidity_sweep"] = True
                df.at[df.index[i], "liquidity_side"] = "Sell Side"

        return df