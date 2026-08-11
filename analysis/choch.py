import pandas as pd


class ChangeOfCharacter:

    def detect(self, df: pd.DataFrame):

        df["choch"] = False
        df["choch_direction"] = None

        last_swing_high = None
        last_swing_low = None

        for i in range(len(df)):

            current = df.iloc[i]

            # -------------------------
            # Remember latest swings
            # -------------------------

            if current["swing_high"]:
                last_swing_high = current["high"]

            if current["swing_low"]:
                last_swing_low = current["low"]

            # -------------------------
            # Bearish CHOCH
            # -------------------------

            if (
                last_swing_low is not None
                and current["close"] < last_swing_low
            ):

                df.at[df.index[i], "choch"] = True
                df.at[df.index[i], "choch_direction"] = "Bearish"

                last_swing_low = None

            # -------------------------
            # Bullish CHOCH
            # -------------------------

            elif (
                last_swing_high is not None
                and current["close"] > last_swing_high
            ):

                df.at[df.index[i], "choch"] = True
                df.at[df.index[i], "choch_direction"] = "Bullish"

                last_swing_high = None

        return df