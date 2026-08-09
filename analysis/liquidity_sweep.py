import pandas as pd


class LiquiditySweep:

    def detect(self, df: pd.DataFrame):

        df["liquidity_sweep"] = False
        df["liquidity_side"] = None

        for i in range(2, len(df)):

            current = df.iloc[i]
            previous = df.iloc[i - 1]

            # -------------------------
            # High Sweep
            # -------------------------

            if (
                current["high"] > previous["high"]
                and current["close"] < previous["high"]
            ):

                df.at[df.index[i], "liquidity_sweep"] = True
                df.at[df.index[i], "liquidity_side"] = "Buy Side"

            # -------------------------
            # Low Sweep
            # -------------------------

            elif (
                current["low"] < previous["low"]
                and current["close"] > previous["low"]
            ):

                df.at[df.index[i], "liquidity_sweep"] = True
                df.at[df.index[i], "liquidity_side"] = "Sell Side"

        return df