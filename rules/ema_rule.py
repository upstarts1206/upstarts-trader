class EMARule:

    def check(self, context):

        market = context.summary
        direction = context.bias["direction"]

        if direction == "Bullish":

            if market["ema20"] > market["ema50"]:

                return True, "✅ EMA supports Bullish bias"

            return False, "❌ EMA rejects Bullish bias"

        elif direction == "Bearish":

            if market["ema20"] < market["ema50"]:

                return True, "✅ EMA supports Bearish bias"

            return False, "❌ EMA rejects Bearish bias"

        return False, "⚪ Neutral Bias"