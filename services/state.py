class MarketState:

    def generate(self, market_summary):

        state = {}

        # Trend
        if market_summary["ema20"] > market_summary["ema50"]:
            state["trend"] = "Bullish"
        else:
            state["trend"] = "Bearish"

        # Momentum
        if market_summary["macd"] > 0:
            state["momentum"] = "Strong"
        else:
            state["momentum"] = "Weak"

        # RSI
        if market_summary["rsi"] > 70:
            state["strength"] = "Overbought"

        elif market_summary["rsi"] < 30:
            state["strength"] = "Oversold"

        else:
            state["strength"] = "Neutral"

        return state