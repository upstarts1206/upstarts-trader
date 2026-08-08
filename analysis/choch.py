import pandas as pd


class ChangeOfCharacter:

    def detect(self, df: pd.DataFrame):

        df["choch"] = False

        last_swing_low = None

        for i in range(len(df)):

            current = df.iloc[i]

            if current["swing_low"]:
                last_swing_low = current["low"]

            if (
                last_swing_low is not None
                and current["close"] < last_swing_low
            ):

                df.at[df.index[i], "choch"] = True

                last_swing_low = None

        return df