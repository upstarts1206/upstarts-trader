import pandas as pd


class BreakOfStructure:

    def detect(self, df: pd.DataFrame):

        df["bos"] = False
        df["confirmed_bos"] = False
        df["bos_direction"] = None

        last_swing_high = None
        last_swing_low = None

        awaiting_bullish_confirmation = False
        awaiting_bearish_confirmation = False

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
            # Bullish BOS
            # -------------------------

            if (
                last_swing_high is not None
                and current["close"] > last_swing_high
            ):

                df.at[df.index[i], "bos"] = True
                df.at[df.index[i], "bos_direction"] = "Bullish"

                awaiting_bullish_confirmation = True

                last_swing_high = None

            # -------------------------
            # Bearish BOS
            # -------------------------

            elif (
                last_swing_low is not None
                and current["close"] < last_swing_low
            ):

                df.at[df.index[i], "bos"] = True
                df.at[df.index[i], "bos_direction"] = "Bearish"

                awaiting_bearish_confirmation = True

                last_swing_low = None

            # -------------------------
            # Bullish Confirmation
            # -------------------------

            if (
                awaiting_bullish_confirmation
                and current["swing_high"]
            ):

                df.at[df.index[i], "confirmed_bos"] = True

                awaiting_bullish_confirmation = False

            # -------------------------
            # Bearish Confirmation
            # -------------------------

            if (
                awaiting_bearish_confirmation
                and current["swing_low"]
            ):

                df.at[df.index[i], "confirmed_bos"] = True

                awaiting_bearish_confirmation = False

        return df