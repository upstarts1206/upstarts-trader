class MarketState:

    def generate(self, market):

        state = {}

        # Trend
        if market["ema20"] > market["ema50"]:
            state["trend"] = "Bullish"
        else:
            state["trend"] = "Bearish"

        # Momentum
        if market["macd"] > 0:
            state["momentum"] = "Strong"
        else:
            state["momentum"] = "Weak"

        # RSI
        if market["rsi"] > 70:
            state["strength"] = "Overbought"

        elif market["rsi"] < 30:
            state["strength"] = "Oversold"

        else:
            state["strength"] = "Neutral"

        return state