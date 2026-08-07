class RSIRule:

    def check(self, market):

        if 40 <= market["rsi"] <= 70:

            return True, "✅ RSI is healthy"

        return False, "❌ RSI is outside the healthy range"