import requests
import pandas as pd


class Market:
    """
    Handles communication with the Bybit Market API.
    """

    BASE_URL = "https://api.bybit.com/v5/market"

    def get_ticker(self, symbol: str) -> dict:
        """
        Returns the latest ticker information for a symbol.

        Example:
            BTCUSDT
            ETHUSDT
            SOLUSDT
        """

        url = f"{self.BASE_URL}/tickers"

        params = {
            "category": "linear",
            "symbol": symbol
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        return data["result"]["list"][0]
    
    def get_candles(self, symbol: str, interval: str = "60", limit: int = 200):
        """
        Downloads historical OHLCV candles from Bybit.

        interval examples:
            1   = 1 minute
            5   = 5 minutes
            15  = 15 minutes
            60  = 1 hour
            240 = 4 hours
            D   = Daily
        """

        url = f"{self.BASE_URL}/kline"

        params = {
            "category": "linear",
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()["result"]["list"]

        columns = [
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "turnover"
        ]

        df = pd.DataFrame(data, columns=columns)

        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
            "volume",
            "turnover"
        ]

        df[numeric_columns] = df[numeric_columns].astype(float)

        df["timestamp"] = pd.to_datetime(
            df["timestamp"].astype("int64"),
            unit="ms"
        )

        df = df.sort_values("timestamp")

        return df   