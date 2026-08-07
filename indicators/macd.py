import pandas as pd


class MACD:

    def calculate(
        self,
        df: pd.DataFrame,
        fast_period: int = 12,
        slow_period: int = 26,
        signal_period: int = 9
    ) -> pd.DataFrame:

        ema_fast = df["close"].ewm(
            span=fast_period,
            adjust=False
        ).mean()

        ema_slow = df["close"].ewm(
            span=slow_period,
            adjust=False
        ).mean()

        df["MACD"] = ema_fast - ema_slow

        df["MACD_SIGNAL"] = (
            df["MACD"]
            .ewm(
                span=signal_period,
                adjust=False
            )
            .mean()
        )

        df["MACD_HISTOGRAM"] = (
            df["MACD"] - df["MACD_SIGNAL"]
        )

        return df