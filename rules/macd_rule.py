class MACDRule:

    def check(self, context):

        market = context.summary

        if market["macd"] > 0:

            return True, "✅ MACD is bullish"

        return False, "❌ MACD is bearish"