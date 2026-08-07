import pandas as pd


class RSI:
    """
    Calculates the Relative Strength Index (RSI)
    and appends it to a DataFrame.
    """

    def calculate(self, df: pd.DataFrame, period: int = 14) -> pd.DataFrame:

        delta = df["close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        df[f"RSI_{period}"] = 100 - (100 / (1 + rs))

        return df
