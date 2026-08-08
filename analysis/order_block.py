import pandas as pd


class OrderBlock:

    def detect(self, df: pd.DataFrame):

        df["order_block"] = None

        for i in range(1, len(df)):

            current = df.iloc[i]
            previous = df.iloc[i - 1]

            # Bullish Order Block
            if (
                current["bos"] == True
                and previous["close"] < previous["open"]
            ):
                df.at[df.index[i - 1], "order_block"] = "Bullish"

            # Bearish Order Block
            if (
                current["choch"] == True
                and previous["close"] > previous["open"]
            ):
                df.at[df.index[i - 1], "order_block"] = "Bearish"

        return df