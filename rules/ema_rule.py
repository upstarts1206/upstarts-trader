class EMARule:

    def check(self, context):

        market = context.summary
        bias = context.bias["direction"]

        if bias == "BUY":

            if market["ema20"] > market["ema50"]:

                return True, "✅ EMA supports BUY bias"

            return False, "❌ EMA rejects BUY bias"

        elif bias == "SELL":

            if market["ema20"] < market["ema50"]:

                return True, "✅ EMA supports SELL bias"

            return False, "❌ EMA rejects SELL bias"

        return False, "⚪ Neutral Bias"