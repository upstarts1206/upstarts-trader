class Summary:

    def generate(self, latest):

        trend = "Bullish"

        if latest["EMA_20"] < latest["EMA_50"]:
            trend = "Bearish"

        return {
            "price": float(latest["close"]),
            "ema20": float(latest["EMA_20"]),
            "ema50": float(latest["EMA_50"]),
            "rsi": float(latest["RSI_14"]),
            "macd": float(latest["MACD"]),
            "trend": trend,
            "pd_zone": latest["pd_zone"],
            "equilibrium": latest["equilibrium"],
        }

    def display(self, latest):

        market = self.generate(latest)

        print()
        print("==============================")
        print("     MARKET SUMMARY")
        print("==============================")
        print(f"Trend : {market['trend']}")
        print(f"Price : {market['price']:.2f}")
        print(f"EMA20 : {market['ema20']:.2f}")
        print(f"EMA50 : {market['ema50']:.2f}")
        print(f"RSI   : {market['rsi']:.2f}")
        print(f"MACD  : {market['macd']:.4f}")
        print("==============================")