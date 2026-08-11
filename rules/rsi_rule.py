class RSIRule:

    def check(self, context):

        market = context.summary
        direction = context.bias["direction"]

        rsi = market["rsi"]

        if direction == "Bullish":

            if 40 <= rsi <= 70:

                return True, "✅ RSI supports Bullish bias"

            return False, "❌ RSI rejects Bullish bias"

        elif direction == "Bearish":

            if 30 <= rsi <= 60:

                return True, "✅ RSI supports Bearish bias"

            return False, "❌ RSI rejects Bearish bias"

        return False, "⚪ Neutral Bias"