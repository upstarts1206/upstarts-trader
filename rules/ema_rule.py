class EMARule:

    def check(self, market):

        if market["ema20"] > market["ema50"]:

            return True, "✅ EMA20 is above EMA50"

        return False, "❌ EMA20 is below EMA50"