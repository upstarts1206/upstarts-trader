class Settings:

    # -------------------------
    # Market
    # -------------------------

    SYMBOL = "SOLUSDT"

    TIMEFRAMES = [
        "15",
        "60",
        "240"
    ]

    # -------------------------
    # Indicators
    # -------------------------

    EMA_FAST = 20
    EMA_SLOW = 50

    RSI_PERIOD = 14

    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9

    # -------------------------
    # Structure
    # -------------------------

    SWING_LOOKBACK = 2
    BOS_CONFIRMATION = "immediate"

    # -------------------------
    # Risk
    # -------------------------

    DEFAULT_RISK = 0.01

    MIN_RISK_REWARD = 2.0

    # -------------------------
    # Scanner
    # -------------------------

    WATCHLIST_NAME = "Default"

    MIN_DECISION = "BUY"

    SCAN_INTERVAL_MINUTES = 15

    # -------------------------
    # Ranking
    # -------------------------

    CONFIDENCE_WEIGHT = 1.0

    CONFLUENCE_WEIGHT = 10

    RISK_REWARD_WEIGHT = 10

    # -------------------------
    # Display
    # -------------------------

    SHOW_SCAN_SUMMARY = True

    SHOW_TOP_TRADE = True