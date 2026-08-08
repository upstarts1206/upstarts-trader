class Settings:

    # Market

    SYMBOL = "SOLUSDT"

    TIMEFRAMES = [
        "15",
        "60",
        "240"
    ]

    # Indicators

    EMA_FAST = 20
    EMA_SLOW = 50

    RSI_PERIOD = 14

    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9

    # Structure

    SWING_LOOKBACK = 2

    BOS_CONFIRMATION = "immediate"

    # Risk

    DEFAULT_RISK = 0.01