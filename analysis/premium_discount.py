import pandas as pd


class PremiumDiscount:

    def detect(self, df: pd.DataFrame):

        df["equilibrium"] = None
        df["pd_zone"] = None

        latest_high = None
        latest_low = None

        for i in range(len(df)):

            if df.iloc[i]["swing_high"]:
                latest_high = df.iloc[i]["high"]

            if df.iloc[i]["swing_low"]:
                latest_low = df.iloc[i]["low"]

            if latest_high is None or latest_low is None:
                continue

            equilibrium = (latest_high + latest_low) / 2

            df.at[df.index[i], "equilibrium"] = equilibrium

            if df.iloc[i]["close"] < equilibrium:

                df.at[df.index[i], "pd_zone"] = "Discount"

            elif df.iloc[i]["close"] > equilibrium:

                df.at[df.index[i], "pd_zone"] = "Premium"

            else:

                df.at[df.index[i], "pd_zone"] = "Equilibrium"

        return df