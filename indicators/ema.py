import pandas as pd


class EMA:
    """
    Calculates an Exponential Moving Average (EMA)
    and appends it to a DataFrame.
    """

    def calculate(self, df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
        """
        Adds an EMA column to the DataFrame.

        Parameters:
            df (pd.DataFrame): Market data
            period (int): EMA period

        Returns:
            pd.DataFrame: Original DataFrame with EMA column added
        """

        df[f"EMA_{period}"] = df["close"].ewm(
            span=period,
            adjust=False
        ).mean()

        return df