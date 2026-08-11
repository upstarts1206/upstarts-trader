class MACDRule:

    def check(self, context):

        market = context.summary
        direction = context.bias["direction"]

        if direction == "Bullish":

            if market["macd"] > 0:

                return True, "✅ MACD supports Bullish bias"

            return False, "❌ MACD rejects Bullish bias"

        elif direction == "Bearish":

            if market["macd"] < 0:

                return True, "✅ MACD supports Bearish bias"

            return False, "❌ MACD rejects Bearish bias"

        return False, "⚪ Neutral Bias"