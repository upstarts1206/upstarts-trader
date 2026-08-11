class EMARule:

    def check(self, context):

        market = context.summary

        if market["ema20"] > market["ema50"]:

            return True, "✅ EMA20 is above EMA50"

        return False, "❌ EMA20 is below EMA50"