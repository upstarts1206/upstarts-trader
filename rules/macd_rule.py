class MACDRule:

    def check(self, market):

        if market["macd"] > 0:

            return True, "✅ MACD is bullish"

        return False, "❌ MACD is bearish"