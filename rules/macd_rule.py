class MACDRule:

    def check(self, context):

        market = context.summary
        bias = context.bias["direction"]

        if bias == "BUY":

            if market["macd"] > 0:

                return True, "✅ MACD supports BUY bias"

            return False, "❌ MACD rejects BUY bias"

        elif bias == "SELL":

            if market["macd"] < 0:

                return True, "✅ MACD supports SELL bias"

            return False, "❌ MACD rejects SELL bias"

        return False, "⚪ Neutral Bias"