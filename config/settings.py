class Settings:

    # -------------------------
    # Market
    # -------------------------

    SYMBOL = "SOLUSDT"

    TIMEFRAMES = {

        # Higher Timeframe
        # Determines overall market bias

        "macro": "240",

        # Intermediate Timeframe
        # Determines market structure

        "structure": "60",

        # Lower Timeframe
        # Used for entries

        "entry": "15",

    }
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
    # Confluence
    # -------------------------

    TREND_WEIGHT = 2

    BOS_WEIGHT = 3

    CHOCH_WEIGHT = 3

    LIQUIDITY_WEIGHT = 2

    FVG_WEIGHT = 2

    PREMIUM_DISCOUNT_WEIGHT = 1

    ORDER_BLOCK_WEIGHT = 2

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

    DEBUG_MODE = True

    # ----------------------------------------
    # Engine
    # ----------------------------------------

    MULTI_TIMEFRAME = False