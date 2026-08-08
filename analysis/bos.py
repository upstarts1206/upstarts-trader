import pandas as pd


class BreakOfStructure:

    def detect(self, df: pd.DataFrame):

        df["bos"] = False
        df["confirmed_bos"] = False

        last_swing_high = None
        bos_active = False

        for i in range(len(df)):

            current = df.iloc[i]

            # Remember latest swing high
            if current["swing_high"]:
                last_swing_high = current["high"]

            # Immediate BOS
            if (
                last_swing_high is not None
                and current["close"] > last_swing_high
            ):
                df.at[df.index[i], "bos"] = True

                bos_active = True

                last_swing_high = None

            # Confirmation
            if bos_active and current["swing_high"]:

                df.at[df.index[i], "confirmed_bos"] = True

                bos_active = False

        return df